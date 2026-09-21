---
episode: "Live from Transition-AI 2026: Inside Google’s massive AI capex"
published: "2026-04-23"
guest: "Amin Vahdat, chief technologist for AI infrastructure, Google"
threads: [ai-compute, data-center-power, demand-flexibility, backup-power, interconnection]
source_transcript: "transcript.md"
note_version: 1
---

## The question

As AI shifts from training models to serving them, does that change the size,
the reliability and the power profile of what Google builds with the $175 to
$185 billion of capital expenditure it has planned for this year?

## The answer

Size changes least. Vahdat expects a medium number of medium-sized sites plus a
small number of large ones, not a swarm of tiny edge deployments. Reliability
changes most, and that is the message he says he would send if he could send
only one: the very high availability that data centers are built to is not
intrinsic, and customers will often trade availability for capacity. On
what is actually holding the buildout back, he refuses to pick, and says power,
chips and construction all bind at different hours of the same day.

## The argument

Training is what drove data centers to gigawatt scale, and inference does not
need that. Vahdat says you could serve on much less than a gigawatt, probably
less than 100 megawatts, though not arbitrarily small, because an accelerator
needs co-located compute, storage and networking around it. There is also a
lifecycle effect: whoever is training wants the newest chips every year, so
after a year or two a gigawatt of training capacity is handed down to serving.
But he does not follow this to the conclusion people expect. Google has found it
easier to build a smaller number of larger sites, with asterisks for fault
tolerance and
geographic spread, and a thousand sites each holding a tenth of a percent of
capacity carries management overhead of its own. His answer, offered with an
explicit apology for imprecision, is a medium number of medium-sized sites
augmented by a few large ones. The case for spreading out strengthens later
rather than now: today a generated token is slow enough that a user in San
Francisco cannot tell whether they are served from the East Coast or Europe,
which is not true of search or maps, so the speed of light only starts to bite
as models get faster and more interactive.

Reliability is where he wants the argument to land, and he says plainly that the
high standard is not intrinsic. The historical logic was that compute made up a
small fraction of the cost of a software service, so overprovisioning it was
cheap; many Google data centers target four nines of availability, with all the
uninterruptible power supplies and backup generators that implies. Constraint
has inverted that arithmetic, because compute is now a much larger share of
service cost. Put the trade to an internal customer as four nines and half the
capacity against two nines and twice the capacity, and very often, though he is
careful to say not always, they take the capacity. Two nines means 3.65 days of
downtime a year, which he does not minimize; the bet is that the other 51 and a
half weeks at double capacity are worth it. Asked whether this is actually
happening, he says only that it is.

That is what makes grid flexibility possible rather than merely virtuous. In
March, Google reached agreements with utilities for a gigawatt of demand
response across its fleet: during the utility's single highest-demand week it
will brown down, letting the utility plan for something below its worst week and
lowering cost for Google and for other ratepayers. Note which way this cuts on
behind-the-meter power. Vahdat says Google would prefer grid-connected capacity,
because going behind the meter means provisioning all that reliability yourself.
On-site generation is a different kind of latency play, the time it takes to get
capacity delivered, so bridge power covers the gap while Google invests with
utilities to bring transmission a year or two later, and could in principle be
mobile. Making any of it work depends on microgrid software the industry is
underinvested in, because a browndown is not the site going dark. It is a
decision about which 20, 30 or 40 percent to shed, which workloads drain and
which service commitments move elsewhere. Kann presses on whether Google can do
this only because it is unusually vertically integrated, designing its own chips
alongside the rack, the building, the power source and the models. Vahdat does
not dispute it. He describes that integration as precisely the point, a chain of
custom interfaces each worth a few percent that multiply into something
meaningful, and does not say how the capability travels to anyone lacking the
stack.

Asked to rank the rate limiter between power, chips and labor, he declines, adds
data center construction and delivery as a fourth category broader than labor,
and says that at 10am it is labor, at noon power and at 2pm chips, every single
day. Pushed with a hypothetical $300 billion budget, he still refuses, saying
all of them are at the limit of what Google can do and none is inherently easier
to scale. The cost question rhymes with the reliability one. A building is
designed for a 25-year life across five or six chip generations, and the watts
per linear foot of a disk rack and a GPU rack differ enormously, so committing a
building to a single purpose buys efficiency at the cost of fungibility. That
trade was not worth making when compute was a small share of cost. It is now.

## What you need to know first

- **Training versus inference.** Training builds the model, inference (which
  Vahdat calls serving) runs it for users. Training rewards putting enormous
  capacity in one place; serving mostly does not.
- **Nines.** Shorthand for availability. Four nines is 99.99 percent uptime; two
  nines is 99 percent, which Vahdat notes is 3.65 days of downtime a year.
  Higher nines mean more backup equipment and more capital.
- **Behind the meter.** Generation or storage on the customer's side of the
  utility connection, so it never touches the grid. "Bridge power" is
  behind-the-meter generation used to run a site during the years before a grid
  connection arrives.

## Details worth keeping

- Google's first data center, at The Dalles in Oregon, was 10 megawatts, which
  Vahdat says stunned people at a time when almost nobody built data centers for
  their own compute.
- The power density gap is widening, not closing, because disks do not draw more
  power each generation and accelerators do.
- Training's spiky on-off power profile is smoothed by some operators running
  filler workloads; Vahdat says Google does not do this and others do.
- On physical AI, he treats self-driving cars as the best current example and
  argues safety pushes compute onto the device, since a robot that cannot get an
  answer for five seconds is a different problem from a chat app pausing. Kann
  draws the consequence that this weakens the case for edge data centers.
- Asked whether the buildout will strand generation, Vahdat says he would love
  that problem, and that energy is a limiter well beyond AI.

## Claims worth citing

All as stated on 2026-04-23 at a live conference session. Capex and deployment
figures move fast.

- Google announced intent to spend $175 to $185 billion in capital expenditure
  this year, in its Q4 2025 earnings report. Kann notes not all of it is AI
  infrastructure. (Google, cited by Kann)
- US electricity transmission capex runs about $25 to $35 billion a year;
  Vogtle cost about $30 billion; NASA's annual budget is about $25 billion.
  (Kann)
- A gigawatt of demand response agreements with utilities across Google's fleet,
  reached in March. (Vahdat)
- Many Google data centers aim for four nines of availability; two nines is 3.65
  days of downtime a year. (Vahdat)
- Offered four nines at half capacity or two nines at twice capacity, internal
  customers very often, but not always, choose the capacity. Vahdat confirms the
  trade is happening at Google but gives no figure for how much of the fleet it
  covers. (Vahdat)
- Inference does not strictly require a gigawatt and probably not even 100
  megawatts of capacity, subject to a minimum he does not quantify. Individual
  racks are trending toward hundreds of kilowatts. (Vahdat)
- Power density gap between storage and accelerators approaching 100x, up from
  at most 10x for storage against general compute; power draw for one workload
  versus another, serving against training, can differ by a factor of two.
  (Vahdat)
- Year-over-year efficiency gain illustrated as 1.2x, a number he explicitly
  says he is making up. (Vahdat)

## Where it's contested

- **He will not name a rate limiter.** Asked twice, including with a doubled
  budget, he says power, chips and construction are all at the limit and none is
  easier to scale. Any summary that has Google naming power as the constraint
  gets this backwards.
- **The reliability trade is asserted, not evidenced.** He confirms it is
  happening "without saying too much," and gives no share of the fleet, no
  workload breakdown and no results. The argument for why it should happen is
  much stronger than the disclosure of how much has.
- **Whether this generalizes beyond Google is left open.** Kann puts the
  vertical integration question directly. Vahdat agrees that co-designing chip,
  rack, building, power source and model is where the capability comes from, and
  does not claim it transfers to operators without that stack.
- **Scale is hedged in both directions.** Inference relaxes the need for
  gigawatt sites, but he still says fewer larger sites are easier to build and
  that concentration has fault tolerance limits.
- **Behind the meter is a schedule decision, not a preference.** He states
  plainly that Google would rather be grid-connected, which cuts against reading
  the on-site generation trend as hyperscalers leaving the grid.
- **He declines specifics repeatedly**, on customer co-design, on self-driving
  and on individual deployments, and says he would need to think the
  robotics-versus-edge question through more. Normal for a live on-stage
  session, but worth noting before treating any of it as disclosure.
