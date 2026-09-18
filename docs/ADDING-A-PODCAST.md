# Adding a podcast

Nothing about any particular show is hard-coded. Adding one means writing a
config, learning the show, and only then scaling up.

The order matters. The Catalyst notes are consistent because the show was
understood before 125 notes were written, not after.

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
podcasts/<show>/
  podcast.json
  SHOW-PROFILE.md
```

Copy `podcasts/critical-capital/podcast.json` as a starting point. The fields:

| Field | What it does |
|---|---|
| `name` | Directory name. Used in commands. |
| `display_name` | Human-readable title, used in transcript frontmatter. |
| `publisher` | Recorded in frontmatter for provenance. Whoever publishes the transcript, which is not always the network. |
| `host` | Recorded for reference. Fill in after reading a transcript. |
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
| `content_start` / `content_end` | Regexes bounding the region of the page that holds the episode's own content. Everything outside is discarded before paragraphs are read. |

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

## 2. Fetch a few episodes and read them

```bash
python run.py fetch <show>
```

Check the count first. If the scraper reports fewer episodes than the show has
released, your discovery configuration is incomplete, and the missing one is
disproportionately likely to be the newest.

Then actually read two or three transcripts. You are looking for:

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

Re-fetch after config changes:

```bash
python run.py refetch <show>
```

Check the word counts. A transcript far shorter than the others usually means
the parser found the wrong starting point, and a transcript that is suspiciously
long usually means boilerplate leaked in.

---

## 3. Fill in the show profile

`SHOW-PROFILE.md` is read by every agent that writes a note for this show, so it
is doing real work. Cover:

- What the show is, who hosts it, and its usual format.
- **Disclosure norms.** Does the host have investing relationships with guests?
  Is it disclosed on air? What is boilerplate self-identification rather than an
  interest in the guest? Be specific about what triggers a `disclosure:` field
  and what does not.
- **Transcript quirks** specific to this show.
- **What the attribution check looks like here**, with real observed examples.

---

## 4. Hand-write one or two reference notes

Do this yourself, slowly, reading the transcript closely, and check the result
against the transcript twice. Then list them in the profile with a sentence each
on what they demonstrate, and name one as the benchmark.

This is the single highest-leverage step. Every agent reads the benchmark before
writing anything, so a weak reference note propagates into every note that
follows. A strong one is worth more than any amount of specification prose.

---

## 5. Scale up

```bash
python run.py brief <show>
```

Paste the brief into an agent. Three episodes per agent, mixed topics, strong
model. Then:

```bash
python run.py validate <show>
python run.py dedupe <show>
```

Have a **different** agent verify the notes than the one that wrote them.

---

## 6. Start the synthesis files

Create `podcasts/<show>/synthesis/` with `hindsight-seeds.md` and
`archive-caveats.md`, even if they start nearly empty. Cross-episode
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
