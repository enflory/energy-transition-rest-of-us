---
episode: "Has Humble Robotics cracked the code on autonomous trucking?"
published: "2026-05-07"
guest: "Eyal Cohen, founder and CEO, Humble Robotics"
threads: [trucking-and-freight, evs, ai-applications, robotics]
source_transcript: "transcript.md"
note_version: 1
disclosure: "EIP portfolio company. Kann says on air that EIP announced an investment in Humble Robotics a couple of weeks before recording. Common for this show; noted because every figure about Humble's vehicle is the company's design intent rather than a measured result."
---

## The question

Why is there still no Waymo of trucking ten years in, and does starting from a
clean sheet, both the vehicle and the software, change the answer?

## The answer

Nobody has cracked it, including Humble. Cohen's diagnosis is that highways
turned out to be harder than city streets for trucks, not easier, and that after
a decade of serious effort there is still no regular driverless trucking service
on the road. His bet is that building the vehicle and the autonomy stack
together fixes two specific problems, the blind spot created by pulling a
conventional trailer and the unit economics of bolting expensive sensors onto an
expensive tractor. The company is less than a year old and the episode contains
no test miles, driverless runs, customers or timelines, so the case is an
argument about design rather than a demonstrated result.

## The argument

The setup is an intuition that both speakers once held and that turned out to be
wrong. Highways look easier than San Francisco: you mostly go straight, and less
happens. That is why autonomous trucking outside defense began in 2016 with
Starsky Robotics and Otto, and why Otto's hundred-mile run with nobody in the
front seat made the problem look nearly solved. What went wrong is not that
highways have more edge cases but that they have different ones. They are rare,
so the system gets few chances to encounter and learn them, and they are far
less forgiving when they arrive, because the vehicle may weigh 80,000 pounds at
full gross weight and its stopping distance is long. Cohen jokes that a truck
with no perception system at all could probably hold a lane at 55 miles an hour
for 200 miles; the difficulty is entirely in the uncommon event. Underneath that
sits the asymmetry that matters most. A confused robotaxi can stop, which is
annoying and occasionally viral but usually safe. A truck that stops on a
highway, particularly past a bend or over a crest, has itself become the hazard.
The graceful fallback that makes passenger autonomy tractable simply does not
exist for trucking, and Cohen thinks that is much of why the timeline slipped.
Ten years on there have been driverless runs, but no regular driverless service,
and even the word driverless is contested: he notes that Aurora's driverless
runs sometimes carry a safety observer, citing the company's public writings.

What has changed since 2016 is the brain, and not much else. Early stacks were
hand-coded to the point of comparing pixel colors to find a lane line, and any
understanding of the world had to be labeled in by people drawing boxes around
objects. Today an off-the-shelf, sometimes open-source vision language model
arrives already carrying a usable interpretation of a scene, including the sort
of judgement that used to require explicit engineering: that a traffic cone
sitting on the back of a pickup is being carried rather than marking a work
zone. Cohen spent most of his career LiDAR-first and has flipped to camera-first
at Humble because of that shift. He will not take the sensor debate as a matter
of principle, though. For an 80,000-pound vehicle with very little margin for
error he wants camera, LiDAR and radar all present, with one of them doing the
heavy lifting depending on the task, since LiDAR cannot read a traffic light's
color, sees better at night, and radar can see through some weather. He accepts
that a human drives with what amounts to two cameras and that trucks may
eventually go vision-only, but treats that as an end state rather than as
today's engineering choice. Meanwhile the unglamorous parts, validation, safety
engineering and hardware robustness, have matured steadily and are reused. So
starting fresh means a new approach to the brain layered on well-understood
practice for everything else.

The vehicle follows from asking what the simplest possible freight mover would
be if no driver were ever involved: a box on wheels, a platform that carries a
container. Humble's truck is a cabless electric Class A vehicle that combines
tractor and trailer into a single platform, and the justification is both
technical and economic. Technically, a smart tractor pulling a conventional
trailer cannot see directly behind itself, which rules out handling someone
driving into the back of it and rules out backing into a dock, and produces
oddities like the legal requirement to deploy warning triangles behind a
stopped truck, something a driverless tractor cannot do; Cohen says Aurora, and
he thinks Waymo when it was working on trucking, proposed high-mounted lights
instead.
Economically, deleting the cab removes both cost and weight. He states the
counter-pressure himself: tractors and trailers are owned separately for good
reasons, trailers being cheap and tractors expensive, and they get detached and
sent in different directions, so a combined platform cuts against how the market
is organised. He calls this a lot of challenges and does not describe how it is
resolved.

Economics is where the episode's own question actually lands. Freight is a
business-to-business market with no cool factor to sell, so unlike Waymo, which
Kann says is currently getting away with inferior unit economics because riders
will pay more for the novelty, an autonomous truck has to save money to be
adopted at scale. The headroom is the driver's wage, roughly a dollar or a
little more out of a fully loaded long-haul cost of about $2.30 to $2.40 a mile
on the industry guide Cohen cites, and he prefaces the figures with a request
not to be quoted on them. Against that sit the sensors, remote assistance, and
the fact that retrofits use expensive high-end sleeper tractors because those
have room for the equipment, which makes an already costly vehicle much costlier
until scale arrives. Cohen's response is to attack the vehicle cost rather than
accept it, which is the actual argument for cablessness. He makes a parallel
structural objection to the dominant long-haul model: hub-to-hub only works if
the hubs exist, someone has to build them, and the short moves into and out of
them are friction competing against simply hauling the load door to door. Humble
instead targets short-haul and drayage, which is also where he thinks
electrification genuinely fits, since long haul demands a very large and heavy
battery and a great deal of charging power, a problem he says the industry still
has to reckon with.

## What you need to know first

- **Level four.** Cohen's shorthand for genuinely driverless operation. The
  industry's usage is looser than that, which is why he distinguishes a
  driverless run from one with a safety observer aboard.
- **Vision language model.** A model that takes an image and returns an
  interpretation of what is happening in it, described in the episode as the
  image-handling counterpart to the models behind chatbots. Useful ones are
  available off the shelf and sometimes open source.
- **Drayage.** Short-distance freight moves, particularly hauling containers out
  of ports. The segment Humble is aiming at, and the one where electric trucks
  are easiest to justify.
- **Hub-to-hub.** The standard long-haul autonomy plan: aggregate freight at a
  depot beside the highway, run it driverless for hundreds of miles, hand it off
  at a depot at the other end, with conventional short moves at each end.

## Details worth keeping

- Cohen joined Otto early, after working on passenger autonomy at Apple.
- The near-term state of play as he describes it: a few driverless runs, a
  company called Bot Auto claiming a first commercial driverless run on LinkedIn
  the day before recording, and no regular driverless service.
- Sensor division of labour: LiDAR is poor at traffic light color and better at
  night, radar can see through some weather, cameras carry the new intelligence.
  Long-range LiDAR was pushed to 300 or 400 meters specifically to cover a
  truck's stopping distance.
- Electric trucks have had a hard rollout in the US, partly on price, but China
  shows rapid uptake once the charging infrastructure and costs arrive. Cohen
  notes the Tesla Semi rolling out of production as helpful for inducing
  charging investment.
- Humble does not intend to build charging. Cohen says they have their hands
  full with autonomy and a clean-sheet vehicle and will instead help customers
  assemble depot, private and public charging solutions.
- Regulation is federal plus state by state. He names two federal trucking
  regulators only by their initials, NHTSA and FMCSA, and does not expand
  either. Texas has been the favorable testing jurisdiction.
- A cabless truck has no clean regulatory category. A windshield is required by
  law, and the vehicle looks like both a tractor and a trailer, so Humble is
  negotiating case by case whether it is regulated as a smart truck or a smart
  trailer. He describes regulators as constructive and motivated partly by what
  is being deployed in China.

## Claims worth citing

All as stated on 2026-05-07. Anything describing Humble's vehicle is the
founder's design intent for a company under a year old, not a measured or
third-party-verified result, and the regulatory and competitive specifics move
quickly.

- Waymo has driven 200 million miles on public roads; its first public ride
  service was December 2018. (Kann)
- US trucks hauled over 11.2 billion tons in the last year. (Kann)
- Autonomous trucking outside defense began in 2016 with two companies, Starsky
  Robotics and Otto; Otto did a hundred-mile run with nobody in the front seat
  that year. (Cohen)
- There is no regular driverless trucking service on highways today, ten years
  into serious effort. (Cohen)
- Aurora's runs described as driverless sometimes include a safety observer, per
  the company's public writings. (Aurora's public writings, cited by Cohen)
- A loaded truck can weigh 80,000 pounds at full gross weight. (Cohen)
- Long-range LiDAR for trucking has been developed to see 300 to 400 meters.
  (Cohen)
- Fully loaded long-haul trucking cost of about $2.30 to $2.40 per mile for 2025
  or 2026, with driver wages about a dollar or a little above it per mile.
  Cohen sources this to an industry cost guide he names only as ATRI and
  explicitly says not to quote him on the numbers. The transcript renders both
  figures loosely, so read the source before repeating them. (ATRI, cited by
  Cohen)
- Kann restates the driver share as 30 to 40 percent of the cost and Cohen says
  correct, though the figures as given work out somewhat higher. (Kann,
  affirmed by Cohen)
- Electric trucks have cost $400,000 to $500,000 in some cases against $150,000
  to $250,000 for a conventional tractor. (Cohen)
- Humble is less than a year old at the time of recording. (Cohen)
- California began permitting driverless trucks, with conditions, about a week
  before recording; it was not legal the week before. (Cohen)

## Where it's contested

- **The title's premise is not the guest's claim.** Cohen never says Humble has
  cracked anything. He describes a design rationale for a company under a year
  old, says they will see what the rollout looks like over time, and offers no
  miles, no driverless runs, no customers, no price and no schedule for his own
  vehicle. Kann's opening monologue puts it more strongly than Cohen does,
  saying the clean-sheet approach will allow Humble to dramatically accelerate
  adoption of trucking autonomy; Cohen's own framing is that the technology is
  now good enough to pull the long-arc vehicle forward a little.
- **The driver-share arithmetic.** Cohen gives the cost figures with a
  don't-quote-me caveat and the transcript garbles them; Kann's 30-to-40-percent
  restatement is lower than what Cohen's own numbers imply, and Cohen affirms it
  in passing. Treat the share as roughly two-fifths and unverified rather than
  as a precise figure.
- **The sensor question is left open deliberately.** Cohen declines the
  camera-versus-LiDAR argument as dogmatic, expects trucks may go vision-only
  eventually, and still wants all three sensor types on a truck today. Both
  positions are his.
- **Combining tractor and trailer fights the market's structure.** He raises the
  separate-ownership problem himself, calls it a lot of challenges, and leaves
  it there.
- **Electrification optimism is scoped.** He is bullish for short-haul and
  drayage and candid that long haul needs a very large, heavy battery and
  substantial charging power. Charging problems are solvable is an assertion,
  and Humble's plan is to help customers solve them rather than to solve them
  itself.
- **The long-haul forecast comes from an interested party.** Cohen predicts
  driverless trucks on highways very soon in specific segments, mostly in Texas,
  while saying there will be no generalized solution for a while. He is a
  competitor to the companies he is forecasting about, and a beneficiary of the
  category's credibility.
- **The regulatory path for a cabless vehicle does not exist yet.** A windshield
  is legally required and the vehicle does not fit either existing category. His
  answer is dialogue with regulators, which is a process rather than a
  resolution.
