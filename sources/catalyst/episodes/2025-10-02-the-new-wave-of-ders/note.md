---
episode: "The new wave of DERs"
published: "2025-10-02"
guest: "Dana Guernsey, co-founder and CEO, Voltus"
threads: [ders, demand-flexibility, market-design, data-center-power, interconnection]
source_transcript: "transcript.md"
note_version: 1
---

## The question

How did demand response get from emergency phone calls to an everyday grid
resource, and what can it now do about load growth?

## The answer

By becoming ordinary. Aggregation, market rules that pay a megawatt of reduction
like a megawatt of supply, and cheap connected hardware turned a crisis-only
tool into something dispatched somewhere every day of the year, earning across
capacity, reserves and energy rather than a few summer afternoons. The newest
move points that resource at the interconnection problem: a large load funds an
incremental virtual power plant in the constrained zone, the accredited capacity
is handed to the utility, and the load gets sited faster. That product launched
the day of recording, so it has no track record yet.

## The argument

The arc Guernsey describes has three stages. Before aggregators there were
utility interruptible programs: manual phone calls to very large industrial
customers, who would cut their usage during a crisis. She calls it a fire
extinguisher, often not used at all. Then aggregators arrived, EnerNOC among the
first, and with them the idea that a technology platform plus a portfolio could
do something no single site could. Then came rules, in particular Federal Energy
Regulatory Commission orders 719 and 745, which she says started to value a
megawatt of demand reduction the way a megawatt of supply is valued. The end
state is the one she leads with, and she is only half joking that it makes the
topic boring:
on her platform at any given moment there are somewhere between one and twenty
dispatches running, and it has been dispatched on 365 of the last 365 days. When
she posted that, the response was surprise, which is the tell that the outside
view of this market is still the fire extinguisher.

What broadened was not one thing. There is more equipment with an automatic
on-off switch and an internet connection; more use cases, having graduated from
capacity emergencies to economic dispatch, balancing renewables, ancillary
services (the fast-response products grid operators buy to keep supply and
demand matched), local congestion management and even carbon-driven dispatch;
and more need, because prices are rising and load is growing. The participant
list now runs to more than 50 verticals within commercial and industrial plus
residential, from an electric vehicle in a driveway and a smart thermostat
through retail, big box stores, school districts, wastewater treatment plants
and commercial real estate, up through paper and steel mills, crypto miners, and
AI data centers at the top. The heterogeneity is the point rather than a
complication: assets with different operating constraints get paired so that the
aggregate can answer what the grid asks, which she describes as Tetris. The
underlying resource is still largely load control on conditioned space, now
increasingly alongside behind-the-meter assets, with battery storage one of the
fastest-growing categories as its costs fall.

Ask what that earns and she answers "it depends," twice, and then gives a trend
rather than a rule. Value is smoothing out. The hottest, peakiest summer day as
the whole ballgame belongs to the earlier era; there are winter peaks now, and
shoulder-season tightness caused by generator outages, and reserve prices can
actually be higher in the shoulder seasons precisely because other resources are
short. Capacity and reserves are both effectively call options, paid for being
available rather than for energy delivered, and reserve markets clear daily.
Customers who participate economically curtail whenever prices cross their own
threshold, or strike price, which clips price spikes rather than calendar peaks.
On top of that, traditional capacity programs are now being called over and
over; she
has lost count of how many times. She likes the frequency for two reasons. It
spreads the payments, and it exercises the muscle, because the thing that
actually matters to her is that when the grid calls, the resource shows up.

That leaves the question of what is holding it back, and here she declines to
name a single binding constraint: it is all of the above. Higher prices widen
the addressable set because more things pencil. Deployment simply takes time.
Market rules move, and the capacity accreditation changes in PJM meant more
megawatts showed up but were counted differently. And the one she would fix with
a magic wand is data access: smart meters were deployed and put into rate base,
and in a shocking number of territories the data is still hard to get, even for
the customer whose meter it is. The new product follows from the same logic. If
the constraint is capacity in a particular zone, define the constraint
geographically, build an incremental virtual power plant inside it, run the
resulting megawatts through the market's own accreditation process, and transfer
the accredited capacity to the utility with no money changing hands there,
because the data center funds it. On her account that is a win all round: the
utility gets capacity it can count, the load gets permission to site, and
ratepayers do not see the cost on their bill and can opt into earning from the
program themselves. The reframe underneath it is that co-location need not mean
the same land parcel; unless the physical constraint is something
like a substation upgrade, co-locating at the constraint is what solves the
problem, which opens up the whole toolkit. And her closing argument is
explicitly one about market design rather than economics: this is a utilization
problem, capacity built for a sliver of hours, so even if you could buy gas
plants off the shelf tomorrow, using what is already there would be the better
outcome.

## What you need to know first

- **Demand response and virtual power plants.** Paying electricity customers to
  use less, or to dispatch their own equipment, when the grid needs it. A
  virtual power plant is an aggregator's portfolio of those customers operated
  together so it can be bid and dispatched like a power plant.
- **Capacity accreditation.** The process by which a market decides how many
  megawatts a resource actually counts for, which is usually less than its
  nameplate. In PJM the resulting unit is called UCAP; other markets name it
  differently. Changing the accreditation method changes everyone's megawatts
  without anything physical changing.
- **Capacity and reserves versus energy.** Capacity and reserve payments buy
  availability, which Guernsey describes as call options on energy. Energy
  payments are for electricity actually delivered or not consumed. The three
  have very different cash flow shapes, which is why the revenue answer is
  "it depends."
- **Behind-the-meter assets.** Generators or batteries on the customer's side of
  the utility meter, dispatchable alongside simply reducing consumption.

## Details worth keeping

- Kann's framing in the introduction is that EnerNOC is a forgotten proof point:
  demand response produced a venture-backed initial public offering in 2007, not
  a special-purpose acquisition, which he says very few categories in this sector
  can claim. It was later bought by Enel and is now Enel X, which is part of why
  newer entrants do not know the history. Guernsey joined EnerNOC around 2007 or
  2008 and co-founded Voltus in 2016.
- Voltus deliberately built for every eligible wholesale market in North America
  rather than concentrating. PJM, ERCOT, New York and SPP are its largest simply
  because those markets are larger, not as a strategic bet.
- She has given up trying to predict where capacity auctions land, and runs the
  business as a portfolio of portfolios with an internal goal of being happy with
  participation in every outcome.
- The customer conversation starts with reading the electricity bill, because
  demand charges are sometimes a shockingly high share of it.
- For data, Voltus either taps existing customer systems through interfaces or
  installs a device it calls a Voltlet on top of the utility meter, streaming
  real-time data to its platform.
- A five to ten year price signal is what she says makes it possible to finance
  more energy storage inside a virtual power plant.
- She points to a Duke University paper by Tyler Norris as making the same point
  she saw in charts during her EnerNOC years: a meaningful share of built
  capacity exists for a tiny share of hours.
- Her read on sentiment after Climate Week was uniform optimism, in contrast to
  what adjacent observers expected her to report.

## Claims worth citing

All as stated on 2025-10-02. Dispatch counts, auction outcomes and the new
product's terms are the fastest-moving items here and should be assumed stale;
the market-structure description is more durable.

- Voltus was dispatched on 365 of the last 365 days, a figure she posted
  publicly a month or two before recording, and there are between one and twenty
  dispatches running on its platform at any given moment. (Guernsey)
- The platform spans more than 50 verticals within commercial and industrial
  customers, plus residential. (Guernsey)
- Battery energy storage is among the fastest-growing categories on the platform,
  which she attributes to its falling cost curve. (Guernsey)
- Federal Energy Regulatory Commission orders 719 and 745 started to value
  demand-side reduction the way a generation resource is valued. (Guernsey)
- EnerNOC went public in 2007 and was later acquired by Enel, becoming Enel X.
  (Kann)
- PJM capacity prices spiked again in the most recent auction while load-side
  participation was roughly flat year over year. This is Kann's premise, not
  Guernsey's; she says more total megawatts showed up but were counted
  differently under new accreditation rules, that Voltus itself grew year over
  year, and that she cannot speak for other aggregators. (Kann, qualified by
  Guernsey)
- Somewhere in the range of 10% to 20% of capacity is built for less than 1% of
  the time. She offers this loosely, as a recollection of charts from her EnerNOC
  years rather than a current figure, and the base is not specified. (Guernsey)
- New gas turbines are back-ordered into roughly 2030. She stumbles over the year
  mid-sentence and waves it off, so treat it as an approximation. (Guernsey)
- The bring-your-own-capacity product is priced by reference to whatever the
  alternative would cost, with the intent of undercutting it; it was launched the
  day of recording. (Voltus company claim, via Guernsey)

## Where it's contested

- **The host's premise about flat demand response growth gets qualified rather
  than accepted.** Kann asked what the rate limiter is, given that PJM's
  load-side participation looked flat. Guernsey's answer is that accreditation
  changes altered how megawatts were counted, that capacity can also be procured
  through incremental auctions and bilateral arrangements rather than the forward
  auction alone, and that one auction is a poor signal to over-rotate on. She is
  careful not to claim this for the industry, saying only that her own company
  grew. She also visibly avoids the word "withholding" when describing why
  bidders might wait for a later auction.
- **She refuses to name a single binding constraint.** Asked what stops the
  market from growing tenfold, the answer is all of the above: price levels,
  deployment time, market rules, and data access. The most concrete ask is
  regulatory, getting at smart meter data that utilities already collect and
  ratepayers already funded, and she frames it as unresolved.
- **The new product has no track record.** Bring-your-own-capacity launched the
  day this was recorded. The claims that it is faster, more affordable, cleaner
  and better for ratepayers are the company's design intent and its pricing
  policy rather than measured results, and no completed transaction is described.
  Attribute them to Voltus. Guernsey herself says the concept is more
  complicated to talk about, which she names as the big challenge with it.
- **The revenue answer is explicitly "it depends."** The smoothing of value
  across the year is offered as a general trend and a general observation, not a
  rule, and she is clear that heat waves and polar vortex events still produce
  concentrated earnings. She has also stopped forecasting capacity auction
  prices altogether, on the grounds that it is not a game worth playing.
- **The closing argument is normative and she says so.** Preferring to use
  existing underused capacity over building more generation is framed from a
  macro market design and societal point of view, and she grants the premise it
  is arguing against, that you might simply build the plants, before rejecting
  it. That is a position, not a finding.
