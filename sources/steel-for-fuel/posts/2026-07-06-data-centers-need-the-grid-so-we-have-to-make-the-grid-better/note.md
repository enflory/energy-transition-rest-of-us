---
post: "Data centers need the grid — so we have to make the grid better"
published: "2026-07-06"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [ai-compute, data-center-power, interconnection, demand-flexibility, ders]
source_document: "essay.md"
note_version: 1
disclosure: "The body is a cross-post by Tim Hade, whose company Brightfield Infrastructure was an Energy Impact Partners investment and was acquired by Voltus, a distributed-capacity aggregator the essay later cites. Lubershane states the investment in his introduction and also names ERock as an EIP portfolio company."
---

## The question

If the grid cannot connect AI data centers fast enough, is building a power
plant next to each one the way out?

## The answer

No. Co-location is not a shortcut around the grid but a second hard project
bolted onto the first, and it cannot scale to a national load shock. The
faster route is to buy controllability instead of steel: enforceable
curtailment terms, technologies that push more through existing wires, and
above all distributed batteries in commercial buildings.

## The argument

Almost none of this post is Lubershane's. He writes an introduction of about
ten paragraphs and then cross-posts an essay by Tim Hade in full, and unlike
other guest sections in this publication there is no handover back at the end,
so everything from the first subheading onward is Hade's, including his own
numbered source list. Hade's starting point is that the constraint on AI in
2026 is neither chips nor talent but the grid, and that what the grid keeps
running out of is not generation but slack: spare transformer capacity, spare
substation bays, spare thermal margin when a single element is out of service,
spare time in equipment supply chains. That converts the question from how to
build more power plants into how to build more power system capacity fast, and
the two have different answers. It is a calendar problem rather than an
ideological one, he argues: data centers are built on roughly an 18-month
clock and bulk power equipment on a 50- to 80-month one.

The seductive answer is to stop waiting and bring your own power. Hade's
objection is not that co-location fails but that it is misdescribed. A grid
connection is not a wire; it is access to a system supplying voltage
stiffness, frequency stability, high fault current and inertia, so stepping
behind the meter changes the physics and not merely the ownership. Data
centers make that harder than most loads would, being dense in power
electronics, drawing non-linear current, ramping fast and designed to be
intolerant of disturbance, so an islanded system has to absorb harmonics, step
loads, a lower and softer fault current that can blind protective devices, and
the risk of one transient tripping everything at once. All solvable, none
trivial. Announced megawatts are also not delivered megawatts, especially
where the project is really three projects: a data center, a power plant, and
the microgrid controls tying them together. Nor is it an unregulated lane, and
he reads a federal rejection of an expanded co-located arrangement at a nuclear
plant as a warning that the rules are being written in real time. His
conclusion is deliberately bounded: co-location will work in some places, for
firms that can execute power-plant-grade projects, and cannot be the only plan.

The load is not a fixed object either, and that is where the argument turns.
Training clusters are large, concentrated and indifferent to latency, so they
can be sited where land and transmission already are. Inference cannot be,
because it has to sit near users, which pulls compute toward metro areas,
distribution substations and congested feeders, exactly where equipment
bottlenecks and permitting friction are worst. Inference is also spikier than
training, and spiky load at a constrained node is not a job for slow thermal
plants but for fast, controllable resources. So the practical question becomes
how to energize a large load sooner without breaking reliability, and the
answer forming in the market is to split first power from ultimate firm
service: a load that accepts an enforceable operating envelope can be
connected while upgrades catch up. But an envelope only works if flexibility
exists on the other side of the contract, and a curtailment obligation is not
by itself a strategy. Hence the toolkit of demand response, grid-enhancing
technologies and distributed batteries, of which he rates batteries highest
because they are modular, fast and placeable. Placeable is the load-bearing
word: for interconnection, location is destiny, and a megawatt of flexibility
at the constrained substation is worth more than ten far away. The scale then
comes from large commercial buildings, the overlooked middle between millions
of homes and a handful of megaprojects.

His last move is that the binding constraint is not technical at all. We know
how to curtail load, deploy batteries and instrument lines; what is missing is
whether institutions can value, verify and accept flexibility as a substitute
for steel, with capacity accreditation for aggregated portfolios the hardest
part. Federal rules have opened a market pathway for aggregations of
distributed resources, but implementation is uneven and the difficult pieces,
coordination with distribution utilities, telemetry standards and accreditation
itself, are unfinished. The political argument is where he ends: the coalition
for using the existing grid better is broader than the coalition for new
corridors, and a hyperscaler funding batteries across local commercial
buildings converts a permitting fight into a visible local benefit. The
closing frame is a choice between fortified private islands, each solving its
own problem, and a better shared grid built partly with the capital already
pouring into AI.

## What you need to know first

- **Distributed energy resources.** The definition Lubershane quotes in the
introduction, without naming whose it is: loads, generators or storage on the
distribution system or behind customer meters that can be influenced or managed
to help balance supply and demand for electricity on the grid.
- **Behind the meter, or co-location.** Generation built on the customer's side
of the utility connection, serving the data center directly rather than
through the grid.
- **Operating envelope.** A service in which a large load accepts caps, ramp
limits, telemetry and defined curtailment rights in return for being energized
sooner.
- **Grid-enhancing technologies.** Equipment and software that raise the usable
capacity of existing lines, such as dynamic line ratings, which set a line's
limit from actual weather rather than a fixed assumption.

## Details worth keeping

- The introduction is where the relationships sit: Lubershane's own earlier
essay on distributed energy, his firm's investment in Hade's company
Brightfield Infrastructure, and Brightfield's acquisition by Voltus. He also
names ERock, formerly Enchanted Rock, as a longtime portfolio company now
listed, and a Tesla, Sunrun and Renew Home collaboration on residential
aggregation.
- Lubershane's own view, offered in passing: off-grid data centers are
compelling to him, especially if going off grid means tapping more low-cost
solar, while space-based ones make no practical or economic sense and look
like a marketing ploy.
- Hade's worked example of the strategy: a 300 MW data center that can cap its
net draw by 75 MW under defined conditions needs no 75 MW plant next door, and
roughly 150 commercial sites each with a 500 kW four-hour battery would supply
the same lever.
- His community argument: a data center offering a town few permanent jobs is
not always a compelling pitch, while paying to harden local businesses and
public buildings with batteries and backup capability is tangible, and
converts opposition into a deal.
- Two of the essay's 31 numbered sources are unpublished memos dated February
2026, one provided to the author and one described as prepared for the federal
regulator. Several of the interconnection and flexibility claims rest on them.
- The post carries a single figure, captioned with a battery manufacturer's
November 2024 press-release headline about a commercial and industrial storage
product. The note cannot see the image, and nothing in the argument depends on
it.

## Claims worth citing

All figures as stated on 2026-07-06. Nearly all are Hade's, citing outside
reports; the load forecasts and equipment lead times move fastest.

- American data centers used about 176 terawatt-hours in 2023, roughly 4.4% of
national electricity, projected at 325 to 580 terawatt-hours by 2028, or about
6.7% to 12%. (Lawrence Berkeley National Laboratory, cited by Hade)
- As average power that is roughly 20 gigawatts now and 37 to 66 gigawatts
then, an increment of 17 to 46 gigawatts in about five years before arguing
about peak. (Hade's arithmetic on the LBNL range)
- Utilities' five-year peak load growth forecasts rose from roughly 24
gigawatts to about 166 gigawatts over three years. (Grid Strategies
compilation, cited by Hade)
- Large power transformer lead times run roughly 80 to 210 weeks, and
distribution transformer lead times up to two years at sharply higher prices.
(National Infrastructure Advisory Council via CISA, and NREL, cited by Hade)
- A single AI campus can request 300 to 500 megawatts at one node. (Hade)
- Announced behind-the-meter or co-located generation tied to data centers is
on the order of 50-plus gigawatts, most identifiable equipment being natural
gas. (Cleanview, cited by Hade)
- AI was roughly a quarter of data center workloads in 2025 and could be about
half by 2030, with inference expected to overtake training as the dominant
requirement around 2027. (JLL, cited by Hade)
- Dynamic line rating can raise line ratings by 10% to 40% in favourable
conditions, and many grid-enhancing technologies can be installed within
months without new rights-of-way. (ESIG, cited by Hade)
- In a modelled mid-sized utility, 400 megawatts of virtual power plant
resource adequacy cost about $2m a year against about $43m for a portfolio of
new gas plants and grid upgrades. (Brattle via RMI, cited by Hade)
- Buildings over 100,000 square feet were about 2% of roughly 5.9 million
American commercial buildings in 2018 but about 34% of commercial floorspace
and about 39% of commercial building energy use, which he works out to on the
order of 118,000 large buildings. (EIA's 2018 commercial buildings survey,
cited by Hade, the arithmetic his)
- Engines from retired military aircraft could add up to 40,000 megawatts of
theoretical generating capacity, which the agency itself warns is theoretical
rather than a statement about feasibility. (EIA, cited by Hade)

## Where it's contested

Nobody argues back, and the one place two voices meet is the introduction,
where Lubershane recommends the essay rather than testing it.

- **Hade, who wrote the argument, has a commercial stake in it.** The
introduction states that Energy Impact Partners invested in Hade's company
Brightfield, which was acquired by Voltus, an aggregator of distributed
capacity, and Hade's essay later offers a Voltus partnership as evidence the
commercial model is arriving. The essay argues for the category his business
sells into, and does not restate the connection in its own text.
- **Hade's own limits are explicit.** Co-location will work in some places for
some firms; grid-enhancing technologies buy time rather than substituting for
new transmission; batteries are not magic; and no single bill or partnership
solves the problem.
- **The demand forecast is a wide range**, and its authors make it conditional
on hardware shipments, utilization and efficiency. The essay treats the growth
itself as given.
- **Two load-bearing sources cannot be checked.** Several of the claims about
what actually accelerates interconnection cite unpublished February 2026
memos.
- **The assumptions it does not defend** are that data center operators will
accept enforceable curtailment, and that accreditation of aggregated
portfolios can be made to work. He names accreditation as the hardest part and
then proceeds as though it is settled.
- **The concession is never sized.** Granting that co-location will succeed for
firms able to execute power-plant-grade projects, he never estimates how much
of the announced pipeline that covers, which is what would decide whether it
is a partial answer or a general one.
