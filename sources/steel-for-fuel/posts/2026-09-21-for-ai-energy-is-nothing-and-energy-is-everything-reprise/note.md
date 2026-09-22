---
post: "For AI, energy is nothing, and energy is everything (reprise)"
published: "2026-09-21"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [ai-compute, data-center-power, electricity-prices, techno-economic-analysis]
source_document: "essay.md"
note_version: 1
---

## The question

How much could an AI data center pay for electricity before the computing stops
being worth doing?

## The answer

Far more than the power industry is used to thinking about. A framework called
the compute heat rate puts the current break-even ceiling for frontier-model
inference at 142 times what American industrial consumers pay. It measures what
a workload can tolerate rather than what anyone will be charged, and its author
says the inputs are moving fast.

## The argument

The post is Lubershane revisiting his own two-year-old piece, and the quoted
passages are the position he is building on rather than the one he holds now.
In 2024 he argued that energy was a trivial share of the cost of computing, so
AI developers ought to pay a substantial premium to secure power. Two things
have changed. Inference, the workloads customers pay for directly, now drives
demand, and there is far more public data on what it earns. Separately, the
public has started watching what data centers do to electricity prices, and he
quotes his own post from a few weeks earlier: an individual project probably is
not raising your bill, because utilities make projects pay more than their
incremental cost, but data centers collectively are putting systemic pressure
on infrastructure costs.

That leaves the question he had previously declined to answer. The compute heat
rate is an outside attempt at it, built by Hans Royal and collaborators, and
the bulk of the post is Royal's own explanation, invited by Lubershane and run
under Royal's headings. The name borrows from a power plant's heat rate, the
efficiency of turning fuel into electricity; this one chains electricity into
floating-point operations, operations into tokens, and tokens into dollars, to
give the most a facility could pay for power and still break even. Royal splits
it in two, and the split is the useful part. The long-run version carries the
full cost stack and a required return, so it governs whether to build. The
dispatch version treats capital as sunk and governs whether to curtail a
facility already running. A developer and an operator across the road from each
other face different thresholds.

What keeps the headline number from being a prediction is that its two main
inputs pull against each other: what matters is price per token multiplied by
tokens per megawatt-hour, and the models that charge most per token are the
ones that burn most electricity making each one. Token prices have already
fallen substantially, and Royal says a continued trend would pull the metric
down with them.

## What you need to know first

- **Heat rate.** For a power plant, how efficiently it turns the energy in its
fuel into electricity. The compute heat rate borrows the name for a conversion
running the other way, from electricity into saleable output.
- **Inference.** Running a trained model to answer requests, as distinct from
training it. It is the part customers pay for directly, which is what makes
revenue per unit of electricity observable.
- **Token.** The unit AI providers meter and bill by. Its public price is what
the framework uses to value a workload's output.

## Details worth keeping

- Roughly two thirds of the post is written by Royal, ending where Lubershane
resumes at "Back to Andy:".
- Lubershane says the question arose when he and his partner Shayle Kann
discussed it on Kann's podcast, and that Royal wrote to him afterwards.
- The formulas, the token price history and the third-quarter 2026 index are all
published as images. The index value appears only in that figure, so this note
cannot carry it.
- Token throughput is estimated from MLPerf scenarios rather than measured, and
self-hosted inference is proxied by GPU rental rates.

## Claims worth citing

All figures as stated on 2026-09-21. The central figure is a third party's
calculation reported by Lubershane, and it is a threshold rather than a price
anyone pays.

- The compute heat rate for frontier labs selling inference is currently
$12,790 per megawatt-hour. (Royal and collaborators, cited by Lubershane)
- Power prices for industrial consumers in the United States averaged about $90
per megawatt-hour. (Lubershane)
- Data centers could therefore theoretically pay up to 142 times what
industrial facilities currently pay. (Lubershane's arithmetic on the two
figures above)
- Larger models can consume three or four times the electricity per token, so a
frontier model may post only a modest compute heat rate while a small model
priced at pennies posts a high dispatch figure. (Royal)

## Where it's contested

Nobody contests anything here; there is no second voice arguing. What the post
does carry is an unusual amount of stated uncertainty, nearly all of it
volunteered by the framework's own author.

- **The framework's author is an interested party.** Royal built the metric and
publishes its index, and describes it here in his own words. The caveats below
are his, to his credit, but nobody independent tests the method.
- **The revenue input may not be real.** Published API pricing is not
necessarily what enterprises pay, since they negotiate bilaterally.
- **The headline number is explicitly not a forecast.** It measures what a
workload can tolerate, not what electricity will cost, and varies dramatically
across model tiers; the blended index rests on weightings Royal calls estimates.
- **It may already be falling.** With token prices declining, the $12,790 is a
reading at one moment rather than a stable ceiling.
- **The prompting question goes unanswered.** It was whether data centers could
offset more of other ratepayers' costs. The post establishes what they could
tolerate paying and never returns to whether they will.
