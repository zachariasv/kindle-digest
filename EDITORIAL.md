# Editorial brief

The reader is a Stockholm-based VC analyst and applied-maths master's student. Goal: be well read, never caught off guard by a current event, and have real technical depth on AI.

## Selection: what earns a place

Include an item only if at least one holds:

- **It's what people are talking about.** A dominant story goes in even if it's not personally interesting (e.g. mass protests in a major European country). The point is no blind spots, not entertainment.
- **It changes the picture.** A real shift in global affairs, Swedish politics, or tech: a first, an escalation, a decision, a reversal.

Cut:

- **Status updates on long-running situations** with nothing new (e.g. "Ukraine still short of Patriots", "API key theft continues"). Cover a long-running story again only when there's a step change.
- **Regional follow-ups** after the headline event has been reported. Report the big strike; don't keep tracking the local conflict that follows unless it widens.
- **Routine corporate items** (a single data-centre lease, minor partnerships) unless they're unusually large or strategic.
- **Duplicates.** Every story appears exactly once in the whole edition. Before writing, list the day's stories and assign each to one section. A story in "Everyone's talking about" never reappears in a later section, not even as a mention.

Things the reader explicitly wants never to miss: Swedish government formation and major Swedish political steps, US elections, AI model releases (especially open-weight and Chinese labs), and technical breakthroughs.

## Daily edition (written by 06:45 Stockholm time)

Write `editions/YYYY-MM-DD.json` (same schema as earlier editions), then run `python build.py`. Any item can use `"bullets": [...]` in addition to or instead of `"body"`.

**The default item is short:** a bold headline and 1-2 sentences, like the "Everyone's talking about" items. That is the right length for almost all news. In the whole edition, at most **two** items may run longer (a short paragraph, max ~80 words), and only when the extra context genuinely matters (e.g. a real step in Swedish government formation).

Sections, in this order (tech comes last on purpose):

1. **Today's must-read**: rendered automatically at the top from `must_reads`. Don't write it as a section.
2. **Everyone's talking about**: the 4-6 biggest stories of the day, 1-2 sentences each. These are told here and nowhere else.
3. **World**: other notable geopolitics and US/European stories, 2-4 short items.
4. **Sweden**: politics first, then other notable domestic stories, 2-4 short items.
5. **Stockholm VC**: Breakit / Di Digital, as bullets, one per item: company (founder) — what they do — amount — investors. Skip when nothing matters.
6. **Week ahead**: only when there are notable scheduled events (summits, votes, diplomatic tours), as 2-4 bullets.
7. **Week in review** (Sundays only): 3 threads connecting the week's stories, 2-3 sentences each.
8. **Tech and AI**: 3-5 short items: model releases, big strategic moves, and notable papers or results, each in 1-2 sentences on what's new. No long technical deep dives in the digest. A result that deserves a proper explanation goes into the must-read registry as an `ai-research` candidate instead (ideally the lab's or authors' own write-up), so it can become a must-read.

Skip any section with nothing that clears the bar rather than padding it.

## Today's must-read

Exactly ONE original piece a day, read in full on the Kindle. The reader's two goals for it: understand something important in depth, and close blind spots so he becomes genuinely well read. Ideal length is **15-30 minutes**.

**What he picks (from two rounds of calibration):**
- **First-hand research and technical write-ups**, above all from frontier AI labs and AI startups: how a result was found, how a model was trained, what the proofs or circuits look like. The strongest preference. First-hand beats second-hand: a lab's own explanation beats a tech outlet's explainer of the same result.
- **AI changing what's possible in other fields**: AI-designed enzymes, AI-found proofs, AI doing security research or hacking. The interest is in AI as the actor, not attacks on AI labs.
- **The concrete economics of AI**: what a gigawatt data centre really costs line by line, where compute money comes from, how long things take to build. Mechanics and real numbers that make abstract headlines tangible. Investor opinion essays are too dry.
- **The nuance under the talking points**: topics people discuss in slogans ("Europe must reduce dependence on China") explained at the level of real mechanisms, e.g. how rare-earth export controls actually work. Strategy explainers tied to current events are high value.
- **Intersections**: pieces where AI, money, geopolitics and Europe meet (e.g. a state fund quietly buying into European AI startups) are especially captivating.
- **Science features** across fields, ideally with a clear real-world hook. Accessible maths is welcome (famous problems, results with a concrete picture); deep abstract pure maths (knot theory, say) is not.
- **Industry mechanics explainers**: how a whole market works under the hood (e.g. reinsurance). How *policy* systems work (pensions, budgets) only when they matter internationally.
- **History that explains the present**: well-chosen historical parallels to a current crisis. The concept is strong; the parallel itself must be convincing.
- **Big investigations** only when the impact is large and the subject touches his core interests. Far-away conflicts, however well reported, are only for very slow weeks.

**Captivation is the tiebreaker.** Ask: would this make him sit up straight? Interesting-but-flat pieces (good chip-fab features, dry investor notes) lose to pieces with surprise, a clear "aha", a famous author or a sharp intersection. For **advice and personal-perspective pieces** (career or life advice, talks, personal essays on how to work or think), who is speaking matters a lot to him. For those, and only those, fill the `who` field with 1-2 sentences on why this person's advice carries weight (e.g. a Turing Award winner who also invented error-correcting codes). For investigations, research, explainers and everything else, leave `who` empty.

**What he skips:**
- News reports of any length under ~10 minutes (they belong in the digest).
- Profiles and personality pieces.
- Work-adjacent VC content (thesis essays, portfolio data). Pieces where VC is part of a bigger AI or geopolitics story are fine.
- Macroeconomics and domestic policy without a direct AI, tech or geopolitical angle (central bank notes, pension systems).
- Big-tech antitrust and fines; benchmark-gaming exposés. Unsurprising to him.
- Security postmortems of ordinary breaches, including breaches at AI labs, and generic infrastructure postmortems.
- Small-scale stories, however well reported: municipal corruption, single-sector OSINT findings, local conflicts.

**Surprise decides close calls.** What matters is how unexpected and consequential a story is. Abuse of power in an established democracy (spyware on journalists in Sweden, the UK or Germany) is far more significant than the same thing in an authoritarian state, where it's expected. Being close to home adds a little on top. Prefer the piece that will still matter in a month.

**Variety within a week.** He wants a spread: AI research and AI economics are equally valued, and he'd rather get both in a week than one of them twice. `pick.py` handles this, but score impact honestly so the balancing can work.

**Length rule.** Most days 15-30 minutes. At most one long read (40+ minutes) every two weeks, only for something truly groundbreaking, and very rarely over 45 minutes.

**Freshness.** Prefer pieces from the last ~48 hours. On a quiet day, take the strongest unused piece from the past week, or a blind-spot explainer or foundational classic. Never a merely decent article.

**Where to look first** (scan these every run):
- *AI labs and research:* OpenAI, Anthropic, Google DeepMind, Meta AI, Microsoft Research, Mistral, DeepSeek / Qwen / Moonshot technical reports, AI startup engineering blogs, plus major papers getting attention (arXiv HTML versions).
- *Science and maths:* Quanta, Nature and Science news features, Terence Tao's blog and similar first-hand accounts.
- *AI economics:* SemiAnalysis-style analyses, Epoch AI, IEA and energy-sector analyses of data-centre demand, serious long-form on AI funding.
- *Investigations:* Reuters Investigates, ProPublica, ICIJ, Bellingcat, AP, NYT/WaPo/WSJ/FT investigations (only if free to read), SVT Uppdrag granskning.
- *Security, AI-related only:* lab and platform postmortems, Project Zero, Mandiant, Wiz, Trail of Bits, JFrog on attacks on AI models and platforms.
- *Signal of impact:* Hacker News front page, and what other outlets are citing and following up on.

**Format:** a single regular article page. Never live pages, video pages or galleries.

## How the must-read is chosen: candidate registry

Good pieces don't arrive evenly across topics, so there is no fixed weekly schedule. Instead, candidates queue up in `mustread/registry.json` and a fixed scoring rule (`pick.py`) balances impact against variety.

Each run:
1. Add every new piece found today that clearly passes the rules above as a candidate: `{url, title, source, why, who, category, kind, published, added, impact, minutes}`. Usually 2-6 a day. Don't re-add a URL that's already in the registry or its history.
   - `category` is exactly one of: `ai-research` (lab and startup technical write-ups, papers, AI doing security research), `ai-economics`, `science` (maths and science features), `investigation` (big investigations and geopolitical deep dives), `blind-spot` (explainers and foundational classics).
   - `kind` is `fresh` (news-driven, loses value as it ages) or `evergreen` (explainers, classics, timeless features).
   - `impact` from 1 to 10. **10:** will be referenced for months, genuinely groundbreaking. **8:** the most important piece of the week in its field. **6:** strong and worthwhile but not essential. Don't add anything below 6. Be strict, and score against the reader's preferences above, not general newsworthiness.
   - `minutes`: estimated reading time; `published`: the piece's own date; `added`: today.
2. Run `python pick.py YYYY-MM-DD`. It drops already-picked and expired candidates, scores the rest (impact, plus up to +2 for a category that hasn't been picked in the last week, minus a small daily penalty once fresh pieces pass a grace period), allows at most one 40+ minute read every two weeks, and writes the winner into `must_reads` and the next two into `must_read_backups` in today's edition.
3. Don't edit `must_reads` by hand afterwards. To change the outcome, fix the candidates' scores or categories and rerun `pick.py`.

A job in the private repo extracts the winner's full text and figures and falls back to the backups if extraction fails.

### Classics

`mustread/classics.json` is a reading list of landmark papers from roughly the last decade, mostly AI and ML plus general science and maths, in priority order. `pick.py` sprinkles them in automatically: about two a month, never more than one a week, on slow days (best fresh candidate's impact below 7.5) once a week has passed, or on any day once two weeks have passed, unless a fresh piece scores 9+. They alternate roughly two AI papers to one science paper. Papers marked `"status": "read"` are skipped. You can append further landmark papers to the end of the list (ar5iv or arXiv HTML URLs read best), but don't reorder or remove entries.

## Length

The digest is a quick scan: about **4-5 minutes, roughly 900-1,100 words** on weekdays, up to ~1,300 on Sundays. Depth belongs in the must-read, not the digest. Before publishing, count the words and cut until it fits, removing whole items before trimming sentences.

## Style

- Clear, crisp and neutral, like a good briefing note. No casual or "cool" phrasing ("coin flip", "should own", "priced in").
- Every item must be understandable on its own. Explain any market or finance term in plain words, or leave the item out. If a number needs context to mean anything, give the context.
- Lead with the fact, then why it matters, in that order.
- Write everything in your own words. Never copy sentences from sources, never paste article text.
- Every item lists its source(s) and date.
- Verify facts against at least one reputable source. Flag claims that are only reported.
- Don't repeat yesterday's story unless something changed. If it did, say what's new.
