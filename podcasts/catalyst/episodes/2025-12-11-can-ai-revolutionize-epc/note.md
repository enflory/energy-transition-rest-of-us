---
episode: "Can AI revolutionize EPC?"
published: "2025-12-11"
guest: "Alex Modon, co-founder and CEO, Unlimited Industries"
threads: [first-of-a-kind, cost-curves, data-center-power, supply-chain-costs]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Big capital projects are chronically late and over budget. Can AI change that,
and is engineering even where the leverage is?

## The answer

The problem is contractual before it is technical: the firms that design and
build these projects make money when projects cost more and take longer, and
software does not change that by itself. AI matters because it can drop the
marginal cost of engineering far enough to finish the design before the price is
committed, which is what would make a genuinely fixed price with no change orders
survivable. None of it is demonstrated; the first project is hoped for by the end
of 2026.

## The argument

Start with what an engineering, procurement and construction contractor is: one
firm that designs the project, runs its supply chain and builds it, engaged in a
single contract after the developer has secured land, permits, power and a
tenant. Modon's complaint is that both available contract forms reward the wrong
thing. Cost-plus pays a margin on whatever the project ends up costing, so the
contractor earns more when the job costs more and takes longer. Fixed-firm names
a price, but against a scope written tightly enough that the inevitable
discoveries during design trigger change orders, which is where Modon says the
margin actually gets made, negotiated when the developer can no longer walk away.
He steelmans it though, and Kann presses him to: these projects run from about
$100 million to several billion, involve hundreds of people, and genuinely cannot
be costed accurately up front, so the flexible contract is a risk-mitigation
device rather than a swindle. The misalignment worsens the more custom the
project, which makes first-of-a-kind facilities the worst case and data centers
bad because their interiors keep changing with chip generations and cooling
choices.

The second problem is less obvious and matters more. Manufacturing has a cost per
widget, so it gets a learning rate. Projects are each treated as an n of one, even
a company's tenth refinery, so nothing accumulates. Some of that is intrinsic,
since every site differs, but Modon argues most is self-inflicted: because
engineering has a high marginal cost, any tweak reintroduces a near-complete
redesign rather than just the delta, so design learning never compounds. Kann
supplies the sharpest illustration almost by accident. Modon credits solar's cost
decline to this kind of iteration, and Kann corrects him that it was module cost
that fell while installed cost did not fall nearly as fast, which is the
construction problem stated as a fact rather than a theory.

That sets up the actual mechanism, and it is not the one the title suggests.
Engineering is only 3% to 10% or 15% of project cost, so cutting engineering fees
is not the prize; spending engineering to buy certainty is. Today a conceptual
design gives roughly plus or minus 50% on cost, front-end engineering narrows
that to about plus or minus 10%, which is enough for a lender, and the project
reaches final investment decision there with only about 30% of the engineering
done. Finishing the rest first would burn development capital, and it is cheaper
to spend the lender's money later. Modon's claim is that if engineering becomes
cheap and fast enough to reach 100% definition before commitment, two things
follow. You know the complete equipment and bulk materials list on the day the
project is funded, so you can buy everything that day or hedge it, which removes
the commodity and tariff exposure that makes contractors demand flexibility in
the first place. And because you are no longer freezing design decisions early to
control engineering spend, you can search a wider space instead of settling into
a local optimum. Together those are what let him write contracts with no change
orders and carry the overrun risk himself.

The technology claim is deliberately modest. Modon says they have not redefined
engineering, they have augmented engineers so the same time and capital buys more
definition. The platform is internal, not a product they sell, and its main move
is consolidating a fragmented tool stack onto a single data model so no piece of
data lives in ten places. That consolidation is what makes agents usable: a trade
study a junior engineer would spend a week on, such as belt versus pneumatic
conveyance for a material-handling problem, can be delegated to a large language
model grounded in the project's own data, vendor spec sheets and simulation
tools, then handed back to the engineer who asked. His explanation for why
incumbents have not built this is the incentive argument again, that a contractor
has no reason to want software which reduces its billable hours, the way a law
firm does not.

## What you need to know first

- **EPC.** Engineering, procurement and construction bundled into one contractor.
  The developer hands over design, supply chain and building in a single contract,
  which is also how it loses control of the decisions that drive cost.
- **Cost-plus, fixed-firm and change orders.** Cost-plus pays the contractor a
  margin on actual cost. Fixed-firm names a price against a defined scope, and
  anything ruled outside that scope becomes a change order priced mid-project, when
  the developer has little leverage.
- **Front-end engineering design and final investment decision.** Front-end design
  narrows the cost estimate enough to finance, typically to about plus or minus
  10%. Final investment decision is when the money is committed.
- **Bulks.** The commodity materials and equipment bought in quantity, such as
  steel and wire. You cannot order or hedge them until the design says what they
  are.

## Details worth keeping

- Of the six to nine months a data center design occupies on the critical path,
  almost none goes to optimization, value engineering, designing around long-lead
  items, or designing for constructability. Speed is the main pitch Modon makes to
  that market.
- Kann's repeatability spectrum, which Modon accepts: utility-scale solar and
  storage at the repeatable end, where hundreds of near-identical projects exist;
  first-of-a-kind facilities at the other; data centers in between, because the
  powered shell repeats while the interior does not. Modon adds that interior
  changes trickle outward into the facility itself.
- The fragmented tool stack spans separate software for design, hand calculations,
  simulation, redline review, drafting handoff and vendor management.
- Meetings are recorded, and the recording itself generates tasks for the agents,
  so an offhand "what if we used a different material here" becomes a delegated
  trade study.
- On subcontractors, the long-term intent is to vertically integrate as far as
  possible, because that is where incentives can be fixed end to end. For early
  projects they work with local general contractors and trades, relying on deeper
  design definition to ask for firm prices against a scope that is actually
  defined.
- The episode is pegged to the company emerging from stealth with a $12 million
  raise, which appears in the show notes and is not discussed on air.

## Claims worth citing

All figures as stated on 2025-12-11 and attributed to the speaker. Claims about
the company's own contracting model describe an approach it intends to use, not
results it has achieved.

- Engineering is 3% to 10% or 15% of total project cost. Stated loosely as a range,
  so treat the upper bound as soft. (Modon)
- Conceptual design gives about plus or minus 50% cost certainty; front-end
  engineering design gets to about plus or minus 10%. (Modon)
- At final investment decision with a plus or minus 10% estimate, a typical project
  is only about 30% through its engineering. (Modon)
- Project costs run from about $100 million at the small end to billions at the
  large end. (Modon)
- The design phase of a data center project currently consumes six to nine months
  of critical path. (Modon)
- The company writes contracts with no change orders, and intends to purchase all
  bulk materials on the day a project is funded or else hedge the exposure. (Modon,
  describing his own company)
- Engineering, procurement and construction is a high-volume, low-margin business.
  (Kann, agreed by Modon, who adds that engineering margin specifically is small
  because engineering spend is small)
- Industry engineering software has not changed much in roughly 20 years. (Modon)
- Solar module costs have fallen much faster than installed costs, so the
  construction and commodity side has not seen the same learning. (Kann, accepted
  by Modon)
- First completed project hoped for by the end of 2026. (Modon)

## Where it's contested

- **This is a founder describing a company that has not yet built anything.** No
  completed project, no cost or schedule results, no named customer. Every
  performance figure is a design target for a business model, which is normal at
  this stage and worth holding in mind before repeating any of it as established.
- **Kann steelmans the incumbent structure, and it is not refuted.** He points to
  the lag between signing a contract and procuring commodities six, twelve or
  eighteen months later, to volatile materials prices, and to labor cost and
  availability. Modon agrees the complexity is real and that the contracts evolved
  as risk mitigation, then locates the fault in incentives anyway.
- **Kann's first theory of the business model is wrong and gets corrected.** He
  proposes that higher margins from cheaper delivery provide the buffer to absorb
  overruns. Modon says no: engineering margin is small relative to construction
  scope, and the buffer is supposed to come from 100% design definition.
- **The hedging answer is thin, and the subcontractor answer is partly ducked.**
  Kann calls buying or hedging all the steel on the day of financial close
  "complex" and gets no detail on how that works project by project. He also asks
  whether the no-change-order structure flows down to subcontractors, and gets
  long-term vertical integration plus "a handful of different ways" in the meantime.
- **The load-bearing assumption is asserted rather than evidenced.** Everything
  depends on AI dropping engineering's marginal cost enough to make 100% definition
  before commitment both affordable and fast. Modon describes the platform but
  gives no numbers on cost per design hour, cycle time, or how much of the design
  work the agents actually carry.
