---
episode: "An ode to electrochemistry"
published: "2025-03-13"
guest: "Yet-Ming Chiang, professor of materials science and engineering, MIT, and co-founder of Form Energy, Sublime Systems and other electrochemistry companies"
threads: [heat-and-industry, batteries, critical-minerals, materials-discovery, ai-applications]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2025-03. The physics and the design heuristics are durable; the read on how far AI had gotten in materials discovery is the perishable part."
disclosure: "Kann discloses on air that two of Chiang's companies, Form Energy and Sublime Systems, are Energy Impact Partners portfolio companies and that he is an investor. Routine for this show, noted because Sublime's cement process is the episode's main worked example."
---

## The question

What is electrochemistry actually good at, and how do you tell which industrial
problems are worth pointing it at?

## The answer

It is exceptionally good at forcing chemical reactions that would not otherwise
happen, driving them with voltage rather than heat and in some cases at room
temperature. Its main limitation is the mirror image of that strength: the
reaction happens only at an electrode
surface, so throughput is capped by area rather than by volume. The rule Chiang
draws from that is to use electrochemistry at the one step where concentrated
energy is indispensable, and let ordinary bulk chemistry do everything else.

## The argument

Start with why the field is powerful at all. Spontaneous reactions run downhill
and happen by themselves; the interesting ones run uphill and do not.
Electrochemistry makes uphill reactions go by applying a voltage. Chiang's
illustration is a lithium-ion cell, which sits at roughly three and a half to
four volts. Charging it pushes a lithium ion across about four volts, imparting
four electron volts of energy to that ion, which he puts at roughly ten times
the heat of vaporization of water and thermally equivalent to about 46,500
degrees kelvin. You do that at room temperature by turning a knob. Set it
against mechanical energy, meaning how much you can store elastically in a
solid before it snaps, and the electrochemical number is enormous by
comparison, which is why he says electrochemistry is powerful enough to break
anything. That is meant literally: put an acoustic sensor on a fresh cell and
cycle it, and you hear the solid compounds inside cracking. His group later ran
that backwards and used electrochemistry as a mechanical actuator, including a
DARPA project to twist helicopter rotors in flight.

The limitation follows from the same picture. Electrons have to cross into or
out of an electrode, so an electrochemical reaction is a two-dimensional
process happening at an interface, while a thermal reaction is a
three-dimensional process happening throughout a volume. You can engineer more
surface area, which Chiang guesses buys you something like a factor of ten, but
the constraint is fundamental and no amount of cleverness removes it. Hence his
warning against the hammer looking for a nail. The interesting designs do not
electrify every step; they electrify the step where electrochemistry does the
most good.

Cement is the worked example. The tempting move, given cheap electricity, is to
use it as heat, and that is precisely what Sublime did not do. Instead the
electricity goes into an electrolyzer, and the electrolyzer makes reagents.
Split water at something above roughly one and a quarter volts and you get
hydrogen at one electrode and oxygen at the other; because you are pulling
hydrogen off the water at one end and oxygen off at the other, one electrode is
left basic and the other acidic. A single device therefore produces acid and
base at once, and those reagents do the chemical work downstream in a tank,
where the reaction is volumetric rather than interfacial. Water splitting is the
familiar illustration; describing his own process he corrects himself in passing
to splitting salt. Chiang says the same pattern has since propagated into
mining. It also solves a second problem
almost for free. Cheap electricity is often intermittent electricity, and acid
and base are storable, so they act as chemical storage and let the downstream
process run continuously on a front end that runs only when power is cheap. He
is careful not to oversell that: if your capacity factor is well below one
hundred percent, the capital cost consequence is what it is and cannot be
engineered away. What storage buys is decoupling in time, not a free lunch.
Kann's summary, which Chiang accepts, is that you either bolt a battery onto
the process or design one into it.

Which gives the hunting-ground heuristic. Look for transformations that are not
merely energy-hungry but energy-intense, where the energy has to be
concentrated in one place, usually involving small inorganic species, and which
today are done by burning fossil fuels for high heat. The contrast is biology,
where the total energy involved may be large but the concentration is low, and
where bulky organic molecules make it hard to reach high current density, the
amount of current you can push through a given area of electrode. The boundary
on the other side is solid-to-solid transformations, which electrochemistry
handles badly because insulating solid particles do not conduct electrons well
enough to react briskly at an electrode. Notably, Chiang names that limitation
and then names a solid-to-solid reaction, reducing iron oxide to iron metal in
an alkaline electrolyte near room temperature, as one of the things he finds
most exciting, on the grounds that his group thinks it has a way around the
problem. The boundary is a live research question, not a settled wall.

## What you need to know first

- **Uphill reaction.** One that will not proceed on its own because it needs
  energy put in. Applying a voltage is how electrochemistry supplies it, and
  this is the source of the field's leverage.
- **Electrolyzer.** A device that uses electricity to split a compound, most
  familiarly water into hydrogen and oxygen. In the cement case its real product
  is not the gases but the acid and base left behind.
- **Current density.** Current per unit area of electrode. Because
  electrochemistry is surface-limited, this is the number that decides whether a
  process is economically plausible at scale.
- **Capacity factor.** The fraction of the time a plant actually runs. Running
  only when electricity is cheap lowers it, which raises the capital cost burden
  carried by every unit of output.

## Details worth keeping

- The largest electrochemical process ever scaled is not hydrogen electrolysis
  but chloralkali: a sodium chloride solution yields sodium hydroxide at one
  electrode, chlorine gas at the other and hydrogen along the way, with
  hydrochloric acid available by recombining the two gases.
- Industries that need enormous amounts of electricity have always chased cheap
  power geographically; Chiang's example is high-temperature ceramics clustering
  around Niagara Falls. Kann notes the modern version of that hunt now competes
  with data centers for the same cheap capacity.
- Electrolyzers making acid and base for extraction show up across several
  projects in the ARPA-E mining program.
- On iron, Boston Metal's approach is high-temperature electrolysis of molten
  iron oxide, reducing iron metal at one electrode and releasing oxygen at the
  other. A colleague of Chiang's (the transcript garbles the name) is
  working on molten sulfides, which he says would take roughly another 300
  degrees C out of the process.
- Rare earth separation is on his list because the elements are chemically very
  similar while a magnet mostly wants neodymium and praseodymium specifically; a
  postdoc in his lab is testing whether an electrochemical route can separate
  them. He also wants an emissionless electrochemical path for copper but says
  that work is not mature enough to discuss.
- His framing of AI in the lab is that it is a continuation, not a break.
  High-throughput computation to narrow down which experiments to run started in
  the mid-1990s, became machine learning over large databases, and AI is the
  next step along the same line.

## Claims worth citing

All figures as stated on 2025-03-13 and attributed to the speaker rather than
independently verified. The physical constants are durable; the assessment of
AI-assisted discovery is a snapshot of that moment.

- A lithium-ion cell sits at roughly 3.5 to 4 volts. (Chiang)
- Four electron volts is about ten times the heat of vaporization of water and
  thermally equivalent to roughly 46,500 degrees kelvin. (Chiang)
- Neutral water splits at something above about 1.25 volts in a pH-7
  electrolyzer. (Chiang)
- Increasing electrode surface area might buy a factor of about ten against the
  two-dimensional limit, given explicitly as an approximation. (Chiang)
- Molten sulfide electrolysis would operate roughly 300 degrees C below molten
  oxide electrolysis for iron. (Chiang)
- On battery cathodes, the judgment is that good solid-state chemist intuition
  has still outperformed computational discovery to date, with disordered rock
  salt cathodes among the few genuine computational wins, and that the balance
  is improving. (Chiang)
- Chiang has co-founded at least six electrochemistry companies, among them Form
  Energy, Sublime Systems, 24M, Desktop Metal and A123 Systems. (Kann)

## Where it's contested

- **Chiang declines the host's setup.** Kann suggests electrochemistry was
  a backwater before lithium-ion; Chiang rejects that, noting there has always
  been sustained work in the field, and agrees only that interest exploded with
  the battery. Kann also calls the field kind of magic. Chiang does not answer
  that directly, but his own framing, offered a little later, is that being
  absolutely clear about the limits is what stops you becoming a hammer looking
  for a nail.
- **The cheap-electricity premise is not resolved.** The whole case rests on
  low-cost electricity, and Kann points out in the same breath that anyone
  seeking cheap power now competes with data centers, and that the genuinely
  cheap power is often the intermittent kind. Chiang's answer is process design
  and storage, not a claim that the power will be there.
- **Solid-state transformations are a limitation he is simultaneously claiming
  to work around.** Both halves are in the episode and neither is demonstrated
  in it.
- **Whether AI can invent is left explicitly open.** Chiang distinguishes
  finding a catalyst for a stated reaction from imagining a whole system that
  links production, use and disposal, and says plainly that he does not know
  enough to answer whether AI can do the second. Kann's closing restatement,
  that AI will make Chiang more efficient rather than redundant, draws a joke
  rather than an endorsement, so it should not be read as his considered view.
- **Two of the companies discussed are portfolio companies of the host's firm**,
  disclosed up front. Nothing here is a product pitch, but the cement and
  grid-storage examples come from a founder describing his own approach.
