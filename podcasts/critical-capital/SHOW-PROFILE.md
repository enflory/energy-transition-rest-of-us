# Show profile: Critical Capital

Read this alongside `docs/NOTE-SPEC.md`. The spec is the portable part; this
file is everything true of Critical Capital specifically.

---

## The show

Critical Capital is a podcast about the money behind energy and physical
infrastructure, hosted by **Alfred Johnson**, co-founder and CEO of Crux, a
capital platform for clean-economy financing. It is a co-production of Crux and
Latitude Studios, which also publishes Catalyst. Episodes are a single long
interview with one guest.

The archive here holds 11 transcripts spanning 2026-04 to 2026-09, plus one
trailer with no transcript. Episodes run 5,300 to 7,400 words, noticeably
shorter than Catalyst. New episodes land every other **Tuesday**, without
exception from 2026-05-26 through 2026-09-15. The first three releases were
irregular, so do not read the early gaps as a schedule.

**Where the transcripts come from.** Latitude Media publishes this show but not
its transcripts. As of 2026-09-18 latitudemedia.com carried 2 of the 12
episodes as show-notes pages with no transcript text at all. Crux publishes
every episode in full at crux.com/critical-capital, so that is the source of
record. `podcast.json` explains the scraping consequences.

**Format.** Every episode opens the same way: a short clip of the guest, then a
host monologue stating the episode's premise, then a second guest clip, then
"This is Critical Capital. I'm Alfred Johnson, the CEO of Crux," then a factual
introduction of the guest, then the interview. It closes with a one-sentence
host sign-off and spoken credits.

---

## The thing that makes this show different from Catalyst

**The guests are principals, not analysts.** They are overwhelmingly founders
and investors being interviewed about the thing they personally sell or fund: a
battery company's CEO on batteries, a flexibility software CEO on flexibility, a
venture partner on the category their fund invests in. That is the show's whole
premise and it is not a defect. It does change what a faithful note looks like.

Two consequences, and they are the main thing to get right here:

1. **The host does not push back much.** Johnson is a warm, affirming
   interviewer who builds on answers rather than testing them. Catalyst notes
   can lean on the host's challenges to find the seams in an argument. Here
   there usually are none, and a note that manufactures contestation to fill the
   section is worse than one that says plainly there was none.

2. **"Where it's contested" therefore usually means something else on this
   show.** The honest content of that section is normally: what the guest is
   selling, which load-bearing claims went unchallenged, and which questions the
   episode did not reach. State it factually, in the same register you would use
   for any other fact. It is not an accusation, and the guest's position is
   almost always stated openly on air.

---

## Disclosures

The host runs a company that finances projects in the sector his guests work in.
This is a more direct structural relationship than a podcast host who happens to
be an investor, and it is worth getting the line right.

Triggers for a `disclosure:` field, both narrow:

- Johnson or the guest states on air that **Crux has a commercial relationship
  with the guest's company**. Observed twice in 11 episodes:
  - `2026-07-21` Nuveen. Johnson states Crux and Nuveen announced a $500 million
    debt facility, and refers to working with Nuveen over the past year.
  - `2026-09-15` Base Power. Johnson states Crux has handled Base's tax credit
    sales since the company's early days, and closes by calling himself Zach
    Dell's partner at Crux.
- Johnson otherwise states a financial interest in the specific subject.

Not triggers:

- **His standard self-identification**, "I'm Alfred Johnson, the CEO of Crux,
  the capital platform for the clean economy." It opens every episode. It is
  boilerplate, not an interest in the guest.
- **The spoken credits**, which thank "the excellent team at Crux" every week.
- A guest praising Crux in passing. In `2026-06-23` the guest says he imagines
  Crux has good market intelligence. That is a compliment, not a relationship.
- The guest's own commercial stake in their argument. That is not a disclosure,
  it is the premise of the show. It belongs in `guest:` and, where it bears on
  a claim, in "Where it's contested."

Record a disclosure as a plain factual field plus at most one measured line.
Do not editorialize and do not frame the episode as untrustworthy.

---

## Transcript quirks specific to this show

- **The credits are garbled, differently every week.** The same production team
  is rendered "John Sheehan" and "John Sheen," "Sean Marquand," "Sean Marwan"
  and "Sean Markwand," "Matthew Filler" and "Matthew Miller." Notes never draw
  on the credits, so this matters only as a warning that the transcription is
  machine-generated and names are unreliable throughout.
- **Guest names are mangled inside episodes too.** `2026-08-18` renders the
  guest as both "Jake Saper" and "Jake Saber" and has him addressing the host as
  "Fredo." Quote the rendering and say it is garbled. Never supply a spelling
  from outside knowledge.
- **The first episode carries inline timecodes** like `[00:12:00]` scattered
  mid-sentence, and one `[THEME MUSIC]` marker. No other episode has them.
  Ignore them; they are not content.
- **The publication date is not always the recording date.** In `2026-06-23`
  the guest says outright that he is recording weeks before launch and then
  describes "this week" in the present tense. Where an episode does this, date
  the claims to the conversation and say so in the note.
- **The show notes are marketing copy and sometimes shift attribution.** The
  notes for `2026-06-23` present the 100-gigawatt figure as the guest's own;
  in the transcript he credits it to a named outside researcher. Write from the
  transcript.
- **The host's monologue is written, not spoken off the cuff.** It is tight,
  quotable, and the single most likely thing to end up in a note as though the
  guest had said it. See below.

---

## Reference examples

Two notes were written by hand against the transcript. Read both before writing
your first note for this show.

| Episode folder | Why it is worth reading |
|---|---|
| `episodes/2026-09-15-what-it-costs-to-make-power-cheap` | **The benchmark.** A founder interview where the host's monologue states a sharper thesis than the guest does, and the note keeps them apart. Also shows the correct, unalarmed handling of a Crux disclosure, and how to write "Where it's contested" when nobody contested anything. |
| `episodes/2026-06-23-the-trillion-dollar-collision-between-ai-and-the-grid` | A guest whose entire argument is his company's product thesis, held at the right distance without insinuation. Also shows a figure correctly re-attributed to its named outside source, and a guest hedge that a careless note would drop. |

---

## What the attribution check looks like on this show

Verification check 3 in the spec is general. Its specific shape here comes from
the opening monologue, which is scripted and states the episode's thesis before
the guest has said a word.

The clearest observed case is `2026-09-15`. The monologue says the binding
constraint on a customer's electricity bill "isn't the hardware, it's the cost
of the money and the tax rules that decide where the parts can come from." The
guest never says that. He says the cost of capital is *a major input* among
several into a fully landed cost, and that the sourcing rules change *where
parts can be bought from*. The monologue is a sharpening, and it is the version
that a note will reach for, because it is better written.

Others to watch for:

- The host's long, admiring questions often contain a proposition the guest then
  only partly takes up. Thin assent is not the guest's argument.
- The host supplies context from Crux's own deal flow inside a question. That is
  the host's observation about his own business, not the guest's testimony.
- Because the host rarely challenges anything, a claim's survival to the end of
  the episode means only that nobody objected. Silence is not agreement, and on
  this show silence is the default.

**Where Johnson's framing and the guest's own words diverge, the guest
governs.**
