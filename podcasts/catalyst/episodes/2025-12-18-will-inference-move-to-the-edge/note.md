---
episode: "Will inference move to the edge?"
published: "2025-12-18"
guest: "Dr. Ben Lee, professor of electrical engineering and computer science, University of Pennsylvania; visiting researcher, Google"
threads: [ai-compute, data-center-power, load-growth, interconnection]
source_transcript: "transcript.md"
note_version: 1
---

## The question

How much AI inference will move out of giant centralized data centers into
smaller local ones or onto personal devices, and what would that do to the energy
picture?

## The answer

Lee thinks most of it could move eventually, guessing around 80% of inference
compute runs locally by 2035, almost all of that in edge data centers rather than
on phones. He sees no technical obstacle. But nothing is forcing the move today,
which is why essentially nobody is building for it, and the energy result runs
backwards from the intuition: distributing inference probably raises total AI
energy consumption, because small facilities lose the efficiency of scale.

## The argument

Compute has been consolidating into hyperscale facilities for fifteen to twenty
years for two reasons that predate AI. The first is efficiency: Google's power
usage effectiveness is close to 1.1, about a tenth of a watt of overhead for every
watt reaching the chips, which smaller operators cannot match. The second is
sharing, since hardware bought once and used by many customers is cheaper per
customer. Training then adds a hard technical reason to centralize. A model with
on the order of a trillion parameters is learned by splitting the data across
hundreds of thousands of graphics processing units, each working its own slice,
which then periodically stop and exchange the weights they have learned. That
exchange is expensive enough that the chips must sit close together, which is why
training means thousand-megawatt campuses, and it is also what produces the
violent power swings that make training loads awkward for the grid.

Inference has none of that structure. A prompt is handled by a single graphics
processing unit, or maybe eight inside one machine, because the model, the data
and your prior conversation all live there, and no large group of chips has to
coordinate to answer. Lee says that to his knowledge there is no real technical
penalty for running inference in a small facility. Two arguments push it outward.
The first is latency, and Lee immediately weakens it: before generative AI users
expected a web service to answer in about a hundred milliseconds, but chatbots
have reconditioned people to wait seconds or tens of seconds. What still demands
low latency is cyber-physical AI, meaning robots and autonomous vehicles, where
responsiveness underpins safety. The second argument is power. Kann's thought
experiment asks whether it will stay easier to find one gigawatt-scale site in a
metro area than ten hundred-megawatt sites; both expect that to flip, which would
make distribution the path of least resistance rather than a technical preference.

So why is nobody doing it? Lee's answer is uncertainty about applications. Until
it is clear which AI products drive inference demand, nobody knows the
performance requirements, so nobody commits capital to a network of small sites.
Meanwhile the giant sites have to be built anyway for training, so inference
rides along on capacity that already exists. The existing edge layer is no
shortcut either: content distribution networks and points of presence were
provisioned for central processing units, with power delivery and cooling sized
for far lower density, so converting one is a retrofit rather than a swap. And
there is a scenario where the shift never becomes necessary. If training hits
diminishing returns, or exhausts the available data, the big facilities free up
and inference absorbs the slack, which weakens the case for small sites. The
trigger Lee names for the other branch is commercial, not technical: a provider
competing on performance rather than on capability has to put chips in the market
it wants to win, even with idle ones in Nebraska.

On-device inference is the version that sounds most disruptive and the one Lee
expects least. The advantages are real: responsiveness, privacy, and tight
integration with a platform such as Apple's. The trade is capability. A frontier
model carries on the order of a trillion parameters; a phone-resident model might
carry seven billion, orders of magnitude smaller and correspondingly less
capable, which works only if you have identified a handful of tasks you care
about. Device compute also changes the binding constraint from power to energy,
because what matters is battery life, and adds a thermal ceiling nobody wants in
a pocket. Lee puts the device share on the order of 1%. Which leaves the energy
conclusion, and it inverts the episode's opening premise. Kann asks whether
spreading inference across many smaller facilities would raise total consumption,
since their power usage effectiveness will be worse than a hyperscaler's, and Lee
agrees. Moving inference to the edge does not shrink AI's energy demand; it
relocates that demand into many smaller grid connections and probably increases
the total.

## What you need to know first

- **Training versus inference.** Training is the one-time, enormously expensive
  process of learning a model's parameters from data. Inference is running the
  finished model to answer a query. The two have opposite technical requirements.
- **Power usage effectiveness.** Total facility power divided by the power actually
  reaching the computing hardware. A value of 1.1 means 10% overhead for cooling
  and power delivery, and it is what makes big facilities more efficient per unit
  of compute than small ones.
- **Edge computing.** Compute placed near the user, in the same city or region,
  rather than in a remote campus. It already exists at scale as content
  distribution networks and points of presence.
- **Parameters.** The learned numbers that make up a model, roughly a proxy for its
  size and capability. A phone-sized model is a different product, not the same one
  running slower.

## Details worth keeping

- On the thirds split of AI energy costs, Lee stresses the fractions are evolving
  fast, thinks training growth is plateauing, and says inference costs rising
  sharply is what real adoption would look like.
- The 15-to-50-megawatt Meta facilities are the concrete reference point for what
  "edge" scale would mean, and they were uncontroversial to build. Lee says it is
  unclear where scaling down toward one megawatt stops making sense.
- Kann calls the dummy-workload practice the wildest thing he knows about training
  operations: because the power swings are hard on the grid and on the equipment
  inside the facility, operators sometimes run meaningless workloads to hold the
  power profile flat, burning energy on nothing. Lee notes batteries could smooth
  it but says modulating software is easier, because the control is precise.
- Siting is driven by more than power: redundancy within a region, tax incentives,
  and proximity to internet exchange points for congestion-free data movement. Lee
  cannot cleanly disentangle their weights. Dispersed sites could still be
  resilient without clustering, provided workloads can roll over to spare capacity
  nearby with a similar latency profile.
- Most future inference will be generated by software, not people. Humans are
  bounded by typing speed, while a search engine summarizing pages or an email
  client drafting replies can issue requests far faster. Where those services
  already run in a large data center, their inference can stay there, which cuts
  against the edge case.

## Claims worth citing

All figures as stated on 2025-12-18 and attributed to the speaker. The forecast
figures are explicitly guesses, and deployment in this field moves quickly.

- Google's power usage effectiveness is close to 1.1. (Lee)
- Before generative AI, users expected internet services to respond in roughly 100
  milliseconds. (Lee)
- AI energy costs split roughly in thirds between data pre-processing, training and
  inference. (Meta study Lee worked on, cited by Lee)
- Fifteen Meta data centers studied before generative AI ran 15 to 50 megawatts
  each. (Meta study, cited by Lee)
- Training uses facilities on the order of a thousand megawatts with hundreds of
  thousands of graphics processing units, for models with on the order of a
  trillion parameters. (Lee)
- A single inference prompt is served by one graphics processing unit, or perhaps
  eight within one machine. (Lee)
- A model resident on a consumer device might have around seven billion parameters.
  (Lee)
- Looking to 2035, roughly 80% of inference compute could run locally and 20% in
  cloud data centers, most of the local share at the edge and on the order of 1% on
  consumer devices, with training remaining entirely centralized. Lee gave this
  after being told he would not be held to it, and the base for the 1% is unclear:
  he states it once as a share of the 80% and once with no stated denominator.
  (Lee)
- Distributing inference across smaller facilities would likely raise total AI
  energy consumption, through worse power usage effectiveness and lost economies of
  scale. (Kann proposed it, Lee agreed)

## Where it's contested

- **The headline number is explicitly a guess.** Kann prefaces the question by
  promising not to hold Lee to it, and Lee says his crystal ball is as cloudy as
  anyone else's. It is an informed intuition, not a model output.
- **Kann's restatement drifts from what Lee said, twice.** Lee says the 80% figure
  excludes training entirely; Kann's summary says it includes training. And Lee
  says most of the 80% would be at the edge, which Kann restates as 80% of
  inference being at the edge. Lee corrects neither, so read the claim from Lee's
  own phrasing.
- **The gap between "no technical downside" and "nobody is building it" is never
  closed.** Lee's explanation, that the applications and their performance
  requirements are unknown, is a judgment about commercial uncertainty rather than
  a technical finding. He also raises the branch where the shift never happens: if
  training demand flattens, spare capacity in the biggest facilities absorbs
  inference and the case for small sites weakens.
- **On-device feasibility is opinion.** Lee calls the resource constraints fairly
  significant but not insurmountable, resting on the assumption that models can be
  shrunk without losing performance on the tasks that matter. That is the strategy
  computer scientists are pursuing, not a demonstrated result.
- **The energy conclusion is directional only.** Both agree total consumption would
  go up, neither quantifies it, and Lee's own phrasing is that it "may" go up. The
  premise itself is being tested rather than endorsed: Kann introduces edge
  inference as a narrative he has heard repeatedly and wants to understand.
