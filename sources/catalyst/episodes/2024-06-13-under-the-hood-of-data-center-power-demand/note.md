---
episode: "Under the hood of data center power demand"
published: "2024-06-13"
guest: "Brian Janous, co-founder, Cloverleaf Infrastructure; former vice president of energy, Microsoft"
threads: [data-center-power, ai-compute, load-growth, demand-flexibility, interconnection]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded June 2024, early in the AI load-growth story; the demand numbers are forecasts that the speakers say were being revised within months, and the flexibility ideas discussed were mostly unbuilt."
disclosure: "Janous names Enchanted Rock, cited as an example of behind-the-meter flexibility work, as a portfolio company of Energy Impact Partners, which is Kann's firm."
---

## The question

Granting that AI will pull a large amount of new load onto the grid, how do we
actually serve it, and what does serving it do to the grid and to the tech
companies' climate commitments?

## The answer

Not by taking data centers off the grid, and not by waiting for utilities to
build everything the queue implies. The leverage Janous sees is in making a
load that has always demanded firm round-the-clock power contribute less to the
utility's annual peak, using the generators and batteries data centers already
own alongside utility-side technologies that squeeze more out of existing
wires; the motive is less cheap electricity than getting connected years
sooner. He is skeptical of both comforting stories in circulation: that AI
training is naturally a flexible load, and that chip efficiency gains will
erase the demand.

## The argument

Note first what this episode deliberately does not do. Kann opens by naming the
loud argument, a recent EPRI report whose high end has data centers at about
10% of US electricity by 2030 against skeptics who expect efficiency to erase
most of that growth, and then sets it aside: he posits that demand will be a
lot, and a lot more than historically, and says the question he wants is how it
gets met. Nothing here is evidence about the size of the load; it is a
conversation about mechanisms, conducted on a premise. What was known in
mid-2024 was mostly utility interconnection queues, and Janous discounts those
immediately. Queues carry zombie requests the same way generation queues do, so
the headline figures, roughly 80 or 90 gigawatts at AEP depending on which
speaker you take, are not forecasts. But the discounted number is still large:
he puts real demand inside AEP's system above 10 gigawatts almost certainly,
against a total US data center fleet Kann recalls at around 20 gigawatts, which
he flags may be a year or two stale. The direction of revision tells more than
the level. Roughly 4 gigawatts of data center demand were anticipated
for AEP by 2030 as of January; by May the figure had been revised to nearer 15.
AEP draws this load for a physical
reason: it runs the country's highest transmission voltage at 765 kilovolts,
and announced hyperscaler sites trace that line, because gigawatt-scale
campuses need a point on the grid that can already support them.

Why campuses rather than fleets is the pivot. A cloud region is a cluster of
data centers within a latency envelope, and a region at the end of the last
decade meant a few hundred megawatts. AI training changed the unit of demand
because a training run cannot be spread across regions, a constraint Janous
flags as outside his expertise, so the requests became gigawatt-scale single
sites. That same batch-process character is what makes people assume training
is curtailable, and Janous thinks the assumption is overblown. Training is
indeed a batch process and inference is not, but the binding constraint is
economics rather than physics: the servers cost so much that utilization has to
stay high, in the same way an electrolyzer or a nuclear plant does, so nobody
will attach a training cluster to a wind farm and run it at a 35% capacity
factor. What is plausible is avoiding significant contributions to system peak
for a few hours a year, not following the sun.

That sounds like a small prize until you look from the utility's side, which is
where the episode turns. Ten gigawatts of firm round-the-clock load
means ten gigawatts of new peak capacity plus a reserve margin on top, and
roughly seven years to build it. Shaving peak can also dodge expensive
afternoon power, but the bigger question for the data center is whether it is
willing to wait seven years. A few hours a year of flexibility becomes the
price of getting online. From there the options sort into three. Going off-grid is the one
Janous finds least interesting, because it mostly means building a gas plant,
which trades the power grid for the gas grid along with its constraints and its
questionable firmness; solar and storage will not serve a site of 500 megawatts
to a gigawatt, and while he is bullish on nuclear it will not deliver inside
the two-to-four-year window these companies are working to. The second is the
assets already on site. A data center, he says, is a power plant and a storage
plant that happens to have a room of servers next to it, and those diesel
generators and uninterruptible power supply batteries can be made to talk to
the grid. Microsoft built a gas turbine project in Cheyenne in 2016 and a
grid-interactive UPS in Dublin some years later, but the practice has
normalized only in Dublin, and only because the grid operator was headed for a
moratorium and was persuaded instead to require dispatchability in exchange for
a connection. The third is the utility's own side of the meter, where
grid-enhancing technologies free up existing capacity and cut how much
flexibility the customer has to supply.

Two things stay unresolved. The utility ask cuts against the rate-base
incentive, since utilities have historically made money by building; Janous's
answer is competitive rather than regulatory, that they want this load and its
economic development badly enough to move fast, and that squeezing the existing
system lets them say yes before their peers do. When Kann presses on fairness,
whether other ratepayers end up subsidizing this and whether other projects get
crowded out, the answer moves to why utilities are motivated rather than to how
the cost is allocated, and the tariff question is left open. On decarbonization
Janous is more direct: the headwinds since the 2030 commitments were written,
COVID, supply chain disruption, interconnection queues and AI, mean those
targets are probably not achievable on the timelines set, though he notes that
none of the companies has said so. Efficiency does not rescue them either, on
his reasoning, because the gains get spent rather than banked. If a company
secures a site that can deliver three gigawatts and chips then double in
efficiency, it does not build a 1.5 gigawatt data center; it builds a three
gigawatt one that is twice as powerful, because the competition is over the
size of the model. Which leaves peak contribution as the most useful lever,
since it is peak that pushes utilities to add fossil generation and extend the
lives of old plants.

## What you need to know first

- **Region.** In cloud terms, a cluster of data centers close enough together
  to look like one machine to a customer. The hyperscalers run dozens of
  regions made of hundreds of buildings; the scale of a region is what changed.
- **System peak and reserve margin.** The single highest hour of demand a
  utility must serve, plus a required cushion above it. Capacity gets built for
  that hour, which is why a load that never steps aside is expensive to add.
- **Training versus inference.** Training builds the model and runs as a batch
  job that could in principle pause. Inference answers a user and cannot, since
  it behaves like a search query.
- **Behind-the-meter assets.** Equipment on the customer's side of the utility
  meter: in a data center, the diesel or gas generators and the uninterruptible
  power supply batteries that hold power quality and bridge outages, all
  installed for resilience rather than for the grid.

## Details worth keeping

- Janous dates his own realization: odd questions about how large a single data
  center could be in summer 2022, the chatbot release that November, then the
  model jump the following spring, which is when he concluded power would be
  the constraint. The transcript garbles the model version numbers.
- Microsoft moved to power-first siting a couple of years before that, as its
  annual procurement tranches grew from tens or hundreds of megawatts to
  gigawatt scale.
- The 48-hour diesel backup standard is a relic of the 5-to-10-megawatt,
  distribution-connected data centers of 15 years ago. Today's sites connect at
  the highest voltages, where reliability is better, so Janous thinks there is
  probably flex in the resilience requirement, while naming the Texas storms
  and California wildfire risk as real counterexamples.
- Microsoft's carbon-negative-by-2030 path was set in late 2019, with Janous in
  the room, before any of those headwinds existed.
- Kann's framing, which Janous accepts: power used to sit well down the siting
  checklist behind latency, fiber, water and workforce, and is now first by a
  wide margin.

## Claims worth citing

All figures as stated on 2024-06-13, when the speakers say the numbers were
being revised every few months. These are projections and queue figures, not
measurements of delivered load.

- Data centers could reach about 10% of US electricity by 2030 at the high end.
  (EPRI report, cited by Kann)
- AEP's interconnection queue: about 80 gigawatts per Kann, answered as 90 by
  Janous, who says there is no reason to believe AEP connects that within ten
  years. Used loosely by both. (Kann, Janous)
- Real demand within AEP's system is in excess of 10 gigawatts almost
  certainly. (Janous)
- Total US data center load is around 20 gigawatts, which Kann says may be a
  year or two old; Janous agrees. (Kann)
- Roughly 4 gigawatts of data center demand were anticipated for AEP by 2030 as
  of January 2024; by May the number had been revised to closer to 15. He
  attributes the first figure to PJM and the revision to AEP. (Janous)
- AEP operates a 765-kilovolt system, the highest voltage in the country, with
  a little 765 also in New York. (Janous)
- A large data center region was a few hundred megawatts at the end of the last
  decade. (Janous)
- Data centers are almost 20% of Ireland's total electricity consumption, and
  nearly all of them are in Dublin. (Janous)
- Microsoft's overall emissions are up 30% since it made its initial
  commitment. (Kann)
- Connecting 10 gigawatts of firm load requires 10 gigawatts of new peak
  capacity, on a roughly seven-year build. An illustration using AEP, not AEP's
  own plan; the reserve margin on top is Kann's addition, which Janous
  explicitly endorses. (Janous)

## Where it's contested

- **The premise is granted, not argued.** Kann explicitly declines the
  how-much-demand conversation and posits a large number at the outset. Anyone
  citing this episode on the size of AI load is citing an assumption.
- **How curtailable AI load is.** Janous calls the curtailable-training idea
  overblown on utilization economics. Kann pushes twice, arguing that if the
  power constraint gets acute enough and the economics stay lucrative, daily
  peak avoidance might become worthwhile. Janous concedes it is possible and
  returns to the capital argument, leaving it unresolved.
- **The efficiency rebuttal is behavioral, not measured.** His answer to the
  efficiency skeptics argues from competitive incentives on a fixed site,
  illustrated with a hypothetical about Meta and a more efficient Nvidia chip.
  No data is offered.
- **Cost allocation is raised and not answered.** Kann asks directly how to
  keep utility spending on behalf of data centers from raising other customers'
  prices or crowding out other interconnections. The reply addresses why
  utilities want the load and notes that cost recovery and dispatchable tariffs
  are new territory for regulators.
- **Janous disclaims expertise twice.** He says the internal architecture of
  training models is not his area when explaining why they cannot span regions,
  and says he is no longer on the inside when describing how hyperscalers now
  rank clean power against speed.
- **The climate-target judgment is his own.** He says the 2030 commitments are
  probably not achievable on the stated timelines while noting that none of the
  companies has said that, and that they describe themselves as doubling down.
- **The central mechanism is largely unbuilt.** By his own account
  behind-the-meter flexibility is demonstrated but normalized only in Dublin,
  and there only because a regulator forced it.
