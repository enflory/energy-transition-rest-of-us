# The Energy Transition for the Rest of Us

Plain-language notes on the energy transition, built from primary sources.

This repository reads energy podcasts closely and writes down what they
actually said: one structured note per episode, accurate enough to quote in a
meeting, written for someone smart who does not work in energy.

It is both an archive and a pipeline. The notes are the product. The scripts,
the specification and the verification process are here so that the notes are
reproducible rather than merely asserted.

---

## Why

There is a great deal of excellent primary-source material about the energy
transition, mostly in long-form interviews with the people actually building
the system. It is also eight hours a month, and almost none of it is in a form
you can hand to a colleague who asked a reasonable question in a meeting.

The usual fix is a summary, and the usual summary fails in a specific way: it
produces a pile of individually true facts that lose the argument. You come
away knowing several things and unable to say why any of them matter.

So the unit here is not a summary. It is a **note with a thesis**, built to a
specification that makes the failure modes explicit and testable.

---

## What is in it

| | |
|---|---|
| Shows covered | 1 (Catalyst), 1 scaffolded (Critical Capital) |
| Episodes with notes | 125 |
| Note text | ~255,000 words |
| Median note | ~2,000 words |
| Span | 2022-11 to 2026-09 |

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
  PIPELINE.md           how an episode becomes a note, end to end
  ADDING-A-PODCAST.md   how to add a second, third, fourth show
podcasts/
  catalyst/
    podcast.json        scraper config: sitemaps, URL filter, corrections
    SHOW-PROFILE.md     this show's disclosure norms, quirks, reference notes
    manifest.csv        every episode ever seen, and its status
    episodes/
      2026-09-10-do-data-centers-really-increase-electricity-prices/
        transcript.md   not committed; regenerate with a fetch
        note.md         committed
    synthesis/
      hindsight-seeds.md    cross-episode threads, for later writing
      archive-caveats.md    data-quality facts about the corpus itself
  critical-capital/     scaffolded, not yet populated
scripts/                scrape, validate, dedupe, stats, new-episode detection
run.py                  task runner
```

Show-specific facts live in `podcast.json` and `SHOW-PROFILE.md`. Nothing about
any particular podcast is hard-coded into the scripts or the spec, which is
what makes adding a second show cheap.

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

That check earns its place. In one independent verification pass over 24 notes,
it found a host's opinion promoted into an expert's testimony, a cost figure
restated on air off by a factor of a hundred, and a guest's ranking attributed
to him that he had never made.

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

Recorded in full in each show's `synthesis/archive-caveats.md`. The three that
would bite a careless reader:

- **One Catalyst episode is published twice**, eleven months apart under
  different titles. Both notes are kept because they differ in substance, but
  it is one conversation, and any count must treat it as one.
- **A published date is not always a recording date.** At least two episodes
  are a rerun or a delayed release, so anything ordered by date needs checking.
- **Show notes sometimes contradict the transcript.** Several figures appear
  only in the marketing blurb and are demonstrably wrong. Notes are written from
  the conversation, never from the blurb.

---

## Adding another podcast

See `docs/ADDING-A-PODCAST.md`. The short version: create a directory under
`podcasts/`, write a `podcast.json` with the publisher's sitemaps and a URL
filter, fetch a few episodes, read them, fill in the `SHOW-PROFILE.md`, and
hand-write one or two notes as reference examples before scaling up.

Verified and ready to add from the same publisher: `open-circuit-` (67
episodes) and `green-blueprint-` (30).

---

## License

Code is MIT. The notes and synthesis are original work, licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use them, quote
them, build on them, with attribution.

Transcripts are not included and remain the property of their publishers.
Nothing here is affiliated with or endorsed by Latitude Media.
