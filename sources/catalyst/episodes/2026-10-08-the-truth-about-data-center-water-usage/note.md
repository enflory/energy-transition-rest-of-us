---
episode: "The truth about data center water usage"
published: "2026-10-08"
guest: "Tim Shedd, founder, Ebullient Insights"
threads: [water, data-center-power, ai-compute, public-opinion]
source_transcript: "transcript.md"
note_version: 1
---

## The question

How much water do data centers really use, and what decides it?

## The answer

According to Shedd, most data centers use little water and new ones use less,
because the water a site consumes is set by how it rejects heat to the outside,
and modern liquid cooling hands that heat off hot enough to reject with little
or no evaporation in most climates. He declines to give a precise figure,
since every site differs, and he does not dismiss communities' concerns: some
water is still used to fill and flush the plumbing and to build the campus,
and he thinks the backlash is ultimately more human than technical.

## The argument

The episode starts from an apparent paradox that Kann names. The industry is
rapidly moving to cooling chips with liquid, which sounds like more water,
while claiming that its data centers consume less. Shedd resolves it by
separating two things. Inside the building, chips are packed ever closer
together because the GPUs need to talk to each other over short, fast
connections, and each generation runs hotter because, in some cases,
chipmakers push the silicon until cooling is the limit. Air cooling worked
when racks averaged
around 9 kilowatts and, with heat exchangers moved right next to the racks,
up to about 80. Today's racks are a multiple of that, so the industry has moved
to pumping coolant (water with propylene glycol) through copper cold plates
on the chips. That coolant circulates in a closed loop. It is not where water
gets consumed.

Consumption happens at the other end of the heat's journey. Shedd describes
three stages: a technology cooling system collects heat from the servers, a
heat exchanger passes it to the facility water system, and that system carries
it to outdoor equipment chosen for the local climate, such as chillers,
cooling towers or dry coolers. The facility side does not care what cooling
architecture sits on the other side of the exchanger. What it cares about is
temperature. If the water arriving from the servers is hotter than the outside
air, heat flows downhill and only pumps are needed. If the outside is hotter,
the heat has to be pushed uphill, which takes either a chiller, costing energy,
or evaporating water, costing water. So in Shedd's framing the cooling
architecture and water consumption are "kind of disconnected," linked only
through the temperature at which heat is handed off.

That is why the history and the future diverge. In the air-cooled era,
hyperscalers' biggest cost was energy, and evaporation was the most
energy-efficient way to cool. Those systems used relatively little water per
unit of cooling, but at megawatt scale some sites consumed, relatively
speaking, a lot, and Shedd
credits the large operators with being transparent about it. Air cooling
also needs cold water to make cold air, which means chillers, and chillers
often run most efficiently, depending on the climate, with cooling towers that
evaporate water. Direct liquid
cooling breaks that chain: coolant can go to the chip at 45°C and come back at
55°C, hot enough to reject outdoors in most places without evaporating water
or spending much energy. Asked by Kann whether falling consumption owes more to
operators re-optimizing for water or to this technical shift, Shedd gives "a
large percentage" to the technology. Most data centers, he says, are built
closed loop with no evaporation at all. Some evaporate on the hottest
afternoons for a few to tens of hours a year, and even those more dependent
on cooling towers use them mostly to trim the heat on those afternoons.

The strongest qualification is Shedd's own. He will not say communities who
have watched their water table fall are wrong. Large campuses use water to fill
enormous pipe networks, to flush them at startup (probably dumped in large
amounts at first, now mostly filtered and reused), and during construction for
dust control, roads and concrete. That water likely comes from local supplies
even when it is not a continuing use, and a falling water table may have
many causes besides the
data center. On the whole, he concludes, data center water use is low compared
with many other uses, and he believes continued innovation is lowering it per
unit of power.

## What you need to know first

- **Rack density.** How much power one cabinet of servers draws, in
  kilowatts, and so how much heat its cooling has to carry away.
- **Direct-to-chip liquid cooling.** Coolant piped to a metal plate sitting on
  each hot chip. "Single-phase" means the coolant stays liquid; "two-phase"
  means a refrigerant boils off the plate. Immersion instead submerges the
  hardware in a fluid.
- **Heat rejection.** The outdoor equipment that dumps the building's heat to
  the environment. Dry coolers use air only; cooling towers and adiabatic
  coolers evaporate water to cool further; chillers use refrigeration and
  energy to push heat out when the outside is too warm.

## Details worth keeping

- Shedd stresses how new this is: the push to cool everything with liquid is
  only about three years old, and he says the industry does not know the
  answers to everything.
- An adiabatic cooler, as Shedd describes it, is roughly a dry cooler with
  pads sprayed with water on hot afternoons; he calls it an elegant way to
  handle a small number of hot hours with a little water.
- Two-phase direct-to-chip cooling is not yet available at scale. Its
  performance is similar to single-phase rather than superior, and its appeal
  is smaller hoses that free up space inside the server. Shedd discloses that
  he once ran a company working on it.
- Single-phase immersion is limited because oil is a poor heat-transfer fluid,
  so proponents now propose cold plates on the hottest chips with immersion
  fluid for the rest. Two-phase immersion faces pressure-management problems
  in large tanks and, per a paper Shedd co-authored a few years ago, is stuck
  for thermodynamic reasons at lower power, though still around 1,000-watt
  processors.
- The industry has settled on single-phase direct-to-chip because it can
  scale now, with a robust global supply chain for cold plates and coolant.
- Coolant longevity rests on a small proprietary corrosion-inhibitor package
  like the one in car antifreeze (where he puts it at about 1% to 2%, "maybe"),
  which lets mixed metals last for years;
  Shedd credits suppliers including Valvoline, Dow and Recochem.
- On public acceptance, which Kann frames as just outside Shedd's expertise,
  he cites
  Microsoft's messaging on a large Wisconsin data center as a good example
  that still met backlash over water. He calls that kind of transparency table
  stakes, suggests inviting communities in and moving away from
  nondisclosure agreements that breed distrust, and wonders whether the
  backlash is really general discomfort with a new technology, taken out on
  big anonymous buildings.

## Claims worth citing

All figures as stated on 2026-10-08. Rack power and cold plate volumes are
changing fast.

- A 300-megawatt data center with evaporative cooling uses roughly 150
  million gallons of water a year; a combined-cycle power plant of the same
  capacity uses roughly three times as much; 150 million gallons is about the
  water for 550 acres of irrigated soybeans. (Kann, monologue)
- Historical average rack density was about 9 kilowatts; high-performance
  computing went to 30 to 40 kilowatts with in-row coolers. (Shedd)
- Shedd shipped racks at Dell at up to 80 kilowatts with rear-door heat
  exchangers, which he says are in many cases almost as efficient as direct
  liquid cooling up to that level but struggle beyond it. (Shedd)
- NVL72 racks are rated at 220 kilowatts. A Dell installation he
  names as the Perlmutter cluster at Lawrence Berkeley National Lab runs
  higher, "I want to say" about 280 kilowatts, a figure he says he does not
  remember exactly. Designs have been mapped to 400 to 500 kilowatts per rack.
  (Shedd)
- Cold plates can now cool a 1,400 to 1,800 watt processor with 45°C water,
  which was not possible three years ago. (Shedd)
- Cold plate fins are about 100 microns thick with about 100 microns between
  them and roughly 3 millimeters tall, on copper 1 to 2 millimeters thick.
  (Shedd)
- The dominant coolant is water with 25% propylene glycol. (Shedd)
- The industry is consuming hundreds of thousands of cold plates a month and
  could approach a million a month next year, against perhaps 100,000 a year
  industry-wide in 2022. (Shedd)
- The 55°C return ("135 or something Fahrenheit," he says, unsure of the
  conversion) can be rejected in most places except the worst summer days in
  places like central India. (Shedd)
- Uphill heat rejection becomes necessary in many climates when outdoor
  temperatures rise above a threshold he gives as "100 degrees Fahrenheit,
  you know, 43 degrees Celsius," often warmer than the facility water system
  wants to run. The two values do not match each other, so quote with care.
  (Shedd)
- Evaporative systems use "a kilogram of water for every 2 megawatts or
  something like that." The figure is given without a time unit and cannot be
  used as stated. (Shedd)

## Where it's contested

- **"Mostly a design choice" is Kann's line.** The monologue's conclusion is
  broadly consistent with Shedd, but Shedd's version is more qualified: water
  use depends on climate, heat load and the trade-off with energy, and he
  says he does not know the consumption figure precisely because every data
  center is different.
- **The monologue's comparison figures are Kann's alone.** Shedd never
  addresses the 150-million-gallon, power plant or soybean numbers.
- **A host restatement Shedd did not correct.** Kann summarizes the technical
  reason as higher temperatures meaning "less heat to reject." Shedd's own
  explanation is that hotter water gives more options for rejecting heat, and
  so uses less water; it is about rejecting heat more easily, not about there
  being less of it. His answer does not take up the wording.
- **Shedd's view is not "nothingburger."** He says most data centers use
  little water and finds the debate frustrating, but explicitly declines to
  tell concerned communities they are wrong, and points to construction and
  fill water as real local draws.
- **The community diagnosis is opinion.** Shedd labels his view that the
  backlash reflects broader unease about AI as a belief outside his area of
  expertise.
- **What went unexamined.** No measured consumption data for modern sites is
  presented, and the share of new capacity actually built without evaporation
  rests on Shedd's characterization of "most" data centers.
