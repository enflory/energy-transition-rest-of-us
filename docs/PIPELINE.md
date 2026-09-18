# The pipeline

How a published episode becomes a note, and why each stage works the way it
does. Most of the design here is a response to something that went wrong.

---

## Overview

```
publisher sitemap
      |
      |  scripts/scrape.py      config: podcasts/<show>/podcast.json
      v
podcasts/<show>/episodes/<date>-<slug>/transcript.md   (not committed)
podcasts/<show>/manifest.csv                            (committed)
      |
      |  an agent, working to docs/NOTE-SPEC.md + the show profile
      v
podcasts/<show>/episodes/<date>-<slug>/note.md          (committed)
      |
      |  scripts/validate_notes.py   structure
      |  three verification checks   accuracy
      v
podcasts/<show>/synthesis/                              (cross-episode work)
```

---

## Stage 1: discovery

`scripts/scrape.py` reads every configured source and keeps URLs containing the
show's `url_filter`. Nothing about any show is hard-coded; it all comes from
`podcast.json`.

Discovery is separated from fetching because the useful daily question is "is
there anything new?", not "re-download everything." `scripts/new_episodes.py`
answers it without writing anything.

**Two sources, unioned, because a sitemap is not a contract.** The obvious
source is the publisher's sitemap, and for Catalyst it is sufficient. It was not
for Critical Capital. On 2026-09-18 the Crux sitemap listed 11 of that show's 12
episodes, and the one it omitted was the newest, published three days earlier.
A scraper reading only the sitemap would have reported "nothing new" for exactly
the episode the daily check exists to find, and would have kept doing so.

So a show can also declare `index_pages`, its own episode listing, which the
scraper walks page by page following a configured "next" link. Results from both
sources are unioned. The sitemap is cheap and usually complete; the listing is
never stale, because it is the page the publisher updates to announce an
episode. Running both costs two extra requests and removes a failure mode that
is silent by construction.

**The publisher of a show is not always the publisher of its transcripts.**
Critical Capital is a Latitude Media show whose transcripts Latitude does not
publish. They come from Crux, its co-producer, on an entirely different CMS.
Everything that differs between the two sites is configuration: which pages list
the episodes, what the title suffix is, where the date is and in what format,
and which region of the page holds the content. No code is show-aware.

**Three states, not two.** A URL is one of: never seen; seen but the publisher
ships no transcript for it; or scraped. That middle state is real, and on
Catalyst it covers 21 of 146 pages, which publish show notes only. Without the
distinction they reappear as pending work on every run forever. The manifest is
what carries it, which is why the manifest is committed and the transcripts are
not.

---

## Stage 2: fetch and parse

One second between requests. Already-saved episodes are skipped unless you pass
`refetch`.

Parsing is where the interesting bugs were.

**The content region is narrowed before anything else.** Site templates put
navigation menus, inline CSS blocks, author bios, related-episode cards and the
footer into `<p>` elements on the same page as the transcript. A show can
declare `content_start` and `content_end` regexes bounding the part of the page
that is actually the episode, and everything outside is discarded before a
single paragraph is read. This is strictly better than enumerating each piece of
furniture as boilerplate: it is one rule instead of eight, and it keeps working
when the footer changes. Both anchors print a warning and fall back to the whole
page if they stop matching, so a template change surfaces instead of silently
corrupting a transcript.

**Zero-width characters are stripped.** Some content management systems emit a
zero-width joiner immediately before a speaker label. It is invisible in every
viewer, and it makes the paragraph fail the speaker-label regex, so the line
drops out of the dialogue for no visible reason. Removing them is normalization
rather than editing: they carry no meaning and there is no rendering in which
they matter.

**Boilerplate is filtered before the transcript start is located.** A transcript
paragraph opens with a speaker label, matched with a regex on the shape
`Name Name:`. Sponsor and credits blocks also open that way, so a line like
`Credits:` matched the speaker pattern and anchored the transcript start too
early, pulling sponsor copy into the dialogue as though a person had said it.
Filtering boilerplate first fixes it. The ordering is load-bearing; do not
reverse it.

**Some labels look like speakers and are not.** `Tag:` is the show's intro
bumper and appeared in 48 Catalyst episodes before it was caught. The
`non_speakers` list in `podcast.json` holds these.

**Corrections are declared, applied document-wide, and counted.** Publishers
misspell names consistently; Catalyst's host is usually rendered phonetically.
Each correction is a pattern, a replacement and a human-readable note, and every
transcript's frontmatter records how many times each fired. Nothing is silently
edited. Keep this list minimal: a correction edits the source text, so it should
only ever cover a demonstrated, repeated publisher error, never a judgment call.

**The manifest merges rather than overwrites.** A partial run must not drop
episodes it did not touch. Precedence is previous manifest, then this run, then
the archive on disk, which is authoritative for anything actually saved. An
earlier version rewrote the file wholesale and a partial run cut it from 146
rows to 48.

---

## Stage 3: writing the note

An agent reads the specification, the show profile, two reference notes, and
then the transcript in full. It writes one note. It does not read other
episodes.

That isolation is deliberate and has two payoffs. Each note is independently
trustworthy, and the work parallelizes with no shared state, so eight agents can
run at once. The cost is that nothing cross-episode can be said in a note, which
is why `synthesis/` exists.

`python run.py brief <show>` prints the exact brief to use. It encodes decisions
that took a while to learn, including the constraints, the file list and the
verification checks.

---

## Stage 4: checking

Two different things, neither substituting for the other.

**Structure, mechanically.** `scripts/validate_notes.py` catches what hides in a
large batch: missing or out-of-order sections, invented thread tags, bulleted
argument sections, unattributed claims, missing date stamps, placeholders,
cross-episode leakage. It parses the controlled vocabulary out of the spec so
the two cannot drift.

Two bugs in the validator itself are worth knowing about, because both made it
worse than useless for a while:

- It checked for a trailing attribution per physical line, but bullets wrap, so
  it flagged every note in the archive as unattributed. A validator that cries
  wolf on everything gets ignored, which is more dangerous than no validator.
  It now rejoins each logical bullet first.
- It read a sentence beginning "2030." as an ordered-list item, so agents
  reworded correct prose to satisfy it. The list-marker pattern now requires one
  or two digits.

**Accuracy, by re-reading.** Three checks against the transcript: a fact check,
a forest test, and an attribution check. `docs/NOTE-SPEC.md` describes them in
full. They catch different failures, and passing one says nothing about the
others.

Verification is best done by an agent that did not write the note. Over 24
unverified notes, an independent pass produced roughly 100 corrections,
including a guest's position reversed, a host's opinion promoted into an
expert's testimony, and several hedges quietly firmed into assertions.

---

## Stage 5: synthesis

Two files per show, both written by hand:

- **`synthesis/hindsight-seeds.md`** — cross-episode threads worth writing
  about later, each with its supporting episodes and a caution against
  overreach.
- **`synthesis/archive-caveats.md`** — data-quality facts about the corpus
  itself, as distinct from its content. Reruns, delayed releases, show notes
  that contradict transcripts, vocabulary decisions.

`scripts/dedupe_check.py` supports the second. It compares 5-gram sets of every
transcript pair by containment, which catches a short episode nested inside a
longer one. It found one Catalyst conversation published twice, eleven months
apart under different slugs, at 99% overlap. Nothing in the filenames or
frontmatter revealed it.

An earlier version of that script sampled shingles to build candidate pairs
before comparing, and missed that genuine pair because the sampled collisions
landed just under its cutoff. It now compares exactly, which takes about a
second for 125 transcripts. A correctness check that sometimes misses is worse
than no check.

---

## Design principles

**The specification is the load-bearing artifact.** Agents are capable and
inconsistent. A precise, testable spec is what makes 125 notes read as though
one person wrote them. When note quality drifts, fix the spec, not the note.

**Put guidance where the decision happens.** Agents read the spec once at the
start and the validator's output at the moment they act. The word-count warning
argues its own case in its message text because a paragraph in the spec was not
reaching the moment of choice.

**Record ambiguity rather than resolving it.** Transcripts are
machine-generated and garble numbers, names and units. A note saying "he puts it
around 6% but the base is unclear" is more useful than a confident 6%. Silent
resolution is how a transcription artifact becomes a fact someone repeats.

**Prefer regenerating to committing.** Transcripts rebuild from the publisher.
That keeps the repository free of someone else's content and keeps the scraper
honest, because a broken scraper is discovered the next time anyone fetches.
