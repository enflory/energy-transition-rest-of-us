---
post: "Some \"complete bullshit\" about AI and energy"
published: "2023-07-06"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [ai-compute, ai-applications, data-center-power, materials-discovery]
source_document: "essay.md"
note_version: 1
age_warning: "A July 2023 snapshot taken before GPT-4's specifications were public. Every per-query and per-training figure in it is an estimate of a fast-moving quantity."
disclosure: "The claim that right-sized small models are enough for the energy industry is supported with two companies in his firm's portfolio, eSmart Systems and Urbint, which he names as such. A footnote also says compute efficiency is an area of research interest for the firm."
---

## The question

Would pursuing human-level AI break the energy system, and does the energy
industry actually need models that big?

## The answer

Probably yes and no, in that order, on a calculation he repeatedly labels
speculation. His stated conclusion is that without a paradigm shift in how AI
is built, approaching anything resembling general, human-level intelligence
would probably break the energy system: the training run turns out to be
affordable if compute efficiency keeps improving, but running such a model at
scale is the larger problem. For energy-sector work he sees no evidence that
better AI is the constraint, and expects the payoff from frontier models to
land in fundamental science instead.

## The argument

The post opens on what he admits may be a non-sequitur. Photovoltaic cells turn
sunlight into electricity more than ten times as efficiently as plants turn it
into biomass, which he offers as a reason he is extremely skeptical of
biomass-based energy strategies. The comparison he actually wants is the
opposite one: nature is terrible at capturing energy and extraordinary at
converting it into intelligence. Training a large language model takes hundreds
or thousands of megawatt-hours, while his own estimate for raising a human
brain to the age of 21 is a few, or about twenty if you count the body as
support equipment for the brain. He concludes, at minimum, that the human brain is at least a few
orders of magnitude more efficient as a learning machine than the neural
networks driving current AI.

From there he runs a deliberately crude extrapolation, and flags it before
starting: from here on, he says, his own speculation may also be complete
bullshit. Take the roughly 100 trillion synapses in a human brain, multiply by a
secondhand estimate that one real neuron does the work of about a thousand
artificial ones, and a human-level model would need something like half a
million times the parameters of GPT-3. If compute efficiency flatlined, a single
training run would consume a double-digit share of annual American electricity
demand and tens of billions of dollars of power. Compute efficiency is probably
not going to flatline, he says, so he assumes another tenfold gain over ten
years, which brings the same run down to a couple of billion dollars and a
price he calls very reasonable. The move that matters is that the frightening
number becomes an affordable one on an assumption he footnotes as one he has no
idea how to evaluate.

Then the turn, which is that training was never the interesting constraint. A
trained model can be copied onto unlimited servers for negligible energy, but
using it cannot. On an estimate he borrows, answering a year of Google's query
volume with ChatGPT would take a couple of thousand times the energy GPT-3
consumed in training. He is careful to say he has not found a source confirming
whether compute for using a model scales with parameter count the way training
does; if it does, actually deploying a brain-scale model could absorb much of
civilization's energy. That conditional carries the whole weight of his second
conclusion, which is that absent a paradigm shift in how AI is built,
approaching human-level intelligence would probably break the energy system.

His third conclusion is the one he is best placed to make and the one he states
most plainly: most valuable tasks do not need frontier models. The energy
industry was putting AI to work years before the large-scale era began, and for
most applications there is not even a training dataset large enough to justify
billions of parameters. He offers two companies from his firm's portfolio as
evidence and then generalizes from his own experience: in all his years
observing and investing in startups putting AI into energy operations, he has
never seen a company whose growth was constrained by the AI inside not being
good enough. The stumbles were prosaic, namely missing data, human workflows
that resist automation, and the difficulty of improving on a status quo already
honed by decades of human intelligence. So he admits to being a skeptic that
bigger, better AI changes much for energy or other large industrial operations,
and puts the value of frontier models in fundamental scientific work such as
materials discovery, where he hopes it accelerates the search for next
generation batteries and solar cells. A cheap fine-tuning technique reinforces
the point: one big foundational model can spawn thousands of specialized
descendants without new training runs.

## What you need to know first

- **Parameters.** The adjustable numbers inside a model, used throughout as the
proxy for its size.
- **Training versus using a model.** Training is the one-off run that builds
it; using it is answering queries afterwards. They are separate energy budgets.
- **Low-Rank Adaptation.** A technique for fine-tuning an existing large model
on a new dataset for a specific application, rather than training a new model
from scratch.

## Details worth keeping

- The title comes from Sam Altman calling the rumour that GPT-4 has 500 times
GPT-3's parameters "complete bullshit". Lubershane notes the rumoured figure,
100 trillion, coincides with the number of synapses in a human brain, and then
borrows the phrase for his own arithmetic.
- His illustration of what the brain does cheaply: ten minutes and a negligible
amount of energy to teach a child to fold an origami frog, a prompt to which he
says the model could only answer "N/A".
- BLOOM learned 46 natural human languages and 13 programming languages in its
one training run, which he grants is more than most human brains manage.
- The two portfolio companies are described concretely. eSmart Systems detects
equipment and defects in drone photographs of transmission towers; Urbint
ingests geospatial data to predict where rust will accumulate on gas service
lines, a major risk factor for leaks, and finds predictors of worker safety
incidents.
- The long quotation about cheap fine-tuning is from a leaked internal memo by
an anonymous Google engineer, titled "We have no moat", and is that engineer's
assessment rather than Lubershane's.
- Five numbered footnotes carry most of the sourcing. None of the seven figures
carries evidence the prose leaves out.

## Claims worth citing

All figures as stated on 2023-07-06. Model sizes, per-query energy and
efficiency trends were moving fast at the time and several are explicitly
rumours or secondhand estimates.

- Plants convert about 1 to 2 per cent of solar radiation into chemical energy;
solar photovoltaic cells run at 16 to 22 per cent, which he calls more than ten
times better. (Lubershane)
- Training BLOOM, a 176 billion parameter model, took about 433 megawatt-hours,
enough to power roughly 40 typical US homes for a year; GPT-3 reportedly
required 1.3 gigawatt-hours. (Lubershane)
- Training a human brain to the age of 21 takes about 4 megawatt-hours, or
about 20 including the rest of the body. (Lubershane, offered as his best
estimate)
- Compute efficiency for training, measured in operations per watt, improved
about tenfold over the past ten years. (Lubershane, alongside a chart credited
to Sun et al, July 2020)
- From 2010 to 2018 global data center computing grew more than fivefold while
total data center energy consumption grew about 6 per cent. (Masanet et al,
Energy, February 2020, cited by Lubershane)
- One real human neuron does the work of about 1,000 artificial neurons.
(A paper cited by Lubershane, who credits "Towards Data Science" for finding
and summarizing it and says the neuroscience is above his pay grade)
- A human-level model would therefore need about 100 quadrillion parameters,
500,000 times GPT-3; training one would take 640 terawatt-hours, 16 per cent of
current annual US electricity demand, costing about $25 billion in energy at
$0.04 per kilowatt-hour, falling to about $2.5 billion and 1.6 per cent of US
generation after another assumed tenfold efficiency gain. (Lubershane's own
extrapolation, which he labels speculation)
- Answering Google's few trillion annual queries with ChatGPT would consume a
few terawatt-hours a year, a couple of thousand times GPT-3's training energy
and about an order of magnitude more than Google search consumes, based on
0.002 to 0.003 kilowatt-hours per ChatGPT query against 0.0003 per Google
search reported in 2011. (Estimates from "Towards Data Science" and a 2011 New
York Times report, relied on by Lubershane, who says he has found no definitive
figure for Google's query volume)
- Fine-tuning updates cost about $100 for the most popular model sizes, with
training times under a day the norm. (Anonymous Google engineer's leaked memo,
quoted by Lubershane)

## Where it's contested

Nobody pushes back, but this is an unusually self-undermining piece: the author
labels his own central calculation bullshit twice, once in the title and once
before he performs it.

- **He marks where knowledge ends.** Translating synapses into model parameters
is, he says, more or less where scientific consensus on both human and
artificial intelligence stops, with known and unknown unknowns in between.
- **He concedes the paradigm may be wrong.** He says it is far from established
that building ever more complex layers of interconnected statistical models
leads to general intelligence, and that some very smart people have argued
convincingly that it does not.
- **The assumption that softens the conclusion is the least defended.** The
tenfold future efficiency gain turns an alarming number into a reasonable one,
and his footnote on it says he honestly has no idea how reasonable the
assumption is.
- **The larger claim rests on an acknowledged gap.** Whether the energy cost of
using a model scales with parameter count the way training does is the hinge of
his warning about deployment, and he says he has not found a good source either
way.
- **What he has at stake.** See the disclosure field. The two examples
supporting his claim that small models suffice are companies his firm has
invested in, which he states plainly, and the generalization around them is
drawn from his own experience as an investor rather than from data.
- **One position is offered as a personal call.** His skepticism that bigger AI
matters for energy or large industrial operations is framed as an admission
rather than a finding, and he names the exception he would bet on, fundamental
science such as materials discovery, as a hope.
