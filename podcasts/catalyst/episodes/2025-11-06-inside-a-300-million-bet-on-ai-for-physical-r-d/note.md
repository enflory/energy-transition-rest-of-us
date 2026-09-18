---
episode: "Inside a $300 million bet on AI for physical R&D"
published: "2025-11-06"
guest: "Ekin Dogus Cubuk, co-founder, Periodic Labs; formerly Google DeepMind"
threads: [ai-compute, venture-and-finance, materials-discovery]
source_transcript: "transcript.md"
note_version: 1
---

## The question

A year ago Cubuk was sober about using AI for materials discovery. What changed
enough in twelve months to justify leaving Google DeepMind and raising $300
million to do it?

## The answer

Two things changed, and neither is the thing that was actually blocking the
field. Reasoning models showed that spending computation at the moment a question
is asked, rather than only during training, buys results beyond what the training
data contains; and robotic high-throughput experimentation became cheap and
standard enough to generate new physical data at volume. The underlying problem,
that machine learning is weakest exactly where science is most valuable, is
explicitly not solved, so the bet is not that AI will reason its way to a
breakthrough but that it can aim a far larger number of physical trials.

## The argument

The sober view a year earlier rested on training data, and that problem is worth
restating precisely because it has not gone away. Machine learning works best on
the distribution it was trained on, while science and technology care almost
exclusively about the opposite: predictions about things unlike anything in the
training set. Language models have the internet to learn from; materials
discovery has something on the order of thousands of data points. Cubuk not only
says this is still true, he speculates that there may be an undiscovered law
bounding how hard out-of-domain discovery is, in the family of thermodynamics or
Landauer's limit on the energy cost of erasing information. He labels that a
guess.

What changed is an opening rather than a fix. Reasoning models demonstrated that
spending compute at inference time improves results, which was the first way he
had seen to invest resources in a direction other than more training data. Those
models then went on to win gold medals in math olympiads and to do well on coding
and physics problems. But Cubuk draws the limit himself, and it is the sharpest
line in the episode: you can practice for a math olympiad by studying previous
years' problems, and you cannot practice discovering the next big theory. He says
plainly that he is not claiming the models are good enough yet. What the results
show is that reasoning over complex problems is improving, which is directional
evidence rather than a solution.

That is why the company is built around a physical laboratory, and why the second
change matters as much as the first. If a model cannot reason its way past its
training set, it has to try things and be wrong often, which is close to how
solid-state chemistry and physics have always worked: many trials, a fair amount
of accident, resting on deep understanding of the system. Robotic experimentation
that mixes powders and liquids and passes samples on for measurement has become
close to commoditized, which makes those trials affordable. The loop is simple:
the model proposes a synthesis recipe or a simulation, runs it itself because
models have become good at tool use, gets back results nobody has seen, and
revises the next step using that plus its prior training and the literature. The
weak link is automated characterization, the step that tells you what you
actually made. Cubuk says that is difficult for AI tools today and that he
expects to improve it quickly, which is a forecast, not a capability they have.

Superconductivity is the flagship target, and he defends the choice on grounds
other than tractability. A discovery pays off before any product exists: it
changes how physicists think, enables experiments that were not possible, and
sits directly under fusion and quantum computing. Chasing it also forces
capabilities valuable in themselves, including automated synthesis, automated
characterization, and predicting high-temperature superconductivity in the
absence of a theory for it; his analogy is that OpenAI and DeepMind were mocked
for prioritizing artificial general intelligence and built a great deal of useful
technology on the way. It has a training virtue too. A critical temperature
measured in a real experiment, meaning the temperature below which a material
conducts with no resistance, is very hard to reward hack in a way a simulated
result is not. And the target is not only room temperature: a higher critical
magnetic field may matter more than temperature for fusion magnets, and a
superconductor ductile enough to be made into devices would matter as well. The
original limitation survives all of this. Cubuk names hypothesis generation as
the thing AI is still not better at than humans, leaving two paths, improving the
models at it or having humans supply hypotheses while AI executes. Periodic is
not prioritizing full automation, and which mix works is, in his words, an
empirical question.

## What you need to know first

- **Out-of-domain generalization.** Making correct predictions about cases unlike
  anything in the training data. Ordinary machine learning is weakest here, and
  it is the only regime that matters for discovery, which is the whole difficulty
  the episode circles.
- **Test-time compute and reasoning models.** Spending computation while
  answering a question rather than only while training. It matters here because
  it is a way to put more resources into a problem without needing more data, and
  data is the resource science does not have.
- **High-throughput experimentation and characterization.** Robotic systems that
  run many small experiments quickly, and the separate measurement step that
  determines what the experiment actually produced. Characterization is the part
  still largely done by people.
- **Reward hacking.** A model finding a way to score well on the objective
  without doing what you wanted. A live risk when the objective is computed in
  simulation, much less of one when it is a physical measurement.

## Details worth keeping

- Kann describes the setup as two frontier laboratories at once, one in the AI
  sense and one in the traditional sense, built to feed each other. Cubuk's
  co-founder is Liam Fedus, one of the co-creators of ChatGPT.
- The cost structure surprised Cubuk. He expected the physical lab to dominate,
  because instruments are real objects, but training models and running
  simulations on GPUs turned out to be the larger line. The raise was sized by
  laying out GPU cost and lab cost and landing on the minimum they thought
  viable.
- The business model is deliberately undecided, in two stages. Near term, sell
  models tuned for physical research to companies already doing it, where
  general-purpose models are limited by firms not wanting proprietary data on a
  public model and by the model never having trained on it. Longer term,
  materials design might become valuable in itself, the way drug design did after
  a period when it looked like a bad business. Kann suspects the services path is
  the smaller prize, and Cubuk does not argue.
- The interdisciplinary case is the most concrete argument for models over
  people. Superconductivity needs world-class solid-state chemistry, including
  kinetically forcing thermodynamically unstable phases into existence, and
  world-class condensed matter physics, and nobody is both. Cubuk describes
  science as a fractal with far more surface between fields than humans have
  worked.
- Scientific data is information-dense in a way raw size hides. An experiment
  producing three floating-point numbers can validate or refute an enormous body
  of simulation, so a small lab dataset may be worth far more than its bytes. He
  thinks this makes synthetic data for science a different problem from what
  frontier labs currently optimize for.
- Periodic rises with the general tide. As models get better at coding,
  simulations get easier and more efficient to run, so improvements at the large
  labs flow through without Periodic doing anything.

## Claims worth citing

All as stated on 2025-11-06. Model capabilities and compute prices move fast, and
everything about Periodic itself is a founder describing a company that has not
published results.

- Periodic Labs raised a $300 million seed round led by Andreessen Horowitz.
  (Kann)
- Since roughly September 2024, reasoning models have won gold medals in math
  olympiads and performed well on coding and physics problems. (Cubuk)
- The training corpus for materials discovery is on the order of thousands of
  data points, against internet scale for language. Kann states the comparison,
  drawing on their earlier conversation, and Cubuk does not dispute it. (Kann)
- Compute, not the physical lab, is the larger share of the company's cost, and
  GPUs have been getting more expensive recently. (Cubuk)
- Robots that mix powders and liquids and hand samples to characterization tools
  are described as quite commoditized; automated characterization is not, and
  Cubuk expects to improve it soon. (Cubuk)
- Cuprate superconductors date from 1985, offered as evidence the field is young
  enough to still have room. (Cubuk)
- A high critical magnetic field may matter more than critical temperature for
  fusion applications. (Cubuk)

## Where it's contested

- **The core problem is explicitly unsolved.** Cubuk calls reasoning models a
  step in a positive direction and immediately adds that he is not saying they
  are good enough. Anyone reporting this episode as "AI cracked the training data
  problem" has it backwards.
- **Hypothesis generation remains a human advantage.** He names it directly as
  something models are not better at, and offers two possible routes without
  claiming either will work.
- **There is no defined objective yet.** Asked what the system is optimizing for,
  he says it is an empirical question, that they are not sure, and that they can
  probably try everything on the list.
- **He does not put odds on room temperature.** Kann asks twice how likely a
  genuine breakthrough is, and Cubuk redirects to other axes of improvement
  rather than answering. He also affirms that you cannot simply reason your way
  to a much better superconductor.
- **The split between lab data and synthetic data three years out is unknown.**
  He says so outright before reasoning about why lab data might be worth more
  than its size suggests.
- **This is a founder describing an unproven program.** No discovery, no
  measurement and no external result is claimed, and the company was months old
  at recording. The framing, timelines and cost structure belong to Periodic
  rather than to the record.
