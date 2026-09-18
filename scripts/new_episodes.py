#!/usr/bin/env python3
"""
Find episodes that still need work, and print the brief for writing their notes.

Usage:
    python scripts/new_episodes.py                 # every podcast
    python scripts/new_episodes.py catalyst        # one podcast
    python scripts/new_episodes.py catalyst --brief  # print the agent brief too

This is the "what do I do now?" command. It answers three questions:

  1. Which published episodes have we never scraped?
  2. Which scraped transcripts have no note yet?
  3. What exactly do I paste into Claude Code to get those notes written?

It only reads. It never scrapes and never writes a note, so it is safe to run
at any time and costs nothing but a sitemap fetch.
"""

import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PODCASTS = os.path.join(ROOT, "podcasts")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def podcast_names():
    if not os.path.isdir(PODCASTS):
        return []
    return sorted(d for d in os.listdir(PODCASTS)
                  if os.path.isfile(os.path.join(PODCASTS, d, "podcast.json")))


def published_urls(cfg):
    """Every episode URL for this show, from the publisher's sitemaps."""
    found, needle = [], cfg.get("url_filter", "")
    for sm in cfg.get("sitemaps", []):
        try:
            xml = fetch(sm)
        except Exception as exc:  # noqa: BLE001
            print(f"  WARN could not read {sm}: {exc}")
            continue
        found += [loc for loc in re.findall(r"<loc>([^<]+)</loc>", xml)
                  if needle in loc]
    return sorted(set(found))


def saved_urls(episodes_dir):
    """URLs already scraped, read from each transcript's frontmatter."""
    urls = {}
    if not os.path.isdir(episodes_dir):
        return urls
    for folder in sorted(os.listdir(episodes_dir)):
        path = os.path.join(episodes_dir, folder, "transcript.md")
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as f:
            head = f.read(2000)
        m = re.search(r'^url:\s*"([^"]+)"', head, re.M)
        if m:
            urls[m.group(1)] = folder
    return urls


def manifest_status(show):
    """url -> status, from the manifest of every episode ever looked at.

    This is what separates "we have never tried this URL" from "we tried it
    and the publisher ships no transcript for it." Without the distinction,
    pages that will never have a transcript show up as pending work forever.
    """
    import csv
    path = os.path.join(PODCASTS, show, "manifest.csv")
    status = {}
    if not os.path.isfile(path):
        return status
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if len(row) == 6 and row[0] != "published":
                status[row[5]] = row[2]
    return status


def report(show):
    cfg_path = os.path.join(PODCASTS, show, "podcast.json")
    with open(cfg_path, encoding="utf-8") as f:
        cfg = json.load(f)
    episodes_dir = os.path.join(PODCASTS, show, "episodes")

    print(f"\n=== {cfg.get('display_name', show)} ({show}) ===")

    live = published_urls(cfg)
    have = saved_urls(episodes_dir)
    seen = manifest_status(show)
    no_transcript = [u for u in live
                     if u not in have and seen.get(u) == "no transcript"]
    unscraped = [u for u in live if u not in have and u not in no_transcript]

    folders = sorted(os.listdir(episodes_dir)) if os.path.isdir(episodes_dir) else []
    noteless = [d for d in folders
                if os.path.isfile(os.path.join(episodes_dir, d, "transcript.md"))
                and not os.path.isfile(os.path.join(episodes_dir, d, "note.md"))]

    print(f"  published on site   {len(live)}")
    print(f"  transcripts on disk {len(have)}")
    print(f"  notes written       {len(have) - len(noteless)}")

    if no_transcript:
        print(f"  no transcript published {len(no_transcript)} "
              "(checked previously; not pending work)")

    if unscraped:
        print(f"\n  {len(unscraped)} episode(s) not yet scraped:")
        for u in unscraped:
            print(f"    {u}")
        print(f"\n  -> python run.py fetch {show}")
    else:
        print("\n  nothing new to scrape.")
        if no_transcript:
            print("     (to retry the no-transcript pages in case the "
                  "publisher has since added one:")
            print(f"      python run.py refetch {show})")

    if noteless:
        print(f"\n  {len(noteless)} transcript(s) with no note:")
        for d in noteless:
            print(f"    {d}")
    elif not unscraped:
        print("  every transcript has a note. Nothing to do.")

    return show, noteless


BRIEF = """
--------------------------------------------------------------------------
Paste the block below into Claude Code to write the missing notes.
Use a strong model. One agent per three episodes works well; for a single
episode just run it in the main session.
--------------------------------------------------------------------------

You are writing episode notes for the {display} archive in this repository.

Procedure, in order:

1. Read `docs/NOTE-SPEC.md` in full. It governs everything you write.
2. Read `podcasts/{show}/SHOW-PROFILE.md` in full. It has this show's
   disclosure norms, transcript quirks, and reference notes.
3. Read at least two reference notes named in that profile, including the one
   it calls the benchmark.
4. For each episode below: read
   `podcasts/{show}/episodes/<folder>/transcript.md` IN FULL (do not skim, and
   do not write from the show-notes section), then write
   `podcasts/{show}/episodes/<folder>/note.md` per the spec.
5. Run `python scripts/validate_notes.py {show} <folder> ...` and fix every
   ERROR. The word-count warning is advisory and its text explains when to
   leave it standing.

Episodes:
{episodes}

Hard constraints:
- Create or modify ONLY those `note.md` files. Never touch `transcript.md`,
  `manifest.csv`, `podcast.json`, the spec, the profile, anything in
  `scripts/`, or any other episode's files.
- Single-episode scope: no cross-episode references, no hindsight, no outside
  knowledge used to correct or update a claim.
- Run verification check 3 (attribution) deliberately on each note: title
  gravity, the host's framing, and your own compression. Where host and guest
  diverge, the guest governs. Silence is not agreement.

Report back, concisely: for each episode the central question and the answer in
one line each; any hard judgment calls; any garbled or ambiguous transcript
passages that affected the note; and the final validator output verbatim.
--------------------------------------------------------------------------
"""


def main(argv):
    want_brief = "--brief" in argv
    argv = [a for a in argv if not a.startswith("--")]

    known = podcast_names()
    if not known:
        sys.exit("no podcasts configured under podcasts/")
    shows = argv or known
    for s in shows:
        if s not in known:
            sys.exit("unknown podcast %r; known: %s" % (s, ", ".join(known)))

    pending = []
    for show in shows:
        pending.append(report(show))

    if want_brief:
        for show, noteless in pending:
            if not noteless:
                continue
            cfg_path = os.path.join(PODCASTS, show, "podcast.json")
            with open(cfg_path, encoding="utf-8") as f:
                cfg = json.load(f)
            episodes = "\n".join("- `%s`" % d for d in noteless)
            print(BRIEF.format(show=show, episodes=episodes,
                               display=cfg.get("display_name", show)))
    elif any(n for _, n in pending):
        print("\nNext: python run.py brief   (prints the note-writing brief)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
