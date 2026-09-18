---
episode: "The case for sodium-ion"
published: "2025-08-14"
guest: "Landon Mossburg, founder and CEO, Peak Energy"
threads: [batteries, energy-storage, cost-curves, manufacturing-capacity, china]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Sodium-ion cells still cost more per kilowatt-hour than the lithium chemistry
that dominates grid storage. So what is the bullish case for building grid
batteries out of them?

## The answer

That the cell premium is real, shrinking, and the wrong thing to optimize.
Mossburg's argument is that his chemistry's tolerance for heat and its milder
failure mode let you delete the cooling system rather than improve it, which
offsets the energy-density penalty on installed cost and then wins decisively on
the operating and maintenance third of project cost that the industry has barely
touched. On his own numbers the total installed cost is still higher than
lithium iron phosphate; the case is about lifetime cost of ownership, not sticker
price.

## The argument

The premise Peak Energy was founded on has already broken, and Mossburg says so.
Two years before recording, the pitch for sodium-ion was that it would be
fundamentally cheaper at the level of raw atoms than lithium iron phosphate, a
continuation of the earlier shift from nickel manganese cobalt, which traded
energy density for cost and turned out to be worth making. Then the price of
lithium iron phosphate fell very fast, to roughly half what it had been two years
earlier, so the bar rose sharply exactly as the company started. He says the
original trajectory remains possible given comparable investment, but that the
reason to be interested changed from the economics of the materials to what the
chemistry lets you do at the system level.

Start with the gap he has to close. Sodium-ion is not one thing; like lithium-ion
it is differentiated mostly by cathode. Layered oxides approach lithium iron
phosphate on energy density but cost more because they contain a transition
metal, cycle less well, and are harder to design safely, and much of the existing
deployment sits there, in small applications like twelve-volt replacements and
scooters, where high power and cold-weather performance matter. Peak chose the
other branch, a sodium pyrophosphate cathode paired with a hard-carbon anode,
which he calls NFPP and never spells out. Its materials are dirt cheap and
substantially less energy dense, which he names as the chemistry's primary
problem. On a cost-per-kilowatt-hour basis those cells currently run $15 to $30
above an equivalent lithium iron phosphate cell, against a Chinese cell at $50 to
$60, and supplier quotes point to about $20 per kilowatt-hour coming out of the
sodium cell price over two to three years. That erodes the premium but not all of
it: he expects to be about $10 more expensive in 2028.

The reversal comes at the system level, and it runs against the usual intuition.
Lower energy density normally makes everything else worse, since fewer
kilowatt-hours per container means more steel, wiring and containers per unit of
storage, for the same reason panel efficiency matters in solar. Two chemistry
properties invert it. NFPP is comfortable between 45 and 60 degrees
Celsius, degrading about as fast there as lithium iron phosphate does at 25, and
managing heat is the hardest problem in a grid battery, which sits in a desert for
twenty years while power is pushed in and out of it. And the cell's failure mode
is gentler: it begins self-heating at a lower temperature, burns cooler in thermal
runaway so propagation is easier to stop, and vents a less explosive gas. Together
those let Peak remove the thermal management system outright rather than engineer
it better. No fans, no pumps, no chillers, no external auxiliary power, no moving
parts at all, on a design philosophy he attributes to a team drawn from Tesla and
SpaceX: the best part is no part. Because cooling is the most complex and
expensive part of a lithium iron phosphate system, deleting it recovers enough
cost and volume to put balance-of-system roughly at parity despite the density
penalty, leaving total installed cost within $20 to $30 per kilowatt-hour of a
good Chinese lithium system today.

And Mossburg is direct that this is still not a reason to buy. If the story ended
with being $10 more expensive in 2028, he says, there would be no reason for his
company to exist. The argument rests on the two-thirds of project cost that is not
hardware. By his accounting hardware is now about a third of the total; operations
and maintenance, including degradation, auxiliary power and round-trip efficiency
losses (the share of stored electricity you get back out), is about another third
on a net present value basis at a 10% discount rate, and undiscounted he says it
is by far the largest bucket; installation and commissioning is the remainder. The
industry has pushed on the hardware third since grid storage began, with most of
the fall in the last three or four years, and left the other two largely alone.
Peak's claims sit there: roughly 50 times less auxiliary power than an equivalent
lithium system, and removal of something close to 90% of the components that need
routine maintenance or fail, which also happen to be the components behind most
storage fires, which he notes are still fairly rare. That nets about $75 per
kilowatt-hour of net present value benefit on a lifetime-cost basis in a hot
climate. Cycle life supports it, with fewer degradation mechanisms than lithium
iron phosphate and cells near 10,000 cycles still well above 80% state of health,
meaning the share of original capacity they still hold. What he does not claim is
calendar life. His cells have been on test for a little over a year against a
twenty-year product,
and while he argues the lithium industry cannot answer that question either, that
is an observation about shared ignorance rather than an answer. He puts that limit
there himself.

## What you need to know first

- **Lithium iron phosphate.** The cheaper, less energy-dense lithium-ion cathode
  chemistry that now dominates grid storage, having displaced nickel manganese
  cobalt for this use. It is the benchmark every comparison in this episode is
  drawn against.
- **NFPP.** The sodium-ion cathode Peak uses, which he describes only as a sodium
  pyrophosphate; he never spells the letters out. He pairs it with a hard-carbon
  anode. Cheaper materials and substantially lower energy density than lithium iron
  phosphate, and more tolerant of heat. The transcript renders the acronym as both
  "NNFP" and "NFPP".
- **Balance of system.** Everything in an installed battery that is not the cells:
  containers, steel, wiring, controls, cooling. Lower energy density normally
  inflates it, which is why removing the cooling equipment is the pivot of the
  whole argument.
- **Auxiliary power.** Electricity the storage system consumes itself, mostly to
  run cooling, which is both an operating cost and a lost sale. The transcript
  renders it as "OX power" throughout.

## Details worth keeping

- Apart from active materials and electrolyte salts, the bill of materials is the
  same as lithium-ion, so tooling, supply chain and operator familiarity carry
  over. That is his argument for why sodium-ion scales faster than flow batteries
  or compressed air, where the unknown unknowns are larger and operators have no
  experience to draw on.
- Sodium bicarbonate, the sodium input, can be made synthetically or mined from
  trona, and he says the raw resource is not the bottleneck. Processing capacity,
  most of it in China, is. He frames a non-Chinese supply chain as a closing
  window: sodium-ion active materials have far less incumbent Chinese scale to
  compete against than lithium iron phosphate does, so entering now is much easier
  than entering in four or five years, by which point it would look like lithium
  does today.
- Chinese stationary deployment is early. First demonstrators were announced late
  2024 and early 2025 at tens of megawatt-hours, driven partly by policy giving
  non-lithium storage preference in the interconnection queue, and partly by
  applications with high safety requirements such as storage for fast charging at
  fuel stations. He says the operating-cost argument he is making has not yet been
  a focus there.
- A design choice worth noting: Peak does not spend its degradation advantage on
  reduced augmentation, meaning bolting on extra capacity later to offset what the
  cells have lost, because customers value that differently. It spends it on
  running the cells hotter with less cooling, and he says degradation could be
  better still if they cooled cells the way lithium systems do.
- The degradation mechanisms differ in count rather than in kind. No graphite
  anode means no graphite exfoliation, and there is almost no iron dissolution in
  the cathode. Both chemistries share solid-electrolyte-interphase dissolution,
  and he says the strategies that stabilize it for lithium iron phosphate appear
  to work for NFPP, which is why he thinks unknown unknowns are less likely here
  than in a genuinely novel chemistry.
- Evidence he cites for direction of travel: CATL's hybrid vehicle pack, which he
  thinks uses layered-oxide sodium cells for power and cold weather with lithium
  iron phosphate for the rest, and BYD pushing out its first sodium packs. The
  Korean majors are largely absent, having committed to catching up on lithium iron
  phosphate instead, though he says interest is starting to appear from both
  smaller and larger Korean players.

## Claims worth citing

All figures as stated on 2025-08-14. Cell prices and manufacturing capacity move
quickly, so treat the dollar figures as a snapshot. Everything describing Peak's
system is the company's own design and laboratory data for a product just now
reaching the grid, not independently measured field performance.

- Somewhere between 30 and 100 gigawatt-hours of sodium-ion manufacturing capacity
  worldwide across all variants, almost entirely in China. He flags the range as
  soft, because lithium lines can be and have been repurposed. (Mossburg)
- Lithium iron phosphate was almost twice as expensive two years ago as at the
  time of recording. (Mossburg)
- NFPP cells today cost $15 to $30 per kilowatt-hour more than equivalent lithium
  iron phosphate, against a Chinese lithium cell at $50 to $60 per kilowatt-hour.
  (Mossburg)
- Supplier and raw material quotes show the sodium cell price falling by about $20
  per kilowatt-hour over two to three years. Asked whether that erases the premium,
  he says not entirely: roughly $10 per kilowatt-hour more expensive at 2028.
  (supplier and raw material quotes, cited by Mossburg)
- Separately, he puts the price crossover with Chinese lithium iron phosphate
  somewhere between 2028 and 2030. He says that during the layered-oxide and
  mobility part of the conversation, about Chinese sodium-ion generally, whereas
  the $10 figure is about Peak's own cells. He does not reconcile the two and Kann
  does not press him. (Mossburg)
- NFPP is comfortable between 45 and 60 degrees Celsius, with degradation similar
  to lithium iron phosphate at 25 degrees. (Peak data, stated by Mossburg)
- Vent gas contains roughly 50% less hydrogen than lithium iron phosphate, with a
  hoped-for path below the threshold at which an open flame would ignite it. The
  sentence is garbled in the transcript and the "50%" appears twice in different
  constructions. (Mossburg)
- A lithium iron phosphate block in a hot region consumes on the order of 50
  megawatt-hours a year in cooling load alone. (Mossburg)
- Peak claims about 50 times lower auxiliary power use than an equivalent lithium
  system, and removal of nearly 90% of components that require regular maintenance
  or break. (Peak, stated by Mossburg)
- Total installed cost within $20 to $30 per kilowatt-hour of a good Chinese
  lithium system today, trending to about $10 by 2028, with balance-of-system cost
  already roughly at parity. (Peak, stated by Mossburg)
- Project cost structure: hardware about one third, operations and maintenance
  about one third on a net present value basis at a 10% discount rate, and
  installation and commissioning the rest. (Mossburg)
- About $75 per kilowatt-hour of net present value benefit on a total cost of
  ownership basis against an equivalent lithium system, in a hot region such as
  Miami or Phoenix. (Peak, stated by Mossburg)
- Cycle life: nearly 10,000 cycles still trending well above 80% state of health.
  In a direct lab comparison at 45 degrees Celsius, an equivalent lithium iron
  phosphate cell was at 80% state of health after about 2,600 cycles while the
  NFPP cell was at 94.5% to 95% after almost 3,000. (Peak lab data, read out by
  Mossburg)
- The United States holds 92% of proven naturally exploitable trona reserves, the
  mined source of sodium bicarbonate. (Mossburg)
- Peak's first 3.5 megawatt-hour unit is going into the grid in Denver, described
  as the largest sodium-ion system deployed to a grid outside China and the first
  fully passive grid-scale thermal management system anywhere. (Peak, stated by
  Mossburg)

## Where it's contested

- **The episode is framed as advocacy and says so.** Kann introduces it as a
  deliberately bullish view from someone with systems to sell, and sets the
  expectation that the guest is optimistic. That framing is unusually explicit and
  should travel with any figure taken from here.
- **Mossburg pre-empts the bias question rather than denying it.** He says Peak is
  not a sodium-ion company but a vertically integrated storage company that will
  pick whatever chemistry suits the application, and mentions work on
  high-temperature lithium iron phosphate. Kann's reply is dry: good, then you will
  be less biased in what follows. Neither of them pretends this is a neutral
  assessment.
- **The energy-density penalty is conceded, not argued away.** He calls it the
  chemistry's primary challenge and says the gap is wide and substantial. Every
  system-level saving is claimed against that penalty rather than instead of it.
- **Calendar life is openly unresolved.** Cells have been on test for a bit over a
  year, including accelerated testing, against twenty-year systems. He argues the
  lithium industry is in the same position because it is not twenty years old
  either, which is fair and is not an answer.
- **The manufacturing plan is contingent.** Cells come from China today. A US cell
  factory depends on first winning offtake agreements, meaning committed forward
  purchases that make the factory financeable. The customer announcements are
  described as coming soon rather than signed.
- **He flags the limits of his own knowledge in two places**, on layered-oxide
  cathode manufacturing and on the worldwide capacity figure, which he calls hard
  to pin down.
- **Cost comparisons are configuration-dependent.** Kann points out that installed
  cost is idiosyncratic to regional labor rates and system design, and Mossburg
  agrees, so the parity and premium figures are directional rather than universal.
