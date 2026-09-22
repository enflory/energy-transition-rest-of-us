---
post: "Why does nobody know how much energy AI will consume?"
published: "2025-06-16"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [ai-compute, data-center-power, load-growth, gas-buildout, demand-flexibility]
source_document: "essay.md"
note_version: 1
disclosure: "The supply-side section draws its examples from Energy Impact Partners portfolio companies and names them as such: Elementl Power, GridBeyond and Enchanted Rock. His estimate that enrolled flexible load could at least triple rests on the approach one of them has pioneered."
---

## The question

Why do the analysts watching data centers disagree so widely about how much
electricity those data centers will consume, even a few years out?

## The answer

Because the forecast depends on four unsettled variables at once: how much
demand there will be for AI products and whether selling them pays, how the
algorithms evolve, how much more efficient the hardware gets, and how much
power will realistically be available to consume. Lubershane's own rough
arithmetic yields what he calls his best guess, a hard cap of several hundred
gigawatts available to AI in the United States over twenty years, and he closes
by saying this leaves him where the best forecasters are: he has no idea
whether that is enough.

## The argument

The premise is that AI news has become energy news, and he opens with a day on
which an independent power producer lost a fifth of its market value on news
about a Chinese model. The forecasts that respectable shops publish for data
center demand nonetheless diverge widely, and the divergence itself is shown in
a chart this note cannot read, sourced in its caption to McKinsey, SemiAnalysis
and EPRI. His explanation is structural rather than a complaint about anyone's
method. The answer depends on four variables that are each genuinely open and
that interact: AI demand and profitability, algorithmic evolution, computing
hardware efficiency, and power supply constraints.

On the demand side the two halves point in different directions. Models are
measurably improving, and he finds the newer deep research tools markedly
better than their predecessors, but adoption has not followed at the same rate,
and the business of building frontier models looks financially precarious
because none of the leaders has been able to pull ahead for long. He cites the
investor Gavin Baker's 2023 line about foundation models being the fastest
depreciating assets in history, notes that the theoretical promise of general
intelligence has kept investors hooked anyway, and asks whether they will stay
hooked, answering: who knows. The algorithmic question is sharper. A 2020
OpenAI paper found that model performance improved smoothly with model size,
dataset size and training compute, and for four years the industry scaled all
three together, to the point that the relationship came to be treated as a law
of nature rather than an observation. Around November 2024 reports surfaced
that it was no longer holding, partly because the internet contains a finite
amount of text but mainly through ordinary diminishing returns. The industry's
answer was to spend compute elsewhere, during inference, letting a model work
through steps as it answers. That matters twice over: the most extreme demand
forecasts assume training-style scaling stays the prime mover, and training and
inference want physically different data centers. Training wants one enormous
facility running for months, and because delay does not matter it can sit
wherever power is cheap. Inference is spread across many smaller instances,
some of which must cluster near population centers because they cannot tolerate
delay, while others, such as research-style project work, could run whenever
and wherever is convenient.

Efficiency is the variable with the most impressive record and, he argues, the
least room left. Through the last decade's cloud boom, computing demand soared
while data center energy use barely moved. He quotes his
own earlier writing to explain why that will not repeat: the gain came largely
from moving workloads out of inefficient server closets into hyperscale
facilities, that migration is essentially finished, and further efficiency
inside those facilities has hit hard diminishing returns. Chips are still
improving, but packing transistors closer together now generates enough heat to
overwhelm the efficiency that density used to deliver, which is why the latest
generation doubles the previous one only by switching to liquid cooling. He has
come to see advanced cooling as an enabler of denser racks rather than an
independent lever on consumption. To matter against order-of-magnitude growth a
hardware lever has to be order-of-magnitude, and he sees only two candidates:
chip architecture, which he says is not his area and which happens mostly
behind closed doors at a handful of companies, and photonics, moving data
between chips as light rather than electricity. The photonics turn is the one
to keep. It is pursued to break a memory bottleneck rather than to save energy,
so if it works it may mainly unlock a scale of AI that was otherwise
unreachable, raising total consumption rather than lowering it. He names
Jevons paradox for that outcome.

The fourth variable bounds the other three, because access to power is shaping
up as the strictest constraint on data center development in most regions
through at least the end of the decade. He walks the options in turn. Gas is
the American default for firm capacity and its vendors are reportedly sold out
for years, with manufacturers deliberately cautious about expanding after
over-investing in the early 2000s. Batteries are deploying fast but are
duration limited, so each further tranche needs more hours of storage attached
and probably costs more. Renewables and storage he still sees great potential
in, with unusually big error bars, because the easy locations are scarcer,
costs have risen, cuts to longstanding tax credits in the then-current version
of the Republican party's bill would raise them further, and the supply chains
run through China. Nuclear and geothermal
he is increasingly bullish on, but he puts the timeline to multiple gigawatts
at roughly ten years, which makes them contributors from the mid-2030s rather
than now, and then only, he says, if investment in their long-term growth
continues. Efficiency and load flexibility sit downstream of essentially all of
the transmission and distribution bottlenecks, which is why he says utilities
are already beginning to take them more seriously. Adding it up in what he
labels extremely rough math, he reaches roughly a doubling of American
dispatchable capacity over twenty years, then subtracts the share that must
replace retiring coal and serve electric vehicles, heat pumps and ordinary
economic growth, and lands on a hard cap of several hundred gigawatts for AI.
Whether that is enough is precisely the thing nobody knows, himself included.

## What you need to know first

- **Dispatchable capacity.** In his own footnote, generation that can be
counted on to deliver power, with a high degree of certainty, when called on.
It is the unit his supply arithmetic is denominated in.
- **Training and inference.** Training is the one-off process of building a
model; inference is running the finished model to answer queries. Each implies
a different size, location and operating pattern for the building it runs in.
- **Scaling laws.** Relationships between a model's performance and its inputs
that were observed rather than derived, which is why they can stop holding.
- **Jevons paradox.** The pattern in which making something more efficient
makes it cheaper to use and so increases total consumption of it.

## Details worth keeping

- He names SemiAnalysis as the source he personally finds most credible in this
domain, while using its forecast as one of the diverging three.
- Voices other than his own present-day one run right through the post: the
2020 OpenAI scaling-laws paper, a 2024 memory-wall paper, an unnamed North
American utility chief executive from a closed-door session, single quoted
lines from Gavin Baker and from Eric Schmidt, and three block passages lifted
from Lubershane's own earlier posts.
- The utility executive's line is that flexible demand-side resources are being
considered as a planning resource for the first time, and that the point is no
longer saving energy for its own sake but saving it to accommodate growth.
- Jensen Huang's reaction to reasoning models is reproduced as an image, so
this note can report only that Lubershane calls it enthusiastic.
- Cooling and chip startups named as examples: JetCool, acquired by Flex;
Akash Systems, which puts chips on diamond for its thermal conductivity; Groq,
whose chip targets tenfold more efficient inference; and Xscape Photonics and
Ayer Labs on chip-level photonics.
- Two energy stories he singles out from the year so far are Elementl Power's
agreement with Google to develop three nuclear projects totaling about 1.8
gigawatts, and Fervo Energy drilling a geothermal well three miles deep to 270
degrees Celsius in sixteen days.

## Claims worth citing

All figures as stated on 2025-06-16. Model performance, chip generations,
turbine order books and deployment rates all move fast, so treat every number
here as a mid-2025 reading. The twenty-year capacity figures are his own
scenario, which he labels extremely rough, and not a forecast.

- Constellation Energy Group lost a fifth of its market capitalization
overnight after the Chinese model DeepSeek made waves on January 27.
(Lubershane)
- A year earlier the lowest hallucination rate among leading-edge models was
around 2.5%; multiple models have now achieved below 1%. (Vectara's tracker,
cited by Lubershane)
- Roughly a third of Americans use a generative AI chatbot at least weekly, but
only 10% are daily active users, with very little movement through the second
half of 2024. (Benedict Evans, cited by Lubershane)
- The example he gives of a forecast predicated on training-style scaling
continuing is Eric Schmidt's recent assertion that AI could grow to consume 99%
of total power generation. (Schmidt, cited by Lubershane)
- ChatGPT reportedly consumed more than three times as much energy in its first
thirty days of public use as it took to train the underlying GPT-3 model.
(reported figure, cited by Lubershane)
- Through the last decade, demand for computing in data centers grew nearly
tenfold while data center energy use grew by just 10%. (IEA, cited by
Lubershane)
- The energy efficiency of leading-edge AI chips has been doubling every two
years. (Epoch AI, cited by Lubershane)
- Since roughly the turn of the century, operations per processor have risen
about 10,000 times while bandwidth between chips has grown about 100 times.
(Lubershane, with the supporting chart from Gholami and colleagues, IEEE Micro,
March 2024)
- The US grid has about 950 gigawatts of dispatchable capacity, the vast
majority already spoken for, and most of the US and Canada face elevated risk
of supply shortfalls within four years. (Lubershane, the shortfall risk from
the North American Electric Reliability Corporation's 2024 assessment)
- Gas additions have averaged about 8 gigawatts a year for two decades after a
2002 peak near 50; the Energy Information Administration projects about 15
gigawatts a year from 2026 through 2030, and the big three turbine vendors are
reportedly sold out through at least 2030. (EIA and Lubershane)
- Nearly 13 gigawatts of batteries were installed in the US the year before
publication, and lead times for large transformers and switchgear now exceed
three years. (Lubershane)
- About 20 gigawatts of US load is enrolled in legacy demand response programs,
down from a 25 gigawatt peak in 2016, and he believes new approaches could at
least triple that. (Lubershane)
- His scenario: about 200 gigawatts of gas plus about 150 gigawatts of firm
capacity from renewables, storage and flexibility over ten years, then about
100 gigawatts more gas, 300 of renewables and storage, 150 of nuclear and 50 of
geothermal in the decade after, for roughly 950 gigawatts and a near doubling
of the system. The second decade carries conditions: gas slowing under carbon
policy and perhaps the cost of carbon capture, and the 300 gigawatts of
renewables assuming a major uptick in transmission investment. (Lubershane,
extremely rough math)
- Separately, he puts renewables and storage closer to 50 gigawatts of extra
dispatchable capacity by 2030, against an optimistic case in which they could
rival the scale of new gas, and says the US could easily add more than 10
gigawatts of nuclear a year as it did in the 1970s. (Lubershane)

## Where it's contested

Nobody argues back; the post is one person setting out why a question cannot be
answered, and its hedges are the content rather than decoration.

- **He hedges almost every forward-looking statement.** Whether investors stay
hooked: who knows. How much energy photonics could save: very hard to say. His
gas constraint, his renewables number, his nuclear and geothermal timelines and
his flexibility estimate are all given as beliefs or estimates, and the
renewables figure explicitly carries especially big error bars.
- **He disclaims expertise where it would matter most.** Chip architecture, he
says, is not his area, and he notes that even expert analysts cannot observe it
because the work happens inside a few companies. One of the two levers he says
could change the answer is therefore one nobody outside can assess.
- **He allows that AI investment may be socially valuable and unprofitable at
the same time**, which would resolve the demand variable in a way none of the
forecasts he shows is built around.
- **The scope shifts between halves and is not reconciled.** The demand
question is about AI generally; every supply number is American. The post does
not say what geography the forecasts it opens with cover.
- **The four variables are presented as the full set** and the framing is never
defended. Water, land, capital costs and permitting appear only obliquely
through the supply discussion.
- **His own position is visible in the supply section.** Three of its
illustrations are portfolio companies of his firm, identified as such, and the
tripling of enrolled flexible load is an estimate about the approach one of
them pioneered.
- **The closing admission is the finding.** His own arithmetic leaves him in
the same position as the forecasters whose disagreement the post set out to
explain.
