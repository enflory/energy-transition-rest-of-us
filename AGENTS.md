# Instructions for agents

This file is for any AI agent working in this repository. It is tool-agnostic.
`CLAUDE.md` adds a few Claude Code specifics on top of it.

Read this before touching anything.

---

## What this repository is

An archive of structured notes on energy-transition podcasts and newsletters,
plus the pipeline that produces them. The notes are the product. Accuracy
matters more than volume, and a wrong note is worse than a missing one, because
a wrong note gets quoted in a meeting.

A **source** is a publication, a **document** is one episode's transcript or
one post's text, and an **item** is the folder holding a document and its note.
Sources are one of two content types, `podcast` or `essay`, declared in
`sources/<source>/source.json`. Which one you are working on changes the
directory names, the note's frontmatter fields and the note's length rule, and
it changes where misattribution comes from.

---

## The three files that govern note-writing

1. **`docs/NOTE-SPEC.md`** — the specification. Format, sections, style,
   controlled vocabulary, and the three verification checks. Portable across
   sources. Read it in full; do not skim it, and read the section for your
   content type, "Notes on a podcast episode" or "Notes on an essay", twice.
2. **`sources/<source>/SOURCE-PROFILE.md`** — that source's disclosure norms,
   document quirks, and reference notes. Read it in full too.
3. **The reference notes** the profile names. Read at least two, including the
   one it calls the benchmark, before writing your first note.

If you are writing a note and have not read all three, stop and read them.

---

## Hard rules

- **Never modify a `transcript.md` or an `essay.md`.** It is the source of
  record.
- **Never modify** `manifest.csv`, `source.json`, `docs/NOTE-SPEC.md`, a
  `SOURCE-PROFILE.md`, or anything in `scripts/` as a side effect of writing
  notes. Those are changed deliberately, on their own, never mid-task.
- **Write only the `note.md` files you were assigned.** Not neighbouring items,
  not other sources.
- **One item per note.** No cross-item references, no hindsight, no outside
  knowledge used to correct or update a claim. If a claim looks dated, record
  it as stated with its date and move on. Cross-item material belongs in
  `sources/<source>/synthesis/`.
  - This binds hardest where it is most tempting: **a post revisiting the
    author's own earlier post is still one item.** Write what this document
    says about the earlier one. Do not go and read the earlier one.
- **Do not supply facts the document does not contain.** If a transcript
  garbles a name, quote the garbled rendering and say so. Do not correct it
  from outside knowledge, and do not guess.
- **Do not write a note from the show-notes section** of a transcript, or from
  the subtitle of a post. Both are marketing copy and both are sometimes
  factually wrong. Read the document.
- **Never attribute a quoted passage to the person quoting it.** In an
  `essay.md`, every `> ` line is someone else's words or the author's at
  another time. In a transcript, a guest's silence is not agreement.

---

## The failure mode to watch for

Every individual fact correct, the thesis roughly right, and the causal
weighting quietly wrong. Three things cause it:

- **The title**, which absorbs causation the guest or author spread across
  several factors.
- **The host's framing**, which states the premise before the guest speaks and
  is not always faithful when it restates a guest's point.
- **Your own compression**, where a hedge is the first thing cut because it
  reads as clutter.

**Where the host's framing and the guest's own words diverge, the guest
governs. Silence is not agreement.** A guest who lets a misstatement pass may
be being polite, may not have caught it, or may be mid-thought. Never upgrade an
uncorrected restatement into a claim the guest endorsed. Record the divergence
in "Where it's contested" instead.

---

## Commands

```bash
python run.py                    # what needs doing
python run.py sources            # list configured sources
python run.py brief <source>     # the note-writing brief, ready to paste
python run.py fetch <source>     # scrape missing items
python run.py validate [source]  # structural check
python run.py dedupe [source]    # find republished items
python run.py stats [source]     # archive size and coverage
```

Run `validate` before reporting a note as finished, and fix every ERROR.

---

## The word-count warning

The validator warns above 2,000 words for a podcast episode, and above a
ceiling computed from the document for an essay. **It is advisory, and it says
so in its own output.** When a note runs over, ask what the excess actually is:

- Duplication between sections, restatement, loose phrasing: cut it.
- Attributed figures, reasoning turns, speakers' hedges: keep them and leave
  the warning standing.

**Trimming a note down to clear the warning is itself a failure.** A note that
lands at 1,998 words is a sign the tool was steering rather than the material.
Survey episodes (annual trends, mailbags, multi-topic roundups) almost always
belong in the keep-it case, because their claims section is the content.

One length rule is **not** advisory: a note that has outgrown its own document
is an ERROR. Fix it by cutting, not by arguing with it. It mostly fires on
short essays, where the honest answer is a short note.

---

## Style

- Plain language. Define jargon or avoid it.
- **Use em-dashes sparingly.** Prefer two sentences, a semicolon, a colon, a
  comma, or parentheses.
- Write for someone smart who does not work in energy. No condescension.
- Report the episode's hedges; do not add your own.
- Wrap lines at roughly 80 characters.
- Do not quote more than a short phrase from a transcript. Summarize in your own
  words; the transcript sits beside the note for anyone who wants the source.
- When an episode never expands an acronym, do **not** supply the expansion from
  outside knowledge. Describe the thing functionally instead.

---

## Working in parallel

Notes are independent by design, so several agents can write them at once
without coordination. Three items per agent works well. Give each agent its own
item folders and nothing else; there is no shared state to conflict over.

Do not mix content types within one agent's batch. The two halves of the spec
pull in different directions on length and on attribution, and an agent holding
both tends to write podcast-shaped notes for essays.

Verification is better done by an agent that did **not** write the note. A
writer has already made each judgment call once and tends to confirm it.

---

## Before you report finished

State what you actually did, including what you could not do. Specifically:

- The final validator output, verbatim.
- Any hard judgment call you made, and why.
- Any garbled or ambiguous passage that affected the note, and how you handled
  it. Recording an ambiguity is a better outcome than resolving it silently.
- For an essay, whose voice you judged each block quote to be in, and any
  figure the argument depended on that you could not see.
- If you found nothing wrong, say so plainly rather than inventing problems.
