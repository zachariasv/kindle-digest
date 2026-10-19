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
- **Duplicates.** If a story is in "Everyone's talking about", only give it a fuller item elsewhere when that item adds material context. Otherwise the one-liner is enough.

Things the reader explicitly wants never to miss: Swedish government formation and major Swedish political steps, US elections, AI model releases (especially open-weight and Chinese labs), and technical breakthroughs.

## Daily edition (written by 06:45 Stockholm time)

Write `editions/YYYY-MM-DD.json` (same schema as earlier editions), then run `python build.py`. Any item can use `"bullets": [...]` in addition to or instead of `"body"`.

Sections, in this order (the technical sections come last on purpose, so the edition ends on them):

1. **Today's must-read**: rendered automatically at the top from `must_reads` (see below). Don't write it as a section.
2. **Everyone's talking about**: 3-5 one-to-two-sentence items.
3. **Geopolitics**: 2-3 items max. Include "Week ahead" when there are notable scheduled events (diplomatic tours, summits); the reader values these.
4. **US and Europe**: big developments only, 1-3 items.
5. **Sweden**: politics first, then a short "In brief" with 3-4 other notable domestic stories.
6. **Stockholm VC**: Breakit / Di Digital, as bullets, one per item: company (founder) — what they do — amount — investors. Skip the section when nothing matters.
7. **Week in review** (Sundays only): 3 short threads that connect the week's stories.
8. **Tech and AI**: 2-3 items. Model releases and big strategic moves.
9. **Breakthrough of the day**: the most important section. ONE technical item explained properly: the mechanism, why it beats prior work, key numbers. Write for a reader with a strong maths background.
   **Also on the radar**: 3-4 further papers or results, each 2-3 sentences on the actual method and result.

## Today's must-read

Exactly ONE original piece a day, read in full on the Kindle. The reader's two goals for it: understand something important in depth, and close blind spots so he becomes genuinely well read. Ideal length is **15-30 minutes**.

**What he picks (from his own calibration answers):**
- **First-hand research and technical write-ups**, above all from frontier AI labs and AI startups: how a result was found, how a model was trained, what the proofs or circuits look like. This is the single strongest preference.
- **The economics of AI**: compute and energy supply and demand, funding and circular deals, whether the spending is sustainable, the actual numbers. Must be analysis with data, not a short opinion column.
- **Mathematics and science features** (Quanta-style), across fields, including ones outside his own interests. He's curious and wants broad scientific literacy.
- **Blind-spot explainers**: how something important actually works (e.g. how the EU budget is negotiated), at 15-20 minutes.
- **Foundational classics**: the most influential essays and papers of the past decade, even if old, when they're relevant to current events. Fresh pieces still come first.
- **Big investigations** (Reuters, WSJ, FT, ProPublica class) only when the impact is large: they change how a major situation is understood, or they're close to home (Sweden, Europe, AI). Prefer the free original, since paywalls block extraction.

**What he skips:**
- News reports of any length under ~10 minutes (they belong in the digest).
- Profiles and personality pieces.
- Work-adjacent VC content (thesis essays, portfolio data). He reads that at work, not in his free time.
- Macroeconomics without a direct AI or tech angle (central bank notes, inflation pass-through).
- Big-tech antitrust and fines; benchmark-gaming exposés. These are unsurprising to him.
- Technical write-ups about infrastructure he doesn't care about (generic cloud outages). A security or postmortem piece qualifies only when it's about AI itself (e.g. a lab's postmortem of an attack on an AI platform).
- Small-scale stories, however well reported: municipal corruption, single-sector OSINT findings, local conflicts.

**Surprise decides close calls.** What matters is how unexpected and consequential a story is, not geography. Abuse of power in an established democracy (spyware on journalists in Sweden, the UK or Germany) is far more significant than the same thing in an authoritarian state, where it's expected. Being close to home (Sweden, Europe, AI) adds a little on top. Prefer the piece that will still matter in a month.

**Length rule.** Most days 15-30 minutes. At most one long read (40-60 minutes) a week, and only for something truly groundbreaking.

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
1. Add every new piece found today that clearly passes the rules above as a candidate: `{url, title, source, why, category, kind, published, added, impact, minutes}`. Usually 2-6 a day. Don't re-add a URL that's already in the registry or its history.
   - `category` is exactly one of: `ai-research` (lab and startup technical write-ups, papers, AI security postmortems), `ai-economics`, `science` (maths and science features), `investigation` (big investigations and geopolitical deep dives), `blind-spot` (explainers and foundational classics).
   - `kind` is `fresh` (news-driven, loses value as it ages) or `evergreen` (explainers, classics, timeless features).
   - `impact` from 1 to 10. **10:** will be referenced for months, genuinely groundbreaking. **8:** the most important piece of the week in its field. **6:** strong and worthwhile but not essential. Don't add anything below 6. Be strict, and score against the reader's preferences above, not general newsworthiness.
   - `minutes`: estimated reading time; `published`: the piece's own date; `added`: today.
2. Run `python pick.py YYYY-MM-DD`. It drops already-picked and expired candidates, scores the rest (impact, plus up to +1.5 for a category that hasn't been picked recently, minus a small daily penalty for ageing fresh pieces), allows at most one 40+ minute read per week, and writes the winner into `must_reads` and the next two into `must_read_backups` in today's edition.
3. Don't edit `must_reads` by hand afterwards. To change the outcome, fix the candidates' scores or categories and rerun `pick.py`.

A job in the private repo extracts the winner's full text and figures and falls back to the backups if extraction fails.

## Length

About a 7-8 minute read on weekdays, slightly more on Sundays. When in doubt, cut. The breakthrough section is the one place to spend words.

## Style

- Clear, crisp and neutral, like a good briefing note. No casual or "cool" phrasing ("coin flip", "should own", "priced in").
- Every item must be understandable on its own. Explain any market or finance term in plain words, or leave the item out. If a number needs context to mean anything, give the context.
- Lead with the fact, then why it matters, in that order.
- Write everything in your own words. Never copy sentences from sources, never paste article text.
- Every item lists its source(s) and date.
- Verify facts against at least one reputable source. Flag claims that are only reported.
- Don't repeat yesterday's story unless something changed. If it did, say what's new.
