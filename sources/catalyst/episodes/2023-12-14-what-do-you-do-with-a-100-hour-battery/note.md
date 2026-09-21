---
episode: "What do you do with a 100-hour battery?"
published: "2023-12-14"
guest: "Mateo Jaramillo, co-founder and CEO, Form Energy"
threads: [long-duration-storage, batteries, renewables, grid-operations, market-design]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2023-12, when Form had announced projects but nothing built at scale; the framework for thinking about duration holds up, but the cost target, the project status and the load-growth expectations are nearly three years old."
disclosure: "EIP portfolio company. Kann discloses on air that EIP is an investor in Form Energy and that Jaramillo is a friend. Routine for this show; noted because the $20 per kilowatt-hour figure is a company target for a product not yet built at scale rather than an achieved cost."
---

## The question

What do you actually do with a 100-hour battery on the grid, and is there a use
for one now rather than only in a far more renewable future?

## The answer

Yes, on Jaramillo's account, because the value of duration is not a smooth curve.
It is clear out to roughly 10 or 12 hours, thins out markedly above that, and
reappears somewhere around 75 to 100 hours, where a battery starts doing what
mid-merit gas plants do and can carry a system through the three-to-five-day
weather events that set reliability. But the whole case is conditional on price:
he names 100 hours at $20 per kilowatt-hour as the combination the system will
pay for, and that was a target Form had not yet met at scale.

## The argument

Kann opens by complaining that "long duration energy storage" has been stretched
from six hours to seasons until it means nothing, and the conversation replaces
the category with a function. Lithium-ion, Jaramillo says, is essentially a power
battery doing intraday work:
it started at fifteen-minute frequency response in PJM and now sits at four
hours, moving toward six, providing peaking and ramping. That maps onto gas
peakers, which the industry defines as plants running less than 5% of the hours
in a year, roughly 400 hours, spread out rather than consecutive. There is no
technical reason a lithium-ion battery cannot discharge for a hundred hours; the
limit is economic, and it turns on rated power. Every additional hour of
discharge at rated power is a cost adder, roughly $100 per kilowatt-hour for
lithium-ion, and because the industry compares resources on dollars per
kilowatt, a hundred hours would mean paying about 25 times as much per kilowatt.
That does not clear. He also does not expect anyone to unseat lithium-ion in
that intraday band, because grid storage rides on the manufacturing scale of the
automotive market and no other chemistry gets the same tailwind; he calls himself
a technology optimist and calls displacement a tall task anyway.

The more interesting claim is that value does not rise smoothly with duration.
Run a capacity expansion model and ask what a storage asset displaces, then walk
up the histogram of gas plant capacity factors from peakers through mid-merit
plants at 20, 30, 50, 70%. Form's modeling, led on the analytics side by
co-founder Marco Ferrara, found clear value up to about 10 or 12 hours, then
markedly less value until you get back up to around 75 and approaching 100
hours, because that is where a battery can start replacing what those mid-merit
plants do. Jaramillo is careful about the middle: he explicitly declines to put
a number on how much value sits between 10 and 40 hours, allows there may be a
day-to-day shifting case, and says it still needs to be worked out. The reason
the answer lands near four days is not total hours but consecutive ones. The
signature of severe weather is three to five days, whether that is a Pacific
Northwest heat dome, an Upper Midwest polar vortex, a nor'easter or Winter Storm
Uri, and a grid increasingly driven by weather has to be able to ride through
that.

None of which matters without a price, and Jaramillo is insistent on this: the
assumption that multi-day duration is irrelevant is really an assumption about
what it costs. Form's own modeling, which he says third parties have confirmed,
put the threshold at 100 hours and $20 per kilowatt-hour. Kann does the
comparison out loud, noting lithium-ion cells around $100 per kilowatt-hour and
fully installed grid systems at two or three times that, which makes the target
roughly an order of magnitude below lithium-ion on an energy basis. The
justification for thinking it reachable is what Jaramillo calls entitlement.
Iron-air chemistry is old and was never commercialized, but its active materials
cost less than a dollar per kilowatt-hour dug out of the ground, against $30 to
$35 for lithium-ion's unprocessed active materials. Starting cheap is necessary
but not sufficient, so the engineering constraint is self-imposed: no expensive
synthesis and no high-precision manufacturing, because the whole point is to end
cheap as well as start cheap.

What utilities buy it for today is not the renewables balancing story. Georgia
Power is dealing with load growth fast enough that it reopened its integrated
resource plan two years early; multi-day storage lets it add cheap intermittent
generation to meet that growth without giving up reliability, and because
Georgia Power runs internal markets rather than bidding into a wholesale market,
it can put a precise internal value on reliability in a way wholesale markets do
not. Jaramillo adds a land argument, that the same benefit can be had from about
half as many acres of solar, while noting he does not want to be a land doomer
because power projects are a small share of industrial land use. At Xcel, which
is wind-heavy and participates in MISO, the same asset also works as a physical
hedge against price spikes, something otherwise available only financially or
through thermal plants. A third application, buffering constrained transmission
lines and letting curtailed wind owners move energy across days to escape the
price spread between where they generate and where they get paid, had been
shelved early and come back quickly. As for how the battery behaves, Kann offers
the simple picture of charging up, waiting for a scarcity event and discharging
for three days, and Jaramillo rejects it: that arbitrage is lithium-ion's game in
ERCOT. The justification is capacity and reliability, and then the asset gets
used for everything else, running flat out for three or four days a few times a
year but otherwise ratcheting its state of charge up across a renewable-heavy
spring and down across a summer deficit.

## What you need to know first

- **Rated power and duration.** A battery is rated for both power and energy, and
  duration only means something at rated power. You can discharge a four-hour
  battery for a hundred hours; you are just getting very little power for a very
  high price.
- **Dollars per kilowatt versus dollars per kilowatt-hour.** Battery people talk
  in kilowatt-hours, but the power industry compares resources in dollars per
  kilowatt, so duration gets priced as how many hours you get for a given cost
  per kilowatt.
- **Peaker and mid-merit.** A peaker is a gas plant running under 5% of the hours
  in a year; mid-merit plants run 20% to 70%. Lithium-ion already displaces the
  first, and the argument for 100 hours is that it reaches the second.
- **Capacity or reliability as a product.** Being available when the system needs
  you, as distinct from selling energy. Jaramillo's point is that most wholesale
  markets do not price it precisely, which is part of why a reliability asset is
  hard to finance on market revenue.

## Details worth keeping

- The Georgia Power project is slated at about 15 megawatts but 1,500
  megawatt-hours, and was not yet built. Kann notes that on energy capacity it
  would be among the three or four largest batteries in the world; Jaramillo
  agrees, with the caveat that something bigger might show up.
- Xcel made its decarbonization commitment explicitly without knowing how it
  would get there, which Jaramillo describes as an early validation for Form.
- 100 hours is not treated as sacred. Jaramillo says nobody at Form believes the
  round number is optimal, that Ireland might want 150 or 175 hours given
  offshore wind and island congestion while Arizona might want 75 or 80, and that
  the product exists to address the bulk of the market rather than every case.
- The competitive set is not lithium-ion. Substitutes for a clean
  capacity-and-reliability resource are carbon capture bolted onto flue gas,
  hydrogen, or a great deal more transmission, each of which he flags for open
  questions on cost, scalability or timeline.

## Claims worth citing

All figures as stated on 2023-12-14 and now nearly three years old. Battery
costs and project status move fast; treat these as a snapshot.

- Lithium-ion on the grid is predominantly four hours, moving to six in some
  applications, having started at fifteen-minute fast frequency response in PJM.
  (Jaramillo)
- Peakers are defined as gas plants running less than 5% of annual hours, roughly
  400 hours, non-consecutive. (Jaramillo)
- Every incremental hour of lithium-ion discharge at rated power adds roughly
  $100 per kilowatt-hour, so 100 hours would cost about 25 times as much per
  kilowatt as four hours. (Jaramillo)
- Fully installed lithium-ion grid systems cost two to three times the cell cost.
  (Kann)
- Form's threshold is 100 hours at $20 per kilowatt-hour, from its own modeling
  and, he says, confirmed by third-party modeling. This is a target for a product
  not yet built at scale. (Jaramillo, about his own company)
- Iron-air active materials cost less than $1 per kilowatt-hour unprocessed,
  against $30 to $35 for lithium-ion's. (Jaramillo)
- Storage value is clear to about 10 or 12 hours, markedly less until roughly 75
  to 100 hours. He declines to quantify the gap in between. (Form modeling, cited
  by Jaramillo)
- Mid-merit gas plants run at capacity factors from about 20% to 70%. (Jaramillo)
- Weather events that stress a grid typically last three to five days.
  (Jaramillo)
- Cost-effective multi-day storage can deliver the same benefit from about half
  as many solar acres. Stated as a general finding, with no specific system or
  study named. (Jaramillo)
- Xcel targets 80% decarbonized by 2030 and 100% by 2045, the latter hedged as "I
  think they said." (Jaramillo, describing Xcel)
- The US grid will need to be roughly twice its current size by about 2045 to
  2050, before accounting for large language model compute, which he says is
  driving demand bonkers. (Jaramillo)
- ERCOT scarcity pricing of $9,000 per megawatt-hour is used as the illustration
  of the arbitrage case. (Kann)

## Where it's contested

- **The disclosure.** EIP is an investor in Form and Kann says so on air, as is
  routine here. The narrow consequence is that the $20 per kilowatt-hour figure
  and the entitlement argument describe a product Form intended to build, not one
  it had delivered. Kann does press on how the target is reachable and gets a
  substantive answer.
- **The gap in the value curve is unresolved and he says so.** Jaramillo will not
  put a number on the value of durations between roughly 10 and 40 hours, calls
  it murkier, and says it still needs to be worked out. That is the weakest link
  in the argument for skipping straight to 100 hours, and he does not paper over
  it.
- **The host pre-answers the central objection.** Kann raises the "we don't need
  it yet" argument and immediately says he does not think it is true, before
  Jaramillo responds. The evidence offered against it is Form's own customer
  commitments and its own modeling rather than independent analysis, and the
  projects discussed were announced rather than operating.
- **The land claim is general.** Half the acreage for the same benefit is stated
  as a repeated modeling result without a named system or study, and Jaramillo
  himself immediately qualifies the land-scarcity framing.
- **100 hours is explicitly not presented as the right answer everywhere.** He
  volunteers that the round number suits human sensibilities rather than physics.
- **Displacing lithium-ion intraday is treated as near-impossible**, by a founder
  who describes himself as a technology optimist; he does not claim Form competes
  there.
- **The framing risk is worth naming.** Jaramillo does not argue that multi-day
  storage substitutes for building generation: he says the industry needs as much
  solar, nuclear, wind and geothermal as it can build, and that this asset makes
  whatever goals a utility already has easier to hit. An enabler, not a
  replacement.
- **Base load is waved off**, as a concept "sort of going away for lots of
  reasons that we probably don't want to go into."
