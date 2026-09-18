---
episode: "Do data centers really increase electricity prices?"
published: "2026-09-10"
guest: "Andy Lubershane, partner and head of research, Energy Impact Partners"
threads: [data-center-power, electricity-prices, supply-chain-costs, public-opinion]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Are data centers making your electricity bill go up?

## The answer

No and yes, and which one is true depends entirely on whether you mean *your
utility bill* or *electricity prices generally*. A data center arriving in your
utility's territory will most likely hold your rates flat or push them down a
little. Meanwhile, at a global level almost every component of the grid is
getting dramatically more expensive, with data center demand the largest single
contributor but well short of the only one, so most people's bills are going up
anyway. Both things are true at once, and the gap between them is the whole
story.

## The argument

Start with how a utility actually sets rates. Take everything it costs to serve
every customer in the territory, divide by the total kilowatt-hours sold, and
that ratio drives the price. Now add a data center. It costs something to connect
and serve, which pushes the top of that fraction up, but it also buys an enormous
volume of electricity, which pushes the bottom up. If the bottom grows faster
than the top, everyone's rate goes *down*. Five years ago that held in a lot of
territories, because many grids still had spare capacity sitting around and a new
customer could be served without building much of anything.

That headroom is now gone. Serving a large new load today usually means new
generation, new transmission, substation upgrades, real money on the top of the
fraction. On the arithmetic alone the local answer became genuinely uncertain.
What rescues it is that rates are not set by arithmetic alone. For a mid-sized 
utility's entire load, a few-hundred-megawatt data center might add 10% or more 
while gigawatt-scale projects might be in the range of 30% or more. That makes 
it an extraordinary customer, and utilities have figured out that they hold the 
cards. They now negotiate bespoke deals that make the data center cover its own 
costs and then some. So the local answer lands back on 
neutral-to-slightly-positive, and utilities have started going to regulators
asking to *lower* rates because of large loads. Early evidence supports it: an
EPRI study found no correlation between data center presence and higher prices,
and a small benefit to customers once you control for confounding variables.

Then the picture inverts when you zoom out to the global level. Lubershane is
precise about the attribution here: data centers are one factor among many,
though the biggest one, behind a surge in electricity demand fast enough to count
as a genuine demand shock. Every link in the supply chain is bottlenecked and
prices show it, with conductor roughly doubled, transformers more than doubled,
switchgear doubled and gas plants two to three times more expensive. Renewables,
which spent a decade pushing prices *down*, now cost more to interconnect while
their tax credits wind down.

The rest of the pressure has nothing to do with AI at all. Tariffs, LNG exports
raising domestic gas prices, general inflation and a rising cost of capital for
an extraordinarily capital-intensive system all push the same direction and are
largely orthogonal to anything data centers are doing. And then the detail that
makes the whole thing bite hardest: roughly two-thirds of what US utilities spend
is not about growth in any form. It is maintenance and hardening, replacing
worn-out equipment, storm and wildfire work, and every dollar of it would be
spent if the data center boom had never happened. That non-negotiable two-thirds
now costs more too, because the supply chain squeeze raises the price of the same
transformer whether it is going into a new data center or replacing a broken one.
No local tariff negotiation touches any of this.

Which produces a genuinely awkward conclusion. Because the local effect is good
and the systemic effect is bad, the rational thing for any individual community
is to want as many data centers as possible in *their* territory. It is a
prisoner's dilemma: everyone competing for the local benefit while collectively
driving the systemic cost.

## What you need to know first

- **How rates get set.** Total cost to serve everybody, divided by total
kilowatt-hours sold. Nearly every argument in this episode is about whether a
new customer moves the top or the bottom of that fraction faster.
- **Headroom.** Spare capacity on the existing grid. When it exists, new
customers are cheap to serve. It is largely used up, which is why the old
intuitions about big new loads no longer hold.
- **Tariff.** The specific negotiated rate structure a utility sets for a large
customer. This is the lever that decides whether a data center subsidizes
everyone else or free-rides on them.



## Details worth keeping

- The public's stated objections do not match the analysis. In a recent Gallup
poll the top reason people oppose nearby data centers is water use, with energy
consumption second and electricity prices third. Lubershane thinks water is
largely a red herring outside genuinely water-stressed regions, while noting it
is not his area.
- There is a trust problem underneath the numbers. Even where data centers lower
rates *relative to what they would have been*, absolute bills still rise for
other reasons, so nobody perceives the benefit. Both hosts suspect people
distrust utilities, data center operators and politicians enough that the
rate argument may not land regardless.
- Energy is only about 5% to 10% of a data center's cost of goods sold, which
means operators could absorb substantially higher power prices. This is what
makes proposals to extract much larger community benefits arithmetically
plausible rather than fantasy.
- Electricity has held remarkably steady at 1% to 1.5% of average personal income
since 2010, and the share of income spent on electricity has been stable for
around 70 years. But for low-income and fixed-income households it can run 5%
to 10% or more, so the averages hide where rate changes actually hurt.
- Several inflationary pressures are unrelated to data centers: tariffs, LNG
exports raising domestic gas prices, general inflation, and a higher cost of
capital for an extremely capital-intensive system.
- On solutions, the honest answer is "all of it," but two get singled out. Energy
efficiency may finally pencil out for consumers and get treated by utilities as
a real planning resource rather than a compliance obligation. Load flexibility
and distributed batteries are the other, with utilities starting to procure
distributed capacity directly.



## Claims worth citing

All figures as stated on 2026-09-10 and attributed to the speaker, not verified
independently. Supply chain prices in particular are moving fast.

- Conductor roughly 2x more expensive, transformers 2x or more, switchgear 2x,
gas power plants 2-3x. (Lubershane)
- Combined-cycle gas turbines quoted in the $3,600-$4,000 per kilowatt range,
with both speakers noting each new data point sets a record. (Kann, Lubershane)
- About two-thirds of all US utility spending goes to maintenance and hardening
rather than growth. (Edison Electric Institute, cited by Lubershane)
- For a mid-sized utility, a few-hundred-megawatt data center might add 10% or
more of total load, while gigawatt-scale projects reach 30% or more. The source
sentence runs the figures together with an aside about gigascale, so it is worth
reading the transcript before quoting a precise split. (Lubershane)
- Data centers are one factor among many behind rising global power costs, and
the biggest single one, but not the only one. (Lubershane)
- Energy is roughly 5-10% of a data center's total cost of goods sold.
(Lubershane)
- Electricity has been 1-1.5% of average personal income since 2010, declining
slightly; 5-10%+ for lower-income households. (Lubershane)
- EPRI study: no naive correlation between data center presence and higher
electricity prices; a modest customer benefit after controlling for
confounders. Lubershane describes the effect as minor and puts a number around
6% on it, but the phrasing is loose enough that the base is unclear. Worth
reading the study before quoting the figure.



## Where it's contested

- **Whether the rate argument changes any minds.** Lubershane explicitly frames
this as an untested hypothesis: if operators and utilities offered genuinely
generous terms to other ratepayers, it is unknown whether opposition would
soften. He suspects the real driver is distrust and broader feelings about AI.
- **Whether water deserves its top billing.** Flagged as likely a red herring in
most locations, but explicitly outside the speaker's expertise.
- **How much the labor shortage matters.** Kann argues electricians are a small
share of total electricity cost, so it is not the main price driver. Lubershane
counters that it is "everything and nothing," small in cost terms but a hard
binding constraint, since an unstaffed substation does not get built. Both
agree it is the slowest problem to fix.
- **The systemic question is genuinely unstudied.** Local impacts are starting to
produce real data. Kann notes he has seen no comprehensive analysis of the
macroeconomic question and expects better evidence within about a year.

