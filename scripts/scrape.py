#!/usr/bin/env python3
"""
Scrape published items and save their source documents.

Usage:
    python scripts/scrape.py <source> <item-url> [<item-url> ...]
    python scripts/scrape.py <source> --all          # every item discovered
    python scripts/scrape.py <source> --all --force  # re-fetch existing too

  <source> is a directory name under sources/, e.g. "catalyst".
  Its source.json supplies where the items are listed, how the page stores
  its title and date, which region of the page holds the content, the known
  publisher misspellings to correct, and the boilerplate to strip. Nothing
  source-specific lives in this file.

Two content types, declared by "content_type" in the config:

  podcast (default)  A conversation. The document is a transcript, and it
                     is found by locating the first paragraph that opens
                     with a speaker label.
  essay              A written piece. There are no speaker labels, so the
                     document is the whole configured content region, and
                     the structure that carries the argument -- headings,
                     block quotes, lists and figures -- is preserved
                     rather than flattened into paragraphs.

A show is not always published by the podcast's own network. Critical
Capital is a Latitude Media show whose transcripts are published by Crux,
its co-producer, on an entirely different CMS. Both are read by this one
script because every difference between them is a line of configuration.

Writes to:
    sources/<source>/<episodes|posts>/<YYYY-MM-DD>-<slug>/<transcript|essay>.md
    sources/<source>/manifest.csv   (one row per item seen)

Documents are stored as published, with two deliberate exceptions, both
recorded in each file's frontmatter:
  1. HTML markup and entities are normalized to plain text or Markdown.
  2. Known publisher transcription errors are corrected, per the
     "corrections" list in the config. Everything else, including the
     author's or guest's wording and the paragraph breaks, is left exactly
     as published.
Sponsor reads, credits, subscribe widgets and the standard footer bio are
separated out of the content rather than deleted.
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

import archive

ROOT = archive.ROOT

# Set by load_config() once the source is known. Module-level because the
# rendering and manifest helpers below are shared across sources.
CFG = {}
KIND = {}
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
# hosted elsewhere override this with "published" in source.json.
DEFAULT_PUBLISHED = [{
    "pattern": r'<meta property="article:published_time" content="([^"]+)"',
    "format": "iso",
}]


def load_config(source):
    """Read sources/<source>/source.json and populate module state."""
    global CFG, KIND, OUT_ROOT, MANIFEST, SITEMAPS, CORRECTIONS, BOILERPLATE
    global NON_SPEAKERS, DELAY_SECONDS, TITLE_SUFFIX, PUBLISHED
    global CONTENT_START, CONTENT_END
    CFG = archive.load(source)
    KIND = archive.kind(CFG)
    OUT_ROOT = archive.items_dir(source, CFG)
    MANIFEST = archive.manifest(source)
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
# source.json.
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
                 "(see docs/ADDING-A-SOURCE.md)")
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
    """Dispatch to the reader for this source's content type."""
    return (parse_essay if KIND.get("items_dir") == "posts"
            else parse_transcript)(page, url)


def common_fields(page, url, tally):
    """The metadata every content type records, however it is published."""
    # The title tag is not always bare: Substack renders <title data-rh="true">,
    # and a pattern anchored on "<title>" silently titled every post "Untitled".
    title = clean(meta(r"<title[^>]*>(.*?)</title>", page)) or "Untitled"
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
            if node.get("@type") in ("NewsArticle", "Article", "BlogPosting"):
                ep["keywords"] = node.get("keywords") or ep["keywords"]

    return ep


def parse_transcript(page, url):
    """Read a conversation: dialogue located by its speaker labels."""
    tally = {}
    ep = common_fields(page, url, tally)

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
    ep["word_count"] = sum(len(p.split()) for p in ep["transcript"])
    ep["speakers"] = sorted({SPEAKER_RE.match(p).group(1)
                             for p in ep["transcript"] if is_dialogue(p)})
    ep["corrections"] = tally
    return ep


# Block-level elements that carry an essay's argument. Everything else in the
# content region is styling.
BLOCK_RE = re.compile(r"<(p|h[1-6]|li)\b[^>]*>(.*?)</\1>", re.S | re.I)
FIGURE_RE = re.compile(r"<figure\b[^>]*>(.*?)</figure>", re.S | re.I)
QUOTE_RE = re.compile(r"<blockquote\b[^>]*>(.*?)</blockquote>", re.S | re.I)

# Substack proxies images through its CDN, wrapping the original URL as an
# encoded path segment. The original is shorter and outlives the proxy.
CDN_RE = re.compile(r"/(https%3A%2F%2F[^\"'\s]+)")


def figure_parts(inner):
    """The caption and image URL of one <figure>, either of which may be ''."""
    caption = clean(meta(r"<figcaption[^>]*>(.*?)</figcaption>", inner))
    if not caption:
        caption = clean(meta(r"<img[^>]*\salt=\"([^\"]*)\"", inner))
    url = (meta(r"<a[^>]*\shref=\"(https?://[^\"]+)\"", inner)
           or meta(r"<img[^>]*\ssrc=\"(https?://[^\"]+)\"", inner))
    m = CDN_RE.search(url)
    if m:
        url = urllib.parse.unquote(m.group(1))
    return caption, url


def spans(pattern, segment):
    return [(m.start(), m.end()) for m in pattern.finditer(segment)]


def inside(pos, ranges):
    return any(a <= pos < b for a, b in ranges)


def blocks(segment):
    """The content region as ordered blocks, keeping the structure intact.

    An essay argues through its structure. A block quote is someone else's
    words, a heading marks where the argument turns, and a figure is often
    the evidence for the sentence before it. Flattening all of that into a
    list of paragraphs, which is all a transcript needs, would hand the
    note-writer an essay whose quotations read as the author's own claims.
    """
    figures = spans(FIGURE_RE, segment)
    quotes = spans(QUOTE_RE, segment)

    found = []
    for m in FIGURE_RE.finditer(segment):
        caption, url = figure_parts(m.group(1))
        found.append((m.start(), {"kind": "figure", "text": caption,
                                  "url": url}))
    for m in BLOCK_RE.finditer(segment):
        # A figcaption lives inside <figure> and is emitted with it; a <p>
        # inside one is the caption again by another name.
        if inside(m.start(), figures):
            continue
        text = clean(m.group(2))
        if not text or is_boilerplate(text):
            continue
        tag = m.group(1).lower()
        if tag.startswith("h"):
            found.append((m.start(), {"kind": "heading", "text": text,
                                      "level": int(tag[1])}))
        else:
            found.append((m.start(), {
                "kind": "quote" if inside(m.start(), quotes) else
                        ("item" if tag == "li" else "para"),
                "text": text}))

    return [b for _, b in sorted(found, key=lambda pair: pair[0])]


def parse_essay(page, url):
    """Read a written piece: the content region is the document."""
    tally = {}
    ep = common_fields(page, url, tally)

    body = blocks(content_region(page))
    if not any(b["kind"] in ("para", "quote") for b in body):
        return None  # page carries no prose; a stub or a landing page

    for b in body:
        b["text"] = apply_corrections(b["text"], tally)

    ep["blocks"] = body
    ep["word_count"] = sum(len(b["text"].split()) for b in body
                           if b["kind"] != "figure")
    ep["figure_count"] = sum(1 for b in body if b["kind"] == "figure")
    ep["quoted_paragraphs"] = sum(1 for b in body if b["kind"] == "quote")
    ep["author"] = apply_corrections(author(page) or CFG.get("author", ""),
                                     tally)
    ep["corrections"] = tally
    return ep


def author(page):
    """The by-line, however this publisher stores it."""
    for blob in re.findall(
            r'<script type="application/ld\+json"[^>]*>(.*?)</script>',
            page, re.S):
        try:
            data = json.loads(blob)
        except json.JSONDecodeError:
            continue
        for node in data.get("@graph", [data]):
            person = node.get("author")
            if isinstance(person, list):
                person = person[0] if person else None
            if isinstance(person, dict) and person.get("name"):
                return clean(person["name"])
    return clean(meta(r'<meta name="author" content="([^"]+)"', page))


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:90].rstrip("-")


def folder_name(ep):
    date = (ep["published"] or "")[:10] or "undated"
    return f"{date}-{slugify(ep['title'])}"


def q(v):
    # JSON string escaping is valid YAML double-quoted-scalar escaping.
    return json.dumps(str(v), ensure_ascii=False)


def frontmatter(ep, extra):
    """The header both content types share, plus the fields only one has."""
    out = ["---"]
    for key in ("title", "url", "published", "modified", "megaphone_id"):
        if ep.get(key) or key in ("title", "url", "published"):
            out.append(f"{key}: {q(ep.get(key, ''))}")
    out.append("keywords: [" + ", ".join(q(k) for k in ep["keywords"]) + "]")
    out += extra
    out.append("scraped_at: " + q(
        datetime.now().astimezone().isoformat(timespec="seconds")))
    out.append("source: " + q("%s - %s" % (CFG.get("publisher", ""),
                                            CFG.get("display_name", ""))))
    out.append("source_name: " + q(CFG.get("name", "")))
    out.append("content_type: " + q(CFG.get("content_type",
                                            archive.DEFAULT_TYPE)))
    if ep["corrections"]:
        out.append("corrections:")
        for note, n in sorted(ep["corrections"].items()):
            out.append(f"  - {q(note)}: {n}")
    else:
        out.append("corrections: []")
    out.append("---")
    return out


def render(ep):
    return (render_essay if KIND.get("items_dir") == "posts"
            else render_transcript)(ep)


def render_transcript(ep):
    out = frontmatter(ep, [
        "speakers: [" + ", ".join(q(s) for s in ep["speakers"]) + "]",
        f"word_count: {ep['word_count']}",
    ])
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


def render_essay(ep):
    """Markdown that keeps the author's voice separable from everyone else's.

    Block quotes stay quoted, because the most likely way to misread an essay
    is to attribute a quoted passage to the person quoting it. Figures are
    emitted as a visible marker rather than dropped: the argument often rests
    on a chart, and a note-writer reading only the prose needs to know that
    something load-bearing is missing rather than infer its absence.
    """
    out = frontmatter(ep, [
        "author: " + q(ep["author"]),
        f"word_count: {ep['word_count']}",
        f"figure_count: {ep['figure_count']}",
        f"quoted_paragraphs: {ep['quoted_paragraphs']}",
    ])
    out += ["", f"# {ep['title']}", "", "## Essay", ""]

    for b in ep["blocks"]:
        if b["kind"] == "heading":
            # Clamped to sit under the "## Essay" heading without running to
            # ###### the moment a publisher's body starts at <h4>, which
            # Substack's does.
            out += ["#" * min(5, max(3, b["level"])) + " " + b["text"], ""]
        elif b["kind"] == "quote":
            out += ["> " + b["text"], ""]
        elif b["kind"] == "item":
            out += ["- " + b["text"], ""]
        elif b["kind"] == "figure":
            label = b["text"] or "no caption in source"
            out += [f"[FIGURE: {label}]" + (f" {b['url']}" if b["url"] else ""),
                    ""]
        else:
            out += [b["text"], ""]
    return "\n".join(out).rstrip() + "\n"


def save(ep):
    d = os.path.join(OUT_ROOT, folder_name(ep))
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, KIND["source_file"])
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(render(ep))
    return path


def saved_urls():
    """URLs already present in the archive, read once up front."""
    found = set()
    if not os.path.isdir(OUT_ROOT):
        return found
    for name in os.listdir(OUT_ROOT):
        p = os.path.join(OUT_ROOT, name, KIND["source_file"])
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as f:
                head = f.read(2000)
            m = re.search(r'^url: "([^"]+)"', head, re.M)
            if m:
                found.add(m.group(1))
    return found


def rows_from_disk():
    """Reconstruct rows for saved items by reading the archive itself."""
    found = {}
    if not os.path.isdir(OUT_ROOT):
        return found
    for name in sorted(os.listdir(OUT_ROOT)):
        p = os.path.join(OUT_ROOT, name, KIND["source_file"])
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8") as f:
            head = f.read(2000)

        def field(key):
            m = re.search(r'^%s: "([^"]*)"' % key, head, re.M)
            return m.group(1) if m else ""

        # Documents scraped before the two content types were unified spell
        # this "transcript_word_count". They regenerate on the next fetch;
        # reading both means an existing archive does not have to be rebuilt
        # just to produce a correct manifest.
        wc = re.search(r"^(?:transcript_)?word_count: (\d+)", head, re.M)
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
    source = argv[0]
    load_config(source)
    argv = argv[1:]

    force = "--force" in argv
    args = [a for a in argv if not a.startswith("--")]
    urls = episode_urls() if "--all" in argv else args
    if not urls:
        sys.exit(__doc__)
    print(f"{CFG.get('display_name', source)}")

    # The middle state of the three: seen, but the publisher ships no document
    # for it. Catalyst's committed manifest spells it "no transcript", so the
    # wording is per content type rather than changed under the existing rows.
    missing = "no " + KIND["document"]

    print(f"{len(urls)} {KIND['item']} URLs to process\n")
    rows, counts = [], {"saved": 0, "skipped": 0, missing: 0, "error": 0}
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
            counts[missing] += 1
            rows.append([date, slug, missing, "", "", url])
            print(f"[{i:>3}/{len(urls)}] NONE   {missing:<14} {slug[:60]}")
        else:
            save(ep)
            counts["saved"] += 1
            rows.append([ep["published"][:10], ep["title"], "saved",
                         ep["word_count"], folder_name(ep), url])
            print(f"[{i:>3}/{len(urls)}] OK     "
                  f"{ep['word_count']:>6,}w  {folder_name(ep)[:70]}")
        time.sleep(DELAY_SECONDS)

    write_manifest(rows)
    print("\n" + "-" * 60)
    for k, v in counts.items():
        print(f"  {k:<16} {v}")
    print(f"  manifest         {os.path.relpath(MANIFEST, ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
