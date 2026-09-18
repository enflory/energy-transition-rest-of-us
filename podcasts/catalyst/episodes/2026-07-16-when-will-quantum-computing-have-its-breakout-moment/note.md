---
episode: "When will quantum computing have its breakout moment?"
published: "2026-07-16"
guest: "Bob Sorensen, chief analyst for quantum computing, Hyperion Research"
threads: [quantum-computing, materials-discovery, ai-applications, venture-and-finance]
source_transcript: "transcript.md"
note_version: 1
---

## The question

How close is quantum computing to being genuinely useful, and what exactly does
useful look like?

## The answer

Sorensen accepts that a breakout is coming and puts it three to four years out,
but he sources that date to vendor roadmaps and prevailing sector belief rather
than to anything measured, and he reframes the question twice. First, nothing
demonstrated so far counts: the headline results are artificial problems built
to suit quantum hardware, and in at least one case the researchers who ran the
benchmark said so themselves. Second, the near-term risk to the field is
financial rather than technical. There are 85 companies trying to sell quantum
hardware, a shakeout is necessary and coming, and his worry is that it gets
misread as proof the technology failed.

## The argument

Begin with what has actually been shown, because the gap between that and the
capital flowing in is the episode's subject. The idea traces to Feynman in the
1980s: simulating quantum phenomena on a classical machine can be intractable,
taking something like the age of the universe, so build a system that operates
in the quantum realm instead. He scopes the prize carefully: quantum is an
accelerator offering enormous gains on a narrow class of applications that
happen to matter to a lot of people, not a general-purpose replacement for
classical computing. Four decades on, his description of the state of play is
deflationary. Hardware exists that you can kick the tires on, not quite
commercial. No vendor has demonstrated what he would call dramatic performance
gains over a classical counterpart; the work is still toy problems.
And the benchmarks that generate headlines are the specific thing he objects to.
His example is boson sampling, which he explains as simulating a pachinko
machine: tracking how a thousand balls deflect off every pin is classically
intractable, and a quantum system can represent it naturally because photons
branch probabilistically. It was run, years ago, and the people who ran it said
it had no practical application. Worse, one organization claimed a speedup of
ten to the twenty-eighth power on that kind of benchmark and concluded in a blog
post that this proved quantum operates across multiple universes. Sorensen's
retort is that engineers designing aircraft and crash tests do not want to hear
that their compute requires additional universes. So the class of results the
money is responding to is a class he explicitly discounts.

Why the distance from a toy to a tool is years rather than months has two
answers, and the second is the one he thinks is underrated. The hardware answer
is the noisy intermediate-scale era, now ending. Qubits are error-prone enough
that you do not run an algorithm once and read an answer; you run it a thousand
times and hope the correct result dominates the histogram, appearing perhaps 70
or 80 percent of the time. Error correction converts error-prone physical qubits
into error-free logical ones, at a cost: a decade ago it took thousands of
physical qubits to make one logical qubit, and hardware, architecture and
algorithmic advances have been driving that ratio down. The target is roughly a
million physical qubits yielding perhaps thousands of logical ones, which is
where he says real science starts, and company roadmaps put that three to five
years out. The lesson he draws is that a raw qubit count is a poor indicator and
the error-correction scheme is the better one. But then the software answer,
which he thinks is the harder problem. Quantum algorithms are not intuitive to
creatures too large to be quantum, and there is no deep corpus to draw on. His
comparison is the Navier-Stokes equations, nearly two hundred years old and only
useful once machines could run them; quantum has had a fraction of that time,
and beyond Shor's algorithm for breaking current encryption he says there have
not been many landmark applications. The metaphor he borrows, and admires,
is that everyone is building a car in their garage while the algorithms are the
roads, and eventually somebody has to open the door and drive somewhere. He
calls the algorithmic problem the greater hill to climb over the next decade and
adds that it is underfunded by governments and academia. That decade sits
awkwardly beside his three-to-four-year hardware date, and he does not reconcile
the two.

Usefulness sorts into three classes. First, simulating quantum phenomena
directly, where classical methods require so many simplifying assumptions the
results cannot be fully trusted: battery materials, catalyst design including
catalysts for cleaner oil and gas products, protein and molecule design, and
computational chemistry. Second, optimization, which carries an important
wrinkle. Optimization does not have to be perfect to be valuable, so a noisy
machine returning a merely better answer is still worth using where a small
improvement multiplies across a fleet or a workforce. Third and most
speculatively, the standard computational kernels under most simulation
software, such as finite element analysis and computational fluid dynamics,
where he cites a Rolls-Royce experiment that beat what quantum algorithm theory
predicted. What he likes there is the implication that practitioners with
heuristics may outrun the theory, which is how high performance computing always
advanced. Against AI for materials discovery, he lands on complement rather than
substitute: AI is data-driven, bounded by what is known, opaque and
non-reproducible, so a human stays in the loop, while quantum computes from the
physics without needing a large corpus and offers explainability and
reproducibility.

Which brings him to what he is actually worried about, and it is not the
physics. Eighty-five organizations are trying to become quantum hardware
suppliers, more than have ever supplied high performance computers, laptops or
smartphones across the entire histories of those markets. He says flatly that 70
could fail within two years without damaging the sector, because consolidation
is a necessary part of the journey. His fear is interpretation. When five take
down rounds and ten fold, investors conclude something is wrong, governments
that spent billions ask what they got, and end users decline to commit to a
vendor that may not exist in three years. The trajectory of the technology would
be unharmed; the perception would not. His evidence that the capital is
undisciplined is a company he consulted for, cheap and proud of it, that
received a check for several hundred million dollars and whose chief executive
told him there was no plan for it. He adds that the investors he speaks to often
do not understand the technology or its timelines.

## What you need to know first

- **Physical and logical qubits.** A physical qubit is real hardware and makes
  errors constantly. A logical qubit is an error-free unit assembled from many
  physical ones. The ratio between them is the number that matters, and vendor
  headlines quoting thousands of qubits are quoting the error-prone kind.
- **Noisy intermediate-scale quantum, and fault tolerance.** The current era,
  which Sorensen says is ending: machines large enough to be interesting and too
  error-prone to trust, so a program is run many times, in "shots," and the
  answer is whichever result dominates the distribution. Fault-tolerant machines
  are ones that correct errors well enough to give a trustworthy answer despite
  errors occurring constantly underneath.
- **Classically intractable.** A problem a conventional computer cannot finish
  in useful time, in the limiting case not before the universe ends. This is the
  category quantum is aimed at, and the trap is that a problem being
  classically intractable does not make it worth solving.
- **Quantum advantage.** The claim that a quantum machine beat a classical one
  on some task. The whole of Sorensen's skepticism sits here: the claims are
  usually true and usually about tasks constructed to favor quantum hardware.

## Details worth keeping

- The classical alternative is getting brutally expensive, which is part of why
  quantum's trajectory attracts attention. Sorensen puts the most capable
  scientific and engineering machines at $600 million to $700 million apiece
  plus perhaps $200 million to $300 million of electricity over five years, and
  heading toward a billion dollars a system, affordable only to governments and
  a small class of large companies.
- The optimization examples he reaches for are illustrations of classically hard
  problems, not quantum results: scheduling ten thousand airline crew against
  rules about who flies with whom and who has which day off.
- Shor's algorithm, which would break the encryption schemes in general use, is
  one of the two things he credits with starting the field. He says there have
  not been many landmark benchmarks or applications beyond it in recent years.
- The episode dates the field inconsistently: he says it started in the 1980s
  and has progressed over "the last 40 years or so," then later says quantum has
  "only been around for 30 years."
- Kann names an AI-in-the-loop materials discovery company, Periodic Labs,
  searching for a high-temperature or possibly room-temperature superconductor
  using classical computing, as the comparison case for what quantum would have
  to beat or complement.
- Some vendors claim their existing technology already scales to a million
  qubits and that what remains is engineering it into a product. Sorensen
  reports this claim without endorsing it.

## Claims worth citing

All as stated on 2026-07-16. Funding totals, vendor counts and roadmap dates in
this sector move quickly, and several figures below are forecasts or vendor
roadmaps rather than measured results.

- About $12 billion went into quantum startups in the prior year, roughly six
  times the year before, and governments worldwide have committed north of $50
  billion. (Kann, in the opening monologue)
- Google ran an algorithm on its Willow chip about 13,000 times faster than a
  classical supercomputer and called it the first verifiable quantum advantage,
  simulating molecules at 15 atoms and then 28, checked against the lab. This is
  Kann's monologue, and he notes several parties have made comparable claims.
  Later in the conversation he refers to the same announcement as running on the
  Sycamore chip, so the transcript names two different chips. Sorensen is asked
  whether it is meaningful and never answers. (Kann)
- Systems delivering performance gains large enough that a scientist or engineer
  would prefer quantum to classical are about three to four years away. Sorensen
  states this twice and attributes it to the trajectory "most people believe"
  the technology is on. (Sorensen)
- The target is roughly a million physical qubits producing perhaps thousands of
  logical qubits, which company roadmaps put three to five years out. Attributed
  by Sorensen to the roadmaps, not to his own analysis. (company roadmaps, cited
  by Sorensen)
- A decade ago it took thousands of physical qubits to implement a single
  logical qubit; the ratio is falling but he gives no current figure.
  (Sorensen)
- A quantum program is typically run on the order of a thousand times, with the
  hope that the correct answer appears 70% to 80% of the time. Offered as
  illustration rather than a measured rate. (Sorensen)
- There are about 85 organizations aspiring to supply quantum computing
  hardware. Sorensen says he can confidently say 70 could go under within two
  years without affecting the sector's vitality. No methodology is given for
  either number. (Sorensen)
- There have never been 85 suppliers in the entire history of high performance
  computing, nor of laptops, nor of smartphones. (Sorensen)
- Top-end classical scientific computers cost $600 million to $700 million, with
  perhaps $200 million to $300 million of electricity over a five-year life, and
  are heading toward roughly a billion dollars per system. (Sorensen)
- One organization claimed a speedup of 10 to the 28th power on what Sorensen
  calls an arbitrarily non-functional benchmark, and argued in a blog post that
  the result proved quantum computation draws on multiple universes. He cites it
  as an example of misleading marketing. (Sorensen)
- The traveling salesman problem becomes impractical to compute classically
  somewhere above 10 to 20 cities. (Sorensen)
- FedEx cut fleet fuel costs by 20% by routing trucks to minimize left turns,
  some years ago. Prefaced with "I think." This is a classical computing
  anecdote used to show that small optimization gains multiply at scale, not a
  quantum result. (Sorensen)

## Where it's contested

- **The title's premise survives only in a weakened form.** Sorensen does expect
  a breakout, but he resists the idea of a moment, saying explicitly that no
  single activity is a harbinger of the sector's ultimate fortunes. His date is
  sourced to what vendors publish and what the sector believes, not to a
  measurement, and he says so.
- **His two timelines do not agree.** Useful fault-tolerant hardware in three to
  four years, but the algorithmic problem is "probably the greater hill to
  climb" for general applicability over the next decade. Both are his, in the
  same conversation, and he never reconciles them.
- **The step-function question goes unanswered.** Kann asks whether quantum has
  a threshold like fusion's energy break-even, after which the rest is easier,
  or whether progress is an incremental drumbeat. Sorensen answers a different
  question, arguing progress is near exponential rather than linear, and neither
  adopts nor rejects the analogy.
- **Google's result is not evaluated by the guest.** Kann raises the molecular
  simulation announcement directly and asks whether it is meaningful. Sorensen
  says only "Right" and moves to comparing quantum with AI. Nothing in this
  episode should be read as the analyst endorsing or disputing that result.
- **Current advantage claims are called misleading, not wrong.** His position is
  that vendors are producing benchmark claims that are "interesting but somewhat
  confusing," true on their own terms and irrelevant to any compute environment
  anyone uses.
- **Making logical qubits is described loosely.** He calls converting physical
  qubits into logical ones "pretty straightforward," then immediately says there
  is a penalty, which is the ratio that defines the entire hardware problem.
  Read the two together.
- **The host's closing summary flattens the guest.** Kann ends with "this is
  hype cycles, so we're in another one." Sorensen's actual position is narrower
  and more specific: the technology trajectory is not in danger, the coming
  consolidation is necessary and healthy, and the risk is that the shakeout gets
  misread as the equivalent of the late-1980s AI winter, drying up government,
  customer and venture money. The two framings are not the same claim.
- **Kann's physical-to-logical ratio is his own construction.** He proposes
  getting to something like 10,000 physical qubits for 9,000 logical ones as a
  hypothetical. Sorensen does not confirm any such ratio is achievable; he
  answers that progress is happening on hardware, architecture and software at
  once.
- **One view he flags as his own opinion.** That algorithm development is
  underfunded by both government and academia is offered as his judgment, "to my
  mind," not as a finding.
