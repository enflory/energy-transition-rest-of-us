# Adding a podcast

Nothing about any particular show is hard-coded. Adding one means writing a
config, learning the show, and only then scaling up.

The order matters. The Catalyst notes are consistent because the show was
understood before 125 notes were written, not after.

---

## 1. Create the directory and config

```
podcasts/<show>/
  podcast.json
  SHOW-PROFILE.md
```

Copy `podcasts/critical-capital/podcast.json` as a starting point. The fields:

| Field | What it does |
|---|---|
| `name` | Directory name. Used in commands. |
| `display_name` | Human-readable title, used in transcript frontmatter. |
| `publisher` | Recorded in frontmatter for provenance. |
| `host` | Recorded for reference. Fill in after reading a transcript. |
| `sitemaps` | The publisher's sitemap URLs. |
| `url_filter` | Substring identifying this show's episode URLs. |
| `delay_seconds` | Politeness delay between requests. Leave at 1.0. |
| `corrections` | Repeated publisher misspellings. **Start empty.** |
| `non_speakers` | Labels matching the speaker shape that are not people. |
| `boilerplate` | Sponsor reads, credits, ad markers. |

**Find the URL filter empirically**, not by guessing. Fetch the sitemap and look
at the slugs:

```python
import re, urllib.request
xml = urllib.request.urlopen(urllib.request.Request(
    "https://example.com/post-sitemap.xml",
    headers={"User-Agent": "Mozilla/5.0"})).read().decode()
for loc in re.findall(r"<loc>([^<]+)</loc>", xml):
    print(loc)
```

For Latitude Media, verified filters are `/catalyst-`, `/critical-capital-`,
`/open-circuit-` and `/green-blueprint-`.

**Leave `corrections` empty until you have seen a real, repeated error.** A
correction edits the source text. It is for a publisher consistently misspelling
a name, not for anything that requires judgment.

---

## 2. Fetch a few episodes and read them

```bash
python run.py fetch <show>
```

Then actually read two or three transcripts. You are looking for:

- **An intro bumper** whose label matches the speaker-label shape. Catalyst's
  is `Tag:`, and it contaminated 48 episodes before anyone noticed. Add it to
  `non_speakers`.
- **Sponsor reads** that name real companies and read like content. Add their
  opening lines to `boilerplate`.
- **A recurring misspelling** of the host's or a regular's name. Add a
  correction with a clear note.
- **Formatting quirks**, such as speaker labels that render as plain text.
- **Whether the host opens with a framing monologue.** This matters more than it
  sounds. A framing monologue is the main source of attribution drift, and
  verification check 3 depends on knowing whether the show does it.

Re-fetch after config changes:

```bash
python run.py refetch <show>
```

Check the word counts. A transcript far shorter than the others usually means
the parser found the wrong starting point, and a transcript that is suspiciously
long usually means boilerplate leaked in.

---

## 3. Fill in the show profile

`SHOW-PROFILE.md` is read by every agent that writes a note for this show, so it
is doing real work. Cover:

- What the show is, who hosts it, and its usual format.
- **Disclosure norms.** Does the host have investing relationships with guests?
  Is it disclosed on air? What is boilerplate self-identification rather than an
  interest in the guest? Be specific about what triggers a `disclosure:` field
  and what does not.
- **Transcript quirks** specific to this show.
- **What the attribution check looks like here**, with real observed examples.

---

## 4. Hand-write one or two reference notes

Do this yourself, slowly, reading the transcript closely, and check the result
against the transcript twice. Then list them in the profile with a sentence each
on what they demonstrate, and name one as the benchmark.

This is the single highest-leverage step. Every agent reads the benchmark before
writing anything, so a weak reference note propagates into every note that
follows. A strong one is worth more than any amount of specification prose.

---

## 5. Scale up

```bash
python run.py brief <show>
```

Paste the brief into an agent. Three episodes per agent, mixed topics, strong
model. Then:

```bash
python run.py validate <show>
python run.py dedupe <show>
```

Have a **different** agent verify the notes than the one that wrote them.

---

## 6. Start the synthesis files

Create `podcasts/<show>/synthesis/` with `hindsight-seeds.md` and
`archive-caveats.md`, even if they start nearly empty. Cross-episode
observations and corpus data-quality findings arrive while notes are being
written, and they are lost if there is nowhere to put them.

---

## Does the spec need changing?

Usually not. `docs/NOTE-SPEC.md` is portable by design, and show-specific facts
belong in the profile.

Change the spec only when you find something true of **note-writing in
general** that it does not yet say. If you do change it, do it between waves,
never while agents are reading it, and bump the version number at the top.

Adding to the controlled vocabulary is the common exception. Do it from
evidence: count how many episodes actually need the tag before adding it. A tag
used once does not help the synthesis layer group anything, and a vocabulary
that fragments is worse than one that is slightly too coarse. Agents propose new
tags through `proposed_threads:` rather than inventing them in `threads:`, which
keeps proposals visible and reconcilable instead of silently splitting the
vocabulary.
