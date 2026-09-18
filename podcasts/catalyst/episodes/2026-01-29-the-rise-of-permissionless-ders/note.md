---
episode: "The rise of permissionless DERs"
published: "2026-01-29"
guest: "James McGinniss, co-founder and CEO, David Energy"
threads: [ders, batteries, interconnection, demand-flexibility, policy-and-regulation]
source_transcript: "transcript.md"
note_version: 1
---

## The question

What are "permissionless" distributed energy resources, and can batteries small
enough to plug into a wall outlet ever add up to enough capacity to matter?

## The answer

Yes on both, on McGinniss's account, and the reason is economic rather than
technical. A standard household outlet is already a legal two-way connection to
the grid, so a device that uses one skips the interconnection process and the
electrician. That removes the soft costs that make up roughly half of a
conventional residential install, which turns distributed storage from a premium
resilience product into a cheap affordability product and opens it to renters,
who have never been an addressable market. He would not be shocked to see tens
of gigawatts in the US within five to ten years, and offers that as a personal
expectation rather than a forecast.

## The argument

Permissionless, in McGinniss's usage, means anything that gets onto the grid
without an interconnection agreement; he says he now prefers "plug-in" when
talking to customers because it describes what the thing actually is. The
physical insight underneath does most of the work in the episode. A 120-volt or
240-volt outlet is already a bi-directional connection point, and it is safe to
push power into it at the circuit level, so a device using one inherits an
interconnection that already exists. A conventional battery install, by
contrast, means opening the electrical panel, which he likens to open-heart
surgery, and it is that surgery which drags in the electrician, the design work
and the utility paperwork.

The consequence is economic, not physical. Soft costs, meaning permitting, labor
and customer acquisition, run at 50% or more of a residential install, and
plug-in attacks all three at once: no permit under the rules being written now,
no installer, and a product bought online rather than sold door to door. What is
left is hardware, so the floor on distributed storage falls to the cell cost and
nothing else. Conventional installs cannot follow, because their soft costs do
not get cheaper when cells do. This is why he insists the category is about
affordability rather than resilience. The last decade of residential storage sold
resilience as a premium product; a device with no soft costs is selling bill
savings, which is a different customer entirely.

Kann puts the obvious objection: the batteries are tiny, so even a cheap one can
only shave a sliver of a bill. McGinniss's answer is that small is only
meaningful relative to the load it serves. A one-kilowatt battery is a large
share of a one-bedroom apartment's draw, and renters are a market nobody
currently addresses at all. His evidence is Germany, where retail power at 40 to
50 cents a kilowatt-hour made plug-in systems pay for themselves purely by
avoiding purchases, with no export compensation, no net metering and no virtual
power plant required. Kann notes, and McGinniss agrees, that the German wave is
mostly balcony solar rather than batteries, so the precedent is about purchasing
behavior and the install model more than about the specific device. The same
logic runs in commercial buildings through a different lever: a small business
exposed to demand charges can save around $50 per month for each kilowatt of
peak it shaves, which compounds across multiple locations.

The regulatory turn is the part most likely to be missed, because two different
ceilings are in play. Bills introduced in roughly 24 to 30 states set an export
limit, typically about 1.2 kilowatts per meter, derived from what a 20-amp
circuit can carry; the utilities' concern is line workers encountering an
energized line during an outage. But a system that never exports, one that simply
carries load off the grid, arguably falls outside that regime entirely, and
McGinniss raises this as an open question rather than a settled one: does 20
kilowatts of behind-the-meter capacity on a 50-kilowatt peak need an
interconnection agreement at all? That distinction is what lets him talk about 5,
10 and 20 kilowatt systems installed through outlets while the pending
legislation argues over 1.2. His aggregate case rests on it. Against grids with
30 to 90 gigawatt peaks, he argues these resources could reach double-digit
percentages of capacity, 10% or more, rather than being a rounding error. He does
not walk through the arithmetic that gets there, and when Kann asks the narrower
question of whether a portfolio of these devices could be packaged as capacity to
accelerate a data center interconnection, McGinniss calls the example interesting
and moves to the grid-wide number instead of endorsing the deal structure.

## What you need to know first

- **Interconnection agreement.** The utility's permission and paperwork for
  connecting a generating device to the grid, and the queue that goes with it.
  Avoiding it is the entire definition of "permissionless."
- **Behind the meter versus export.** A device can either reduce what a building
  draws from the grid, which the meter sees as lower consumption, or push power
  back out onto it. Almost every regulatory fight in this episode is about the
  second case only.
- **Soft costs.** Everything in an installed system that is not hardware:
  permitting, design, labor, sales and customer acquisition. The claim that these
  are half of a residential install is the load-bearing number here.
- **Demand charge.** A commercial bill component priced on the highest power draw
  in the period rather than on total energy used. It is why a small battery can
  be worth more to a business than to a household.

## Details worth keeping

- The category is broader than batteries. McGinniss cites a battery built into a
  cooktop (Impulse Labs), battery-buffered DC fast charging that avoids an
  interconnection upgrade (Electric Era), and a battery inside a heat pump
  (Carrier). Commercial and industrial off-grid systems may still need permits
  even when they need no interconnection.
- Safety is largely settled even where policy is not. He says UL-certified
  products conforming to the electrical code, which he names only as the NEC and
  never spells out, are already allowed under current guidance. The live disputes
  are local fire and permitting authorities and the state export bills.
- Demand response eligibility is set by program rules, not physics. An aggregator
  may face a 100-kilowatt threshold while the per-device minimum runs as low as
  100 or even 10 watts. He cites a possible 10-kilowatt-per-meter rule in the New
  York grid operator's territory against Massachusetts enrolling devices directly
  without going through the meter.
- Duration comes from the pairing, not the battery. Systems are often sized
  roughly one-to-one with the load, so a 1.2-kilowatt battery attached to a
  400-watt appliance behaves as a three-hour battery.
- Product design is still at the beginning. Early plug-in deployments used camping
  power stations because that is what existed. The open questions are basic ones:
  120 versus 240 volts, whether the unit hangs on a wall, sits on a fridge or
  tucks into a corner, and whether it is built to be networked at utility scale
  rather than as a consumer appliance.
- Kann's framing of customer acquisition cost is stronger than McGinniss's answer.
  Kann says the model only works if that cost is effectively zero; McGinniss says
  a digital channel still carries one, that it differs between a manufacturer
  listing a product for sale and a third party recruiting devices into a virtual
  power plant, and that even if it is not zero it is exponentially cheaper than
  door knocking.

## Claims worth citing

All figures as stated on 2026-01-29. The regulatory count describes pending
legislation and will move quickly; the cost figures are a founder's
characterization of his own market rather than published data.

- Soft costs are typically 50% or more of a residential install, and plug-in can
  put them near zero. The three components named are permitting, labor and
  customer acquisition cost. (McGinniss)
- Bills allowing grid export from plug-in devices have been introduced in roughly
  24 to 30 states, typically capping export at about 1.2 kilowatts per meter,
  tied to the capacity of a 20-amp circuit. (McGinniss)
- Germany adopted about 4 million of these systems over four years, more than a
  gigawatt of installed capacity. He describes that as about the same size as
  traditional single-family installs, which could mean comparable in unit count
  or in capacity; the transcript does not resolve it, and 4 million units to one
  gigawatt implies a very small average system. (McGinniss)
- German retail electricity at 40 to 50 cents per kilowatt-hour was the trigger
  for that adoption, with the value coming from avoided purchases rather than
  export compensation. (McGinniss)
- New York City commercial work is yielding about $50 per month for each kilowatt
  of demand shaved. (McGinniss)
- Installed cost is under 10% of total system cost in their commercial
  applications and "closer to zero" in residential plug-in. This is a different
  metric from the 50% soft-cost figure above. (McGinniss)
- Kann's payback arithmetic, which McGinniss does not confirm: $50 per month is
  $600 a year, against a residential battery at perhaps $800 per kilowatt-hour
  today and maybe $400 later, giving payback under a year. The savings figure is
  per kilowatt of demand and the cost figure is per kilowatt-hour of energy, so
  the two do not combine cleanly. (Kann)
- Tens of gigawatts of these systems in the US over the next five to ten years,
  stated as something that "wouldn't shock" him rather than as a projection.
  (McGinniss)
- Against grids with 30 to 90 gigawatt peaks, potential in the double-digit
  percentages of capacity, "10% or more." Stated as potential, with no arithmetic
  given. (McGinniss)
- A data-center-scale deal built from these devices would need roughly 100
  megawatts, implying about one hundred thousand premises. (Kann)

## Where it's contested

- **The founder is describing his own market.** McGinniss runs a company
  deploying these systems, no third-party deployment data or independent cost
  study appears, and Kann does not press for one. Kann states no financial
  interest in the company. The category diagnosis is separable from the company's
  prospects and is the more durable part.
- **The regulatory status of the non-exporting case is unresolved, by his own
  account.** He raises the question of whether large behind-the-meter capacity
  that never exports needs an interconnection agreement, and leaves it open. Much
  of his scale argument depends on the answer being no.
- **The scale objection is answered by redefinition rather than rebuttal.** Kann's
  point is that a tiny battery saves little; McGinniss's reply is that the right
  comparison is a small load, which is true and also narrows the market to
  apartments and small commercial sites. He concedes that apartments specifically
  are "a little limiting" relative to what plug-in could do generally.
- **Customer acquisition cost is asserted rather than demonstrated.** The claim
  moves from plug-in "totally removing" that cost to it being not zero but small,
  within a few minutes and without a figure.
- **The German precedent is a solar precedent.** Both speakers acknowledge the
  four million systems are largely balcony solar, while the US category under
  discussion is mostly batteries, which earn their return through a different
  mechanism.
- **Product maturity is early by his own description.** He calls form factors
  "extremely nascent" and notes the companies in the space have nearly all been
  founded within the last five years.
