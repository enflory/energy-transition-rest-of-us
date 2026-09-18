---
episode: "Can AI revolutionize materials discovery?"
published: "2024-09-19"
guest: "Ekin Dogus Cubuk, research scientist working on materials discovery, Google DeepMind"
threads: [ai-applications, materials-discovery, batteries, carbon-capture]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2024-09, with DeepMind's 2023 GNoME paper as the reference point. The structural argument about data and serendipity is durable; any statement about what AI has so far demonstrated is a snapshot and should be rechecked."
---

## The question

Is materials discovery the killer application for artificial intelligence in
climate tech, or is it much harder than it looks?

## The answer

Much harder, on the account of a researcher who does this work at DeepMind: asked
what AI has actually discovered so far, Cubuk says not a whole lot, and widens
the question to note that roughly twenty-five years of physics simulation has put
very few materials into real products either. What computation is plausibly good
at in the near term is optimizing within families of materials we already
understand, not finding genuinely new ones. The constraints he emphasizes are
less about model size than about experimental data, which is scarce, mostly
unlabeled and noisy enough to cap how good the simulations can get, and about
which physics the underlying simulation happens to handle well.

## The argument

Cubuk starts by establishing how much of materials history was luck. Tungsten
became usable as a light bulb filament around 1905 after it was dropped into
liquid mercury by mistake and came out ductile. Lithium-ion storage fell out of
work at Exxon that was aimed at superconductivity. Bardeen's transistor notebooks
show one of the best solid-state physicists who ever lived trying material after
material, with silicon failing, germanium working, then trouble with the glue and
the metal electrode. He is careful that none of this was purely random, since
Bardeen knew the semiconductor would be something like silicon or germanium. But
the pattern sets up the structural problem.

That problem is a contradiction he applies to science and to machine learning
equally: the better you know a system, the more you can keep optimizing it, and
that knowledge does not help you find something different. Expertise in material
A does not get you to C, or even B. Machine learning has the same bias in sharper
form, because accuracy falls off as you move away from the training distribution,
and the materials worth predicting are precisely the ones furthest from what we
already know. His asymmetry is that humans have at least demonstrated paradigm
shifts and AI has not; today's best models are strong on textbook-level work and
weak on the creative jump. So the honest near-term claim is about exploitation
rather than exploration, and he argues that is still worth a lot. Nobody knows,
forty or fifty years on, why high-temperature superconductivity happens in
cuprates. That did not stop researchers who had LBCO from swapping in a similar
element to get YBCO, which was the first superconductor above liquid nitrogen
temperature. Machine learning can plausibly accelerate that substitution search.
It is not positioned to make the leap that put cuprates on the table in the first
place, and Cubuk notes that even the human leap was made on reasoning about
conventional superconductivity that turned out not to transfer well.

The constraint underneath all of this is data. The Inorganic Crystal Structure
Database holds a bit more than 200,000 inorganic crystals, which is nothing
beside internet scale. Simulation can manufacture more, and does: the GNoME work
trained on several million computed points and other groups are now at tens of
millions, with returns that appear to follow a predictable power law in the
amount of data. The trouble is that a crystal structure is not a property. For
most of those 200,000 entries nobody has measured the band gap or the electronic
conductivity, so the labeled set for a given property can fall to a thousand or
two thousand points. The hoped-for path is the one large language models took,
pre-training on abundant low-quality data and fine-tuning on a smaller set of
real measurements, but Cubuk offers that as a maybe rather than a result. Worse
for the near term, he makes a point that is easy to miss: experimental
uncertainty in materials science is usually at the same level as computational
error. That means the labels are too noisy to improve simulations against, which
is a ceiling that no amount of model work removes. It is also why he cannot
imagine eliminating lab work. When Kann suggests the chicken-and-egg version,
that you might need much more lab work up front to train the thing meant to
replace lab work, Cubuk agrees and points to efforts building experimental
synthesis datasets for exactly that reason.

Where the field lands first therefore depends less on AI than on which physics
the underlying simulation handles well. Density functional theory predicts
structural stability better than it predicts electronic properties such as band
gap, which makes optical applications a poor early bet and batteries a good one,
since stability and how fast lithium moves through an electrolyte are the kinds
of question it answers. Catalysis is attractive but the reacting surface is messy
and changes during use. Superconductivity involves quantum interactions the
method may simply not reach. A second filter comes from the product rather than
the physics, and Kann and Cubuk build it together: the problems that fit are
self-contained ones. A solid electrolyte is not a battery and has to work with
the cathode, the anode, the interfaces and the manufacturing line, whereas a
carbon-capture sorbent is closer to being a product by itself, which is Cubuk's
speculation about why so many startups pitch metal-organic frameworks. He adds
that MOFs are not currently very commercially impactful, so those startups are
betting on the future. And there is no AlphaFold moment in sight, because
AlphaFold had a problem the community cared about and an objective, shared
benchmark to be measured on. Materials science does not have one yet, and
building one runs into the noise problem again, which is why the missing
ingredient on his account is clean experimental data at least as much as better
models.

## What you need to know first

- **Density functional theory (DFT).** The standard way to simulate how atoms
  interact quantum-mechanically, fast enough and accurate enough to be used
  almost universally in materials science. Nearly every claim about computational
  materials discovery, AI-driven or not, sits on top of it.
- **Training distribution.** The kind of data a model was trained on. Predictions
  degrade the further you move away from it, which is the technical form of "you
  can optimize what you already know."
- **High-temperature superconductor.** Still extremely cold in human terms; the
  threshold that mattered was operating above liquid nitrogen temperature. A
  room-temperature superconductor remains undiscovered.
- **Metal-organic framework (MOF).** A porous crystalline material that can trap
  gases such as carbon dioxide. The example that recurs because it is nearly a
  standalone product.

## Details worth keeping

- The commercial output of decades of materials simulation is strikingly thin.
  Cubuk names a cathode material, which he thinks came from the Ceder group and
  the Materials Project, now in Duracell batteries, and separately notes that the
  first three-dimensional topological insulators were proposed in a DFT paper. He
  offers little else, and dates the arrival of simulation in the field to the late
  1990s or early 2000s.
- Incumbency is part of why discovery has got harder. Most plastics in use were
  discovered seventy or eighty years ago and have been optimized ever since, so a
  genuinely new one has to beat a heavily refined incumbent rather than a fresh
  idea.
- Materials in use are often the simple ones: pure silicon in transistors, and
  superconductors in MRI machines that are older and simpler than the cuprates.
- Cubuk's own account of why climate-adjacent materials startups cluster on
  carbon capture includes a sociological factor. People at Google who want to
  contribute to materials science usually arrive motivated by climate, so they ask
  how to help carbon capture rather than how to improve ionic conductivity.
- GNoME's stated follow-on goals are finite-temperature stability, which is much
  harder because of entropy effects, finding materials that are not just stable
  but interesting, and using data and machine learning to improve DFT itself,
  whose equations were built to be simple enough for a theorist to write down.
- The scaling behaviour he invokes, more data yielding predictably better results,
  he traces to a Baidu Research paper from around 2016 and says it appears to hold
  for quantum mechanics and materials science too.

## Claims worth citing

All figures as stated on 2024-09-19. Statements about what AI had demonstrated
were explicitly a snapshot of a fast-moving field.

- Asked what AI has discovered that we would not otherwise have, or would have
  taken much longer to get: "not a whole lot." (Cubuk)
- The Inorganic Crystal Structure Database holds a bit more than 200,000
  inorganic crystals. (Cubuk)
- GNoME trained on several million computed data points; other groups have since
  reached about 50 million. (Cubuk)
- For a given property such as band gap or electronic conductivity, the
  experimentally labeled set may be only 1,000 to 2,000 points. (Cubuk)
- Experimental uncertainty in materials science is usually at the same level as
  computational error, so experimental labels are noisier than the accuracy
  simulations are trying to reach. (Cubuk)
- On the prior state of zero-kelvin stability data before GNoME, he gives at most
  48,000 known materials, about 28,000 from computation and 20,000 from earlier
  experiments. The sentence runs the three numbers together and is ambiguous about
  whether 48,000 is the total of the other two; read the transcript before
  quoting. He gives no count of what GNoME itself predicted. (Cubuk)
- One cathode material, probably from the Ceder group and the Materials Project,
  is in Duracell batteries; the first three-dimensional topological insulators
  were proposed in a DFT paper. Offered as the examples that get talked about, not
  as a survey. (Cubuk, hedged)
- Simulation became common in materials science in the late 1990s or early 2000s.
  (Cubuk)
- Most plastics in use were discovered seventy to eighty years ago. (Cubuk)

## Where it's contested

- **The title's question gets a mostly negative answer, from an insider.** The
  deflation comes from a DeepMind researcher describing his own field and his own
  paper, which is the opposite of the usual incentive. Treat his optimism and his
  skepticism as carrying the same weight.
- **Demonstrated versus projected.** Nothing in this episode claims a material
  discovered by machine learning has been made, tested in a device or sold.
  Progress is described as being in useful predictions, and the one commercial
  example given comes from physics simulation rather than modern machine
  learning, and is hedged with "I think."
- **The optimistic path is a hypothesis.** Pre-training on hundreds of millions
  of computed points and fine-tuning on perhaps a hundred thousand experimental
  ones is offered as something that might work. So is the idea that better data
  will let DFT itself be improved.
- **Whether AI can ever make the creative jump is left open.** Cubuk says models
  have not produced a paradigm shift, not that they cannot, and rests the
  distinction on an observation about humans rather than a theory about models.
- **Two of the cleanest formulations are the host's.** Kann proposes both the
  incremental-optimization-versus-novel-discovery split and the idea that
  computation will tune high-temperature superconductors rather than find a
  room-temperature one. Cubuk endorses both, but they originate with Kann, and
  the guest's own framing is more hedged and more domain-by-domain.
- **The startup claims are described, not tested.** Kann characterizes a wave of
  companies promising a black box that outputs the material you need. No company,
  figure or result from that world appears in the episode, and Cubuk's account of
  why they converge on metal-organic frameworks is explicitly his own
  speculation.
