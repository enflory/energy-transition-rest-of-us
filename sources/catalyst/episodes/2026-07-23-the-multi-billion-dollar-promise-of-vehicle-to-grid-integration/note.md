---
episode: "The multi-billion dollar promise of vehicle-to-grid integration"
published: "2026-07-23"
guest: "Steve Letendre, senior advisor, Vehicle-Grid Integration Council; founder and editor, V2Gnews.com"
threads: [evs, ders, demand-flexibility, backup-power, policy-and-regulation]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Bidirectional cars and chargers finally exist, so if the parked battery in the
garage still does not show up on the grid, what is actually holding it back?

## The answer

Revenue and rules rather than hardware, with the qualification that the hardware
is newer and thinner than the headline suggests. Using the car to back up the
house already pays for itself against the cost of a whole-home generator.
Selling power to the grid pays only in the handful of territories that run a
program, warranty language is mostly silent on whether exporting voids anything,
and the safety standard for the cheaper of the two architectures was approved
about a month before recording. Letendre expects policy to unlock the market the
way it unlocked rooftop solar; Kann argues the real unlock was financing, and
they settle on the same requirement, a revenue stream stable enough to lend
against.

## The argument

Three things have to be in place: a vehicle that can push power out of its
battery, a charger that can take power in both directions, and software that
optimizes the flow while respecting the owner's constraints, because the car was
bought for mobility first. The interesting split is in the second piece, and it
is really a question of where the inverter lives. In the DC architecture the
conversion happens off-board, in the charger or a wall box beside it, which is
how the Ford F-150 Lightning and General Motors' vehicles work; in the AC
architecture the vehicle carries its own grid-interactive inverter and exports
alternating current to a much simpler charger, which is how the Tesla Cybertruck
works. Letendre says there is a pretty clear cost advantage to AC, since the
off-board conversion device is expensive at today's limited production volumes,
and that AC will likely be the lower-cost option for residential light-duty
vehicles, while being equally clear that the cost does not disappear, it moves
onto the vehicle. He does not extend the conclusion to
electric school buses, the other big V2G market, where DC dominates and he does
not expect a switch to AC to save much. Asked why the large automakers went DC
first, he says he has no visibility into their internal decisions and points
instead at standards: the safety standard for AC systems was only approved about
a month before recording, and there was previously a simpler route through DC.

The economics then decide everything, and this is where the assumptions matter
more than the totals. A DC system today runs roughly $8,000 to $10,000 fully
installed. Letendre has no good figures for AC and guesses the premium for
bidirectional capability over an ordinary charger lands somewhere between the
high hundreds and a few thousand dollars, explicitly a guess given how few
systems are deployed. On the value side he splits the question in two.
Home backup already clears the bar, because the comparison is a whole-home
standby generator and he expects a bidirectional system to be competitive
against one. Grid export is the harder case, because it requires a utility
willing to pay and an interconnection process worth going through. His figure
for what it could be worth is the one to watch: in some jurisdictions utilities
compensate peak shaving at $200 to $300 per kilowatt per season, so a
ten-kilowatt system could potentially earn about $3,000 a year. Every word of
that sentence is load-bearing. The arithmetic only reaches $3,000 at the top of
the stated range, it applies in the minority of territories that run such a
program, it assumes the full ten kilowatts is available when called, and it does
not net out the interconnection cost that Letendre himself names as an open
question a sentence earlier. Kann converts it into a payback of a few years and
calls it compelling, which is a fair reading of the number but a stronger claim
than the number supports. Letendre does not correct him; he changes the frame
instead, to stacking backup value on top of grid revenue, which is how Ford and
GM have actually gone to market, selling for home backup and later unlocking
grid export by software update where a program existed.

Then the two objections that have dogged V2G for years, battery degradation and
warranties. Letendre calls the warranty picture a lot of gray area, and the
concrete examples are thin: Nissan publicly stated that using the Fermata Energy
platform would not affect its warranty, which he believes was a first anywhere,
and Ford's warranty indicates that using an F-150 for home backup does not void
coverage. Beyond those he describes little clarity, and his expectation that
manufacturers will publish explicit parameters is a forecast, offered with
confidence but without a timeline. On degradation his argument is mechanical:
driving draws 125 to 150 kilowatts out of the pack while grid service draws
around ten, so the discharge rate and its wear are far gentler than ordinary
acceleration, and he adds that recent reports suggest batteries are lasting
longer than expected, without naming them. The related worry, that exporting
during an outage strands the owner without range, he answers with the software
constraint and the principle that mobility comes first, while conceding there is
not much data yet on what limits people actually set. Underneath sits the
assumption the whole market rests on and which nobody quantifies: participation.
His own analogy is ride-hailing, where most people never drive strangers around
but enough do that it works, and he expects V2G to be similar, a fraction of
owners adding up to a significant grid resource. He does not say what fraction.

The closing exchange is the most useful disagreement in the episode. Letendre's
model is rooftop solar: state interconnection rules, net metering and incentives
came first because policymakers decided rooftop solar was a public good, and 20
years later it is a multi-billion-dollar industry with dramatically lower
prices, so V2G needs equivalent policy leadership. Kann partly disputes the
causal account. Policy was table stakes, he says, but the inflection in the late
2000s came from financing, when SolarCity, Sunrun and Sungevity turned a large
upfront payment with a seven-year payback into no money down and savings from
day one. The V2G analogue he would want to see is a manufacturer bundling the
bidirectional charger at no incremental cost and giving away whole-home backup
in exchange for the right to call on the battery under defined conditions.
Letendre agrees and closes the loop rather than conceding: what made the solar
lease bankable was the policy-guaranteed revenue behind it, so the missing piece
for V2G is a revenue stream predictable enough to finance against. That is
where the episode lands, and it is a sharper answer than either the hardware
story or the policy story alone.

## What you need to know first

- **Vehicle-to-grid and vehicle-to-home.** Exporting the car's battery to the
  electricity system versus using it to power the house during an outage. They
  need the same equipment and have completely different economics, and most of
  the episode's apparent contradictions dissolve once you keep them apart.
- **AC and DC architecture.** Whether the inverter that converts the battery's
  direct current into the alternating current a house or grid uses sits in the
  charger, off the vehicle, or on board the vehicle itself. That placement
  decides which part of the system carries the cost.
- **Peak shaving compensation.** Utilities paying a customer-owned resource for
  being available to reduce demand at system peak, quoted here per kilowatt per
  season rather than per kilowatt-hour delivered.
- **Aggregation programs.** Many small customer-owned devices dispatched
  together as one resource. Both speakers call these VPPs and neither expands
  the acronym; Kann also describes the same idea as aggregated distributed
  capacity.

## Details worth keeping

- The current shopping list is short but growing: the Cybertruck as a complete
  in-house system, the F-150 Lightning with Ford's charging station and a Sunrun
  conversion box, GM's own branded bidirectional charger working with most of
  its electric range, Kia paired with the Spanish manufacturer Wallbox, and a
  company called Decibel whose home energy station is paired with Volvo and
  Polestar. Rivian has announced an AC-architecture R2.
- Electric school buses are the quiet other half of this market. Letendre says
  nearly all of them now come off the line bidirectional-capable, with
  higher-power DC chargers available to match.
- Connector standards have already turned over once. Letendre's earlier work at
  Fermata Energy deployed dozens of projects on Nissan Leafs using a charger the
  company built on the CHAdeMO platform, which has since fallen out of favor in
  the US in favor of CCS and the North American Charging Standard.
- Letendre understands that Tesla already offers in-app enrollment in grid
  programs, starting in Texas and now with Pacific Gas and Electric's pilot in
  California, though he states it as his understanding rather than firsthand. He
  says
  manufacturers envisage enrollment eventually happening at the dealership at
  point of sale, with the customer's permission, and that the industry is
  definitely not there yet.
- Programs exist or are emerging in California, Massachusetts, New York,
  Maryland, Colorado and Connecticut, which is also a useful list of where the
  economics currently do not apply.
- Letendre's affordability argument is that electric vehicles can help rather
  than burden a grid facing load growth and cost pressure, by shifting when they
  charge as well as by discharging.

## Claims worth citing

All as stated on 2026-07-23. Hardware prices, program compensation and the list
of participating states are all moving quickly and should be re-checked before
quoting.

- Electric cars spend 90 to 95 percent of their lives parked. (Kann)
- A Kia EV9 carries about 100 kilowatt-hours, roughly seven Powerwalls of
  capacity. (Kann)
- Every Cybertruck on the road can export north of 11 kilowatts. (Kann)
- GM says it alone has more than 250,000 bidirectional-capable vehicles on the
  road; at about 10 kilowatts each Kann calculates 2,500 megawatts of nameplate
  capacity. The nameplate figure is Kann's own arithmetic, not a measure of
  capacity that is enrolled, available or contracted. (GM, cited by Kann;
  arithmetic by Kann)
- GM's bidirectional charging bundle runs about $7,000 before installation, and
  Kann says grid programs have so far paid drivers far less than that. (Kann)
- A V2G DC system costs roughly $8,000 to $10,000 for the full installation
  today, at limited production volumes. (Letendre)
- No good numbers exist yet for AC systems; Letendre guesses the incremental
  cost of bidirectional capability over a one-way charger at high hundreds to a
  few thousand dollars, explicitly a guess. (Letendre)
- Some jurisdictions compensate peak shaving at $200 to $300 per kilowatt per
  season, so a 10-kilowatt system could potentially earn about $3,000 a year.
  The phrasing runs kilowatts and seasons together, and the $3,000 only appears
  at the top of the range. (Letendre)
- The UL safety standard for AC bidirectional systems, numbered 1741 SC, was
  approved about a month before recording, intended to comply with an
  institute-issued standard for interconnecting distributed resources whose
  number the transcript garbles. (Letendre)
- Nissan publicly stated that use of the Fermata Energy bidirectional platform
  would not affect its vehicle warranty, which Letendre believes was the first
  such statement by any manufacturer worldwide. (Letendre)
- Ford's warranty indicates that using an F-150 for home backup power would not
  void it, stated with an "I believe." (Letendre)
- Driving draws 125 to 150 kilowatts from the pack against roughly 10 kilowatts
  for grid service, so discharge for the grid is gentler than ordinary driving.
  (Letendre)
- Numerous unnamed studies are said to show electric vehicles will be the single
  largest source of grid flexibility in the not-too-distant future. (unnamed
  studies, cited by Letendre)
- Rooftop solar became a multi-billion-dollar industry roughly 20 years after
  states put interconnection, net metering and incentives in place. (Letendre)

## Where it's contested

- **The title's figure belongs to rooftop solar, not to V2G.** Nobody in the
  episode sizes the vehicle-to-grid opportunity in dollars. The only
  multi-billion-dollar number is what rooftop solar became after two decades of
  policy support, offered as an analogy, and the nearest thing to a market
  estimate is Letendre calling the cost-versus-value question the billion-dollar
  question. Everything quantified here is per household.
- **The $3,000 a year is a ceiling under favorable conditions, not a typical
  return.** It requires the top of the compensation range, one of the minority
  of territories running a program, full availability of the system when called,
  and no deduction for interconnection, which Letendre flags as unresolved in
  the same breath.
- **Kann's payback conclusion is his own.** He converts the figure into a
  few-year payback and calls it compelling; Letendre neither endorses nor
  disputes it, and answers on a different point about stacking backup value with
  grid revenue.
- **The host's premise that the hardware question is settled is partly
  undercut by the guest.** Kann's monologue argues the hardware excuse is
  running out. Letendre describes a fairly limited number of compatible vehicle
  and charger combinations, chargers in limited production, and an AC safety
  standard approved only a month earlier, which makes the hardware constraint
  loosening rather than gone.
- **The guest is an industry advocate and says so.** He advises a council
  representing manufacturers and charger makers and previously worked at a V2G
  company, both stated on air. Kann calls him obviously a bull on the space and
  he does not dispute it. That is not a reason to discount his facts, but his
  forecasts about manufacturers and policy are made from inside the industry
  asking for the policy.
- **Warranties are the weakest documented area.** Two manufacturer statements
  exist, one of them recalled with a hedge, and his expectation that the rest
  will follow is a forecast rather than an observation.
- **Degradation is argued from mechanism, not measurement.** The low discharge
  rate argument is plausible and the supporting reports are not named or dated.
- **Participation is unquantified.** The ride-hailing analogy concedes that most
  owners will never take part; how large the willing fraction is, and therefore
  how much of the theoretical capacity ever reaches the grid, is left open, as
  is what limits consumers set on their batteries, where he says there is not a
  lot of good data.
- **Policy versus financing.** Letendre credits regulation with creating the
  rooftop solar industry; Kann counters that regulation was necessary but the
  inflection came from the lease and power-purchase model. They converge on a
  bankable revenue stream being the requirement, but the disagreement about what
  caused the solar takeoff is real and matters for what one would ask
  policymakers to do.
