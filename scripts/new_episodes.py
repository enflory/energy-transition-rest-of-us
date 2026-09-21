#!/usr/bin/env python3
"""
Find items that still need work, and print the brief for writing their notes.

Usage:
    python scripts/new_episodes.py                   # every source
    python scripts/new_episodes.py catalyst          # one source
    python scripts/new_episodes.py catalyst --brief  # print the agent brief too

This is the "what do I do now?" command. It answers three questions:

  1. Which published items have we never scraped?
  2. Which saved documents have no note yet?
  3. What exactly do I paste into Claude Code to get those notes written?

It works for both content types. The wording of every report and of the brief
itself comes from the source's content type, so a run against a newsletter
talks about posts and essays rather than episodes and transcripts, and points
the writer at the half of the spec that applies.

It only reads. It never scrapes and never writes a note, so it is safe to run
at any time and costs nothing but a sitemap fetch.
"""

import os
import re
import sys

import archive
import scrape

ROOT = archive.ROOT


def published_urls(source):
    """Every item URL for this source, from every configured source of URLs.

    This delegates to the scraper rather than reimplementing discovery. An
    earlier version read only the sitemaps, which quietly disagreed with what
    a fetch would do: a source declaring `index_pages` got its freshness check
    during `fetch` and not during the status check, so `run.py` could report
    "nothing new to scrape" for a just-published item and then scrape it on
    the very next fetch. Both now ask the same question.
    """
    scrape.load_config(source)
    return scrape.episode_urls()


def saved_urls(items_dir, source_file):
    """URLs already scraped, read from each document's frontmatter."""
    urls = {}
    if not os.path.isdir(items_dir):
        return urls
    for folder in sorted(os.listdir(items_dir)):
        path = os.path.join(items_dir, folder, source_file)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as f:
            head = f.read(2000)
        m = re.search(r'^url:\s*"([^"]+)"', head, re.M)
        if m:
            urls[m.group(1)] = folder
    return urls


def manifest_status(show):
    """url -> status, from the manifest of every item ever looked at.

    This is what separates "we have never tried this URL" from "we tried it
    and the publisher ships no document for it." Without the distinction,
    pages that will never carry one show up as pending work forever.
    """
    import csv
    path = archive.manifest(show)
    status = {}
    if not os.path.isfile(path):
        return status
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if len(row) == 6 and row[0] != "published":
                status[row[5]] = row[2]
    return status


def report(show):
    cfg = archive.load(show)
    kind = archive.kind(cfg)
    items_dir = archive.items_dir(show, cfg)
    doc = kind["document"]

    print(f"\n=== {cfg.get('display_name', show)} ({show}) ===")

    live = published_urls(show)
    have = saved_urls(items_dir, kind["source_file"])
    seen = manifest_status(show)
    missing = [u for u in live
               if u not in have and seen.get(u) == "no " + doc]
    unscraped = [u for u in live if u not in have and u not in missing]

    folders = archive.item_folders(show, cfg)
    noteless = [d for d in folders
                if os.path.isfile(
                    os.path.join(items_dir, d, kind["source_file"]))
                and not os.path.isfile(os.path.join(items_dir, d, "note.md"))]

    print(f"  published on site    {len(live)}")
    print(f"  {kind['documents'] + ' on disk':<20} {len(have)}")
    print(f"  notes written        {len(have) - len(noteless)}")

    if missing:
        print(f"  no {doc} published {len(missing)} "
              "(checked previously; not pending work)")

    if unscraped:
        print(f"\n  {len(unscraped)} {kind['item']}(s) not yet scraped:")
        for u in unscraped:
            print(f"    {u}")
        print(f"\n  -> python run.py fetch {show}")
    else:
        print("\n  nothing new to scrape.")
        if missing:
            print(f"     (to retry the no-{doc} pages in case the "
                  "publisher has since added one:")
            print(f"      python run.py refetch {show})")

    if noteless:
        print(f"\n  {len(noteless)} {doc}(s) with no note:")
        for d in noteless:
            print(f"    {d}")
    elif not unscraped:
        print(f"  every {doc} has a note. Nothing to do.")

    return show, noteless


BRIEF = """
--------------------------------------------------------------------------
Paste the block below into Claude Code to write the missing notes.
Use a strong model. One agent per three {items} works well; for a single
{item} just run it in the main session.
--------------------------------------------------------------------------

You are writing {item} notes for the {display} archive in this repository.

Procedure, in order:

1. Read `docs/NOTE-SPEC.md` in full. It governs everything you write.
   Its shared rules apply to every source. Read the section called
   "{section}" twice; it is the half that applies here.
2. Read `sources/{show}/SOURCE-PROFILE.md` in full. It has this source's
   disclosure norms, {document} quirks, and reference notes.
3. Read at least two reference notes named in that profile, including the one
   it calls the benchmark.
4. For each {item} below, read its document IN FULL{skim}, then write its
   note per the spec:
     read  sources/{show}/{items_dir}/<folder>/{source_file}
     write sources/{show}/{items_dir}/<folder>/note.md
5. Run `python scripts/validate_notes.py {show} <folder> ...` and fix every
   ERROR. The word-count warning is advisory and its text explains when to
   leave it standing.

{Items}:
{episodes}

Hard constraints:
- Create or modify ONLY those `note.md` files. Never touch `{source_file}`,
  `manifest.csv`, `source.json`, the spec, the profile, anything in
  `scripts/`, or any other {item}'s files.
- Single-{item} scope: no cross-{item} references, no hindsight, no outside
  knowledge used to correct or update a claim.
- Run verification check 3 (attribution) deliberately on each note.
{attribution}

Report back, concisely: for each {item} the central question and the answer in
one line each; any hard judgment calls; any garbled or ambiguous passages that
affected the note; and the final validator output verbatim.
--------------------------------------------------------------------------
"""

# The attribution check is the one place the two content types genuinely
# diverge, so each gets its own wording rather than a generic paraphrase that
# would be accurate for neither.
ATTRIBUTION = {
    "podcast": """  Title gravity, the host's framing, and your own compression. Where host
  and guest diverge, the guest governs. Silence is not agreement.""",
    "essay": """  Title gravity, quoted voice, and your own compression. A block quote in
  the document, rendered as a "> " line, is someone else's words and often
  the author's own earlier position that the surrounding prose goes on to
  revise. Never attribute a quoted passage to the author of the essay, and
  never let a revised earlier view stand as the current one.
- Lines reading `[FIGURE: ...]` mark a chart you cannot see. Where the
  argument rests on one, say in the note that the evidence is in a figure
  rather than inferring what it showed.""",
}

SKIM = {
    "podcast": ",\n   not skimming and not writing from the show-notes section",
    "essay": ",\n   not skimming and not writing from the subtitle alone",
}


def main(argv):
    want_brief = "--brief" in argv
    argv = [a for a in argv if not a.startswith("--")]

    known = archive.source_names()
    if not known:
        sys.exit("no sources configured under sources/")
    shows = argv or known
    for s in shows:
        if s not in known:
            sys.exit("unknown source %r; known: %s" % (s, ", ".join(known)))

    pending = []
    for show in shows:
        pending.append(report(show))

    if want_brief:
        for show, noteless in pending:
            if not noteless:
                continue
            cfg = archive.load(show)
            kind = archive.kind(cfg)
            content_type = cfg.get("content_type", archive.DEFAULT_TYPE)
            episodes = "\n".join("- `%s`" % d for d in noteless)
            print(BRIEF.format(
                show=show, episodes=episodes,
                display=cfg.get("display_name", show),
                item=kind["item"], items=kind["items"],
                Items=kind["items"].capitalize(),
                items_dir=kind["items_dir"],
                document=kind["document"],
                source_file=kind["source_file"],
                section=kind["spec_section"],
                skim=SKIM[content_type],
                attribution=ATTRIBUTION[content_type]))
    elif any(n for _, n in pending):
        print("\nNext: python run.py brief   (prints the note-writing brief)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
