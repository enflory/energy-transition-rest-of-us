#!/usr/bin/env python3
"""Build the reading site for the notes.

    python reader/build.py            # writes reader/_build/
    python reader/build.py --serve    # builds, then serves it on :8000

Standard library only, like the rest of the repository. The notes use a small,
fixed subset of Markdown (paragraphs, `-` lists, bold, italics), and the
validator already enforces their shape, so the renderer below handles exactly
that subset and fails loudly on anything else rather than guessing.

The site is published to energy.lonelymtnlabs.com by
.github/workflows/reader.yml on every push to main, so a new note appears on
the site as soon as it is merged.
"""

import csv
import html
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "reader")
OUT = os.path.join(HERE, "_build")
REPO_URL = "https://github.com/enflory/energy-transition-rest-of-us"
SITE_URL = "https://energy.lonelymtnlabs.com"
LAB_URL = "https://lonelymtnlabs.com"
SITE_TITLE = "The Energy Transition for the Rest of Us"

# Display order, and the one or two sentences each source gets on the site.
# Drawn from each SOURCE-PROFILE.md; kept here rather than in source.json so
# the reader never has to touch pipeline configuration.
SOURCES = [
    ("catalyst",
     "A podcast about energy, climate tech and the electricity system. "
     "Usually one long interview, organized around a single question, with a "
     "host who pushes back."),
    ("critical-capital",
     "A podcast about the money behind energy and physical infrastructure. "
     "One long interview per episode, every other Tuesday."),
    ("steel-for-fuel",
     "Andy Lubershane's newsletter. The name means displacing fossil fuel with "
     "the steel in turbines, panels and reactors. Essays of very uneven length, "
     "roughly monthly."),
]

SECTIONS = [
    ("question", "The question"),
    ("answer", "The answer"),
    ("argument", "The argument"),
    ("terms", "What you need to know first"),
    ("details", "Details worth keeping"),
    ("claims", "Claims worth citing"),
    ("contested", "Where it's contested"),
]

# Short, reader-facing gloss for each section, shown on the About page.
SECTION_PURPOSE = {
    "question": "One line. The question the episode is organized around.",
    "answer": "One to three sentences. What it actually concludes. If the "
              "answer is “it depends,” what it depends on.",
    "argument": "Prose, never bullets. The reasoning, including wherever it "
                "turns. Arguments live in their connectives: but, which "
                "means, only if.",
    "terms": "The two to four terms the argument depends on, in plain "
             "language.",
    "details": "Facts and examples that support the piece but are not its "
               "spine.",
    "claims": "Specific numbers, each attributed to whoever said it and "
              "dated.",
    "contested": "Disagreements, hedges, and where the host pushed back. "
                 "Flattening a hedge is the likeliest way a note misleads, "
                 "so this section is never padding.",
}

THREAD_LABELS = {
    "ai-compute": "AI compute",
    "ai-applications": "AI applications",
    "ders": "DERs",
    "evs": "EVs",
    "construction-and-epc": "Construction and EPC",
    "data-center-power": "Data-center power",
    "first-of-a-kind": "First-of-a-kind",
    "techno-economic-analysis": "Techno-economic analysis",
    "china": "China",
}

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------

def parse_frontmatter(text, path):
    if not text.startswith("---\n"):
        sys.exit("%s: no frontmatter" % path)
    head, body = text[4:].split("\n---\n", 1)
    meta = {}
    for line in head.split("\n"):
        m = re.match(r"^([a-z_]+): (.*)$", line)
        if not m:
            sys.exit("%s: unreadable frontmatter line: %r" % (path, line))
        key, raw = m.groups()
        if raw.startswith('"'):
            meta[key] = json.loads(raw)
        elif raw.startswith("["):
            meta[key] = [t.strip() for t in raw.strip("[]").split(",") if t.strip()]
        else:
            meta[key] = raw
    return meta, body


def split_sections(body, path):
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    found = [h.strip() for h in parts[1::2]]
    expected = [h for _, h in SECTIONS]
    if found != expected:
        sys.exit("%s: sections are %r, expected %r" % (path, found, expected))
    return {key: parts[2 + 2 * i].strip() for i, (key, _) in enumerate(SECTIONS)}


def load():
    sources = []
    for name, blurb in SOURCES:
        sdir = os.path.join(ROOT, "sources", name)
        cfg = json.load(open(os.path.join(sdir, "source.json")))
        essay = cfg.get("content_type") == "essay"
        with open(os.path.join(sdir, "manifest.csv"), newline="") as f:
            urls = {r["folder"]: r["url"] for r in csv.DictReader(f) if r["folder"]}
        items_dir = os.path.join(sdir, "posts" if essay else "episodes")
        notes = []
        for folder in sorted(os.listdir(items_dir)):
            path = os.path.join(items_dir, folder, "note.md")
            if not os.path.exists(path):
                continue
            meta, body = parse_frontmatter(open(path).read(), path)
            notes.append({
                "source": name,
                "folder": folder,
                "title": smart_quotes(meta["post" if essay else "episode"]),
                "published": meta["published"],
                "byline": smart_quotes(meta["author" if essay else "guest"]),
                "threads": meta.get("threads", []),
                "age_warning": meta.get("age_warning"),
                "disclosure": meta.get("disclosure"),
                "sections": split_sections(body, path),
                "words": len(re.findall(r"\S+", body)),
                "original": urls.get(folder),
                "repo_path": os.path.relpath(path, ROOT),
                "url": "/%s/%s/" % (name, folder),
            })
        notes.sort(key=lambda n: (n["published"], n["folder"]))
        for i, n in enumerate(notes):
            n["number"] = i + 1
        sources.append({
            "name": name,
            "display": cfg["display_name"],
            "short": cfg["display_name"].split(" with ")[0],
            "person": cfg.get("author") if essay else cfg.get("host"),
            "role": "Written by" if essay else "Hosted by",
            "publisher": cfg.get("publisher"),
            "essay": essay,
            "kind": "essay" if essay else "episode",
            "blurb": blurb,
            "notes": notes,
            "url": "/%s/" % name,
        })
    return sources


# --------------------------------------------------------------------------
# Markdown, the subset the notes actually use
# --------------------------------------------------------------------------

def smart_quotes(text):
    text = re.sub(r"'(?=\d\ds\b)", "\u2019", text)          # the '90s
    text = re.sub(r"(^|[\s(\[\u2014/-])'", "\\1\u2018", text)
    text = text.replace("'", "\u2019")
    text = re.sub(r'(^|[\s(\[\u2014/-])"', "\\1\u201c", text)
    return text.replace('"', "\u201d")


def inline(text):
    s = html.escape(smart_quotes(text), quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s, flags=re.S)
    s = re.sub(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])", r"<em>\1</em>", s, flags=re.S)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
               r'<a href="\2" rel="noopener">\1</a>', s)
    return s


BULLET = re.compile(r"^[-*] (.*)$")
ORDERED = re.compile(r"^\d+\. (.*)$")


def blocks(md):
    """Yield ('p', text) and ('ul'|'ol', [item, ...]) from a section body."""
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        kind = "ul" if BULLET.match(line) else "ol" if ORDERED.match(line) else None
        if kind:
            pat = BULLET if kind == "ul" else ORDERED
            items = []
            while i < len(lines):
                line = lines[i]
                m = pat.match(line)
                if m:
                    items.append(m.group(1))
                elif line.strip():
                    items[-1] += " " + line.strip()   # continuation, indented or lazy
                else:
                    # A blank line ends the list unless another item follows.
                    j = i
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and pat.match(lines[j]):
                        i = j
                        continue
                    break
                i += 1
            yield kind, items
            continue
        if line.startswith(("#", ">", "|", "<")):
            raise ValueError("unsupported Markdown: %r" % line[:60])
        para = []
        while i < len(lines) and lines[i].strip() and not BULLET.match(lines[i]):
            para.append(lines[i].strip())
            i += 1
        yield "p", " ".join(para)


def render(md, mode=None):
    out = []
    first_p = True
    for kind, value in blocks(md):
        if kind == "p":
            cls = ""
            if mode == "argument" and first_p:
                cls = ' class="lede"'
            elif mode == "claims":
                cls = ' class="aside"'
            out.append("<p%s>%s</p>" % (cls, inline(value)))
            first_p = False
        elif mode == "terms" and all(re.match(r"^\*\*.+?\*\*", v) for v in value):
            out.append('<dl class="terms">')
            for v in value:
                m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", v)
                term = m.group(1).rstrip(".:")
                out.append("<div><dt>%s</dt><dd>%s</dd></div>" % (inline(term), inline(m.group(2))))
            out.append("</dl>")
        elif mode == "claims":
            out.append('<ul class="claims">')
            for v in value:
                m = re.match(r"^(.*?)\s*\(([^()]{1,90})\)\.?$", v, flags=re.S)
                if m:
                    out.append('<li>%s <span class="attr">%s</span></li>'
                               % (inline(m.group(1)), inline(m.group(2))))
                else:
                    out.append("<li>%s</li>" % inline(v))
            out.append("</ul>")
        else:
            out.append("<%s>%s</%s>" % (kind, "".join("<li>%s</li>" % inline(v) for v in value), kind))
    return "\n".join(out)


def plain(md):
    """Section text with Markdown markers stripped, for search and previews."""
    s = " ".join(v if k == "p" else " ".join(v) for k, v in blocks(md))
    return smart_quotes(re.sub(r"[*`]", "", s))


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def esc(s):
    return html.escape(s or "", quote=True)


def thread_label(t):
    return THREAD_LABELS.get(t) or t.replace("-", " ").capitalize()


def d(iso):
    return date(*map(int, iso.split("-")))


def date_short(iso):
    x = d(iso)
    return "%d %s %d" % (x.day, MONTHS[x.month - 1][:3], x.year)


def date_long(iso):
    x = d(iso)
    return "%s %d, %d" % (MONTHS[x.month - 1], x.day, x.year)


def month_year(iso):
    x = d(iso)
    return "%s %d" % (MONTHS[x.month - 1][:3], x.year)


def minutes(words):
    return max(1, round(words / 230))


ARROW = ('<svg class="arrow" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 8 8 2M3.5 2H8v4.5" '
         'fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>')


def byline(note, source):
    return ("by " if source["essay"] else "with ") + note["byline"]


def chips(threads, cls="chips"):
    return '<ul class="%s">%s</ul>' % (cls, "".join(
        '<li><a href="/threads/%s/">%s</a></li>' % (t, esc(thread_label(t))) for t in threads))


# --------------------------------------------------------------------------
# Page shell
# --------------------------------------------------------------------------

def shell(title, body, *, description, path, active=None, body_class="", extra_head=""):
    nav = []
    for key, label, href in [("catalyst", "Catalyst", "/catalyst/"),
                             ("critical-capital", "Critical Capital", "/critical-capital/"),
                             ("steel-for-fuel", "Steel For Fuel", "/steel-for-fuel/"),
                             ("threads", "Threads", "/threads/"),
                             ("about", "About", "/about/")]:
        cur = ' aria-current="page"' if key == active else ""
        nav.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    full_title = title if title == SITE_TITLE else "%s · %s" % (title, SITE_TITLE)
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{site}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:url" content="{site}{path}">
<meta name="theme-color" content="#f4efe4">
<link rel="icon" type="image/svg+xml" href="/static/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/style.css">
{extra_head}</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<div class="grain" aria-hidden="true"></div>
<header class="masthead">
  <div class="masthead-inner">
    <a class="wordmark" href="/">
      <span class="wm-kicker">Field notes</span>
      <span class="wm-title">The Energy Transition <em>for the Rest of Us</em></span>
    </a>
    <nav class="nav" aria-label="Sections">{nav}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="colophon">
  <div class="colophon-inner">
    <p class="colophon-lede">Notes from <em>{site_title}</em>, written from primary sources and
    checked against them by an agent that did not write them. CC BY 4.0.</p>
    <p class="colophon-links">
      <a href="{repo}">Source on GitHub {arrow}</a>
      <a href="{lab}">A Lonely Mountain Labs project {arrow}</a>
    </p>
  </div>
</footer>
<script src="/static/app.js" defer></script>
</body>
</html>
""".format(full_title=esc(full_title), title=esc(title), description=esc(description),
           site=SITE_URL, path=path, nav="".join(nav), body=body, site_title=SITE_TITLE,
           repo=REPO_URL, lab=LAB_URL, arrow=ARROW, body_class=body_class,
           extra_head=extra_head)


def write(path, content):
    full = os.path.join(OUT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


# --------------------------------------------------------------------------
# Rows and cards shared across pages
# --------------------------------------------------------------------------

def note_row(n, src, show_source=False):
    question = plain(n["sections"]["question"])
    label = esc(src["short"]) + " · " if show_source else ""
    return """<li class="row" data-threads="{threads}" data-text="{text}">
  <a href="{url}">
    <span class="row-date">{label}{date}</span>
    <span class="row-body">
      <span class="row-title">{title}</span>
      <span class="row-by">{by}</span>
      <span class="row-q">{q}</span>
    </span>
  </a>
</li>""".format(threads=" ".join(n["threads"]),
                text=esc((n["title"] + " " + n["byline"] + " " + question + " " +
                          " ".join(thread_label(t) for t in n["threads"])).lower()),
                url=n["url"], label=label, date=date_short(n["published"]),
                title=esc(n["title"]), by=esc(byline(n, src)), q=esc(question))


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------

def build_note(n, src, prev_n, next_n, related, by_name):
    s = n["sections"]
    kind = src["kind"]
    notices = []
    if n["age_warning"]:
        notices.append('<aside class="notice"><span class="notice-label">Dated</span><p>%s</p></aside>'
                       % inline(n["age_warning"]))
    if n["disclosure"]:
        notices.append('<aside class="notice"><span class="notice-label">Disclosure</span><p>%s</p></aside>'
                       % inline(n["disclosure"]))

    toc = "".join('<li><a href="#%s"><span class="toc-n">%02d</span>%s</a></li>'
                  % (key, i + 1, esc(smart_quotes(label))) for i, (key, label) in enumerate(SECTIONS))

    def section(i, key):
        label = dict(SECTIONS)[key]
        return """<section class="part" id="{key}" aria-labelledby="{key}-h">
  <h2 id="{key}-h"><span class="part-n">{n:02d}</span>{label}</h2>
  <div class="prose prose-{key}">{html}</div>
</section>""".format(key=key, n=i + 1, label=esc(smart_quotes(label)), html=render(s[key], key))

    parts = "\n".join(section(i, key) for i, (key, _) in enumerate(SECTIONS) if i >= 2)

    def neighbour(x, rel):
        if not x:
            return '<span class="pager-empty"></span>'
        return """<a class="pager-link pager-%s" href="%s" rel="%s">
  <span class="pager-dir">%s</span>
  <span class="pager-title">%s</span>
  <span class="pager-date">%s</span>
</a>""" % (rel, x["url"], rel, "← Older" if rel == "prev" else "Newer →",
           esc(x["title"]), date_short(x["published"]))

    rel_html = ""
    if related:
        rel_html = '<section class="related"><h2 class="kicker">Shares threads with</h2><ol class="rows">%s</ol></section>' % (
            "".join(note_row(r, by_name[r["source"]], show_source=True) for r in related))

    original = ""
    if n["original"]:
        original = '<a class="meta-link" href="%s" rel="noopener">Original %s %s</a>' % (
            esc(n["original"]), kind, ARROW)

    body = """<div class="progress" aria-hidden="true"><span></span></div>
<article class="note" data-prev="{prev}" data-next="{next}">
  <div class="note-grid">
  <header class="note-head">
    <p class="kicker"><a href="{src_url}">{src_short}</a> <span class="dim">N&deg; {num:03d} of {total}</span> <span class="dim">{date}</span></p>
    <h1 class="note-title">{title}</h1>
    <p class="note-by">{by}</p>
    <div class="note-meta">
      {chips}
      <p class="meta-line"><span>{mins} min read</span>{original}</p>
    </div>
  </header>

    <nav class="toc" aria-label="In this note">
      <p class="toc-label">In this note</p>
      <ol>{toc}</ol>
    </nav>

    <div class="note-body">
      <details class="toc-mobile"><summary>In this note</summary><ol>{toc}</ol></details>
      {notices}
      <section class="qa" id="question" aria-label="The question and the answer">
        <div class="qa-block qa-q">
          <span class="qa-mark" aria-hidden="true">Q.</span>
          <div><h2 class="qa-label">The question</h2><div class="qa-text">{question}</div></div>
        </div>
        <div class="qa-block qa-a" id="answer">
          <span class="qa-mark" aria-hidden="true">A.</span>
          <div><h2 class="qa-label">The answer</h2><div class="qa-text">{answer}</div></div>
        </div>
      </section>
      {parts}
      <footer class="note-foot">
        <p class="cite">Cite as: &ldquo;{title_plain},&rdquo; <em>{site_title}</em>, note on {src_display}, {date_long}. CC BY 4.0.
        <a href="{repo}/blob/main/{repo_path}">View the Markdown {arrow}</a></p>
      </footer>
    </div>
  </div>

  <nav class="pager" aria-label="More from {src_short}">
    {older}
    <a class="pager-index" href="{src_url}">All {total} {kind}s</a>
    {newer}
  </nav>
  {related}
</article>""".format(
        prev=prev_n["url"] if prev_n else "", next=next_n["url"] if next_n else "",
        src_url=src["url"], src_short=esc(src["short"]), num=n["number"], total=len(src["notes"]),
        date=date_short(n["published"]), title=inline(n["title"]), by=esc(byline(n, src)),
        chips=chips(n["threads"]), mins=minutes(n["words"]), original=original, toc=toc,
        notices="\n".join(notices), question=render(s["question"]), answer=render(s["answer"]),
        parts=parts, title_plain=esc(n["title"]), site_title=SITE_TITLE, src_display=esc(src["display"]),
        date_long=date_long(n["published"]), repo=REPO_URL, repo_path=n["repo_path"], arrow=ARROW,
        older=neighbour(prev_n, "prev"), newer=neighbour(next_n, "next"), kind=kind,
        related=rel_html)
    write(n["url"], shell(n["title"], body, description=plain(s["answer"])[:300], path=n["url"],
                          active=src["name"], body_class="page-note"))


def thread_filter(threads, person):
    opts = "".join('<option value="%s">%s (%d)</option>' % (t, esc(thread_label(t)), c)
                   for t, c in sorted(threads.items(), key=lambda kv: thread_label(kv[0])))
    return """<div class="filter" role="search">
  <label class="filter-field"><span class="sr">Filter</span>
    <input type="search" data-filter-text placeholder="Filter by title, {person}, or question" autocomplete="off"></label>
  <label class="filter-field filter-select"><span class="sr">Thread</span>
    <select data-filter-thread><option value="">All threads</option>{opts}</select></label>
  <p class="filter-count" data-filter-count aria-live="polite"></p>
</div>""".format(opts=opts, person=person)


def build_source(src):
    notes = src["notes"]
    threads = Counter(t for n in notes for t in n["threads"])
    words = sum(n["words"] for n in notes)
    years = defaultdict(list)
    for n in notes:
        years[n["published"][:4]].append(n)
    groups = []
    for y in sorted(years, reverse=True):
        rows = "\n".join(note_row(n, src) for n in reversed(years[y]))
        groups.append('<section class="year" data-group><h2 class="year-label">%s <span class="dim" data-group-count>%d</span></h2><ol class="rows">%s</ol></section>'
                      % (y, len(years[y]), rows))
    body = """<header class="page-head">
  <p class="kicker">Source &middot; {kindcap}s</p>
  <h1 class="page-title">{display}</h1>
  <p class="page-lede">{blurb}</p>
  <dl class="facts">
    <div><dt>{role}</dt><dd>{person}</dd></div>
    <div><dt>Published by</dt><dd>{publisher}</dd></div>
    <div><dt>Notes</dt><dd>{count}</dd></div>
    <div><dt>Span</dt><dd>{first} &ndash; {last}</dd></div>
    <div><dt>Reading</dt><dd>~{words:,} words</dd></div>
  </dl>
</header>
<div class="listing" data-filterable>
  {filter}
  {groups}
  <p class="empty" data-filter-empty hidden>Nothing matches. Try a broader word, or a different thread.</p>
</div>""".format(kindcap=src["kind"].capitalize(), display=esc(src["display"]), blurb=esc(src["blurb"]),
                  role=src["role"], person=esc(src["person"]), publisher=esc(src["publisher"]),
                  count=len(notes), first=month_year(notes[0]["published"]),
                  last=month_year(notes[-1]["published"]), words=round(words, -3),
                  filter=thread_filter(threads, "author" if src["essay"] else "guest"), groups="\n".join(groups))
    write(src["url"], shell(src["display"], body, path=src["url"], active=src["name"],
                            description="Plain-language notes on every %s of %s." % (src["kind"], src["display"])))


def build_threads(sources, all_notes, by_name):
    by_thread = defaultdict(list)
    for n in all_notes:
        for t in n["threads"]:
            by_thread[t].append(n)
    ordered = sorted(by_thread, key=lambda t: thread_label(t).lower())
    letters = defaultdict(list)
    for t in ordered:
        letters[thread_label(t)[0].upper()].append(t)
    cols = []
    for letter in sorted(letters):
        items = "".join('<li><a href="/threads/%s/"><span>%s</span><span class="leader"></span><span class="count">%d</span></a></li>'
                        % (t, esc(thread_label(t)), len(by_thread[t])) for t in letters[letter])
        cols.append('<section class="index-letter"><h2>%s</h2><ul>%s</ul></section>' % (letter, items))
    body = """<header class="page-head">
  <p class="kicker">Index</p>
  <h1 class="page-title">Threads</h1>
  <p class="page-lede">Every note is tagged with two to five threads from one fixed vocabulary, so the same subject is
  called the same thing across all three sources. Pick one to read everything that touches it, newest first.</p>
</header>
<div class="book-index">{cols}</div>""".format(cols="".join(cols))
    write("/threads/", shell("Threads", body, path="/threads/", active="threads",
                             description="Browse the notes by subject."))

    for t, notes in by_thread.items():
        notes = sorted(notes, key=lambda n: n["published"], reverse=True)
        per_source = Counter(n["source"] for n in notes)
        split = " · ".join("%s %d" % (esc(by_name[s]["short"]), per_source[s]) for s, _ in SOURCES if per_source[s])
        body = """<header class="page-head">
  <p class="kicker"><a href="/threads/">Threads</a></p>
  <h1 class="page-title">{label}</h1>
  <p class="page-lede">{count} note{pl} &middot; {split}</p>
</header>
<div class="listing"><ol class="rows">{rows}</ol></div>""".format(
            label=esc(thread_label(t)), count=len(notes), pl="" if len(notes) == 1 else "s",
            split=split, rows="\n".join(note_row(n, by_name[n["source"]], show_source=True) for n in notes))
        write("/threads/%s/" % t, shell(thread_label(t), body, path="/threads/%s/" % t, active="threads",
                                        description="Notes on %s." % thread_label(t).lower()))
    return by_thread


def build_home(sources, all_notes, by_thread, by_name):
    total_words = sum(n["words"] for n in all_notes)
    first = min(n["published"] for n in all_notes)
    last = max(n["published"] for n in all_notes)
    cards = []
    for i, src in enumerate(sources):
        notes = src["notes"]
        cards.append("""<a class="source-card" href="{url}">
  <span class="kicker"><span class="accent">{n}</span> &middot; {kindcap}s</span>
  <span class="source-name">{display}</span>
  <span class="source-person">{role} {person}</span>
  <span class="source-blurb">{blurb}</span>
  <span class="source-foot"><span>{count} notes</span><span>{first} &ndash; {last}</span></span>
</a>""".format(url=src["url"], n=["I", "II", "III"][i], kindcap=src["kind"].capitalize(),
               display=esc(src["display"]), role=src["role"].lower().capitalize(), person=esc(src["person"]),
               blurb=esc(src["blurb"]), count=len(notes), first=month_year(notes[0]["published"]),
               last=month_year(notes[-1]["published"])))
    latest = sorted(all_notes, key=lambda n: (n["published"], n["folder"]), reverse=True)[:8]
    top = sorted(by_thread, key=lambda t: -len(by_thread[t]))[:14]
    top_html = "".join('<li><a href="/threads/%s/">%s <span class="count">%d</span></a></li>'
                       % (t, esc(thread_label(t)), len(by_thread[t])) for t in top)
    body = """<section class="hero">
  <div class="hero-main">
  <p class="kicker">Lonely Mountain Labs &middot; Field notes</p>
  <h1 class="hero-title">The energy transition, <em>for the rest of us.</em></h1>
  <p class="hero-lede">Plain-language notes on the podcasts and essays where people building the energy system explain it.
  One note per episode or essay, accurate enough to quote in a meeting, written for someone smart who doesn&rsquo;t work in energy.</p>
  <p class="hero-stats"><span><b>{count}</b> notes</span><span><b>3</b> sources</span><span><b>~{kwords}k</b> words</span><span>{first} &ndash; {last}</span></p>
  <div class="search" role="search">
    <label for="q" class="sr">Search every note</label>
    <input id="q" type="search" placeholder="Search every note: nuclear, transformers, PJM, Lovering&hellip;" autocomplete="off" data-search>
    <kbd aria-hidden="true">/</kbd>
    <p class="search-count" data-search-count aria-live="polite"></p>
    <ol class="rows search-results" data-search-results hidden></ol>
  </div>
  </div>
  <aside class="sample" aria-label="From the latest note">
    <p class="kicker"><span class="accent">Latest</span> {s_src} &middot; {s_date}</p>
    <a class="sample-title" href="{s_url}">{s_title}</a>
    <div class="sample-qa"><span class="qa-mark" aria-hidden="true">Q.</span><p class="sample-q">{s_q}</p></div>
    <div class="sample-qa"><span class="qa-mark" aria-hidden="true">A.</span><p class="sample-a">{s_a}</p></div>
    <p class="more"><a href="{s_url}">Read the argument &rarr;</a></p>
  </aside>
</section>

<section class="home-block">
  <h2 class="block-label">Start with a source</h2>
  <div class="source-cards">{cards}</div>
</section>

<section class="home-block home-split">
  <div>
    <h2 class="block-label">Latest notes</h2>
    <ol class="rows">{latest}</ol>
  </div>
  <div>
    <h2 class="block-label">Or follow a thread</h2>
    <ul class="thread-cloud">{top}</ul>
    <p class="more"><a href="/threads/">All {nthreads} threads &rarr;</a></p>
    <div class="how">
      <h2 class="block-label">How a note reads</h2>
      <ol class="how-list">
        <li><b>The question</b> and <b>the answer</b>, up front, so you know in ten seconds whether it&rsquo;s the one you need.</li>
        <li><b>The argument</b> in prose, because the reasoning lives in the &ldquo;but&rdquo; and the &ldquo;which means.&rdquo;</li>
        <li><b>Claims worth citing</b>, each number attributed and dated.</li>
        <li><b>Where it&rsquo;s contested</b>, so the hedges survive.</li>
      </ol>
      <p class="more"><a href="/about/">More on how these are made &rarr;</a></p>
    </div>
  </div>
</section>""".format(count=len(all_notes), kwords=round(total_words / 1000), first=month_year(first),
                     last=month_year(last), cards="".join(cards),
                     latest="\n".join(note_row(n, by_name[n["source"]], show_source=True) for n in latest),
                     top=top_html, nthreads=len(by_thread),
                     s_src=esc(by_name[latest[0]["source"]]["short"]), s_date=date_short(latest[0]["published"]),
                     s_url=latest[0]["url"], s_title=esc(latest[0]["title"]),
                     s_q=inline(plain(latest[0]["sections"]["question"])),
                     s_a=inline(plain(latest[0]["sections"]["answer"])))
    write("/", shell(SITE_TITLE, body, path="/", body_class="page-home",
                     description="Plain-language notes on the energy transition, built from primary sources: "
                                 "every episode of Catalyst and Critical Capital and every Steel For Fuel essay."))


def build_about():
    rows = "".join('<div><dt><span class="toc-n">%02d</span>%s</dt><dd>%s</dd></div>'
                   % (i + 1, esc(smart_quotes(label)), esc(SECTION_PURPOSE[key])) for i, (key, label) in enumerate(SECTIONS))
    body = """<header class="page-head">
  <p class="kicker">About</p>
  <h1 class="page-title">A note with a thesis</h1>
</header>
<div class="about prose">
  <p class="lede">It started in a work meeting, when people asked about the environmental impact of AI data centers and
  I found myself relaying podcasts and essays I&rsquo;d learned from. I wished I had something to hand them.</p>
  <p>There is a great deal of excellent primary-source material about the energy transition, mostly long-form
  interviews with the people actually building the system, and newsletters written by people close to it. It is also
  hours a month plus a reading list, and almost none of it is in a form you can hand to a colleague who asked a
  reasonable question.</p>
  <p>The usual fix is a summary, and the usual summary fails in a specific way: it produces a pile of individually
  true facts that lose the argument. So the unit here is not a summary. It is a note with a thesis, built to a
  specification that makes the failure modes explicit, and every note has the same seven parts in the same order.</p>
  <dl class="spec">{rows}</dl>
  <h2>Checked by someone who didn&rsquo;t write it</h2>
  <p>Each note is written from the full transcript or essay, never from show notes or a subtitle, and then verified
  against the source by a separate agent that did not write it. A writer has already made each judgment call once
  and will mostly confirm it; an independent pass over two dozen early notes found roughly a hundred corrections.</p>
  <p>Notes stay strictly inside their own episode or essay: no hindsight, no outside knowledge used to correct a
  claim. When a claim looks dated, it is recorded as stated, with its date, and older notes carry a warning saying
  what has likely moved since.</p>
  <h2>What isn&rsquo;t here</h2>
  <p>Transcripts and essay text belong to their publishers and are not republished. Every note links to the original.
  The notes themselves are licensed CC BY 4.0, and the pipeline, specification and validator that produce them are
  <a href="{repo}">on GitHub</a>.</p>
</div>""".format(rows=rows, repo=REPO_URL)
    write("/about/", shell("About", body, path="/about/", active="about",
                           description="How the notes are written and checked."))


def build_404():
    body = """<header class="page-head">
  <p class="kicker">404</p>
  <h1 class="page-title">No note here.</h1>
  <p class="page-lede">The page moved or never existed. <a href="/">Start from the index</a>, or pick a
  <a href="/threads/">thread</a>.</p>
</header>"""
    write("404.html", shell("Not found", body, path="/404.html", description="Page not found."))


def related_notes(n, all_notes, k=3):
    mine = set(n["threads"])
    scored = []
    for o in all_notes:
        if o is n:
            continue
        overlap = len(mine & set(o["threads"]))
        if overlap >= 2:
            scored.append((overlap, o["published"], o))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return [o for _, _, o in scored[:k]]


def build():
    sources = load()
    by_name = {s["name"]: s for s in sources}
    all_notes = [n for s in sources for n in s["notes"]]

    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(HERE, "static"), os.path.join(OUT, "static"))
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write(SITE_URL.split("//")[1] + "\n")

    for src in sources:
        notes = src["notes"]
        for i, n in enumerate(notes):
            build_note(n, src, notes[i - 1] if i else None, notes[i + 1] if i + 1 < len(notes) else None,
                       related_notes(n, all_notes), by_name)
        build_source(src)
    by_thread = build_threads(sources, all_notes, by_name)
    build_home(sources, all_notes, by_thread, by_name)
    build_about()
    build_404()

    index = [{
        "u": n["url"], "t": n["title"], "s": by_name[n["source"]]["short"], "d": date_short(n["published"]),
        "b": byline(n, by_name[n["source"]]), "q": plain(n["sections"]["question"]),
        "h": " ".join(thread_label(t) for t in n["threads"]),
        "x": plain(n["sections"]["answer"]),
    } for n in sorted(all_notes, key=lambda n: n["published"], reverse=True)]
    with open(os.path.join(OUT, "search.json"), "w") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

    urls = ["/", "/about/", "/threads/"] + [s["url"] for s in sources] + \
           ["/threads/%s/" % t for t in sorted(by_thread)] + [n["url"] for n in all_notes]
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.writelines("  <url><loc>%s%s</loc></url>\n" % (SITE_URL, u) for u in urls)
        f.write("</urlset>\n")

    print("built %d notes across %d sources and %d threads into %s"
          % (len(all_notes), len(sources), len(by_thread), os.path.relpath(OUT, ROOT)))


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUT)
        print("serving on http://localhost:8000")
        http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()
