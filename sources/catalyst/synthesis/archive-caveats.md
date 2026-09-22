# Archive caveats

Data-quality notes about the corpus itself, as distinct from analytical
content. Layer 2 must read this before treating `published:` as a recording
date or before comparing figures across episodes by date.

## Reruns: published date is not always the recording date

`2024-08-09-understanding-the-transmission-bottleneck` is a rerun. Kann's
August 2024 monologue wraps a conversation he says aired "last year," and the
internal evidence agrees: the guest is awaiting 2022 congestion data, a FERC
rule is still possibly final "late spring," and Glick has already left. The
interview is from 2023.

Batch 3D handled it correctly: kept `published: 2024-08-09` per the spec,
attributed the Princeton figures to Kann's 2024 introduction, and date-stamped
the claims section as 2023 numbers. That is the right pattern.

**Why this matters.** Any cross-episode comparison that buckets by published
date will place this episode's 2023 figures in 2024, and the transmission and
interconnection numbers moved fast in that window. A trend line drawn through
them would be wrong in a way that looks plausible.

A second case, found independently: in `2024-12-02-from-biowaste-to-biogold`
Kann states on air that the conversation was recorded some time before its
release, so its figures are older than the publish date implies. Not a full
rerun, but the same hazard.

**Open action for layer 2:** scan for other reruns and delayed releases before
building anything date-ordered. The tell is a host monologue that frames rather than introduces,
or internal references that predate the published date. Do not assume this is
the only one; it was found by accident because one agent read carefully.

## Show notes are marketing copy and sometimes contradict the transcript

The spec already forbids writing a note from the show notes. Wave 3 produced a
concrete instance of why, beyond mere omission:

- `2024-08-29-why-are-we-still-flaring-gas` — the show notes claim flaring
  equals "about half the global carbon emissions of aviation over a 30-year
  period." The transcript does not support it; Bredariol says flaring emissions
  exceed those of all international flights last year. Different comparison,
  different period, different magnitude.

Other instances where show notes and transcript disagreed on facts, collected
from agent reports:

- `2024-03-06-shopify...` — a $55M figure appears only in the show-notes blurb
  and never in the conversation; Kauk gives just under 85,000 tons cumulative.
- `2023-08-10-beaming-24-7-solar-from-space` — show notes give a 10km x 10km
  array; the guest says "10 square kilometers of collection area or more."
- `2024-01-11-2023-climate-tech-venture-investment-trends` — show notes claim
  non-equity financing "expanded in 2023," which is not in the transcript.

**Implication for layer 2:** never source a figure from a show-notes blurb, and
treat any claim that appears only there as unverified. Several are demonstrably
wrong, not merely promotional.

## One true duplicate: the archive holds 124 unique conversations, not 125

`2023-11-16-the-cost-of-nuclear` and `2024-08-15-the-cost-of-nuclear` are the
same conversation with the same guest (Jessica Lovering). The 2024 source URL
ends in `-2`, and Kann says inside the 2024 transcript "we're at the end of
2023." A 5-gram containment scan over all 125 transcripts puts the overlap at
99% and finds **no other near-duplicate pair**, so this is the only one.

Both notes were written independently and both are kept. They are not
redundant: the 2024 note deliberately carries material the 2023 note does not
(an illustrative $3,000/kW fixed-price example, the eight-reactor South Korean
project, Belgium's phase-out pause, Kann's restatement and Lovering's partial
endorsement, her internal $2,200-vs-$2,000 inconsistency, and the
publish-date/recording-date gap).

**Layer 2 must treat them as one conversation.** Any count of episodes, any
thread-frequency tally, and any "how often does the archive discuss nuclear
cost" statistic will otherwise double-count a single interview. Prefer the 2024
note when quoting, since it is the more complete of the two, but date the
claims to late 2023.

Method note for re-running the scan later: compare 5-gram sets of the
transcript body with frontmatter stripped, using containment
(|A∩B| / min(|A|,|B|)) rather than Jaccard, so a short episode nested inside a
longer one is still caught.

## Sponsors are sometimes in the episode's own business

Episodes carry sponsor reads, and the sponsor is occasionally a direct
commercial participant in the subject under discussion. Example: the
2025-09-18 DERs episode is sponsored by EnergyHub, which sells virtual power
plant and DERMS software, the episode's exact topic.

**House rule, decided deliberately: no per-note sponsor disclosure.** The
sponsor is not a speaker, states no position, and nothing in any transcript
suggests editorial influence. Adding a `disclosure:` field for it would produce
the prominent red-flag framing the notes are specifically meant to avoid, and
would misuse a field scoped to speakers' financial interests.

Recorded here once so the synthesis layer knows the pattern exists and can
weigh it if a sponsor's product ever turns out to be the thing an episode
recommends.

## Vocabulary decisions, for the record

Tags proposed by note-writing agents and resolved deliberately:

- **`ai-applications` — ADDED (v1.2).** AI as a tool used by the energy system,
  as distinct from `ai-compute`, which is AI as a load on it. The archive
  genuinely asks both questions and conflating them inverts several episodes.
- **`oil-markets` — ADDED (v1.3).** Crude balances, oil demand and oversupply
  appear in 11 episodes and nothing covered them. `fuels-and-shipping` reads as
  maritime and liquid fuels, not crude.
- **`fuel-cells` — ADDED (v1.3).** 6 episodes, including two on AI and data
  center power where fuel cells appear as onsite generation. Neither `hydrogen`
  nor `metal-fuels` covers that use.
- **`consumer-adoption` — DECLINED.** The concept matched loosely across ~25
  notes, which makes it a catch-all rather than a grouping. `public-opinion`
  plus the sector tags (`evs`, `buildings-efficiency`, `agriculture-and-land`)
  already carry the specific cases. Recorded so it is not re-proposed.

Zero `proposed_threads` fields now remain in the archive.
