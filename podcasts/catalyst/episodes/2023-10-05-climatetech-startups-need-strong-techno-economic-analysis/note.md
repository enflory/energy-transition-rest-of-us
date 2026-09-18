---
episode: "Climatetech startups need strong techno-economic analysis"
published: "2023-10-05"
guest: "Dr. Greg Thiel, director of technology, and Dr. Melissa Ball, associate director of technology, Energy Impact Partners"
threads: [techno-economic-analysis, venture-and-finance, cost-curves, energy-storage, hydrogen]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2023-10. The method is durable, but the cost thresholds quoted for batteries, hydrogen and CO2 are late-2023 figures and should be re-priced before anyone uses them as targets."
---

## The question

What is a techno-economic analysis actually for at an early-stage hard technology
company, and what do people most often get wrong when they build one?

## The answer

It is a prioritization tool, not a document for the data room. Kann's closing
summary, which both guests endorse, is that a good one answers three questions:
how hard you have to squint to believe the plan, which variables swing success or
failure, and what you have to prove next. Nearly every failure they describe
comes from drawing the analysis too narrowly: the wrong inputs, the wrong system
boundary, the wrong benchmark or the wrong metric. One runs the other way, since
precision beyond what the company's stage can support is wasted time.

## The argument

Start with what the model is for, because that decides how to build it. Thiel's
framing is that a techno-economic analysis earns its keep from the moment an idea
is still being mulled over, when it answers a crude question: could this compete
at all? Refined, it becomes a roadmap. If the thing is not economic today, the
model says what it would have to achieve to become economic, and which design
decisions move affordability and which do not. For a company with a handful of
engineers, that ranking is the value. The practical consequence: run the analysis
backwards from the competitive threshold rather than forwards from what is
achievable now. Thiel does this with synthetic fuels: priced at today's clean
hydrogen and captured CO2 costs the answer is absurd, so instead ask what the
inputs must cost for the fuel to compete unsubsidized. Pushed for numbers, he
offers hydrogen around a dollar per kilogram and CO2 at $100 to $200 per ton,
with the CO2 necessarily atmospheric or biogenic or the fuel is not carbon
neutral.

The first discipline is inputs, and its logic is that optimism has a budget. A
novel technology already requires believing something unbuilt can be built, so
every optimistic input compounds a bet you were already making; Kann's rule is to
isolate the magical thinking to the technology leap itself, the part within your
control. Ball's standing example is the company whose process runs on electricity
and assumes very cheap power and full-time operation at once. Those are close to
incompatible, because cheap green power means tethering yourself to a resource
that runs perhaps 30% of the time for good solar or 50% for good wind, and the
levelized cost of generating electricity is not the delivered price a customer
pays. Her second is chemical: organic molecules look cheap to organic chemists,
but yield and purification sit inside the boundary, and the practical floor is
near ethylene, around a dollar per kilogram. Thiel's is free waste heat, flagged
against his own instincts as a thermal engineer: it is abundant and genuinely
tempting, but wrapping a large heat exchanger around a long run of
moderate-temperature flue gas can cost more than the recovered energy is worth. Ball's fix is not to ban the optimistic
number but to ask what would have to be true for it, then range it. If you are
only in the money in the rosiest case, that is the finding.

The second discipline is where you draw the box, because cost lives in the system
rather than the component. Total installed cost of a facility can be two, three,
four times or more the core equipment, so being 50% better than state of the art
on a component that is 20% of system cost barely moves the delivered number.
Ball's case is modular ammonia, where the clever low-pressure, low-temperature
reactor is real but the hydrogen and nitrogen supplies upstream of it dominate
cost and scale down badly; draw the boundary around the reactor and you miss the
business. Kann adds that this worsens as a market matures, since the widely
quoted sub-$100 per kilowatt-hour battery cell price is not a system price, and
in utility-scale solar the module is a minority of project cost, the rest being
labor, interconnection and permitting. It cuts the other way too: a couple of
points of efficiency in an already 90%-efficient electric vehicle drivetrain
component matter a lot, because every wasted kilowatt-hour has to be carried in
the most expensive part of the vehicle. Components are not unimportant; only the
system tells you which ones are. The same widening applies to the benchmark,
which has to be the right object and a moving target. Ball's version is comparing
your levelized production cost against a market selling price, which is apples to
oranges: the price includes delivery and a margin, and delivery is not always
small, since her team found ammonia distribution reaching twice production cost.
Kann's addition is that in a commodity market the number to beat is not the
incumbent's current price but its floor, its ongoing operating cost, because an
incumbent facing a cheaper entrant will cut toward that floor and undercut you
anyway. And the floor moves: the late-2000s thin-film solar companies priced
themselves against crystalline silicon as it then was, and silicon fell faster
and further than anyone expected, so they arrived out of the money. Thiel applies
the same test to new storage chemistries, where the question is not whether you
beat lithium iron phosphate today but whether you beat it in 2035.

The last discipline is choosing the metric, and Thiel scopes that claim
carefully: he is not arguing against research on efficiency or catalysis, only
that from a venture perspective the improvement has to move the economics. If the
model says input costs dominate, a better single-pass CO2-to-methanol catalyst is
good science and a hard investment story, because hydrogen and CO2 are where the
money goes. Kann extends it past cost to what the customer buys: a weeding robot
optimized for capital cost may lose to one that covers the field faster, and 99%
mineral recovery is worthless if the leaching kinetics are too slow for the
mine's downstream capacity. Which is why, Thiel argues, the work needs commercial
and technical people together, since the economics half of techno-economics is a
claim about customers. Then comes the counterweight, Kann's own pet peeve, which
cuts against everything above: seed-stage models arrive with four decimal places
on numbers nobody can know. Ball's worry is that counting pump power and valves
is precisely how you miss the one driver that decides the company. Thiel's is
that early designs are still in flux, so detailed work on one subsystem gets
thrown out when something learned elsewhere changes the design. His sequencing
rule resolves the tension: error bars and sensitivities early, detailed rabbit
holes only once the high-level design is fixed. The effort belongs in the width
of the analysis rather than its depth.

## What you need to know first

- **Techno-economic analysis (TEA).** A model holding an engineering process
  design and a cost-and-market picture in the same place, so you can ask whether
  a technology could compete and what would have to change for it to.
- **Capacity factor.** Actual output divided by what the same equipment would
  produce running flat out all year. It is why cheap renewable power and
  round-the-clock operation are hard to assume together.
- **Levelized cost.** Lifetime cost per unit of output, capital included. A cost,
  not a price: it excludes delivery and profit, which is what makes
  cost-versus-price comparisons misleading.
- **System boundary and balance of system.** Where you draw the box around what
  you are costing. Balance of system is everything surrounding the core
  component, and in mature markets it is most of the money.

## Details worth keeping

- Kann runs EIP's $485 million frontier fund, investing in hard technology before
  it is proven. Reviewing a company's TEA is one of the first diligence jobs; the
  team has seen hundreds, and Kann says they have driven conviction, or cost it,
  many times.
- Ball makes the point that TEA is not universal vocabulary. Founders who trained
  as engineers usually know it; chemists and physicists often have not
  encountered it. EIP makes job candidates build one as a hiring case study.
- Some founders pay consultants for a TEA; Ball and Thiel rebuild it internally
  anyway, to learn the real drivers for themselves.
- A recurring benchmarking error Thiel sees: companies with novel hydrogen
  transport media compare themselves against steel tube trailers, when composite
  high-strength lightweight tubes already carry far more hydrogen per load. Beat
  the old benchmark and you can flatter yourself into a false sense of advantage.
- First Solar was the exception among the late-2000s thin-film companies.

## Claims worth citing

All figures as stated on 2023-10-05, attributed to the speaker rather than
verified. Several are cost *targets* rather than measurements, and battery,
hydrogen and CO2 costs move fast.

- Grid storage competitiveness in the 2030s needs roughly $100 to $150 per
  kilowatt-hour total installed system cost, against $200 to $300 per
  kilowatt-hour installed today, so a half to a third of current cost. Given as
  the numbers EIP has landed on in its own work. (Thiel)
- For synthetic fuels to approach competitiveness without subsidies: hydrogen on
  the order of $1 per kilogram, CO2 at $100 to $200 per ton, and the CO2
  atmospheric or biogenic. Offered only when pressed for a number, and explicitly
  varying by timeframe and geography. (Thiel)
- Capacity factors of roughly 30% for a really good solar resource and 50% for a
  really good wind resource; two-cent electricity at 100% capacity factor is not
  something to build economics on. (Ball, agreed by Kann)
- Ethylene at roughly $1 per kilogram as a practical floor for ubiquitous organic
  molecules, and the bar a novel organic active species has to approach to beat
  lithium iron phosphate or vanadium flow batteries. (Ball)
- Total installed cost of a facility can be two, three, four times or more the
  cost of the core componentry. (Thiel)
- Ammonia distribution and transport costs can reach roughly 2x production cost
  depending on US location. (Ball)
- Battery cell prices recently reported below $100 per kilowatt-hour are cell
  prices, not delivered system costs, and in utility-scale solar the module is a
  minority share of total project cost. (Kann)
- Assuming delivered electricity gets cheaper is a bet, not an extrapolation:
  Kann says that is not the historical trend. (Kann)

## Where it's contested

- **How much analysis is the right amount is genuinely unresolved.** Kann's final
  pet peeve, false precision, runs against everything else in the episode and he
  says so. He asks both guests where the line sits between useful work and
  modeling theater, and neither draws a crisp one. Ball answers in terms of the
  company's stage, Thiel with sequencing. The tension is acknowledged, not
  settled.
- **Thiel's objection to performance metrics is scoped to venture, not to
  science.** He twice declines to knock work on efficiency, conversion or power
  density, and calls them good goals that can move the needle. His claim is only
  that they may not justify an investment if the model shows other costs
  dominating. Efficiency likewise both does and does not matter: he argues a
  relentless efficiency focus often fails to move the economics, then gives the
  drivetrain example where a couple of points move it a lot. The model is what
  tells you which case you are in.
- **The synthetic fuel input numbers are a hedged answer.** Thiel calls the
  question hard and says it varies by timeframe and geography before giving
  figures under pressure from Kann.
- **Thiel puts himself inside the critique**, calling component-versus-system
  thinking a common pitfall rather than a pet peeve and saying he has probably
  been guilty of it himself.
- **This is one investor's diligence preference, not a survey.** All three
  speakers work at the same firm, describing what they want to see in a model
  they are evaluating. Stated openly, and it means the examples come from deals
  they looked at rather than any representative sample.
