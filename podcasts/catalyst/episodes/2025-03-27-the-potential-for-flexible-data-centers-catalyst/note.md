---
episode: "The potential for flexible data centers | Catalyst"
published: "2025-03-27"
guest: "Tyler Norris, PhD candidate, Nicholas School of the Environment, Duke University"
threads: [demand-flexibility, data-center-power, interconnection, load-growth]
source_transcript: "transcript.md"
note_version: 1
age_warning: "Recorded 2025-03, when almost no utility had a standing large-load flexibility tariff. The headroom analysis is durable; the snapshot of programs, deals and installed data center capacity is a moment in time."
---

## The question

How much additional data center load could the existing US grid absorb if that
load agreed to be a little bit flexible?

## The answer

A great deal, on the study's terms: up to 98 gigawatts of new data center load at
half a percent curtailment, or 76 gigawatts at a quarter percent. The terms are
doing heavy work. That curtailment is measured as a share of the new load's
maximum potential annual energy rather than a share of hours, the headroom is
calculated against generation and historical peaks only, and transmission and
distribution constraints are not modeled at all.

## The argument

The study started from a contradiction. Utility regulators in the southeast told
Norris and his co-authors in the fall that they had been told data centers are
100% inflexible, so they were planning for all of it as firm load. At the same
time the Secretary of Energy Advisory Board had issued recommendations on data
center flexibility and the Electric Power Research Institute had launched a
flexibility initiative. Both cannot be right. The question matters because the
power system is sized for rare extremes, heat waves and polar vortex cold snaps,
so much of it sits idle most of the time. Across the 22 largest balancing
authorities, covering roughly 95% of US load, the average load factor is 53%,
meaning average consumption is about half of peak consumption. In 90% of hours
more than 30% of the system goes unused. If a new load could be added that
simply never showed up at those extremes, the question is how much of that idle
capacity it could occupy.

The method is what makes the answer defensible, and it is also where the
conditions live. Norris calibrated to each balancing authority's realized peaks
over the past nine years and required that new load never push a realized peak
above them, which deliberately leaves unused the reserve margin, the cushion of
spare generating capacity a system carries above its peak. That choice is
conservative, since the numbers would be larger if reserve margin counted; it
also means the added load does not lean on the dirtiest, least efficient units.
The team originally planned to model one to five percent curtailment, one to two
percent being roughly what existing demand response programs ask for. The
results came back so large they ran it down to 0.5% and then 0.25%. The critical
thing to understand about those numbers, which Kann first restated as a share of
hours before the two of them settled on the right reading, is that they are
percentages of the new load's maximum potential
annual energy consumption, not percentages of hours. The model assumes the new
data centers otherwise run at 100% utilization constantly. The budget is
therefore energy and not hours, and it can be spent as many shallow reductions
instead of a few full shutdowns, which means curtailment touches more hours of
the year than the headline percentage suggests.

That distinction is what makes the ask plausible operationally. At the 0.25%
setting, curtailment of some amount would be required in about 85 hours a year
on average, and in 73 of those 85 hours at least half the new load is retained,
in 50 of them at least three quarters. This is mostly partial dimming, not
switching off. The extreme peaks themselves average two and a half to five
hours, and Norris says forecasting has improved enough to see polar vortex
events coming up to two weeks out, so at least the cold-snap events are short
and can be anticipated. The menu of responses is correspondingly wide: defer or
front-load a training run, shift workloads
between data centers in different markets, lean on on-site generation or
storage, or reduce cooling, which is a large share of data center draw and is
conveniently not needed at full power on the winter mornings when the southeast
actually peaks. Straight reduction of operations is the last resort and the one
operators like least.

The catch is that the study answers the generation question and not the
deliverability question. In many places the binding constraint is not whether
there is enough power but whether the wires can carry it to that spot under
contingency conditions. Asked how much of the 98 gigawatts survives real
transmission and distribution limits, Norris said there is no way to know
without running it, then under pressure offered roughly 10% erosion as a guess
he immediately labeled as just him talking. Kann was audibly skeptical it could
be that small. Norris's counter is that full deliverability is an extremely
strict criterion tested against conditions
that are genuinely rare, and that load and generation can be connected before
those upgrades are finished, which is how ERCOT, the Texas grid operator, gets
generation online faster. The second catch is institutional rather than
physical. This is not simply enrolling data centers in demand response, which
Norris calls a simplistic reading, because existing participants were planned as
firm load and opted in later for economic reasons. Doing this properly means
treating the load as flexible in the planning and
interconnection study itself, which is a different act by a different set of
people. And the market is arranged against it: financing counterparties and
owner-operators are used to firm service as the gold standard, and hyperscalers
have competitive reasons not to disclose what they can actually do. The lever
most likely to break that open, in Norris's view, is an explicit trade of
flexibility for a faster grid connection.

## What you need to know first

- **Balancing authority.** The entity responsible for matching supply and demand
  across a defined chunk of the grid. The study covers the 22 largest, roughly
  95% of US electricity load, and computes headroom separately for each.
- **Load factor.** Average consumption divided by peak consumption. A 53% load
  factor means the system is on average running at about half of what it was
  built to deliver, which is the idle capacity this study is trying to sell.
- **The curtailment metric.** Not hours. A share of the maximum energy the new
  load would use running flat out all year, spendable as partial reductions.
- **Deliverability.** The standard that a grid connection has no bottlenecks
  even under contingencies with all local generators running at once. Norris
  calls the word a misnomer, since failing the test does not mean electrons
  cannot reach the load in ordinary conditions.

## Details worth keeping

- The programs that exist are thin. ERCOT has a controllable load service that
  makes the trade explicit. Pacific Gas and Electric's Flex Connect works mostly
  at distribution scale for electric vehicle chargers, with hopes of expanding
  it, and Southern California Edison runs something similar. What is missing is
  an established published offering for large loads that says what flexibility
  buys you in interconnection time.
- Bridge power may solve the economics by accident. Data centers increasingly
  bring their own generation, often gas, to start operating before the grid
  connection arrives. Once the grid connection lands, that already-amortized
  asset can become the curtailment backstop, running a fraction of a percent of
  hours, which would never pencil if bought for that purpose alone. Norris
  agreed and said the better version is leasing, so the equipment moves on to
  the next customer; he described a California company building that model with
  trucked-in lithium-ion batteries.
- Norris pushes back on the 24-7 framing itself. Servers may run continuously,
  but a data center does not draw its maximum all year, and he thinks regulators
  have been badly confused on this point.
- Crypto mining is the most flexible large computational load on the system
  today, able to go from maximum draw to zero within a minute or a few minutes.
- He is explicit that none of this is an argument against building generation
  and transmission, which he says are needed for other loads, decarbonization
  and reliability regardless.

## Claims worth citing

All figures as stated on 2025-03-27. The program and deal landscape in this
episode is the fastest-moving part and should be assumed stale; the study's
structural findings are more durable.

- Up to 98 gigawatts of new data center load could be added at 0.5% curtailment
  of that new load's annual energy, and 76 gigawatts at 0.25%, across 22
  balancing authorities representing about 95% of US load. (Norris, Duke
  University study)
- That is roughly three to five Project Stargates, the data center initiative
  announced by President Trump and OpenAI in January. (Norris)
- Average load factor across those 22 balancing authorities is 53%; in 90% of
  hours more than 30% of the power system sits unused. (Norris)
- At the 0.25% setting, curtailment would be needed in about 85 hours per year
  on average; in 73 of those hours at least 50% of the new load is retained, and
  in 50 of them at least 75%. (Norris)
- Extreme peak events last on the order of two and a half to five hours.
  (Norris)
- Forecasts suggest AI-specialized data centers will be the single largest
  driver of US load growth for the next five to seven years, with some putting
  data centers at about 44% of all US load growth. (forecasts cited by Norris)
- Existing demand response programs typically ask for peak shaving in the range
  of 1% to 2%. (Norris)
- Roughly 10% of the 98 gigawatts might be eroded by transmission and
  distribution constraints. Norris volunteered this only under pressure and
  called it a very rough first-order estimate, "just me talking." Treat it as a
  guess, not a finding. (Norris)
- Data center utilization rates in circulation differ sharply: Lawrence Berkeley
  National Laboratory's congressionally mandated December report used 50%, while
  the Energy Information Administration and E3 have used numbers closer to 85%.
  (cited by Norris)
- Existing operating data center load on the US grid is under 30 gigawatts.
  (Kann, who explicitly said he did not know the exact current number)
- Duke Energy said at a public event the week before recording that it will
  require all new hyperscale loads above 100 megawatts to participate in demand
  response. Norris described himself as quite surprised by it. (Duke Energy
  public statement, reported by Norris)

## Where it's contested

- **The deliverability gap is the study's biggest open question and the guest
  says so.** The model constrains against generation and historical peaks, not
  against transmission and distribution. Norris declined to quantify it, then
  gave 10% as an off-the-cuff figure, and Kann pushed back that it sounded low.
  Anyone repeating the 98 gigawatt number without this caveat is repeating a
  generation-side headroom estimate as though it were a buildable number.
- **The host restated the core metric incorrectly at first.** Kann described the
  curtailment as a percentage of hours in which the data center would shut off.
  Norris half-agreed and then restated it as a share of maximum potential annual
  energy use, and Kann drew the distinction himself a moment later. The two are
  not interchangeable: an energy budget can be spent across many partly curtailed
  hours, so curtailment is called on in more hours than the percentage suggests,
  while each of those hours is usually only a partial reduction.
- **Conservatism runs in both directions.** Excluding reserve margin makes the
  number smaller than it could be; omitting transmission constraints, and limits
  on how fast generation and load can move from hour to hour, makes it larger.
  Norris names both and does not claim the errors cancel.
- **Whether operators will actually take the deal is untested.** Hyperscalers
  and colocation developers publicly maintain they are not flexible; Norris
  thinks they are underdisclosing deliberately, both to keep negotiating
  leverage and to hide capability from competitors. Financing counterparties are
  accustomed to firm service. His expectation that faster interconnection will
  be the wedge, and that flexibility deals will then spread beyond speed to
  power, is a forecast about market psychology, not a modeled result. He notes
  the live negotiations are bilateral and confidential, so the evidence is thin
  by construction.
- **This is not just demand response with a new name.** Kann floated that
  shorthand; Norris called it simplistic and drew the distinction between load
  that was planned firm and opted in later versus load planned as flexible from
  the interconnection study onward.
- **Kann calls it harder than it sounds and explicitly not a panacea** in his
  opening, and the episode never resolves whether the regulatory and contractual
  machinery to capture this headroom can be built.
