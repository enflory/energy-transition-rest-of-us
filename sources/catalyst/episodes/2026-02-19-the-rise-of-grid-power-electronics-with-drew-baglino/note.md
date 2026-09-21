---
episode: "The rise of grid power electronics with Drew Baglino"
published: "2026-02-19"
guest: "Drew Baglino, founder and CEO, Heron Power"
threads: [transformers, grid-hardware, supply-chain-costs, data-center-power, manufacturing-capacity]
disclosure: "Kann states on air that he has been an investor in Heron Power since the company's first external round, and that EIP invested again in Heron's $140 million Series B, led by Andreessen Horowitz and announced the week of recording."
source_transcript: "transcript.md"
note_version: 1
---

## The question

What changes if the grid's transformers stop being passive lumps of steel and
become controllable power electronics, and why is that finally possible now?

## The answer

Two things make it possible: silicon carbide devices now block enough voltage to
interface with distribution circuits directly, and the traditional transformer
supply chain has stayed jammed long enough to open a door for new equipment. The
near-term selling point is not intelligence, it is deletion. A solid state
transformer removes components and failure modes from solar plants, battery
plants and data centers. The control capability pays off later, by letting
utilities push more power through wires they already own.

## The argument

Start with why power semiconductors got interesting. The familiar Moore's Law
story is about shrinking logic transistors; power transistors improved over the
same five decades along different axes, including how much voltage they can
block, current density, thermal conductivity and, above all here, switching
speed. Speed matters because of how electricity behaves on a wire: everything
connected to a contiguous circuit affects everything else instantaneously unless
something in the middle decouples the flow. Power electronics are that something,
and modern silicon carbide and gallium nitride devices start and stop current
millions of times per second. Applications arrived in the order the devices
allowed, from variable frequency drives on industrial motors around 1980, to
direct-current links letting grid regions at different frequencies trade power,
to consumer switching power supplies, to the parts that made solar inverters and
electric vehicle drive inverters possible in the early 1990s.

Now contrast the grid, where none of that happened. At the branch points the
equipment is still mechanical switches and passive transformers. The switches
actuate in hundreds of milliseconds, can operate maybe once every couple of
minutes, and are not built for more than a couple of thousand operations in their
whole life. The transformers are fixed-ratio voltage dividers with no control over
power flow; power simply takes the path of least resistance. Baglino says this
was true in 1970 and is broadly still true in the 2020s, while the inverter in a
battery or an EV charger controls voltage and current hundreds of thousands of
times a second. What changed is device voltage. Silicon carbide was a 600-volt or
1.2-kilovolt technology ten years ago and now reaches 4.6 kilovolts, close enough
to US distribution voltages that you no longer need an impractical stack of
devices in series to work at grid voltage.

The commercial opening comes from a different direction: the legacy transformer
market cannot keep up. Baglino declines to rank the causes and simply lists them.
Demand is up broadly, from data centers interconnecting at transmission, from new
generation, and from electric vehicles and home electrification, and part of it
is replacement of 1970s equipment rather than growth at all. Regulatory
uncertainty made it worse: the Department of Energy floated changing transformer
efficiency rules, which would touch the grain-oriented electrical steel that is
the largest material input by mass, so nobody expanded steel supply while the
question was open. Tariff volatility makes it hard to know which country to build
a factory in. Kann adds a cause Baglino does not, which is that incumbent
manufacturers have lived through boom-bust cycles and expand by 2x rather than
5x, by which time the data center forecast has doubled again. He defends that as
reasonable rather than negligent, since every manufacturer would rather sell into
an undersupplied market. Baglino has a stake in one of his own listed causes:
part of the hesitation he describes is people betting that solid state
transformers will displace the steel, which is, as he says, one of the reasons he
started Heron.

Kann then raises the objection that matters most in this industry. Better does
not necessarily win, so what is the net outcome a buyer actually pays for?
Baglino leads with reliability rather than capability. Inverters, not modules,
are the largest source of underperformance on utility-scale solar, with central
inverter availability averaging 97.5% to 98%. The transformers fail too, at
roughly 1% to 1.4% a year, because desert plants run them at nameplate for eight
or nine hours a day, which is not what they were designed for, and they carry
essentially no instrumentation, so owners send people out to check oil and
bushings. Against that, the solid state approach moves the 60-hertz transformer
to 100 kilohertz, making the magnetics 50 to 100 times more power dense and
letting the unit be built in 100-to-200-kilowatt modules rather than megawatt
blocks, so a fault costs 100 kilowatts instead of a megawatt, with no crane and
no months-long wait for a replacement. Components disappear with it: the legacy
transformer, low-voltage breakers and fuses, power-factor-correcting capacitors,
and some protection complexity, since a power electronics front end that faults
pushes only slightly above rated current instead of hard-faulting and catching
fire.

The data center case is the same argument with more to delete. Racks are still
fed with alternating current the way they were in the 1990s, which is fine at 10
kilowatts a rack and increasingly absurd at 100 kilowatts or a megawatt. At that
density the right answer starts to look like EV charging or a battery plant:
distribute direct current at higher voltage and raise the rack backplane from 48
volts, itself a telecom leftover, to 800 volts or more. One device can then go
from 34 kilovolts straight to 800 volts with no intermediate transformers and no
gray space full of uninterruptible power supplies and distribution panels. The
GPUs are still where the money is, but the scarce inputs are certified
electricians and copper, and both fall sharply when you stop distributing power
at low voltage. The long-run grid version is that one of these can cost about
what an oil-filled transformer costs while also doing the jobs of the components
that surround it: overcurrent protection and fault isolation, tap-changer voltage
correction, three-phase balancing, synchronous-condenser-like inertia, capacitor
banks for power factor. Those functions raise utilization, and since a rate case
divides total utility cost by kilowatt-hours served, higher utilization of
existing poles and wires is the lever on affordability.

## What you need to know first

- **Solid state transformer (SST).** A device that changes voltage using fast
switching power electronics and a small high-frequency transformer rather than a
large passive 60-hertz magnetic core. Because the conversion runs through
transistors, power flow through it can be controlled rather than merely passed
along.
- **Blocking voltage.** The voltage a single power transistor withstands when
switched off. It sets how many devices must be stacked in series to work at a
given grid voltage, which is why 4.6-kilovolt silicon carbide is what makes
grid-scale devices practical.
- **Grain-oriented electrical steel.** The laminated steel in conventional
transformer cores, used to hold down idle losses. It is the largest input by mass
and sits at the center of the shortage story.
- **Gray space and white space.** In a data center, gray space holds electrical
and cooling equipment and white space holds the racks. Deleting electrical
equipment converts one into the other.

## Details worth keeping

- Transformer efficiency ratings are measured at rated load, but magnetizing
losses in the steel never go away and most grid transformers are not fully
loaded. The DOE inquiry was aimed at that idle loss.
- Transformers are mostly made in China, India and Mexico, and very few in the
US. Inverter makers often mount one on the skid for ease of installation but
usually do not build it.
- In 2010 the silicon carbide supply chain was tiny and served LEDs. Wolfspeed,
Infineon and others built it out for 600-volt EV devices first and higher grid
voltages later.
- Higher switching frequency shrinks magnetics roughly linearly, which is why
Tesla's Model 3 onboard charger roughly doubled in power density and fell in cost
on silicon carbide.
- STATCOMs, switched capacitors used for power factor control, are the main
example of power electronics already on the grid, and Baglino says they are not
used often.
- Baglino's analogy: a junction today splits flow in a fixed ratio, so 100 units
in means 10 and 90 out and 200 in means 20 and 180. Power electronics let you
choose the split.

## Claims worth citing

All figures as stated on 2026-02-19. Performance and cost figures come from the
founder about his own equipment and should be read as company claims and design
targets rather than independently measured results.

- Over 70% of distribution transformers are more than 30 years old. Baglino
hedges this as "something like that." (Baglino)
- Demand for power and generator transformers has more than doubled since 2019;
generation step-up transformers up over 250%; distribution transformers up over
100%. Some of that is replacement of aging equipment rather than load growth.
(Baglino)
- Conventional transformers run at 99% to 99.3% efficiency depending on loading,
and a typical solar conversion chain is roughly 97.5% efficient end to end.
(Baglino)
- Silicon carbide at Tesla: about $100 more in device cost saved $400 to $500 in
battery, and roughly 1% drive inverter efficiency was worth three miles on a
300-mile pack. (Baglino)
- Silicon carbide blocking voltage went from 600 volts and 1.2 kilovolts ten
years ago to 2.3 and 4.6 kilovolts today, against US distribution voltages of 7
to 35 kilovolts. (Baglino)
- Central inverter availability on utility-scale solar averages 97.5% to 98%,
making inverters the largest source of underperformance, ahead of modules.
(Baglino)
- Utility-scale solar transformers fail at roughly 1% to 1.4% per year, so a
plant with 100 of them replaces at least one a year. (statistics gathered by
Heron Power, cited by Baglino)
- Moving from a 60-hertz to a 100-kilohertz transformer makes the magnetics 50 to
100 times more power dense and allows 100-to-200-kilowatt modularity. (Baglino)
- A 5% to 6% net present value uplift for customers versus conventional
inverter-plus-transformer builds, including roughly 1% absolute efficiency gain,
counted twice for batteries as round-trip. (Heron Power, cited by Baglino)
- In data centers, the design removes about 70% of the electrical equipment on
the diagram and a similar share of footprint, going from 34 kilovolts to an
800-volt rack backplane with roughly 30 seconds of hold-up. (Heron Power, cited
by Baglino)

## Where it's contested

- **The guest is selling the product.** Kann discloses his investment in Heron
and EIP's participation in the $140 million Series B announced that week.
Performance and cost figures for Heron's equipment are the founder's claims about
his own product, and the cost comparison is partly forward-looking: he says one
can cost about what an oil-filled transformer costs today and will ultimately
cost less per unit of voltage conversion.
- **Kann pushes on the "better isn't enough" problem.** He notes the electricity
industry's long history of technology pitched on capability that never wins
commercially, and asks what net outcome customers actually pay for. Baglino
accepts the framing and answers on reliability, space and capital cost rather
than control.
- **The causes of the transformer shortage are unranked by design.** Baglino says
he will not try to put them in order, and one cause he lists is the expectation
that solid state transformers displace conventional ones, a bet he has a direct
interest in. Kann adds incumbent caution as a factor Baglino did not raise, and
argues it is rational rather than a failure.
- **Efficiency comparisons need care.** The 99%-plus rating of a conventional
transformer is measured at rated load, while most units sit well below it and
carry constant idle losses, so headline figures on either side are not directly
comparable to field performance.
- **Timing on the grid case is open-ended.** Both treat wholesale replacement of
grid transformers as something that happens slowly, unit by unit, as aging
equipment comes due, and Kann frames the grid question explicitly as long term.
