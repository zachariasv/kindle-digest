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

Exactly ONE original piece a day, read in full on the Kindle. It must be the most impactful long read published in roughly the last 48 hours, the piece people will be referencing this week. Think: a Reuters or ProPublica investigation that just broke; OpenAI or DeepMind walking through the maths behind a new result; a security firm's full technical breakdown of a major attack.

**Impact test.** It must pass all of these:
- **Primary and original:** the investigation itself, the lab's own write-up, the researchers' own incident analysis. Not a summary or reaction piece.
- **Consequential:** it changes how informed people understand something important, or it will drive news and discussion for days.
- **Deep:** 10+ minutes of substance: evidence, mechanism, data, figures.
- **Fresh:** published in the last ~48 hours. On a quiet day, take the strongest piece from the past 7 days that hasn't been a must-read yet. Never fall back to a merely decent article.

**Where to look first** (scan these every run):
- *Investigations:* Reuters Investigates, ProPublica, ICIJ, Bellingcat, AP and NYT/WaPo investigations, The Markup, Bloomberg Big Take, SVT Uppdrag granskning / DN granskning (only if free to read).
- *AI labs and research:* OpenAI, Anthropic, Google DeepMind, Meta AI, Microsoft Research, Mistral, DeepSeek / Qwen / Moonshot technical reports, plus major papers getting attention (arXiv HTML versions).
- *Security research:* Google Project Zero and Threat Intelligence, Mandiant, Microsoft Threat Intelligence, Wiz, Trail of Bits, Palo Alto Unit 42, Check Point, JFrog, Kaspersky GReAT, Citizen Lab.
- *Science and maths:* Quanta, Nature news features, Terence Tao's blog and similar first-hand accounts.
- *Signal of impact:* Hacker News front page, and what other outlets are citing and following up on.

**Weighting:** technical AI and ML, mathematics and science, security, geopolitics and strategy, tech and VC. Swedish topics only for a genuinely major investigation.

**Format:** a single regular article page. Paywalls usually block extraction (FT, WSJ, Bloomberg, DN+, Breakit), so prefer the free original. Reuters is often readable; if it fails, a backup takes over. Never live pages, video pages or galleries.

In the edition JSON: `must_reads` holds exactly 1 item `{title, source, url, why}`, where `why` is one sentence on why it matters. `must_read_backups` holds 2 more that also pass the impact test, best first. A job in the private repo extracts the full text and figures and falls back to the backups if needed.

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
