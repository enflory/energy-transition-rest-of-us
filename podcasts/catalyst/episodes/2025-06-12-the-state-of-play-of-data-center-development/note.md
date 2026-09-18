---
episode: "The state of play of data center development"
published: "2025-06-12"
guest: "Chris Sharp, chief technology officer, Digital Realty"
threads: [data-center-power, ai-compute, interconnection, backup-power, load-growth]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Is the AI buildout spreading data centers out to wherever cheap power happens to
be, or concentrating them further into the regions that are already full?

## The answer

Concentrating them. Training frontier models did push some geographic spread, but
Sharp sees that leveling out, and the growth he expects from here is inference,
which wants to sit inside existing cloud regions and close to the data it runs
on. Chasing stranded power works for a narrow class of workloads and is shrinking
as a share of the market, which means the power constraint keeps binding in
exactly the places that are hardest to build.

## The argument

Sharp starts from the workload, because the workload dictates what infrastructure
a site needs. Training a frontier model is the part that can travel: you feed it
one large fixed data set, so the site mostly needs power, land, labor and water.
That did force broader regional deployment, and he thinks that wave is leveling
out. Inference is what he sees driving region-specific growth from here, and it
lands inside the existing cloud availability zones, the clusters near major city
centers built to hold uptime and performance commitments for enterprise
customers. Kann offers the standard lay version of this, training anywhere and
inference near users because latency matters, and then the more interesting
speculation on top of it: split inference into latency-sensitive and
latency-insensitive halves, and send the insensitive half out to cheap, clean,
possibly intermittent power in the middle of nowhere.

Sharp grants that this works, then explains why it is the shrinking half. Latency
is not really the binding property, because as long as latency is consistent most
workloads tolerate it. Throughput is the constraint, meaning the sheer volume of
data that has to move. Simple text-to-text inference can serve all of North
America from two or three markets, but he calls that an early-innings picture.
More advanced reasoning models do not generate one token against one prompt and
stop; a token may pass through several models to check for hallucination or to
route through a mixture of experts, so AI infrastructure increasingly wants to be
near other AI infrastructure. Real-time inference also wants to be near the data
it learns from, which sits in the tier-one markets. Chip economics push the same
way, since GPUs are expensive and training is spiky, so operators want to backfill
an installation with inference to raise utilization and return on invested
capital. Kann's summary, which Sharp endorses, is that going where the power is
retains real validity while the relative share of what can be built that way
dries up.

The consequence is that the constraint binds where it hurts most. Northern
Virginia is a multi-gigawatt market at roughly 0.5% vacancy, and Sharp is careful
about what is actually short there: not necessarily generation, but distribution.
Concept to delivery for a versatile data center runs about 24 months, some
interconnections now run longer than that, and utilities are asking for four-year
forward load projections. Transformer lead times are past 50 weeks and gas
turbines are backlogged beyond 2029. His two answers are unglamorous. One is
vendor-managed inventory, buying switchgear and long-lead equipment ahead of
need. The more important one is master planning with the utility over five years
or more, which he frames as a mutual credit test: a utility will not overbuild
unless it believes the load will show up and stay, so the developer's job is to
bring creditworthy customers who intend to occupy the asset for ten years or
more, and then actually take the power down when it said it would.

Two intuitions get overturned along the way. If inference arrives in
five-megawatt chunks, why not build a scatter of 120-megawatt sites, each easier
to interconnect than one two-gigawatt campus? Sharp says customers really do
think in five-megawatt blocks but want them contiguous, plugged into a single
hundred-megawatt hall for operations and resiliency; the customer indifferent to
location is the outlier. And like the grid, you have to size for the peak. The
second is the long-standing hope that some workloads could skip backup power and
be sited anywhere. Sharp wanted to build that facility and never saw one come to
market with an acceptable service-level agreement, and liquid cooling has made it
worse rather than better, because the heat does not displace itself and a stopped
pump ruins the chips. Bridge power lands the same way. Running a data center off
site generators until the interconnection arrives is an outlier; the common
version is a negotiated deal with the utility, bringing your own generation or
batteries under something like an interruptible tariff in exchange for faster
power. His reason is strategic rather than technical. Becoming a generator is a
short-term gap nobody would attempt absent the constraint, and he would rather
invest in the utility doing the thing it is already good at.

## What you need to know first

- **Training and inference.** Training builds the model once against a large
  fixed data set. Inference is running the finished model to answer requests,
  continuously. Almost every siting argument here turns on that split.
- **Availability zone.** A cluster of cloud capacity in a region carrying a
  specific uptime and performance promise. They sit near major city centers and
  do not exist in most smaller markets.
- **Throughput versus latency.** Latency is delay; throughput is how much data
  moves per unit time. Sharp's point is that consistent latency is usually
  tolerable while throughput is what actually pins a workload to a location.
- **Bridge power.** On-site generation covering the gap between when a data
  center wants to run and when its grid connection arrives.

## Details worth keeping

- The cold open is Sharp joking about "bragawatts," the noise of everyone
  claiming a gigawatt. His serious version: the power, and even the financing,
  required to meet the upper-end projections does not exist.
- He predicts failures that will get written about, from customers who secured a
  total capacity block but could not support the power density inside it, or who
  built for a spike whose long-run utilization came in far below projection.
- Demand is not uniformly for the largest possible building. Some customers want
  a contiguous hundred-megawatt GPU array, inference comes in roughly
  five-megawatt blocks, and private AI deployments can be a couple of megawatts
  embedded in a customer's existing footprint.
- Digital Realty operates almost three gigawatts of diesel generation today, some
  of it used for peak shaving as well as backup.
- Sharp frames AI as an "and" rather than an "or" to cloud, embedded into
  services people already buy rather than replacing them.
- Liquid cooling is his efficiency story and his reliability problem at once:
  liquid is 800 times denser than air, which improves efficiency, and it is also
  why he wants roughly three nines of reliability on the cooling loop.
- His closing example is Gefion in Copenhagen, one of the largest DGX pods, built
  for Novo Nordisk's pharmaceutical work.

## Claims worth citing

All figures as stated on 2025-06-12 and attributed to the speaker, not verified
independently. Lead times, backlogs and vacancy rates move fast.

- Northern Virginia has about a 0.5% vacancy rate in a multi-gigawatt market.
  (Sharp)
- All else equal, about 24 months from concept to delivery for a versatile data
  center; some interconnections now run longer than that. (Sharp)
- Utilities are requesting roughly four-year-ahead load projections. (Sharp)
- Transformer lead times are 50-plus weeks. (Sharp)
- Gas turbines are backlogged beyond 2029. (Sharp)
- Digital Realty operates almost three gigawatts of diesel generators. (Sharp)
- Liquid is 800 times denser than air. (Sharp)
- He describes a gigawatt-scale master-planned build near Dulles airport, and
  separately a 500-megawatt example of projecting load and then taking it down.
  (Sharp)
- On liquid-cooled builds he says billions and billions of dollars for a 30 to 35
  megawatt build scaling up to 50 megawatts. The sentence runs cost and capacity
  together, so what the billions are counting is not clear. (Sharp)
- Company and career context: Digital Realty around 20 years old, Sharp 10 years
  there and 15-plus years in the sector. (Sharp)

## Where it's contested

- **Whether flexible workloads migrate to stranded power.** Sharp says the
  approach is viable and then argues its share shrinks. He does not say it
  disappears, and nothing in the episode settles the question either way. It is
  also worth noting he runs technology for a colocation developer whose footprint
  sits in the tier-one markets his argument favors.
- **How much of the pipeline is real.** Kann frames it as two things being true
  at once: genuine explosive demand for compute, alongside a volume of load
  interconnection requests an order of magnitude larger than what will get built.
  Sharp agrees, says on record that Digital Realty works to avoid being aligned
  to a bubble, and separately says he only sees demand increasing. He puts no
  number on how much of the pipeline is noise.
- **The workload-flexibility hope is dismissed from experience, not analysis.**
  He says he was hopeful, never saw one built with the right service-level
  agreement, and concedes some individual components could carry less resiliency.
  That is weaker than saying it cannot be done.
- **Tapped out is scoped, not universal.** He says power has been tapped out in a
  lot of these markets, and in Northern Virginia specifically identifies
  distribution rather than generation as the shortfall. Both qualifiers are easy
  to drop, and the meaning changes if you do.
- **Customer specifics are off limits.** He declines to describe workloads he is
  building for particular customers and reasons instead from public
  announcements, so even the person building the buildings is partly inferring
  the workload picture from the outside.
