"""Pick today's must-read from the candidate registry and write it into the edition.

Usage: python pick.py YYYY-MM-DD

The registry (mustread/registry.json) holds candidates the daily job has found:
  {"candidates": [{url, title, source, why, category, kind, published, added, impact, minutes}],
   "history":    [{date, url, title, category, minutes}]}

Score = impact + variety bonus - age penalty, where
  - variety bonus grows with days since the category was last picked (max +2 at 7+ days)
  - fresh pieces lose 0.3 points per day once past a grace period (2 days for investigations,
    5 for research, economics and science, which don't go stale as fast); evergreen pieces don't age
Must-reads go out only on Tuesday, Thursday and Sunday; on other days the edition gets an
empty must_reads slot and candidates simply keep queueing.
Rules: never repeat a pick; at most one long read (40+ min) per 14 days;
fresh candidates expire after 7 days, evergreen after 30.
The top pick goes into must_reads, the next two into must_read_backups.

Classics (mustread/classics.json): landmark papers sprinkled in about twice a month, never
more than once a week. One is due on a slow day (best fresh impact below SLOW_DAY_SCORE) once
7 days have passed since the last, or on any day once 14 have passed, unless a fresh piece
scores 9+. Roughly two AI papers for every science or maths paper. Classics skip the
long-read limit.
"""
import json
import pathlib
import sys
from urllib.parse import urlparse
from datetime import date

ROOT = pathlib.Path(__file__).parent
REGISTRY = ROOT / "mustread" / "registry.json"
CATEGORIES = ["ai-research", "ai-economics", "science", "investigation", "blind-spot"]
MAX_VARIETY_BONUS = 2.0
VARIETY_FULL_AFTER_DAYS = 7
AGE_PENALTY_PER_DAY = 0.3
FRESH_GRACE_DAYS = {"investigation": 2}  # all other categories: 5
DEFAULT_GRACE_DAYS = 5
EXPIRY_DAYS = {"fresh": 7, "evergreen": 30}
LONG_READ_MINUTES = 40
LONG_READ_GAP_DAYS = 14
CLASSICS = ROOT / "mustread" / "classics.json"
CLASSIC_MIN_GAP_DAYS = 7
CLASSIC_DUE_DAYS = 14
SLOW_DAY_SCORE = 7.5
BIG_FRESH_SCORE = 9
# Must-reads go out only on these weekdays (Monday = 0): Tuesday, Thursday, Sunday.
MUST_READ_WEEKDAYS = {1, 3, 6}


def d(s):
    return date.fromisoformat(s)


def days_since_category(history, category, today):
    dates = [d(h["date"]) for h in history if h["category"] == category]
    return (today - max(dates)).days if dates else VARIETY_FULL_AFTER_DAYS


def score(c, history, today):
    gap = days_since_category(history, c["category"], today)
    bonus = MAX_VARIETY_BONUS * min(gap, VARIETY_FULL_AFTER_DAYS) / VARIETY_FULL_AFTER_DAYS
    age = (today - d(c["published"])).days
    penalty = 0 if c.get("kind") == "evergreen" else AGE_PENALTY_PER_DAY * max(0, age - FRESH_GRACE_DAYS.get(c["category"], DEFAULT_GRACE_DAYS))
    return round(c["impact"] + bonus - penalty, 2), round(bonus, 2), round(penalty, 2)


def main(day):
    today = d(day)
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    history = [h for h in reg["history"] if h["date"] != day]  # re-running a day replaces its pick
    picked = {h["url"] for h in history}

    def alive(c):
        added = d(c.get("added", c["published"]))
        limit = EXPIRY_DAYS.get(c.get("kind", "fresh"), 7)
        return c["url"] not in picked and (today - added).days <= limit

    reg["candidates"] = [c for c in reg["candidates"] if alive(c)]
    if today.weekday() not in MUST_READ_WEEKDAYS:
        # No must-read today: keep collecting candidates, write an empty slot, record no pick.
        reg["history"] = history
        REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        ed_path = ROOT / "editions" / f"{day}.json"
        ed = json.loads(ed_path.read_text(encoding="utf-8"))
        ed["must_reads"], ed["must_read_backups"] = [], []
        ed_path.write_text(json.dumps(ed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"No must-read on {today.strftime('%A')}s (only Tuesday, Thursday and Sunday)")
        return 0
    recent_long = any(h.get("minutes", 0) >= LONG_READ_MINUTES and (today - d(h["date"])).days < LONG_READ_GAP_DAYS
                      for h in history)
    # Sites that refuse the private extraction job (it would silently fall back to a backup)
    blocked = tuple(reg.get("unfetchable_domains", []))

    def fetchable(c):
        host = urlparse(c["url"]).hostname or ""
        return not any(host == b or host.endswith("." + b) for b in blocked)

    pool = [c for c in reg["candidates"]
            if c["category"] in CATEGORIES and fetchable(c)
            and not (recent_long and c.get("minutes", 0) >= LONG_READ_MINUTES)]
    for c in reg["candidates"]:
        if not fetchable(c):
            print(f"skipped (site blocks the Kindle job): {c['title'][:70]}")
    ranked = sorted(pool, key=lambda c: score(c, history, today)[0], reverse=True)
    for c in ranked[:6]:
        s, b, p = score(c, history, today)
        print(f"{s:5.2f}  impact {c['impact']:>2}  +{b} -{p}  [{c['category']}] {c['title'][:70]}")

    top_impact = max((c["impact"] for c in ranked), default=0)  # raw impact, without variety bonus
    classic = next_classic(history, today, top_impact)
    if classic:
        pick = {"url": classic["url"], "title": classic["title"], "source": classic["source"],
                "why": classic["why"], "who": classic.get("who", ""), "category": "classic",
                "minutes": classic["minutes"]}
        backups = ranked[:2]
    elif ranked:
        pick, backups = ranked[0], ranked[1:3]
    else:
        print("No eligible candidates and no classic due")
        REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return 1

    entry = {"date": day, "url": pick["url"], "title": pick["title"],
             "category": pick["category"], "minutes": pick.get("minutes", 0)}
    if classic:
        entry["field"] = classic["field"]
    reg["history"] = history + [entry]
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    ed_path = ROOT / "editions" / f"{day}.json"
    ed = json.loads(ed_path.read_text(encoding="utf-8"))
    fields = ("title", "source", "url", "why", "who")
    ed["must_reads"] = [{k: pick.get(k, "") for k in fields}]
    ed["must_read_backups"] = [{k: c.get(k, "") for k in fields} for c in backups]
    ed_path.write_text(json.dumps(ed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(("Classic: " if classic else "Picked: ") + pick["title"])
    return 0


def next_classic(history, today, top_impact):
    """The next unread classic if one is due today, else None."""
    if not CLASSICS.exists():
        return None
    past = sorted((h for h in history if h["category"] == "classic"), key=lambda h: h["date"])
    # before the first classic, count from the first day the registry has any pick
    since = past[-1]["date"] if past else min((h["date"] for h in history), default=today.isoformat())
    gap = (today - d(since)).days
    due = gap >= CLASSIC_DUE_DAYS or (gap >= CLASSIC_MIN_GAP_DAYS and top_impact < SLOW_DAY_SCORE)
    if not due or top_impact >= BIG_FRESH_SCORE:
        return None
    sent = {h["url"] for h in past}
    papers = [p for p in json.loads(CLASSICS.read_text(encoding="utf-8"))["papers"]
              if p.get("status", "unread") == "unread" and p["url"] not in sent]
    if not papers:
        return None
    last_two = [h.get("field") for h in past[-2:]]
    want = "science" if last_two == ["ai", "ai"] else "ai"
    return next((p for p in papers if p["field"] == want), papers[0])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
