# Show profile: Catalyst with Shayle Kann

Read this alongside `docs/NOTE-SPEC.md`. The spec is the portable part; this
file is everything true of Catalyst specifically.

---

## The show

Catalyst is a podcast about energy, climate tech and the electricity system,
published by Latitude Media and hosted by Shayle Kann, a partner at Energy
Impact Partners (EIP). Episodes are usually a single long interview with one
guest, opened by a host monologue that states the episode's question.

The archive here holds 125 transcripts spanning 2022-11 to 2026-09.

**Format note that matters for note-writing.** Kann structures most episodes
around one central question and pushes back on his guests. That makes the
"question / answer / argument" shape of a note fit well. It also means the
opening monologue frames the topic *before* the guest speaks, which is the
single most common source of attribution drift. See verification check 3.

---

## Disclosures

**Many Catalyst episodes feature EIP portfolio companies. This is normal for
the show and is not a red flag.** Kann typically discloses it on air, usually in
the introduction or at the moment the company comes up.

Record it as a plain factual `disclosure:` field, plus at most one measured line
in "Where it's contested." Do not editorialize and do not frame the episode as
untrustworthy.

Triggers for the field, both narrow:

- Kann states on air that EIP has invested in, incubated, or holds a board seat
  at the guest's company.
- Kann otherwise states a financial interest in the subject.

Not triggers:

- Kann's standard self-identification ("I lead early-stage venture strategy at
  Energy Impact Partners"). That is boilerplate, not an interest in the guest.
- A guest who is Kann's own EIP colleague. Put the affiliation in `guest:`.
- An EIP portfolio company mentioned only in passing as an example.
- **Sponsor reads.** Latitude sells sponsorships, and a sponsor is occasionally
  in the episode's own line of business. A sponsor is not a speaker and takes no
  position. No disclosure. See `synthesis/archive-caveats.md`.

---

## Transcript quirks specific to this show

- **The intro bumper is labelled `Tag:`** and matches the speaker-label shape.
  It is filtered by `podcast.json`, but if one survives, ignore it.
- **Sponsor reads name real companies** (EnergyHub, Bloom, ENGIE and others) and
  read like content. They are filtered before the transcript start is located.
  If any remain, they are not content.
- **The host's name is rendered phonetically** by the publisher, most often
  "Shayle Khan." The scraper corrects it and records the correction count in the
  transcript's frontmatter.
- **Some episodes are reruns or delayed releases**, so the published date is not
  always the recording date. If the monologue frames rather than introduces the
  conversation, or internal references predate the publish date, say so in the
  note and date the claims to the conversation, not the file.
- **Guest names are frequently mangled.** Normalize only when you are certain;
  otherwise quote the transcript's rendering and say it is garbled. Never supply
  a spelling from outside knowledge.

---

## Reference examples

Five notes were written by hand and reviewed against the transcript. Read at
least two before writing your first note, including the benchmark.

| Episode folder | Why it is worth reading |
|---|---|
| `episodes/2026-09-10-do-data-centers-really-increase-electricity-prices` | **The benchmark.** The argument preserves a counterintuitive setup and its reversal, and causation stays carefully shared rather than collapsing onto the title subject. |
| `episodes/2025-06-05-the-gas-turbine-crunch` | An answer that overturns the premise: the bottleneck is mostly outside the power sector. Also shows a specialist disputing a widely-circulated figure. |
| `episodes/2023-11-16-the-cost-of-nuclear` | An older episode handled with an `age_warning` and dated claims. Shows how to keep a durable analytical frame while marking the numbers as historical. |
| `episodes/2026-08-27-the-rise-of-metal-fuels` | A portfolio company episode. Shows the correct, non-alarmed handling of a disclosure. |
| `episodes/2024-03-28-the-electricity-gauntlet-has-arrived` | A guest who holds two apparently opposed positions at once, preserved rather than smoothed over. |

The two older reference notes end with a "Why this one matters in hindsight"
section. That section is **deprecated** and belongs to the synthesis layer. Do
not reproduce it; ignore it when using those notes as format examples.

---

## What the attribution check looks like on this show

Verification check 3 in the spec is general. On Catalyst it has a specific
shape, and this is where notes fail most often. Observed cases:

- The monologue treats a labour shortage as the binding constraint while the
  guest ranks it third.
- The host restates a guest's figure at the wrong value and the guest lets it
  pass. In one episode the host converts a cost figure by a factor of 100.
- The host supplies a ranking or a thesis in a long question and the guest
  answers "I think so." That is thin assent, not the guest's argument.
- The host's opinion gets promoted into the expert's testimony, so the note
  reads as though the specialist said the confident thing.

**Where Kann's framing and the guest's own words diverge, the guest governs.**
Silence is not agreement. A guest who does not correct the host may be being
polite, may not have caught it, or may be mid-thought.
