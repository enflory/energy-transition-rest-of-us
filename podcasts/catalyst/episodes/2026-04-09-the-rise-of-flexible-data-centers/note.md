---
episode: "The rise of flexible data centers"
published: "2026-04-09"
guest: "Varun Sivaram, CEO, Emerald AI"
threads: [demand-flexibility, data-center-power, interconnection, utility-business, ai-compute]
source_transcript: "transcript.md"
note_version: 1
disclosure: "EIP portfolio company. Kann states on air that EIP led a $25 million round in Emerald AI announced a couple of weeks before recording, that he invested, and that he and Sivaram are now on the same side of the business; Siemens, Eaton and GE Vernova also joined the round. Routine for this show; noted so that company demonstration results are attributed to the company rather than read as independent measurement."
---

## The question

Almost everyone now agrees data centers should be flexible grid assets. What is
actually stopping it from happening at scale?

## The answer

The utility side, not the compute side. Sivaram argues AI workloads already
carry substantial inherent flexibility and cloud providers are already selling
differentiated service tiers, while electric utilities still offer essentially
one product: firm power. What is missing is a non-firm service tier that trades
occasional curtailment for a faster or larger grid connection. He believes that
if grids offered it, the rest of a genuinely complicated multi-party problem
would fall into line.

## The argument

Start with the intuition the episode exists to overturn. Data centers have been
treated as the most inflexible load on the planet, historically declining demand
response and demanding extreme redundancy. The economic version is sharper: an
AI accelerator turns power into extremely valuable tokens, so curtailing one
looks obviously irrational, and Sivaram says that intuitive blocker is part of
why he has so little competition. Kann's framing is that most people in the
market would locate the constraint there, on the compute side. Both then argue
the compute side is the part that is moving. Google has announced flex and
priority inference tiers, where a developer chooses between immediate and
delayed delivery at different prices and, more importantly, at genuinely
different service levels. Anthropic has peak and off-peak periods where rate
limits bite earlier. And a March 2026 paper from Emerald's chief scientist and
co-authors finds 18 to 55 percent power flexibility across representative AI
workloads. On the utility side, by contrast, you get one service level, which is
that you get power.

Why that gap matters is the stranded capacity argument. The grid runs at roughly
50 percent utilization or less for most of the year, which Sivaram translates
into more than 100 gigawatts of capacity that could serve AI factories today if
they would ramp down partially during rare peaks, perhaps 50 to 200 hours a
year. Set that against the demand numbers he cites, a NERC forecast in January
of a 224 gigawatt summer peak increase almost all from data centers and an EPRI
projection that data centers could use up to 17 percent of American power by the
end of the decade. If the only response is building, he argues, you get higher
rates and slower AI growth at the same time.

The economics are where the argument turns, and where the two men partly
disagree. Both accept that traditional demand response does not work here: if
the reward for curtailing is a smaller electricity bill, the value of the tokens
you did not generate dwarfs the saving, which is the watt-bit spread Kann
attributes to Brian Janous. What flips the calculation is not money but access.
Sivaram's example is a 200 megawatt data center able to reach 230 megawatts a
year ahead of schedule while swapping in liquid cooling and next-generation
accelerators, which he puts at billions of dollars of value, easily covering the
cost of curtailing during rare peak hours. He half-disagrees with Kann on the
operating-cost half of it, arguing some workloads already pencil today because a
data center can sit at a point on the power-performance curve where it sheds
much more power than performance, and that as the cost of generating tokens
falls toward the cost of power, the only real operational input into
intelligence, responding to prices will increasingly pay for itself.

The obstacle he does not minimize is that a data center is not one entity. There
may be a developer and operator, a tenant cloud provider, an inference-serving
company above that and an end customer above that, and all of them have to
cooperate for net withdrawal at the grid connection to move. His answer is that
the incentive has to come from the top: if utilities, system operators,
regulators and governors say a flexible data center connects faster and bigger,
everyone below aligns. Behind-the-meter equipment then becomes an amplifier
rather than an escape. Sivaram argues AI factories belong on the grid and calls
the opposite view shortsighted, because a load heading toward a quarter or more
of national electricity is the system's anchor tenant and losing it would be a
catastrophe for everyone's rates. Bridge power is rational in the near term and
should be folded back into grid service once the connection arrives. Kann
proposes a mini dispatch curve as the organizing idea: inside a single site,
workload flex is the cheapest increment and should be used first up to the point
where customer performance suffers, then generators, batteries or fuel cells.
Sivaram likes the analogy but insists the curve is dynamic rather than static.

## What you need to know first

- **Firm versus non-firm service.** Firm service is the promise utilities have
  made for a century: you get power whenever you ask. Non-firm means cheaper or
  faster access in exchange for accepting occasional curtailment. Sivaram's
  whole argument is that the non-firm product does not exist for data centers.
- **Stranded grid capacity.** Capacity that physically exists but goes unused
  because the system is sized for a handful of peak hours.
- **The watt-bit spread.** A term Kann attributes to Brian Janous, rendered
  "Bitwat spread" in the transcript, for the gap between what a data center pays
  for electricity and what it earns from the computing that electricity powers.
  The gap is why bill savings alone cannot motivate curtailment.
- **Workload flex.** Slowing, delaying or relocating computing jobs so the site
  draws less power, as distinct from firing up an on-site generator to replace
  grid power. Both look the same to the grid and cost very different amounts.

## Details worth keeping

- Emerald has run five commercial demonstrations since Sivaram's previous
  appearance, with partners including NVIDIA, EPRI's DC Flex initiative, Oracle,
  Nebius and National Grid, on production-grade workloads using real models from
  OpenAI, Meta and Alibaba, excluding anything a customer labeled
  mission-critical.
- The London demonstration cut power 30 to 40 percent during the halftime kettle
  spike of a soccer match and responded within seconds to a simulated lightning
  strike. With Oracle, inference queries moved from Virginia to Chicago within
  milliseconds during Dominion's winter peak. Another addressed a heat dome with
  Portland General Electric and NVIDIA.
- NVIDIA announced a reference architecture for AI factories called DSX at
  CERAWeek, with a DSX Flex component; Emerald is a software partner and six of
  the largest American power companies joined. Designs including bridge power are
  called hybrid AI factories.
- Later in 2026, Emerald, NVIDIA, Digital Realty, EPRI, Dominion and PJM plan
  what Sivaram calls the world's first 100 megawatt commercial-scale AI factory
  built from the ground up to be power flexible.
- A battery behind the meter creates a flexibility requirement of its own. A 200
  megawatt site with a 200 megawatt interconnection cannot charge one without
  either a bigger connection, which Kann says nobody can get, or workload flex to
  make room.

## Claims worth citing

All as stated on 2026-04-09. Several of these are forecasts rather than
measurements, and the demonstration results come from the company.

- NERC forecast in January of a 224 gigawatt summer peak increase, almost all
  from data centers. Sivaram calls that between a quarter and a third of peak
  demand but does not state the forecast horizon or base year, so the window is
  unclear. (NERC, cited by Sivaram)
- Data centers account for 94 percent of PJM's projected peak load growth, with
  no source named, and could use up to 17 percent of America's power by 2030.
  (the second figure from EPRI, both cited by Sivaram)
- The grid runs at roughly 50 percent utilization or less for most of the year,
  leaving more than 100 gigawatts of stranded capacity. (Sivaram)
- 18 to 55 percent power flexibility across representative AI workloads spanning
  training, inference and fine-tuning. (March 2026 paper by Emerald's chief
  scientist Ayse Coskun of Boston University with two co-authors, cited by
  Sivaram)
- Flexible service tiers would require curtailment on the order of 50 to 200
  hours a year, stated loosely as a range. (Sivaram)
- Google has reached a gigawatt of contracted flexible capacity across about five
  utility territories, hedged with "I think" and "at least some of whom" provide
  connection benefits. (Sivaram)
- Taking a 200 megawatt data center to 230 megawatts a year early, with a cooling
  and accelerator upgrade, creates billions of dollars of value. Illustrative,
  not a measured case. (Sivaram)
- More than 3,000 American utilities. (Sivaram)

## Where it's contested

- **The host is an investor.** Kann discloses that EIP led a $25 million round
  in Emerald weeks earlier and that he is now on the same side of the business.
  Routine for the show, and he still pushes back in places, but the demonstration
  results and the claim that essentially nobody else does this come from the
  company.
- **Whether operating-cost savings alone ever justify curtailment.** Kann says
  no, because of the watt-bit spread, and that only faster or larger
  interconnection flips the math. Sivaram half agrees, claiming some cases pencil
  today and more will as inference costs fall toward power costs. Neither
  resolves it.
- **Causation on electricity rates is deliberately scoped.** Sivaram says
  historically the drivers of rate increases may well not have been data centers,
  that data centers may have been conflated in the data, and that some data shows
  rates rising more slowly where data centers grew faster. His claim is
  conditional: if data centers drive most peak load growth and peak load drives
  most rate increases, then without mitigation they could drive affordability
  problems.
- **The central product does not exist yet.** There is no non-firm service tier
  for data centers, which he says is for good reason given a century of firm
  service obligations and unresolved legal questions. The 100 megawatt facility
  is planned, not built, and his timing for takeoff in late 2026 and 2027 is a
  forecast by an interested party.
- **The dispatch curve analogy is accepted with a caveat**, since Sivaram says
  battery duration limits, forecasting and workload arrival patterns reshuffle
  the order continuously. He also acknowledges that his position that AI
  factories belong on the grid is counterintuitive, and that the pull toward
  going off-grid is a live counterforce.
