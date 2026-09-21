# CLAUDE.md

**Read `AGENTS.md` first.** It holds the rules that govern work in this
repository and they apply here unchanged. This file adds only the parts that
are specific to Claude Code.

---

## Orientation

Start with `python run.py`. It reads the publisher's sitemap, compares it
against what is on disk, and tells you whether there is anything to do. In the
steady state it prints `every transcript has a note. Nothing to do.`

If there is work, `python run.py brief <source>` prints a complete, ready-to-use
brief naming the exact items, files and constraints. Prefer it over writing
your own; it encodes decisions that were expensive to learn, and it is
generated from the source's content type, so it already points at the right
half of the spec.

---

## Writing notes with subagents

Notes are independent, so this parallelizes cleanly.

- **Three items per agent.** Beyond that, quality drifts as context fills.
- **Use a strong model.** This is judgment about what matters in a conversation,
  not summarization. A cheaper model produces notes that are correct sentence by
  sentence and miss the argument, which is the exact failure the specification
  exists to prevent.
- **Mix topics within a batch, but not content types.** Giving one agent three
  episodes on the same subject invites blending, so give it three unrelated
  ones. Do not give it two episodes and a post: the spec's two halves differ on
  length and on attribution, and an agent holding both writes podcast-shaped
  notes for essays.
- **Warn about near-duplicate titles.** If two episodes in flight share a title
  or subject, tell each agent the other exists and to write only from its own
  transcript.
- **Never edit the spec or a source profile while agents are reading them.**
  Queue those changes and apply them between waves. Agents read the spec once at
  the start; a mid-flight edit reaches some and not others.

## Verifying notes with subagents

Use a **fresh** agent, not the one that wrote the note. A writer has already
made each judgment call once and will mostly confirm it. Give the verifier the
document, the note, and the three checks, and tell it to report every error it
found specifically, plus anything it judged borderline and left alone.

For an essay, tell the verifier to check every `> ` block in the document
against the note. Quoted voice is this content type's version of the
attribution check and it is the thing a writer is most likely to have got
wrong.

An independent pass over 24 unverified notes found roughly 100 corrections,
including several that changed meaning. Self-review would not have found them.

---

## When you change the tooling

The validator's messages are read by agents at the moment they decide something,
whereas the spec is read once at the start. If you want an agent to behave
differently, changing the warning text is often more effective than adding a
paragraph to the spec.

Keep the controlled vocabulary in the spec as the single source of truth. The
validator parses it out of `docs/NOTE-SPEC.md` so the two cannot drift.

Everything that differs between a podcast and an essay lives in
`scripts/archive.py`: directory names, document filenames, note field names,
the words used in reports and briefs, and the note length rule. If you are
adding a branch on content type anywhere else, it belongs there instead.

---

## House conventions

- Use em-dashes sparingly in anything user-facing, including commit messages.
- Any statistic about the archive should say what window it covers, and which
  content type it counts. "125 episodes" and "125 unique conversations" are
  different numbers here, because one episode is published twice; and note
  lengths are not comparable across content types, because essay notes are
  sized against their source.
- Avoid shell heredocs for Python that contains backslash escapes; this
  environment mangles them. Use the file-writing tools instead.
