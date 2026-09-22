---
episode: "AI is disrupting services. What does that mean for power demand?"
published: "2026-08-18"
guest: "Jake Saper, partner, Emergence Capital; enterprise software and AI infrastructure investor who began his career developing solar in India. The transcript renders his surname as both \"Saper\" and \"Saber\"; this note uses the dominant rendering."
threads: [ai-compute, ai-applications, load-growth, electricity-prices, venture-and-finance]
source_transcript: "transcript.md"
note_version: 1
---

## The question

If AI starts to change how services such as law, accounting and insurance are
actually delivered, what does that imply for how much compute, and how much
power, the economy will end up needing?

## The answer

Saper answers the direction and explicitly refuses the magnitude. Enterprise
deployment has barely started, 80% of the American economy is services, and
today's compute is tiny relative to the eventual need, so demand for tokens
will be exponentially higher than it is now. What he will not do is convert that
into an infrastructure figure, because how efficient the models become is the
open variable and he says anyone with a strong opinion on it is guessing. The
constraint he spends most of the episode on is not power at all: it is whether a
services business can actually be delivered by AI rather than by quietly hiring
people.

## The argument

The ground he argues from is a bet his firm made about three years ago, around
2023 and shortly after GPT-3.5, that open-source models would become a dominant
way AI gets delivered, because enterprises would want something cheaper, more
private and more customizable than a frontier model call. What followed was
Together AI, which sells inference and training for open-source models and is
therefore a heavy consumer of compute and data centers. He names Baseten as
another player in the space he likes, without saying he has invested. What
interests him is what the Together investment turned into. It began as software,
optimizing training and inference, became infrastructure, and then
infrastructure in the physical sense. He treats that blurring as general rather
than a quirk of one company, and it is also why he thinks his read on deployment
is grounded: he can see what traffic actually runs through both businesses.

What he sees is that almost nothing has happened yet. He borrows Demis
Hassabis's phrase about the foothills of the singularity, declines the larger
claim by saying he is not smart enough to judge whether the singularity is near,
and keeps the narrower one: we are in the foothills of enterprise deployment,
particularly for larger and less technology-forward companies. He splits the
capital three ways. The vast majority of AI dollars went into developing models;
a shift toward the infrastructure to run them has come over the past 12 to 18
months; and the third bucket, deploying the technology across the country, is
paltry relative to where it needs to go. The error he attributes to his own
industry is treating capability as deployment, imagining a single binary
threshold after which everything changes at the speed of light. The real world
does not work that way, and it will take a lot longer to deploy: 80% of the
American economy is services-driven, so until a way is found to get AI into
services businesses, he says, this is going to take a while. That is what makes
today's compute, in his phrase, infinitesimally
low relative to the ultimate need, and why this year's hyperscaler capital
spending could look small in a few years. Demand for tokens is the part he is
confident about; how much physical infrastructure is needed to deliver them as
models get more efficient is the part nobody can answer.

The bulk of the conversation is the thesis underneath that deployment claim. An
AI-native service, a term he says he made up and concedes is not well
understood, is any service deliverable with AI faster, better and/or cheaper
than the incumbent, with, for many of them, a highly paid and highly valued
human on top to check the work and put their name to it. The obvious way to
build one is to buy existing firms for their distribution and add AI, which he
says ignores how hard behavior change is: roll-ups are difficult anyway, and
this one requires convincing the people
you did not fire to work differently inside a new conglomerate. Building from
scratch is easier, though still exceedingly difficult, because you can build the
general ledger for one use case, build agents against it, run it yourself with a
few customers, then hire senior practitioners to sit on top and train it. His
example is Hanover Park, a fund administrator for private equity that built its
ledger and its agents from scratch and now serves clients faster and at higher
quality than the legacy providers. The reversal is the part that matters. For
the best versions of an AI-native service, he says, you generally are not demand
constrained, because a faster, better or cheaper version of an existing service
sells itself; the question is only whether you can deliver it primarily with AI.
The failure mode he names is mirage product market fit: you sell plenty,
customers are satisfied, and you got there by hiring people, which makes you an
ordinary services
business that took the wrong form of capital. The best operators, Hanover Park
included, periodically stop selling to let the platform catch up to 80 or 90% of
the work. He is blunt that this is harder than software, because you have to
build Stripe and McKinsey at once and make them fit together.

On energy his worry is political rather than physical, and this is where his
position and the host's sit side by side unreconciled. AI has become genuinely
unpopular for reasons all over the map; electricity pricing is one, and that one
he calls imminently addressable: make the grid more flexible, make it cheaper to
build, and in most cases data centers should lower energy prices rather than
raise them. He adds that the industry has explained AI's benefits poorly, beyond
a vague promise to cure cancer someday. Johnson then puts the structural case,
that demand from air conditioning, vehicles and data centers outruns supply so
prices rise regardless, with AI the obvious villain. Saper's reply is a hedged
concession, that this is probably true and the pinch point would probably have
arrived anyway; he does not withdraw his own claim, and neither man puts the two
together. He then offers a future he himself labels Pollyanna and too rosy, in
which the buildout deliberately supports the communities hosting it, noting that
a calm, non-screamy policy position is a centrist one and centrism is out of
fashion. Robotics runs the same way: he is a bull, having invested in Bedrock
Robotics, whose self-driving construction equipment does a lot of data center
work and, when that works at scale, should let data centers be built faster and
more cheaply, which he hopes ultimately translates into cheaper power. On labor
he insists on being granular rather than ham-fisted, since excavator operators
are already in shortage and the immigration crackdown
deepened it, so many robots deploy before any current worker is displaced. His
overall position is that the best outcome is a medium pace of deployment, too
slow and the country is outrun by China and others, too fast and the
unemployment shock arrives before anyone can retrain. The current pace feels
medium if not slow, and what he fears is that not enough people are planning for
the tails.

## What you need to know first

- **Tokens, and why token demand is not infrastructure demand.** Tokens are the
units of text a model reads and writes, and how the work of running a model is
counted and paid for. His central distinction is between the tokens the economy
will want, which he expects to grow exponentially, and the physical capacity
needed to produce them, which depends on model efficiency and which he treats as
unknowable today.
- **Open-source models, post-training and model routing.** An open-source model
is one an enterprise can run and adapt itself; post-training is adapting it on
its own data; routing is deciding, task by task, whether to call an expensive
frontier model, a fine-tuned open one, or a cheap off-the-shelf one. He treats
this as an "and" rather than an "or," and making the routing decision so the
client does not have to is part of what an AI-native services firm sells.

## Details worth keeping

- Emergence was founded in 2003 on being early experts in emerging business
models: Salesforce first, then vertical cloud software, with Veeva in
pharmaceuticals its biggest hit. Saper joined and built a thesis around cloud
software for natural resources, covering agriculture, energy and water.
- The origin anecdote: as a solar developer in the Thar Desert in Rajasthan he
hired a hot air balloonist to drag a balloon into the desert for the aerial
imagery he needed to scout land and prove completion to banks. He later backed
DroneDeploy, a drone software company rather than a manufacturer, and says
energy and solar became one of its largest categories a decade on.
- The Hanover Park illustration: distributing a public stock through a legacy
fund administrator runs through a partner discussion, an email to the fund
admin, a stack of Excel files to work out which of the fund's investors owns
what, and a queue of emails, and can take days or weeks.
- On legal, the promise he sees for contract-focused AI-native firms is
capturing a benefit that currently stops at the law firm. His illustration is
Harvey selling to Kirkland & Ellis, where the client never sees the benefit in
fees or speed; an AI-native firm takes the AI problem on itself and may shift
pricing from per hour to per contract.
- He has done a lot in insurance and expects to continue: high value, high
labor, high data, recurring transactions. He also biases toward categories
needing a human in the loop indefinitely, because a service that needs no human
judgment or accountability is one the frontier labs may eventually just do
themselves. Customs brokerage interests him for that reason, though he has not
invested:
paper-heavy, constantly shifting with the tariffs, gated behind a demanding
license.
- He gives three reasons for a rotation back toward controlling the model: a
hangover from what he calls the token-maxing spring, which lasted about six
weeks; open-source models getting better; and enterprises, specifically
tech-forward ones, getting smarter about which of their data is valuable and how
to build evaluation sets to post-train with, which nobody knew at the start of
the generative AI rush.
- His evidence that deployment lags the discourse is anecdotal and deliberately
so: outside the technology bubble almost nobody knows what Anthropic is, and
when he says he takes a robot to work every day, outside a major American city
people do not believe him.

## Claims worth citing

All figures as stated in an episode published 2026-08-18. Several are the
guest's own portfolio figures, given by their investor. Capital and deployment
numbers in this area move quickly.

- 80% of the American economy is services-driven, stated flatly, and it is the
basis for his claim that AI deployment will take a long time. (Saper)
- Demand for tokens will be very high and exponentially higher than today. What
is not clear is how much infrastructure is needed to deliver them as models get
more efficient, and anyone claiming a strong opinion is guessing. (Saper)
- The vast majority of AI dollars went into developing models; the shift toward
infrastructure to run them came over the past 12 to 18 months; the third bucket,
deployment across the country, is paltry. Today's compute is infinitesimally low
relative to the ultimate need. (Saper)
- Hyperscaler capital spending this year is put at "$750 billion or whatever" by
the host. Saper does not confirm it and says it is very possible it will look
small in a few years. (Johnson, direction endorsed by Saper)
- Together AI: Emergence did the Series A at a couple million in revenue; it is
over a billion three years later. Portfolio figure. (Saper)
- The services AI-native firms displace are often 10, 20 or 30% gross margin
businesses, so gross margin still has to be watched and this is not a free
lunch. Offered against Johnson's premise that these businesses typically operate
at high gross margin. (Saper)
- The best AI-native services firms aim for the platform to do 80 to 90% of the
work, and some, Hanover Park included, stop selling periodically so delivery can
catch up. (Saper)
- Electricity pricing is imminently addressable, and if the grid is made more
flexible and cheaper to build, that should in most cases have data centers lower
energy prices rather than raise them. The condition and both hedges are his.
(Saper)
- The current pace of deployment feels medium, if not slow, and a medium pace is
the best available scenario: too slow risks being outpaced by China and others,
too fast risks a rapid unemployment shock. (Saper)
- Excavator operators are in large and worsening shortage, which he attributes
in part to the immigration crackdown, so many robots deploy before current
workers are affected. (Saper)
- Bridgewater published a paper in the week of the conversation showing
post-training an open-source model produced dramatically better results at much
lower cost. Described by the host; Saper does not restate or verify it.
(Johnson)

## Where it's contested

Johnson does not challenge Saper, and states on air that Saper is one of his
closest friends. Where their views differ, the difference is left standing
rather than resolved. What follows is mostly what went untested.

- **The title's question is answered with a refusal.** Reading the episode as a
power demand forecast would invert what its guest says.
- **Two divergences, both unreconciled.** The argument records the first, over
whether data centers push power prices down or up. The second is cleaner.
Johnson says AI-native services typically operate in high gross margin
transactions, so the problem is improving the deal process rather than
minimizing token cost. Saper declines that outright: the services being
displaced are often 10, 20 or 30% gross margin businesses, so margin still has
to be watched and this is not a free lunch.
- **He is invested in most of his evidence.** Together AI, Hanover Park and
Bedrock Robotics are all positions, and the category he argues for is one he
named. He says all of this openly and concedes the term is not well understood.
Johnson also says Saper is on the board of Ironclad; Saper neither confirms it
nor mentions it.
- **Two explicit disclaimers.** He says he is not smart enough to comment on
whether the singularity is near, and labels his own optimistic scenario for the
buildout a Pollyanna and too rosy version of the future.
- **The host supplies a premise from his own business.** Johnson says that in
the transactions Crux operates in, law firms are increasingly adopting AI tools
without it flowing through into client value or lower costs. That is his
observation about his own deal flow. Saper takes it up as the promise for
AI-native law firms rather than confirming it independently.
- **No commercial numbers for the thesis.** Nothing in the episode gives
revenue, customer counts or margins for any AI-native services company. Hanover
Park's advantage is described qualitatively, and the 80-to-90% delivery figure
is a target.
- **An unexplained reference.** Johnson raises "Mythos" as an early example of
what could become a massive global cyber threat, and Saper picks it up as a
"Mythos-like product." Neither says what it is, and the episode gives no basis
for describing it further.
- **Transcript quality.** The guest's surname appears as "Jake Saper" throughout
and as "Jake Saber" in Johnson's sign-off, and the guest's closing line thanks
the host as "Fredo" where the host is Alfred Johnson. The transcription is
machine-generated and names in it are unreliable.
