# The Energy Transition for the Rest of Us

Plain-language notes on the energy transition, built from primary sources.

This repository reads energy podcasts and newsletters closely and writes down
what they actually said: one structured note per episode or post, accurate
enough to quote in a meeting, written for someone smart who does not work in
energy.

It is both an archive and a pipeline. The notes are the product. The scripts,
the specification and the verification process are here so that the notes are
reproducible rather than merely asserted.

**Read them at [energy.lonelymtnlabs.com](https://energy.lonelymtnlabs.com)**,
which is built from this repository on every push to `main`. Browse by source,
by episode, or by thread, or search all of them at once.

---

## Why

There is a great deal of excellent primary-source material about the energy
transition, mostly in long-form interviews with the people actually building
the system, and in newsletters written by people close to it. It is also eight
hours a month plus a reading list, and almost none of it is in a form you can
hand to a colleague who asked a reasonable question in a meeting.

The usual fix is a summary, and the usual summary fails in a specific way: it
produces a pile of individually true facts that lose the argument. You come
away knowing several things and unable to say why any of them matter.

So the unit here is not a summary. It is a **note with a thesis**, built to a
specification that makes the failure modes explicit and testable.

---

## What is in it

As of 2026-09-24:

| | Catalyst | Critical Capital | Steel For Fuel | Total |
|---|---|---|---|---|
| Content type | podcast | podcast | essay | |
| Items with notes | 126 | 11 | 56 | **193** |
| Items awaiting notes | 0 | 0 | 0 | **0** |
| Note text | ~256,000 words | ~25,000 words | ~78,000 words | **~359,000 words** |
| Median note | 1,998 words | 2,254 words | 1,560 words | |
| Span | 2022-11 to 2026-09 | 2026-04 to 2026-09 | 2023-03 to 2026-09 | |

Every transcript and essay the publishers have released has a note. Note lengths are not comparable across content types, because essay notes
are sized against their source: Steel For Fuel's range from about 400 to 2,500
words.

Counted as unique conversations and essays rather than items, the total is 192:
one Catalyst episode is published twice, eleven months apart under different titles.

---

## What a note looks like

Every note has the same seven sections, in the same order:

| Section | What it is for |
|---|---|
| **The question** | One line. The question the episode is organized around. |
| **The answer** | One to three sentences. What the episode actually concludes. If the answer is "it depends," what it depends on. |
| **The argument** | Two to four paragraphs of prose, **never bullets**. The reasoning, including wherever it turns. |
| **What you need to know first** | The two to four terms the argument depends on, in plain language. |
| **Details worth keeping** | Discrete facts and examples that support the episode but are not its spine. |
| **Claims worth citing** | Specific numbers, each attributed to whoever said it, date-stamped. |
| **Where it's contested** | Disagreements, hedges, uncertainty, and where the host pushed back. |

Two of those deserve explanation.

**The argument is prose because arguments live in their connectives.** "But,"
"which means," "only if," "the catch is." Bullet points cannot hold those
words. Converting that section to a list destroys the thing the note exists to
carry, so the validator rejects bullets there.

**"Where it's contested" is not padding.** Flattening a hedge into a confident
assertion is the single most likely way a note misrepresents its source.
Guests qualify heavily, and a note that drops the qualifiers reads cleaner while
being less true.

Frontmatter carries an `age_warning:` when an episode's specifics are likely
superseded, and a `disclosure:` when a speaker states a financial interest.

---

## Layout

```
docs/
  NOTE-SPEC.md          the specification every note is written to
  PIPELINE.md           how an item becomes a note, end to end
  ADDING-A-SOURCE.md    how to add another podcast or newsletter
sources/
  catalyst/                     a podcast source
    source.json         scraper config: sitemaps, URL filter, corrections
    SOURCE-PROFILE.md   this source's disclosure norms, quirks, reference notes
    manifest.csv        every item ever seen, and its status
    episodes/
      2026-09-10-do-data-centers-really-increase-electricity-prices/
        transcript.md   not committed; regenerate with a fetch
        note.md         committed
    synthesis/
      hindsight-seeds.md    cross-item threads, for later writing
      archive-caveats.md    data-quality facts about the corpus itself
  critical-capital/     same layout, 11 notes
  steel-for-fuel/               an essay source, 56 notes
    source.json         content_type: essay
    posts/
      2026-09-21-for-ai-energy-is-nothing-and-energy-is-everything-reprise/
        essay.md        not committed; regenerate with a fetch
        note.md         committed
scripts/
  archive.py            what differs between a podcast and an essay; nothing else knows
  scrape.py             fetch and parse, both content types
  validate_notes.py     structural check
  dedupe_check.py  stats.py  new_episodes.py
reader/
  build.py              builds the reading site from the notes (stdlib only)
  static/               its stylesheet, script and icon
.github/workflows/
  reader.yml            publishes the site to GitHub Pages on push to main
run.py                  task runner
```

Source-specific facts live in `source.json` and `SOURCE-PROFILE.md`. Nothing about
any particular source is hard-coded into the scripts or the spec, which is
what makes adding a second show cheap.

The second show tested that claim harder than expected. Critical Capital is a
Latitude Media programme whose transcripts Latitude does not publish; they come
from Crux, its co-producer, on an entirely different content management system.
Different listing pages, different title format, no publication-date metadata,
and the transcript buried in a page that also renders its navigation menu and
footer as body text. All of it turned out to be expressible as configuration.
No code in `scripts/` knows which show it is working on.

---

## Quickstart

Requires Python 3.9+. No dependencies, no install; everything uses the standard
library.

```bash
git clone https://github.com/enflory/energy-transition-rest-of-us
cd energy-transition-rest-of-us

python run.py                      # what needs doing right now
python run.py fetch catalyst       # rebuild transcripts from the publisher
python run.py validate             # structural check on every note
python run.py stats                # archive size and coverage
```

The notes are readable immediately. The fetch is only needed if you want the
transcripts alongside them.

---

## When a new episode drops

This is the loop the repository is built around. It is three commands and one
paste.

**1. See what is new.**

```bash
python run.py
```

Reads the publisher's sitemap and compares it against what is on disk. It
distinguishes three states: never seen, seen but the publisher ships no
transcript, and scraped but not yet written up. In the steady state it prints
`every transcript has a note. Nothing to do.`

**2. Fetch it.**

```bash
python run.py fetch catalyst
```

Scrapes only what is missing, one second between requests. Existing transcripts
are untouched unless you pass `refetch`.

**3. Get the brief.**

```bash
python run.py brief catalyst
```

Prints a ready-to-paste block naming the exact episodes, the files to read, the
constraints, and the verification checks. Paste it into Claude Code (or any
capable agent) and let it write the notes. Use a strong model; the work is
judgment about what matters in a conversation, not summarization.

**4. Check and commit.**

```bash
python run.py validate catalyst
python run.py dedupe catalyst        # occasionally; catches republished episodes
git add -A && git commit -m "notes: <episode title>"
```

The whole loop is a few minutes of your attention plus the agent's runtime.

---

## How the notes are kept honest

Structure is checked mechanically. Accuracy is checked by re-reading. Both
matter, and neither substitutes for the other.

**The validator** (`python run.py validate`) catches what would otherwise hide
inside a large batch: missing or out-of-order sections, thread tags invented
outside the controlled vocabulary, bulleted argument sections, claims with no
attribution, missing date stamps, placeholder text, and cross-episode leakage.
It reads the controlled vocabulary out of the spec, so the two cannot drift
apart.

It is deliberately not a style cop. Its word-count warning says so in its own
output: the ceiling is advisory, and trimming a note down to clear it is itself
a failure, because the first thing cut under length pressure is always a
speaker's hedge.

**Three verification checks** are run against the transcript before a note is
saved, and they catch different failures:

1. **Fact check.** Every number, name and claim confirmed against the
   transcript, with particular attention to qualifiers that got dropped and
   figures that lost the condition attached to them.
2. **Forest test.** Reading only the note, can you state the central question,
   the answer, the main reason, and the strongest objection? A pile of accurate
   facts with no thesis has failed.
3. **Attribution check.** The subtle one. Three things pull a note off course:
   the episode **title**, which absorbs causation the guest spread across
   several factors; the **host's framing**, which states the premise before the
   guest speaks and is not always faithful when it restates; and **your own
   compression**, where the hedge is the first thing to fall out because it
   reads as clutter.

The governing rule for the third: **where the host's framing and the guest's
own words diverge, the guest governs, and silence is not agreement.** A guest
who does not correct a host may be being polite, may not have caught it, or may
be mid-thought. An uncorrected restatement never becomes a claim the guest
endorsed.

That check earns its place. One independent pass over 24 notes found a host's
opinion promoted into an expert's testimony, a cost figure restated on air off
by a factor of a hundred, and a guest's ranking attributed to him that he had
never made.

A later pass over 11 notes found, among others, a tariff ladder recorded as
matched at every step when the point of the passage was that the last step went
unmatched; a concession reversed, so the host's "I take the point" became the
guest's; eleven named companies and agencies erased from a single note,
including from its most citable claim; and a date imported from a different
episode's transcript into the very bullet flagging a dating problem.

A third pass, over the 54 Steel For Fuel notes, made 195 corrections. The worst
was a note whose answer inverted its essay's conclusion: the post argues that
without a paradigm shift, human-level AI would probably break the energy system,
and the note answered "probably not". Others included a definition that made its
own post incoherent, a drawback the essay listed among its reasons for
excitement recorded as a limitation, and three true facts imported from outside
the document.

**Verification is done by an agent that did not write the note.** That is the
part that matters. In the first two rounds the writers had reviewed their own
work and reported it clean, and every error found in those rounds survived that
review.

---

## What is deliberately not here

**Transcripts are not committed.** They are the publisher's copyrighted
content. This repository holds original work derived from them and points at
the source. `python run.py fetch <show>` rebuilds them in minutes.

That is also better engineering. A committed transcript is a snapshot nobody
re-runs, so a broken scraper goes unnoticed. A regenerated one proves the
pipeline still works every time somebody uses it.

**Cross-episode claims are not in the notes.** Each note is written from one
episode, with no hindsight and no outside knowledge used to correct a claim.
That keeps every note independently trustworthy and lets them be written in
parallel. Material that spans episodes lives in `synthesis/`.

---

## Caveats worth knowing

Recorded in full in each source's `synthesis/archive-caveats.md`. The ones that
would bite a careless reader:

- **One Catalyst episode is published twice**, eleven months apart under
  different titles. Both notes are kept because they differ in substance, but
  it is one conversation, and any count must treat it as one.
- **A published date is not always a recording date.** At least two episodes
  are a rerun or a delayed release, so anything ordered by date needs checking.
- **Show notes sometimes contradict the transcript.** Several figures appear
  only in the marketing blurb and are demonstrably wrong. In one case the blurb
  presents a headline figure as the guest's own finding when he credits it on
  air to a named outside researcher. Notes are written from the conversation,
  never from the blurb.
- **The sources are different kinds of evidence.** Catalyst mostly interviews
  analysts and researchers, and the host argues with them. Critical Capital
  mostly interviews founders and investors about the category they personally
  sell into, and the host builds on their answers rather than testing them.
  Steel For Fuel is one investor's own written argument, with no interlocutor
  at all. All three are legitimate; blending them without marking which is
  which would silently upgrade a founder's plan, or an essayist's stated bet,
  into a finding.
- **Charts do not survive the pipeline.** It is text-only. That costs nothing
  on the podcasts and costs real content on an essay source: Steel For Fuel
  carries 524 figures across 56 posts, half of them uncaptioned. The scraper
  records each figure's position and URL so the gap is visible rather than
  silent, and notes say so where an argument rests on one.

---

## Adding another source

See `docs/ADDING-A-SOURCE.md`. The short version: decide the content type, find
out who actually publishes the text, create a directory under `sources/`, write
a `source.json`, fetch a few items, read them, fill in the
`SOURCE-PROFILE.md`, and hand-write one or two notes as reference examples
before scaling up.

**Two content types.** `podcast` for conversations with transcripts and `essay`
for written pieces. The test is not what the publisher calls itself but whether
the document has speaker labels: the podcast parser finds a transcript by
locating the first `Name:` paragraph, so pointed at a newsletter it produces a
clean run in which every page is logged as having no transcript.

**Step zero is not optional.** The network that publishes a show does not
necessarily publish its transcripts, and the obvious sitemap can be both
incomplete and stale. Latitude carried 2 of Critical Capital's 12 episodes and
no transcript text at all. Crux's own sitemap listed 11 of 12, and the one it
omitted was the newest, which is the only one a routine check is looking for.
Both failure modes are silent. Five minutes of checking up front avoids an
archive that quietly stops updating.

Verified as publishing full transcripts on Latitude, and ready to add:
`open-circuit-` (67 episodes) and `green-blueprint-` (30).

---

## License

Code is MIT. The notes and synthesis are original work, licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use them, quote
them, build on them, with attribution.

Transcripts are not included and remain the property of their publishers.
Nothing here is affiliated with or endorsed by Latitude Media.
