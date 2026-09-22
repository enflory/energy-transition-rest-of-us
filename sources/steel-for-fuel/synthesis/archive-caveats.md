# Archive caveats: Steel For Fuel

Facts about this corpus as a corpus, as distinct from what any post says. Read
this before counting anything or ordering anything by date.

Window: the whole archive, 2023-03-31 to 2026-09-21, as fetched on 2026-09-21.

---

## Counts

- **57 pages published. 56 essays.** The 57th, `Coming soon` (2023-03-23), is
  the placeholder Substack shows before a publication's first real post; its
  entire body is the sentence "This is Steel For Fuel." It is recorded in the
  manifest as `no essay` and correctly produces no note.
- **Posts total about 160,000 words**, median 2,349. That is roughly the size
  of the Critical Capital transcript archive spread over four and a half times
  as many items.
- **Cadence is irregular.** 12 posts in 2023, 19 in 2024, 16 in 2025, 9 through
  2026-09-21. Do not read a gap as a hiatus; the publication has never kept a
  fixed schedule.

---

## Length varies more than anywhere else in this repository

Posts run from **248 to 11,869 words**. Eleven are under 900 words, which is
the floor the podcast note band uses, and thirteen are over 4,000.

This is why essay notes are sized against their source rather than against a
fixed target. A 300-word note on a 400-word post is correct here and would be a
failure on Catalyst. Any statistic comparing note lengths across sources has to
say which content type it is counting, or it is comparing two different things.

---

## Two posts share a title, and they are not duplicates

`2024-11-20` "For AI, energy is nothing, and energy is everything" and
`2026-09-21` the same title marked "(reprise)".

They share **no identical paragraph**. The later post quotes the earlier one at
length and then revises it, which is a different relationship from the Catalyst
rerun, where one conversation was published twice. Both deserve notes, and a
count of distinct arguments here is 56, not 55.

---

## Both duplicate-checker hits are self-revisiting, not republication

`python run.py dedupe steel-for-fuel` reports two pairs, and the same post is
one half of each:

| overlap | pair |
|---|---|
| 52% | `2025-05-28-an-ode-to-physical-ai` and `2026-03-13-the-robots-are-coming` |
| 28% | `2025-07-16-on-linemen-robots-hands-and-brains` and `2026-03-13-the-robots-are-coming` |

`2026-03-13` "The robots are coming" is a synthesis of the author's own two
earlier robotics posts. It opens by naming the first of them, "Around this time
last year I wrote 'An Ode to Physical AI'", and block-quotes about six
paragraphs in the course of the piece.

It is reuse, not republication. All three posts are separate arguments and all
three should get notes. **Do not read the two earlier posts while writing the
note on the later one**, however tempting: the single-item rule binds here
exactly as it does for the reprise.

Expect more hits of this shape as the archive grows, because this author
revisits himself deliberately. Both pairs checked and dismissed on 2026-09-21.

---

## The byline does not always name the author of the argument

This is the corpus-level version of the quirk in `SOURCE-PROFILE.md`, and it
matters for any count of who wrote what.

- **1 post is bylined to someone else**: `2025-06-30` "Full Steam Ahead", by
  Addison Stark, CEO of AtmosZero. The frontmatter `author` field is correct.
  It carries no handover marker and never returns to Lubershane, and it closes
  with an ASME notice saying it first appeared in *Mechanical Engineering*,
  July 2025.
- **3 more are bylined to Lubershane while carrying substantial guest-written
  text**: `2026-04-08` "Duration is all you need" is almost entirely Ben
  Haley's essay, cross-posted from Evolved Energy Research; `2026-07-06` "Data
  centers need the grid" is almost entirely Tim Hade's, cross-posted from his
  personal blog; and `2026-09-21` hands its middle section to Hans Royal. For
  these the frontmatter `author` field is **wrong about the body**, because it
  records the Substack byline.

So: `author` in the document frontmatter is the byline, not an assertion about
authorship of the argument. Do not aggregate on it without reading.

**The notes follow the byline too, deliberately.** A note's `author:` records
what the byline says; guest authorship of the argument is carried in the prose
and in the per-claim attributions instead. That is what the hand-written
benchmark note does for `2026-09-21`, where two thirds of the post is Royal's,
and the other cross-posts were brought into line with it on 2026-09-22. A field
that sometimes means byline and sometimes means author-of-the-argument can be
aggregated on by neither.

**A note on a cross-post must never say "the author" unqualified.** This is the
corollary of the convention above and it was caught in verification, not in
writing. With `author:` reading Lubershane on `2026-07-06`, a contested-section
bullet headed "The author has a commercial stake in the answer" pointed at the
wrong man: the stake is Tim Hade's. Name whoever is meant.

**"Back to Andy:" is not a reliable handover marker.** Where it appears it is
load-bearing, as `SOURCE-PROFILE.md` says. But two of the four guest posts do
not carry it at all: `2025-06-30` and `2026-07-06` hand over and never return,
the latter at "Without further ado, here's Tim:". Absence of the marker means
either no guest section or one that runs to the end of the post, so it cannot
be used as a test for either.

---

## Quoted voice is not reliably marked, and the frontmatter count is not a test

This is the most consequential thing found while writing the 2026-09-22 batch,
because quoted voice is the attribution risk this source is graded on.

`SOURCE-PROFILE.md` says the scraper preserves block quotes as Markdown `> `
lines, and `CLAUDE.md` tells a verifier to check every `> ` block against the
note. Both are true as far as they go, and both under-detect. Across the 54
posts written that day, quoted material appeared in five renderings:

| rendering | example |
|---|---|
| `> ` block quote | `2026-06-18`, five Keynes passages |
| ordinary paragraph in curly quotes | `2024-10-02`, Churchill, Noah Smith, and a long Kapsis and Sachse passage carrying the fund counts |
| `#####` heading | `2023-12-21`, four paragraphs of Gas Technology Institute copy |
| `###`/`####` heading | `2025-04-07`, three executives; `2025-07-07`, Tu Le |
| no marker at all | `2023-10-01`, a passage introduced only by "As I wrote in a prior post on heating decarbonization" |

The sharpest case is `2026-06-18`, which marks five Keynes quotations with
`> ` and then renders two more as plain paragraphs introduced by "He said:".
The marker is unreliable **within a single document where it demonstrably
works**.

`quoted_paragraphs` in the document frontmatter counts only the `> ` form. It
reads 0 for posts containing six distinct quoted passages, so a zero there
means nothing at all.

**What to do instead:** read the introducing sentence. On this source the
reliable signal is the prose that hands off ("Per Google:", "Quoting myself:",
"As I wrote", "here's Tim:"), not the punctuation that follows it.

---

## Substack link-cards to other posts appear mid-body and read as prose

The scraper's `content_end` anchor trims the page furniture below
`post-footer`, and the `boilerplate` patterns catch the subscribe pitches. What
survives is the embedded card Substack renders when a post links to another
post: an `###` heading with the other post's title and a teaser line from it,
sitting inside the body.

Six of the 54 posts written on 2026-09-22 carried one. They are furniture, not
argument, and one is actively misleading: the card in `2025-04-07` carries the
line "Today's charts come from two of our portfolio companies", which is true
of the linked post and false of the post it appears in, whose charts are the
IEA's and the Federal Reserve's. Another, in `2025-04-17`, carries a quoted
sentence the host post never attributes to anyone.

Treat an `###` heading that reproduces another post's title as the start of a
card, and read nothing after it as the present post's claim.

---

## Figures are lost, and half of them were never labelled

524 figures across 56 posts, of which **266 carry a caption** and 258 render as
`[FIGURE: no caption in source]`. Twenty posts have ten or more; one has forty.

The pipeline is text-only, so no chart is readable from the archive. The
scraper records each figure's position and original URL so the gap is visible
rather than silent, but any claim of the form "the archive contains Lubershane's
data on X" is false where X was only ever a chart. Notes say so where the
argument depends on one.

---

## Nothing here is paywalled

Checked 2026-09-21: the publication has `payments_state: disabled` and all 57
posts report `audience: everyone`. No session cookie is needed and none should
be added. If that changes, the scraper will start saving truncated posts rather
than failing, so a sudden drop in word counts is the symptom to watch for.
