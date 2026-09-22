---
episode: "Unpacking DOE's proposal to transform data center interconnection"
published: "2025-10-30"
guest: "Allison Clements, FERC commissioner 2020-2024, now partner at ASG and principal of 804 Advisory; and Tyler Norris, doctoral student, Duke University Nicholas School of the Environment"
threads: [interconnection, data-center-power, demand-flexibility, policy-and-regulation, energy-storage]
source_transcript: "transcript.md"
note_version: 1
---

## The question

The US Secretary of Energy has told federal regulators to rewrite how large
electricity loads connect to the grid. What does the proposal actually do, and
would it work?

## The answer

It does three things: claims federal jurisdiction over large-load interconnection
for the first time, directs that a load and a generator built together be studied
together rather than separately, and offers loads willing to be switched off a
fast lane with a study capped at 60 days. Both guests think the substance is
right and unusually well received, and both think the requested April deadline is
unrealistic. Clements' concern is not that the effort fails but that it moves too
fast, leaving undefined exactly the details, what curtailment is, how it is
bounded and how it gets paid for, that decide whether anyone uses it.

## The argument

Procedurally this is a letter, not a rule. Secretary Chris Wright used a
provision known as 403(b) in the statute that created the Department of Energy to
direct the Federal Energy Regulatory Commission to consider issuing an advance
notice of proposed rulemaking on large-load interconnection. It runs fourteen
pages against the twelve hundred of the regional transmission planning rule the
commission issued the previous year, so it is conceptual by design. The
commission can decline but must justify declining; the precedent people remember
is the 2017 letter under the neighboring provision asking it to subsidize coal
and nuclear plants that kept fuel on site, which it rejected unanimously.
Reception this time looks different. Rosner signaled eagerness, Senator Mike Lee
supported it from the other side of the aisle, and the stakeholders Norris has
seen view it favorably, though he adds that perspectives not yet heard will
surface and that the jurisdictional piece will draw objections from state
commissions and investor-owned utilities.

That jurisdictional claim is the part most likely to be fought. Under the Federal
Power Act the commission has the transmission system and wholesale sales, while
states keep generation and distribution. The fuzzy area is the transmission
portion of a bundled retail bill in a state with a vertically integrated utility,
where the state commission has historically overseen everything, including when a
new load may hook up. The commission has never asserted authority there, which
Clements attributes to tradition or practice rather than law: it does have
jurisdiction over practices affecting transmission rates, and little affects
those rates more directly than new loads connecting and the costs they impose.
Nothing about who does the work would change. The utility still runs the study,
still connects you, still names the cost, and the retail sale from a generator to
a data center stays with the state. What changes is who supervises, which is what
makes a standardized national approach possible instead of the current patchwork.
Norris frames the gap as an old puzzle: generator interconnection was
standardized twenty-three years ago and loads never got the equivalent.

The substantive heart is less about speed than about an accounting error. Today a
load interconnection request and a generation interconnection request are
considered independently, so when a utility studies a data center's withdrawal
during the most stressed hours to decide what upgrades the grid needs, it ignores
an on-site generator or battery that would be offsetting that withdrawal during
exactly those hours. The project therefore looks far more likely to trigger major
network upgrades, which cost a great deal and take years. Study the two together
and in many cases that requirement shrinks, which is why battery deals sized to
the full nameplate of a facility have started appearing, one announced as
accelerating interconnection by years. The curtailment fast lane applies the same
logic explicitly: a load that will stop drawing when the grid operator asks does
not impose the same worst-case burden, so it should not wait in the same line.

The catch is that almost everything determining whether this works sits in
details the letter does not contain. Clements' read, offered as instinct, is that
the commission rarely regulates to that level of specificity, has been skittish
about mandating standardization since standard market design collapsed in 2000,
and issues principles instead. Layer on a timeline where an advance notice draws
comments, becomes a proposed rule, draws comments again, and only then becomes a
rule. Her worry is a rushed rule that never defines what a curtailment service
is, whether you are selling energy or capacity, for how long, and how you get
paid. Norris supplies the shape of the missing answer: bounded flexibility, a
defined maximum of curtailed hours per year plus limits on event duration, since
unbounded obligation is exactly what large loads refuse. Partial precedent exists
in conditional firm transmission service, and the UK runs a curtailable
connections program that compensates the customer when curtailment exceeds the
guarantee. Both guests also warn against a rule so tied to on-site equipment that
it disadvantages nearby but not-behind-the-meter options, with the Federal Power
Act's non-discrimination requirement as the guardrail. And Norris makes the
argument that softens the whole risk: even if no rule issues, the record the
proceeding generates would be portable to states and grid operators.

## What you need to know first

- **Interconnection study and network upgrades.** Before a large facility can
  plug in, the utility models whether the system can serve it under stressed
  conditions. If it cannot, the customer pays for network upgrades: new wires and
  equipment costing a great deal and taking years. Nearly every delay and cost
  fight here traces back to that study and its assumptions.
- **Who regulates what.** The Federal Energy Regulatory Commission oversees the
  high-voltage transmission system and wholesale power sales; states oversee
  generation and local distribution. In states with a vertically integrated
  utility, the state commission has also overseen the transmission portion of the
  bill and the hookup decision. That is the authority this proposal would move.
- **Advance notice of proposed rulemaking.** The earliest formal step in federal
  rulemaking, used to gather comment before a proposed rule exists. The sequence
  runs advance notice, comments, proposed rule, comments, final rule, which is
  why the April deadline strikes both guests as implausible.
- **Curtailable load, behind and front of the meter.** A curtailable load agrees
  to stop or reduce its draw on request: by shutting down, by running on-site
  generation or batteries (behind the meter, on its own side of the connection
  point), by shifting or slowing computing work, or by paying someone else on the
  grid to cut demand instead (front of the meter).

## Details worth keeping

- Kann insists on a distinction the two uses of on-site equipment blur: an asset
  that gets you interconnected faster is not the same as an asset for backup
  power. Diesel generators carry runtime limits that likely rule them out for
  regular curtailment. Norris agrees, and notes the announced battery deals still
  keep diesel for long emergencies; the two are complements.
- Norris questions the 48-hour backup specification itself. An outage that long
  on a transmission-connected load implies an event on par with the largest
  blackouts in US history, the ones that produced the North American Electric
  Reliability Corporation. He doubts a data center would be prioritized for diesel
  deliveries over life-threatening needs, and notes storing that much fuel is
  itself hazardous.
- Duration arithmetic matters more than duration labels. A two-hour battery sized
  at 100% of nameplate becomes a four-hour resource if the goal is cutting draw
  by half, and scales from there.
- Clements lists the menu for a large load that must stop drawing: curtail
  outright, run diesel generators or the gas reciprocating engines now emerging,
  reduce compute intensity, shift compute elsewhere, or contract a third party
  such as a virtual power plant to curtail on its behalf.
- Interconnection studies today are steady-state snapshots, typically a summer
  case, a winter case and perhaps a shoulder-season case. Studying flexibility
  properly means extending to far more hours, maybe a thousand rather than all
  8,760. Norris says few transmission providers can do that today, and training
  more people to do it is part of the task.
- Clements relays a phrase that captures the direction: behind the meter and
  front of the meter are evolving into "around the meter". Storage sited close
  to, but not behind, a large load's connection point should not be written out.

## Claims worth citing

All as stated on 2025-10-30. This is a proposal at its earliest formal stage, so
procedural specifics and the deal examples will date quickly.

- The letter is fourteen pages; the regional transmission planning rule issued the
  previous year ran twelve hundred pages. (Clements)
- The proposal would cap interconnection study time for curtailable loads at 60
  days. (Clements)
- Order 2003 standardized large generator interconnection roughly twenty-three
  years ago. Clements says "23 years ago" and later "23 years ago, 25 years ago",
  so treat it as approximate. (Clements)
- The 2017 letter under the neighboring provision, asking the commission to
  subsidize coal and nuclear plants with on-site fuel, was rejected unanimously.
  (Clements)
- Order 1920 on regional transmission planning took four years from proposed rule
  to final, plus two rehearing orders. (Clements)
- Iron Mountain announced two-hour battery storage sized at 100% of its facility
  in New Jersey and again in Virginia. Caliber and Aligned Data Centers announced
  a two-hour battery for a new Pacific Northwest data center and said it
  accelerated interconnection on the order of years. (Norris)
- Two to six hours is widely recognized as the range covering most periods of
  system stress. (Norris)
- An E3 study using the Southwest Power Pool market found four-hour duration
  flexibility yields an effective load carrying capability, meaning the share of
  a resource's capacity that counts as firm, above 50% in many cases, close to
  some generation and longer-duration storage options. (E3 study, cited by
  Norris)
- Google told the PJM grid operator it might participate in demand response but
  for the fact that the program places no limit on curtailed hours. (Google
  comments, cited by Norris)

## Where it's contested

- **Jurisdiction is the real fight.** Clements believes the legal arguments are
  strong and cannot explain why the authority was never asserted. Norris expects
  objections from state commissioners and investor-owned utilities and says some
  of those concerns are legitimate. Clements separately names concerns about the
  commission's independence as something to acknowledge rather than dismiss.
- **The timeline is treated as unattainable.** Clements concludes there is no way
  to reach the required level of detail by April, calling visible progress a
  satisfactory outcome instead.
- **Her biggest stated concern is a rushed rule, not a failed one.** A rule that
  underspecifies what curtailment service is and how it is compensated would
  waste the opportunity while technically succeeding. How specific the commission
  will get is explicitly her instinct, separated from the political context she
  declines to discuss.
- **Whether nearby, non-on-site flexibility gets squeezed out.** Asked whether
  the proceeding could disadvantage emerging bring-your-own virtual power plant
  models, Clements answers that there is always a risk and points to the
  statute's non-discrimination requirement as the protection.
- **How much backup duration is actually needed is unsettled.** Norris calls
  whether to specify to 48 hours a live debate and does not resolve it.
- **No one here opposes the substance.** Both guests are favorably disposed and
  Norris says not all perspectives have surfaced, so the episode does not contain
  the strongest case against.
