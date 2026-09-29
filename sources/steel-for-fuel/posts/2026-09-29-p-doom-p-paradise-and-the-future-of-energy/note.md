---
post: "P(doom), p(paradise), and the future of energy"
published: "2026-09-29"
author: "Andy Lubershane, Partner and Head of Research, Energy Impact Partners"
threads: [ai-compute, data-center-power, load-growth, public-opinion]
source_document: "essay.md"
note_version: 1
---

## The question

If demand for AI turns out to be practically unlimited, what actually decides
how much energy it ends up consuming?

## The answer

Supply, not demand. Lubershane now expects demand for cheap AI analytical labor
to be practically unlimited for at least the next decade, so through at least
2030 the binding constraint is power supply, with off-grid projects and newly
emerged public resistance as the main sources of uncertainty. Beyond 2030 he
names computing and algorithmic efficiency as the biggest open questions and
defers them to a future post.

## The argument

The post is a sequel to his piece a year earlier on why nobody knows how much
energy AI will consume, and it reaches the energy question by way of AI risk.
His premise is that AI is a machine for turning electricity into cognitive
capacity, so how useful that capacity is, for good or ill, sets demand for AI
and therefore its pull on the energy system. He sorts the arguments for a
non-zero p(doom) into two paths. The first, which he calls "Superintelligence,
dot dot dot", runs from recursive self-improvement to an intelligence so far
beyond ours that the mechanism of catastrophe is left as an ellipsis. He does
not find it compelling. He accepts some self-improvement as practically
inevitable but calls superintelligence implausible, on the view, quoted from
Francois Chollet via Noah Smith, that intelligence is a conversion ratio from
data to knowledge with an upper bound, not an unbounded quantity like height.
He is careful to say he does not rule it out and that anyone confident about
where this is headed deserves skepticism.

The second path is the one that matters to him, and it is the hinge of the
post. It needs no superintelligence. He lays it out as a narrative others make
and, judging by his first-person asides and summary, largely endorses it: AI
already offers something like "Infinite Analysts," highly capable, amoral,
able to coordinate at machine speed, and far cheaper than people, with costs
still falling fast. His summary is that AI has already obviously lowered the
cost for malign actors to try, with cyberattacks the biggest near-term risk in
his reading. The same logic runs the other way for p(paradise): an army of
analysts pointed at cancer or cheap fusion should lower the cost of trying,
though he is equally skeptical that superintelligence will turn such problems
completely on their heads. His own estimates of both remain very low. What the
exercise prompted was a re-examination of his priors on AI's economic value
and profitability. He concludes that demand for the analysts will be
practically unlimited, and points to his own growing use at work, an
inflection in inference demand around the start of the year that has become a
hockey stick (the OpenRouter data for it is in a chart the note cannot
reproduce), and an enormous gap between what a megawatt-hour is worth to a lab
selling inference and what power costs. Profitability, still in flux under intense
competition, is therefore unlikely to be the limit.

With demand effectively unbounded, the remaining variables set the ceiling. To
2030 he is more convinced than ever that power supply dominates. Forecasts
there have become somewhat tighter, because utilities have largely firmed up
which data centers they will serve and how much they can deliver, leaving
execution risk on gigawatt projects. In his view the biggest remaining error
bar is projects that generate their own power on site as a bridge to a later
grid connection, which are harder to pull off. A new variable has also appeared: public resistance.
He still thinks energy supply is more likely to be the rate-limiting step, but
the two are linked, since opposition can close off sites where power is easy to
get, and opinion of data centers is shaped by their perceived effect on energy.
He expects resistance to push development further from population centers and
perhaps toward off-grid campuses running on solar, batteries and gas, which he
says more and more signs seem to point to as the only way to sustain
exponential growth past 2030, unless efficiency gains cut the need for power.

## What you need to know first

- **p(doom) and p(paradise).** Shorthand for the probability that AI leads to
  human extinction or close to it, and, as he uses the mirror-image term,
  the odds that AI makes major contributions to human prosperity.
- **Recursive self-improvement.** AI developing better AI, which in the first
  path compounds into an accelerating takeoff.
- **Inference.** Running a trained model to answer requests, as distinct from
  training it; the output is sold as tokens.
- **Bridge to power.** A data center that runs its own on-site generation as a
  large microgrid for its first years, intending to connect to the grid later.

## Details worth keeping

- He illustrates the first path with Mickey's enchanted brooms in "The
  Sorcerer's Apprentice" from Fantasia (1940), doing exactly what they were
  told and nearly drowning him, and compares them in passing to a swarm of
  agents that he says breached HuggingFace in July.
- "Infinite Analysts" is framed as a step up from the "infinite interns"
  Benedict Evans described in 2018.
- The would-be users he lists run from nation-states and terrorist groups to
  well-intentioned researchers who cause harm by accident.
- Physical energy bottlenecks give him "some additional comfort," because most
  would-be supervillains will not be able to command very large agent
  operations.
- The four variable sets from his earlier post are laid out in a figure. The
  prose treats demand explicitly and, by implication, power supply and
  computing and algorithmic efficiency; public resistance is the added one.
- As a longtime nuclear supporter, he finds data centers polling worse than
  nuclear "a little bit heartening," but calls it a pyrrhic victory because
  hyperscaler demand is nuclear's best hope of scaling in decades.
- The public-opinion evidence, including a Gallup survey from May 2026 on local
  opposition to AI data centers, sits in figures the note cannot see.
- He closes by telling readers to update their personal cyber strategy.

## Claims worth citing

All figures as stated on 2026-09-29. AI prices and data center forecasts move
quickly.

- The human cost of a set of professional tasks averaged about $25 per task
  against $1-2 for agentic labor. (Carnegie Mellon and Stanford researchers,
  cited by Lubershane; he dates it October 2025, the figure caption November
  2025)
- On complex machine-learning research tasks, eight hours of agentic labor cost
  about $123 against $1,855 for skilled humans, though AI could not yet match
  human performance over longer working periods. (METR, which he describes as
  a nonprofit focused on AI safety, 2024, cited by Lubershane)
- The price of AI inference has fallen by roughly an order of magnitude every
  six months since ChatGPT's public launch. (Lubershane, as a step in the
  Infinite Analysts argument; the supporting chart is uncaptioned)
- AI could make schemes causing mass harm at least 10% easier, maybe 20% or
  more, especially for lower-level actors. (Lubershane, as a step in the
  Infinite Analysts argument: he says exactly how much easier is up for debate,
  but calls the 10% floor hard to deny)
- A megawatt-hour is currently estimated to be worth $12,790 to frontier labs
  selling inference. (Lubershane, from his post of a couple of weeks earlier;
  this post does not name who made the estimate)
- US industrial power prices averaged about $90 per megawatt-hour, so data
  centers could theoretically pay up to 142 times as much. (Lubershane's
  earlier post, quoted as a block in this one; no date is given for the
  average)
- Realistic scenarios put US data center consumption in 2030 at about 8% to 17%
  of total electricity demand, a gap larger than the demand of every household
  air conditioner in the country. (EPRI, which the post names only by acronym;
  "Powering Intelligence," Feb 2026, per a figure caption; cited by
  Lubershane, and the comparison is his)
- Gigawatts of sites in the American Southwest could support hyperscale
  campuses getting around 90% of their power from solar. (Lubershane, from an
  earlier post of his and a December 2024 study by Baranko et al)

## Where it's contested

No one argues back in the post. What it carries instead is a good deal of
flagged uncertainty.

- **His rejection of superintelligence is labeled intuition.** He says so, adds
  that he is not discounting it entirely, and says readers should be skeptical
  of anyone claiming high confidence about where AI is headed, as he is. The
  bounded-intelligence
  view he leans on is Chollet's and Smith's, which he finds "extremely
  convincing" but does not test.
- **The risk estimates are guesses.** He calls the size of AI's uplift to
  malign schemes up for debate, offering 10% as a floor and 20% as a maybe,
  and cybersecurity as the biggest near-term risk is his reading.
- **Demand being unlimited is the load-bearing assumption.** It rests on his own
  experience, one usage chart and a single profitability estimate from his
  earlier post, and he hedges it to "the foreseeable future" and "at least the
  next decade," with profitability still in flux.
- **The supply-versus-resistance ranking is held loosely.** He still believes
  energy supply is more likely the rate-limiting step, but says how far
  resistance will disrupt plans remains to be seen.
- **The long-run question is deferred.** Computing and algorithmic efficiency,
  which he calls the biggest question marks after 2030 and which could negate
  the need for so much power, are left for a future post.
- **His firm has interests in two threads here.** He notes that industrial
  cybersecurity is in Energy Impact Partners' investment scope, naming Dragos
  and Xona, and recommends a white paper on bridge-to-power microgrids from
  ERock, which he identifies as an EIP portfolio company.
