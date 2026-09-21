---
episode: "AI scaling pathways: On grid, on edge, off grid, off planet"
published: "2026-03-12"
guest: "Jake Elder, senior vice president of research and innovation, Energy Impact Partners"
threads: [ai-compute, data-center-power, transmission, interconnection, supply-chain-costs, space-systems]
source_transcript: "transcript.md"
note_version: 1
---

## The question

If demand for compute keeps climbing, which ways of siting and powering data
centers can actually scale: large grid-connected sites, small sites at the edge,
off-grid sites, or data centers in orbit?

## The answer

Mostly the boring one. Elder's ten-year guess is that grid-connected hyperscale
still holds 50% to 60% of all operating compute, with another 10% to 15% built
off grid in a hyperscale-like format, roughly 15% at the edge and 5% to 10% in
space. Kann would shift share toward off grid and away from edge, which neither
has been able to build a case for despite trying. The exercise is conditional on
two assumptions they state and then set aside: that compute demand keeps scaling,
and that no large efficiency breakthrough changes the paradigm.

## The argument

The incumbent path has three constraints, unequal in difficulty. Elder names
physical grid capacity and deliverability, power quality, and social license to
operate, pointing to blanket bans in some states and projects pulled years after
announcement. Kann rates power quality the most manageable, since it is an
engineering problem, and social license the most underappreciated. On capacity
Kann separates two
problems people conflate: generation equipment, transformers, switchgear and
substation upgrades sit in a rough three-to-seven-year window, bad but finite,
while new interregional transmission is, in his phrasing, essentially infinite
years, because it largely is not happening. That matters because transmission is
the constraint unique to this pathway. Going off grid still leaves you waiting
for turbines and transformers; it only escapes the poles and wires. One
clarification to carry: the behind-the-meter generation now being built at data
centers is almost entirely hybrid, sites that are grid-connected or intend to be,
and close to none of it is true off-grid operation.

Edge is where the episode sets up an intuition and knocks it down twice. The
first-principles case is latency, and both conclude it is a red herring: the
standard example cuts the other way, since a Waymo makes its driving decisions in
the car and its calls to the cloud are not so latency-bound that a regional
hyperscale site fails. The second case is cost, usually argued from cheap land at
a substation or commercial property, but land is a very small share of a fully
loaded data center, where the money is in GPUs, the building and labor, and a
small site is subscale against a 300-megawatt one. Strip both away and what
remains is speed: a site provisioned for five megawatts and drawing two can
absorb three more without waiting for a system upgrade. But matching a single
300-megawatt development means a hundred successful site evaluations rather than
one, and neither speaker has seen that demonstrated. Elder calls it frustrating
because edge looks like it should be the right answer.

Off grid relaxes almost everything at once, which is why Kann finds it the most
underrated option: land is not scarce, siting can avoid communities that do not
want data centers, and a study Elder cites found over a terawatt of opportunity
in the American Southwest alone. What stops it is that the grid absorbs shocks.
Islanded, you build that absorber yourself, meaning inertia, fault response and
black-start capability, and very few people know how to run a gigawatt-scale
grid. Early anecdotal data, mostly from bridge-power projects, is that they are
not holding even 90% uptime. Elder's refinement is the useful part: 90% may be
tolerable if you know when the missing 10% falls, and intolerable if it lands at
random inside long training runs. He also notes that grid operators cannot yet
manage the voltage swings and harmonic distortion from data centers while those
are a small share of load, which is a bad sign for managing them when they are
the only load. Kann's counterweight is that five nines is partly a legacy of
cloud service contracts, while engineering to it off grid means overbuilding
generation and storage, at a cost that matters for a ten-billion-dollar asset.

Orbital gets taken seriously and still loses on cost. Both say plainly they do
not believe Musk's claim that space will be the cheapest compute within three or
four years, and neither calls the idea insane. Heat rejection, the objection
people reach for first, is real but not the killer, because heat radiates with
the fourth power of temperature and chips keep getting denser and hotter. The
harder problems are debris, since a gigawatt-scale orbiting asset is roughly four
square kilometers of radiator and solar, and maintenance, since a failed GPU that
an engineer swaps in near-real time on the ground stays broken in orbit. The
economic case rests on free power, but energy is only 5% to 15% of an AI data
center's cost, chips cost the same either way and maintenance costs more. So the
case for orbital is not that it is cheap; it is that Earth may not allow building
fast enough. That sets up the comparison Kann says he rarely hears made. Off
grid's rate limiter is the supply chain for generation and electrical equipment,
orbital's is Starship launch cadence, and standing up a couple hundred gigawatts
a year of turbine manufacturing seems to him more plausible than five Starship
launches a day. Elder's pushback is the episode's strongest objection and it is
not technical: would society tolerate 200-plus gigawatts a year of new gas
infrastructure for twenty years, which is Musk's own carbon argument? Kann
answers that you could be maximalist on solar and storage, geothermal and nuclear
instead. Elder half-concedes, then adds the constraint above both pathways,
semiconductor fabrication, which he is confident cannot supply that build rate
and so probably binds first. That points him to off grid moving faster, and
leaves Kann surprised not that anyone would go to space but that they would skip
the terrestrial waypoint on the way.

## What you need to know first

- **Behind the meter versus off grid.** Behind-the-meter generation sits on the
customer's side of the utility connection, so a data center can have a lot of it
and still be grid-connected. Truly off grid means no connection at all, a
different engineering problem and, per this episode, still rare.
- **The grid as shock absorber.** A connected site borrows the whole system's
inertia, fault response and restart capability. An islanded site provides all of
it itself, which is the core difficulty of going off grid.
- **Five nines.** 99.999% uptime, the standard the cloud industry promised its
customers, or roughly five minutes of downtime a year. Whether AI workloads need
it is an open question here.

## Details worth keeping

- Elder splits edge into three things: inference moving onto devices such as
phones and vehicles; 15-to-30-megawatt sites that look like small hyperscale
builds placed where power arrives sooner; and deployments of 100 kilowatts to a
few megawatts at substations or in office basements. Kann defines edge for the
forecast as anything under roughly 50 megawatts.
- Going off grid may partly dodge the turbine queue, because redundancy pushes
you toward many small units, such as one-megawatt reciprocating engines and
smaller aeroderivative turbines, rather than one 500-megawatt combined-cycle
plant. Redundancy can also mean two separate fuel supplies, including two gas
pipelines, which constrains siting and adds cost.
- Siting is broadening fast. Kann says tier-one markets such as Northern
Virginia, Chicago, Phoenix and Atlanta were once expected to take 90% of new
demand, and speed to power is now pulling development toward West Texas, though
workforce, electricians and water still matter.
- Latency is worse in orbit than in West Texas, so even a future that trains
models in space still builds heavily on the ground.

## Claims worth citing

All figures as stated on 2026-03-12. Lead times, uptime data and anything
touching launch costs move fast, and several of these are explicitly rough
estimates rather than measurements.

- Interconnecting gigawatt-scale sites to new power supply runs five to seven
years in many markets. (Elder)
- Turbines, transformers, switchgear and substation upgrades sit in a three-to-
five or up-to-seven-year window; new interregional transmission is "essentially
infinite years" in recent US practice. (Kann)
- An unnamed report put roughly 50 gigawatts of behind-the-meter generation in
development at data centers, of which close to zero is true off-grid capacity.
(report cited by Kann)
- A study co-authored by Stripe, Paces and Scale Microgrids about two years
earlier found over a terawatt of off-grid opportunity in the American Southwest
alone, with roughly 50% solar plus batteries at cost parity to all-gas and up to
80% or 90% solar without meaningful cost increase. Elder hedges the second figure
with "I think," and the transcript garbles "parity" as "priority." (study cited
by Elder)
- Early off-grid projects, mostly bridge-power sites intending to connect later,
are not holding even 90% uptime. Elder calls the data anecdotal. (Elder)
- The International Space Station rejects under 100 kilowatts of heat with a
radiator the size of a soccer field, while one high-density Nvidia rack could
soon exceed 100 kilowatts; a gigawatt-scale orbital data center works out to
roughly four square kilometers. (Elder)
- A Starlink satellite's odds of a debris strike run a couple percent per year,
implying a strike roughly every hour for a four-square-kilometer object. The
analyst is rendered in the transcript as "Thunder Set Energy." (analysis cited by
Elder)
- Orbital solar gets about a 95% capacity factor plus better irradiance, five to
ten times the energy per panel over its life, but energy is only 5% to 15% of an
AI data center's total cost. (Elder)
- Musk's claims, characterized by both speakers and disbelieved by both: orbital
compute cheapest within three or four years, hundreds of gigawatts of compute
built per year on the same timeline, and Starship launch at about $100 per
kilogram. (Musk, as characterized by Kann and Elder)
- Ten-year share of all operating compute: 50-60% grid-connected hyperscale,
10-15% off grid, about 15% edge, 5-10% orbital. (Elder)

## Where it's contested

- **The premise is assumed, not argued.** Kann sets the demand question aside,
saying he has nothing insightful to say about how much compute will be needed,
and assumes no major efficiency gain. The shares are also sensitive to the size
of the pie: a 10-terawatt answer and a 300-gigawatt answer imply different mixes.
- **Edge is an open disagreement between them.** Elder allocates it about 15%
while calling it the least-cost and theoretically fastest option; Kann would take
share from edge and a little from grid-connected hyperscale, and cannot see why
edge becomes a large portion of compute. Both spent
three or four months trying to convince themselves of the edge case and failed,
and Kann invites listeners to try.
- **Off-grid reliability is unresolved.** Elder expects the engineering gets
solved over time but calls it a large risk for a first mover on a
ten-billion-dollar asset, and the uptime evidence behind it is anecdotal.
- **Orbital timing is left deliberately vague.** Elder agrees it is not the
cheapest option before 2030, then says whether it arrives in five years or 500 he
is not sure. Both frame orbital as not insane and its technical problems as not
obviously insurmountable, which is weaker than either endorsement or dismissal.
- **Whether society accepts the gas buildout off grid implies.** Elder raises it
as the strongest argument for going to space and Kann counters with clean firm
alternatives; neither resolves it. Elder also suspects developers remain
sensitive to location, while Kann thinks that constraint is loosening in real
time.
- **Chips as the real ceiling.** Elder does not know how many chips a couple
hundred gigawatts a year translates into, only that fabrication capacity today
cannot do it, so the binding constraint may sit upstream of this whole framework.
