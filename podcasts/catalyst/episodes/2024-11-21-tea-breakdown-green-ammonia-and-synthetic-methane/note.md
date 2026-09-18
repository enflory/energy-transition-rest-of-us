---
episode: "TEA breakdown: green ammonia and synthetic methane"
published: "2024-11-21"
guest: "Greg Thiel, managing director of technology, and Melissa Ball, associate director of technology, Energy Impact Partners"
threads: [techno-economic-analysis, hydrogen, fuels-and-shipping, carbon-capture, heat-and-industry]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2024-11. The thermodynamic and scaling logic is durable, but every dollar figure here rests on 2024 assumptions about electrolyzer performance, electricity, hydrogen, carbon dioxide and natural gas prices."
---

## The question

What would actually have to change for green ammonia and synthetic methane to be
made at a cost anyone would pay?

## The answer

In both cases the answer is hydrogen, and in both cases thermodynamics sets a
floor that no clever process design gets under. Green ammonia is the closer of
the two, with the electricity for the hydrogen alone eating close to half the
target selling price on aggressive assumptions, while synthetic methane is
further out, because even at a hydrogen price nobody has achieved the hydrogen
input alone costs several times what natural gas sells for. Neither is called
impossible, but the remaining paths are narrow: cheap electrons plus cheap
electrolyzer capital for ammonia, and for methane a niche market, an unusually
cheap carbon source, or equipment flexible enough to run only when power is
nearly free.

## The argument

Start with ammonia, and start with operating cost, because that is what sets the
floor. Ball anchors everything to a long-term US selling price of $500 to $600
per ton. Today about 75% of the hydrogen feeding an ammonia plant comes from
steam methane reforming, and that hydrogen step accounts for roughly 80% of
ammonia's greenhouse gas emissions, so the simplest version of green ammonia is
to swap in electrolytic hydrogen and leave the century-old Haber-Bosch process
alone. Now price the swap. Take 50 kilowatt-hours of electricity per kilogram of
hydrogen, which is roughly what a good electrolyzer does and which Kann notes
only a few machines beat, and take two cents per kilowatt-hour, which is cheap
power. That lands at about 20 cents per kilogram of ammonia, or around $210 per
ton: almost half the entire budget, spent on electricity, before a dollar of
capital is amortized. The reason this matters more than it first appears is that
it is not an engineering shortfall anyone can design away. Ball's point is that
the thermodynamics of water electrolysis are what they are: getting the energy
cost down far enough already requires running electrolyzers near the
thermodynamic limit for hydrogen, so there is little headroom left and the burden
shifts onto capital cost, which now has to fit inside the remaining half.

That pressure is what pushes startups toward redesigning Haber-Bosch rather than
just feeding it differently, and the redesigns run into a second constraint. The
two pitches are lower-temperature, lower-pressure synthesis reactors, so the loop
can ramp up and down with renewable output instead of running flat out, and
decentralization, so you stop paying to ship a corrosive, hazardous chemical
around the world. Both answer real problems. Intermittency genuinely costs
something: an electrolyzer running below full capacity forces you to buffer
hydrogen on site, and hydrogen storage runs 30 cents to about $1.20 per kilogram
of hydrogen as compressed gas, which works out to 5 to 20 cents per kilogram of
ammonia. That is large against a $500 to $600 per ton target, and Ball's point is
that it can eclipse the very transport saving decentralization is chasing. The
decentralization prize is real but bounded: transport is roughly 20% to 25% of
the delivered price, and that share is the entire budget a small plant has to
work within. Against it sits the six-tenths rule, the observation that equipment
cost scales as capacity raised to about the 0.6 power. Run that in reverse and
half the capacity costs well more than half as much. Electrolysis cells and
stacks are modular enough to partly escape it; the ammonia synthesis loop and the
air separation unit that supplies the nitrogen are not. So a decentralized plant
has to pay a scaling penalty out of a transport budget that is at most a quarter
of the price.

Synthetic methane is the same arithmetic, harsher. Nothing technical is in the
way: the methanation reaction is over a century old, commercial today in
coal-to-gas plants, with high conversion, high selectivity and mild reactor
conditions. The problem is the bill of materials. Best case you need about half a
kilogram of hydrogen per kilogram of methane. Grant the aspirational $1 per
kilogram hydrogen on the Department of Energy's roadmap, and the hydrogen alone
costs $10 per million British thermal units of gas, against a Henry Hub price
that has spent the past decade mostly in the $2 to $5 range, as low as $1.50 and
spiking near $10. So the cheapest input, priced at a level nobody has reached, is
already two to five times the whole benchmark commodity, and it scales roughly
linearly, so $2 hydrogen means $20 per million BTU. Carbon dioxide matters less
but is not free: best case 2.75 kilograms of carbon dioxide per kilogram of
methane, so even hitting the hoped-for $100 per ton for direct air capture adds
about $6 per million BTU, and today's direct air capture is in the high hundreds
to $1,000 per ton. Before any capital, the product is outside the market.

There is one real lever left, and Thiel is careful about how much it buys. The
whole chain is only around 50% efficient, with losses split roughly evenly
between electrolysis and the methanation step, which throws off a lot of heat.
That split is a hint: high-temperature electrolyzers fed by the methanation heat,
with very tight heat recovery and integration, could recover part of it. But his
verdict on the base case is that it is really hard, and the scope of that verdict
matters. He limits it to run-of-the-mill, high-capacity-factor power-to-gas with
no special markets and no edge cases, and leaves the edge cases explicitly open:
a buyer who will pay in the $20s per million BTU, where Kann notes some very
low-carbon renewable natural gas already sells; an unusually cheap carbon source
such as biogenic point-source capture or biogas upgrading where the carbon
dioxide and methane already arrive mixed; or capital cheap and flexible enough to
grab hours of near-zero or negative-priced power and do something else the rest
of the time. Thiel's summary covers both halves of the episode: what matters is
the hydrogen, then the hydrogen, then the hydrogen. Ball's version for ammonia is
that there is no single miracle. You need cheap electrons and cheap electrolyzer
capital together, and ideally a reactor that could take air directly and let you
delete the nitrogen separation step altogether.

## What you need to know first

- **Techno-economic analysis.** Building up the full cost of making something
  from first principles: the capital equipment spread over its life, plus the
  energy and materials consumed, expressed as a levelized cost per unit of
  output. It is how an investor decides whether a technology can ever be cheap,
  as distinct from whether it works.
- **Haber-Bosch and steam methane reforming.** Haber-Bosch is the century-old
  ammonia process, combining nitrogen and hydrogen at 400 to 500 degrees Celsius
  and 100 to 200 bar. Steam methane reforming is how the hydrogen fed into it is
  usually made, by reacting natural gas with steam; it is the source of most of
  ammonia's emissions.
- **The six-tenths rule.** A chemical engineering rule of thumb: the cost ratio
  between two plant sizes is the capacity ratio raised to roughly the 0.6 power.
  Ten times the capacity costs nowhere near ten times as much, which is why big
  plants win and why building small ones is an uphill fight.
- **MMBtu and Henry Hub.** A million British thermal units is the standard unit
  natural gas is priced in. Henry Hub is the US benchmark price for it, which is
  the number every synthetic methane cost has to be measured against.

## Details worth keeping

- There are only around 300 Haber-Bosch plants in the world, and they make all
  the ammonia for all the fertilizer. They are massive, and the industry trend
  has been toward larger rather than smaller. (Kann)
- The decentralization pitch rests on a comparison that Kann flags as arguable: a
  small plant would not have to beat the factory-gate cost from a world-scale
  Haber-Bosch reactor, only something closer to the delivered price a farmer
  actually pays. That relaxes the constraint, if you accept it.
- The US already has a 2,000-mile ammonia pipeline running from Louisiana to the
  Corn Belt. Ammonia is corrosive and dangerous and needs special handling, which
  is much of why delivered price and production cost diverge.
- Outside the United States the ammonia comparison changes, because the main
  sensitivity for conventional Haber-Bosch is the natural gas price. Where gas is
  expensive, incumbent ammonia is expensive, and distribution can cost more too.
- Novel ammonia reactors come in electrochemical, photochemical and thermochemical
  flavors. All are early; Ball says thermochemical is the furthest along, split
  between simply shrinking conventional high-temperature, high-pressure
  Haber-Bosch and designing genuinely lower-temperature, lower-pressure loops.
- A reactor tolerant of oxygen would help the decentralized case, since oxygen
  can foul catalysts and corrode the synthesis loop. That is on Ball's wish list
  alongside eliminating nitrogen separation.
- The reason e-methane is so attractive despite the economics is that it needs no
  new infrastructure at all. Thiel notes that gas storage is by far the largest
  form of energy storage in existence today.

## Claims worth citing

All figures as stated on 2024-11-21. These are technology screening assumptions
rather than market quotes, and the input prices in particular, for electricity,
hydrogen, carbon dioxide and natural gas, move quickly.

- Long-term US ammonia selling price target of $500 to $600 per ton, used as the
  budget for everything else. (Ball) Kann once says "four to $500" in passing;
  Ball's figure is the one the analysis uses throughout.
- About 75% of the hydrogen feeding ammonia synthesis today comes from steam
  methane reforming, and hydrogen production accounts for around 80% of ammonia's
  greenhouse gas emissions. (Ball)
- At 50 kilowatt-hours per kilogram of hydrogen and two cents per kilowatt-hour,
  electricity for the hydrogen costs about 20 cents per kilogram of ammonia, or
  about $210 per ton, close to half the budget. (Ball) The transcript is muddled
  here; see "Where it's contested" before quoting the number.
- Hydrogen storage costs 30 cents to about $1.20 per kilogram of hydrogen for
  compressed gas, which is 5 to 20 cents per kilogram of ammonia. (Ball, citing a
  couple of unnamed sources)
- Transportation is roughly 20% to 25% of the delivered ammonia price, and is
  therefore the budget available to a decentralized producer. (Ball, from EIP's
  own modeling)
- Haber-Bosch operating conditions: 400 to 500 degrees Celsius, 100 to 200 bar.
  (Ball)
- The six-tenths rule: cost scales as capacity to about the 0.6 power. (Thiel)
- Synthetic methane needs about 0.5 kilograms of hydrogen per kilogram of methane
  in the best case, so $1 per kilogram hydrogen equals $10 per million BTU of gas
  from hydrogen alone. (Thiel)
- Henry Hub over the prior decade: as low as about $1.50 per million BTU, spiking
  close to $10, nominally in a $2 to $4 or $5 range. (Thiel)
- Synthetic methane needs about 2.75 kilograms of carbon dioxide per kilogram of
  methane in the best case, so $100 per ton carbon dioxide adds about $6 per
  million BTU. (Thiel)
- Hard to picture synthetic methane below the $20s or $30s per million BTU, which
  is not far off prices some very low-carbon renewable natural gas already
  fetches. (Kann, with Thiel agreeing the base case is really hard)
- Overall power-to-methane efficiency around 50%, with losses split roughly half
  in electrolysis and half in methanation. (Thiel)

## Where it's contested

- **The central ammonia figure is garbled in the transcript.** Ball first states
  the electricity cost as "about 26 a kilo" of ammonia; Kann reads that as $26
  per kilogram and converts it to roughly $2,600 per ton; Ball then restates it
  as 20 cents per kilogram and $210 per ton. Only the restated pair is internally
  consistent, and it is what the rest of the discussion uses. Quote that one.
- **The key assumptions are acknowledged as aggressive.** Kann says so directly:
  two-cent electricity and 50 kilowatt-hours per kilogram are favorable inputs,
  and the conclusion is that green ammonia struggles even on favorable inputs.
  That strengthens the argument but means the numbers are illustrative, not
  quotations of market prices.
- **Thiel's negative verdict on e-methane is explicitly scoped.** He rules out
  run-of-the-mill, high-uptime power-to-gas with no special markets, and in the
  same breath points to the edge cases where it might work. Reporting the verdict
  without the scope would misstate him.
- **The decentralization value proposition is flagged as debatable by the host.**
  Kann raises the claim that small plants compete against delivered price rather
  than factory-gate cost and says openly that whether that is real is arguable.
- **Ball declines to name a single breakthrough for ammonia.** Asked for one
  miracle, she says she has thought about it and cannot reduce it to one: cheap
  energy and cheap capital are both required, with the air-fed reactor idea as an
  addition rather than a substitute.
- **Both guests work for the host's firm, which has looked at these areas and not
  invested.** Kann states that EIP has made no investment in either category
  because the techno-economics are challenging, while adding "never say never."
  The analysis is a screening view from people who passed, based on the firm's own
  modeling rather than on published studies, and is presented as such.
- **One suggested route out is itself unproven.** Among possible sources of very
  cheap hydrogen Thiel floats geologic hydrogen, offered as a possibility rather
  than an available input.
