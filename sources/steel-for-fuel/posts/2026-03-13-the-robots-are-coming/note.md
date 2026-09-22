---
post: "The robots are coming"
published: "2026-03-13"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [robotics, ai-applications, skilled-labor, construction-and-epc]
source_document: "essay.md"
note_version: 1
disclosure: "Three of the post's examples are his firm's portfolio companies, including the maker of the GridVision inspection software; he names the relationship each time."
---

## The question

Why should anyone building energy infrastructure care about robotics, and how
far has the field actually got?

## The answer

Because in his account the limit on building physical things is physical labor,
and its supply is shrinking while demand for it accelerates. He can see no
plausible route other than putting AI into machines that act on the world, and
says three converging trends have moved the frontier far enough to expect robots
across the economy in many forms. The hardest human jobs, though, stay in his
description very, very far out of reach.

## The argument

The post is openly a partial repost. He is reprising the robotics section of a
piece written about a year earlier, and says two things have changed since: he
is more convinced that robotics specifically is accelerating, enough to call it
one of the century's biggest global trends, and the world appears to him to be
waking up to it, which the earlier piece had complained it was not. The case
itself starts away from robots. Our biggest problems are still mostly material,
so models confined to a screen can address them only obliquely, and across the
economy the bottlenecks are generally not the PhD-level ones language models are
good at. Knowledge work has been made tremendously more productive over
twenty-five years, while labor productivity in manufacturing and construction,
the two sectors that actually shape the physical world, has been flat to
declining for two decades. Demographics compound it. The post-war infrastructure
spree ran on a bumper crop of prime-age workers, and today's pool of young
people with strong backs is shallower, with immigration restrictions shrinking
it further. The squeeze is already visible in energy, where a survey of solar
developers and utilities put labor availability above inflation and
interconnection queues, and where nearly every established trade the transition
depends on is in high demand and projected to grow fast. His conclusion is
framed as an elimination rather than an enthusiasm: he can see only one
plausible option, a leap in physical labor productivity, which means embedding
AI in machines.

How far along that is depends on which job you mean, so he organizes the field
as a spectrum of task difficulty. At the easy end are discrete, repetitive,
fully programmable tasks needing little dexterity, which is what essentially
every robot doing real work today performs: industrial arms in car plants,
electronics and metal fabrication, now numerous and cheap, with China the
largest buyer by far and a domestic industry challenging the leading suppliers
elsewhere. At the hard end sit jobs whose tasks are nearly impossible to pull
apart, vary every time, sometimes involve members of the public rather than
trained handlers, and may demand fine manipulation. His evidence on that last
point is quoted rather than newly argued: the roboticist Brad Porter on the
space of words being constrained where the space of physical interactions is
not, and a block-quoted calculation on the human hand credited to Lubershane
with his colleague Anil Achyuta. His model of the far end is a plumber: an upset
customer with a badly defined problem, a messy crawl space, a system assembled
over decades, a diagnosis from a few observations, then strength and delicacy at
once. We are still very, very far from replacing him.

What has moved, he argues, is everything between those ends, pushed by three
interlocking trends. The first is deployment outside tightly controlled
settings, warehouses being the step past the factory floor, where Amazon's robot
count is rising as its human headcount starts to fall, and drones being a cheap
and versatile testbed that has gone from inspecting energy infrastructure to
helping build it. The second is the arrival of vision-language-action models,
where the point is not the models themselves but the starting position. Five
years ago an autonomous system began as a blank slate and had to gather its own
data about both the world and its own body, which is why Waymo needed six years
to reach its first million autonomous miles and then sixteen months for the
second. Now the world-understanding can be loaded in at the outset and only the
action half has to be learned, which he says cuts years and sometimes billions
out of building a new robotic product. The third is the decade of autonomous
vehicle spending, and here the argument is about spillover rather than cars:
capital went into driving and came out as a cohort of experienced engineers now
founding robotics companies, and as a collapse in the cost of LIDAR sensors,
which he credits to that ecosystem, with batteries, servo motors and chips
cheaper too.

Where he lands is deliberately unspecific about shape. The humanoid thesis is
easy to state, since the world was built by humans for humans and human-shaped
machines can be trained by imitation, and it is very well funded. He concedes
humanoids may prove necessary to reach the plumber end of the spectrum, but says
personally he is not so sure, and would expect more value from a wide range of
purpose-built forms, the way evolution filled different niches with different
bodies. If he is right, what follows is not one robot but a proliferation of
them across the physical economy. That conditional is the post's own framing of
its prediction.

## What you need to know first

- **Vision-language model and vision-language-action model.** The post's own
terms. The first takes in images and text and produces language, which is what
most large models today do. The second adds outputs that drive motors and
actuators, turning comprehension into movement.
- **Proprioception.** The sense of where your own body is positioned. In his
newborn analogy it is what a model with full world-understanding still lacks,
and closing that loop is what makes a robot autonomous rather than merely
knowledgeable.
- **Imitation learning.** Training a robot by recording a human doing the task,
which is part of why a human-shaped machine is attractive.

## Details worth keeping

- Three examples come from his firm's portfolio: RobustAI, whose "Carter" looks
like an ordinary warehouse cart but is built to collaborate with human workers;
GridVision, machine-vision software from a portfolio company for drone
inspection of turbines, solar farms and transmission towers; and Infravision, a
drone-based system for stringing transmission lines.
- He dates the vision-language-action trend to Google's PaLM-E in 2023 and
describes it by quoting Google's own account of feeding raw robot sensor data
into a language model. He adds that the field has a strong open-source current,
which NVIDIA has every incentive to feed.
- Bedrock Robotics, an autonomous construction company founded by a Waymo
alumnus, is his example of talent dispersing out of self-driving.
- Drones got cheap because Chinese manufacturers entered the sector, which is
also what made them a practical playground for autonomy.
- Evidence sits in figures at several points. His five reasons that energy is
hard terrain for a new technology company appear only inside one, so this note
cannot list them, though the prose says all five stem from an industry of big
physical systems and global commodity flows. So do the productivity series, the
survey ranking of developer concerns, and the insurance-claims comparison behind
his claim that Waymo now beats human drivers on safety.

## Claims worth citing

All figures as stated on 2026-03-13. Several are read off charts rather than
derived in the text, and the deployment and component-cost figures move fast.

- US labor productivity in manufacturing and construction has been flat to
declining for the past two decades. (Lubershane, from a US Census total factor
productivity series shown as a chart)
- A 2022 survey of solar developers and utilities found labor availability to be
the group's top concern, ahead of inflation and clogged interconnection queues.
(McKinsey, June 2023, cited by Lubershane)
- Solar installers and wind turbine service technicians are projected to be
among the fastest growing job categories of the next decade at 40-50% compound
annual growth, from a small base; electricians, HVAC technicians and utility
line workers are projected to grow 7-9% a year, more than doubling within ten
years. (US Bureau of Labor Statistics, cited by Lubershane)
- Roughly five million industrial robots are in service globally, mostly in
automotive, electronics and metal fabrication; sales have roughly quintupled
since 2010 and the average price has fallen about 50%, to less than $20,000 an
arm. (Lubershane)
- Amazon began its robotics program with the 2012 acquisition of Kiva Systems
and may soon have more discrete robot workers than human employees. (Lubershane,
citing news reports including a June 2025 Wall Street Journal piece)
- Collapsed to ten positions per joint, the hand's 27 joints still give 10^27
arrangements, against roughly 500,000 words in the Oxford English Dictionary;
the hand also carries about 17,000 touch receptors, roughly 40 per square
centimeter. (quoted passage credited to Lubershane and Anil Achyuta, receptor
count attributed to the National Institutes of Health)
- Waymo has invested about $6 billion against tens of billions more from
competitors, runs in ten cities with plans for over a dozen more, opened to the
public less than three years ago, and holds data on over 200 million autonomous
miles. (Lubershane)
- Over the past decade the cost of LIDAR sensors has fallen more than 90%, servo
motors more than 50%, and GPUs and related microchips more than 95%.
(Lubershane, who gives no separate start date for each)
- Tesla was reportedly hiring workers at nearly $50 an hour to wear motion
capture suits and train its humanoid robots. (reported, cited by Lubershane)
- At least half a dozen well-funded companies are building generalist robotic
foundation models, among them Physical Intelligence and Field AI. (Lubershane)

## Where it's contested

Nobody argues back. This is one person's brief for a trend he invests in, so the
useful content is his own hedges and what he leaves alone.

- **The quoted passages are not his present voice.** The hand arithmetic is a
block quote credited to him and a colleague, carried over from earlier writing;
the dexterity line is Brad Porter's and the model description is Google's. The
present-tense prose keeps the difficulty claim intact and adds only that the
frontier has moved toward it.
- **The revision he states is an upgrade, not a retreat.** A year ago his
complaint was that people were not paying attention; now he says the world is
waking up and that he is more convinced than before, giving the three trends the
post documents as his reason. He walks nothing back.
- **The form factor is explicitly a guess.** On humanoids he says personally he
is not so sure, and the closing prediction is conditioned on "if I'm correct".
- **The load-bearing step is never defended.** He treats robotics as the one
plausible answer to the labor and demographic squeeze without weighing
alternatives, and nothing here says when robots would be cheap or capable enough
to relieve the trades he names.
- **One tension sits unresolved.** He opens by saying the world is waking up to
this phenomenon, and later says he is still shocked at how little the arrival of
self-driving cars has entered everyday conversation.
