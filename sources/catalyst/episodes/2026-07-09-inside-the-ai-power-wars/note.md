---
episode: "Inside the AI power wars"
published: "2026-07-09"
guest: "Jeremie Eliahou Ontiveros, leads infrastructure and power research, SemiAnalysis"
threads: [ai-compute, data-center-power, gas-buildout, venture-and-finance, interconnection]
source_transcript: "transcript.md"
note_version: 1
---

## The question

Everyone can describe how the AI companies differ on chips. How do they differ
on power?

## The answer

A lot, and the differences sort along two axes: how much balance sheet a company
has, and whether it owes anyone else uptime. Google and Amazon spend credit
blanketing utilities with deposits for future grid capacity, while Meta and the
operators the AI labs lease from bring generation on site to control the delivery
date. Underneath both sits one selection criterion, speed to power, which is also
why nuclear and geothermal deals look structurally different from everything else
being signed.

## The argument

The hyperscalers are not interchangeable. Ontiveros puts Google at the frontier:
the biggest energy trading desks, large load flexibility deals, and a name that
appears in the proceedings of grid operators like PJM and ERCOT more than anyone
else's. Kann traces that to
a history of early power purchase agreements, the first 24/7 clean energy
commitment, and shifting workloads geographically for carbon reasons well before
AI made flexibility fashionable. Microsoft was the clear second for years;
Ontiveros now ranks it fourth, in a market where the few people who know how to
procure data center power change jobs the way AI researchers do. Amazon rose on
unusual deals such as Talen and Vistra's Comanche Peak. Meta does the strangest
things for a structural rather than cultural reason: with no cloud business it
serves only its own workloads and builds for itself rather than for maximum
fungibility, which Kann suggests may free it from the four nines the others owe
customers. That is how it can run behind-the-meter gas with roughly 10 megawatts
of backup on a 100 megawatt site.

Why go behind the meter? Almost none of it is off-grid ambition. These are
bridges to a grid connection expected in a few years, and the case is arithmetic.
Buildout runs in the tens of gigawatts a year growing around 50% annually,
against maybe five or six gigawatts of gas next year and twenty to twenty-five
gigawatts of nameplate solar and batteries worth far less once adjusted for peak
contribution. Utility commitments are also soft: the story he says every
developer tells is a promised gigawatt by 2027 revised to a hundred megawatts by
2029 with the gigawatt in 2042, and no penalty for missing. For a lab that is
intolerable, because power is revenue rather than overhead. Anthropic goes from
about 1.5 gigawatts at the end of 2025 to wanting more than 10 by 2027, the size
of Google in two years, and nobody commits that capital against a date somebody
else controls. But Kann declines the framing. He bets far more generation gets
added and argues the chokepoint is transmission and distribution, where a
substation upgrade or a high-voltage transformer runs years. Pressed, he guesses
roughly 35 gigawatts total for 2027 or 2028; Ontiveros's adjusted figures are
lower and he calls both small against fifty gigawatts a year of data centers.
They disagree about which constraint binds first, not whether one does.

The reframe is the most useful thing here: ask about the AI labs rather than the
hyperscalers, because roughly half of what Amazon and Microsoft build now goes to
OpenAI and Anthropic. The labs' binding limit is credit, not ambition. They are
not investment grade, the capital is front-loaded, and a construction loan at
high loan-to-cost needs an investment-grade signature. That gap is the product
hyperscalers sell into, and Google's response was the aggressive one. Instead of
buying equity the way Nvidia did with the neoclouds, the specialist GPU rental
companies, Google lent its own credit to Anthropic's buildout, backstopping about
a gigawatt with third-party developers and carrying on the order of $50 billion
of commitments. Ontiveros reads this as commercial rather than generous, since
that support is what lets Anthropic buy Google's own AI chips, its tensor
processing units, at around $20 billion a gigawatt.

The same logic explains who loses and what gets bought. CoreWeave scaled
contracted power from about 1.3 gigawatts to three and a half, then stalled after
the third quarter of 2025 when a bond selloff froze the high-yield market, while
rising turbine and interconnection deposits structurally disadvantage anyone
without a balance sheet. Ontiveros calls this existential for Nvidia and expects
it to start lending its own credit in the second half of 2026. What gets bought
follows a tier list ordered by how fast it energizes: premium turbines, then
aeroderivative and industrial units, then reciprocating engines, then fuel cells.
Bloom inverts the usual bridge logic, fast to deploy when permitting stalls but
two days from zero to full output, so it cannot double as backup and choosing it
means islanding more or less for good. Clean firm generation sits outside the
ranking, because nuclear and geothermal contracts are mostly non-binding and
milestone-contingent: options on long-term capacity rather than answers to speed
to power, a framing Kann proposes and Ontiveros endorses, then extends into a
call that gas turbine orders top out this year.

## What you need to know first

- **Behind the meter.** Generation on the customer's own site, serving the load
  directly rather than through the utility's connection. Here it is nearly always
  a bridge to a grid connection expected later, not a decision to leave the grid.
- **Capacity-adjusted.** Shorthand for counting how much of a resource's
  nameplate rating can be relied on when the system is stressed. Twenty-five
  gigawatts of nameplate solar and batteries is worth far less than that as firm
  capacity, which is why both speakers quote adjusted numbers.
- **Four nines.** 99.99% uptime, the availability data centers normally promise
  customers. Kann's suggestion, offered tentatively, is that Meta can relax it
  because its customers are its own products.
- **Backstop.** A creditworthy company guaranteeing someone else's obligations so
  a lease or construction loan can be financed at all.

## Details worth keeping

- Meta's Columbus, Ohio site is the vivid example of improvised speed. It uses a
  fast-to-build design nicknamed "the tent," and with no time to build a
  substation Meta bought land between two already-connected substations and ran a
  new medium-voltage line to it. That adds no generation, so Ontiveros expects
  curtailment on peak summer days until on-site generation arrives.
- xAI is credited with showing the way in 2024 with 20 to 30 megawatt industrial
  and aeroderivative turbines, after which OpenAI followed at Abilene with Crusoe
  and Oracle, and Meta in Columbus. The largest reciprocating-engine deployment
  cited, OpenAI and Oracle's 2.3 gigawatts in Shackelford County, uses flywheels
  spinning continuously to handle transients.
- Bloom Energy was worth roughly $90 billion at the time of recording, which Kann
  attributes largely to having fuel cells available when turbine order books did
  not.
- Hyperscalers were slow to see the squeeze, which is part of why self-build gave
  way to leasing. Meta and Microsoft now scale substantially through third-party
  operators, who often use behind-the-meter generation at gigawatt-scale sites.
- Google and Amazon are the two he says have mostly avoided behind-the-meter so
  far, being the most aggressive at placing deposits with utilities nationwide.
  Google is nonetheless in behind-the-meter renewables via Intersect Power.
- He expects the very large campuses to concentrate in West Texas, tens of
  thousands of acres mixing gas, solar, batteries and possibly wind, with on-site
  solar hedging power prices and batteries earning arbitrage. Lancium at Abilene
  and Crusoe's Armstrong County wind-connected site are named as active.
- One fix Kann raises for bridge power: hand the generation to the utility once
  the grid connection arrives, so it keeps serving the grid instead of idling.

## Claims worth citing

All figures as stated on 2026-07-09 and not independently verified. Deposits,
order books and contracted-capacity numbers move within months, and several
figures below are offered in conversation as orders of magnitude.

- Buildout in the tens of gigawatts a year, growing around 50% annually, reaching
  roughly 100 gigawatts a year by 2030 if the trend holds. (Ontiveros)
- Gas additions next year of five to six gigawatts; solar and batteries of 20 to
  25 gigawatts nameplate before capacity adjustment. (Ontiveros)
- For 2027-2028, Kann's off-the-cuff 10 to 15 gigawatts of gas plus about 20
  gigawatts of capacity-adjusted solar and storage, roughly 35 total. Ontiveros
  says his firm's adjusted figures are lower. (Kann, with Ontiveros dissenting)
- Anthropic at about 1.5 gigawatts end of 2025, targeting over 10 by 2027, which
  he equates to the size of Google today. (Ontiveros)
- A gigawatt of capacity costing roughly $50 billion, or $60-70 billion under
  some contract structures. Said loosely in passing. (Ontiveros)
- Roughly half the megawatts Amazon and Microsoft build go to OpenAI and
  Anthropic. (Ontiveros)
- Google backstopping about a gigawatt across TeraWulf, Hut 8 and Cipher Mining
  with Fluidstack, and carrying roughly $50 billion aimed at Anthropic's
  buildout, which he equates to four or five gigawatts and about $100 billion of
  TPU revenue at roughly $20 billion a gigawatt. The transcript garbles the
  balance-sheet term, so the instrument is unclear. (Ontiveros)
- CoreWeave at 3.5 gigawatts contracted, up from about 1.3 in Q4 2024, with
  little added since Q3 2025. (Ontiveros)
- Around 150 gigawatts of contracted large loads across US utilities at end of
  2025, mostly Google and Amazon. The listing sentence is garbled, so the base is
  unclear. (Ontiveros)
- OpenAI and Oracle deploying 2.3 gigawatts of four megawatt reciprocating
  engines in Shackelford County, Texas. (Ontiveros)
- Prediction: turbine orders peak in 2026, since utilities placed the bulk of
  them and the delivery window has narrowed to late 2027 and 2028, which are sold
  out. The transcript renders the verb ambiguously, though the surrounding
  argument makes "peak" the clear reading. (Ontiveros)

## Where it's contested

- **Which constraint actually binds.** The episode's real disagreement. Ontiveros
  treats generation scarcity as the driver of behind-the-meter building; Kann
  bets substantially more generation gets added and argues transmission and
  distribution is the larger problem. Neither concedes; Ontiveros lands on both.
- **The rankings are opinions.** That Google leads and Microsoft has slipped to
  fourth rests on deal structures and regulatory filings, not a metric. Kann
  flags his own point about Google's energy headcount as speculative and
  anecdotal.
- **The forecasts are forecasts.** The turbine order peak, the Nvidia response
  and the shape of 2030 demand are presented as the firm's current theses, one of
  them explicitly as a bold call against consensus.
- **Growth assumptions are conditional.** The West Texas megacampuses and Bloom
  becoming enormous are attached to the trend continuing, and he says plainly he
  is not religious about a terawatt-a-year scenario.
- **Non-binding means non-binding.** Nuclear and geothermal announcements that
  read as commitments are described as contingent on approvals and milestones.
  That qualifier is load-bearing and easy to drop.
