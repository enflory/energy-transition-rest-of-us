---
episode: "Building inference data centers on the high seas"
published: "2026-05-28"
guest: "Garth Sheldon-Coulson, co-founder and CEO, Panthalassa"
threads: [ai-compute, data-center-power, renewables, first-of-a-kind, marine-energy]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Could you power AI compute by putting the generator and the servers together on
untethered steel structures bobbing in the deep ocean, and would it pencil?

## The answer

Sheldon-Coulson's case is that it does, but not for the reason you would expect.
The power is cheap, and cheap power stopped being the point once the payload
became chips, because the chips dominate the cost. The design now optimizes for
uptime, manufacturability and cooling instead, and the object is best understood
as replacing the power plant and the data center building at once. None of this
is demonstrated commercially; at recording the first pilot series had not yet
gone in the water.

## The argument

A node is a steel structure ten to thirty meters across at the top, running
seventy to a hundred meters down, which Kann likens to the height of Big Ben. It
is generator, vehicle and data center at once. The hull shape forces water into a
pressurized reservoir as the structure rises and falls, and that water falls back
through a turbine on a mostly closed seawater circuit, which a colleague named
ocean hydro: the aim is hydro's cost structure without depending on a finite
supply of rivers. A second feature of the same hull pushes water backwards, so
the node always moves forward and only needs steering, like a Roomba you cannot
stop. And because the design rests on cutting the cable to shore, the energy has
to be consumed on board, which is why each node carries a computing cluster or an
electrolyzer instead of exporting electricity. Wave energy stayed coastal
historically because it assumed a cable, and usually a seafloor connection to
push against. Removing both is what lets these go thousands of miles out.

Going out is the point, because that is where the resource is. Waves are wind
energy accumulated over long fetches with very little loss, so they keep running
after the wind stops, which he calls the world's biggest solar battery. Coastal
water gets a small, degraded fraction of it while competing with fishing and
seafloor regulation. In the target regions he says a fifteen meter object
intercepts about 2.5 megawatts of wave flux on average, with wave heights
averaging four to four and a half meters across the year and rarely below three.
Simulating against ten or eleven years of historical weather data, he gets
capacity factors over 90% and, with two to four hours of battery, payload
availability between 99 and 99.8%. The contrast he draws with solar is about
shape rather than average: output has drawdowns lasting half a day, to perhaps
50% of the payload, and never reaches zero.

The most interesting move is economic. Panthalassa started out chasing a one-cent
levelized cost of electricity and abandoned the goal, because with compute as the
payload the node is only a fifth to a tenth of the total cost structure once you
count replacing servers several times over its life. Making the node cheaper
barely moves the answer, so the company now deliberately optimizes toward a more
expensive node in exchange for higher uptime, more battery and shapes that can be
stamped out of steel quickly. The power stays cheap anyway, at an optimum around
three and a half to four cents per kilowatt-hour, but the claim that carries the
argument is the other one: seawater provides free convective cooling, so the node
replaces the power plant and the data center together, and that combined cost
structure is what he says the comparison should be against.

Which leaves the objections, and Kann presses the right ones. Maintenance in open
ocean is answered by designing for none, a solid steel hull with coatings and one
water turbine on bearings as the only moving part. Kann points out that
generators and power electronics fail on land regardless of the sea, and the
response is a design philosophy rather than a result: an avionics-derived
approach from people out of Raytheon and Collins Aerospace, analog logic with no
firmware and no liquid capacitors. Sheldon-Coulson is explicit that
maintenance-free operation is still a design goal and it remains to be seen
whether they achieve it. On servers, the modeled answer is roughly one percent
lower availability than land systems at the right deploy-and-recover cadence, and
he argues failure rates may actually be lower at sea because the payload is
sealed with nitrogen replacing oxygen, colder, and free of vibration and dust.
The second answer is to change the workload, since much valuable work is
CPU-heavy reinforcement learning and tool use, and newer accelerators use less of
the most failure-prone memory. That also settles the market question: added
satellite latency is about a hundred milliseconds, which vanishes into the time a
human or an agent already waits, so the targets are long-running inference and
reinforcement learning rather than tightly interconnected training clusters or
anything genuinely latency-critical. The oddity Kann flags is the density
inversion: a node's economic optimum is around 400 kilowatts, roughly one rack in
a hyperscale data center, inside a structure tens of meters wide and seventy
deep. It works only because ocean area is effectively unconstrained.

## What you need to know first

- **Capacity factor versus availability.** Capacity factor is the share of
  nameplate output actually produced over time; availability here is the share of
  time the payload gets the power it needs. Over 90% and over 99% are different
  claims, and the battery is what bridges them.
- **Levelized cost of electricity.** Lifetime cost divided by lifetime output, in
  cents per kilowatt-hour. The metric the company says it stopped optimizing once
  chips dominated the cost.
- **Inference, training and reinforcement learning.** Inference is running a
  trained model to produce output. Conventional training needs many chips wired
  tightly together in one place, which is what this platform cannot do.
  Reinforcement learning is the part of training where a model tries many
  approaches and is scored, which parallelizes well and is the workload he wants.
- **Latency.** The delay between request and response. The satellite link adds
  about a hundred milliseconds, irrelevant for work measured in minutes and
  disqualifying for work measured in milliseconds.

## Details worth keeping

- Because propulsion comes from the hull shape rather than a motor, there is no
  auxiliary generator and no chicken-and-egg problem at launch, and he describes
  steering systems through figure eights at sea. Factories go near the good
  resource rather than near North America, so a node is towed roughly fifty
  miles, flipped vertical, and then walks itself out; the economic optimum is as
  short a tow as possible.
- The seawater circuit is mostly closed. The tube is open at the bottom and some
  mixing occurs, but it is not pumping through fresh seawater and so is not
  continuously drawing in nutrients for things to grow on.
- A failed node can be commanded home, a week or two depending on distance, for a
  fast payload swap. Routinely recovering nodes would break the cost structure,
  so the model depends on it being rare.
- Payloads are bespoke rather than standard racks: custom enclosures and servers
  qualified with several server makers and chip companies, offered as a menu.
  Mesh radio between nearby nodes is possible but not central to the pitch, since
  the target workloads gain little from node-to-node communication.
- Reinforcement learning is described as probably already a larger energy demand
  than what has historically been called training.
- Deployment history: Ocean One in 2021, Ocean Two and Wavehopper in 2024, all
  full scale for the North Pacific off Oregon and Washington. Ocean Three is the
  first commercial pilot series and the first designed for factory manufacture.

## Claims worth citing

All figures as stated on 2026-05-28. Every number about the product comes from
the founder and describes designed or modeled performance rather than commercial
operation, so attribute them to the company. Dates below are targets stated
before the fact.

- Nodes ten to thirty meters across the top, with diminishing returns past about
  twenty-five to thirty, running seventy to a hundred meters down. Kann's opening
  describes them as 85 meters, roughly the height of Big Ben. (Sheldon-Coulson;
  Kann for the comparison)
- Node capacity 200 kilowatts to one megawatt, with about 400 kilowatts the
  likely economic optimum. (Sheldon-Coulson)
- Wave flux through a fifteen meter object in target regions: about 2.5 megawatts
  on average, with wave heights averaging four to four and a half meters
  year-round and rarely below three. (Sheldon-Coulson)
- Over 90% capacity factor by standard metrics; 99 to 99.8% payload availability
  with two to four hours of battery. (Sheldon-Coulson)
- Power at two cents per kilowatt-hour in some designs, optimum around three and
  a half to four cents. (Sheldon-Coulson)
- Cost structure excluding battery: about half steel, roughly a quarter
  powertrain, a little under a quarter marine coatings. With a nominal battery,
  the battery is about a third of the total and roughly equals the steel.
  (Sheldon-Coulson)
- With compute as payload, the node is a fifth to a tenth of the cost structure,
  especially counting multiple payload replacements. (Sheldon-Coulson)
- Land footprint about one hundredth of the weighted average across other energy
  technologies per unit of power, counting factories. Challenged by Kann and
  immediately narrowed: the weighted average is dominated by solar and the claim
  does not hold against gas. (Sheldon-Coulson)
- Modeled compute availability roughly 1% below land systems at the right
  deploy-and-recover cadence, using empirical failure rates for the most
  failure-prone GPUs. Added satellite latency about 100 milliseconds.
  (Sheldon-Coulson)
- Roadmap: Ocean 3.1 in the water October 2026, 3.2 and 3.3 by spring or summer
  2027 as an autonomous fleet demonstrating propulsion, generation and the
  company's first inference compute at sea; larger southern-hemisphere systems
  from early 2028. (Sheldon-Coulson)

## Where it's contested

- **This is an unshipped product described by its founder.** No third-party
  testing, named customer or independent measurement appears, and the first
  inference compute at sea is scheduled for after the recording, so every
  operating figure is modeled or drawn from prototypes.
- **The guest concedes the central uncertainty himself.** On maintenance-free
  operation he says it remains to be seen whether the design goal is achieved,
  and supports it with the narrower evidence that hulls and turbines have
  survived endurance testing. The chip reliability advantage is similarly a
  belief with an analogy behind it: strong reason to believe failure rates will
  be lower, citing Iceland and past underwater deployments rather than his own
  fleet.
- **Kann pushes back twice and gets partial concessions.** On footprint he
  objects that it cannot hold for gas and the claim is narrowed. On power
  electronics he notes inverters and generators fail on land anyway, and the
  answer is design philosophy plus an acknowledgment that a failed node would be
  dead in the water or degraded until recovered. He also frames the offering as
  probably not best-in-class uptime, and the response is the roughly one percent
  gap rather than a denial.
- **Two questions Kann raises up front are never answered.** His opening lists
  decommissioning cost and what jurisdiction applies to compute hundreds of miles
  from any coast. Neither returns. Environmental effects are addressed only
  indirectly, by arguing that avoiding the seafloor avoids seafloor consequences,
  and survivability in heavy weather is asserted from prototype experience rather
  than examined.
