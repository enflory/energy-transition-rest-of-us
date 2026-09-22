---
post: "Is the future of low-carbon industry off grid?"
published: "2025-01-10"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [microgrids, data-center-power, solar, energy-storage, heat-and-industry]
source_document: "essay.md"
note_version: 1
age_warning: "A January 2025 reading of solar, battery, gas and interconnection costs; every price in it has had time to move."
disclosure: "Lubershane says in a footnote that he was an early reviewer of the white paper this post is built on, and the cost-decline half of his argument rests on two Energy Impact Partners portfolio companies, Form Energy and Rondo Energy, which he names as such."
---

## The question

If off-grid solar can already power a data center at grid prices, does the same
logic put the future of low-carbon manufacturing off the grid too?

## The answer

He thinks it is possible, and thinks the case is stronger for industry than for
data centers. Industry is not pinned by the latency problem in the same way,
and many plants can tolerate planned outages, which lets them cut gas capacity
and reach a lower cost of energy than the data center version of the same
system.

## The argument

The post is built on a white paper by people at Scale Microgrids, Paces AI and
Stripe, which asks whether off-grid solar microgrids in the US could be big,
fast and cheap enough to be a compelling near-term alternative to new gas
plants for AI demand. Its answer is probably yes, and his own gloss is that the
costs it reports are close enough to grid power that a hyperscaler with a
carbon commitment would not blink at them. He says he was not surprised by
that, since the cost assumptions are reasonable and going off-grid avoids both
the interconnection charge and the decade it takes to build any transmission
line of consequence.
What surprised him was the scale. Screening for practical siting rather than
raw sunlight, the study still found more viable Southwest capacity for
mostly-solar data centers than the whole United States grid peaks at.

He then supplies the caveat that turns the post. Clustering that much computing
that far from population centers is almost certainly unrealistic, because
training a model is not sensitive to communications delay but using one is, and
he suspects that is a large part of why the strategy is not already happening.
The paper asks itself the same question. That caveat is exactly what does not
apply to a factory. From an energy point of view a data center is a big box
drawing a steady load, and so is an electrified manufacturing plant; the
difference is that the distance goods travel often matters less than the
distance data travels. With automation pushing labor down as a share of
production cost, he argues, energy is what is left to decide where industry
sits, and industry has always gravitated toward cheap primary energy.

Two further things make the industrial case cheaper rather than merely
equivalent. The white paper priced solar and batteries at what they cost today,
and he expects further cost reduction to outweigh the escalation risk he sees
coming from trade conflict with China, pointing to multi-day iron-air storage
and to storing energy as high-temperature heat as the routes to running a
system at 90% solar or better. And most industrial facilities do not need a
data center's uptime: for some of them 90 to 95% firm supply may be good
enough, so long as the interruptions are not unexpected, which means many can
probably get away with less gas capacity and a lower total cost. That is how he
gets to an off-grid cost of energy well below today's, and to a conclusion
about the country rather than the technology.
America already has the gas and the pipelines to serve as the backstop fuel,
and it is the solar and wind resource on top that could make it a clean
manufacturing superpower.

## What you need to know first

- **Levelized cost of energy.** The all-in average cost of a unit of energy
across a project's lifetime, capital and fuel together. Every comparison in the
post is made in it.
- **Running islanded.** Generating on site without a firm grid connection, so
the facility is its own small power system rather than a utility customer.
- **Firm supply.** Power you can count on at any moment. At 90 to 95% firm the
system will be down some of the time, which is tolerable only if the outages
are scheduled.

## Details worth keeping

- The site screen was Paces AI's contribution, and it excluded more than it
included: sites had to be within 30 miles of airports and highways for staff
and equipment, within 10 miles of an interstate gas pipeline, and clear of
protected land, steep slopes and property setbacks.
- A footnote records that the paper assumes a facility on small modular gas
generators needs 25% spare capacity to guarantee uptime.
- The premise that grid capacity is scarce rests on the North American Electric
Reliability Corporation's 2024 long-term assessment, which he says shows big
swaths of the continent struggling to keep up with demand growth.
- He is lukewarm on the thing driving the demand, calling himself only kinda
sorta excited about AI; a footnote explains that he finds the argument that
scaling laws will not hold up convincing, while still expecting much untapped
value from machine learning of other kinds.

## Claims worth citing

All figures as stated on 2025-01-10, and the cost figures are the white paper's
rather than his own except where noted. Prices for solar, batteries and
interconnection move fast.

- An off-grid data center on small gas generators would deliver energy at about
$86 per megawatt-hour, against a current United States average of $82 for
industrial-scale grid consumers. (white paper, cited by Lubershane)
- Adding solar and lithium-ion batteries at a good Southwest site gets about
half of total energy from the sun at practically the same price, around 70%
solar for under $100 per megawatt-hour, and 90% solar for about $110. (white
paper, cited by Lubershane)
- A single large combined-cycle plant serving a 500 MW data center would be on
the order of $40 to $50 per megawatt-hour, though he discounts that because one
big unit cannot match a fleet of small generators for reliability, so backup
generators get added back. (Lubershane, as an aside)
- Interconnection costs for United States solar projects now average more than
$200 per kilowatt, which can exceed 20% of a project's total installed cost,
and a transmission line of any consequence still takes about ten years to plan
and build. (Lubershane)
- The screen identified 1,294 gigawatts of viable Southwest sites for data
centers running on 90% solar, against a United States electricity demand peak
last year of about 745 gigawatts. (Paces AI, cited by Lubershane)
- Iron-air batteries can store multiple days of energy for less than a tenth of
the installed cost of a lithium-ion system. (Lubershane, on an Energy Impact
Partners portfolio company)
- His own expectation for future off-grid industrial power is roughly $60 per
megawatt-hour, with $30 to $50 not out of the question. (Lubershane, offered as
opinion)

## Where it's contested

Nobody argues with him here. The post carries one substantial caveat of his
own, several marked opinions, and interests he states plainly.

- **The caveat he raises against his own enthusiasm.** He calls it almost
certainly unrealistic for that much data center capacity to sit so far from
population centers, and flags the latency problem as probably one of the
biggest sticking points. He also marks the technical premise as secondhand,
saying it is his understanding that latency matters little for training.
- **The escalation risk he names but does not weigh.** He acknowledges
significant potential for solar and battery costs to rise on trade conflict
with China, then states without argument that he sees more potential for them
to fall.
- **The load-bearing assumption.** That siting follows cheap energy. He calls
it his bet and supports it with the historical pattern rather than testing it;
the Southwest manufacturing hub depends on it entirely.
- **Confidence markers worth keeping.** The headline conclusion is stated as "I
think it's possible", the future cost range as opinion, and the AI enthusiasm
underlying the whole exercise as somewhat skeptical.
- **What he has at stake.** He reviewed the white paper before publication, and
the two storage technologies he offers as the route to lower future costs are
his firm's portfolio companies' products, which he identifies as such in the
text.
