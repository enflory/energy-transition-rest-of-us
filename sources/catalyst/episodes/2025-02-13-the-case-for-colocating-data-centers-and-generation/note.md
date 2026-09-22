---
episode: "The case for colocating data centers and generation"
published: "2025-02-13"
guest: "Sheldon Kimber, founder and CEO, Intersect Power"
threads: [data-center-power, interconnection, renewables, energy-storage, load-growth]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2025-02, weeks into the second Trump administration and about three weeks after the DeepSeek selloff. The colocation logic is durable; the tariff outlook, contract prices and project dates are a snapshot."
---

## The question

Why build generation on a data center's own site instead of connecting the data
center to the grid, and does that logic run all the way to going off grid?

## The answer

Because the binding constraint is speed and scale, and colocation attacks it on
three fronts that are easy to run together: a cost-allocation rule, a physical
adequacy problem, and a permitting problem. On off grid, Kimber's position is
that grid connection should become optional rather than absent, since customers
keep wanting it as insurance even on sites engineered to run without it.

## The argument

Kimber starts from a premise he has been making for years: the grid is broken, so
load has to come to generation rather than the other way round. Three trends are
pulling load up at once, and he is careful that only one of them is about
climate. Digitalization is the loud one. Electrification is the one he finds more
interesting, because it is increasingly happening on product merit rather than
policy, as electric motors and arc-furnace steelmaking simply get better.
Decarbonization is the third and, in his view, survives whatever the policy
environment. Against that, the conventional path is to secure a site and wait
roughly a decade for a transmission line. He grants that works if you have the
patience and the capital, and that there have been successes, but he doubts it is
the solution set the new loads need.

The case for colocation is really three separate claims of three different kinds,
and colocation arguments routinely blur them. The first is regulatory and is
about who pays. In most jurisdictions, he says, the network upgrades triggered by
a large load interconnection get socialized across ratepayers, so a hyperscaler's
transmission line ends up on everyone's bill, whereas a generator interconnection
usually makes the generator cover more of the substation and related work.
Shifting the interconnection from the load side to the generation side changes
who bears the cost, and that is a rules question rather than a physics one. The
second claim is engineering, and turns on the difference between energy and
capacity. Most places, he says, have enough energy in most hours; the real
question is whether the new load pushes the system over at its peak moments.
Onsite batteries, dispatchable gas or the solar itself can keep the site from
contributing at those moments. The third is about permission: renewables are
still the fastest generation to bring online in the United States and will be for
at least another five or six years, and community and regulatory acceptance is
already a constraint on renewables, which he expects to bite harder on new
combined-cycle plants and reactors.

The economics then support a reframe of what baseload means. In the Texas
panhandle, where Intersect's largest sites sit, renewable capacity factors reach
the high seventies, so wind, solar and batteries on one site can run the load
fully carbon free for 75 to 80 percent of the hours in a year, with a bit over 20
percent covered by gas or by the grid. The gas he means is simple cycle or
reciprocating engines, not combined cycle, which he dismisses for this purpose.
He claims that package beats a new combined-cycle plant on cost, given the price
he quotes for one, a five to six year build, and a construction labor pool that
in many cases has never built one. Note what the claim is and is not: he is not
saying gas is unnecessary, he is saying the gas actually needed is a different,
smaller and faster kind than the debate assumes.

The limit on all of this is the demand side, and here he is blunt. Asked whether
data centers will run flexibly, he says power is still the tail of the dog and is
not wagging anything. His rough capital cost stack for a gigawatt site is what
carries the argument: on the order of ten billion dollars of data center
structure, five to six billion of power assets, and roughly thirty billion of
chips. Against that denominator, every second the site is not running at full
output is an enormous amortized cost, so curtailing for maintenance or model
changes is normal and curtailing because power is expensive is, in his words,
never. That is what makes colocation a supply-side answer specifically. If the
load will not bend, the generation has to come to it.

## What you need to know first

- **Behind the meter.** Generation sited on the customer's own side of the
  utility meter, serving the load directly rather than selling into the grid.
  Colocation here means behind-the-meter generation on the data center's site.
- **Load interconnection versus generator interconnection.** Two different
  processes with different cost-allocation rules. The asymmetry Kimber relies on
  is that load-side upgrades are more often spread across ratepayers while
  generator-side upgrades are more often charged to the developer. He scopes this
  to "most jurisdictions," not all.
- **Energy versus capacity.** Energy is total kilowatt-hours over time; capacity
  is the ability to serve demand in the worst hour. A grid can be long on the
  first and short on the second, which is why a battery that shifts a few hours
  of supply can unlock a large new load.
- **Combined cycle versus simple cycle.** A combined-cycle plant adds a steam
  cycle to capture waste heat, buying efficiency at the price of capital cost and
  build time. Simple-cycle turbines and reciprocating engines are less efficient
  but cheaper and faster, which is why they suit a resource meant to run only a
  fifth of the hours.

## Details worth keeping

- The head start came from an unrelated bet. Intersect built megasites and
  bespoke interconnection arrangements, technically and commercially, for
  hydrogen production. Hydrogen demand never materialized and AI took over the
  assets. Kimber rejects the prescient framing: they decided a miracle was not
  going to happen and then did the obvious thing.
- His two Texas panhandle sites are described as capable of running fully off
  grid while also holding a grid interconnection, which he calls an energy
  Disneyland.
- The solar and storage market he describes as a weird limbo, with supply-side
  policy support and enormous AI-driven demand both in place and both uncertain
  enough that he does not know whether the business will be ten times larger or
  nonexistent.
- On trade, his point is that tariffs are only part of it. Commerce, trade policy
  and national-defense agencies have all been pressing on Chinese-sourced
  renewable equipment for some time. He expects no improvement and says he is
  surprised it has not already worsened. Intersect's largely American supply
  chain limits its own exposure; he calls it a big problem for the industry.
- Contract prices have risen off their record lows mostly because input costs
  rose, not because developer margins expanded. Developers who signed the
  low-priced contracts and now cannot deliver are, in his description, in chaos.
  He also flags an odd separation: spot prices remain low while 15-year power
  purchase agreement prices drift up, because community choice aggregators and
  corporate buyers know their own load and want the risk off the table.
- On AI demand, his argument for why it compounds is recursive rather than
  demographic. Small distilled models running on phones will launch thousands of
  queries to larger reasoning models, which he likens to adding billions of new
  internet users. He expects inference in aggregate to be a much larger draw than
  training in the long run.

## Claims worth citing

All figures as stated on 2025-02-13, and several describe projects not yet built.
Equipment prices, contract prices and project dates in this market move fast.

- At the panhandle sites, renewable capacity factors in the high seventies allow
  75 to 80 percent of annual hours to run fully carbon free on wind, solar and
  batteries, with a bit over 20 percent needing gas or the grid. He calls this
  probably the cleanest achievable mix in the country outside California and
  Hawaii. (Kimber)
- Rough capital cost for a gigawatt data center: about $10 billion of data center
  structure, of which roughly $2.5 billion is the powered shell; $5 billion to $6
  billion of power assets; and roughly $30 billion of chips. He explicitly rounds
  these. (Kimber)
- A new combined-cycle plant is quoted as "2,000 KW," which in context means
  about $2,000 per kilowatt, on a five to six year build. The transcript garbles
  the unit, so check the source before quoting it. (Kimber)
- Renewables are the fastest form of generation to bring online in the United
  States and will remain so for at least five or six more years. (Kimber)
- Two Texas panhandle sites, one 3 gigawatts and one over 1 gigawatt, each with
  multiple gigawatts of wind and solar and the ability to interconnect comparable
  battery capacity. First gigawatt-scale phases could come online by end of 2027
  or early 2028. (Kimber)
- A very large data center announced under the Google partnership is targeted to
  come online in 2026 and will have a colocation element, which he calls close to
  unheard of. (Kimber)
- Roughly $800 million of initial investment into Intersect from TPG and Google,
  funding solar, storage, wind and some gas colocated with data centers in the
  United States. (Kann)
- Intersect is in the middle of project financing about $9 billion of capital
  expenditure, and expects next year to be larger if two deals under negotiation
  sign. (Kimber)
- Intersect has about $4 billion of assets operating, probably less contracted
  than the market average, with open positions in ERCOT (the Texas grid market)
  and California across energy, capacity and renewable energy credits. (Kimber)
- Power purchase agreement tenors collapsed to 15 years; he does not expect a
  return to 20-year deals. (Kimber)
- Data center load growth was already easily double digit percent four years ago,
  on a substantial base, driven by e-commerce and basic machine learning. Stated
  from memory with no source, and the base is not specified. (Kimber)

## Where it's contested

- **Kann's history of contract tenors gets corrected.** Kann restates the arc as
  20-year deals, then shorter 10-year deals driven partly by Intersect, then a
  swing back toward longer. Kimber disagrees: tenors collapsed to 15, and
  Intersect's short deals and open merchant slices were a response to that rather
  than a cause, because a 15-year deal pushes merchant risk onto the back end of
  a project where you least want it. Take the guest's version.
- **Whether data center load ever flattened.** Kann's counter to the Jevons
  argument is the historical record: two decades of efficiency gains held
  compute's total power draw roughly flat despite far more computing. Kimber
  disputes the premise itself, offers a source-off, and says load never really
  flattened. Neither resolves it, and the disagreement is about a factual premise
  rather than an interpretation.
- **How seriously to take the DeepSeek argument.** Kimber twice says he is not an
  AI engineer. His skepticism rests on distillation requiring an expensive
  predecessor model, and on China's incentive to claim a cheap model without
  conceding that the chip embargo is toothless. He says it feels a little like
  nonsense to him, then argues his conclusion holds even taking it at face value.
- **Flexible load.** Kann says he has seen no evidence of data centers operating
  anything other than 24/7 and asks whether anyone is even discussing it.
  Kimber's answer is a flat no on economics, unhedged, and rests entirely on his
  own rounded capital cost figures.
- **The off-grid question stays open inside the guest's own answer.** He argues
  grid connection should be optional and that his sites could sever from the
  grid, while also reporting that customers pursuing off-grid data centers keep
  trying to get the grid extended to the site anyway.
- **The cost comparison is asserted, not shown.** The claim that renewables plus
  reciprocating engines beat a new combined-cycle plant is directional. He gives
  a price for the plant he is beating and none for the configuration he is
  selling, and the capacity factors and dates describe projects in development
  rather than measured operating results.
