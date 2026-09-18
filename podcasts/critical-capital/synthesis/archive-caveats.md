# Archive caveats: Critical Capital

Facts about this corpus as a corpus, as distinct from what any episode says.
Read this before counting anything or ordering anything by date.

Window: the whole archive, 2026-04-12 to 2026-09-15. The show is five months
old, so unlike the Catalyst archive there is no historical era to segment away.
Every figure below covers all of it.

---

## Counts

- **12 episodes published. 11 conversations.** The twelfth, `Introducing
  Critical Capital` (2026-04-12), is a trailer. The page exists and carries a
  `Transcription` heading with nothing under it. There is no transcript because
  there is no interview. It is recorded in the manifest as `no transcript` and
  correctly produces no note.
- **No duplicates.** `python run.py dedupe critical-capital` finds no
  near-duplicate pairs. Unlike Catalyst, nothing here has been republished.
- Transcripts run 5,275 to 7,378 words, mean about 6,100. Catalyst episodes are
  noticeably longer, so a shorter note here is usually correct rather than thin.

---

## The transcripts do not come from the show's publisher

Latitude Media publishes Critical Capital. It does not publish the transcripts.
As of 2026-09-18, searching both Latitude sitemaps returned **2** Critical
Capital pages out of 12 episodes, and both were show-notes pages with no
transcript text at all.

Crux, the co-producer, publishes every episode in full at
crux.com/critical-capital. That is the source of record for this archive, and
it is why `podcast.json` for this show points at a completely different site
from the Catalyst one.

**The general lesson, which cost an hour to learn:** a show being on a network
does not mean the network publishes its transcripts. Check before configuring a
scraper against the obvious sitemap.

---

## The Crux sitemap is stale, and stale in the worst way

On 2026-09-18 the Crux sitemap listed 11 of the 12 episodes. The one it omitted
was `what-it-costs-to-make-power-cheap`, published 2026-09-15, which was the
newest episode and therefore the only one a routine "anything new?" check was
looking for.

This is why `podcast.json` also walks the show's own paginated listing pages and
unions the two sources. A scraper configured only from the sitemap would have
reported nothing new, indefinitely, for exactly the episode that mattered.

---

## The URL slug is not the title

`crux.com/critical-capital/physical-ai-aidan-madigan-curtis` is the episode
titled **"Atoms, bits, and the trillion-dollar manufacturing race."** The slug
looks like a working title that was changed before release. Folder names in this
archive are built from the published title, not the slug, so folder and URL do
not match for that one episode. Nothing is wrong; do not "fix" it.

---

## Dating

- **Published biweekly on Tuesdays from 2026-05-26 onward**, without exception
  through 2026-09-15. The first three releases were irregular: the trailer on a
  Sunday, then gaps of 16, 9 and 19 days.
- **Publication date is not recording date.** In `2026-06-23` the guest says on
  air that the recording precedes release by weeks, then describes "this week"
  in the present tense and refers to meetings happening that day. Any claim in
  that episode should be dated to the conversation, not the file. Other episodes
  may have the same gap without saying so.

---

## Transcription quality

Machine-generated, and the name handling is poor.

- **The spoken credits are garbled differently every week.** The same production
  team appears as "John Sheehan" and "John Sheen," "Sean Marquand," "Sean
  Marwan" and "Sean Markwand," "Matthew Filler" and "Matthew Miller." No note
  draws on the credits, so this matters only as a signal about the transcription
  generally.
- **Guest names are mangled inside episodes.** `2026-08-18` renders its guest as
  both "Saper" and "Saber" and has him addressing the host as "Fredo."
- **One episode carries a studio direction as a speaker label.** In `2026-06-09`
  the host's closing voiceover is labelled `ALFRED TRACKING:` rather than with
  his name. It is Alfred Johnson speaking. It is deliberately left in place
  rather than filtered, because demoting it to unlabelled prose would make it
  read as a continuation of the guest's last answer.
- **Zero-width characters precede some speaker labels** in the source HTML,
  which silently breaks speaker detection. The scraper strips them. If speaker
  labels ever start disappearing from a new episode, check for these first.
- **Only the first episode has inline timecodes** such as `[00:12:00]` dropped
  mid-sentence, plus one `[THEME MUSIC]` marker. No other episode has them.

---

## The show notes are unreliable

As on Catalyst, the blurb above each transcript is marketing copy and sometimes
misattributes. The clearest case: the notes for `2026-06-23` present the
100-gigawatt latent-capacity figure as the guest's own finding. In the
transcript he explicitly credits it to a named outside researcher. Notes are
written from the conversation, never from the blurb.

---

## A structural fact about the guest list

Every guest in the archive so far has a direct commercial stake in the argument
they are making: founders discussing the category they sell into, investors
discussing the category they fund, and in one case a sitting senator discussing
policy he votes on. This is the show's premise rather than a flaw, and the
positions are stated openly on air.

It does mean the archive as a whole is a record of what principals say about
their own markets, which is a different evidentiary thing from a record of what
analysts say about them. Anything that aggregates across these notes should
carry that qualification.

---

## Host relationships disclosed on air

The host runs Crux, which finances projects in the sector. Two of eleven
episodes involve a stated commercial relationship with the guest's company, both
disclosed by the host himself:

- `2026-07-21` Nuveen: a $500 million debt facility announced with Crux.
- `2026-09-15` Base Power: Crux has handled the company's tax credit sales since
  its early days.

His weekly self-identification as Crux's chief executive, and the weekly credits
thanking the Crux team, are boilerplate and are not disclosures. See
`SHOW-PROFILE.md` for where the line sits.
