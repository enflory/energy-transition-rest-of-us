#!/usr/bin/env python3
"""
Scrape podcast episode pages and save their transcripts.

Usage:
    python scripts/scrape.py <podcast> <episode-url> [<episode-url> ...]
    python scripts/scrape.py <podcast> --all          # every episode in sitemap
    python scripts/scrape.py <podcast> --all --force  # re-fetch existing too

  <podcast> is a directory name under podcasts/, e.g. "catalyst".
  Its podcast.json supplies where the episodes are listed, how the page
  stores its title and date, which region of the page holds the content,
  the known publisher misspellings to correct, and the boilerplate to
  strip. Nothing show-specific lives in this file.

A show is not always published by the podcast's own network. Critical
Capital is a Latitude Media show whose transcripts are published by Crux,
its co-producer, on an entirely different CMS. Both are read by this one
script because every difference between them is a line of configuration.

Writes to:
    podcasts/<podcast>/episodes/<YYYY-MM-DD>-<slug>/transcript.md
    podcasts/<podcast>/manifest.csv   (one row per episode seen)

Transcripts are stored as published, with two deliberate exceptions, both
recorded in each file's frontmatter:
  1. HTML markup and entities are normalized to plain text.
  2. Known publisher transcription errors are corrected, per the
     "corrections" list in podcast.json. Everything else, including guest
     wording and paragraph breaks, is left exactly as published.
Sponsor reads, credits and the standard footer bio are separated out of the
dialogue rather than deleted.
"""

import csv
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PODCASTS = os.path.join(ROOT, "podcasts")

# Set by load_config() once the podcast is known. Module-level because the
# rendering and manifest helpers below are shared across shows.
CFG = {}
OUT_ROOT = ""
MANIFEST = ""
SITEMAPS = []
CORRECTIONS = []
BOILERPLATE = []
NON_SPEAKERS = set()
DELAY_SECONDS = 1.0
TITLE_SUFFIX = None
PUBLISHED = []
CONTENT_START = None
CONTENT_END = None

# The publisher's own default: an ISO timestamp in a WordPress meta tag. Shows
# hosted elsewhere override this with "published" in podcast.json.
DEFAULT_PUBLISHED = [{
    "pattern": r'<meta property="article:published_time" content="([^"]+)"',
    "format": "iso",
}]


def load_config(podcast):
    """Read podcasts/<podcast>/podcast.json and populate module state."""
    global CFG, OUT_ROOT, MANIFEST, SITEMAPS, CORRECTIONS, BOILERPLATE
    global NON_SPEAKERS, DELAY_SECONDS, TITLE_SUFFIX, PUBLISHED
    global CONTENT_START, CONTENT_END
    path = os.path.join(PODCASTS, podcast, "podcast.json")
    if not os.path.isfile(path):
        sys.exit("no config at %s (see docs/ADDING-A-PODCAST.md)" % path)
    with open(path, encoding="utf-8") as f:
        CFG = json.load(f)
    OUT_ROOT = os.path.join(PODCASTS, podcast, "episodes")
    MANIFEST = os.path.join(PODCASTS, podcast, "manifest.csv")
    SITEMAPS = CFG.get("sitemaps", [])
    DELAY_SECONDS = CFG.get("delay_seconds", 1.0)
    NON_SPEAKERS = {s.lower() for s in CFG.get("non_speakers", [])}
    CORRECTIONS = [(re.compile(c["pattern"]), c["replacement"], c["note"])
                   for c in CFG.get("corrections", [])]
    BOILERPLATE = [re.compile(p, re.I) for p in CFG.get("boilerplate", [])]
    TITLE_SUFFIX = (re.compile(CFG["title_suffix"])
                    if CFG.get("title_suffix") else None)
    PUBLISHED = [(re.compile(p["pattern"], re.S), p.get("format", "iso"))
                 for p in (CFG.get("published") or DEFAULT_PUBLISHED)]
    CONTENT_START = (re.compile(CFG["content_start"], re.S)
                     if CFG.get("content_start") else None)
    CONTENT_END = (re.compile(CFG["content_end"], re.S)
                   if CFG.get("content_end") else None)
    return CFG

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

# A transcript paragraph opens with a speaker label, e.g. "Jane Doe:".
# This shape is shared across shows; everything else show-specific is in
# podcast.json.
SPEAKER_RE = re.compile(r"^([A-Z][A-Za-z.\-']*(?: [A-Z][A-Za-z.\-']*){0,3}):\s")

# Zero-width characters. Some CMSes emit these ahead of a speaker label, which
# makes the paragraph invisibly fail SPEAKER_RE and drop out of the dialogue.
# They carry no meaning, so removing them is normalization, not editing.
ZERO_WIDTH_RE = re.compile("[​‌‍⁠﻿]")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def clean(fragment):
    """HTML fragment -> plain text."""
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = html.unescape(fragment)
    fragment = fragment.replace(" ", " ")
    fragment = ZERO_WIDTH_RE.sub("", fragment)
    fragment = re.sub(r"[ \t]+", " ", fragment)
    return fragment.strip()


def apply_corrections(text, tally):
    """Fix known publisher transcription errors, counting each change."""
    for pattern, replacement, note in CORRECTIONS:
        text, n = pattern.subn(replacement, text)
        if n:
            tally[note] = tally.get(note, 0) + n
    return text


def is_boilerplate(p):
    return any(pat.search(p) for pat in BOILERPLATE)


def is_dialogue(p):
    m = SPEAKER_RE.match(p)
    return bool(m) and m.group(1).lower() not in NON_SPEAKERS


def meta(pattern, page, group=1):
    m = re.search(pattern, page)
    return m.group(group) if m else ""


def topic_bullets(page):
    """The 'Shayle and X discuss:' list that follows the episode blurb."""
    anchor = re.search(r"discuss:\s*</p>", page, re.I)
    if not anchor:
        return []
    window = page[anchor.end():anchor.end() + 4000]
    ul = re.search(r"<ul[^>]*>(.*?)</ul>", window, re.S)
    if not ul:
        return []
    items = [clean(li) for li in
             re.findall(r"<li[^>]*>(.*?)</li>", ul.group(1), re.S)]
    return [i for i in items if i]


def sitemap_urls():
    """Episode URLs for this show listed in the publisher sitemaps."""
    found = []
    needle = CFG.get("url_filter", "")
    for sm in SITEMAPS:
        try:
            xml = fetch(sm)
        except Exception as exc:  # noqa: BLE001
            print(f"WARN   could not read {sm}: {exc}")
            continue
        for loc in re.findall(r"<loc>([^<]+)</loc>", xml):
            if needle in loc:
                found.append(loc)
    return found


def index_urls():
    """Episode URLs harvested by walking the show's own episode listing.

    A sitemap can lag the site. Crux's was missing the newest Critical Capital
    episode on 2026-09-18, which is the one case that matters, because the
    newest episode is the whole point of checking. Walking the listing pages
    costs a couple of requests and does not have that failure mode, so both
    sources are read and the results unioned.
    """
    pages = CFG.get("index_pages") or []
    if not pages:
        return []
    if not CFG.get("index_link_pattern"):
        sys.exit("index_pages is set but index_link_pattern is not; the "
                 "scraper cannot tell which links on the page are episodes "
                 "(see docs/ADDING-A-PODCAST.md)")
    link_re = re.compile(CFG["index_link_pattern"])
    next_re = (re.compile(CFG["index_next_pattern"])
               if CFG.get("index_next_pattern") else None)
    found, visited = [], set()
    for start in pages:
        url = start
        for _ in range(50):  # pagination guard; no show has 50 index pages
            if not url or url in visited:
                break
            visited.add(url)
            try:
                page = fetch(url)
            except Exception as exc:  # noqa: BLE001
                print(f"WARN   could not read {url}: {exc}")
                break
            for href in link_re.findall(page):
                found.append(urllib.parse.urljoin(url, html.unescape(href)))
            nxt = next_re.search(page) if next_re else None
            url = (urllib.parse.urljoin(url, html.unescape(nxt.group(1)))
                   if nxt else None)
            time.sleep(DELAY_SECONDS)
    needle = CFG.get("url_filter", "")
    return [u for u in found if needle in u]


def episode_urls():
    """Every known episode URL for this show, from every configured source."""
    return sorted(set(sitemap_urls()) | set(index_urls()))


def published_date(page):
    """The episode's publication date, however this publisher stores it."""
    for pattern, fmt in PUBLISHED:
        m = pattern.search(page)
        if not m:
            continue
        raw = clean(m.group(1))
        if fmt == "iso":
            return raw
        try:
            return datetime.strptime(raw, fmt).strftime("%Y-%m-%d")
        except ValueError:
            print(f"WARN   date {raw!r} does not match format {fmt!r}")
    return ""


def content_region(page):
    """Narrow the page to the region that holds the episode's own content.

    Without this the parser sees the whole document, and a template that drops
    a stray capitalized label into the navigation or the footer can start or
    extend the transcript. Shows whose pages need no narrowing leave
    content_start and content_end unset and get the whole document.
    """
    if CONTENT_START:
        m = CONTENT_START.search(page)
        if m:
            page = page[m.end():]
        else:
            print("WARN   content_start did not match; using the whole page")
    if CONTENT_END:
        m = CONTENT_END.search(page)
        if m:
            page = page[:m.start()]
        else:
            print("WARN   content_end did not match; using the whole page")
    return page


def parse(page, url):
    tally = {}
    title = clean(meta(r"<title>(.*?)</title>", page)) or "Untitled"
    if TITLE_SUFFIX:
        title = TITLE_SUFFIX.sub("", title)

    ep = {
        "title": apply_corrections(title, tally),
        "url": url,
        "published": published_date(page),
        "modified": meta(
            r'<meta property="article:modified_time" content="([^"]+)"', page),
        "megaphone_id": meta(
            r"playlist\.megaphone\.fm\?e=([A-Za-z0-9]+)", page),
        "keywords": [],
    }

    for blob in re.findall(
            r'<script type="application/ld\+json"[^>]*>(.*?)</script>',
            page, re.S):
        try:
            data = json.loads(blob)
        except json.JSONDecodeError:
            continue
        for node in data.get("@graph", [data]):
            if node.get("@type") == "NewsArticle":
                ep["keywords"] = node.get("keywords") or ep["keywords"]

    body = content_region(page)
    paras = [clean(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S)]
    paras = [p for p in paras if p]

    # Drop sponsor reads, credits and ad markers first, so a boilerplate block
    # that happens to look like a speaker label cannot start the transcript.
    content = [p for p in paras if not is_boilerplate(p)]

    start = next((i for i, p in enumerate(content) if is_dialogue(p)), None)
    if start is None:
        return None  # page has no published transcript

    ep["show_notes"] = [apply_corrections(p, tally) for p in content[:start]]
    ep["topics"] = [apply_corrections(t, tally) for t in topic_bullets(page)]
    ep["transcript"] = [apply_corrections(p, tally) for p in content[start:]]
    ep["transcript_word_count"] = sum(len(p.split()) for p in ep["transcript"])
    ep["speakers"] = sorted({SPEAKER_RE.match(p).group(1)
                             for p in ep["transcript"] if is_dialogue(p)})
    ep["corrections"] = tally
    return ep


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:90].rstrip("-")


def folder_name(ep):
    date = (ep["published"] or "")[:10] or "undated"
    return f"{date}-{slugify(ep['title'])}"


def q(v):
    # JSON string escaping is valid YAML double-quoted-scalar escaping.
    return json.dumps(str(v), ensure_ascii=False)


def render(ep):
    out = ["---"]
    for key in ("title", "url", "published", "modified", "megaphone_id"):
        out.append(f"{key}: {q(ep[key])}")
    out.append("keywords: [" + ", ".join(q(k) for k in ep["keywords"]) + "]")
    out.append("speakers: [" + ", ".join(q(s) for s in ep["speakers"]) + "]")
    out.append(f"transcript_word_count: {ep['transcript_word_count']}")
    out.append("scraped_at: " + q(
        datetime.now().astimezone().isoformat(timespec="seconds")))
    out.append("source: " + q("%s - %s" % (CFG.get("publisher", ""),
                                            CFG.get("display_name", ""))))
    out.append("podcast: " + q(CFG.get("name", "")))
    if ep["corrections"]:
        out.append("corrections:")
        for note, n in sorted(ep["corrections"].items()):
            out.append(f"  - {q(note)}: {n}")
    else:
        out.append("corrections: []")
    out.append("---")
    out += ["", f"# {ep['title']}", ""]

    if ep["show_notes"]:
        out += ["## Show notes", ""]
        for n in ep["show_notes"]:
            out += [n, ""]
    if ep["topics"]:
        out += ["### Topics covered", ""]
        out += [f"- {t}" for t in ep["topics"]]
        out.append("")

    out += ["## Transcript", ""]
    for p in ep["transcript"]:
        m = SPEAKER_RE.match(p) if is_dialogue(p) else None
        out.append(f"**{m.group(1)}:** {p[m.end():].strip()}" if m else p)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def save(ep):
    d = os.path.join(OUT_ROOT, folder_name(ep))
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "transcript.md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(render(ep))
    return path


def saved_urls():
    """URLs already present in the archive, read once up front."""
    found = set()
    if not os.path.isdir(OUT_ROOT):
        return found
    for name in os.listdir(OUT_ROOT):
        p = os.path.join(OUT_ROOT, name, "transcript.md")
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as f:
                head = f.read(2000)
            m = re.search(r'^url: "([^"]+)"', head, re.M)
            if m:
                found.add(m.group(1))
    return found


def rows_from_disk():
    """Reconstruct rows for saved episodes by reading the archive itself."""
    found = {}
    if not os.path.isdir(OUT_ROOT):
        return found
    for name in sorted(os.listdir(OUT_ROOT)):
        p = os.path.join(OUT_ROOT, name, "transcript.md")
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8") as f:
            head = f.read(2000)

        def field(key):
            m = re.search(r'^%s: "([^"]*)"' % key, head, re.M)
            return m.group(1) if m else ""

        wc = re.search(r"^transcript_word_count: (\d+)", head, re.M)
        url = field("url")
        if url:
            found[url] = [field("published")[:10], field("title"), "saved",
                          wc.group(1) if wc else "", name, url]
    return found


def write_manifest(rows):
    """Merge this run into the manifest rather than replacing it.

    A partial run must not drop episodes it did not touch. Precedence is
    previous manifest, then this run, then the archive on disk, which is
    authoritative for anything actually saved.
    """
    os.makedirs(OUT_ROOT, exist_ok=True)
    merged = {}
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, encoding="utf-8", newline="") as f:
            for r in csv.reader(f):
                if len(r) == 6 and r[0] != "published":
                    merged[r[5]] = r
    for r in rows:
        merged[r[5]] = r
    merged.update(rows_from_disk())

    # csv.writer emits CRLF by default, which .gitattributes then normalizes
    # to LF on commit. The net effect is a manifest that shows as modified
    # after every fetch even when not one field changed, which buries a real
    # change in noise. Write LF directly.
    with open(MANIFEST, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["published", "title", "status", "words", "folder", "url"])
        for r in sorted(merged.values(), key=lambda r: (r[0] or "9999", r[1])):
            w.writerow(r)


def main(argv):
    if not argv or argv[0].startswith("--"):
        sys.exit(__doc__)
    podcast = argv[0]
    load_config(podcast)
    argv = argv[1:]

    force = "--force" in argv
    args = [a for a in argv if not a.startswith("--")]
    urls = episode_urls() if "--all" in argv else args
    if not urls:
        sys.exit(__doc__)
    print(f"{CFG.get('display_name', podcast)}")

    print(f"{len(urls)} episode URLs to process\n")
    rows, counts = [], {"saved": 0, "skipped": 0, "no transcript": 0,
                        "error": 0}
    have = set() if force else saved_urls()

    for i, url in enumerate(urls, 1):
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        if url in have:
            counts["skipped"] += 1
            rows.append(["", slug, "already saved", "", "", url])
            print(f"[{i:>3}/{len(urls)}] SKIP   already saved  {slug[:60]}")
            continue
        try:
            page = fetch(url)
            ep = parse(page, url)
        except Exception as exc:  # noqa: BLE001
            counts["error"] += 1
            rows.append(["", slug, f"error: {type(exc).__name__}", "", "", url])
            print(f"[{i:>3}/{len(urls)}] ERROR  {type(exc).__name__}: {exc}")
            time.sleep(DELAY_SECONDS)
            continue

        if ep is None:
            date = published_date(page)[:10]
            counts["no transcript"] += 1
            rows.append([date, slug, "no transcript", "", "", url])
            print(f"[{i:>3}/{len(urls)}] NONE   no transcript  {slug[:60]}")
        else:
            save(ep)
            counts["saved"] += 1
            rows.append([ep["published"][:10], ep["title"], "saved",
                         ep["transcript_word_count"], folder_name(ep), url])
            print(f"[{i:>3}/{len(urls)}] OK     "
                  f"{ep['transcript_word_count']:>6,}w  {folder_name(ep)[:70]}")
        time.sleep(DELAY_SECONDS)

    write_manifest(rows)
    print("\n" + "-" * 60)
    for k, v in counts.items():
        print(f"  {k:<16} {v}")
    print(f"  manifest         {os.path.relpath(MANIFEST, ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
