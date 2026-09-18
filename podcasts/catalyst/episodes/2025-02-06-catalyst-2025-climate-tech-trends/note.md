---
episode: "Catalyst: 2025 Climate Tech Trends"
published: "2025-02-06"
guest: "Nat Bullard, co-founder, Halcyon; former chief content officer, BloombergNEF"
threads: [load-growth, ai-compute, solar, energy-storage, china]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded in the last week of January 2025, days after DeepSeek's release moved markets, so the deployment figures, load forecasts and the unresolved AI-efficiency question are all snapshots of a fast-moving moment."
---

## The question

Entering 2025, what do the underlying data actually show about where energy and
climate stand, and does a sudden jump in AI model efficiency break the
load-growth story?

## The answer

Almost every trend Bullard walks through is a divergence that markets alone are
not resolving: solar and storage compounding while US wind flattens, enormous
volumes of clean power thrown away for lack of storage and transmission, load
growth returning to a rate the system last saw in the early 2000s, and Chinese
vehicle exports going vertical. On the AI question neither speaker picks a side.
A tenfold efficiency gain either means far less power is needed or, by the Jevons
logic, that cheap compute expands until the energy picture is unchanged; Bullard
expects the answer somewhere in between. The more consequential question for the
grid, they argue, is not how much compute demand there is but what size the
individual data center ends up being.

## The argument

Start with the split between solar and wind, because the same cause runs through
most of what follows. Globally 2024 was a record year for both, 599 gigawatts of
solar and more than 130 gigawatts of wind, which Bullard notes would have looked
like a fantasy to an analyst in 2008 who assumed it would take a $200 per ton
global carbon price to get there. In the United States the two have come apart.
Wind investment is well off a peak he places around late 2019 to mid-2020, solar
is climbing past $40 billion in trailing twelve-month investment, and storage now
attracts more US investment than wind does. His explanation is not primarily
political: solar is simply faster and simpler to develop absent transmission
reform, and storage is complementary to a high-solar grid. Politics makes it
worse rather than causing it, and Kann's framing is that it was already a tale of
two markets before the new administration, which is unfavorable to renewables
generally and has a long-standing particular animus toward wind. The tell is
ERCOT in Texas, the least constrained large market in the country, where the same
shape appears without the policy overlay: cumulative solar likely passing wind in
2025, and batteries growing faster still.

What the grid does with all that solar is the second thread, and it is a
market-design failure rather than a technical one. California curtails more than
750 gigawatt-hours of solar in a typical spring, when it is sunny, cool and
demand is low, and as of 2024 the state's minimum net load across the entire
spring was negative in aggregate, meaning intermittent generation exceeded total
demand. Europe's version is priced rather than dumped: instances of negative
hourly power prices rose from 500 to 550 in 2022 to more than 9,000 last year,
summed across member states and grids, which is more hours than exist in a year.
Bullard's point is not that this is unfixable but that nothing is currently
rewarded for fixing it. We cannot see the counterfactual, since we do not know
what California would look like without the roughly 10 gigawatts of storage it
has already built, and the four-hour duration standard that shapes what gets
built there is an artifact of written regulation rather than of physics, so the
market has no incentive even to find out what longer-duration storage or flexible
load would do. Kann's version is blunter: hundreds of gigawatt-hours of clean
electricity wasted every year and growing, an inefficiency staring you in the
face, fixable by policy, by a storage business model or by a business model for
intermittent load. Transmission is the same diagnosis in harsher form. The US
built 3,200 miles of high-voltage long-distance transmission in 2013 and 125
miles last year, and Bullard argues the shortfall is not for lack of funding or
of demand to use it but because building is difficult or impossible, which makes
it a planning and permitting question rather than a market one.

Load growth is where the episode does its most useful reframing, and it cuts
against the panic rather than feeding it. Twenty years ago the official
reliability forecasts assumed ten-year compound growth of 1.5% to 2%. That
eroded steadily to roughly half a percent by 2020 and has now unwound back above
1%. Kann's point is that if you round up to about 1.5% you get triple the 2020
expectation, which explains the whiplash, but still less than the roughly 2% the
system was running at in the early 2000s. This is not historic load growth; it is
load growth the country did historically, arriving at a sector that had spent a
decade getting used to stagnation and, in Bullard's phrase, doing a very good job
of making itself hard to build into. Two qualifications travel with it. Bullard
notes the chart is a chart of expectations, and that in the period when half a
percent was expected the realized growth in total electricity demand was zero.
And both allow that today's forecast may be too low rather than too high; Kann
floats 3%.

Then DeepSeek, recorded the Monday its release knocked the market down and
released that Thursday. Bullard's angle is training hours as a direct proxy for
electricity, since a training hour is GPU time and GPU time is power. Meta's
Llama 3.1 used just under 31 million training hours at 405 billion parameters;
DeepSeek reached comparable results with 671 billion parameters and fewer than
2.8 million training hours, built by a Chinese hedge fund's $5.5 million rather
than billions in venture capital and under constrained access to chips. Kann puts
it at roughly ten times more efficient on training and about thirty times on
inference, flagging the second as his own understanding, and lays out the two
readings explicitly: either the gigawatts are not needed, which is what the stock
market priced that day, or the Jevons paradox applies and cheap compute gets
consumed in far greater volume, leaving energy demand flat or higher. Bullard
observes that Microsoft's chief executive invoked Jevons by name while
reaffirming $80 billion of capital expenditure, and Kann notes that he has an
interest in that reading. Bullard expects the truth in between and says the
harder questions are who captures the value and whether lightweight models get
hosted in third-party facilities or on a company's own. The thread Kann pulls out
is granularity: the entire reason for gigawatt-scale campuses is that bigger
training runs wanted to sit on one site, and 20 megawatts is an interconnectable
load while a gigawatt is not, so if this efficiency buys the same performance at
20 megawatts it changes where compute can be sited and how it can be powered.
That the answer is undetermined is the honest conclusion, and it is reinforced by
the cost structure: energy is a small line item in training, so the buyer is one
that cares about whether power is available and when, not what it costs.

## What you need to know first

- **Net load and curtailment.** Net load is total electricity demand minus
  intermittent generation. When it goes negative there is more solar and wind
  than the system can use, and the surplus is curtailed, meaning generation is
  deliberately turned down and the energy is lost.
- **Negative prices.** When supply exceeds demand in a market that must balance
  instantly, the clearing price can go below zero and generators pay to keep
  producing. Counting them by the hour matters because a year has 8,760 hours,
  which is why a figure above 9,000 is a sum across many separate markets rather
  than a share of one year.
- **Parameters and training hours.** Parameters are a rough measure of a model's
  size; training hours are the GPU time spent building it. Training hours are the
  useful number for energy, because GPU time is electricity consumed.
- **Jevons paradox.** The observation that making the use of a resource more
  efficient can increase total consumption of it, because the cheaper it becomes
  the more of it people do.

## Details worth keeping

- Grid-connected batteries hold up in extreme weather. Data from Modo, with good
  visibility into Texas, clusters availability in the mid to high 90% range both
  below 32 degrees Fahrenheit and above 105, with the lowest point at extreme heat
  still above 75%. Bullard's caveat is that above 105 degrees everything on the
  grid starts degrading, including lines sagging, so batteries are not uniquely
  exposed.
- Plug-in hybrids need a mental reset, in Bullard's view. The American image is a
  Prius with a plug; the Chinese product has 200-plus kilometers of battery range
  plus a small efficient engine, marketed in Southeast Asia as an extended-range
  electric vehicle, capable of 800 to 1,000 kilometers without refueling. He sees
  them advertised in Thailand and Brazil, with BYD preparing an extended-range
  pickup for Australia. The appeal is not range anxiety but range reality where
  charging infrastructure is thin.
- Bullard, based in Southeast Asia, uses Singapore as his live example of how fast
  Chinese brands move: BYD went from 0.2% market share in December 2021 to 14.4%
  in December 2024, second only to Toyota, in a market of roughly 40,000 new
  vehicles a year with weak charging infrastructure. He names two more Chinese
  brands he sees routinely in his own garage that Americans have not heard of;
  the transcript garbles both names.
- Data center construction spending passed hospitals last year, $31 billion
  against $27 billion, and Bullard stresses that this is structures only, not
  GPUs or mission-critical equipment, which is where the real money goes. The
  series only begins in 2014 and has smoothed from a jagged low line into
  something that looks like the start of exponential growth.
- Servers have been migrating from on-premises closets to hyperscale and
  colocation facilities for 25 years, which changes what has to be built. Bullard
  wonders aloud whether efficiency gains could partially reverse that, sending
  some workloads back to a chilled closet rather than an industrial park.
- Rappahannock Electric Cooperative's filing in Virginia is the episode's sharpest
  illustration of the scale mismatch: a cooperative with a 1.2 gigawatt peak load
  receiving interconnection requests for single assets larger than its whole peak,
  in some cases four times larger. Bullard connects it to the duty to serve, a
  framing he attributes to Severin Borenstein at Berkeley (the transcript renders
  the name "Severn Bernstein"), and to the reverse risk of building for five
  gigawatts that never arrive, citing the VC Summer nuclear project in South
  Carolina as roughly $7 billion of poured concrete and nothing more. He coins
  "deep sunk" for the failure mode.
- Kann frames the closing segment around an idea he credits to Brian Janous,
  whose surname the transcript garbles: the bits are worth far more than the
  watts consumed to produce them, which is where the near-limitless willingness
  to pay in the data center world comes from.

## Claims worth citing

All figures as stated on 2025-02-06, recorded the Monday of that week. Deployment
totals, model efficiency figures and load forecasts in this episode were moving
weekly at the time.

- 599 gigawatts of solar and more than 130 gigawatts of wind installed globally in
  2024, a record year for both. (Bullard)
- US solar investment above $40 billion on a trailing twelve-month basis, with
  wind well below its peak and storage now drawing more investment than wind.
  (Rhodium Group data, cited by Bullard)
- More than 750 gigawatt-hours of solar curtailed in California, a spring
  phenomenon peaking around April. California has roughly 10 gigawatts of storage
  already built. (California ISO data, cited by Bullard)
- As of 2024 California's minimum net load was negative across the entire spring
  in aggregate. Bullard is careful that this is an aggregate and negative "to a
  very tiny degree," not negative at every moment. (Bullard and Kann)
- Instances of negative hourly electricity prices in Europe: 500 to 550 in 2022,
  more than 9,000 in 2024. Summed across member states and grids, so it exceeds
  the 8,760 hours in a year. (Pexapark data, cited by Bullard)
- Grid-connected battery availability in the mid to high 90% range below 32
  degrees Fahrenheit and above 105, lowest observed point above 75%. (Modo data,
  cited by Bullard)
- US ten-year load growth expectations: 1.5% to 2% compound annual growth twenty
  years ago, about 0.5% by 2020, now above 1%. Kann rounds it to about 1.5% and
  compares it with roughly 2% actual growth in the early 2000s. The series is
  Bullard's own reconstruction, hand-loaded from PDFs, with a gap where no data
  was published in 2012. (NERC forecasts, compiled and cited by Bullard)
- Meta's Llama 3.1: 405 billion parameters, just under 31 million training hours.
  DeepSeek V3: 671 billion parameters, fewer than 2.8 million training hours, for
  comparable results. DeepSeek is open source and was funded with $5.5 million
  from a Chinese hedge fund. (Bullard)
- Roughly ten times more efficient on training and about thirty times on
  inference. Kann gives the training figure as an inference from Bullard's numbers
  and explicitly qualifies the inference figure as his own understanding. (Kann)
- Microsoft's chief executive publicly invoked the Jevons paradox and reaffirmed
  $80 billion of capital expenditure in connection with the Stargate data center
  plan. (Bullard)
- US high-voltage transmission of 345 kilovolts and above: 3,200 miles built in
  2013, 125 miles built last year. (Bullard)
- Chinese vehicle exports of 6.4 million last year, including 5.5 million
  passenger cars of which 2 million were electric, up from roughly 1 million a
  year until about four years ago. More than Japan or Germany export, far more
  than the US. China was just under 40% of global auto production, not capacity,
  in 2023. (Bullard)
- GM sold close to 4 million vehicles a year in China in 2017, almost all built
  locally, and under 1 million in 2024. (Bullard)
- BYD in Singapore: 0.2% market share in December 2021, 14.4% in December 2024,
  second only to Toyota, in a market of about 40,000 new vehicles a year.
  (Bullard)
- US data center construction spending of $31 billion last year against $27
  billion for hospitals; structures only, excluding GPUs and computing equipment.
  (Bullard)
- Virginia data centers consumed just under 34 terawatt-hours in 2023, almost 26%
  of state power. 2024 data was not yet available. (Bullard)
- Rappahannock Electric Cooperative: 1.2 gigawatt peak load, with single
  interconnection requests larger than that and in some cases four times larger.
  (Bullard)
- Energy is between 1.7% and 6.3% of the cost of training and experimenting with
  an AI model, ranking behind AI accelerator chips, other server components,
  interconnection costs, research staff and the cost of equity, the last two of
  which run 30% to almost 50%. (Epoch AI, via Andy Lubershane, cited by Bullard)

## Where it's contested

- **The DeepSeek question is left open on purpose.** Both readings are stated,
  neither is chosen, and Bullard says only that the answer lands somewhere in
  between. Kann's efficiency multiples rest on an assumption he states out loud,
  that DeepSeek's method and efficiency become the standard, and he flags the
  inference figure as his own understanding rather than reported data.
- **Forward-looking statements, with their conditions and who made them.**
  Bullard expects ERCOT to show more cumulative solar than wind in 2025 with
  batteries growing faster. He reports that European developers expect negative
  pricing to resolve itself, through hybridized wind or solar plus storage plants
  and new contract structures, because the price signal to act is unmistakable;
  he presents this as what a good developer will tell you rather than as his own
  forecast. He doubts a five-gigawatt data center request in Virginia actually
  goes through, and expects Virginia's data center consumption numbers to blow the
  doors off once companies' expansion plans land. Kann expects a wave of Chinese
  vehicles across most of the world absent tariffs and import bans, and suggests
  the load growth forecast of about 1.5% could turn out to be 3%.
- **The load growth chart measures expectations, not outcomes.** Bullard makes the
  point himself: during the period when half a percent was forecast, actual total
  demand growth was zero. He also flags that the series is his own hand-built
  reconstruction with a hole in 2012.
- **The curtailment counterfactual is unknowable.** Bullard says directly that we
  cannot see what California would look like without the storage already built,
  and that the four-hour duration norm is a regulatory artifact, so the market has
  no incentive to discover what other business models would achieve.
- **The energy cost share carries an explicit caveat.** The 1.7% to 6.3% figure
  covers training and experimentation only. Bullard says energy is probably, and
  should be, a bigger share of inference. The figure is also third-hand, from
  Epoch AI by way of Andy Lubershane. The conclusion drawn from it, quoted from
  Lubershane, is that energy is everything and nothing: binary in availability,
  minor in cost, which makes this buyer unlike an aluminum or steel producer.
- **Whether gigawatt-scale headroom ever existed.** Kann notes that a portfolio
  company recently found an industrial site with 40 megawatts of spare capacity,
  which still happens, while nobody stumbles across a spare gigawatt. Bullard
  doubts that scale was ever easily available, and says that if it was, it
  happened quietly and by design.
- **Coverage reflects the host's selection.** The episode is Kann picking slides
  out of Bullard's roughly 200-slide annual deck, and he says as much in thanking
  Bullard for letting him cherry-pick. It is not a systematic survey of the year.
