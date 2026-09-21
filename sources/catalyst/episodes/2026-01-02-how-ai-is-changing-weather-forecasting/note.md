---
episode: "How AI is changing weather forecasting"
published: "2026-01-02"
guest: "Peter Battaglia, senior director of research, Google DeepMind sustainability program"
threads: [ai-applications, weather-and-forecasting, grid-operations, climate-adaptation]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Everyone assumes AI will improve weather forecasting. Through what mechanism,
exactly, and what would better forecasts actually unlock?

## The answer

The mechanism is narrower and more specific than the framing suggests. AI is
being applied to one half of the forecasting pipeline, the step that turns an
estimate of today's weather into a prediction of tomorrow's, using fairly
ordinary supervised learning whose advantage is that it can connect distant
points in space directly rather than propagating information locally. Battaglia
gives no accuracy figures and says plainly that nobody understands how the
models do what they do. He also argues the binding constraint is data rather
than model architecture, which is awkward, because weather data can only
accumulate at the speed of weather.

## The argument

Start with how forecasting works without AI, because the AI story only occupies
one part of it. The atmosphere is a fluid, fluids are governed by the
Navier-Stokes equations, and those equations are too hard to solve exactly at
planetary scale. So the field approximates them numerically and runs the
approximation on supercomputers, which is what "numerical weather prediction"
means. Battaglia calls the result a triumph: decade on decade the useful horizon
stretched out to ten, twelve, fifteen days. But prediction is only the second
half of the job. The first half is working out what the weather is *right now*,
by fusing satellites, ground stations, balloons and ships into an estimate of
the global state. Because the atmosphere is chaotic, a perfect forecast would
require knowing where every butterfly is, so that estimate is always incomplete
and forecasts are irreducibly probabilistic. That is why your phone says a
chance of rain rather than rain. There is also a third structural feature worth
holding onto: the industry is a pipeline. Public bureaus issue coarse global
forecasts, and a downstream post-processing layer specializes them for
particular places and uses. Machine learning showed up in that post-processing
layer first, sharpening the last mile rather than touching the base forecast.

The current wave targets the prediction half instead, and the method is less
exotic than the branding implies. It is supervised learning: feed the model a
state, train it to produce the next state, then feed its own output back in to
roll the forecast forward step by step. What the newer architectures add is
reach. A convolutional network learns a local operation and stacks layers until
information can cross an image, whereas a transformer, which Battaglia treats as
essentially a graph neural network with connections at any distance, links far
apart points directly. The pointed detail is what they use that reach *for*.
Language models look backward across a long stretch of text because the next
word depends on context from far earlier. Weather does not work that way; it is
Markov, meaning the present state in principle determines the next one, so his
team deliberately does not let the model look far back in time. They spend the
long-range connections on space instead. And that, he suggests, is where the
qualitative difference lives: a traditional simulator resolves a hurricane
strictly locally out of pressure, temperature, wind and moisture, while a model
that can see the whole structure at once appears to treat the hurricane almost
like a macroscopic object sliding across the globe. He hedges that twice, with
"almost like" and with a flat admission that the field does not understand how
the models actually forecast it.

Then the data question, where Kann sets up an intuition the guest partly
overturns. Robotics is starved of training data, but weather should be the
opposite: a long historical record in which every observation is paired with the
measurement that followed. Battaglia agrees the historical record was a
windfall, specifically ERA5, a decades-long reconstruction of Earth's weather
built by the European forecasting centre for climate purposes and not for
machine learning at all, which happened to be almost perfectly shaped for it.
But the record is uneven, because the satellites and stations behind it changed
over the decades, so accuracy degrades as you go back. More importantly, you
cannot make more of it. Weather has to happen before it can be recorded, and
with models stepping in six-hour increments, a day of waiting buys a day of
data. Hence the search for stranger inputs: cheap rooftop weather stations,
doorbell cameras, car thermometers and rain-sensing wipers, even people posting
about the weather, all of which he flags as unproven in quality. His
generalization is that in modern
AI you are always data poor, and he volunteers that he personally doubted
scaling would keep working and was wrong about it.

What this buys is the least settled part of the conversation, because Battaglia
is describing possibilities rather than results. Nothing in the episode
quantifies how much better an AI forecast is. He is proud of his team's tropical
cyclone work and hopes it means earlier and more accurate warnings; he raises
intervening in a wildfire before it escapes control and immediately says that is
not something anyone can do today. On energy he is more concrete about where the
headroom sits: wind and solar operators already forecast weather to decide what
they can sell and at what price, so the gains he expects are further along, in
planning grid operations and in predicting demand, including second-order
effects like humidity raising the energy cost of heating and cooling air. He
also flags the limit on the whole enterprise, which is that improvements come
from better data as much as better models, and nobody knows what the ceiling is
or which new observation would move it. The honest summary is that this episode
establishes a mechanism and a constraint, not a magnitude.

## What you need to know first

- **Numerical weather prediction.** The conventional approach: approximate the
  fluid equations governing the atmosphere and grind them out on a
  supercomputer. It is the incumbent AI is being compared against, and it is
  good, not a strawman.
- **Estimating the current state.** Before anything is predicted, scattered
  observations have to be turned into a picture of the weather everywhere at
  once. Errors here propagate into every forecast, and this half of the pipeline
  is mostly *not* where the AI work has gone so far.
- **Markov.** A process where the present state determines the next one, so
  history adds nothing. Weather is treated as Markov and text is not, which is
  why these models use long-range connections across space rather than across
  time.
- **Transformers and graph neural networks.** Architectures that let any two
  points in the input interact directly, regardless of distance, instead of
  passing information hop by hop through local neighborhoods. Battaglia treats
  the two as near-equivalent and says architecture is not the interesting part
  anymore; data handling and training are.

## Details worth keeping

- Weather has historically been treated as a public good funded by taxes, and
  Battaglia says it is understood to return well on the public dollar. He offers
  no figure and presents it as received wisdom in the field.
- Not all weather is equally hard. Temperature varies smoothly across a map, so
  coarse grids plus interpolation work. Precipitation and wind do not: a
  thunderstorm can sit a few miles from clear sky, and resolving that means
  predicting far more information at a finer scale than many models capture.
- Raw resolution still pays. Battaglia notes the European centre increased the
  spatial resolution of its forecasts within roughly the last decade and the
  forecasts got more accurate.
- The first uses of machine learning in this field were downstream, improving
  the calibration of a specific product such as chance of rain, rather than
  rebuilding the forecast itself.
- ERA5 was the fifth generation of its dataset, originally released covering
  1979 onward and later extended back into the 1960s, at six-hour temporal and
  25-kilometer spatial resolution.
- Battaglia is unusually open about having been wrong: he argued modern AI would
  not keep improving with more data, and says the people who bet on scaling were
  right.
- The show notes reference a model his group launched in November 2025. The
  conversation itself never discusses that model, its results, or any benchmark.

## Claims worth citing

All as stated on 2026-01-02. This conversation is unusual in containing almost
no quantitative claims, and no accuracy or benchmark figures at all, so there is
little here to go stale and also little to cite as evidence of improvement.

- Systematic scientific weather observation dates back roughly 100 to 150 years;
  large government weather agencies emerged roughly 50 years ago. Both
  approximate. (Battaglia)
- The US national weather agency, which he calls NOAA and never spells out, was
  formed in the 1970s, as was the European Center for Medium Range Forecasting,
  which he calls ECMWF. He prefixes both with "I think." (Battaglia)
- Numerical weather prediction now produces useful forecasts 10 to 15 days out.
  (Battaglia)
- The European centre has "the best weather forecast." Stated as his judgment,
  without a metric. (Battaglia)
- ERA5: six-hour time steps, 25-kilometer spatial resolution, covering 1979
  onward and later extended into the 1960s. (Battaglia)
- No cost, market-size, error-rate or forecast-skill numbers appear anywhere in
  the conversation. Any figure attributed to this episode did not come from the
  transcript.

## Where it's contested

- **The guest twice disclaims standing.** He opens by calling himself a
  relative newcomer to weather forecasting who came to it from simulating
  fluids, and asks to be forgiven for errors. Asked how much past improvement
  came from better data versus more compute versus better methods, he says
  outright that he does not know, and that all three contribute.
- **Nobody knows how the models forecast.** The hurricane-as-moving-object
  description is his best account of what the models seem to do, not a
  mechanism anyone has established. Kann restates it as the models having
  "spatial awareness in a way the old models didn't," and Battaglia agrees with
  the phrase and immediately says the field does not understand how they see the
  world. The restatement should not be read as a claim he asserted.
- **Whether weather is a harder problem than language is left open.** Kann
  argues weather is easier in one respect because there is a correct answer,
  unlike the next word in a sentence. Battaglia partly pushes back: the physics
  is deterministic underneath, but because the model cannot see the fine detail,
  from its point of view the process is still random. He calls the comparison an
  opinion question and declines to adjudicate it.
- **The rich-training-data premise gets qualified rather than confirmed.** The
  historical record is real, but degrades in quality going back, cannot be
  expanded faster than real time, and the exotic alternatives he is excited
  about have unknown quality by his own admission.
- **The ceiling is unknown.** He says the field does not know how much a given
  new satellite or station would improve things, and sometimes has to just try
  it.
- **The benefits are aspirations, stated as such.** Wildfire intervention is
  explicitly not currently possible. The grid operations and demand forecasting
  upside is described as headroom he has "a feeling" about and an area barely
  scratched, not a demonstrated result.
