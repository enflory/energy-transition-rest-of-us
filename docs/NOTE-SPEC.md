# Episode note specification

**Version 1.3**

You are writing a single `note.md` for a single podcast episode, from
its transcript. Read this whole file before starting. Reference examples are
listed at the bottom; read at least two before writing your first note.

---

## Context

This repository turns podcast episodes about the energy transition into
structured, plain-language notes. You are writing one note for one episode.

**Show-specific context lives in `podcasts/<podcast>/SHOW-PROFILE.md`**: who
hosts the show, what disclosures are normal for it, its particular transcript
quirks, and which existing notes to read as worked examples. Read that file as
well as this one before you start. This spec is the portable part; the profile
is the part that changes per show.

The reader is a non-specialist who follows this space closely. He wants to
answer questions like "should I worry about AI's energy use?" accurately in a
meeting, without oversimplifying, and to build a newsletter from this material.

**Your note is infrastructure, not the final product.** A later synthesis layer
reads across all the notes to build cross-episode threads and newsletter items.
That means two things: your note must be accurate enough to be trusted without
re-reading the transcript, and it must stay strictly within its own episode
(see Scope below).

---

## Input and output

- **Read:** `podcasts/<podcast>/episodes/<episode-folder>/transcript.md`
- **Write:** `podcasts/<podcast>/episodes/<episode-folder>/note.md`
- **Never modify** `transcript.md`, `manifest.csv`, `podcast.json`, this spec,
  anything in `scripts/`, or any other episode's files.

Read the entire transcript before writing anything. These run 3,000 to 10,000
words. Do not skim, and do not write the note from the show notes section alone;
the show notes are marketing copy and routinely miss the actual argument.

---

## Scope: single episode only

Write only what this episode supports. Do not:

- Reference other episodes, even if the transcript mentions them.
- Add hindsight, "what happened since," or "read this alongside X."
- Bring in outside knowledge to correct, update or contextualize a claim.
- Speculate about how the topic developed after the recording date.

Cross-episode synthesis happens in a later layer that reads all the notes at
once. If you add it here, it will be wrong, because you can only see one episode.

If a claim in the episode looks dated or superseded, that is fine. Record it as
stated, with its date, and move on. The date stamp is how staleness gets handled.

---

## The format

Write exactly these sections, in this order, with these headings.

```markdown
---
episode: "<exact title from transcript frontmatter>"
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

Two optional frontmatter fields:

- `age_warning: "..."` when the episode is more than about 18 months old and its
  specifics are likely superseded. One sentence.
- `disclosure: "..."` when the host states a financial interest in the guest's
  company, or the show profile's disclosure pattern applies. See Disclosures
  below.

Target 1,300 to 1,900 words total, and treat that as a guide rather than a
budget. Match the note to the material: a dense 8,000-word episode earns a longer
note than a 4,000-word one, and a genuinely short episode should get a short note
rather than padding.

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

One line. The central question the episode is organized around. Shayle usually
states it explicitly in the opening monologue, and it is often close to the
episode title. Phrase it as a real question a person would ask.

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
guest cites one, for example `(EPRI study, cited by Lubershane)`.

Where a speaker states a number loosely or ambiguously, record the ambiguity
rather than resolving it. A note saying "he puts it around 6% but the base is
unclear" is far more useful than a confident 6%.

### Where it's contested

Where speakers disagreed, hedged, flagged uncertainty, or explicitly labeled
something an untested hypothesis. Also where a guest disclaimed expertise, and
where the host pushed back.

**This section is not optional padding.** Flattening hedges into confident
assertions is the single most likely way a note misrepresents its source. Guests
on this show qualify heavily, and a note that drops the qualifiers reads cleaner
while being less true. If you found nothing contested, look again; near-zero
episodes have no disagreement or uncertainty at all.

---

## Disclosures

Hosts in this space are often investors, and guests are often companies the
host or the show has a relationship with. **This is normal and is not a red
flag.** It is usually disclosed on air. Your show profile says what the normal
pattern is for your show.

When it applies, record it as a plain factual `disclosure:` field, and
optionally one measured line in "Where it's contested." Do not editorialize, do
not warn the reader away from the content, and do not frame the episode as
untrustworthy.

The legitimate and narrow point to make: a founder's figures about their own
unshipped product are design targets rather than measured results, so attribute
them to the company. Make that point once, without alarm.

Sponsors are a separate question and are **not** disclosed per note. A sponsor
is not a speaker and takes no position in the conversation.

---

## Style

- Plain language. Define jargon or avoid it. Never use an acronym unexpanded.
  When the episode itself never expands one, the scope rule wins: do **not**
  supply the expansion from outside knowledge. Describe the thing functionally
  instead ("a federal energy research program"), or name it as the transcript
  does and say the speaker does not spell it out. The reader needs to understand
  the sentence, not to learn the acronym.
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

**1. Fact check.** Go back through the transcript and confirm every number,
name, company and specific claim in your note. Check that qualifiers survived:
if the speaker said "in a lot of territories," your note must not say "always."
Watch for figures that a speaker attached to a specific condition, where the
condition got dropped.

**2. Forest test.** Reread only your own note, with the transcript closed. Can
you state the central question, the answer, the main reason, and the strongest
objection? If you have a pile of accurate facts and no thesis, the note has
failed its main purpose. Rewrite the argument section.

**3. Attribution check.** This one is subtle and gets missed most often.

The failure: every individual fact stays correct, the thesis stays roughly
right, and the causal weighting is quietly wrong. A guest says "data centers are
one factor among many, though the biggest," and the note comes out reading as
though data centers are the cause.

It happens because something in the episode exerts a gravitational pull on the
summary. Three sources, and you have to check all three.

*The title.* Episodes are named after one subject, and that subject tends to
absorb credit or blame that the guest spread across several. Find every place
the episode scoped, shared or qualified causation, and confirm your note
preserves that scope rather than collapsing it onto the headline subject. Pay
particular attention wherever the guest lists contributing factors,
distinguishes local from global effects, or says something would have happened
anyway.

*The host's framing.* Shayle's opening monologue states the premise before the
guest has spoken, and he restates the guest's points as the conversation goes.
Those restatements are not always faithful. In one episode the monologue treats
a labor shortage as the binding constraint while the guest ranks it third,
behind power and community opposition. In another, the host twice restates a
guest's inferred figure at the wrong value and the guest lets it pass. **Where
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
whether the transcript supports it at exactly that strength, not merely in that
direction.

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

These hold for machine-generated transcripts generally. Your show profile lists any that are specific
to your show.

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

Worked examples are per-show, because a good note looks slightly different for
a technical interview than for a market roundup. **Your show profile lists
them.** Read at least two before writing your first note, including the one it
names as the benchmark.
