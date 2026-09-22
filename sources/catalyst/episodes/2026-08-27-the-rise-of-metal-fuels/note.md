---
episode: "The rise of metal fuels"
published: "2026-08-27"
guest: "Richard Wang, co-founder and CEO, Voya Energy"
threads: [metal-fuels, backup-power, data-center-power, long-duration-storage, defense-energy]
source_transcript: "transcript.md"
note_version: 1
disclosure: "EIP portfolio company. Kann discloses on air that EIP incubated Voya and led its seed and Series A. Common for this show; noted so product figures are attributed to the company rather than read as independent measurement."
---

## The question

Diesel generators are universally disliked and nobody has managed to replace
them. Could aluminum do it?

## The answer

Voya's bet is that it can, because aluminum beats diesel on the exact dimensions
that made diesel impossible to displace: it is denser than diesel, it stockpiles
for years, and it cannot catch fire. The most valuable part of the episode is not
the product itself but the diagnosis underneath it, which finally explains why a
technology everyone complains about has survived every attempt to replace it.

## The argument

The setup is the strongest part, because it explains a failure everyone has
observed without understanding. Diesel generators are terrible and ubiquitous:
roughly 170 gigawatts installed in the US alone, over 10,000 in Northern
Virginia, a $30-40 billion annual global market. Users dislike them. Communities
fight them. And nothing has displaced them.

The reason is a combination of properties no alternative matches at once. A
diesel generator is a microgrid in a box needing nothing else. It is remarkably
cheap, roughly $500 to $800 per kilowatt for hardware and about $1,000 with
emissions controls, against far more for turbines or fuel cells. And the fuel
stores enormous energy in a small, stable, unpressurized space, so 48 or 96 hours
of runtime sits in a plastic tank. What the battery world calls very long
duration is trivial for diesel.

That is why the obvious substitutes fail. Natural gas introduces a pipeline
dependency, and pipelines are stressed at precisely the moments the grid is
stressed, so a winter storm threatens both at once. That correlated failure means
gas can never be as provably reliable as fuel physically sitting on site.
Batteries have excellent power quality and instant start but die on duration,
since backup wants 48 hours and batteries get sized for four to eight. And for
equipment running perhaps 50 hours a year, capital cost dominates, which is why
over-engineering the generator makes no economic sense.

Aluminum enters as a way to beat diesel on its own terms. Aluminum exists in
nature bonded to oxygen, and smelting uses large amounts of electricity to break
that bond. The metal therefore carries that energy, and it "wants" to return to
oxide. Let it, in a controlled way, and you recover the energy. Voya does this
electrochemically rather than by burning, using millimeter-scale pellets fed into
cells where ambient oxygen meets an alkaline water-based electrolyte, dissolving
the aluminum and driving electrons through an external circuit. Burning the metal
would produce high-grade heat requiring a steam turbine, which is expensive and
hard to scale. The electrochemical path also inherits two decades of cost
reduction and talent from the battery and fuel cell industries.

The properties that follow are what matter. Aluminum is claimed at roughly twice
diesel's energy density by volume on an electricity-out basis and slightly better
by weight. It is a solid that does not burn, rust or corrode, so it stockpiles
for years and ships on ordinary rail, trucks and bulk carriers with no special
handling. And because nothing in the system is flammable, including the aluminum
hydroxide byproduct, the fire-separation distances and buried tanks that make
diesel installations mostly empty space disappear.

## What you need to know first

- **Energy density.** Energy per unit volume or weight. The reason diesel won and
  the reason batteries cannot do multi-day backup in a reasonable footprint.
- **Metal-air reaction.** Metal reacting with oxygen from ambient air to release
  energy, here captured as electricity directly rather than as heat.
- **Power quality.** How clean and stable the electrical output is. Diesel is poor
  at it, which matters enormously for GPUs and requires extra batteries or
  capacitors to buffer.
- **Common-mode failure.** When your backup fails for the same underlying reason
  your primary system failed. The core argument against pipeline-fed gas backup.

## Details worth keeping

- Diesel's maintenance burden is worse than its reputation suggests. The fuel
  attracts atmospheric moisture and can grow algae, so it must be "polished" every
  few months, and the generators need test runs once or twice a quarter. That is
  substantial overhead for equipment used a handful of hours a year.
- The grid-asset argument is the most interesting secondary claim. That 170
  gigawatts of installed diesel would be enormously valuable as peak capacity, and
  the DOE has pursued emergency rulings to let it run during grid stress. What
  blocks it is air quality runtime limits and community objection. Clean backup
  with no runtime cap would convert an idle fleet into a dispatchable resource
  already paid for by data center operators.
- The claimed two-in-one benefit: because it responds like a battery, it could
  replace both the diesel stack and the lithium buffer that hyperscalers install
  for power quality, in a smaller footprint than either alone.
- The defense case is vivid. Military generators idle badly, running far off peak
  efficiency, and run hot and loud. Wang relays that in Ukraine a diesel generator
  is treated as a homing beacon for drones, spottable on infrared from miles off.
- The fuel strategy deliberately avoids clean scrap. Beverage cans recycle in a
  tight closed loop and displace primary aluminum, which is genuinely useful, so
  Voya says it will not touch those streams. It targets contaminated mixed-alloy
  scrap such as shredded end-of-life vehicles, which is discounted, largely
  decoupled from primary aluminum pricing, and today often landfilled or exported
  cheaply to Asia.
- The long-term vision is the more radical idea: recycle the aluminum hydroxide
  byproduct back through smelting, siting smelters where electricity is
  extraordinarily cheap, and ship the metal to energy-importing regions. That
  makes aluminum a globally transportable energy carrier, a way of moving cheap
  electricity across oceans in solid form.

## Claims worth citing

As of 2026-08-27. Figures about Voya's own product come from the CEO and describe
designed rather than deployed performance, so attribute them to the company. The
diesel market figures are the more broadly quotable ones.

- Roughly 170 gigawatts of diesel generation installed in the US; more than
  10,000 generators in Northern Virginia. (Kann)
- Global market of roughly $30-40 billion annually for generators plus fuel.
  (Wang)
- Diesel generator hardware roughly $500-800 per kilowatt, about $1,000 with
  emissions controls. (Wang)
- Aluminum roughly 2x diesel energy density by volume on an as-converted basis,
  slightly better by weight. (Wang)
- Voya at approximately 100 megawatts per acre in high-density configuration,
  about 4x a diesel installation. (Wang)
- Instant cold start versus 5-10 seconds for diesel. (Wang)
- Defense logistics: roughly 20-30% less mass and about 70% less volume shipped
  versus a typical military diesel generator. (Wang)
- Claimed fuel cost parity with diesel in the US on fully delivered cost, and
  cheaper in Europe and Asia. Explicitly no green premium. (Wang)
- Backup generators at data centers may run only about 100 hours a year. (Wang)
- Only about one operational aluminum smelter remains in the US. (Wang)
- Target of capturing roughly 1-cent-per-kilowatt-hour electricity in metal form
  at favorable global sites. (Wang)

## Where it's contested

- **It's a portfolio company conversation**, disclosed up front, as is routine on
  this show. Kann does put the two standard objections to Wang, why this is
  possible now and where the fuel comes from, and gets substantive answers to
  both.
- **The product claims are design targets, not deployment results.** No
  third-party testing, customer data, installed base or manufacturing timeline
  comes up. That is normal for a company at this stage and worth remembering
  before repeating the cost parity figure as established.
- **The long-term smelting vision is explicitly aspirational.** Closing the loop
  depends on breakthroughs described as things Voya is "working on" and believes
  it can leverage. The near-term scrap strategy and the long-term energy-carrier
  vision should be judged separately, since the second is far more speculative.
- **The diesel diagnosis is the durable part.** Why diesel resists displacement,
  why gas backup carries correlated risk, and why batteries cannot reach multi-day
  duration are all independently useful and not contingent on Voya succeeding.
  That analysis would survive even if this particular company does not.
