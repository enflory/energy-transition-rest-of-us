---
episode: "Explaining the ‘Watt-Bit Spread’"
published: "2024-12-05"
guest: "Brian Janous, co-founder and chief commercial officer, Cloverleaf Infrastructure; previously vice president of energy at Microsoft"
threads: [ai-compute, data-center-power, utility-business, market-design, interconnection]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2024-12; the framework is durable but the capital costs, lead times and market conditions it is illustrated with are nearly two years old and move fast."
---

## The question

Why can data centers not get power, when the companies that want it are willing
to pay almost anything for it?

## The answer

Because the price of electricity does not reflect what electricity is worth to
someone converting it into compute, and nothing in a standard utility tariff lets
a customer pay for speed. Janous calls that gap the watt-bit spread, and argues
it is really a gap in the value of capacity in a given year rather than in the
price of energy. Until someone builds a way to price delivery timing, utilities
have no reason to hurry and buyers have no way to make them.

## The argument

The framework is borrowed from the spark spread, which power traders use to
compare the cost of a unit of gas against the value of the electricity that unit
can produce. Janous applies the same shape one conversion downstream. The data
center industry exists to turn watts into bits, so the relevant spread is between
the cost of the electricity going in and the value of the compute coming out. He
thinks no energy conversion in the economy returns more. The value side has risen
steeply over the previous 18 to 24 months, and not only because compute earns
revenue: securing electrons is itself a moat, since whoever holds the power can
train larger models and run more inference. The cost side has barely moved,
because a standard utility tariff does not reprice when demand surges. The
practical consequence of the gap is a price signal that never arrives. If
utilities and independent power producers cannot see what the next watt is
actually worth, they build less infrastructure and fewer GPUs get plugged in, and
the same muted signal fails to reach the people making transformers and
switchgear.

To use the framework you need three inputs, and the third is the one that gets
lost in summaries. The first is what a watt is worth to a compute buyer, which is
high. The second is what the buyer currently pays, which is the prevailing
tariff. The third is the year of delivery. Janous is explicit that the spread is
about the value of capacity in a given year: a megawatt in 2027 is worth more
than a megawatt in 2032, because by 2032 he expects power to be relatively more
abundant and the scarcity premium to have decayed. So the spread is not one
number but a term structure that narrows as you look further out, and the thing
being mispriced is not energy but the timing of the first electron. That
reframing is what makes the framework operational: a utility should be hunting
for investments that pull delivery forward, and for customers who will pay more
for 2027 than for 2032. The premium shows up as higher demand charges recovering
the cost of acceleration rather than as a permanently higher price per
megawatt-hour, and it is underwritten by the fact that data centers run 8,760
hours a year and do not get switched off, so the asset stays used and useful.

The reason the gap persists is that the two sides of the table are running
different playbooks. Downstream players, which is to say cloud providers, chip
makers and model developers, think in terms of the theory of constraints, where
enterprise value comes from throughput and you therefore overbuild at the
bottleneck and pay a premium to clear it. That is rational for them because base
infrastructure is cheap relative to the whole stack. Land is about 1% of the
fifteen-year total cost of ownership, and the full build including GPUs runs
about $25 million per megawatt, so the roughly $1 billion of utility work behind
a gigawatt sits in front of some $24 billion that follows it. A utility faces the
opposite arithmetic: it sells an electron in 2027 for the same price as one in
2030, which gives it no reason to stockpile 345 kilovolt transformers or to
compress a schedule, and a lead time stretching from two years to seven is
absorbable inside that model. Janous says that is not ultimately in the utility's
interest, since it should want more customers sooner, but its business model was
not designed for this. Kann pushes back that the framing understates the
constraints utilities live under, including regulators with their own priorities,
a mandate to put reliability first, and a rate-of-return structure that governs
what they can spend and recover. Janous's answer is the instrument he calls an
advanced grid tariff, named by Katie Fehrenbacher: the same logic as a green
tariff, where a customer who wants a particular quality of service pays for it
without harming other ratepayers, except that here the thing being bought is
speed. A utility identifies technologies that can be deployed quickly, grid
enhancing technologies, dynamic line rating, storage used as transmission, long
duration batteries, and recovers their cost from the specific customers who want
power in 2027 instead of 2030.

Where it breaks down is on the durability of the spread and on who is good for
the money. Kann's sharpest challenge is that the spread may be an artifact of the
cycle, inflated by an arms race and a lot of capital sloshing around, and that an
infrastructure owner is being asked to commit to assets lasting 20 to 40 years
against willingness to pay that is only visible to about 2030. Janous concedes
the possibility and then states a belief rather than evidence: he expects demand
for compute to exceed available power through 2030, so the marginal gigawatt
stays valuable until equilibrium returns. The second weakness is buyer quality.
Utilities cannot easily tell a hyperscaler from what Janous calls two guys with a
truck, when a queue position can cost as little as $10,000 and a single utility
can be sitting on tens of gigawatts of requests. His filter is capital: anyone
holding a gigawatt of queue position should be able to point to billions of
dollars they have access to, and if they cannot they are not a serious player.
The third constraint is political rather than analytical. Both speakers say
directly that they do not want residential rates rising to serve AI, which means
the whole design depends on cost allocation being done properly, with benefits
flowing to other ratepayers through better reliability or lower cost. Kann makes
that condition explicit and immediately adds that he does not know how far it can
go.

## What you need to know first

- **Spark spread.** The margin between the cost of the natural gas burned and the
  value of the electricity produced from it. The watt-bit spread copies its shape
  one step further downstream, from electricity to compute.
- **Tariff and demand charges.** A tariff is the rate structure a utility charges
  a class of customer. Demand charges bill for the capacity made available rather
  than for the energy consumed, which is why they are the natural place to put a
  premium for getting connected sooner.
- **Theory of constraints versus lean manufacturing.** Lean holds as little
  inventory as possible and accepts longer lead times to protect margin. Theory
  of constraints maximizes throughput by deliberately overbuilding capacity at
  whatever step is the bottleneck. Janous's claim is that the buyers run the
  second and utilities effectively run the first.
- **Hyperscalers and colocation.** Hyperscalers such as Microsoft, Amazon, Google
  and Meta build mainly for their own platforms. Colocation companies build
  capacity and lease it out, and historically filled the gap when hyperscalers
  underbuilt.

## Details worth keeping

- Kann opens by contrasting the two industries' clock speeds. Natural gas went
  from about 17% of US power generation in 2000 to 40% by 2020, a seismic shift
  by energy standards, and it took twenty years to get 2.3 times the market
  share.
- Janous joined Microsoft in 2011 and says it was not obvious to him then why the
  job existed. He relays an old manager's line that Steve Ballmer probably thought
  about energy one minute a year, and says energy has since become existential for
  anyone touching cloud and AI.
- The companies that filled the capacity gap in the 2010s were built on real
  estate and fiber skills. Janous argues their energy benches are thin, so they
  are poorly equipped to fill the gap this time, when the question is not proximity
  to Northern Virginia but where to find a gigawatt.
- In a world of power abundance, buying land put you roughly 18 months from
  serving traffic at trivial cost. Now the entry ticket is land plus clear line of
  sight to power on an 18 to 24 month horizon, which can mean multi-billion dollar
  purchase and cancellation agreements with a utility.
- Labor gets flagged as an underrated constraint precisely because of the power
  problem. Today's data centers are roughly ten times the size of recent ones, and
  the search for power is pushing everyone toward remote sites; if too many do it
  at once, construction labor becomes the delay.
- Janous names AEP as a leader on guaranteeing cost recovery through minimum
  take-or-pay commitments, which creates friction with hyperscalers who lack
  visibility into their own future demand. Kann recalls a recent settlement in
  MISO territory between hyperscalers and a utility on large load interconnection,
  without naming the utility.
- The template for the advanced grid tariff is Google's arrangement in Nevada to
  be served by a Fervo geothermal project. Among the accelerating technologies
  Janous names is Form Energy, which he identifies on air as an EIP portfolio
  company, alongside LineVision for dynamic line rating.

## Claims worth citing

All figures as stated on 2024-12-05. Capital costs, lead times and queue volumes
in this market move quickly, and several figures below are offered as
illustrations rather than survey data.

- Land is about 1% of the total cost of operating a data center over fifteen
  years, counting the full stack including servers. (Janous)
- Full-stack data center capital expenditure runs about $25 million per megawatt,
  or $25 billion per gigawatt, including GPUs. (Janous)
- A gigawatt of utility infrastructure is on the order of $1 billion, which he
  frames as small next to the roughly $24 billion of capital that follows it.
  Offered as an illustrative example, not a quoted price. (Janous)
- A queue position can be obtained for as little as $10,000, which he calls
  shockingly low. No utility is named. (Janous)
- Interconnection timelines that used to be two years are now seven in his
  illustration of utility behavior. Stated as an example of the pattern rather
  than a measured average. (Janous)
- Data centers consume power 8,760 hours a year, which is the whole year, and
  once a customer is there they do not go away. (Janous)
- A single utility facing 80 gigawatts of large load requests, much of it not
  real. Kann's example; the utility name is garbled in the transcript and is
  probably AEP, which is named later in a different context. (Kann)
- The "$600 billion question": announced and planned capital expenditure from the
  major data center players totals roughly $600 billion, which has to be matched
  by revenue and ideally earnings. (David Kahn of Sequoia as transcribed, cited
  by Kann)
- Natural gas rose from about 17% of US power generation in 2000 to 40% in 2020.
  (Kann)
- Janous has worked on data centers and energy for at least 13 years. (Janous)

## Where it's contested

- **Whether the spread is real or cyclical.** Kann asks directly whether it is
  artificially inflated by where we are in the cycle. Janous answers "it's
  possible," then gives a belief rather than evidence: that compute demand will
  exceed available power through 2030 and the marginal gigawatt stays valuable
  until equilibrium returns. Nothing in the episode tests this.
- **Whether utilities really lack the incentive to hurry.** Janous's theory of
  constraints framing implies they simply have no reason to move. Kann qualifies
  it, arguing that regulators, reliability obligations and the regulated
  rate-of-return model constrain utilities in ways the framing understates, and
  that they have already begun adjusting to the new volume of requests.
- **Whether the timing premium survives contact with asset lives.** Kann's
  objection is that 20 to 40 year assets are being underwritten by visibility that
  runs to roughly 2030. Janous answers with demand charges recovering acceleration
  costs and with the claim that data center load never leaves, which is an
  assumption about the durability of the customer rather than a demonstrated fact.
- **Whether other ratepayers benefit.** Kann says he wants to make explicit what
  he takes to be implied, that the accelerating investments should raise
  reliability or lower costs for everyone else, and then says he does not know how
  far that can go. Janous agrees that rates should not rise for ordinary consumers
  to serve data centers, and rests on cost allocation practices utilities already
  use. It is a design intention, not a result.
- **Why buyers resist the price.** Asked whether customer pushback is negotiating
  posture or genuine failure to grasp the spread, Janous says some of both, and
  distinguishes sophisticated big-tech energy teams from entrants who recently
  pivoted from bitcoin mining or green hydrogen. He does not resolve which
  dominates.
- **The guest's position.** Janous co-founded a company that develops power-ready
  sites for large loads, so a framework concluding that speed to power is
  underpriced aligns with his business. He says so implicitly by using his own
  company as an example of a developer that should face stricter capital tests.
