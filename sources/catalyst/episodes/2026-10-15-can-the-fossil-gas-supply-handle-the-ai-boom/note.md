---
episode: "Can the fossil gas supply handle the AI boom?"
published: "2026-10-15"
guest: "Eric McGuire, director of natural gas and LNG trading analytics, Wood Mackenzie"
threads: [gas-buildout, data-center-power, load-growth, backup-power]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Data centers are increasingly plugging straight into gas pipelines to avoid the
power grid. Is the natural gas system about to hit the same kind of capacity
crunch the electricity system already has?

## The answer

McGuire's answer is that gas is already constrained, regionally rather than
nationally, and that data center demand will matter more than its share of the
market suggests. Supply has kept pace with a doubling of demand over a decade
and he expects production to keep rising to meet new load, so he does not expect
sharply higher average prices. What he expects instead is more volatility and
more regional price dislocation, concentrated on the coldest winter days when
data centers, liquefied natural gas (LNG) exports and home heating all draw on
gas that freeze-offs have just taken away.

## The argument

Kann opens with a premise that leans toward reassurance. Historically it has
been easier to build gas pipelines than transmission lines, and easier to ramp
gas production, so gas should not suffer the same constraints as power. The
complication he names is LNG exports, a newer and much larger demand driver than
data centers for at least the next few years. McGuire's first answers partly
support the easier-than-power picture. Tapping an interstate pipeline means
negotiating a connection and committing to capacity, and the pipeline projects
he describes take anywhere from 8 months to 6 years, brownfield at the short
end and greenfield at the long. Kann calls that short by grid standards and
McGuire agrees: it is faster, faces less regulatory scrutiny and does not draw
on the grid. He adds that a Texas moratorium covers only grid-connected data
centers, so behind-the-meter ones there are still progressing. But asked
whether the pipeline system is constrained, he says it
has been for some time. The question used to be how to get enough gas to LNG
terminals, and now it is also how to get it to data centers.

Geography does most of the work in his account. Pipelines are generally easier
to build in Texas and the South than in the Northeast, where crossing many
states and populated areas brings environmental and regulatory hurdles.
Production has moved out of the Gulf Coast to West Texas, Colorado and the
Marcellus region in the Northeast, and with LNG growth Henry Hub, the national
benchmark in Louisiana, has become a premium location. Most regional gas prices
now trade *below* it, where they used to trade above it, though extreme markets
such as New England and California remain at a premium. Constrained takeaway
has also produced local gluts: early in the year Permian gas, largely a
byproduct of oil drilling, traded at a negative price because high oil prices
made producers willing to pay to be rid of gas that could not get out; and
Northeast producers appear to be shutting in gas now, as demand has dropped and
short-term outbound capacity is lacking. So the logical place for a gas-fed data
center is in the producing basins, close to supply, where it avoids competing
with LNG for long-haul pipeline space. Wood Mackenzie's risk assessment of
proposed data centers rates the ones in the basins as the most likely to be
built.

The turn comes in winter. Data centers and LNG are both baseload demand: they
draw steadily, barely respond to temperature, and at current prices barely
respond to price either. Everything else, heating above all, is the marginal
demand that swings on top. Cold snaps do not just raise demand, they also cut
supply, because liquids freeze at wellheads in the Permian and the South and
production drops. The market has stopped fearing that it will run out of gas by
the end of winter, but storage capacity has not grown alongside the market, so
the fear has moved to individual peak days in January and February. He reads
current pricing as saying there are already winter peak days when supply cannot
meet peak demand. His
expectation is that production will rise to meet new demand, especially demand
located in producing regions, and that the unsolved problem is deliverability:
who gets the gas on the coldest day.

The sharpest exchange is at the end. Kann offers a summary: data center gas
demand is meaningful but, next to the larger LNG driver and a gas system better
able to ramp, not earth-shattering the way it is for electricity. McGuire does
not accept it. Measured in volume LNG is bigger, he says, but markets price off
the marginal unit of demand, not the baseload. He no longer thinks the US gas
market trades as one market; it trades as many regional markets, more like
power does. Dropping large data center loads into the Permian or western
Pennsylvania will be revolutionary for those regions, setting up competition
with LNG terminals for local supply and, in the Northeast, with the cities that
gas currently flows to in winter.

## What you need to know first

- **Header.** The connection point where a new customer ties into an
interstate pipeline. A small header tie-in is routine; pulling large volumes
through an area without spare capacity means a pipeline expansion and much
more scrutiny.
- **Firm versus interruptible capacity.** Firm capacity is paid for with a
reservation fee whether or not you use it, and is cut last. Interruptible
capacity is cut first. Taking delivery at a different point than the path you
paid for lowers your priority.
- **Freeze-off.** Production lost when liquids at the wellhead freeze in
extreme cold. It removes supply at exactly the moment demand spikes.
- **Henry Hub and regional spreads.** Henry Hub, a small location in southeast
Louisiana, is the national balancing point and reference price for US gas.
Regional prices trade as a premium or discount to it; McGuire explains today's
discounts by production having moved away from the Gulf, so that gas now flows
back toward Henry Hub.

## Details worth keeping

- How a large pipeline contract works: a big new user is asked to be a
"backbone shipper," committing to ten or more years of capacity and paying a
use-it-or-lose-it reservation fee. On an existing pipeline a term might be three
years, but McGuire says a data center would want the longest term it could get.
- In a force majeure event, where a pipeline loses capacity, interruptible
shippers can be cut entirely and even firm shippers get cut. He says a major
one was under way in the Northeast at recording.
- McGuire says pipeline reliability is generally very good, and in his first
job as a junior trader he priced expected downtime pipeline by pipeline. His
point is that for a data center even a few days a year matters, so operators
must either price that into the compute they sell or arrange other energy
sources.
- Building storage needs wide seasonal price spreads to justify it. Most is
depleted-reservoir storage, meaning old gas fields refilled. Little has been
built, though he thinks today's wider spreads are bringing new projects online
and into proposal.
- The fear indicator traders used to watch, the March-to-April spread nicknamed
the "widowmaker," has collapsed. The spread to watch now runs from January or
February to March.
- LNG contracts are long-term bilateral deals with a cargo due in another
country 15 to 30 days later, so sellers cannot unwind them on screen. He thinks
the only economic shut-in of US LNG came during COVID, and only once the European price
had fallen all the way to Henry Hub, not merely once the margin no longer
covered shipping.
- The drops in LNG exports during cold snaps line up closely with freeze-offs.
His reading is that this is supply disappearing, not exporters choosing to
sell gas at home.

## Claims worth citing

All figures as stated on 2026-10-15. Several are given "off the top of my
head," and prices and spreads move quickly.

- A new pipeline connection or build takes 8 months to 6 years; brownfield
work, building on existing capacity, about 8 months. (McGuire, citing Wood
Mackenzie analysis)
- The US gas market has almost doubled in ten years, with production rising
from about 65 to a recent high of about 112 or 113 billion cubic feet a day.
(McGuire)
- LNG exports run at around 19 billion cubic feet a day, which he rounds to 20
against a market he rounds down to 110. (McGuire)
- Up to 5 billion cubic feet a day of behind-the-meter gas demand is expected
over the next five years. (Wood Mackenzie analysis, cited by McGuire) Kann
later calls this 4% or 5%, "5 out of 120," though McGuire's own base was
about 110. (Kann)
- Winter Storm Fern produced almost 18 billion cubic feet a day of freeze-offs
nationally. He puts the whole event at about 350 billion cubic feet, 120 of it
supply loss and about 220 demand gain. The parts sum to 340 rather than 350;
he flags these as from memory. (McGuire)
- During Fern, Henry Hub printed a high close to $50 and averaged about $30 for
the day; the Permian reached about $17 or $18 before trading negative in the
following months. Prices are per MMBtu, the standard gas pricing unit, which
the episode does not spell out. (McGuire)
- Northeast gas is trading under a dollar, with what look like production
shut-ins. (McGuire)
- The March-April 2027 spread is about 10 cents. (McGuire, "I think")
- Wood Mackenzie tracks "over 900 gigawatts" of proposed data centers, of which
it expects significantly fewer to be built, with basin locations rated most
likely. He gives no figure for the risked total. (McGuire)
- Three days of downtime a year would be roughly 99% uptime, against data
centers' usual expectation of three to five nines. This is Kann's arithmetic on
McGuire's hypothetical, not a measured pipeline outage rate. (Kann)

## Where it's contested

- **The host's summary and the guest's verdict diverge.** Kann's wrap-up says
data centers are meaningful for gas but not earth-shattering. McGuire answers
"I don't know," says he may have done data centers "a disservice," and argues
the opposite: because markets price at the margin, the effect will be large,
regionally and above all in winter. The note follows the guest.
- **The monologue's "easier than power" premise is only partly borne out.**
McGuire agrees connections are faster and less scrutinized, but says the system
has been constrained for some time and that ease of building pipelines depends
heavily on region.
- **His price outlook is explicitly personal and hedged.** Speaking "just me
personally," he expects some support for prices and some increase, but is not
very bullish and does not expect a return to $10 gas. His real claim is about
volatility, not level.
- **Production keeping pace is an expectation, not a certainty.** It rests on
history (supply has met every increase so far) and current breakevens, and
nobody tests it. He himself limits it: rising production does not, on his
account, solve peak-day winter deliverability.
- **Price-insensitivity of data centers is Kann's statement.** McGuire says
baseload demand will not swing much "at least right now" because it is all in
the money, which is narrower.
- **Unexamined:** Kann's report that some gas-fed data centers skip backup
generators is secondhand ("I've heard talk"), and nobody discusses how those sites would ride
through the peak-day shortfalls the episode describes.
