---
episode: "The mechanics of data center flexibility"
published: "2025-08-28"
guest: "Varun Sivaram, founder and CEO, Emerald AI"
threads: [ai-compute, data-center-power, demand-flexibility, load-growth, interconnection]
source_transcript: "transcript.md"
note_version: 1
---

## The question

What does it actually take to make an AI data center flexible, and how much
flexibility is really there?

## The answer

Mechanically it is mostly software: pausing, slowing, reallocating or relocating
AI workloads rather than firing up generators. A demonstration on a GPU cluster
in Phoenix cut demand 25% for three hours while meeting representative
performance requirements, one run reaching 40%. But the binding constraints are
commercial rather than technical: a new kind of uptime contract with compute
customers, and enough demonstrated reliability for grid operators to count the
reduction as capacity. Sivaram thinks both are reachable, and says so as a
probability rather than a settled fact.

## The argument

The setup is a mismatch that looks like free money. When a hyperscaler asks to
connect a 400-megawatt data center, the grid operator studies the worst case: not
just whether it can serve 400 megawatts across all 8,760 hours of a year, but
whether it could do so in the worst hour of any year over the next seven to ten,
with a transmission line out and record air conditioning demand. The facility
does not behave that way. It ramps over years as halls get filled, may run at
three-quarters utilization even during an intensive training run, and produces a
jagged profile: training runs spike by tens or hundreds of megawatts, dip at
synchronized checkpoints, then drop away when the run ends. Inference is smoother
but still hard to predict. So there is obvious headroom between what is reserved
and what is used.

The move that makes the episode worth reading is that Sivaram refuses to call the
grid wrong. He says the risk-averse study method is neither irresponsible nor
analytically incorrect, because a customer granted a 400-megawatt entitlement may
well use all of it, and some large data centers do run flat out. The headroom is
therefore not free. It becomes usable only if somebody can convert "probably will
not draw full power" into a commitment the operator can plan against, which is a
different problem from the one the load profile suggests.

Delivering that commitment is where the mechanics come in. The physical route,
running backup generation, is usually blocked by air permits. The computational
route works on the load itself: pause or delay a job that can tolerate it, such
as fine-tuning a model for an enterprise customer that does not mind if it
finishes an hour later; slow a job down; change how many chips are allocated to
it; or go down to the silicon and cut the clock frequency so computation happens
more slowly and draws less power. Flexibility can also be spatial, moving a
workload to another site. What makes this hard is the dual optimization. The grid
needs a precise reduction, not a megawatt over the agreed cap, while every
workload has its own tolerance for delay, throttling or power capping, so the
system has to know what it is running. Sivaram is direct that this is far harder
than pausing a batch of jobs.

The evidence and its limits sit together. In Phoenix, Emerald AI worked with the
Electric Power Research Institute, Nvidia, Salt River Project and an Oracle data
center to hold a 25% reduction for the three hours the Arizona grid needed, using
ensembles of workloads specified by Databricks' chief AI scientist, who reported
that only about 10% of a representative cluster's workloads were strictly
non-preemptible. The 25% target was not arbitrary: it is the threshold from Tyler
Norris's Duke University paper, which argued roughly 100 gigawatts of spare
capacity exists on US grids if large loads can curtail about that much for around
two hours, up to 200 hours a year. What remains unsettled is the contract. Two
decades of service-level agreements promise essentially uninterrupted power, and
flexibility needs a third product between a guaranteed instance and a preemptible
spot instance: an almost-firm agreement where a customer is left alone 99% of the
time and gracefully power-capped for the rest. Sivaram's evidence that this will
sell is conversations with hundreds of AI companies plus the logic of scarcity,
since customers who cannot get compute at all have reason to trade a small
bounded performance risk for more of it. His answer on whether the new contract
works is "probably yes." Grid operators need to see it before they believe it,
which is why his pitch to a room of utility chief executives was to join an
escalating series of demonstrations.

## What you need to know first

- **Service-level agreement.** The contract between a data center operator and
its compute customer, historically promising near-uninterrupted availability.
Changing it is the pivot the argument turns on.
- **Preemptible workload.** A job that can be paused, delayed or slowed without
breaking what the customer was promised. The preemptible share sets the ceiling
on how much flexibility exists.
- **Power capping and clock frequency.** Throttling chips so they compute more
slowly and draw less power, rather than switching anything off. This is how a
reduction is made precise instead of all-or-nothing.
- **Interconnection study.** The utility's worst-case test of whether a new load
can connect. Because it assumes full draw at the worst hour for years, it is what
flexibility has to change to unlock capacity.

## Details worth keeping

- Historically a data center lost around a third of its power to cooling and
other non-computing uses. In newly customized AI facilities, 80% to 90% reaches
the computation itself.
- Rack density is rising by orders of magnitude: about 5 kilowatts a few years
ago, 132 kilowatts for a liquid-cooled Nvidia GB200 rack Sivaram saw in Silicon
Valley, and one megawatt racks on the horizon.
- A data center will not keep one load profile for its life. GPUs bought to train
a large model get repurposed for fine-tuning, research and inference, so Sivaram
would not count on a stable profile even a year out.
- Emerald AI is training a model to infer what workload is running from the power
signature alone, and has built a digital twin, the Emerald Simulator, to predict
what a given orchestration would do.
- Google is the precedent on both halves: it moved video indexing to nighttime
years ago for carbon reasons, and has announced demand response arrangements with
two utilities, named in the episode as Michigan Power and the Tennessee Valley
Authority.
- Per-chip efficiency is improving across Nvidia generations, but the gains are
consumed by compute growth, so total power still climbs.
- Sivaram reads the politics as regulators squeezed between affordability and
economic development, with flexibility seeming to dissolve that trade-off.

## Claims worth citing

All figures as stated on 2025-08-28, attributed to the speaker rather than
independently verified. Growth rates and load forecasts here move fast.

- Phoenix demonstration: 25% demand reduction sustained for three hours on a
large GPU cluster, one run reaching 40%, using representative workloads; posted
as a preprint. (Sivaram, with the Electric Power Research Institute, Nvidia, Salt
River Project and Oracle)
- Only about 10% of workloads on a representative cluster were strictly
non-preemptible, which Sivaram says surprised him. (Jonathan Frankle of
Databricks, cited by Sivaram)
- Roughly 100 gigawatts of spare grid capacity is available if large loads curtail
about 25% for around two hours, up to 200 hours a year. (Tyler Norris's Duke
paper, cited by Sivaram, who notes Norris advises his company)
- 50 to 100 gigawatts of latent AI demand in the pipeline that Sivaram says will
not get built without flexibility. (Sivaram)
- Data center power demand has more than doubled every year for several years,
because compute demand is more than quadrupling annually. No source given.
(Sivaram)
- Data centers are about 4% of American energy consumption today and AI data
centers about 5 gigawatts of load, growing to 12% by the end of the decade, with
AI data centers possibly exceeding 50 gigawatts and reaching 25% of American load
by 2035 and beyond. The sentence runs the two categories together, so which
figure applies to all data centers versus AI specifically is unclear. (Sivaram)
- Shifting a latency-sensitive workload within a 500-mile radius costs under 50
milliseconds of added latency, which one real-time world-model company said it
could tolerate for under 1% of the year. (unnamed CEO, cited by Sivaram)
- Emerald AI plans commercial scale, whole data centers made flexible, early the
following year. (Sivaram)

## Where it's contested

- **The demonstration is narrower than the claim it supports.** It ran on a large
GPU cluster for three hours with representative rather than live customer
workloads. Whole-data-center operation at commercial scale is a company plan for
early 2026, not a result, and figures about Emerald AI's own capability are the
founder's targets.
- **Disclosed relationships sit under the central number.** Tyler Norris, whose
paper supplies both the 100-gigawatt headroom estimate and the 25% threshold the
demonstration was designed to hit, advises Emerald AI; Sivaram says so on air.
Nvidia, a partner in the demonstration, is the company's biggest investor.
- **The contract question is explicitly open.** Sivaram's answer on whether an
almost-firm service-level agreement can work is "probably yes," resting on
conversations with prospective customers rather than signed agreements.
- **He declines the easy argument that utilities are being irrational.** Rather
than calling conservative interconnection studies a mistake, he defends them,
which narrows the claim from "headroom is going to waste" to "headroom becomes
usable only once flexibility is guaranteed."
- **Not every workload is flexible, and the product is narrow today.** Kann
raises the reason hyperscalers long resisted flexibility, commitments to deliver
quickly, and suggests some inference has no room in it; Sivaram answers with the
range of customers willing to tolerate a little disruption rather than claiming
all workloads flex. The application is also 100 to 200 hours a year of demand
response, not daily load shifting, which is described as possible later with the
same toolkit if prices justify it.
- **What would convince grid operators is unresolved.** Sivaram asks for
escalating demonstrations, accuracy from the digital twin and a fail-safe. Kann
notes traditional demand response took a long road to acceptance and this is a
further level of complexity.
