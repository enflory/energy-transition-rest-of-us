# Adding a source

A *source* is a publication this archive tracks: a podcast, or a newsletter.
Nothing about any particular one is hard-coded. Adding one means writing a
config, learning the source, and only then scaling up.

The order matters. The Catalyst notes are consistent because the show was
understood before 125 notes were written, not after.

---

## 0a. Decide the content type

Two exist, and the choice decides the directory layout, the parser, the note
frontmatter and the note length rule. It is the first line of the config:

| `content_type` | for | items live in | the document is |
|---|---|---|---|
| `podcast` (default) | conversations with transcripts | `episodes/` | `transcript.md` |
| `essay` | written pieces | `posts/` | `essay.md` |

The test is not what the publisher calls itself but **whether the document has
speaker labels**. The podcast parser finds where a transcript starts by locating
the first paragraph opening `Name:`; an essay has none, so that parser finds
nothing and records every page as having no document. If you point the default
parser at a newsletter, that is the symptom: a clean run, no errors, and
everything logged as `no transcript`.

`scripts/archive.py` holds every difference between the two. If you find
yourself wanting a third behaviour somewhere else, it belongs there.

---

## 0. Find out who actually publishes the transcripts

Do this before anything else. It takes five minutes and it decides the entire
configuration.

**The network that publishes a show does not necessarily publish its
transcripts.** Critical Capital is a Latitude Media show, and the obvious move
was to point the scraper at the Latitude sitemap that already works for
Catalyst. Latitude carried 2 of that show's 12 episodes, both show-notes pages
with no transcript text at all. The transcripts live on the co-producer's site,
on a different CMS, with different markup, a different date format and a
different pagination scheme.

So: pick two or three episodes, open the pages a listener would actually land
on, and confirm a full transcript is there. Then find the place that lists every
episode. Only then write the config.

Search the publisher's sitemap for the show's slug and count what comes back:

```python
import re, urllib.request
xml = urllib.request.urlopen(urllib.request.Request(
    "https://example.com/sitemap.xml",
    headers={"User-Agent": "Mozilla/5.0"})).read().decode()
print([l for l in re.findall(r"<loc>([^<]+)</loc>", xml) if "showname" in l])
```

If that count is well below the number of episodes the show has actually
released, the sitemap is not your source. Find the show's own index page.

---

## 1. Create the directory and config

```
sources/<source>/
  source.json
  SOURCE-PROFILE.md
```

Copy `sources/critical-capital/source.json` for a podcast or
`sources/steel-for-fuel/source.json` for an essay source. The fields:

| Field | What it does |
|---|---|
| `name` | Directory name. Used in commands. |
| `content_type` | `podcast` or `essay`. Omitted means `podcast`. |
| `display_name` | Human-readable title, used in transcript frontmatter. |
| `publisher` | Recorded in frontmatter for provenance. Whoever publishes the transcript, which is not always the network. |
| `host` | Podcasts. Recorded for reference. Fill in after reading a transcript. |
| `author` | Essays. The default by-line, used only when a page carries none. |
| `sitemaps` | Sitemap URLs to read. May be empty if the site has none worth using. |
| `url_filter` | Substring every episode URL contains. Applied to all sources. |
| `delay_seconds` | Politeness delay between requests. Leave at 1.0. |
| `corrections` | Repeated publisher misspellings. **Start empty.** |
| `non_speakers` | Labels matching the speaker shape that are not people. |
| `boilerplate` | Sponsor reads, credits, ad markers. |

Five more fields exist for sites that are not the default WordPress shape. All
are optional, and omitting one keeps the original behaviour.

| Field | What it does |
|---|---|
| `index_pages` | Listing pages to walk for episode links, unioned with the sitemap results. Use whenever the sitemap might lag. |
| `index_link_pattern` | Regex with one capture group extracting an episode href from a listing page. |
| `index_next_pattern` | Regex with one capture group giving the "next page" link, for paginated listings. Omit if there is one page. |
| `title_suffix` | Regex stripped off the end of `<title>`, usually the site name. |
| `published` | List of `{pattern, format}` extractors for the publication date, tried in order. `format` is `iso` for an ISO timestamp, otherwise a `strptime` format. Defaults to the `article:published_time` meta tag. |
| `content_start` / `content_end` | Regexes bounding the region of the page that holds the item's own content. Everything outside is discarded before paragraphs are read. |

For an essay source, `content_start` / `content_end` are not optional in
practice. The podcast parser has a second way of finding where the content
begins, namely the first speaker label; the essay parser does not, so the
content region *is* the document. Get these two anchors wrong and the whole
page becomes the essay, navigation and footer included.

**Find the URL filter empirically**, not by guessing, using the snippet in step
0. For Latitude Media, verified filters are `/catalyst-`, `/open-circuit-` and
`/green-blueprint-`; all three shows publish full transcripts there. Critical
Capital is the exception and is configured against crux.com instead.

**Prefer `content_start` / `content_end` over a long boilerplate list.** Modern
site templates put navigation menus, inline CSS, author bios, related-article
cards and the footer into `<p>` elements on the same page as the transcript.
Narrowing to the content region removes all of it at once and keeps working when
the footer changes. Both anchors warn and fall back to the whole page if they
stop matching, so a template change is visible rather than silent.

**Leave `corrections` empty until you have seen a real, repeated error.** A
correction edits the source text. It is for a publisher consistently misspelling
a name, not for anything that requires judgment.

---

## 2. Fetch a few items and read them

```bash
python run.py fetch <source>
```

Check the count first. If the scraper reports fewer items than the source has
published, your discovery configuration is incomplete, and the missing one is
disproportionately likely to be the newest.

Then actually read two or three documents.

### On a podcast, you are looking for:

- **An intro bumper** whose label matches the speaker-label shape. Catalyst's
  is `Tag:`, and it contaminated 48 episodes before anyone noticed. Add it to
  `non_speakers`.
- **Sponsor reads** that name real companies and read like content. Add their
  opening lines to `boilerplate`.
- **A recurring misspelling** of the host's or a regular's name. Add a
  correction with a clear note.
- **Formatting quirks**, such as speaker labels that render as plain text, or
  zero-width characters ahead of a label. The latter are invisible and silently
  drop a paragraph out of the dialogue. The scraper strips them, but if speaker
  labels go missing on a new show, look for them first.
- **Whether the host opens with a framing monologue.** This matters more than it
  sounds. A framing monologue is the main source of attribution drift, and
  verification check 3 depends on knowing whether the show does it.
- **Whether the host pushes back.** This changes what a good note looks like. On
  a show where the host argues with guests, an episode with no disagreement is
  rare and probably means you missed something. On a show where the host builds
  on the answers, it is the norm, and a note that manufactures contestation to
  fill the section is worse than one that says plainly there was none. Say which
  kind of show it is in the profile.
- **What the guests have at stake.** A show that interviews researchers and a
  show that interviews founders about their own companies produce different
  kinds of evidence. Neither is better, but the profile should say which, so
  notes attribute claims at the right strength.

### On an essay source, you are looking for:

- **Whether the by-line is trustworthy.** Guest posts and cross-posts are
  common and the metadata does not always reflect them. On Steel For Fuel one
  post is correctly bylined to its guest author while two others are bylined to
  the newsletter's owner and are substantially written by someone else. Find
  the marker the publication uses for a handover and record it in the profile.
  This is the single highest-value thing to learn about an essay source.
- **Block quotes, and whom they quote.** The parser preserves them as `> `
  lines because they are the main attribution hazard. Read a few and find out
  whether the author mostly quotes outside sources, or mostly quotes their own
  earlier posts in order to revise them. The second is more dangerous and
  should be called out in the profile.
- **How much of the argument is in charts.** Count the `[FIGURE: ...]` markers
  and how many carry captions. A source where half the figures are unlabelled
  and the prose says "as you can see above" is one where notes have to say
  plainly that the evidence is not in the text.
- **Boilerplate that is prose.** Subscribe pitches and cross-promotion sit in
  `<p>` elements exactly like argument does. Anchor these patterns carefully:
  on Steel For Fuel the subscribe pitch shares a paragraph with the marker that
  ends a guest section, so a loose pattern would delete the one signal that
  says whose words the preceding page was.
- **The length distribution**, because it decides whether the note band will
  fit. Steel For Fuel runs 248 to 11,869 words, which is why essay notes are
  sized against their source.

### For both

Re-fetch after config changes:

```bash
python run.py refetch <source>
```

Check the word counts. A document far shorter than the others usually means the
parser found the wrong starting point, and one that is suspiciously long
usually means boilerplate leaked in. Check the titles too: a publisher that
appends a by-line or site name to some pages and not others will put it in
folder names and note titles unless `title_suffix` catches every variant.

---

## 3. Fill in the source profile

`SOURCE-PROFILE.md` is read by every agent that writes a note for this source,
so it is doing real work. Cover:

- What the show is, who hosts it, and its usual format.
- **Disclosure norms.** Does the host have investing relationships with guests?
  Is it disclosed on air? What is boilerplate self-identification rather than an
  interest in the guest? Be specific about what triggers a `disclosure:` field
  and what does not.
- **Document quirks** specific to this source.
- **What the attribution check looks like here**, with real observed examples.
  For a podcast this is the gap between the host's framing and the guest's
  words. For an essay it is quoted voice: which `> ` blocks are the author's
  own earlier position, which are outside sources, and where a guest's section
  starts and stops.

---

## 4. Hand-write one or two reference notes

Do this yourself, slowly, reading the document closely, and check the result
against it twice. For an essay source, make one of them a **short** post: the
compact note and the long one do not look alike, and a single benchmark drawn
from a 6,000-word essay teaches the wrong shape for the 400-word one. Then list them in the profile with a sentence each
on what they demonstrate, and name one as the benchmark.

This is the single highest-leverage step. Every agent reads the benchmark before
writing anything, so a weak reference note propagates into every note that
follows. A strong one is worth more than any amount of specification prose.

---

## 5. Scale up

```bash
python run.py brief <source>
```

Paste the brief into an agent. Three items per agent, mixed topics, strong
model. The brief is written from the source's content type, so it already
points at the right half of the spec and the right attribution check. Then:

```bash
python run.py validate <source>
python run.py dedupe <source>
```

Have a **different** agent verify the notes than the one that wrote them.

---

## 6. Start the synthesis files

Create `sources/<source>/synthesis/` with `hindsight-seeds.md` and
`archive-caveats.md`, even if they start nearly empty. Cross-item
observations and corpus data-quality findings arrive while notes are being
written, and they are lost if there is nowhere to put them.

---

## Does the spec need changing?

Usually not. `docs/NOTE-SPEC.md` is portable by design, and show-specific facts
belong in the profile.

Change the spec only when you find something true of **note-writing in
general** that it does not yet say. If you do change it, do it between waves,
never while agents are reading it, and bump the version number at the top.

Adding to the controlled vocabulary is the common exception. Do it from
evidence: count how many episodes actually need the tag before adding it. A tag
used once does not help the synthesis layer group anything, and a vocabulary
that fragments is worse than one that is slightly too coarse. Agents propose new
tags through `proposed_threads:` rather than inventing them in `threads:`, which
keeps proposals visible and reconcilable instead of silently splitting the
vocabulary.
