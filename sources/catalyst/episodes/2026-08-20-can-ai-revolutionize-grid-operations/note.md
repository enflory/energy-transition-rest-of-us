---
episode: "Can AI revolutionize grid operations?"
published: "2026-08-20"
guest: "Josh Wong, CEO and founder, ThinkLabs AI"
threads: [grid-operations, interconnection, utility-business, transmission, data-center-power]
source_transcript: "transcript.md"
note_version: 1
disclosure: "Energy Impact Partners, where Kann invests, is an investor in ThinkLabs AI, which he discloses in the opening. Routine for this show; noted so that figures describing the company's own models are attributed to the company rather than read as independent measurement."
---

## The question

What actually happens inside a utility's planning and operations functions, and
where could AI change it?

## The answer

The binding problem is not that studies are slow, though they are. It is that
every tool a utility owns reports what is broken and none of them say what to do,
so the fix still comes from one engineer's experience and trial and error. Wong's
claim is that a model taught the physics of the grid can generate solutions
instead of flagging problems, and that the larger prize sits in operations rather
than planning, which is the opposite of what the automation there suggests.

## The argument

Planning is not one activity. It is bulk resource planning, transmission
planning, distribution planning and distributed-energy-resource planning, each
siloed, and inside one large East Coast utility Wong counts roughly a dozen
departments doing transmission planning separately. Every request becomes its own
study, even though connecting a generator and connecting a load run against the
same model of the same grid, and half or more of the effort, especially in
distribution, goes into cleaning scattered data. The analysis is then tuned to a
worst case, the five hours in a year that will be worst over the next decade.
Better practice is moving toward hundreds of representative hours and, as a gold
standard, all 8,760, which is what you need if storage or flexible load is part
of the answer. Then the assumptions change and the whole thing is restudied.
Wong's old line is that planners are always right, because they can blame the
assumptions, and always wrong, because the assumptions are never correct. Kann
asks whether the price is systematic overbuild; Wong half agrees, calling the
grid an engineering marvel for its time that failed to keep up with
digitalization.

The deeper problem is what a study returns. A decades-old simulator reports
congestion and voltage violations, which amounts to a red or yellow light:
restrict access, or build more lines. What to do is left to the planner's
experience. That was survivable while the answer was always more substations,
wires and transformers. Affordability pressure and supply chain lead times have
taken that answer away, so the menu now includes curtailing generation or load,
adding a battery of some size somewhere on some charge schedule, and
reconfiguring switching, several of which are operations decisions a planner does
not own. Against millions of candidate line segments, trial and error cannot
scale. Volume makes it worse: a cluster or large-load transmission study runs six
to nine months and costs roughly a quarter of a million dollars, restudies
compound that, and clustering helps less than it looks because the queue keeps
changing. Distribution studies are simpler and parallelizable, but the data is
worse and the volume far higher.

His answer is deliberately not a large language model. ThinkLabs trains deep
machine learning models at the intersection of the physics equations and the
model itself, so the system learns how power flows and how loads behave under
contingency. The point of the physics is trustworthiness, since the utility
authorizes the interconnection and has to believe a result enough to act on it.
Two properties follow. The models are deterministic, so the same question returns
the same answer and they cannot hallucinate, which is the first objection a
utility would raise. And they are trained per utility on that utility's own data,
with no cross-training, which answers the security objection. The payoff he
emphasizes is not only speed. It is that the model becomes generative: pre-train
across whole ranges of futures, from load growth to renewable penetration to data
center buildout, and inference can propose the upgrades that solve a region
rather than listing what is broken.

Operations is where the episode turns. Kann assumes the ceiling is lower there,
since the grid already looks automated. Wong says the opposite. The automation
that exists is field automation, with substations and generator sites acting on
their own faster than any human could intervene, which is precisely why
reliability is so good. What humans do is alarm management, rules and dispatch,
plus switching plans a week or two out deciding which lines can come out of
service for planned work, and that last one is quietly becoming a crisis, because
a congested grid leaves little room to take anything out of service in order to
upgrade it. The business case today points at planning because interconnection is
the growth engine, but Wong argues the durable value has always been reliability
and workflow efficiency. The missing piece is a feedback loop: nothing learns
from a day's events until a postmortem, and the records never reconcile into one
account of what happened. The same gap explains why planning and operations
barely speak, since study results reach operators, if at all, as a spreadsheet of
fixed criteria. His diagnosis is that no platform
exists that can hold all the planning horizons at once, so utilities have
organized themselves around the limits of their tools.

## What you need to know first

- **Worst-case planning and 8,760.** Utilities have traditionally sized the
system for the handful of worst hours in a year. The alternative is simulating
all 8,760 hours, the only way to evaluate resources whose value depends on
timing, such as batteries or flexible load.
- **Interconnection and energization studies.** The analysis run before
connecting a new generator or load, deciding whether the grid can take it and
what must be upgraded first. On the bulk system these are batched into cluster
studies; on distribution they arrive as individual requests in high volume.
- **Physics-informed, deterministic AI.** A model trained on the equations
governing power flow rather than on text, producing the same output for the same
input every time. The claim is that this is what makes a result usable by the
utility that has to formally authorize a connection.

## Details worth keeping

- Utilities are struggling to find windows to take equipment out of service for
planned work, because a grid planned for worst case and now congested cannot
afford the contingency. If you overload the grid you cannot work on it.
- Short-term forecasts have stopped being reliable, and Wong wants planning and
operations to move from a single crystal-ball future to probabilistic ensembles
with risk-adjusted decisions. He is clear utilities are not there yet.
- Planning runs on at least four horizons that do not connect: 25 to 40 years
out, a medium-term bulk generation view, five to ten years for transmission
expansion (partly set by how long it takes to buy a transformer), and months to
three years for distribution.
- Nobody in planning or operations can say how much a given cable has actually
been used historically, especially in distribution.
- AI's established utility uses are data cleansing, forecasting and retrieval
over manuals and rate filings. Wong positions running the system study itself as
the unclaimed step.
- The records that would support a feedback loop come from supervisory control
systems, phasor measurement units and work orders. They exist separately and,
Wong says, cannot be reconciled into one account of an event.
- Traditional power flow solvers use iterative methods bound by conventional
processors. ThinkLabs is working with Nvidia on running these calculations
natively on graphics processors, which Wong calls still evolving.
- His closing argument is that a data center at this scale is effectively a new
town, so it should be treated as a micro utility rather than a microgrid, with a
responsibility and a capability to reinforce the grid around it.

## Claims worth citing

All figures as stated on 2026-08-20. Performance figures for ThinkLabs' models
come from its CEO and describe the company's own product.

- A cluster or large-load transmission interconnection study takes most utilities
six to nine months and costs roughly a quarter of a million dollars, before any
restudy. (Wong)
- Southern California Edison projects up to 10,000 energization requests per
month, each currently taking 30 to 45 days. (a public study ThinkLabs did with
SCE, cited by Wong)
- Training a power flow model for a system the size of a state, described as a
couple of thousand buses, takes about 10 minutes and roughly $5 of compute, and
yields models over 99.9% accurate across system states, against an unspecified
baseline. (Wong, ThinkLabs)
- Interconnection studies that took nine months run in about 10 minutes or less,
and inference on a full 8,760-hour power flow is sub-second. (Wong, ThinkLabs)
- In a recent example with a large unnamed utility, about 15 minutes generated
more than 10,000 candidate line builds covering a system operator's whole region
for load growth. The transcript garbles this phrase, so the unit counted is worth
checking before quoting. (Wong, ThinkLabs)
- Example pre-training ranges: up to 50% load growth by 2030, half a gigawatt to
20 gigawatts of data centers, and zero to 100% renewable penetration by 2040.
(Wong)
- The grid has enough existing latent capacity to connect the majority, if not
all, of today's data centers, if utilities could find where it is. Stated
explicitly as a belief, with no supporting analysis on air. (Wong)
- Tens of gigawatts of data centers are being planned with behind-the-meter
generation, increasingly as a bridge to a later interconnection. (Kann)

## Where it's contested

- **Kann's premise about operations gets rejected outright.** He suggests the
ceiling for AI is lower in operations because the grid is already automated; Wong
answers that the potential is higher there, because the automation sits in the
field rather than in the decisions, and because the real value is reliability
rather than the growth-driven business case now attracting attention.
- **The company's own numbers carry the argument.** Training cost, accuracy,
study speed and generated solution counts all come from the CEO, describe
ThinkLabs' models, and are not independently verified here. Customers are named
only as large investor-owned utilities. That is normal for the format and worth
remembering before repeating the 99.9% figure.
- **The latent capacity claim is the loosest thing said.** Wong prefaces it as a
personal belief and offers no study behind it. It also points toward the software
he sells, since his remedy is better planning and operations rather than new
capacity.
- **On data center microgrids he refuses a clean answer.** He grants that
behind-the-meter generation relieves an immediate capacity constraint and speeds
time to power, then argues it creates harder problems on the transient and
electromagnetic side whose study would burden utilities further. His summary is
that you might alleviate some constraints and create others.
- **He hedges on how much utilities vary.** The claim that planning assumptions
almost never reach operations comes with the caveat that each utility is
different, and his broader point is framed as a limitation of available tools
rather than a failure by the people using them.
