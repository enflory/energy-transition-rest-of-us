---
episode: "When to colocate data centers with generation"
published: "2025-09-12"
guest: "Brian Janous, co-founder and chief commercial officer, Cloverleaf Infrastructure"
threads: [data-center-power, interconnection, demand-flexibility, gas-buildout, nuclear]
source_transcript: "transcript.md"
note_version: 1
---

## The question

When does it actually make sense to build generation on site at a data center,
and when has the idea simply become fashionable?

## The answer

Almost never for the reasons usually given: Janous argues the economics are bad,
the speed advantage is weaker than it looks because gas pipelines are congested
too, and the premise underneath both is wrong, since utilities are trying to
survive a handful of peak hours rather than match a 24/7 load with a 24/7
machine. The version that holds up is using on-site resources to shrink how large
you look to the grid, and even there generation competes with storage, demand
response and grid upgrades. The weak point he concedes is that this alternative
requires orchestration across thousands of utilities.

## The argument

Start with the clarification that reframes everything. Nearly every cloud data
center already has generation on site: diesel backup gensets, sized for rare
transmission-level outages and limited by air permits that cap runtime and eat
into the allowance needed just to test them. What is new is generation meant to
be prime power, running close to around the clock alongside a grid connection.
The case for it has two parts. First, speed: if the utility says five to seven
years for a connection at the scale you want, building your own might be faster.
Second, that a 24/7 load needs a 24/7 generation source to match it, an argument
Janous hears from the current administration as a case for more baseload plants
and calls flatly false.

He attacks the second part first, because it decides what problem you are
solving. A utility does not study whether it can supply you across all 8,760
hours of the year. It asks whether adding you pushes the system past what it can
serve on the hottest summer afternoon and the coldest winter morning. That makes
this a capacity problem rather than an energy problem, and capacity problems have
far more solutions than building a machine that runs constantly. Janous describes
the grid as moving power through space and time, so its pieces substitute for
each other: a transmission line substitutes for baseload generation, since moving
power across congestion reduces what has to be generated locally, and
long-duration storage substitutes in turn for transmission. Add grid-enhancing
technologies, advanced conductors, storage of varying durations and virtual power
plants, and you can replicate a 24/7 output with a dozen things instead of one,
faster because much of it already exists and cheaper because you build less.

The economics are unattractive, though not disqualifying. Work the arithmetic on
a 100-megawatt data center: a power usage effectiveness of 1.2 puts you at 120
megawatts of generation, redundancy adds 20 or 30 more, so you build 150 and run
it at perhaps 90 on average, because data centers chronically underuse nameplate.
At roughly $2,700 per kilowatt with an overbuild approaching 2x, the cost per
kilowatt-hour is extraordinarily high: in Texas something like $150 to $200 per
megawatt-hour around the clock, while the data center next door buys grid power
near $20 and the old reason to own a baseload machine there, occasional scarcity
prices of $5,000 to $9,000, has been decimated by solar and storage. But Kann
turns Janous's own bit-watt spread back on him: electricity is small against what
a data center earns, so a developer might pay the premium for speed anyway.
Janous concedes it, probably in a lot of cases. Overpaying is not a deal killer,
just no economic benefit and worse margins than a competitor who got grid access.

Which leaves the version both accept: not going off-grid, but shrinking your
interconnection footprint, siting a 500-megawatt data center where the utility
can deliver 300 and holding your grid draw under that ceiling. Janous agrees,
then reframes it as orchestration, because behind-the-meter generation is only
one way to fill the gap. A long-duration battery on the utility's side of the
meter might do the same job, and the fastest option builds nothing: aggregate
enough sheddable load inside the deliverable zone that the utility credits it as
capacity. Nobody has done that at real scale, and vertically integrated utilities
object that they want rate base rather than a program, to which Janous answers
that a virtual power plant is a bridge letting them connect the load sooner and
build against it later. The limit he volunteers is that this is where his
argument may fall apart: orchestrating across roughly 3,000 US utilities and
several regional markets with different accreditation rules is hard, and the tool
that would price a stack of capacity options for any point on the grid, trusted
by utility and developer alike, does not exist. On-site nuclear, meanwhile, fails
every test at once. It is not faster, not cheaper early, you will already hold
your full interconnection by the time it arrives, and no one plugs a $20 billion
facility into a novel reactor without a decade of operating data.

## What you need to know first

- **Behind the meter.** Generation on the customer's side of the utility meter,
serving the facility directly instead of selling into the grid.
- **Capacity versus energy.** Utilities plan against system peaks, not annual
consumption, so anything that cuts your draw in those few hours can substitute
for generation that runs all year.
- **Capacity accreditation.** How much of a resource's nameplate rating a grid
operator counts as firm. It decides whether batteries or shed-able load can stand
in for a generator in an interconnection decision.
- **The bit-watt spread.** Janous's term for the gap between what electricity
costs a data center and what the compute earns. It is wide enough that power
price is rarely the deciding factor.

## Details worth keeping

- AI training sites are moving away from backup generators, partly because a
training run can tolerate a rare outage and partly because diesel at gigawatt
scale is difficult to permit in most markets. xAI's Colossus site did build them
anyway, though Janous notes it is smaller than recently announced sites, citing
1.3 gigawatts in Port Washington, Wisconsin and around 1.4 in Abilene.
- Going off-grid assumes gas is available where electricity is not. Janous says
gas congestion is real and you cannot put a pipe in the ground anywhere and get
unlimited supply.
- Data centers have always been microgrids, designed for two power sources, but
reaching the redundancy an engineer expects from an islanded system requires a
significant overbuild.
- On-site wind and solar combinations work where land is abundant, such as West
Texas, but stay a small share of the market because most demand wants to sit near
major metros.
- Both speakers are bullish on new nuclear in the US generally. The objection is
specifically to putting it behind a data center's meter.

## Claims worth citing

All figures as stated on 2025-09-12, attributed to the speaker rather than
independently verified. Equipment prices and interconnection timelines move fast.

- Roughly $2,700 per kilowatt for on-site generation, described as a rough
number. (Janous)
- Worked example, not a measured case: 100-megawatt data center, power usage
effectiveness of 1.2, plus 20 to 30 megawatts of redundancy, giving about 150
megawatts built against a 90-megawatt average draw. (Janous)
- One data center operator reported average utilization of 40% to 50% of
nameplate over a year. (unnamed operator, cited by Kann)
- Off-grid power in Texas at roughly $150 to $200 per megawatt-hour around the
clock versus a real-time grid price near $20, with Janous noting he excludes
transmission and distribution charges from the grid side. (Janous)
- ERCOT scarcity prices used to reach $5,000 to $9,000 per megawatt-hour and have
largely stopped appearing; Kann agrees volatility there is down. (Janous, Kann)
- Utilities quoting five to seven years for large connections, given as the
premise of the speed argument rather than a surveyed figure. (Janous)
- Roughly 3,000 utilities in the United States. (Janous)
- No credible argument for behind-the-meter nuclear for the next couple of
decades, with about ten years of operating data needed before anyone connects a
$20 billion to $50 billion facility to a new reactor design. (Janous)
- An 11-gigawatt campus near Amarillo is mentioned, but the transcript garbles the
developer's name, rendering it as the company named earlier for 100-hour
batteries. Check it before repeating. (Kann, Janous)

## Where it's contested

- **Janous names his own weak point.** Asked whether the multi-resource approach
can be done programmatically rather than as bespoke deals, he says this is where
his argument maybe falls apart. It has to work across thousands of utilities and
several regional markets with different accreditation rules, and the software
that would make it routine does not exist yet.
- **How much grid headroom exists is a judgment call.** Kann frames the
disagreement explicitly: the prevailing view is that necessity forces colocation
even when it is suboptimal, while Janous thinks more interconnection capacity is
reachable on a reasonable timeframe. Janous confirms that is his view. Neither
offers data; it is a difference in expectation.
- **He is a commercial participant in the answer he prefers.** Janous says
Cloverleaf's business is working with utilities case by case to connect load
faster, the same approach he argues should win.
- **Using demand response as interconnection capacity is untested.** Kann knows
of nobody who has implemented it and notes accreditation at that level is nuanced
and geographically constrained. Janous agrees no one has done it at real scale,
says Cloverleaf is close on a couple of projects and expects it soon. That is a
forecast from an interested party.
- **Firm gas supply is raised and then parked.** Janous questions whether a firm
gas connection is obtainable, then explicitly sets the issue aside.
- **The cost argument does not settle the decision.** Janous accepts developers
may build uneconomic on-site generation anyway, because revenue from operating
sooner outweighs the power premium.
