---
episode: "What comes after the data center backlash?"
published: "2026-09-03"
guest: "Brian Janous, co-founder and chief commercial officer, Cloverleaf Infrastructure"
threads: [data-center-power, public-opinion, electricity-prices, policy-and-regulation, ai-compute]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Is the backlash against data centers something developers can actually fix, and
if it is not, where does the buildout go instead?

## The answer

Only half of it is fixable. The specific grievances, meaning rate impacts, water
draw, secrecy and who pays for the substation, have a playbook and the better
developers are learning to run it. Underneath them sits a values fight about AI
itself that no individual project can settle. Kann expects it to get worse before
it gets better, largely for electoral reasons, and Janous expects the constraint
to persist into the early 2030s. The escape
routes are weaker than they look, because every version of leaving the grid still
requires someone's permission to build on a specific piece of land.

## The argument

Kann splits the opposition into two issues wearing the same jacket. One is a list
of concrete, negotiable complaints, several well founded, answerable by siting
differently, paying for the upgrade and structuring the tariff so the big load
carries its own cost. The other is not about that data center at all and would
survive a facility that drew half the power and never touched the water table.
Janous traces the first partly to compression: what Quincy, Washington absorbed
over two decades now arrives as an eighteen-month proposal, which invites people
to multiply the water and power numbers, and some of that arithmetic extrapolates
from older cooling designs rather than today's closed loops. But correcting it
does not land, because of the double whammy. A car factory has worse
externalities and still gets a red carpet, since people like cars. Here the
objection is to the building and to what happens inside it, so fixing the
building fixes half the problem.

Why sentiment turned so fast is a puzzle he cannot solve. He reaches for an
inverted Fukushima: nuclear's collapse in public opinion had a meltdown behind
it, and this had none, since the water and power concerns were always true. By
his reading of Politico's monthly polling, perception was steady across both
parties and then fell off a cliff starting around the previous September. His
hope is a catalyst in the other direction, something people actually want AI to
do, but the politics run against it: through the midterms and a presidential
race, candidates compete to brand each other the pro-data-center candidate, and
because it works, others will copy it. Favorable local stories exist, but nobody
with influence will carry them before an election, and neither speaker claims to
know whether a positive catalyst would work even if one arrived.

On prices the two of them hold a distinction rather than collapsing it. Kann
relays a colleague's argument that a data center arriving in your territory today
tends to lower your rates, since that is what the utility deal is designed to do,
while the national buildout simultaneously inflates the price of transformers,
turbines and gas, and therefore everyone's electricity. Janous accepts both
halves and reframes the second: producing more of something usually makes it
cheaper, and prices did not rise across a century of grid expansion, but this
expansion follows a long stretch of no load growth and has to rebuild supply
chains that were allowed to wither. What he does not concede is the causal claim.
Bills are higher, and whether that is because of data centers is "maybe
partially," with pressures that exist regardless doing the rest. His answer is
not to stop growing but to take the short-term pain seriously and aim community
benefits at the specific thing a specific community is hurting about, rather than
writing generic checks that read as a bribe.

The exits mostly fail on one point. Bring-your-own-capacity policies in Texas and
Pennsylvania are worded vaguely enough that nobody knows whether they mean
on-site generation or an obligation to fund new supply. Janous's own version is
the latter, and Cloverleaf is doing it on a project with a small municipal
utility in Oklahoma, sourcing the wind, solar and storage and handing the package
to the utility to serve the data center. If the intent is behind-the-meter
generation instead, he thinks it makes things worse,
because the inflation comes from equipment cost and buying the same equipment for
your own fence line adds to the same pressure, and because islanding forces you
to overbuild. He starts to argue that pulling a large load off the grid also
removes the denominator that spreads costs, then walks himself back: not
negative, just not positive. Kann pushes hardest here, arguing that if grid
connection hits a ceiling, off-grid is the small plausible step because the
country has empty places. Janous does not buy it, because off-grid does not touch
community acceptance; you still have to permit land, and sea and space will stay
marginal. Edge computing is the one he has warmed to, on economics rather than
politics: in a short market the marginal megawatt carries real value, so models
that failed on break-even in an unconstrained world start to pencil, though he
still expects most compute in facilities of 100 megawatts or more.

## What you need to know first

- **Behind the meter.** Generation on the customer's side of the utility meter,
serving the facility directly instead of through the grid. "Bring your own
capacity" is used loosely by policymakers and can mean either this or an
obligation to fund new grid supply, and the ambiguity does a lot of work here.
- **The rate denominator.** Rates roughly reflect the cost of serving everyone
divided by total kilowatt-hours sold, so a very large customer that pays its own
way spreads fixed costs across more sales. That is why removing load from the
grid entirely is not free to other ratepayers.
- **Edge computing.** Many small distributed sites instead of one enormous
campus, more plausible as workloads shift from training toward inference. The
appeal is partly less community friction and partly speed, since small sites can
avoid the long queues for grid interconnection.

## Details worth keeping

- Quincy, Washington is the counterexample Janous returns to: two decades of
steady buildout produced an aquatic center, a new school and a collapse in
unemployment. His point is about pace, not scale.
- Cloverleaf does not sign non-disclosure agreements with government officials.
Janous supports the transparency provisions in Pennsylvania's deal, including no
NDAs and disclosure of the cooling system, while noting that implementation could
either enable good projects or grind everything to a halt.
- Early-stage developers have a transparency problem they cannot solve.
Cloverleaf is asked to name the end user of a project it is developing on spec
and genuinely does not know yet, which reads to communities as evasion.
- Microsoft ran two underwater data center experiments starting around 2016,
ending with a megawatt-scale unit in the North Sea, and it went nowhere at the
time. Janous, who was there, was skeptical of Panthalassa's revival and now says
maybe, while doubting it scales.
- If location genuinely stops mattering, Janous expects compute to leave the
country before it leaves the planet. He calls a pitch to reuse abandoned
industrial sites in Mexico not a bad idea, subject to data sovereignty concerns,
and notes the Middle East looks less attractive than it did.
- Opposition follows the generation too. Kann describes a Texas town hearing
where the fight was mostly about emissions from the gas stacks.
- The edge developer field is already crowded, and Janous expects most of those
teams to fail on execution.

## Claims worth citing

All figures as stated on 2026-09-03. Sentiment polling and project economics in
this market move quickly.

- Quincy, Washington: Microsoft has close to a gigawatt there, built from a first
facility in about 2007; the town has a $15 million aquatic center and a $150
million school, and unemployment fell from roughly 29% to about 6%. Janous flags
that he does not know the exact gigawatt figure and is relaying a recent news
story. (Janous)
- Public perception of data centers was steady across both parties until roughly
the previous September, then declined sharply in monthly surveys. (Politico
polling, cited by Janous)
- A gigawatt data center going fully behind the meter required about 2.6
gigawatts of capacity across generation, batteries and everything else. (a GE
Vernova employee, relayed by Janous)
- Loudoun County is the richest county in the country, has the highest
concentration of data centers, and its property taxes have fallen every year for
a decade. The transcript garbles speaker labels here. (Kann and Janous)
- Large means 100 megawatts or more, and most computation is expected to stay
there; the most capacity-desperate buyers still set a floor around 50 megawatts.
(Janous)
- Microsoft's first underwater unit, off California, was perhaps kilowatt scale
and the second, in the North Sea, megawatt scale. The details are explicitly
uncertain. (Janous)
- Rising power bills are "maybe partially" attributable to data centers, with
general inflationary pressure responsible for the rest. No split is quantified.
(Janous)

## Where it's contested

- **Kann and Janous disagree about where compute goes if grid connection
stalls.** Kann thinks off-grid on cheap empty land is the obvious next step and
the ocean and space are exotic; Janous thinks off-grid barely helps because
community acceptance, not power, is the binding constraint, and is more open to
sea and space than he was. Neither persuades the other.
- **Janous corrects himself on behind-the-meter load.** He first frames removing
a large load from the grid as actively negative for other ratepayers, then
revises to not negative, just not positive. The weaker version is where he lands.
- **Whether facts move anyone is openly doubted.** Janous says communities
respond to full transparency with disbelief or simple dislike, and that the
industry has attacked an emotional problem with data. The proposed fix, a
positive catalyst, is a hope rather than a plan, and he cannot say what it is.
- **The optimism about jobs is labeled as belief.** Janous rejects the AI job
displacement narrative because every prior efficiency gain created prosperity,
while conceding that some technology could in theory be the first exception.
- **Nobody explains the timing.** The central puzzle, why sentiment collapsed
without a triggering event, is raised and left open.
- **Both speakers are participants.** Janous runs a company built on
grid-connected development, the approach he defends against the behind-the-meter
alternative, and Kann invests in the sector.
