---
episode: "Will AI deliver the promise of a digital grid?"
published: "2024-03-08"
guest: "David Groarke, managing director, Indigo Advisory Group"
threads: [grid-operations, ai-applications, utility-business, ders, venture-and-finance]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2024-03, when large language models were still new to utilities. The structural obstacles described are durable, but the state of deployment, the funding figures and the judgment of what AI can do are two and a half years old."
---

## The question

The last wave of smart grid investment did not deliver what it promised. Is the
current wave of AI in the power sector any different?

## The answer

Somewhat, and less dramatically than the framing suggests. Groarke's view is that
AI is being absorbed into utilities incrementally, against the priorities they
already had, and that the use cases working today are deliberately sited away
from real-time power flow, because grid physics is hard to model and the data is
not granular enough. He picks incremental change over both the pessimistic and
the transformational scenarios, and says plainly that he cannot claim an
enormous new market is emerging because of AI.

## The argument

The honest starting point is that the previous wave mostly did not work. Utilities
spent years installing smart meters, now past 70% penetration in the US, along
with information technology, operational technology and systems to manage
distributed resources, funded through vendor cycles and rate cases. Groarke says
the promises of that first wave of digital infrastructure largely did not prove
out, and offers as evidence that the cost of the infrastructure needed to deliver
power is nearly equal to the cost of generating it. Kann makes the point sharper:
if the objective was to reduce transmission and distribution costs, it failed.
Groarke agrees without qualification and adds that operating expenses are running
up about 14% a year.

What makes this wave different is not a change in the utility but a change in
what arrived on top of it. That failed investment left behind something valuable,
which is years of multimodal training data covering electrical, customer,
weather, gas, visual and text sources. Meanwhile, in Groarke's phrase, AI was
doing press-ups in the background: algorithms got better, handled more tasks and
became more efficient, and the cost of building an application collapsed once
vendors could assemble solutions from open-source frameworks. That inverts the
economics of the last cycle, which was dominated by large platforms,
communications infrastructure and hardware. The sector now wants low-cost
solutions with high returns, and for the first time software of that shape is
available to point at data it already owns.

But the ceiling on how far that goes is physical and institutional, not a
question of ambition. Modeling grid physics accurately is genuinely difficult for
an algorithm, because anything touching power flow has to respect Ohm's law and
Kirchhoff's law while making accurate real-time decisions, and for many such use
cases the data does not exist at the millisecond granularity required. Around
that sit rate-basing, cybersecurity, utility data architectures Groarke calls
among the most complex diagrams you will ever see, sales cycles long enough that
startups give up, half the workforce retiring within ten years, and competition
for capital from transmission buildout. The consequence shows up directly in
which use cases are live. Wildfire and vegetation management works because it is
discrete, uses genuinely new data from cameras, drones, lidar and satellites,
does not touch operations, is not especially political and can be rolled out
quickly. Customer propensity modeling works differently: the smart meter data has
been sitting there for years, and what changed is the ability to disaggregate a
meter signal well enough to detect an electric vehicle charging and act on it,
which is running at utilities including Duke and Southern California Edison.
Substation asset management is where Groarke sees the most mature combination of
information technology, operational technology and AI, and the largest dollars,
since extending transformer life and avoiding downtime is worth a great deal. The
one case that does touch power flow is transmission capacity optimization,
replacing static line ratings with near-real-time sensing, which he calls right
in AI's wheelhouse precisely because it is non-intrusive, though he notes the
regulatory direction is still emerging.

Who builds this is somewhat different from last time, though less than a venture
investor would hope. Groarke's team looked at several hundred deployments and
found that startups tied to them took about $1.5 billion across 80 funding rounds
since 2021, concentrated at the grid edge in distributed energy integration and
electric vehicle charging management, with some enterprise work applying language
models to regulatory documents. Kann tests the figure immediately, pointing out
that venture funding shows startups are being backed, not that they will win, and
Groarke concedes the point. Deeper into core operations it remains the incumbents
making incremental product improvements and acquiring startups along the way.
Then comes the most important sentence in the episode, and it deflates the
premise: Groarke says he cannot claim an enormous new market is emerging because
of AI, that AI is riding the wave of priorities the sector already had, and that
complete reinvention would require policy and business model change rather than
better algorithms. Offered three futures by Kann, he picks the middle one:
incremental change that eventually produces a very automated system, supported by
proven technology and regulatory infrastructure. Full real-time optimization he
considers potentially possible but distant, since today's data is AMI at minutes
to hours, SCADA at seconds to minutes and phasor measurement units at
milliseconds, most analysis happens after the event, and getting there would need
something close to complete nodal visibility.

## What you need to know first

- **Advanced metering infrastructure, or AMI.** Smart meters and the systems that
collect their data. Non-intrusive load monitoring is the technique of
disaggregating a whole-home meter signal into individual devices, which is how a
utility detects an electric vehicle without visiting the house.
- **Power flow and grid physics.** Electricity distributes itself across a
network according to physical laws rather than instructions, so any tool that
controls or predicts it must solve those equations correctly. This is the line
that separates the easy AI use cases from the hard ones.
- **The data ladder.** AMI reports at minutes to hours, supervisory control
systems at seconds to minutes, and phasor measurement units at milliseconds. What
a use case needs from this ladder determines whether it is feasible today.
- **Rate case.** The regulatory proceeding in which a utility gets permission to
recover an investment from customers. It is why utility technology adoption moves
at the speed of regulators rather than of software.

## Details worth keeping

- Groarke's working taxonomy for utilities is capability-based rather than
technology-based: machine learning and predictive analytics, computer vision,
natural language processing, robotics, digital twins, distributed AI embedded at
the edge for sites like remote substations with weak communications, and
explainable AI.
- Explainable AI is the one he flags as strategically important and immature,
because a regulator will need to know how a decision was made before automation
is permitted.
- The wildfire case has real money behind it. PG&E filed a $1.3 billion rate case
tied to wildfires, utilities collectively spend billions a year on vegetation
management, and the fire potential index PG&E built with partners draws on 30
years of historical data sampled several times a day. Against that exposure the
tools are cheap, running to millions over multi-year software and sensor
agreements.
- Substation predictive maintenance runs on vibration, partial discharge, gas and
temperature sensors plus inspection drones and computer vision detecting
corrosion on video feeds, feeding digital twins that go beyond anomaly detection
into scenario modeling.
- The transformer point is the sharpest economic argument in the episode: units
cost from $100,000 to $1 million and lead times are long, so extending their life
has value independent of anything else.
- Electric vehicle detection pays on both sides of the meter, letting a utility
segment customers onto new tariffs and communicate with them more directly, while
also informing where charging and grid infrastructure should be built.
- Workforce turnover is a live constraint rather than a background trend, with
roughly half the workforce retiring within ten years and field technicians
leaving first.

## Claims worth citing

All figures as stated on 2024-03-08. The market and funding figures come from a
Latitude Intelligence report Groarke co-authored that had not yet been published
at the time of recording.

- US smart meter penetration is over 70%. (Groarke)
- The cost of the infrastructure needed to deliver power is nearly equal to the
cost of generating it. (Groarke)
- Operating expenses are up about 14% a year. He does not specify whose, over
what period, or against what baseline, so the number is worth checking before
repeating. (Groarke)
- PG&E had a $1.3 billion rate case in 2022 for wildfires. The sentence attaches
both "that year" and "over a three-year period" to the figure, so what the $1.3
billion covers is ambiguous in the source. (Groarke)
- Utilities collectively spend billions a year on vegetation management.
(Groarke)
- PG&E's fire potential index uses 30 years of historical data sampled several
times a day. (Groarke)
- Predictive maintenance can reduce downtime of critical components by roughly
30% to 50%. Stated without a baseline or a source. (Groarke)
- Transformers cost from about $100,000 to $1 million and have long delivery
times. (Groarke)
- About 50% of the utility workforce will retire in the next 10 years. (Groarke)
- Startups in this space raised about $1.5 billion across 80 funding rounds since
2021, drawn from a review of roughly 350 deployments since 2001. The description
of that deployment sample is garbled in the transcript, so quote the funding
figure rather than the sample definition. (Groarke)
- Data granularity available today: AMI at minutes to hours, SCADA at seconds to
minutes, phasor measurement units at milliseconds. (Groarke)
- Electric vehicle detection through non-intrusive load monitoring is live at
utilities including Duke and Southern California Edison. (Groarke)

## Where it's contested

- **Funding is not traction, and Kann says so.** He interrupts to confirm the
$1.5 billion is venture capital rather than customer revenue, then notes it shows
startups are being funded and nothing about whether they will win. Groarke
agrees, and adds that the journey of a startup in this sector looks different
from other markets.
- **The guest is more deflationary than the host's framing.** Kann's opening
suggests something big is probably there and could be transformative if you look
closely. Groarke's own conclusion is that AI is riding an existing wave of
utility imperatives, that markets are forming around traditional priorities, and
that he cannot say a large new market is emerging because of AI. Where the two
differ, the guest's version is the one the episode actually supports.
- **His forecast carries an internal tension he leaves standing.** He picks
incremental change leading to a system that eventually becomes very automated,
while also saying that a regulator will require an explanation for each decision
and that it therefore could not be fully automated. Both statements are his.
- **The transformational scenario is not ruled out, only deferred.** He calls it
potentially possible with the right investment and technologies, and dates it
with the line that we are a few years away from being a few years away, which is
a hedge rather than a timeline.
- **Several numbers are loose or self-sourced.** The 30% to 50% downtime
reduction has no baseline, the operating expense growth figure has no stated
base, and the funding and deployment figures come from Groarke's own
then-unpublished report. He is also a consultant advising utilities on this
question, which is why the episode is useful on what is deployed and thinner on
independent evidence of results.
