---
episode: "Fresh intel from state utility regulatory filings"
published: "2025-07-03"
guest: "Nat Bullard, co-founder, Halcyon"
threads: [policy-and-regulation, utility-business, data-center-power, electricity-prices, gas-buildout]
source_transcript: "transcript.md"
note_version: 1
---

## The question

What do state utility regulatory filings actually reveal right now about how
utilities are absorbing data center load, and about where costs are heading?

## The answer

They reveal that individual customers are now large enough to reshape whole
utility territories, and that the regulatory machinery for handling them is
being improvised in public, docket by docket. They do not reveal the number
everyone wants, which is what large loads will actually pay; that is either
redacted as commercially sensitive or still under deliberation. Where the record
is complete enough to build a dataset from, it shows new combined-cycle gas
plants, the standard design for large new gas generation, costing roughly double
both their own price a couple of years earlier and the federal government's own
published benchmark.

## The argument

Public utility commissions are where electricity actually gets decided, and they
publish an enormous amount in the process. The problem is the form: esoteric,
long, hard-to-read PDFs, with the redaction landing precisely on the number you
want. Halcyon's approach is to use large language models to pull structure out of
these documents at scale, which is what makes a cross-state canvass possible.
The first thing that falls out is scale. Pennsylvania's commission convened an en
banc hearing on large load interconnection, meaning all the commissioners sitting
at once. Bullard had never seen one; an advisor told him it almost never happens
outside of something market-defining like restructuring a generation fleet. It
pulled every intervenor and expert witness into one room, and the testimony is
where the eye-popping numbers sit. Duquesne Light, with a relatively small
service territory, said four projects in advanced stages of connection could add
40% to its demand, and one large hyperscale project could add 30% on its own.
Rappahannock Electric Cooperative in Virginia has a 1.2 gigawatt summer peak and
individual interconnection requests four times that size.

Numbers like that force a regulatory construct that does not exist yet, and the
dockets are where it is being invented. Bullard reduces it to two questions: how
does the build get paid for when you are building on behalf of a handful of
customers rather than a hundred thousand, and what happens if the customer never
shows up. The second is the one he thinks has been left out of the conversation.
Anyone in power generation takes for granted that not every announced project
gets built, but that discipline has never been applied to the demand side, and
asked whether every planned hyperscale data center on paper will be built,
Bullard's answer is flatly no. Kann extends it a step: even the ones that get
built are being underwritten by tariffs that assume payment over a decade or two,
and that assumption can change fast.

The dockets also show the second-order effect, which is incumbent large loads
elbowing into proceedings that are ostensibly about data centers. East Kentucky
Power Cooperative is working a custom large-load tariff through its commission,
and Nucor, the mini-mill steel producer and the region's biggest load, filed as
an intervenor. Bullard reads that as a useful reminder that other large loads
exist, alongside things like the Ford and SK On battery plant nearby, and as a
caution about a world where everybody gets a bespoke tariff. Kann pushes it
further, into an inference the filings do not make: because large-load
interconnection capacity is genuinely limited, anything that is not a data
center is now competing with data centers for sites, and he says it is getting
harder to site manufacturing, industrial electrification, even medium- and
heavy-duty fleet charging. Bullard adds the asymmetry underneath that. Data
centers are a class of customer almost uniquely underexposed to the price of
electricity relative to what access to it is worth. Raise power prices 30% and
the cost of steel from an electric arc furnace moves materially; do the same to a
training run, where the premium is on speed, and it barely registers. That is a
clean argument in principle, and when Kann asks the obvious follow-up, whether
large-load tariffs are in fact being set at a premium to other industrial rates
and whether data centers are accepting them, the filings go quiet. Bullard says
it is partly redaction and mostly that these are early and under deliberation,
with the terms that matter unknown: whether the premium is an adder to an
existing rate or a new flat rate, whether it escalates, how long it runs.

The rate side is where the filings are most legible and least reassuring.
Bullard deliberately looked at small service territories, which get less
scrutiny, serve a smaller customer base that is often almost entirely
residential with few large ratepayers, and can go a decade between rate resets,
so the reset arrives as a nonlinear jump rather than a drift. A Vermont village
electric and light department asked for roughly a 21.5% increase
effective July 1 on a timeline with none of the years-long California-style
process, and the state Department of Public Service pushed back that it needed a
conference first. A Mississippi operator is collapsing three residential tiers
into a single statewide flat rate for water and sewer, which lands hardest on
whoever was in the lowest tier. Bullard's point is that rate increases are
inherently regressive and that these are appearing everywhere at once. The gas
cost work is the counterweight and the episode's best demonstration of why this
mining exercise is worth doing. The NextEra chief executive's roughly $2,400 per
kilowatt figure for a new gas plant, delivered from a conference stage, had
become gospel through third-hand repetition. Bullard set out to demystify it and
found the opposite of a debunking: canvassing more than 100 plants and about 55
gigawatts across all 50 states, he gets a figure in the low $2,200s per kilowatt
for plants landing in 2031 and 2032, as best the garbled transcript can be read,
legitimately double the price of a couple of years earlier. The figure that
fails is the official one. The Energy Information Administration's 2024
cost-of-generation benchmark of about $1,100 to $1,200 per kilowatt is, in
Bullard's words, a conclusion not found in evidence.

## What you need to know first

- **Public utility commission docket.** A state regulator's case file on a
  proposed rate, tariff or plan. Utilities file, outside parties intervene, and
  the whole record is public unless redacted. It is the primary source here.
- **Intervenor.** A party that formally joins someone else's proceeding because
  the outcome affects it. Nucor intervening in a data center tariff case is a
  steel company buying a seat at a table it was not invited to.
- **En banc hearing.** All of a commission's members sitting on one matter at
  once, rather than the usual single presiding officer. Rare, and a signal that
  the commission treats the question as defining for the state.
- **Large load tariff.** A custom rate structure for a single enormous customer,
  covering who pays for the upgrades, on what schedule, and what happens if the
  customer does not materialize.

## Details worth keeping

- The redaction pattern is the recurring frustration: page after page survives
  and the single number that says what the gas plant costs, or what mode the
  data center will run in, is blacked out for trade-secret reasons.
- Bullard describes the volume of disclosure as its own defense mechanism, a
  denial-of-service attack by public record. His example is a landscape-printed
  PDF of an Excel file converted into 1,500 JPEGs and uploaded in one go.
- His historical analogy for the current moment is the 1930s far-west buildout:
  state-built generation, government-owned transmission, and coincident large
  loads such as smelters, whose eventual departure left the spare grid capacity
  that data centers have been using up. Kann floated two alternatives, the gas
  buildout and state deregulation, and Bullard accepted both as partial. His
  point is that nobody has the muscle memory: people have handled rapid growth,
  or deregulation, or large-load customers, but not all three at once plus a new
  kind of large-load customer with unfamiliar characteristics.
- South Dakota has a one-of-one tariff in process: Otter Tail designed a rate
  schedule applicable essentially only to Antora, which received a state grant in
  April alongside an international cheesemaker. Details are still largely
  obscured. Bullard's read is that you do not have to be the world's biggest
  company to get a custom tariff, but you may need to be in a small territory.
- Kann's investable read on rising rates is distributed energy resources plus,
  on a colleague's suggestion rather than his own instinct, energy efficiency,
  which he calls unloved in tech and venture circles. Bullard's
  counter-history: in the Cleantech 1.0 era, showing people real bill savings did
  not move them the way offsetting all their demand with a home solar contract
  did, and the psychology of getting less is a hard sell.

## Claims worth citing

All as stated on 2025-07-03. Nearly every docket described here was pending at
the time, so treat outcomes as unresolved rather than decided, and treat gas
plant costs as a fast-moving quantity.

- Duquesne Light: four projects in advanced stages of connection could add 40% to
  its demand; one large hyperscale project could add about 30% on its own.
  (Duquesne Light testimony in the Pennsylvania en banc proceeding, cited by
  Bullard)
- Rappahannock Electric Cooperative: 1.2 gigawatt summer peak load, with
  individual interconnection requests four times that size. (cooperative's
  filing, cited by Bullard)
- New combined-cycle gas plants price at roughly $2,220 to $2,240 per kilowatt
  for 2031 and 2032, about double a couple of years earlier, from a canvass of
  more than 100 plants and about 55 gigawatts across all 50 states. The
  transcript garbles the figure itself, so read it as low-$2,200s per kilowatt
  rather than a precise range. (Bullard, Halcyon)
- Roughly $2,400 per kilowatt for a new gas plant, stated from a conference
  stage (the venue name is garbled in the transcript) and since repeated
  third-hand as established fact. Bullard's own data says the number is close to
  right. (NextEra chief executive, cited by Bullard)
- The Energy Information Administration's 2024 cost-of-generation publication put
  combined-cycle capacity at roughly $1,100 to $1,200 per kilowatt, which Bullard
  calls a conclusion not found in evidence. (Energy Information Administration,
  cited by Bullard)
- A Vermont village electric and light department requested about a 21.5% rate
  increase effective July 1; the Department of Public Service pushed back and
  called for a conference. The utility's name is garbled in the transcript and
  the percentage is stated twice in mangled form, so verify both before quoting.
  (Bullard)
- A Mississippi operator, transcribed as the Great River Utility Operating
  Company, is eliminating tiered and mitigated residential rates in favor of a
  single statewide flat rate for water and sewer. Bullard estimates the old
  mitigated residential rate may have been about a third of the new rate, and
  hedges the estimate. (Bullard)
- US electricity load growth ran close to 10% per year in the 1950s. (Bullard)
- The Ford and SK On battery plant in the region is a couple hundred megawatts of
  load on its own. (Bullard)

## Where it's contested

- **The most decision-relevant question in the episode goes unanswered, and the
  guest says so plainly.** Whether large-load tariffs are actually priced above
  other industrial rates, and whether data centers are accepting them, cannot be
  established from the filings yet. Bullard cites both redaction and the fact
  that most of these are early and under deliberation, and lists the terms still
  unknown: adder or flat rate, escalation, duration.
- **Distinguish the filings from the inferences drawn around them.** The
  Pennsylvania and Virginia load numbers, the Kentucky intervention, the rate
  requests and the gas cost dataset are primary-source material. The claims built
  on top of them are not: Kann's assertion that data centers are crowding
  everything else out of viable sites is his own market observation, stated with
  high confidence and unsupported by any document cited here, and the
  willingness-to-pay asymmetry is an argument in principle that the episode
  explicitly fails to confirm in practice.
- **Bullard's gas cost figure is a canvass, not a census.** He stresses that the
  right posture is a change log rather than a fixed number, because prices,
  timelines and construction costs will move, and because project cost disclosure
  is not systematic. It surfaces through responses to information requests inside
  particular proceedings rather than any standard filing.
- **He set out to check a widely-repeated figure and largely confirmed it.**
  Worth noting the direction of that surprise. The number he ends up calling
  unsupported is the government benchmark, not the executive's stage remark.
- **Whether announced load materializes is unresolved by construction.** Both
  agree that not all of it will be built and neither will say how much or which.
  Kann adds the further uncertainty of how long the plants that do get built will
  operate under the tariffs being written now.
- **Energy efficiency is an open disagreement.** Kann treats it as an obvious bet
  in a rising-rate environment; Bullard answers with the historical failure mode
  and ends on "I don't really know" rather than agreeing.
- **The historical analogy is offered as a posit.** Bullard frames the 1930s
  comparison as something he would argue rather than something established, and
  Kann's competing candidates were left standing.
