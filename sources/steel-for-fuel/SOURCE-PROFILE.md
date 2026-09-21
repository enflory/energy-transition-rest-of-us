# Source profile: Steel For Fuel

Read this alongside `docs/NOTE-SPEC.md`, and read the **Notes on an essay**
section of that spec closely. The spec is the portable part; this file is
everything true of Steel For Fuel specifically.

This is the archive's first essay source. If you have written notes here
before only for Catalyst or Critical Capital, the habits transfer less well
than you would expect. The section on attribution at the bottom is the part to
read twice.

---

## The source

Steel For Fuel is **Andy Lubershane's** Substack. He describes himself on the
publication's about page as "Partner and Head of Research at Energy Impact
Partners," working with a consortium of strategic limited partners to invest in
energy-transition technology, and says he lives in South Portland, Maine.

The title is explained on the same page: "Steel For Fuel" is displacing fossil
fuel emissions with the steel in wind turbine towers, solar panels, nuclear
reactors and other lower-carbon generation.

The archive here holds **56 essays spanning 2023-03-31 to 2026-09-21**, plus
one placeholder page with no essay. Cadence is irregular and roughly monthly:
12 posts in 2023, 19 in 2024, 16 in 2025 and 9 through late September 2026.
Nothing is paywalled; the publication has payments disabled entirely.

**Length varies more than anything else in this repository.** Posts run from
248 words to 11,869, with a median of 2,349 and a total of about 160,000.
Eleven are under 900 words. This is why essay notes are sized against their
source rather than against a fixed target, and why a short note here is a
correct note rather than a lazy one. See the spec.

**Format.** Continuous prose, usually without subheadings; where they appear
they are rendered `####` or `#####`. Long posts sometimes carry numbered
footnotes as `#####` headings at the foot. There is no standard opening or
closing, no interviewer and no second voice unless the post is a guest post.

---

## The thing that makes this source different from the podcasts

**There is no interlocutor.** Catalyst has a host who pushes back; Critical
Capital has one who builds on the answers. Here there is one person making an
argument they have had time to edit. Nobody interrupts, nobody asks for a
number, and nothing is extemporaneous.

Three consequences, and they are the main thing to get right:

1. **The prose is already compressed.** A transcript has slack in it: false
   starts, restatements, a guest circling a point three times. An essay does
   not. Cutting a sentence usually costs a step of the argument rather than
   removing a repetition. Notes here should be shorter than podcast notes, and
   they should be shorter by quoting less and connecting more.

2. **"Where it's contested" nearly always means something other than
   disagreement.** Use it for the author's own hedges, which are frequent and
   carefully placed; for the places he revises himself; for the assumption the
   argument rests on and never defends; and for what he has at stake. The spec
   lists these in order. Manufacturing a dispute is worse than reporting that
   there was none.

3. **The hedges are the most valuable sentences in the piece.** Lubershane
   marks his confidence deliberately: "in my opinion," "I'm somewhat skeptical,"
   "I'm not so sure," "fair warning," "one important caveat." A note that
   flattens those reads more authoritative than the post and is less true than
   it. Keep them.

---

## Disclosures

Lubershane is a working investor writing about the sector he invests in. **This
is normal, he is consistently open about it, and it is not a red flag.** He
names the relationship inline and unprompted: "Heron is a portfolio company at
Energy Impact Partners, where I work," "at my firm, Energy Impact Partners,
we've invested in one such set of solutions." Energy Impact Partners is named
in 35 of the 56 posts, and about 30 carry an explicit portfolio or investor
statement.

Because it is true of every post, **the standing affiliation does not belong in
`disclosure:`.** Put it in `author:` where the reader will look for it:

```yaml
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
```

Triggers for a `disclosure:` field, narrowly:

- The post's argument **turns on a company his firm has invested in**, and he
  says so. The narrow, legitimate point is the one the spec already makes: a
  named portfolio company's performance figures come from an interested party.
  State it once, factually.
- The post is a **guest post by someone at a portfolio company**. The
  2025-06-30 post is written by the CEO of AtmosZero and opens by stating that
  AtmosZero is an Energy Impact Partners portfolio company. That is a
  disclosure, and the post is also product advocacy by its author, which the
  note should say plainly and without insinuation.

Not triggers:

- A passing mention of EIP as the place he works.
- "At Energy Impact Partners, many of us have sorted ourselves into Team
  Ammonia and Team Methanol." That is colour, not an interest.
- The subscribe pitch.

---

## Quirks specific to this source

- **The byline is not always the author of the argument.** This is the most
  dangerous quirk here and it defeats the obvious check. The 2026-04-08 post
  "Duration is all you need" carries `author: "Andy Lubershane"` in its
  frontmatter, but the body is Ben Haley's essay, cross-posted from Evolved
  Energy Research, wrapped in a short Lubershane introduction and a closing
  "[Back to Andy: ...]". Only the prose tells you. Read the first two
  paragraphs of any post before deciding whose argument you are summarizing.
  - `2025-06-30` "Full Steam Ahead" is the opposite case and the easy one: the
    frontmatter correctly names Addison Stark, and the body opens with a
    bracketed note saying it is a guest post.
  - `2026-09-21` is bylined Lubershane and is mostly his, but hands a long
    middle section to a guest before returning at "Back to Andy:".
- **"Back to Andy:" is the handover marker** and it is load-bearing. The
  scraper deliberately does not strip it, even where the rest of that paragraph
  is a subscribe pitch, because it is the only thing marking where a guest's
  voice ends. Where you see it, everything above it back to the previous
  handover is someone else.
- **He quotes himself.** Ten posts contain block quotes, and the quoted
  material is often his own earlier writing, which the surrounding prose then
  updates or walks back. `2026-09-21` quotes his 2024 post and his own post
  from six weeks earlier. Attribute quoted text to the earlier piece and the
  revision to the present one. Never merge them.
  - Related: `2026-03-13` "The robots are coming" quotes about six paragraphs
    of his own `2025-07-16` post. The duplicate checker flags the pair at 28%
    overlap. It is self-quotation, not a republication, and both notes should
    be written.
- **Figures carry real argument, and half of them are bare.** There are 524
  figures across 56 posts, and only 266 carry a caption; the rest render as
  `[FIGURE: no caption in source]` with a URL. Some posts are chart-led: one
  has 40 figures against 128 paragraphs. Where the prose says "here's the
  index" or "as you can see above" and the number is only in the image, say in
  the note that the evidence sits in a figure. Do not infer it.
- **Two posts share a title.** `2024-11-20` "For AI, energy is nothing, and
  energy is everything" and `2026-09-21` the same title marked "(reprise)".
  They share no paragraph and are separate arguments; the later one quotes and
  revises the earlier. If you are writing one of them, you are not writing the
  other, and the single-item scope rule means you do not go and read the other
  to check.
- **Titles sometimes carried a by-line suffix** on the publisher's side. The
  scraper strips " - by <Name>" and " - Steel For Fuel"; if you see either in a
  note title, the suffix rule has drifted and should be reported rather than
  edited around.
- **Machine-transcription quirks do not apply here.** The text is written and
  edited, so a garbled phrase is not a transcription artifact. If something
  reads oddly, it is what he wrote. Quote it as-is and do not "correct" it.

---

## Reference examples

Two notes were written by hand against the essay. They are deliberately a long
post and a short one, because the two do not look alike and one benchmark would
not cover both. Read both before writing your first note for this source.

| Post folder | Why it is worth reading |
|---|---|
| `posts/2026-09-21-for-ai-energy-is-nothing-and-energy-is-everything-reprise` | **The benchmark.** Shows the three hardest things about this source at once: a block quote of his own earlier position that the post then revises, a long guest-written section ending at "Back to Andy:", and a central framework whose numbers live in a figure the note cannot see. Also shows "Where it's contested" written for a piece nobody contested. |
| `posts/2024-07-26-ai-versus-computing-efficiency` | A 377-word post. Shows what a compact note looks like: every section present, none padded, the argument carried in three sentences, and the note comfortably shorter than its source. |

---

## What the attribution check looks like on this source

Verification check 3 in the spec is general. Its specific shape here is **quoted
voice**, and it replaces the host's framing that the podcast profiles describe.

The failure mode: a note that reads as though Lubershane asserts, today, in his
own voice, something that the post attributes to someone else or to his earlier
self. It is easy to fall into because an essay has no speaker labels, and once
the `> ` markers are dropped from your reading the text is uniform.

The clearest observed case is `2026-09-21`. The post opens by quoting, at
length, his own 2024 framing: energy is a trivial share of the cost of
computing, so AI developers ought to pay a large premium for power. The post
then spends its remaining two thirds complicating that. A note written from the
quoted passage would report the 2024 position as the 2026 conclusion, and the
post exists to say something more careful than that.

Others to watch for:

- **The intro-to-a-guest-post problem.** Where Lubershane introduces someone
  else's essay, his framing of it is a recommendation, not a claim he has
  argued. `2026-04-08` calls the guest essay "the best wonky post on the
  techno-economics of the power system I've encountered in years." That is
  praise for a piece, and the note's argument section belongs to Ben Haley.
- **A firm's marketing inside a cross-post.** The closing paragraph of
  `2026-04-08` describes Evolved Energy Research's own modelling product. It is
  the firm's copy, not a finding of the essay.
- **Title gravity applies unchanged.** These titles are argumentative and often
  deliberately overstated. "Duration is all you need," "For AI, energy is
  nothing, and energy is everything," "The US is a natural gas superpower."
  Each post is more qualified than its title. Write from the body.

**Where the title, the quoted passage and the author's own present-tense prose
diverge, the present-tense prose governs.**
