---
post: "Duration is all you need"
published: "2026-04-08"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [energy-storage, long-duration-storage, batteries, market-design, demand-flexibility]
source_document: "essay.md"
note_version: 1
disclosure: "A bracketed note from Lubershane inside the guest essay says its modelled \"Iron-Air\" category effectively stands in for Form Energy, a portfolio company of his firm, Energy Impact Partners, and that he was pleased to see it perform well."
---

## The question

Once short-duration batteries have covered the daily peak, what kind of storage
does the power system still need?

## The answer

Longer-duration storage, and sooner than the current build implies. The
modelling finds that the room for four-hour batteries to count as full capacity
resources by 2031 is about the size of the fleet the United States has already
installed. Past that point the scarce thing stops being power and becomes
sustained energy.

## The argument

The argument belongs to Ben Haley and was first published by his firm, Evolved
Energy Research; Lubershane's contribution is an introduction recommending it,
plus a frame of his own about duration-limited resources. Haley starts from a
fact about the system being replaced. Coal, gas and nuclear plants had no
effective limit on how long they could run, so if a plant was needed in one
hour there was little concern about whether it could also run in the next, and
capacity adequacy could often be assessed without regard to chronology.
Hydro-dominated regions were the exception, constrained by water, and have long
planned around duration explicitly. What is being built now is overwhelmingly
four-hour lithium-ion, which suits the problem it was bought for: nearly every
system has needle peaks, one or two hours where load rises well above the
surrounding hours, and a short battery covers those while earning from
ancillary services. The essay is organized around what happens once those peaks
are covered.

The answer is that the system stops being capacity-limited and becomes
energy-limited, and it does so to itself. Haley's team ran net load, meaning
demand after wind and solar generation, across 100 scenarios for the United
States, calculating at every discharge duration how much dispatchable capacity
must persist in order to satisfy reliability criteria. Two structural features
fall out of the resulting curve: the system needs only a limited quantity of
capacity at short durations, and as duration lengthens the required capacity
declines but stays meaningful. He draws the parallel to renewables, where early
solar happened to generate during peak demand until enough of it was built that
the moment of system risk moved to the hours when wind and solar output is
lowest. Short-duration storage follows the same saturation logic, so an
additional four-hour battery must either accept a lower capacity rating or add
hours to reach the remaining need. The mechanism is that each addition flattens
the peak it was built to serve, which he calls being a victim of its own
success.

Which technologies then win depends on where along the duration axis the need
sits, and the modelled answer is not a simple march toward ever longer storage.
Lithium-ion occupies the short durations in virtually every run. Storage of
some type almost always serves needs out to roughly sixteen hours, and beyond
that it typically cannot compete with generation that has no duration limit at
all, such as gas. Storage becomes economic again only at very long durations,
above roughly ninety hours, where iron-air chemistry, with its high power cost,
low energy cost and low efficiency, is frequently competitive in the modelling.
He keeps that last finding qualified: the capacity needed at those durations is
smaller than at medium durations, and what multi-day storage can potentially
beat there is other low-utilization resources such as thermal plants running
peaker-like profiles. Cutting across all of this, a lot of four-hour
lithium-ion may still be built to serve longer peaks despite reduced
capacity accreditation, because arbitraging daily energy prices can pay enough
to carry it, most often in solar-heavy systems. What Haley concludes is
narrower than his title: the binding constraint migrates from instantaneous
discharge to sustained delivery, planning framed in gigawatts obscures that,
and overreliance on short-duration storage and load flexibility, including data
center flexibility, to keep pace with rapid load growth may itself introduce
reliability risk.

## What you need to know first

- **Power capacity versus energy capacity.** Gigawatts against gigawatt-hours.
A one gigawatt battery running at full output for four hours delivers four
gigawatt-hours. The essay's whole claim is that the scarce quantity switches
from the first to the second.
- **Net load.** Demand after wind and solar output is subtracted. It is what
dispatchable resources actually have to cover, and its shape rather than raw
demand sets the duration requirement.
- **Needle peak.** One or two hours in which load rises well above the hours on
either side of it.
- **Capacity accreditation, or effective load carrying capacity.** How much of
a resource's nameplate a system operator counts toward meeting peak demand.
De-rating means lowering that credit.

## Details worth keeping

- The document's frontmatter bylines Andy Lubershane, but the essay from the
heading "Duration is all you need" down to the bracketed "Back to Andy" is Ben
Haley's, written in the first person plural of his firm. The post gives him no
title beyond naming the firm as his.
- Lubershane's introduction is a recommendation rather than a claim he argues.
He calls it possibly the best wonky post on the techno-economics of the power
system he has encountered in years, says he invited Haley to cross-post it, and
says it should be required reading.
- The introduction supplies its own examples of duration-limited resources
beyond batteries. A heat pump on a smart thermostat can be turned down remotely
by a grid operator, but only until customers get cranky. Backup diesel and gas
engines increasingly tapped for distributed capacity are usually capped at a
maximum runtime per year in urban and suburban areas because of their effect on
local air quality.
- All three figures are uncaptioned. The prose carries the headline numbers,
but the scenario distributions themselves, for 2031 and for 2035, exist only in
the images and the note cannot reproduce them.
- The post closes with a bracketed "Back to Andy" line in which Lubershane
encourages readers to follow Evolved Energy Research. The footnote below it is
separate and describes the firm's own three proprietary modelling tools, among
them a supply-side optimization model and one that explores 100 near-optimal
system configurations rather than a single least-cost answer. That footnote is
the firm's copy about its products, not a finding of the essay.

## Claims worth citing

All figures as stated on 2026-04-08. Every number below is an output of one
firm's scenario modelling rather than an observation, except the installed
battery base and the Northwest Power and Conservation Council's planning metric.

- There will be only around 40 to 70 gigawatts of opportunity in 2031 for
batteries with just four hours of duration to qualify as full capacity
resources, roughly, across many potential scenarios. (Haley, Evolved Energy
Research)
- The United States has already surpassed 50 gigawatts of installed battery
capacity, nearly all of it with just two to four hours of duration. (Haley)
- Over the long term, capacity needs approaching roughly sixteen hours are
almost always served by storage of some type; beyond sixteen hours storage
typically cannot compete with duration-unlimited generation such as gas. (Haley)
- Storage becomes economic again above roughly ninety hours, with iron-air
batteries frequently competitive in the ninety to 150 hour range. (Haley)
- The Northwest Power and Conservation Council, planning a hydro-dominated
system, has long evaluated resource performance across durations using a
five-hour sustained-peaking capacity metric. (Haley)
- Some power markets may be relying too heavily on four-hour batteries, which
could lead to the need to de-rate those assets in future years. (Lubershane, in
his introduction, offered as a worry he is beginning to have)

## Where it's contested

Nothing in the post is contested. There is no second voice arguing, and the
only other voice present is the introducer, who is recommending the piece.
What is worth recording is the gap between the title and the body, and what the
analysis rests on.

- **The title overstates the essay.** Duration is not all you need on Haley's
own numbers: storage loses to duration-unlimited generation across the middle
of the duration range, and he expects a great deal of four-hour lithium-ion to
keep being built for arbitrage revenue even as its capacity credit falls.
- **The introduction is praise, not a finding.** Lubershane's assessment is of
the piece, and the one substantive claim he adds is hedged as a worry.
- **The evidence is one firm's proprietary modelling.** The cost and
performance inputs for competing storage technologies are the firm's own best
estimates from publicly available information, and nothing independent checks
either those or the tools.
- **An assumption the argument rests on and does not defend.** The case that
additional short-duration batteries must accept lower capacity credit assumes
accreditation rules will track the modelled marginal contribution. Lubershane's
introduction treats that as a change still to come, saying the calculation
needs to become much more sophisticated and dynamic.
- **What the introducer has at stake.** See the disclosure field: the iron-air
result concerns a technology he identifies with one of his firm's portfolio
companies, and he says so inline.
