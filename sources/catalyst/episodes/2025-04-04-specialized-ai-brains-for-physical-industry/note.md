---
episode: "Specialized AI brains for physical industry"
published: "2025-04-04"
guest: "Sam Smith-Eppsteiner, partner, Innovation Endeavors"
threads: [ai-applications, venture-and-finance, skilled-labor, construction-and-epc]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded in April 2025; the claims about what general-purpose models can and cannot do with technical drawings, and about what it costs to build a specialized one, are the fastest-moving material here and should be read as a snapshot of that moment."
---

## The question

Do physical industries need their own specialized AI products, or will the big
general-purpose models eventually get good enough to do the job?

## The answer

Smith-Eppsteiner's theory is that there is real room for vertical AI products in
industrial sectors, and that the reason has almost nothing to do with the models
and almost everything to do with the customer's data, which is fragmented across
legacy systems, heavily unstructured and visual, and private, so the big model
developers have never seen it. She is explicit that this is a theory rather than
a finding. She cites cases running both directions and says plainly that nobody
knows yet where it nets out.

## The argument

Her case lives on the supply side, meaning the customer's data, and it has three
parts. Industrial data is fragmented across legacy systems of record: in
manufacturing alone a customer might run an ERP, an MES and a PLM, some of them
on the company's own servers, alongside piles of PDFs in SharePoint and email.
The data is conceptually related but not practically linked. It is also
unstructured, and unstructured in two different ways. Maintenance logs and
similar text actually suit language models well, but blueprints, schematics,
diagrams and 3D models look nothing like what the big models were trained on.
And it is private, sitting on the customer's cloud or on-premise rather than in
the public domain, which is why she thinks general models read a technical
drawing poorly: they have not seen enough of them. One scope qualifier is easy
to lose here. Kann asked whether this is special to physical industries or true
everywhere, and her answer was that there is probably some of it everywhere but
more of it here, a difference of degree rather than kind, with the tooling older
because there has barely been a category-defining product built for hardware
engineers since the 1990s.

The catch is that the wall keeping the big labs out also keeps the startup out.
Kann presses this hard: if the training data is private, you have to train on
your customers' data, they will not like that, and if you cannot get past it you
never build a product that scales or improves. Smith-Eppsteiner says she thinks
that is likely true, and her supporting evidence is commercial rather than
technical. A founder she knows
wrote training rights into every master services agreement from the start, found
it very hard to get signed at first and now finds it boilerplate, and regards
that clause as what made the product both performant and defensible. So the moat
and the barrier to entry are the same object, and the defensibility argument is
only as strong as a young company's ability to win a contract term.

The demand-side leg is weaker, and she says so herself, calling the data points
the main thrust. Her demand argument is
the great crew change: experienced field engineers and technicians are retiring
faster than they are being replaced, so the same work must be done by fewer
people and the expertise sitting in their heads needs capturing. Kann's
objection is that this is a genuine macro driver that plays out over decades, a
slow-release painkiller with no urgency behind it. She concedes it is a
long-term trend and counters with customer sentiment rather than purchasing
behavior: in oil and gas, customers described it to her as a major pain point
and a real fear. On whether a specialized product can be built economically, she
reports founders getting to roughly 70% to 90% of required performance on prompt
engineering alone, leaving open whether that is sufficient or whether a person
fills the remaining gap. Past that the approaches scatter. She hears that
embedding works poorly on non-textual data, that fine-tuning is the natural next
step, and that some teams intend to build their own models, and she describes
the field as very early innings.

The last turn is economic, and it is where Kann is most skeptical. Plenty of
these applications are obviously useful without being large; his example is
siting optimization for energy developers, which he thinks is genuinely valuable
and not a venture-scale business by itself. Her answer is about stickiness and
expansion rather than proof. Upstream work like siting and permitting runs on
third-party external data, and when they talked to customers those customers
sounded ready to switch tools, whereas a product deeply integrated with a customer's
own data, with a model trained on it, is much harder to leave. Expansion comes
from embedding into the transaction layer sitting above the workflow, her
example being the fines for missed delivery appointments in trucking. Underneath
sits a business model choice with real consequences: sell the technology like
traditional software, or sell the work and absorb the AI cost yourself, which
she finds most attractive where the customer already outsources that function.
Either way inference cost is not trivial, so she expects gross margins in the
40% to 70% range rather than the 90% of classic software, and layering services
on top lowers margin further while raising the dollar value of the contract. The
prize she names is a budget shift: industrial companies have limited willingness
to pay for software but spend heavily on labor, so a product sold as labor
augmentation reaches a much larger pool. Whether that actually happens, she
says, is still to be seen.

## What you need to know first

- **Systems of record.** The core databases a company runs on. ERP is enterprise
  resource planning, covering finance, orders and inventory; MES is
  manufacturing execution, covering what is happening on the shop floor; PLM is
  product lifecycle management, covering designs and their revisions. In these
  industries they are typically old, separate from one another, and sometimes
  running on the company's own hardware rather than in the cloud.
- **The specialization ladder.** Four increasingly expensive ways to make a
  general model work on your problem: prompt engineering, meaning carefully
  written instructions, and the cheapest option; embedding, converting your
  documents into a form the model can search; fine-tuning, further training an
  existing model on your data; and training a model of your own. Most of the
  disagreement among the founders she talks to is about which rung to stop at.
- **Inference cost.** What it costs to run the model every time someone uses the
  product. Traditional software has almost no equivalent, which is why she
  expects structurally lower margins here.
- **The great crew change.** The industry's term for the retirement wave among
  experienced field engineers and technicians, and for the undocumented
  expertise leaving with them.

## Details worth keeping

- She lays out four categories of company: the knowledge base, which she prefers
  to describe as making sense of complexity rather than as search; agentic AI
  that does the work; copilots for engineering and discovery; and compliance and
  risk mitigation.
- The knowledge-base example is concrete. On a construction site, answering
  "when are the light fixtures for the second floor arriving?" means parsing the
  phrase, finding the right fixture on the blueprints, identifying the specific
  item and then looking it up in a supply chain system. Conceptually trivial,
  and today it takes several people across several systems.
- Hubflow automates scheduling between truckers and receiving warehouses for one
  side of the transaction while the other side sees its normal workflow
  unchanged. A company called Conduit is automating the other side, so the two
  may end up negotiating appointments with each other.
- Cadstrom, an early investment of hers, is building a copilot for electrical
  engineers doing circuit board design, starting at verification and validation
  because engineers dislike that work. The sequence it performs, inferring the
  engineer's intent, parsing each component's limits, modeling how the board
  would behave, then deciding on and running the simulations, is what she thinks
  transfers to structural and other engineering domains. The transcript garbles
  the company name to "Strom."
- WeaveBio, from her firm's health and bio portfolio, is, she says,
  significantly speeding up preparation of Investigational New Drug
  applications for the US Food and Drug Administration and improving their
  quality. She uses it as her example of a single narrow workflow that is a
  large opportunity on its own terms.
- One company she describes breaks a relatively simple task into nine separate
  agents, some of which check and test the answers the others produce.
- Adoption depends on not threatening the user. Starting with work the end user
  dislikes doing gets them on your side; otherwise you get the familiar tension
  where the executive sees the return and the process engineer fears for their
  job.
- Kann's extension is that the largest budget is neither software nor labor but
  capital: maintenance spending, or a claim to extend asset life so the capital
  budget falls by 10%. Both agree it is very hard to sell upfront, for the
  timescale reason recorded below.

## Claims worth citing

All as stated on 2025-04-04. Everything here comes from a venture investor
describing her own portfolio and her conversations with founders, not from
measurement. The model-capability and cost figures date fastest.

- Prompt engineering alone gets a specialized product to roughly 70% to 90% of
  required performance, described as widely variable. (founders, relayed by
  Smith-Eppsteiner)
- Expected gross margins of roughly 40% to 70% for these businesses, against
  about 90% for traditional software, driven by inference cost. She attaches a
  condition to the figure: there are ways to manage inference cost, and she
  hopes it comes down over time. (Smith-Eppsteiner)
- Industrial customers have limited willingness to pay for software but spend
  heavily on labor, making labor the much larger budget to sell into. Whether
  these products actually reach that budget is explicitly unproven.
  (Smith-Eppsteiner)
- General models handle industrial text such as maintenance logs well but read
  technical diagrams, blueprints and 3D models poorly, because that material was
  not in their training data. (Smith-Eppsteiner)
- The last company to build a multi-billion-dollar, category-defining product
  selling to hardware engineers was started in the 1990s, possibly the 1980s.
  (Smith-Eppsteiner)
- One company uses nine separate agents to complete a single simple task,
  including compliance checking and testing of the answer. (Smith-Eppsteiner)
- On proving value: demonstrating the same work done with 20% of the people
  takes a week or two, while a ten-year asset-life claim takes thirty years to
  confirm. (Smith-Eppsteiner)
- DeepSeek and others have shown a path to cheaper, smaller models that a
  startup could viably build. She frames this as her hope, not a result.
  (Smith-Eppsteiner)

## Where it's contested

- **The thesis is offered as unsettled, at both ends of the conversation.** She
  opens with cases running both ways: high-growth general-purpose AI tools
  losing deals to vertical specialists, and law firms using Anthropic rather
  than a legal-specific tool like Harvey. Her stated position is that she does
  not know where this nets out, and the episode ends without resolving it.
- **Whether the data conditions are actually distinctive.** Pressed by Kann on
  whether siloed PDFs are special to physical industry, she scales the claim
  back to a difference of degree rather than kind. The argument rests on that
  qualified version, not the stronger one.
- **The moat is also the barrier.** Kann's version is strong: a company unable
  to obtain rights to train on customer data has no scalable product. She
  accepts it only as likely true. Either way it makes the defensibility case
  contingent on commercial terms rather than on technology.
- **The demand-side argument is weak by both accounts.** Kann calls the
  retirement wave a slow-release painkiller. She accepts it is a long-term trend
  and answers with what customers say rather than with what they buy.
- **Venture scale is unresolved.** Kann's worry is a landscape of hundreds of
  small companies solving real problems in markets too small to produce
  generational businesses. Her reply is a framework for judging stickiness and
  expansion, not evidence that the large outcomes are there.
- **No consensus on how to build one.** She reports founders saying
  incompatible things about embedding, fine-tuning and building their own
  models.
- **The evidence base is investor-sourced throughout.** The named examples are
  her own investments or her firm's portfolio companies, and the performance
  figures come from founders describing their own products. Nothing in this
  episode is independently measured or third-party tested.
