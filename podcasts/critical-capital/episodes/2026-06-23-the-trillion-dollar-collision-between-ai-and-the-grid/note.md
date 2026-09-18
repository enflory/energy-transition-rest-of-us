---
episode: "The trillion-dollar collision between AI and the grid"
published: "2026-06-23"
guest: "Varun Sivaram, founder and CEO, Emerald AI; previously an executive at two clean energy developers and a senior advisor at the US State Department"
threads: [data-center-power, demand-flexibility, ai-compute, load-growth, geopolitics]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Can the grid absorb the data centers that AI wants to build, and if the answer
is no, what is the cheapest thing to change?

## The answer

Sivaram's answer is that the constraint is not how much capacity the grid has
but how rigidly that capacity is allocated. Utilities size connections for the
worst hour of the next decade, which leaves a large amount of capacity unused
almost all the time. If AI data centers will accept being flexible for a small
fraction of the year, that unused capacity becomes available immediately. He
argues this is unusual in giving four benefits at once with almost no tradeoff,
which is also the product his company sells.

## The argument

The setup is that two systems built on incompatible assumptions have collided.
The grid is deliberately conservative: a utility studies whether it could serve
you at the single worst moment over the next ten years, and if it could not, you
wait in line while it builds. Data centers arrive from the opposite culture,
wanting a connection now and openly willing to go build their own power if they
do not get one. Sivaram's numbers for the resulting mismatch are 50 gigawatts
wanting to come online in the United States between the recording and 2028
against 25 that can actually be built.

What makes this new rather than a repeat of past load growth is the shape of the
load, not its size. He contrasts it with air conditioning, which added tens of
gigawatts over the second half of the twentieth century but spread thinly and
predictably across the country. Data centers are the opposite: concentrated on
single nodes, with racks that used to draw five or ten kilowatts now drawing
hundreds and heading toward a megawatt each. They are also volatile in a way
ordinary load is not, because a training run can ramp up and down within seconds
or milliseconds, and sensitive enough that a mild disturbance in power quality
can make several of them trip off the grid simultaneously. He cites the North
American reliability watchdog warning that enough such loads could produce a
cascading blackout.

The turn in the argument is that the property making these loads dangerous is
the same property that could make them useful. An AI data center is
electronically controllable in a way a steel mill is not, so its consumption can
be modulated from software without wrecking a process mid-run, and its work can
be moved between sites at the speed of light. That gives two kinds of
flexibility. Temporal flexibility means pausing or slowing work whose timing
does not matter to the customer. Spatial flexibility means moving work to
another location, where the added latency is measured in milliseconds against
response times users already tolerate in seconds. Combine those with an on-site
battery and the load becomes a resource the grid can lean on rather than a
problem it has to absorb. The payoff he claims is a rare absence of tradeoff:
more data centers connected sooner, lower rates because the existing system is
better used instead of triggering expensive upgrades everyone pays for, a more
stable grid, and later in the conversation a fourth, more intermittent renewable
supply integrated by a responsive demand side.

The most interesting move is his argument against the apparently reassuring
alternative. If data centers give up and go off-grid, the intuition is that a
local community is spared: no new load, no rate pressure. Sivaram says this is
exactly backwards and that every local community suffers. The grid loses its
largest and most lucrative customers, and the fixed cost of serving everyone
else gets spread across a smaller base. It is worse for the data centers too,
since building redundant on-site power to grid-quality reliability is expensive
and technically hard. And it raises costs for everybody regardless, because a
wave of islanded projects bids up the same scarce gas generators and switchgear
the public grid needs. So the off-grid path has no winner, which is why he wants
the connection deal made attractive enough that nobody takes it.

## What you need to know first

- **Load flexibility.** A customer agreeing to reduce or shift consumption when
the grid needs it. The economically important part is how rarely it has to
happen: Sivaram's case rests on a small percentage of hours per year, not on
routine curtailment.
- **Stranded or latent capacity.** Grid capacity that physically exists but
cannot be sold, because connections are sized against a worst-case peak that
occurs for a few hours a year. The rest of the time the wires and plants run
below what they could carry.
- **Temporal versus spatial flexibility.** Moving computing work in time, by
pausing or slowing it, versus moving it in space, to a data center somewhere
else. The second is specific to computing; almost no other large electrical load
can relocate its work.
- **Behind-the-meter generation.** Power built on the customer's own site rather
than bought through the grid. It is the off-grid path Sivaram argues against as
a permanent arrangement, though he accepts it as a bridge while a connection is
waited on.

## Details worth keeping

- Emerald AI has run five demonstrations at commercial data centers: Phoenix
with Oracle, Chicago, Virginia, London with National Grid, and Hillsborough,
Oregon. In the London demonstration the site responded within seconds to
stabilize the grid after a lightning strike.
- The commercialization strategy is to build a public track record rather than
argue the theory. Named examples are a program with Silicon Valley Power and
Nvidia, and the Aurora facility in Virginia with Nvidia and Digital Realty,
described as the world's first power-flexible AI factory and expected later in
2026. He says he is getting notes from other utilities asking how to be fast
followers.
- He reports utilities as already convinced rather than resistant. Their own
reasoning, as he relays it, is that off-grid data centers bid up equipment costs
and deprive them of revenue they could spread across their rate base.
- Nvidia's chief executive has publicly endorsed accepting what he calls
imperfect power: enough power almost all the time, with the expectation of
ramping down in rare circumstances.
- The host cites a Quinnipiac poll putting 55% of Americans on the view that AI
will do more harm than good against 34% for more good than harm. Sivaram treats
changing this as urgent and as something proof points rather than arguments will
do.
- Emerald AI was about 17 months old at recording and had just been named to
Time's list of 100 most influential companies. Sivaram says flexibility was
treated as a crackpot idea when the company was founded.

## Claims worth citing

All figures as stated in an episode published 2026-06-23 and recorded some weeks
earlier. Deployment and capacity figures in this area move quickly.

- In the United States, 50 gigawatts of data center demand wants to come online
between now and 2028, and only 25 gigawatts can be built. (Sivaram)
- There are 100 gigawatts or more of latent capacity on existing US grids that
could serve data centers, and more than double that worldwide. Sivaram
attributes the US figure to Tyler Norris at Duke University, not to his own
company. (Norris, cited by Sivaram)
- China will have 400 gigawatts of spare power capacity by 2030 available for AI
data centers. On his account energy is not China's bottleneck, chips are, and
the position is reversed in the United States: not fab-limited in 2030, but
energy-limited on current course. (Sivaram)
- Server racks have gone from 5 to 10 kilowatts each to hundreds of kilowatts,
heading toward a megawatt per rack. (Sivaram)
- Data centers historically represented less than 5% of American electricity
consumption. (Sivaram)
- If 25% or more of American load became flexible, the power system could be
substantially more supplied by clean energy. Stated as a possibility, not a
forecast. (Sivaram)
- Multiple data centers in Northern Virginia have tripped off the grid
simultaneously, and the North American reliability watchdog has warned this
could produce a cascading blackout. (Sivaram)
- Quinnipiac poll: 55% of Americans expect AI to do more harm than good, 34%
more good than harm. (Johnson)

## Where it's contested

The host does not challenge any of this, so what follows is where the argument
is load-bearing and untested rather than where anyone disagreed.

- **The guest sells the solution.** Sivaram founded and runs the company whose
software provides the flexibility the episode argues for, and he says so
plainly, along with describing himself as an AI maximalist and a foreign-policy
realist. The argument is his company's thesis stated by its chief executive. He
does not overclaim its scale, calling Emerald a tiny part of a much larger
ecosystem.
- **One hedge that a summary would lose.** Asked about rate impacts, he says
directly that he does not think data centers have raised costs historically,
while adding that they very well could in future if they keep triggering grid
upgrades. The episode's affordability argument is about a risk ahead, not a
harm already measured.
- **The 100-gigawatt figure is not his.** He credits it to a named outside
researcher. The show notes for this episode present it as his own claim, which
is a reason to work from the transcript.
- **The strongest claim goes unexamined.** He says the number one determinant of
American geopolitical success this century will be how many data centers the
country can build, calls it provocative himself, and raises the obvious
objection, that allied countries could host them instead, before setting it
aside. Nobody presses it.
- **The unwritten condition.** The whole case depends on utilities and
regulators offering a real trade, faster and larger connections in exchange for
flexibility. He is explicit that these inaugural offers do not broadly exist
yet, and names a small number of places he expects them from.
- **Timing.** Sivaram notes on air that the recording precedes release by weeks
and then describes events in the present tense. Date the claims to the
conversation, not to the publication date.
