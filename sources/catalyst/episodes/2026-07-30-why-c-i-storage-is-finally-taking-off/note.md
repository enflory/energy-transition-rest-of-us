---
episode: "Why C&I storage is finally taking off"
published: "2026-07-30"
guest: "Tim Hade, senior vice president, Voltus; previously co-founder and CEO, Brightfield Infrastructure"
threads: [energy-storage, batteries, ders, data-center-power, market-design]
source_transcript: "transcript.md"
note_version: 1
disclosure: "Energy Impact Partners co-led the seed round in Brightfield Infrastructure, the guest's company, which Voltus acquired shortly afterward. Kann discloses this on air and calls himself an erstwhile investor. Routine for this show; noted because the cost reductions the guest reports are measured on his own company's projects."
---

## The question

Commercial and industrial storage, meaning batteries installed at a business's
own site, has never gone anywhere. Is that actually changing, and why would this
time be different?

## The answer

Not in the deployment numbers, not yet. By Hade's own figures, commercial and
industrial, or C&I, accounts for essentially none of the 40 gigawatts of storage
the US grid added in five years. What has changed, mostly in the last 18 months,
are the inputs: a fourth revenue stream in capacity that barely existed before,
a federal storage tax credit that survived when others did not, hardware down 30
to 40%, and AI cutting the transaction-cost slice of his own projects by three
quarters or more. The claim in the title is a forecast built on those inputs, and
Hade narrows it under questioning to fastest growth *rate* off a near-zero base,
not fastest growth in megawatts.

## The argument

Kann sets the episode up with a cautionary history. In the mid-2000s the US solar
market was mostly commercial and industrial, and the first big acquisition in the
space was SunPower buying PowerLight, a C&I developer, for $330 million in 2007.
Then residential solar scaled, utility-scale solar scaled, and C&I simply did
not. Storage has so far repeated the pattern exactly: under 2 gigawatts on the US
grid going into 2020, about 40 gigawatts by 2025, of which roughly 90% is utility
scale and 10% residential, which as Hade points out leaves basically nothing for
C&I. His diagnosis is that the residential share is not purely an economic
decision, since much of it is bought for resilience, whereas C&I customers buy on
economics alone and the economics were not good enough. The pioneers of the
2015-2020 era, Stem, Green Charge, AMS, went after demand charge management and
sometimes came close to penciling, but the value proposition was an edge case
that mostly needed state subsidy to work. His phrase for the average customer is
that the juice was not worth the squeeze: you could build an NPV-positive
project, and the bill savings still were not large enough to justify the time a
business would have to spend on something that was never going to save the
business.

On the revenue side, Hade counts four streams, and Kann inserts an important
qualifier before he starts: rising retail rates are inherently good for
behind-the-meter generation but not inherently good for storage, because what
matters is how the rates are *structured*. Time-of-use arbitrage now exists in
many utility territories where it did not a decade ago. Demand charges, the part
of a commercial bill set by the single highest power draw rather than by total
energy, have been rising faster than the energy component, which makes shaving
them worth more. Ancillary services, once the whole market, are now a minor
share. The fourth, capacity, is the one Hade says has changed most in 18 months:
PJM capacity prices are up elevenfold in three years, and the auction has hit its
price cap without clearing for several rounds running, which he describes flatly
as a market not functioning properly. That dysfunction is precisely what creates
the opening, because hyperscalers can contract bilaterally for capacity outside
the capped auction and pay whatever they think an incremental megawatt is worth.
Kann then presses the counterargument, that storage erodes its own revenue: in
ERCOT the arbitrage spread has been flat to declining because so many batteries
were built, and on a recent record net-load day 10 gigawatts of batteries
dispatched and prices never cleared $250 a megawatt-hour. Hade concedes the point
and generalizes it into the episode's sharpest unresolved problem. Storage has
demonstrably helped every grid where it has been deployed at scale, and in the
markets where it helped most it has not necessarily been a good investment. He
says market design has to fix that over the next five to ten years and that we
are not there yet.

The cost side is where his case is strongest and also where measured results and
forecasts have to be separated carefully. A typical C&I battery today runs about
$800 per kilowatt-hour after the tax credit: $300 to $400 of hardware, about $100
of software, about $200 of installation and about $200 of transaction costs,
meaning interconnection, permitting, financing, customer acquisition and the
people who do all of it. The tax credit itself is the first piece of good news,
30% at base, plus 10% for domestic content and another 10% in an energy
community, so up to 50%, and it came through the 2025 budget law unchanged when
the solar and wind credits did not. Hardware is the second, down about 40% at the
pack level and 30% at the system level in 18 months. But soft costs are the
historical killer, because a C&I project carries roughly utility-scale complexity
amortized over a far smaller asset, and this is where Hade's specific bet lives:
transaction costs are repetitive workflows, financial modeling, contracts,
interconnection filings, and agents can be trained to do them. Projects his team
runs today cost $25 to $50 per kilowatt-hour in that bucket against $200
historically, and he adds that they are not even good at this yet. He forecasts
about $20 within three years. Installation he is visibly less confident about,
calling it harder to predict and offering a learning-curve argument: today you
pay an electrician both to learn how to install a C&I battery and to install it,
and as volume arrives that halves, to maybe $100 over five years. Put together,
$800 becomes something like $510, which he thinks pushes many more customers past
the threshold where this gets interesting. His heuristic there is worth carrying:
5% off a customer's net electricity spend makes the conversation worth having,
above 10% is a really good project, and rising rates have moved the pitch from
vitamin to painkiller.

The claim that C&I grows fastest does not rest on C&I being good. It rests on
utility-scale being stuck. A new utility-scale battery joins the same
interconnection queue as large loads, and Hade puts the average wait at about six
years in PJM, maybe nine in CAISO and maybe four in ERCOT, so demand for
batteries over the next three to five years has to be met behind the meter, where
interconnection is fast. Kann's objection is the obvious one and Hade does not
answer it: the queue is long precisely because it is full of storage projects,
and those will eventually come online too. The remaining problem is scale.
Hyperscalers think in gigawatts, and a single one-megawatt commercial site is
irrelevant to them, while a thousand of them is a competitive advantage. Bridging
that gap is aggregation into a virtual power plant, which is why Hade's company
ended up inside Voltus, and it is also the part he explicitly says he does not
understand, suggesting his boss come on the show to explain how bring-your-own
capacity actually works. Underneath all of it sits an unresolved hardware gap in
exactly the size range most C&I facilities need, which he can only say he hopes
more manufacturers fill.

## What you need to know first

- **C&I.** Commercial and industrial: a battery or solar system at a business
  site, historically hundreds of kilowatts to a megawatt or two. Bigger than a
  house, far smaller than a power plant, and awkward in both directions.
- **Demand charge.** The portion of a commercial electricity bill set by the
  single highest rate of power draw during the billing period rather than by
  total energy used. A battery can discharge into that peak and cut the charge
  without changing how much electricity the business consumes.
- **Capacity, and bring-your-own capacity.** Capacity is payment for being
  available at peak, separate from payment for energy delivered. Bring-your-own
  capacity is the arrangement where a data center developer must supply capacity
  to the grid to get connected, and can buy it bilaterally rather than through a
  price-capped auction.
- **The investment tax credit.** A federal credit worth a percentage of a
  project's capital cost. The speakers refer to the two laws involved only as the
  IRA and the OBBB and never expand either acronym; what matters here is that the
  storage credit carried over unchanged when the later law passed on 4 July 2025.

## Details worth keeping

- The solar precedent that frames the episode: SunPower's $330 million
  acquisition of PowerLight in 2007 was the first big deal in US solar and
  PowerLight was a C&I developer. Kann notes in passing that PowerLight's
  president, Dan Sugar, is now CEO of NexTracker.
- Where early C&I storage did work, it was subsidy or incident driven. Hade cites
  California's state-level incentives and Southern California Edison's Load
  Control Response program, which came out of the Aliso Canyon gas leak and
  needed a lot of storage on the grid quickly.
- The hardware gap is specific. Residential blocks of roughly 10 kilowatts can be
  stacked to serve a 70 to 100 kilowatt facility, and utility-scale one-megawatt
  blocks serve anything above a megawatt. Between 100 kilowatts and one megawatt,
  where most C&I facilities sit, the product range is thin, though Hade names
  Socomec and Sungrow as good providers there and says those products have seen
  the same cost declines as the rest.
- Customer acquisition cost is really a measure of how hard the thing is to sell.
  Ten years ago Hade had to price the nineteen wasted sales trips into the one
  deal that signed, and he says he was good at it.
- A quieter change he credits the industry with: contracts are simpler and
  clearer, economics are more transparent to the buyer, and project finance for
  these assets has gone from one-off structuring to a standard offering. Since
  the binding constraint for a business is often management time rather than
  money, and since a battery is never going to save a struggling company, that
  reduction in effort matters as much as the savings number.

## Claims worth citing

All figures as stated on 2026-07-30. Battery hardware prices, capacity prices and
interconnection queue times are all fast-moving, and the cost reductions Hade
reports on transaction costs are measured on his own company's projects rather
than industry-wide.

- Less than 2 gigawatts of total storage on the US grid going into 2020; about 40
  gigawatts as of 2025, roughly 90% utility scale and 10% residential, leaving
  effectively nothing for C&I. (Hade)
- PJM capacity prices up 11x in the last 36 months, with the auction hitting its
  price cap and failing to clear needed capacity for several auctions running.
  (Hade)
- Average interconnection wait for a new utility-scale battery: about six years
  in PJM, maybe nine in CAISO, maybe four in ERCOT, in the same queue as large
  loads. (Hade)
- Storage investment tax credit: 30% base, plus a 10% domestic content adder,
  plus a 10% energy community adder, so up to 50%, unchanged from the IRA to the
  OBBB, which passed 4 July 2025. Neither acronym is expanded on air. (Hade, with
  Kann noting it outlasts the solar and wind credits)
- Battery costs down about 40% at the pack level and about 30% at the system
  level over 18 months, which he qualifies as depending on which analysis you
  look at. (Hade)
- Typical C&I project about $800 per kilowatt-hour post-tax-credit: $300 to $400
  hardware, about $100 software, about $200 installation, about $200 transaction.
  Note that he rounds hardware plus software to $400, so the components do not
  add up exactly. (Hade)
- Transaction costs on his own current projects: $25 to $50 per kilowatt-hour
  against $200 historically. (Hade)
- Forecasts: transaction costs to about $20 per kilowatt-hour within three years,
  a roughly 90% reduction credited primarily to AI and agentic tooling;
  installation halved to about $100 over five years; all-in cost to roughly $510.
  He calls the total his best guess and the installation number harder to
  predict, and the components sum slightly above the $510 he quotes. (Hade)
- Customer threshold heuristic: 5% off net electricity spend is worth a
  conversation, above 10% is a really good project. (Hade)
- Customer acquisition hit rate roughly 5% ten years ago, maybe 30% now. (Hade)
- On a record ERCOT net load day, 10 gigawatts of batteries dispatched and prices
  stayed under $250 per megawatt-hour. (Kann)
- Forecasts: C&I becomes the fastest-growing segment of the storage market over
  three to five years, by growth rate rather than by total megawatts; and
  bring-your-own capacity becomes a very quickly growing segment over the next 36
  to 48 months, because hyperscalers in constrained regions like PJM have nowhere
  else to get near-term capacity. (Hade)

## Where it's contested

- **The title's premise is the main thing to hold onto.** Nothing in the episode
  shows C&I storage taking off in deployment; the same speaker who makes the case
  supplies the number showing C&I at essentially zero percent of five years of
  US additions. What is measured is the change in inputs, cost, tax treatment and
  capacity value. What is forecast is the deployment.
- **The growth claim narrows under pressure.** Kann immediately notes that
  fastest growth from a small base is easy, and asks whether he means total
  megawatts. Hade says no, he means the rate. That concession should travel with
  the claim.
- **Market design is unsolved and Hade says so.** Grid operators have benefited
  from storage everywhere it has been deployed at scale, and the people who
  installed it in the markets where it helped most have not necessarily been
  rewarded. His answer is that rules have to change over five to ten years, and
  "I don't think we're there yet."
- **Storage erodes its own arbitrage.** Kann's ERCOT example is a genuine
  counterweight to the revenue case, partially offset in his own telling by
  expected load growth in Texas. The arbitrage value is a function of how many
  batteries are already there, not only of how peaky the market is.
- **The interconnection argument cuts both ways.** Kann points out that queues
  are long precisely because they are stuffed with storage projects that will
  eventually connect, which weakens the claim that only behind-the-meter storage
  can move over the next three to five years. Hade does not rebut it and the
  conversation moves on.
- **Rising rates are not automatically good for batteries.** Kann's qualifier, and
  Hade does not dispute it: rate *structure* determines whether a battery earns
  anything, so the retail price trend alone proves nothing.
- **Installation cost is the weak leg of the cost forecast**, by Hade's own
  admission, and it rests on a learning-curve argument rather than on anything
  demonstrated. The hardware gap between 100 kilowatts and one megawatt is
  similarly unresolved, and he describes the fix as something he hopes happens.
- **He disclaims the aggregation piece entirely.** Asked how bring-your-own
  capacity actually works, Hade says he does not get it and suggests his boss at
  Voltus come on the show to explain, while describing his own job as building as
  many one-megawatt projects as possible.
- **The disclosure, stated plainly.** EIP co-led the seed round in the guest's
  company, which Voltus then acquired, and Kann says he is an erstwhile investor;
  Hade closes with warm remarks about EIP and Kann jokes about a bribe check.
  This is routine for the show. The narrow consequence is that the striking
  transaction-cost reduction is a company-reported figure from a company selling
  the service, not an independently measured industry number.
