---
episode: "Inside Crusoe's energy-first approach to data centers"
published: "2024-10-22"
guest: "Chase Lochmiller, co-founder and CEO, Crusoe"
threads: [ai-compute, data-center-power, load-growth, renewables, skilled-labor]
source_transcript: "transcript.md"
note_version: 1
disclosure: "Labeled in the show notes as a partner episode brought to you by Crusoe, and hosted by Latitude's Stephen Lacey rather than Shayle Kann. Pipeline, siting and design figures come from Crusoe's CEO describing his own company, so they are company statements rather than independent measurement."
age_warning: "Recorded 2024-10, when Blackwell was the coming GPU generation and data center vacancy was the headline scarcity number; the chip figures, vacancy rates and pipeline are the perishable parts."
---

## The question

If you site computing around energy instead of siting energy around computing,
what changes?

## The answer

Crusoe's answer is that almost everything does, because AI training is unusually
tolerant of latency and can therefore be put wherever power is cheap, clean and
abundant rather than wherever users are. Lochmiller's second claim is the one
worth carrying: he thinks AI's electricity demand is being under-forecast, not
over-forecast, and he treats that as an opportunity to catalyze new clean
generation rather than a reason for restraint.

## The argument

Start with the constraint, because it drives the rest. Asked directly whether
power or chip supply limits AI today, Lochmiller says power, and describes the
bottleneck moving. A year earlier the scramble was for chips. Once the existing
data center capacity was absorbed, US vacancy ended 2023 below 2% and was below
1% at the time of recording, which for a commercial real estate asset class is
effectively nothing. What now limits new capacity is access to power, and he
lists the specific chokepoints rather than leaving it abstract: grid
interconnection queues, high-voltage transformers, switchgear and backup
generation.

If power is the scarce input, the siting logic inverts, and one property of AI
makes that possible. Training workloads are far more tolerant of latency than
most computing, so the load can be positioned geographically in a way that, say,
a trading system or a consumer app cannot. That is the whole basis of the
energy-first approach. It sends Crusoe to places that are not traditional data
center markets: West Texas, where wind and solar are heavily built out and there
is substantial curtailment and negatively priced power; a former Alcoa factory
in upstate New York attached to a large hydro dam Lochmiller describes as
massively underutilized; and Iceland, where geothermal and hydro are cheap and
the climate makes cooling easier. Alongside those brownfield sites, the company
partners with independent power producers on new generation, taking load behind
the meter, using the existing substation infrastructure and keeping the grid
connection as a backup rather than as the primary supply. His analogy is that
aluminum smelting already made this trade, shipping ore across an ocean to do
the electricity-intensive step in Iceland. Training a model is the better
version of the trade, because what moves is data over subsea cables rather than
physical material.

The demand argument is where he separates himself from the industry's public
posture, and Lacey names the contrast: large tech companies concede privately
that this will use a lot of power while hedging in public. Lochmiller does not
hedge. He thinks demand is under-forecast, and supports it with a thought
experiment rather than a model: if every American adult ran half an H100 as a
copilot for daily work and social interaction, that alone would require 250
gigawatts, which he says is orders of magnitude larger than the forecasts on
offer. He adds positive reflexivity, meaning that as the models get more useful
people use them more, which drives more compute, which draws more power. The
reason he frames this as an opportunity rather than a threat is that the load is
steerable, so it can pull net new clean generation into existence where it would
not otherwise be built: batteries alongside West Texas wind and solar as costs
fall, or new gas paired with carbon capture and sequestration, an area he says
Crusoe spends a great deal of time on. Underneath that sits a value judgment he
states plainly, that power consumption is not bad in itself if it advances
things worth advancing, and an expectation that AI will invent solutions to
sustainability problems. That last step is the load-bearing one and it is
asserted rather than demonstrated.

## What you need to know first

- **Latency tolerance.** How much delay a workload can absorb before it stops
  being useful. Large-model training can absorb a lot, which is why the compute
  can be moved to remote power instead of the power being brought to population
  centers. This single property carries the whole energy-first thesis.
- **Curtailment and negative prices.** When a grid has more wind or solar output
  than it can use or move, generators are cut back, and prices can go below zero.
  That surplus is the resource Crusoe is trying to convert into compute.
- **Behind the meter.** Connecting a load directly to a generator rather than
  taking supply through the grid. Here it lets a data center use an existing
  substation and treat the grid connection as backup.
- **Power density per chip.** Watts drawn by a single accelerator. It is rising
  fast across chip generations, and it is what forces liquid cooling and
  redesigned data center layouts.

## Details worth keeping

- The pipeline number and the scale shift behind it: roughly 12 gigawatts in
  development or advanced commercial discussions. Lochmiller says a remarkable
  number of people now ask for gigawatt-scale sites, and some of those asking for
  one gigawatt actually want ten, which is pushing customers toward linking data
  centers across geographies into a more synchronized, decentralized footprint.
- Training clusters behave like nothing else on a grid connection. Data is
  broadcast to the GPUs, they compute, they publish results, and the cycle
  repeats hundreds or thousands of times a second, so the cluster "breathes,"
  with power draw spiking and dropping at that frequency. He describes this as a
  genuine and unexpected power management problem they had to engineer around.
- Chip power density is the main design driver: about 300 watts per chip for the
  previous-generation A100, about 700 watts for the current H100 and H200, and
  about 1,200 watts for the coming GB200. Cooling those systems is what he calls
  the biggest engineering challenge from the data center side, and the
  large-scale liquid cooling that follows is mostly plumbing.
- He points at a labor story that he says is under-discussed: massive shortages
  of electricians, welders and plumbers, an AI boom that is simultaneously a
  blue-collar boom, and a revitalization of regions such as the Rust Belt.
- Two responses to remote siting. Modularity and offsite fabrication, because
  getting labor to a remote low-cost-energy site is hard and work done in a
  controlled factory deploys faster and cheaper on site. And cabling, where he
  notes that one of their large clusters involves over a million strands of
  fiber.
- On water, the approach is closed-loop cooling systems to minimize net water
  consumed.
- The most speculative idea in the episode comes from a conversation with Orbital
  Materials, a team out of DeepMind working on foundation models for inorganic
  chemistry. The proposal is a custom-engineered direct air capture material
  tuned to the specific temperature of a data center's waste heat, absorbing
  carbon and chilling the water at the same time, which would point at a net
  carbon-negative facility. Lochmiller calls it a bit science-fictiony himself.

## Claims worth citing

All figures as stated on 2024-10-22. Figures about Crusoe's own pipeline, sites
and designs come from its CEO in a partner episode, so attribute them to the
company. Chip specifications, vacancy rates and demand forecasts move quickly.

- Power, not chip supply, is the main constraint on scaling AI. (Lochmiller)
- US data center vacancy ended 2023 below 2% and was below 1% at the time of
  recording, the second figure hedged as what he thinks it is. (Lochmiller)
- Roughly 12 gigawatts in Crusoe's pipeline, defined loosely as development or
  advanced commercial discussions. (Lochmiller)
- Chip power draw: about 300 watts for an A100, about 700 watts for an H100 or
  H200, about 1,200 watts for a GB200. (Lochmiller)
- If every American adult used half an H100 as a copilot, it would require 250
  gigawatts. This is an illustration rather than a forecast, and the assumptions
  converting chips to gigawatts are not given. (Lochmiller)
- Demand is being under-forecast, and the illustration above is orders of
  magnitude larger than the forecasts in circulation. (Lochmiller)
- One of Crusoe's large clusters involves over a million strands of fiber.
  (Lochmiller)
- Third-party projections offered by the host as framing: the International
  Energy Agency and Goldman Sachs expecting electricity demand to double in three
  to five years; Morgan Stanley projecting that generative AI alone in 2025 could
  account for a third of the total computational demand seen from data centers in
  2022; regulated utilities potentially facing $5 to $10 billion of annual
  capital investment. The first of these is stated without saying whether it
  means data center demand or total electricity demand, and Lochmiller does not
  engage with the individual numbers. (Lacey, citing IEA, Goldman Sachs and
  Morgan Stanley)
- Named siting examples: West Texas wind and solar with heavy curtailment and
  negative prices, a former Alcoa site in upstate New York on an underutilized
  hydro dam, and geothermal and hydro in Iceland. (Lochmiller)

## Where it's contested

- **This is a partner episode and the conversation runs with the guest rather
  than against him.** Lacey does not test the 250-gigawatt illustration, the
  12-gigawatt pipeline or the claim that demand is under-forecast. The sharpest
  moment is his observation that large tech companies concede the power demand
  privately and hedge publicly while Lochmiller does not, which Lochmiller
  accepts as a fair characterization.
- **The company's own figures are exactly that.** Pipeline, site descriptions,
  closed-loop water claims and deployment plans come from the CEO, with no
  third-party data, operating results or customer figures in the episode. Normal
  for this format, and worth remembering before repeating them as measured.
- **The 250-gigawatt figure is a hypothetical, not a projection.** It assumes a
  usage pattern that does not exist, does not state utilization or supporting
  infrastructure, and is never reconciled with the third-party forecasts quoted
  earlier in the episode. Its purpose is to argue that forecasts are too low, not
  to give a number.
- **The host's closing restatement runs ahead of the guest.** Lacey sums up the
  conversation as Lochmiller thinking the industry already has the business
  models and clean energy technologies to solve most of the problem. Lochmiller's
  own answer is narrower: he says he is optimistic that the load itself has
  control over how it demands power, and then argues from the technological upside
  of AI. He never claims the solutions are in hand, and the note should not be
  read as saying he did.
- **The strongest claim is the least evidenced.** That AI's payoff will include
  inventing solutions to sustainability problems is offered as a perspective,
  explicitly framed as a choice between two attitudes toward the technology
  rather than as a result. He supports it with examples of customers doing work
  in that direction, including fusion modeling, advanced weather modeling for
  climate adaptation, battery chemistry work with SES and materials for direct
  air capture, but those are activities under way, not demonstrated payoffs.
- **The carbon-negative data center is a concept from a conversation**, not a
  system anyone has built, and he says so.
