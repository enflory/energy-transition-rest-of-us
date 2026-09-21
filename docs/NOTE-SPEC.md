# Note specification

**Version 1.6**

You are writing a single `note.md` for a single item, from its source
document. Read this whole file before starting. Reference examples are
listed at the bottom; read at least two before writing your first note.

The archive holds two kinds of source, and almost everything here applies to
both:

| content type | an item is | its document is | the note names |
|---|---|---|---|
| `podcast` | one episode | `transcript.md`, a conversation | `episode:` and `guest:` |
| `essay` | one post | `essay.md`, a written piece | `post:` and `author:` |

Where they differ, two sections near the end say so: **Notes on a podcast
episode** and **Notes on an essay**. Read the one that applies to your source,
in full. Your source profile says which content type you are working on, and
so does `content_type` in the document's own frontmatter.

The difference is smaller than it looks and larger than it sounds. The sections
are the same, the vocabulary is the same, and the verification checks are the
same three checks. What changes is where the misattribution risk lives: in a
conversation it is the gap between a host's framing and a guest's words, and in
an essay it is the gap between the author's voice and the voices they quote.

---

## Context

This repository turns podcast episodes and written essays about the energy
transition into structured, plain-language notes. You are writing one note for
one item.

**Source-specific context lives in `sources/<source>/SOURCE-PROFILE.md`**: who
makes it, what disclosures are normal for it, its particular quirks, and which
existing notes to read as worked examples. Read that file as well as this one
before you start. This spec is the portable part; the profile is the part that
changes per source.

The reader is a non-specialist who follows this space closely. He wants to
answer questions like "should I worry about AI's energy use?" accurately in a
meeting, without oversimplifying, and to build a newsletter from this material.

**Your note is infrastructure, not the final product.** A later synthesis layer
reads across all the notes to build cross-item threads and newsletter items.
That means two things: your note must be accurate enough to be trusted without
re-reading the source, and it must stay strictly within its own item
(see Scope below).

---

## Input and output

- **Read:** `sources/<source>/<episodes|posts>/<folder>/<transcript|essay>.md`
- **Write:** `sources/<source>/<episodes|posts>/<folder>/note.md`
- **Never modify** the source document, `manifest.csv`, `source.json`, this
  spec, anything in `scripts/`, or any other item's files.

Read the entire document before writing anything, and do not skim. How long it
runs, and which part of the page is marketing rather than content, differ by
content type; see the two sections near the end.

---

## Scope: single item only

Write only what this item supports. Do not:

- Reference other episodes or posts, even if the document mentions them.
- Add hindsight, "what happened since," or "read this alongside X."
- Bring in outside knowledge to correct, update or contextualize a claim.
- Speculate about how the topic developed after the publication date.

This rule has one consequence that surprises people, and it matters most for
essays. **An author revisiting their own earlier piece is still a single
item.** Write what this document says, including what it says about the earlier
one. Do not go and read the earlier post to check, fill in or correct it.

Cross-item synthesis happens in a later layer that reads all the notes at once.
If you add it here, it will be wrong, because you can only see one item.

If a claim looks dated or superseded, that is fine. Record it as stated, with
its date, and move on. The date stamp is how staleness gets handled.

---

## The format

Write exactly these sections, in this order, with these headings.

Three frontmatter fields are named for the content type. A podcast note opens:

```markdown
---
episode: "<exact title from the document frontmatter>"
published: "<YYYY-MM-DD>"
guest: "<Name, role, organization>"
threads: [<from the controlled vocabulary below>]
source_transcript: "transcript.md"
note_version: 1
---

## The question

## The answer

## The argument

## What you need to know first

## Details worth keeping

## Claims worth citing

## Where it's contested
```

An essay note is identical except for three field names:

```markdown
---
post: "<exact title from the document frontmatter>"
published: "<YYYY-MM-DD>"
author: "<Name, role, organization>"
threads: [<from the controlled vocabulary below>]
source_document: "essay.md"
note_version: 1
---
```

The seven `##` sections are the same for both, in the same order, with the same
headings. The validator will tell you if you have used the wrong set of field
names for your source.

Two optional frontmatter fields:

- `age_warning: "..."` when the item is more than about 18 months old and its
  specifics are likely superseded. One sentence.
- `disclosure: "..."` when a financial interest in the subject is stated, or the
  source profile's disclosure pattern applies. See Disclosures below.

Target 1,300 to 1,900 words total, and treat that as a guide rather than a
budget. Match the note to the material: a dense 8,000-word episode earns a longer
note than a 4,000-word one, and a genuinely short episode should get a short note
rather than padding. **For essays this target is replaced by one that scales
with the source; see Notes on an essay.**

**Stop trimming when further cuts would remove a citable figure, a reasoning turn
in the argument, or a speaker's qualifier.** Those three are worth more than
hitting a word count. Compression that costs a hedge is a bad trade.

The validator warns above 2,000 words. That warning is a smoke alarm, not a
budget, and it is the one warning you should be most willing to leave standing.
When a note runs over, ask what the excess actually *is*:

- Duplication between sections, restatement, or loose phrasing: cut it. This is
  the common case and the note gets better.
- Attributed figures, reasoning turns, or speakers' hedges: keep them, and let
  the warning stand. Say so in your report.

Survey episodes, meaning annual trends, ask-me-anything and multi-topic
roundups, almost always fall in the second case, because their claims section
*is* the content.

**Trimming down to the ceiling is itself a failure.** If your note lands at
1,998 words, the tool was steering and not the material. A note that genuinely
needed to be 2,300 words should be 2,300 words.

---

## Section by section

### The question

One line. The central question the episode is organized around. Hosts on these
shows usually state it explicitly in the opening monologue, and it is often
close to the episode title. Phrase it as a real question a person would ask.

### The answer

One to three sentences giving what the episode actually concludes. Not a topic
summary. If the answer is genuinely "it depends," say what it depends on. If the
episode does not reach a conclusion, say that plainly rather than manufacturing
one.

### The argument

**Two to four paragraphs of prose. Never bullets.** This is the most important
section and the one most likely to be done badly.

Carry the reasoning, including wherever it turns. Arguments live in their
connectives: "but," "which means," "only if," "the catch is." Bullet points
cannot hold those words, which is why this section is prose and why converting it
to a list destroys it.

A good test: after reading only this section, could someone explain *why* the
answer is the answer, and reconstruct the strongest objection to it? If they
would come away with a set of true statements that do not obviously connect, the
section has failed even if every sentence is accurate.

Where the episode sets up an intuition and then overturns it, preserve both
halves. The setup is not filler; the reversal is meaningless without it.

### What you need to know first

Two to four terms or concepts the *argument you just wrote* depends on, defined
in plain language. Write this section after the argument, not before, because you
cannot know which terms matter until the argument exists.

This is what lets the note stay technically honest for a non-expert. Rather than
simplifying a claim, define its terms and then state the claim at full strength.

Skip any term a general reader already knows. If the episode requires no special
vocabulary, keep the section short rather than padding it.

### Details worth keeping

Three to eight bullets. Discrete facts, examples, anecdotes and secondary points
that support the episode but are not part of its main spine. Bullets are correct
here, because these genuinely are a list.

### Claims worth citing

Specific numbers and factual assertions someone might repeat, each attributed to
the speaker who said it.

Open with a one-line date stamp, for example: *All figures as stated on
2025-06-05.* Add a staleness caution for fast-moving quantities such as prices,
lead times and deployment figures.

Attribute every claim: `(Guest surname)`, `(Host surname)`, or the original source where the
guest cites one, for example `(EPRI study, cited by the guest's surname)`.

Where a speaker states a number loosely or ambiguously, record the ambiguity
rather than resolving it. A note saying "he puts it around 6% but the base is
unclear" is far more useful than a confident 6%.

### Where it's contested

Where speakers disagreed, hedged, flagged uncertainty, or explicitly labeled
something an untested hypothesis. Also where a guest disclaimed expertise, and
where the host pushed back. In an essay, where the author argued against a
position, conceded a point, marked something as a guess, or revised something
they had previously said.

**This section is not optional padding.** Flattening hedges into confident
assertions is the single most likely way a note misrepresents its source. Guests
qualify heavily, and a note that drops the qualifiers reads cleaner while being
less true.

If you genuinely found nothing contested, look again before concluding it. On a
show where the host pushes back, near-zero episodes have no disagreement at all.
On a show where the host mostly builds on the answers, an episode with no
disagreement is common and you should say so plainly rather than manufacturing
some. In that case the useful content of this section is what went unexamined:
which load-bearing claims nobody tested, what interest the speaker has in the
claim being true, and which questions the episode did not reach. Your show
profile says which kind of show you are working on.

---

## Place each fact once

Three independent verification passes over nine notes found the same defect in
every one of them, and it is the largest source of length that should not be
there. A figure gets stated in "The argument" where it reads as reasoning,
indexed again in "Claims worth citing," and sometimes defined around a third
time in "What you need to know first."

Each section has a distinct job and they do not overlap.

- **The argument** carries the reasoning. It needs the figures that *are*
  reasoning turns and no others. A number you could delete without breaking the
  logic of the paragraph belongs somewhere else.
- **What you need to know first** defines terms. If a bullet restates a sentence
  from the argument rather than defining a word in it, cut the bullet.
- **Details worth keeping** stays qualitative: examples, anecdotes, secondary
  points. It is not an overflow bin for numbers.
- **Claims worth citing** is the index of figures. In a well-built note most of
  its bullets are new on first reading.
- **Where it's contested** *points at* claims rather than re-deriving them. One
  clause naming a figure already in Claims is enough. Restating the figure, its
  source and its caveat a second time is not.

The testable version: in the reference notes, 7 of 9 claims bullets state
something the reader has not already seen. In the nine notes that failed this,
the ratio ran the other way, in one case 10 of 12 restating.

This does not compete with the word-count rule above. Fixing it removes words
that were never doing work, and a note still running long afterwards is running
long for the right reason.

---

## Disclosures

Hosts in this space are often investors, and guests are often companies the
host or the show has a relationship with. **This is normal and is not a red
flag.** It is usually disclosed on air. Your source profile says what the normal
pattern is for your source.

When it applies, record it as a plain factual `disclosure:` field, and
optionally one measured line in "Where it's contested." Do not editorialize, do
not warn the reader away from the content, and do not frame the item as
untrustworthy.

The legitimate and narrow point to make: a founder's figures about their own
unshipped product are design targets rather than measured results, so attribute
them to the company. Make that point once, without alarm.

Sponsors are a separate question and are **not** disclosed per note. A sponsor
is not a speaker and takes no position in the conversation.

**Essays differ in one way that matters.** A podcast disclosure is usually an
event: something the host says on air about this guest, in this episode. An
essayist's position is instead a standing fact that is true of every post they
write, and repeating it in all 56 notes as though it were news would be both
noise and, by the fifth time, faintly accusatory.

So for an essay, the standing affiliation belongs in the source profile and in
the note's `author:` field, which is where the reader will look for it. Use
`disclosure:` only when this particular post turns on it: the author writes
about a company they fund or sit with, discusses their own employer's product,
or says outright that they have a position in what they are describing.

---

## Style

- Plain language. Define jargon or avoid it. Never use an acronym unexpanded.
  When the episode itself never expands one, the scope rule wins: do **not**
  supply the expansion from outside knowledge. Describe the thing functionally
  instead ("a federal energy research program"), or name it as the transcript
  does and say the speaker does not spell it out. The reader needs to understand
  the sentence, not to learn the acronym.
- **That rule targets terms a general reader would not already know.** An
  abbreviation in ordinary use, or the familiar name of a well-known law, is
  vocabulary rather than a fact about the episode, and writing it plainly costs
  the reader nothing. Applied to those, the rule produces circumlocutions that
  make the note harder to read while protecting nothing. Two were observed in a
  single batch: world economic output written around at length because a speaker
  said "GDP," and a statute named on air rendered as "post-crisis financial
  regulation." Both were worse than the plain word.
- Use em-dashes sparingly. Prefer two sentences, a semicolon, a colon, a comma,
  or parentheses.
- Write for someone smart who does not work in energy. No condescension, no
  oversimplification.
- Do not hedge your own prose. Report the episode's hedges; do not add your own.
- Wrap lines at roughly 80 characters.
- Do not quote more than a short phrase from the transcript. Summarize in your
  own words. The transcript sits beside the note for anyone who wants the source.

---

## Verification, before you save

Run all three. They catch different failures and passing one says nothing about
the others.

**1. Fact check.** Go back through the document and confirm every number,
name, company and specific claim in your note. Check that qualifiers survived:
if the speaker said "in a lot of territories," your note must not say "always."
Watch for figures that a speaker attached to a specific condition, where the
condition got dropped.

**2. Forest test.** Reread only your own note, with the document closed. Can
you state the central question, the answer, the main reason, and the strongest
objection? If you have a pile of accurate facts and no thesis, the note has
failed its main purpose. Rewrite the argument section.

**3. Attribution check.** This one is subtle and gets missed most often.

The failure: every individual fact stays correct, the thesis stays roughly
right, and the causal weighting is quietly wrong. A guest says "data centers are
one factor among many, though the biggest," and the note comes out reading as
though data centers are the cause.

It happens because something in the item exerts a gravitational pull on the
summary. Three sources, and you have to check all three. The first and third
are the same for both content types. The second is where they differ: in a
conversation it is the host's framing, and in an essay it is quoted voice,
described under Notes on an essay.

*The title.* Items are named after one subject, and that subject tends to
absorb credit or blame that the speaker or author spread across several. Find
every place the item scoped, shared or qualified causation, and confirm your
note preserves that scope rather than collapsing it onto the headline subject.
Pay particular attention wherever contributing factors are listed, local is
distinguished from global, or something is said to have been going to happen
anyway.

*The host's framing.* (Podcasts. For essays, see quoted voice instead.) These shows open with a host monologue that states the
premise before the guest has spoken, and the host restates the guest's points as
the conversation goes. Those restatements are not always faithful, and the
monologue is usually scripted, so it is tighter and more quotable than anything
the guest says extemporaneously. That is exactly what makes it dangerous: it is
the version a note reaches for.

Observed cases. In one episode the monologue treats a labor shortage as the
binding constraint while the guest ranks it third, behind power and community
opposition. In another, the host twice restates a guest's inferred figure at the
wrong value and the guest lets it pass. In a third, the monologue names a single
binding constraint on a cost where the guest describes it as one input among
several. **Where
the host's framing and the guest's own words diverge, the guest governs.** Write
the note from what the guest actually said, and if the divergence is
substantive, one line in "Where it's contested" recording it is usually worth
more than anything it displaces.

Note the asymmetry: silence is not agreement. A guest who does not correct the
host may be being polite, may not have caught it, or may be mid-thought. Do not
upgrade an uncorrected restatement into a claim the guest endorsed.

*Your own compression.* When you shorten a hedged claim, the hedge is the first
thing that falls out, because it is the part that reads as clutter. Reread every
sentence in "The answer" and "The argument" that carries causation and ask
whether the document supports it at exactly that strength, not merely in that
direction.

---

## Notes on a podcast episode

Applies when your source has `content_type: "podcast"`. The document is
`transcript.md`.

**Length of the source.** Transcripts run 3,000 to 10,000 words, several times
the length of the note, so the 1,300 to 1,900 word target and the validator's
900 to 2,000 band both apply as written.

**Do not write the note from the show notes.** The document carries a "Show
notes" section above the transcript. It is marketing copy, it is sometimes
factually wrong, and it routinely misses the actual argument. Read the
transcript.

**The transcript is machine-generated.** Expect garbled phrases, false starts
and self-corrections, and interpret them charitably rather than treating an
obvious transcription error as a substantive claim. Where a name or number is
garbled, quote the garbled rendering and say so; never repair it from outside
knowledge.

**Attribution risk lives in the host's framing**, as described in verification
check 3 above. Silence is not agreement.

---

## Notes on an essay

Applies when your source has `content_type: "essay"`. The document is
`essay.md`.

An essay is easier to read than a transcript and harder to summarize. It is
already edited, already compressed, and already argued in the author's own
preferred order, which means there is far less slack in it. Four things follow.

**1. Length scales with the source.** Essays vary enormously: in this archive
they run from 248 words to nearly 12,000. The fixed 1,300 to 1,900 target does
not survive that range, so for essays the validator computes the band from the
document's own word count: a note runs between a fifth and two thirds of its
source, bounded by the usual 900 to 2,000.

Two thirds rather than a half because a note has fixed overhead. Seven sections
and an attribution on every claim cost about the same whatever the source
length, which is why the shortest podcast transcripts in this archive also
produce the least compressed notes.

A note that is longer than its source is a validator **error**, not a warning.
At that point you are no longer summarizing, and the surplus has to come from
somewhere, which in practice means outside knowledge.

For a genuinely short post, write a genuinely short note. Three sentences of
argument that carry the actual reasoning beat six paragraphs of elaboration.
The sections are still all required, and a one-line section is a fine answer
when the post gives you one line's worth.

**2. Quoted voice is the attribution risk.** This is the essay's equivalent of
the host's framing, and it is sharper, because quotation marks are easier to
lose than a change of speaker.

The scraper preserves block quotes as Markdown `> ` lines. **Every one of those
lines is someone other than the author speaking, or the author at another
time.** Three cases, all observed in this archive:

- *The author quoting themselves.* A post revisiting an earlier piece quotes it
  at length and then revises it. The quoted passage is the old position. The
  prose around it is the new one. A note that merges them attributes to the
  author, today, a view the post exists to correct.
- *The author quoting a source.* A study, a report, an executive. The claim
  belongs to that source, and the author's contribution is the use they make of
  it. Attribute it the way the spec already requires for a guest citing an
  outside study.
- *A guest section.* Some posts hand several paragraphs to another writer.
  Where the document marks the handover, say who is speaking; where it does
  not, the source profile will tell you the marker to look for.

**3. Figures carry argument, and you cannot see them.** The scraper emits a
line like `[FIGURE: no caption in source] <url>` at each image. These are
frequently charts, and frequently the evidence for the sentence immediately
before them.

Do not infer what a figure showed. Where the argument rests on one, say so
plainly in the note: the reader is better served by "he puts the supporting
data in a chart the note cannot reproduce" than by a confident number nobody
verified. Where a figure merely decorates, ignore it.

**4. "Where it's contested" usually means something else.** A solo-authored
essay has no interlocutor. Nobody pushed back, so there is rarely a
disagreement to record, and manufacturing one is worse than reporting its
absence.

What the section is for here, in rough order of usefulness:

- **Where the author hedges or marks a guess.** Essayists signal confidence
  carefully. "I suspect", "my best guess", "this is the part I am least sure
  about" are the most valuable sentences in the piece and the first ones a
  careless summary drops.
- **Where the author revises themselves.** An explicit change of mind is a
  finding, and so is the reason given for it.
- **What the argument rests on and does not defend.** The load-bearing
  assumption stated in passing and never returned to.
- **What the author has at stake.** See Disclosures. State it factually, once.
- **Counterarguments the author raises and answers**, where the answer is
  weaker than the argument it answers.

If the piece genuinely contests nothing, say that plainly and use the section
for the last three.

---

## Controlled vocabulary for `threads`

Use only these tags. They exist so the synthesis layer can group episodes, and a
vocabulary that fragments across 120 notes is useless.

```
ai-compute            data-center-power     load-growth
electricity-prices    interconnection       transmission
grid-operations       demand-flexibility    ders
microgrids            energy-storage        long-duration-storage
batteries             nuclear               geothermal
fusion                solar                 wind
renewables            marine-energy         space-systems
gas-buildout          coal-retirement       clean-firm-generation
hydrogen              carbon-capture        carbon-removal
carbon-markets        geoengineering        methane
supply-chain-costs    manufacturing-capacity critical-minerals
grid-hardware         transformers          metal-fuels
construction-and-epc  skilled-labor         electrification
evs                   trucking-and-freight  heat-and-industry
buildings-efficiency  fuels-and-shipping    agriculture-and-land
climate-adaptation    water                 waste-and-recycling
public-opinion        policy-and-regulation utility-business
market-design         cost-curves           first-of-a-kind
techno-economic-analysis venture-and-finance china
geopolitics           defense-energy        backup-power
robotics              materials-discovery   quantum-computing
weather-and-forecasting  ai-applications     oil-markets
fuel-cells
```

One distinction in that list is easy to get wrong and matters a great deal to
the synthesis layer. `ai-compute` means **AI as a load on the energy system**,
and sits with `data-center-power` and `load-growth`. `ai-applications` means
**AI as a tool used by the energy system or by industry**: grid operations,
industrial control, materials discovery, forecasting. An episode about software
that helps run a grid is not an episode about electricity demand, and tagging it
`ai-compute` tells the synthesis layer the opposite of the truth. The narrower
tags (`materials-discovery`, `weather-and-forecasting`, `robotics`) sit happily
alongside `ai-applications` rather than replacing it.

Assign two to five tags. Choose the ones a person looking for this episode would
actually search.

If nothing fits, do **not** invent a tag in `threads:`. Add a separate
`proposed_threads: [your-tag]` field instead, so new vocabulary stays separable
and can be reconciled deliberately rather than silently fragmenting.

---

## Known transcript quirks

These hold for machine-generated transcripts generally, and so apply to podcast
sources only. Your source profile lists any that are specific to your source.

- Occasional paragraphs render a speaker name as plain text instead of a bolded
  label, from a formatting error on the source page. Attribute by context.
- Transcripts are machine-generated and contain garbled phrases, false starts and
  self-corrections. Interpret charitably and do not treat an obvious
  transcription error as a substantive claim.
- Some episodes include a third "speaker" that is really a station bumper or
  sponsor read. Ignore it.
- Sponsor reads and credits are already separated out of the transcript section.
  If any remain, do not treat them as content.

---

## Reference examples

Worked examples are per-source, because a good note looks slightly different
for a technical interview, a market roundup and a written argument. **Your
source profile lists them.** Read at least two before writing your first note,
including the one it names as the benchmark.
