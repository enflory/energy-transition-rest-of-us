---
episode: "The clean energy transition has a hardware problem"
published: "2026-05-26"
guest: "Drew Baglino, founder and CEO, Heron Power; previously nearly two decades at Tesla, where he was powertrain architect for the Model S and later led the global charging and energy business"
threads: [transformers, grid-hardware, supply-chain-costs, manufacturing-capacity, electrification]
source_transcript: "transcript.md"
note_version: 1
---

## The question

If the world has to build several times as much electricity system as it has
today, what is actually holding up the build, and can the equipment that moves
the power be replaced with something that scales faster?

## The answer

Baglino's answer is that the hard part is not generating electricity but
converting and distributing it, and the specific choke point is the
medium-voltage transformer, whose supply base grew at roughly 1% a year for many
years and then had to absorb hundreds of gigawatts a year of new solar,
batteries, charging and data centers. His company's bet is that the transformer
can be deleted rather than scaled, by pushing semiconductor-based power
electronics all the way up to medium voltage. He is explicit that the open
question is whether it can be made reliable at mass production scale, which he
states as the company's objective and which it has not yet done.

## The argument

The premise is arithmetic. To have a sustainable energy economy, which will be
largely electric, Baglino says the world needs to triple or maybe even quintuple
electricity generation and consumption, and his point is about who has to grow
to deliver it. Renewable developers are demonstrably good at deploying solar and
batteries, and the load side can produce heat pumps and millions of electric
vehicles a year. What is not obvious to him is that the electricity sector
itself, the utilities and the supply base serving them, can grow by 500%. He
says he found the specific version of that problem by accident, meeting founders
at venture events working on carbon sequestration, clean hydrogen,
next-generation solar, long-duration batteries, fusion and electric steel.
Nearly all of them said the core process was figured out and there were no power
electronics to buy. Two distinct failures sat behind that. The gear was sold
out, and a startup ordering one or two units went to the back of a line where
even utilities were struggling. And what they needed was a whole conversion
solution rather than a catalog part; going to a scale supplier of solar
inverters and asking for a custom build for a clean steel operation could, he
says, be really painful a lot of the time.

The obvious objection is that other parts of the stack did ramp, and Johnson
raises it with solar panels. Baglino's answer is that the transformer was never
given a reason to. Solar was heavily subsidized in Europe, China and
intermittently the United States, and what got subsidized was a genuinely
high-technology process: producing polycrystalline silicon and then etching and
doping it, which carries specialty capital expenditure. A legacy medium-voltage
transformer has no material science in it and is not a high-technology
production process, so it was not juiced in the same way and politicians never
intervened in that market. He offers that and two further reasons as
possibilities rather than findings: repeated federal efforts to raise
transformer efficiency standards, which he thinks left investors facing
regulatory uncertainty, and the chance that some incumbents saw power
electronics eventually climbing to medium voltage and disrupting the product.
The scale of what then landed on that under-invested base is the crux. In the
mid-2000s there was no utility-scale solar, no utility-scale batteries and under
a gigawatt a year of data center development, and medium-voltage transformers
served utility distribution at about 1% annual growth. Over the last 10 to 15
years almost a terawatt of transformer demand has appeared globally, and last
year alone almost 600 gigawatts of utility-scale solar was deployed, which he
sets against a total US peak power of a terawatt. He never scopes the 600
gigawatts and it sits inside that global frame, so the two sides of the
comparison are not stated on the same basis. He is careful about what kind of
problem this is: not a technology problem but a capacity one. It is hard to ramp
something up that quickly.

What Heron sells is power conversion at the megawatt scale and above, and he
calls the case for it a combination of factors: efficiency is one, reliability
and serviceability another. The argument turns on the second. The incumbent
product is monolithic. A medium-voltage transformer weighs multiple tons, needs
a crane, and costs weeks of downtime if something goes wrong, which is why data
centers overbuild: if four or five will do the job you install six or seven, so
a failure does not cost you the load. A power electronics equivalent is modular
and fail-operational, so one failed block leaves the rest running, and swapping
it could be a 10-to-15-minute job rather than a two-to-three-week one. It is not
literally hot-swappable at medium voltage, he says, but it is as fast as if it
were. That lets a site drop the overbuild or accept a few minutes at slightly
reduced power.

The argument's real load sits in what it would take to make that real, about
which he is unusually plain. The objective is to be the first solid-state
transformer solution reliable at mass production scale, and he stresses both
words. Successive engineering revisions raise complexity toward the full-power
five-megawatt product and maturity at the same time; his framing is that you
design for the known knowns, provision for the known unknowns, and only find the
unknown unknowns by testing, which they have already hit and expect to hit
again. Manufacturing steps up from hand-built prototypes to semi-automatic
tooling at the Scotts Valley headquarters to full automation at a factory site
still to be announced, and customers are chosen the same way, a few partners who
trade project pipeline for product maturity rather than a broad sales push. Why
this component justifies all that is a leverage argument: on its current
trajectory the medium-voltage transformer alone is on track to consume almost
half of all grain-oriented electrical steel in the world, so deleting it frees
that supply base for pole-mounted transformers and other electrification needs.
On policy he does two things. He asks whether electrical infrastructure should
be treated as critical infrastructure, drawing the analogy to the debate over
Huawei telecom equipment, and he says plainly that some incentives are needed to
drive the behavior, because it has run the opposite way for decades. On the
critical-infrastructure question his own answer splits: a passive
steel-and-oil transformer carries little hazard, but the more intelligence and
software go into the grid, the more where it is made and who owns it matters.

## What you need to know first

- **Medium voltage.** The tier between long-distance transmission and the wires
on a residential street; Baglino points to the lines along a town's main roads
and gives 12, 21 and 35 kilovolts as examples. It matters because almost
everything new connects there: utility-scale solar, grid batteries, vehicle
charging and data centers.
- **Power electronics and the solid-state transformer.** Equipment that changes
voltage, or converts between alternating and direct current, using
semiconductors and software rather than the passive steel-and-oil equipment it
replaces. "Deleting the transformer" means extending that semiconductor
conversion up to medium voltage so the passive transformer is no longer needed
in the chain.
- **Grain-oriented electrical steel.** A specialized steel that medium-voltage
transformers consume and that also serves pole-mounted transformers and other
lower-power electrification needs. Baglino never says what it does inside the
equipment, only that it is a shared and limited supply base, which is what makes
his leverage argument work.

## Details worth keeping

- Heron's first markets are solar, batteries and data centers, which Baglino
sizes together at roughly a $40 billion market for power conversion and growing
quickly. He says customers respond to the framing of deleting the transformer.
- The policy that exists today is narrow. He points to incentives for domestic
solar inverter manufacturing under two laws he names only by their initials, the
IRA and OB3, spelling out neither. Foreign names that supply US solar have plans
to relocate production or are in the middle of doing so, from Spain to Texas and
from Japan to the Southeast. He notes this is specific to solar.
- Two further consequences follow from removing the transformer rather than
improving it. Without oil there are no flammability or fire-code clearances, so
a site can be packed more closely. And what he cares about in the labor saving
is not the wage bill: there are not enough trained people, so a design needing
far fewer of them is likelier to make its schedule.
- His financing point is about working capital, not subsidy. He calls the cash
flow cycle one of the biggest inhibitors to ramp rate, with project delays,
supplier problems and payment terms outside a manufacturer's control, and notes
that how fast a first factory converts cash determines how fast a second can be
financed.
- On AI inside his own company: coding assistants mean hiring fewer software
engineers who each get more done, but what he finds more striking is building
internal business systems, such as program management and bill-of-materials
tracking, instead of buying software that needs consultants to integrate.
- He describes today's distribution grid as mechanical switches taking hundreds
of milliseconds to actuate and large spinning machines regulating frequency,
which he calls steampunk-era electronics, and argues this is why utilities find
rooftop solar and vehicle charging hard to absorb. His analogy for the fix is
chip integration, the first iPhone against the current one: functions added in
software later on hardware already installed, which he says comes almost for
free once the passive gear is replaced.
- The lesson he takes from Tesla is commitment and focus, conditional on knowing
the physics work and that money coming in can exceed money going out. He thinks
founders come out of Tesla because they lived through the bad stretch and out
the other side, and that a lot of people give up too early.

## Claims worth citing

All figures as stated on 2026-05-26. Deployment and supply-chain figures in this
area move quickly. Several performance numbers below are Heron's own claims for
a product not yet in mass production, and read as design targets rather than
measured field results.

- A sustainable, largely electric energy economy requires tripling or maybe
quintupling global electricity generation and consumption, and it is not obvious
the electricity sector itself can grow by 500%. (Baglino)
- In the mid-2000s there was no utility-scale solar or batteries, data center
development ran under a gigawatt a year, and the medium-voltage transformer base
had grown at roughly 1% a year for many years. (Baglino)
- Almost a terawatt of transformer demand globally has appeared over the past 10
to 15 years. (Baglino)
- Almost 600 gigawatts of utility-scale solar was deployed last year, which he
sets against a total US peak power of a terawatt. He does not say whether the
600 gigawatts is global or US, and it sits inside a passage about global
transformer demand, so the two figures are not stated on the same basis.
(Baglino)
- Power conversion for solar, batteries and data centers is roughly a $40
billion market and growing quickly. (Baglino)
- Servicing a power electronics block could be 10 to 15 minutes against two to
three weeks for a comparable service action on a medium-voltage transformer.
(Baglino, for Heron's product)
- Removing the fire clearances around oil-filled transformers cuts the site
footprint of a battery installation by about 40%, and more for a data center.
(Baglino, for Heron's product)
- Going from medium voltage directly to the rack in a data center is almost an
order of magnitude less labor across fabrication, installation and
commissioning. He states this as what the company believes rather than what it
has measured. (Baglino, for Heron's product)
- On its current trajectory the medium-voltage transformer alone will consume
almost half of all grain-oriented electrical steel in the world. (Baglino)
- Eighty percent of the transformers deployed in the United States are
manufactured abroad. (Baglino)
- A 40-gigawatt factory, with the market described as much bigger than that. It
appears inside a hypothetical about financing a second facility, so it is not
clear whether the figure describes a plant being built or an illustration.
(Baglino)
- The full-power product is five megawatts, and the factory site for full
automation is to be announced later in 2026. (Baglino)

## Where it's contested

Nothing here is disputed. Johnson and Baglino know each other personally, which
Johnson establishes in the first exchange by joking about dislocating his
shoulder the last time they were together, and the conversation is friendly
throughout. The useful content is what went unexamined.

- **One restatement the guest did endorse.** Johnson compresses the pitch into
four claims, that it is faster to fix by minutes rather than weeks, needs
dramatically less labor, requires fewer additional parts and does not catch
fire, and asks whether he has it right. Baglino says it is a good summary. That
is explicit endorsement rather than the silence that carries no weight, and it
is worth marking because there is little else like it here.
- **Cost never comes up.** No price, no comparison against the installed cost of
a medium-voltage transformer, no named customer. The commercial case rests
entirely on availability, serviceability, footprint and labor, and the partners
are described only as lighthouse partners in general terms.
- **The tax credit proposal is the host's.** Johnson says it has long seemed
intuitive to him that transformers and the electrical supply chain should have
some form of the credit he names only as 45X, a tax credit rewarding domestic
manufacture of the components, of the kind he says batteries received, plus
receivables financing to solve working capital. Baglino's answer is more
general, that the country should
decide whether it wants this equipment built domestically and that incentives
are needed because behavior has run the other way for decades. His own specific
ask is about the cash flow cycle.
- **The framing is about volume, not age.** The opening monologue describes a
century-old machine straining to keep up and says the limiting factor often is
not generation but the hardware that delivers electricity. Baglino's diagnosis
is narrower and different in kind: one component class whose supply base cannot
ramp fast enough, plus a technology-generation argument that it should be
replaced rather than expanded. He does not argue that existing transformers are
failing from age.
- **The demand side is taken as given.** The tripling-to-quintupling premise
that motivates the whole company is stated once and never examined, and neither
speaker asks what happens to the thesis if electricity demand grows more slowly.
