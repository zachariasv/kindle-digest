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

Sections, in this order:

1. **Everyone's talking about**: 3-5 one-to-two-sentence items.
2. **Geopolitics**: 2-3 items max. Include "Week ahead" when there are notable scheduled events (diplomatic tours, summits); the reader values these.
3. **US and Europe**: big developments only, 1-3 items.
4. **Sweden**: politics first, then a short "In brief" with 3-4 other notable domestic stories.
5. **Tech and AI**: 2-3 items. Model releases and big strategic moves.
6. **Breakthrough of the day**: the most important section. ONE technical item explained properly: the mechanism, why it beats prior work, key numbers. Write for a reader with a strong maths background.
   **Also on the radar**: 3-4 further papers or results, each 2-3 sentences on the actual method and result.
7. **Stockholm VC**: Breakit / Di Digital, as bullets, one per item: company (founder) — what they do — amount — investors. Skip the section when nothing matters.
8. **Week in review** (Sundays only): 3 short threads that connect the week's stories.

Must-reads: exactly 3 original articles per day, the best pieces to read in full. KOReader extracts the article body with the CSS selectors `.wysiwyg, .c-article-content, article, main` (first match wins), so pick pages where one of these wraps the article text and little else:
- Good: Al Jazeera news articles (`.wysiwyg`), Euronews regular articles (`.c-article-content`), SVT and SR articles (`article`), Anthropic / OpenAI / DeepMind research posts (`article`), Quanta.
- Never: live blogs or live pages, video pages, galleries, paywalled sites (FT, WSJ, DN+, Breakit), or pages that need JavaScript to show the text.
- Before choosing, fetch the page and confirm it's a single regular article.

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
