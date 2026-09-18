---
episode: "Repurposing EV batteries for grid storage"
published: "2025-07-24"
guest: "Colin Campbell, chief technology officer, Redwood Materials"
threads: [batteries, energy-storage, waste-and-recycling, evs, long-duration-storage]
source_transcript: "transcript.md"
note_version: 1
---

## The question

When is it better to put a worn-out electric vehicle battery back on the grid
than to shred it for the materials inside it?

## The answer

The choice is a false one, in Campbell's account. Redwood does both, in
sequence: a pack that passes a short inspection goes out to a grid site first
and gets recycled afterwards, so the grid stint is additive rather than an
alternative use. What changed recently is not the batteries but two things
arriving together: enough returning packs to build a business on, and an
installation cost low enough that a pack now needs only one or two years and low
hundreds of cycles of remaining life to be worth deploying.

## The argument

Kann frames the decision as a fork, and it is the standard framing: an
end-of-life pack goes either to materials recycling or to stationary storage,
and which one wins is an economic calculation over the value of recovered
cathode and anode material against the value of grid services, net of processing
or refurbishment cost in each case, with new lithium iron phosphate storage as
the competing option. Kann qualifies that competing price: outside the United
States it has been a falling knife, while inside it tariffs and similar factors
make it more complicated. Historically the fork resolved to recycling. The packs themselves are in better shape than that framing implies.
Campbell says they arrive physically almost new, because a vehicle battery is an
extremely durable engineered object, and electrically they arrive when the owner
gets frustrated rather than when anything fails, typically around 20% less
capacity and 20% more impedance. They are predominantly nickel-based NMC cells,
because what comes back today is roughly what was built a decade ago.

Campbell's first move is to reject the fork. Redwood does not choose: it sends
the pack to a grid site to earn grid services and then recovers the metals
afterwards, which he describes as a detour rather than a destination. That
reframing is what makes the economics work, because it means the grid stint does
not have to beat recycling, only add to it. The second move is the surprising
one. Because the cost of getting a pack onto a grid site is now very low, the
amount of useful life a pack needs to have left is correspondingly small, on the
order of one to two years and low hundreds of cycles. Kann works out the
implication out loud: for that to be true against a new purpose-built system
with a ten-year warranty, the fully installed cost of the second-life asset has
to be far below the new one. Campbell agrees, and volunteers that he was
sceptical of second-life storage until roughly the previous year, on the
reasonable grounds that a repurposed object rarely beats something optimized for
the job. What changed his mind was the return volume arriving at the same time
as a cheap way to install the packs.

The integration cost is the part that fell, and the description is almost
anticlimactic. A five-minute electrical inspection checks cell balance and
impedance and whether the pack's internal electronics still report diagnostics;
if those come back clean, the pack is wheeled into the field and plugged in. The
packs are not opened and the modules are not removed, so the site amounts to a
parking lot of electric vehicles with the wheels taken off. Kann presses on the
obvious objection, which is that this sounds like something anyone could do.
Campbell's answer is three things rather than one: power electronics designed to
talk to an extremely wide variety of pack types and dispatch each sensibly as
part of one coherent asset, site mechanical design cheap enough not to eat the
margin, and access to the feedstock in the first place, since Redwood already
collects north of 80% of end-of-life electric vehicle packs in the United
States. The third of those is positional rather than technical, and Campbell
says so himself: collecting packs like this is not simple, and what is hard to
copy is aggregating a heterogeneous stream arriving from a million places.

That heterogeneity also shapes where these assets fit on the grid. Campbell says
second-life packs can compete head to head in the two-hour and four-hour
markets, but they shine at longer durations, four to eight hours and possibly as
much as twenty. The technical reason is that a pack's degradation shows up as
cell imbalance, and because cells sit in series the whole pack is limited by its
weakest member during hard discharge; discharge slowly and that weakness matters
much less. Kann correctly points out that this is true of any battery, not just
a used one, and that the reason nobody builds twenty-hour lithium-ion projects
is economic, since cost scales roughly linearly with duration. Campbell concedes
the point directly: it is not a different equation, the energy is simply cheap
enough that stacking more of it stays affordable. On scale, the supply curve is
unusually predictable because it was set a decade ago by vehicle production.
Roughly five gigawatt-hours a year is coming off US roads now against roughly
fifty gigawatt-hours of US storage deployed in the prior year, so the retirement
stream is about a tenth of deployment; Redwood expects to deploy low single-digit
gigawatt-hours of second-life storage this year and next.

## What you need to know first

- **Second life.** Reusing a battery pack substantially intact in a new
  application before recycling it, as distinct from refurbishing it back into a
  vehicle or breaking it down for materials. The whole episode turns on second
  life being a stage rather than a fork.
- **NMC and LFP.** The two dominant lithium-ion cathode families. NMC is the
  nickel-based chemistry used in most electric vehicles a decade ago and carries
  more recoverable metal value; LFP is the iron-phosphate chemistry, cheaper,
  with less metal worth recovering. Returning packs are mostly NMC today and
  will shift toward LFP as the newer fleet ages out.
- **C-rate.** How fast a battery is charged or discharged relative to its
  capacity. Campbell's duration argument depends entirely on it, because a tired
  pack's weakest cell constrains it much less at low discharge rates.
- **Cell balance and impedance.** The two electrical health measures in the
  five-minute inspection. Impedance is internal resistance, which rises as cells
  age; cell balance is how evenly the cells in a series string have aged.

## Details worth keeping

- The rest of Redwood's feedstock is everything else with a cell in it: earbuds,
  toothbrushes, power banks. Campbell calls it a battery nerd's fantasy land and
  says it is too varied to reintegrate, so second life for those streams is not
  something the company has looked at closely.
- On how far second life could stretch, he cites what he calls a constitutional
  distaste for throwing away anything with useful life left. He doubts
  toothbrushes ever qualify and thinks kilowatt-hour-scale power banks might
  eventually, but says that is a long way off.
- On chemistry the power electronics are agnostic: high nickel or iron
  phosphate, high or low voltage, old or new, all plug in. The economics differ
  for LFP, with lower metals value and different cycle life, degradation and
  energy value, but Campbell says the grid detour still makes sense. He gives no
  numbers for it.
- Most manufactured battery energy goes into vehicles, which Campbell reads as
  good news for second life, because vehicle packs are the most robustly
  engineered and the easiest to redeploy.
- Kann notes the timing problem in the other direction: because recycling
  volumes lag manufacturing by about a decade and the electric vehicle
  inflection came less than ten years ago, the real ramp in available packs
  arrives over roughly the next five years rather than now.
- The occasion for the episode is that Redwood, best known as a battery
  materials recycler, has launched a stationary storage division called Redwood
  Energy. Kann describes the company as founded by Tesla founder JB Straubel and
  introduces Campbell as a longtime Tesla veteran.

## Claims worth citing

All figures as stated on 2025-07-24, and all of them from the chief technology
officer of a company selling this service. Storage prices, deployment volumes
and return volumes all move quickly; the forward-looking figures are company
projections rather than results.

- A returning electric vehicle pack typically shows about a 20% capacity
  decrease and about a 20% impedance increase. (Campbell)
- If the mechanical and electrical inspection comes back clean, about 95% of
  packs are usable for grid-scale storage. Campbell later reuses "95% of the
  time" to describe when the grid detour is economically sensible; the two uses
  are not obviously the same measurement. (Campbell)
- A pack needs roughly one to two years and low hundreds of cycles of remaining
  life for grid deployment to pay. This is stated as the threshold for making
  economic sense; he never separately states how long the packs actually last
  once deployed. (Campbell)
- Redwood collects north of 80% of end-of-life electric vehicle packs in the
  United States. (Campbell)
- About five gigawatt-hours a year of electric vehicle batteries are coming off
  US roads, stated on a rated, as-new capacity basis. Discounting 50% to be
  conservative or 70% to be extremely conservative still leaves gigawatt-hours
  a year of useful energy. Campbell gives no single available-energy figure.
  (Campbell)
- About 150 gigawatt-hours a year of new electric vehicle production is going
  into service. He confirms the five gigawatt-hour figure is US-only but does
  not say whether the 150 is US or global. (Campbell)
- About 50 gigawatt-hours of battery energy storage was deployed in the US in
  the prior year, making the retirement stream roughly a tenth of deployment.
  (Campbell)
- Roughly 80% of manufactured battery energy goes into electric vehicles.
  (Campbell)
- Redwood expects to refurbish and deploy low single-digit gigawatt-hours of
  second-life storage this year and next. (Campbell, company projection)
- Second-life packs can compete in two-hour and four-hour markets and are better
  suited to four, eight, or possibly twenty hours. (Campbell)
- A new fully delivered LFP storage project at a couple of hundred dollars per
  kilowatt-hour with a ten-year warranty life. (Kann, explicitly a guess)

## Where it's contested

- **The guest states his own prior scepticism plainly.** Campbell says he was
  always a little sceptical that second-life storage could compete with a
  purpose-built product, and that it only started to make sense in about the
  last year, on the back of return volumes and the low-cost integration method
  arriving together. That is a recent reversal, not a settled position.
- **Kann's sharpest push goes to where the innovation actually is.** If the
  process is a five-minute check and a plug, anyone could do it. Campbell's
  answer is at least as much a statement about Redwood's position in the
  collection market as about a technical breakthrough.
- **The 95% figure carries a condition that is easy to drop.** It applies to
  packs whose inspection comes back clean, not to all incoming packs.
- **The volume figures need care.** The five gigawatt-hours is rated rather than
  available capacity, and Campbell offers two different haircuts without
  settling on one.
- **Second-life LFP is a forecast, not a result.** Those packs have not started
  arriving. Campbell says the economics differ but still work, without numbers
  and without deployment experience behind it.
- **Nothing in the episode is independent measurement.** No third-party
  performance data, no degradation data from deployed second-life sites, no
  warranty, insurance or safety terms, and no customers are named. The framing
  as a two-way decision tree comes from Kann's opening monologue and is
  overturned by the guest within a few minutes.
- **Campbell hesitates to generalize.** Asked to confirm the tidy rule that
  vehicle packs end up on the grid and everything else gets recycled, he
  explicitly declines to commit.
