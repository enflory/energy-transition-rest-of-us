---
episode: "The promise and perils of sodium-ion batteries"
published: "2025-02-20"
guest: "Adrian Yao, founder of the STEER battery research program at Stanford; board member and former co-founder and chief technology officer of the lithium-ion manufacturer EnPower"
threads: [batteries, energy-storage, cost-curves, critical-minerals, china]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded February 2025; the cost framework is durable but every dollar figure here is a snapshot of a market that was moving during the recording itself."
---

## The question

What would it actually take for sodium-ion batteries to beat lithium-ion on
cost?

## The answer

Not scale, which is the usual prescription. Sodium's cheaper raw materials
cannot overcome its lower energy density, because the cost of a cell per
kilowatt-hour is the cost of its materials per kilogram multiplied by the
kilograms of material needed per kilowatt-hour. Yao's conclusion is that
sodium-ion beats lithium-ion on cell cost only through research breakthroughs
that raise energy density, or if something breaks in the lithium-ion supply
chain and pushes lithium's cost curve back up; he treats both as live
possibilities, and offers a third route that sidesteps the contest entirely,
competing on total cost of ownership or in a performance niche.

## The argument

Sodium-ion attracts attention for three theoretical reasons, and Yao attaches an
asterisk to each. Kann ranks the supply chain case the most certain of the three
and safety the least; Yao agrees safety carries the biggest asterisk, but he
hedges the supply chain case too, saying the geopolitical advantage holds in
some cases and not in others. The raw spread is striking: soda ash, the sodium
feedstock, runs about $200 a ton against roughly $10,000 a ton for lithium,
which reached something like $60,000 to $80,000 at the 2022 peak. More than 93%
of the world's battery-grade graphite comes from China, which had recently
imposed export controls on it. The drop-in manufacturing case is that a
sodium-ion cell is the same physical sandwich as a lithium-ion one, built on the
same equipment in the same order, so the capital equipment supply chain already
exists. Yao narrows that: a small Chinese cell maker can genuinely switch a
line, but a dedicated factory at the 10 to 35 gigawatt-hour scale is designed
around a single product and, he says, you are most likely not going to
experiment much at that scale. So the honest version is that a greenfield
sodium-ion plant is a smaller leap than a genuinely novel chemistry, not that
gigafactories get retrofitted. Safety gets the largest asterisk of all.
A blanket claim that sodium-ion is safer is, in Yao's words, objectively wrong,
because safety tracks the specific cathode chemistry rather than the ion.

Kann then says what he thinks of all three, which is that none of them matter
except through cost, and the rest of the conversation is about cost. Yao's frame
is an identity. Dollars per kilowatt-hour equals dollars per kilogram of
material times kilograms of material per kilowatt-hour, and the industry
celebrates sodium's advantage on the first term in the same breath as admitting
its disadvantage on the second, without multiplying the two together. The
multiplication is unforgiving. His illustration: suppose it costs $3 a kilogram
to manufacture LFP cathode powder and the minerals add $2, so $5 a kilogram, and
that kilogram yields about 500 watt-hours. That is $10 per kilowatt-hour of
material. Now take a sodium equivalent that costs the same $3 a kilogram to make
but yields only 250 watt-hours. Even with its minerals free, it lands at $12.
Cheap inputs lose to a bad denominator.

The same arithmetic explains where lithium-ion's cost decline actually came
from. Yao puts lithium-ion's thirty-year learning rate around 20% to 22%, and
says the larger share of it came from better cell design, meaning less inactive
material per kilowatt-hour, rather than from cheaper inputs; lithium itself is
only about 7% of a lithium-ion cell by mass. So when Kann asks whether
sodium-ion is simply early on the same curve and needs scale, Yao says no,
flatly. Scaling today's sodium chemistries scales today's materials intensity.
The investment has to go into energy density instead, which he frames as the one
piece of good news, since a developer is not trapped in the usual
chicken-and-egg where low cost requires scale and scale requires low cost. The
catch is that raising energy density far enough needs materials research and not
only cell engineering. The most promising configuration he models is an
anode-free sodium cell, which could reach $40 to $50 per kilowatt-hour and cross
the line where LFP sits, but only if the underlying cathode capacity and
anode-free plating both work out.

Kann then puts the uncomfortable version to him: a decade of research to arrive
at roughly where LFP already is, an outcome that assumes LFP stops falling,
which Kann flags as an unsafe assumption given that lithium-ion costs have kept
surprising to the downside. Yao does not dispute the arithmetic. He offers two
answers instead. The first is
that the lithium-ion curve may bend upward rather than sodium's bending down,
with the graphite export controls the live candidate; their modelling shows a
lithium-ion price shock genuinely accelerates the crossover, though he is clear
that this is a kink in LFP's curve and not progress on sodium's. The second is
to stop competing on cell cost at all, either on total cost of ownership, where
a safety or cycle-life advantage lowers system-level capital cost, or by finding
a performance niche, and he says US companies are currently split across all
three strategies. On whether China is about to settle the question he is
deliberately unsure: the builders today are tier-two and tier-three players, the
ones to watch are the tier-one manufacturers CATL and BYD, and CATL's chairman
and chief executive had publicly said he expects sodium-ion to take up to half
of LFP's market. Yao's own read, which he sources
to the grapevine rather than to evidence, is that the announcement may function
partly as leverage to keep lithium prices low.

## What you need to know first

- **Dollars per kilowatt-hour, and its two factors.** The battery industry's
  headline cost metric. Yao splits it into dollars per kilogram of material and
  kilograms of material per kilowatt-hour delivered, and almost every turn in
  the argument is about which of those two a given change moves.
- **Energy density and materials intensity.** Energy density is how much energy
  a given mass or volume stores; materials intensity is effectively its inverse,
  the kilograms you need per kilowatt-hour. Sodium is inherently worse here for
  atomic reasons, and that is the part scale does not fix.
- **The chemistry families.** Lithium-ion splits into nickel-based cells (NMC,
  higher energy density) and iron-phosphate cells (LFP, cheaper and safer).
  Sodium-ion has parallels: layered oxides (NFM), iron-based pyrophosphates
  (NFPP), and Prussian blue, which is low energy but high power. The negative
  electrode differs too, since graphite is chemically incompatible with sodium
  and hard carbon is used instead.
- **Anode-free.** A cell built with no dedicated negative-electrode material at
  all, where the metal plates directly onto the current collector on charge.
  Removing that material removes its cost and its weight, which is why it is the
  cheapest configuration Yao models and also the least proven.

## Details worth keeping

- The sandwich analogy runs through the whole episode: two electrodes as slices
  of bread, the separator as lettuce, the electrolyte as soup. Sodium-ion is the
  same sandwich with different fillings.
- Sodium-ion's negative current collector can be aluminum where lithium-ion
  requires copper, which is lighter and cheaper and also allows cells to be
  shipped fully discharged at zero volts, cutting thermal runaway risk in
  transit. Yao notes the benefit is unproven in practice: most sodium cells
  shipped commercially in China today are not shipped at zero volts, and he does
  not know whether that reflects a cycle-life problem, mere habit, or a lack of
  confidence.
- Kann adds a supply chain point Yao accepts: lithium mining sits mostly in
  South America and Australia but lithium refining is almost exclusively in
  China, so a sodium refining chain could be stood up domestically from scratch.
  Yao later turns this around, noting China refines most of the world's lithium
  while holding little in its own ground, so the West arguably controls the
  source and sodium may be as much a geopolitical hedge for China as an economic
  bet.
- CATL's 2021 sodium-ion announcement landed shortly before the lithium price
  spike, and Yao says the company weathered that spike decently well on
  long-term contracts. He raises but does not answer whether having the
  alternative in hand was part of how it did so.
- Yao's explanation for why China is hard to read: there, many players build
  first and evaluate later, and many die; in the West the evaluation comes first
  and often ends in not building. That asymmetry is why an announcement count
  out of China is weak evidence about economics.

## Claims worth citing

All figures as stated on 2025-02-20. Cell and lithium prices move fast enough
that Yao revises one of his own figures mid-sentence; treat every dollar here as
a February 2025 snapshot rather than a current number.

- Soda ash roughly $200 per ton, against roughly $10,000 per ton for lithium at
  the time and $60,000 to $80,000 at the 2022 peak. (Yao)
- More than 93% of the world's battery-grade graphite comes from China, with
  export controls imposed a couple of months before the recording. (Yao)
- LFP cells reported at about $56 per kilowatt-hour in mid-2024, down to
  "40-something, sub-50" by the time of recording. (Yao)
- A modeled lithium-ion floor around $35 per kilowatt-hour on a
  bill-of-materials basis with manufacturing cost excluded, which he says is
  reachable today. The exchange gets
  tangled over whether 35 refers to sodium or lithium; Yao confirms lithium-ion.
  (Yao)
- Sodium-ion cells above $80 per kilowatt-hour for layered-oxide (NFM)
  chemistries, and possibly higher for the pyrophosphates. Kann later restates
  this as "might be 85 bucks" and Yao does not correct him; the figure Yao
  actually gave is "above $80." (Yao)
- Anode-free sodium-ion modeled at roughly $40 to $50 per kilowatt-hour,
  conditional on materials breakthroughs in both cathode capacity and anode-free
  operation. (Nature Energy paper co-authored by Yao, cited by Yao)
- A lithium-ion learning rate of roughly 20% to 22% over thirty years, with
  improved cell design contributing more than falling materials cost. (Yao)
- Lithium is about 7% of a lithium-ion cell by mass. (Yao)
- The illustrative materials math: LFP at $3 per kilogram to manufacture plus $2
  of minerals, yielding about 500 watt-hours per kilogram, works out to $10 per
  kilowatt-hour; a sodium equivalent at $3 per kilogram yielding 250 watt-hours
  works out to $12 even with free minerals. These are round illustrative
  numbers, not measured costs. (Yao)
- CATL announced a 160 watt-hour-per-kilogram Prussian-blue sodium-ion cell in
  2021. (Yao)
- CATL's chairman Robin Zeng said in November 2024 that he expects sodium-ion to
  take up to half of LFP's market share. (Zeng, cited by Yao)

## Where it's contested

- **Safety is the claim Yao most wants corrected.** A blanket statement that
  sodium-ion is safer than lithium-ion is "objectively wrong" in his phrasing.
  Safety follows the cathode: the sodium pyrophosphate NFPP is safer than the
  sodium layered oxide NFM in the same way LFP is safer than NMC. He flags the
  zero-volt shipping benefit as genuinely uncertain too.
- **Drop-in manufacturability is true in some cases and not others.** Small
  Chinese lines yes, dedicated gigafactories no. Kann's reframing, that the real
  benefit is lower risk on a greenfield plant, is his own and Yao accepts it.
- **Kann's framing that only cost matters is narrower than Yao's own answer.**
  Yao lets the editorial stand at the time, then later describes two strategies,
  total cost of ownership and performance niche, that are explicitly ways of not
  competing on cell cost. The broader version is the guest's.
- **The China read is explicitly anecdotal.** Yao calls the sector opaque, says
  he is relying on what is anecdotal, and attributes his suspicion about CATL's
  announcement to grapevine talk. It should not be repeated as analysis.
- **Whether sodium-ion survives on techno-economics alone is left open.** That
  is Yao's closing phrasing, and the episode does not resolve it. His negative
  result is narrow and specific, that scale is not the missing ingredient. It is
  not a verdict that sodium-ion fails.
- **The guest's own background is lithium-ion.** Kann introduces him as a former
  battery entrepreneur in that world and as the former co-founder and chief
  technology officer of EnPower, where he still sits on the board. His argument
  rests on a published model rather
  than on proprietary data, and he is not dismissive of sodium-ion, but the
  vantage point is worth knowing.
