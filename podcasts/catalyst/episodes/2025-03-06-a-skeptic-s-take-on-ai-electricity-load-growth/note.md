---
episode: "A skeptic’s take on AI electricity load growth"
published: "2025-03-06"
guest: "Jonathan Koomey, founder and president, Koomey Analytics"
threads: [ai-compute, data-center-power, load-growth, utility-business]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2025-03, weeks after DeepSeek and with 2023 as the most recent year of real data. The forecasting argument is durable; every quantity in it is old."
---

## The question

How much electricity will AI data centers actually use, and how much weight
should anyone put on the forecasts saying the answer is enormous?

## The answer

Koomey's skepticism is aimed at the forecasts and at one adjective, not at the
direction of travel: he accepts the bottom-up estimate that US data centers
roughly doubled their share of national electricity in a few years, and says
another doubling by 2030 would not surprise him. What he rejects is that anyone can
forecast computing more than a few years out, and the "explosive growth" framing
at the national aggregate level, which he says the statistics do not yet show
even as he grants that regional growth is real. Underneath both sits a mechanism
claim: efficiency has historically absorbed most compute growth, and the AI
buildout has barely tried it yet.

## The argument

Every projection of data center electricity use, stated or not, multiplies two
things: how much service people demand, and how much electricity it takes to
deliver a unit of it. Koomey's history is that the second has repeatedly
swallowed the first. Data center electricity did double from 2000 to 2005, taking
the sector from roughly half a percent of US electricity to about 1% by 2010.
Then from 2010 to 2018 compute output rose roughly sixfold while electricity use
rose 6% in total, partly from shrinking transistors and new hardware
architectures, and substantially from workloads migrating out of inefficient
corporate server rooms into hyperscale facilities with better cooling, better
power delivery and much higher equipment utilization.

Kann presses the obvious objection: the migration to hyperscale was a one-time
move that has already happened, so that lever cannot be pulled twice. Koomey's
answer is that it was never the only lever. Beyond transistor shrink there is
hardware architecture, more efficient software, better algorithms, which he notes
are domain-specific but often worth orders of magnitude, and special-purpose
silicon co-designed with the software it runs. DeepSeek, which he describes as
hitting similar accuracy benchmarks on much less compute and at much lower cost,
is his live example that the software side is not exhausted. He puts the
remaining headroom at orders of magnitude, as a possibility rather than a
forecast. What makes him expect it to be used is not technology but constraint:
from 2000 to 2005 the industry built as fast as it could until the power bill
became a problem and then went after efficiency, and he expects that pattern to
repeat, with efficiency neglected so far only because the constraints had not yet
bitten. The incentive is money, since energy and capital are both large shares of
what a data center costs.

On demand he makes a narrower point than the episode's framing suggests. The
argument he is attacking is not really Jevons paradox, and he says tying it to
efficiency is a mistake, since measured rebound effects run about 10% to 20%, far
too small to carry the claim. What the AI suppliers actually assert is that demand
for their product is effectively infinite, so cheaper compute just means more
compute and the electricity gets used regardless. Koomey does not say that is
false. He says it is an assertion that should be open to discussion rather than
assumed, and gives three reasons to hold it loosely. Accuracy gains have
historically come from scaling, at something like 10% to 30% per tenfold increase
in compute, and each further tenfold is a far harder construction job than when
this was a small industry. Hallucinations may or may not be reducible enough that
companies accept the liability for what their agents do, which he says nobody
knows. And the revenue to justify the announced capital expenditure has not
appeared. Kann grants the revenue point and pushes back on the hallucination one,
that the models keep getting better at removing false answers. Neither claims to
know where demand lands, and both say so.

That is the actual thesis. After thirty years of energy forecasting, Koomey holds
that nobody can predict computing more than a few years out, that the two or
three year pipeline of announced projects is the limit of anyone's visibility,
and that a stated figure for 2035 is made up. It is a claim about confidence, not
about direction, and when Kann pins him to a number the direction turns out to be
up. He allows data centers going from about 4.5% of US electricity to roughly 9%
or 10% by 2030, which he works out to about one percentage point of total US
demand growth per year, and it is that one point he calls manageable rather than
explosive. Electrification of vehicles, industry and heat then adds one or two
points on top, for perhaps 3% annual growth against the 0.5% of the past twenty
years, which he calls the reasonable range. He does not apply the word manageable
to the 3%, and by his own arithmetic it is a sixfold acceleration on the last two
decades. His evidence for the softer adjective is that the bottom-up estimates
and the aggregate statistics disagree: US generation in 2023 came in below 2022
and roughly level with 2018, so the doubling of the data center share shows up as
a reshuffling of a flat pie rather than as visible national growth. He offers
that as a tension to be ironed out, not a finding.

## What you need to know first

- **Service demand and efficiency.** The two numbers behind any forecast: how much
  work people want done, and the electricity per unit of that work. Electricity
  use rises only when the first outruns the second.
- **Hyperscale versus corporate data centers.** Hyperscalers run huge
  purpose-built facilities with economies of scale, better power and cooling
  design and much higher utilization. Moving workloads into them was a large
  one-time efficiency gain.
- **Jevons paradox, or the rebound effect.** The idea that making something
  cheaper to run makes people use more of it, offsetting the saving. Measured
  rebounds are usually modest, which is why Koomey says the industry's real claim
  is about unlimited demand rather than about rebound.
- **Bottom-up versus aggregate accounting.** Bottom-up adds up equipment and
  facilities to estimate what the sector used; aggregate uses national generation
  and sales statistics. Here the two do not match.

## Details worth keeping

- His priors come from the dot-com era, when he was the Berkeley staff scientist
  asked to check widely-circulated claims about computing's electricity use and
  found them wrong by a wide margin. He says the experience left him skeptical of
  forecasts pushed by people with an interest in the narrative.
- The historical numbers are uncertain, not just the forecasts. Proprietary data
  held by firms such as IDC and Gartner, plus multi-year lags before it can be
  analyzed, mean a year like 2022 is still being revised.
- His practical test for any forecast is reproducibility. The December 2024
  Lawrence Berkeley report to Congress lets you see its assumptions, and he notes
  he was on that team; the International Energy Agency's projections, he says, do
  not release data or calculations in usable form.
- The assumption he says is most common in AI forecasts: taking NVIDIA's own sales
  plan as the growth forecast, which imports uncertainty about how many units sell
  and separately about how efficiently they get used.
- The efficiency story has a physical break point. Transistor shrink came with
  falling voltage until roughly 2000, when silicon hit a floor near one volt, and
  multicore chips arrived around 2005 as the workaround. Everything since has come
  from architecture, software, algorithms and specialization.
- Constraints work, illustrated by a Berkeley supercomputer proposal budgeted at
  40 megawatts. Then-director Steve Chu refused on the grounds that the power did
  not exist, and the redesign came back at 16 or 18 megawatts and worked.
- Sophisticated utilities are hedging the forecasting problem through rate design
  rather than better prediction: upfront payments and take-or-pay contracts that
  keep existing customers off the hook if a load never materializes, and that
  filter serious projects from speculative ones. He names Dominion in Virginia as
  experienced at this and says not every utility is.
- The bits-and-atoms mismatch: software moves in a year, generation, transmission
  and backup generators in ten or twenty. He recalls backup generator waits of a
  couple of years "a while ago" and says they are probably longer now, without
  putting a current number on it.

## Claims worth citing

All figures as stated on 2025-03-06 and attributed to the speaker rather than
verified. The share numbers come from a report published in December 2024 whose
most recent year is 2023, so they were already lagging at recording, and anything
about the AI buildout has moved since.

- US data centers were on the order of 2% of national electricity in 2020-2021 and
  4.4% in 2023, from a bottom-up calculation. (Lawrence Berkeley National
  Laboratory report to Congress, cited by Koomey, who was on the team)
- Data center electricity use doubled from 2000 to 2005, taking the sector from
  about 0.5% of US electricity to about 1% by 2010. (Koomey)
- From 2010 to 2018, data center compute output rose roughly sixfold while data
  center electricity use rose about 6% in total. (Koomey)
- In 2000, claims in circulation put all computing at 13% of US electricity and
  the internet on track for half of it within a decade; his Berkeley team found
  the actual figure was 3%. (Koomey)
- Two 2024 International Energy Agency estimates of the same historical year,
  2022, disagreed about global data center electricity: the January number came
  in 50% above the October one, against a stated uncertainty range of 220 to 340
  terawatt-hours per year. (International Energy Agency, cited by Koomey)
- Historically, roughly 10% to 30% accuracy improvement per tenfold increase in
  compute. (Koomey)
- Rebound effects from efficiency typically run 10% to 20%, and energy is only 7%
  to 8% of GDP. (Koomey)
- Energy is a meaningful but minority share of data center costs, more than 1% and
  less than half, alongside a very large capital cost. Kann calls it a large share
  of operating expense and Koomey only partly agrees, so the split is left loose.
  (Koomey, Kann)
- By 2030, data centers plausibly reach about 9% of US electricity from 4.5%,
  which he immediately rounds to 5% to 10%, and glosses as roughly a one
  percentage point addition to US demand per year. The phrasing runs shares and growth rates together, and the
  calculation assumes total electricity use stays flat, which he agrees it may
  not. (Koomey)
- Adding electrification of vehicles, industry and heat, perhaps 3% annual US
  demand growth against about 0.5% over the past twenty years, which he calls the
  reasonable range. (Koomey)
- US electricity generation in 2023 was lower than in 2022 and roughly equal to
  2018, and commercial sector use in 2023 was also below 2022. He adds that 2024
  probably showed a little growth, and that weather and other factors are in
  there too. (Koomey, citing Energy Information Administration aggregates)
- Current US data center capacity around 20 to 25 gigawatts. This is Kann's
  figure, offered as approximate and a few years old; Koomey says the 20 gigawatt
  number was true a few years ago and that today's is probably more, but gives no
  number and switches to percentages instead. (Kann)
- The announced capital expenditure on AI data centers sets a revenue bar a
  Sequoia piece framed as a $600 billion question, which Kann guesses is nearer
  $2 trillion now while saying he does not know the current figure. (Kann, citing
  a Sequoia piece by David Khan)
- Data center capacity or electricity use doubled from 2021 to 2024, raised to
  point out that the answer depends on the base year. He does not say which of the
  two doubled. (Koomey)

## Where it's contested

- **The efficiency lever is asserted, not demonstrated.** Kann's challenge is that
  the shift to hyperscale was a one-time gain already banked. Koomey answers with
  a list of remaining levers, one current example in DeepSeek and an argument
  from incentives and historical pattern, but nothing measured from this
  buildout, and when asked whether the curve bends in three years, ten or one,
  says nobody can know because it also depends on demand.
- **The core disagreement is never resolved.** Kann's position is that
  infrastructure binds first, chips, transformers, labor and power, so demand will
  not be the limiting factor for at least a few years. Koomey treats that as the
  same infinite-demand assumption in different clothing, says most of the industry
  believes it, and says whether it is true is exactly the conversation nobody is
  having. Neither persuades the other, and both state plainly that they cannot
  predict demand.
- **What he actually disputes is narrow.** He does not claim AI load growth is a
  myth, and he grants both regional growth and a further doubling. His objection
  is to the word "explosive" at the national aggregate level and to long-horizon
  forecasts, and he is explicit that a 2035 number is fabricated regardless of
  who publishes it.
- **He is reluctant about his own number and says so.** He calls himself squirrely
  about predicting, gives the 5% to 10% range only after Kann pins him down, and
  frames a further doubling as something that would not surprise him and is
  probably the limit, rather than as a forecast.
- **The size of the DeepSeek gain is Kann's number, not Koomey's.** Kann describes
  DeepSeek as doing the same thing with more than an order of magnitude less
  energy. Koomey's own description is similar accuracy benchmarks on much less
  compute at much lower cost, with no multiple attached, and he does not repeat
  Kann's figure.
- **The spike-then-plateau shape is Kann's formulation.** Kann proposes that AI
  load repeats the 2000-2020 pattern, fast rise then long slow one. Koomey calls
  it a reasonable way to think about it while adding that nobody can know and that
  it depends on service demand growth. Treat the shape as agreed-with, not as his
  own prediction.
- **The bottom-up versus aggregate gap is unexplained.** Koomey uses flat national
  generation as evidence against explosive growth and also calls it a tension to
  be ironed out, floating shifting loads, efficiency gains elsewhere and weather
  as partial explanations without settling on one.
- **Hallucinations as a demand ceiling is speculative on both sides.** Koomey says
  nobody knows whether the errors can be reduced enough to be worth the liability;
  Kann counters that the models are getting better. Neither claims evidence.
