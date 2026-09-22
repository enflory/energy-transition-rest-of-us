---
episode: "Making DERs work for load growth"
published: "2025-01-09"
guest: "Pier LaFarge, co-founder and CEO, Sparkfund"
threads: [ders, load-growth, utility-business, energy-storage, data-center-power]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2025-01, when distributed capacity procurement had barely been tried; the capacity accreditation values and the state of utility and regulator adoption are the parts most likely superseded."
disclosure: "Sparkfund is a portfolio company of Energy Impact Partners, where Kann is a partner. Kann states this on air and it also appears in the show notes."
---

## The question

Load growth is being answered almost entirely with big centralized projects. Can
distributed energy carry a real share of it, and how would a utility actually
buy it?

## The answer

Yes for a share of it, and the trade is explicit rather than free. Distributed
solar and storage cost more per megawatt than centralized equivalents and are
credited with less capacity, but they can be built much faster, and LaFarge
argues the premium is covered by stacking avoided grid costs on top of the
capacity value and by large new customers who will pay for speed. His proposed
mechanism is distributed capacity procurement: the utility puts distributed
capacity into its resource plan, pays for the assets, hosts them on customer
buildings and dispatches them itself. Neither speaker claims it substitutes for
central generation at system scale, and both say so directly.

## The argument

The premise LaFarge starts from is that the load growth consensus formed
unusually fast and that its scale is now being understated rather than
exaggerated. Electric vehicles were the largest driver of electrification growth
two years earlier and are now, in his description, a distant third behind
manufacturing and data centers. He raises the obvious skeptical response himself
and calls it sober: the internet and personal computing were once forecast to
create a legendary amount of new demand, and efficiency gains swallowed it. His
answer is a robustness claim rather than a forecast. Haircut the data center and
manufacturing projections by 80% or 90% and you still double the grid, which he
argues makes doubling a degraded baseline rather than a high-side case. The
reason to look at distributed resources in that world is not that they are cheap
or clean but that they are fast: it is easier to build many small things quickly
than a few large things slowly, and permitting, interconnection queues,
environmental review and capital formation all bite hardest on the large things.

Distributed capacity procurement is his name for doing the ordinary thing with
unusual assets. Strip the first word and it is what utilities have done for a
century: work out how much capacity you need and where, buy it, and run it.
Keeping the first word changes the asset rather than the logic. He argues most
of that capacity ends up on customer property for a pragmatic reason rather than
an ideological one, which is that in the parts of the grid where capacity is
actually needed, downtown Atlanta or Minneapolis being his examples, there is
nowhere to put batteries except on and around buildings. The commercial form is
a host agreement: the utility rents the space and pays the building owner a
long-term annuity for the asset's life, with no debt, no financing and no
maintenance obligation on the host, often plus first call on backup power or a
guaranteed share of the battery during an outage. Set against a virtual power
plant, he calls this a utility-led version. The assets are paid for by the
utility as grid infrastructure and dispatched by the utility, possibly through
an aggregator's control layer, and the starting point is solar and batteries
with thermostats, water heaters and vehicles as later additions.

The economics are where he concedes most and recovers it with a value stack.
Distributed resources are more expensive per megawatt, and their accredited
capacity is lower. His first illustration is a comparison Kann rejects, a gas
plant accredited near 80% against standalone solar at 8%, and he accepts the
correction that the fair comparison is rooftop solar against utility-scale
solar, leaving a residual of construction cost spread over fewer megawatts plus,
as Kann adds, the soft costs that get worse as projects get smaller. Pairing
solar with storage pulls accreditation back into the high fifties or low
sixties, and his rule of thumb is that about 1.6 gigawatts of nameplate solar
and storage buys a gigawatt of accredited capacity. The premium becomes payable
only if you count everything the sited asset displaces: compare the accredited
capacity against a peaker plant, add congestion value where the asset sits on a
constrained part of the network, subtract transformers that no longer need
replacing, which matters because transformers are expensive and supply
constrained, and then subtract substation rebuilds, feeder upgrades and even
transmission. He says that math looks good so far while stressing that it is
early and that utilities and regulators are only beginning to do the modeling
that would locate the value. The rest of the premium, on his account, gets paid
by large new loads, not because they are rich but because they value time to
power, which he ties to a 1947 analogy about grid investment unlocking the
postwar manufacturing economy.

The limit gets put on the table by both of them, which is the most useful part
of the conversation. LaFarge's thought experiment is that Microsoft's 800
megawatt contract for the restarted Three Mile Island unit delivers power onto
the grid rather than next to the data center, so in principle 800 buildings each
hosting 1.6 megawatts of solar and storage could substitute for it. Kann's
pushback is that nuclear runs around the clock and solar plus storage does not,
so the substitution holds for one project but not at system level, where you
would still need more storage, more generation, or gas backup. LaFarge does not
resist. He says he does not know whether the accreditation arithmetic breaks
down at system scale for physical reasons such as inertia, load management and
conductor temperature, suggests accreditation may be more a contractual and
market construct than a physical one, and invites listeners to correct him. On
scale limits generally his answer is that nobody knows, because it has not been
tried at this scale. Both of them land in the same place: distributed belongs in
the mix on speed grounds, and for every public conversation about a nuclear
restart there should be one about a feeder full of buildings.

## What you need to know first

- **Distributed energy resources.** Small generation, storage and controllable
  loads sited at customer premises rather than at a central plant. In this
  episode it mostly means rooftop solar and building-sited batteries.
- **Capacity accreditation, or effective load carrying capacity.** Grid
  operators discount a resource's nameplate rating to what it can be counted on
  to contribute when the system is stressed. Nameplate times that percentage is
  what counts toward a capacity requirement, so a low accreditation means you
  must build more of the thing to meet the same obligation.
- **Integrated resource plan.** The regulated plan in which a utility states how
  much capacity of what type it needs and when. LaFarge's whole proposal is
  about getting distributed capacity written into that document, because that is
  what forces the siting and optimization work to happen.
- **Feeder.** The distribution circuit that serves a particular set of
  buildings. It is the unit at which his examples of distributed benefit,
  congestion relief and deferred upgrades are measured.

## Details worth keeping

- The feeder picture he keeps returning to: 900 buildings on one circuit, solar
  and storage on 500 of them, producing what he calls fractal reliability and
  blurring the distinctions between resilience and reliability, and between
  behind the meter and in front of it.
- Kann's explanation for why utilities were slow to react to data center growth:
  they had been burned by Bitcoin miners promising hundreds of megawatts of
  flexible load that evaporated when prices crashed, and they had already been
  serving cloud data center growth, so the new trajectory read at first as more
  of the same rather than a different paradigm.
- The host deal is deliberately undemanding on the customer. A payment stream
  for the asset's life, which he puts at 10, 15 or 20 years, with no obligation
  to finance or maintain anything, and typically backup priority or a reserved
  share of the battery, 20% or 50% being his examples.
- Distributed capacity procurement starts with hard assets and extends
  downstream to thermostats, connected appliances, water heaters and vehicles.
  Kann notes that this second category is much harder because load shifting
  requires counterfactuals rather than metered output.
- LaFarge argues vertically integrated utilities are the best-placed actors
  because they see transmission, distribution and generation at once, and
  because grid operation is where the physics actually binds.
- His sequencing argument for why the modeling gap is not disqualifying:
  committing to a gigawatt of distributed capacity in the resource plan is what
  forces the where and the how to get answered.

## Claims worth citing

All figures as stated on 2025-01-09. Capacity accreditation values are set by
grid operators and change; the deployment claims describe an approach that was
barely in the market at the time.

- Electric vehicles were the biggest driver of electrification growth 24 months
  earlier and are now a distant third. (LaFarge)
- Cutting forecast data center and manufacturing growth by 80% to 90% still
  doubles the grid, which he frames as a baseline case rather than a high case.
  No base year, geography or horizon is attached to the doubling, so the claim
  is directionally strong and quantitatively loose. (LaFarge)
- In PJM, a gas plant is accredited at close to 80% of nameplate and solar
  without storage at 8%. Kann objects that this is not the right comparison and
  LaFarge agrees. (LaFarge)
- Solar paired with storage accredits in the high fifties to low sixties
  percent. (LaFarge)
- Roughly 1.6 gigawatts of nameplate solar and storage per gigawatt of
  accredited capacity, offered explicitly as his own rough arithmetic. (LaFarge)
- Microsoft contracted for 800 megawatts of baseload capacity from the restarted
  Three Mile Island unit through Constellation, with the power going onto the
  grid rather than to an adjacent data center. (LaFarge)
- Host agreements run the life of the asset, put at 10 to 20 years, and often
  reserve 20% or 50% of the battery for the host during outages. (LaFarge)
- Sparkfund has helped utilities run first distributed procurements, and LaFarge
  claims a decade of related utility work. No deployment volumes are given.
  (LaFarge)

## Where it's contested

- **The system-scale limit is the live disagreement.** Kann argues the
  building-by-building substitution for a nuclear plant works at project level
  and breaks at system level, because round-the-clock output is not replaced by
  solar and storage without additional storage, generation or gas backup.
  LaFarge accepts the framing and says he does not know the answer.
- **Whether accreditation is physics or paperwork.** LaFarge explicitly
  disclaims expertise here, wonders aloud whether the arithmetic holds at scale
  once inertia, load management and conductor temperature are considered, and
  suggests capacity ratings may be more a contract and market function than a
  physical reality. He asks listeners to weigh in, which is the clearest signal
  in the episode that this is unsettled.
- **The numbers are rules of thumb and he labels them as such.** The 1.6 to 1
  ratio comes with an invitation for better-informed listeners to correct it,
  and the accreditation comparison he reaches for first is one he withdraws
  under pushback.
- **The load forecast is asserted, and its counter-history is raised by the
  guest himself.** He offers the internet and personal computing forecasts that
  efficiency swallowed, calls the fool-me-twice question well anchored, and then
  answers it with a haircut argument rather than with evidence.
- **Scalability is untested.** Asked what limits it, he says nobody knows
  because it has not been done at this scale.
- **The disclosure is relevant in a narrow way.** Sparkfund sells this approach
  and Energy Impact Partners, where Kann is a partner, is an investor. Kann
  discloses it. The value-stack economics described here are the company's case
  for its own product rather than published results from completed programs, and
  LaFarge says as much when he notes that utilities and regulators are still
  getting their hands around the math.
