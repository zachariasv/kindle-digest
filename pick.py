"""Pick today's must-read from the candidate registry and write it into the edition.

Usage: python pick.py YYYY-MM-DD

The registry (mustread/registry.json) holds candidates the daily job has found:
  {"candidates": [{url, title, source, why, category, kind, published, added, impact, minutes}],
   "history":    [{date, url, title, category, minutes}]}

Score = impact + variety bonus - age penalty, where
  - variety bonus grows with days since the category was last picked (max +1.5 at 10+ days)
  - fresh pieces lose 0.3 points per day once older than 2 days; evergreen pieces don't age
Rules: never repeat a pick; at most one long read (40+ min) per 7 days;
fresh candidates expire after 7 days, evergreen after 30.
The top pick goes into must_reads, the next two into must_read_backups.
"""
import json
import pathlib
import sys
from datetime import date

ROOT = pathlib.Path(__file__).parent
REGISTRY = ROOT / "mustread" / "registry.json"
CATEGORIES = ["ai-research", "ai-economics", "science", "investigation", "blind-spot"]
MAX_VARIETY_BONUS = 1.5
VARIETY_FULL_AFTER_DAYS = 10
AGE_PENALTY_PER_DAY = 0.3
FRESH_GRACE_DAYS = 2
EXPIRY_DAYS = {"fresh": 7, "evergreen": 30}
LONG_READ_MINUTES = 40
LONG_READ_GAP_DAYS = 7


def d(s):
    return date.fromisoformat(s)


def days_since_category(history, category, today):
    dates = [d(h["date"]) for h in history if h["category"] == category]
    return (today - max(dates)).days if dates else VARIETY_FULL_AFTER_DAYS


def score(c, history, today):
    gap = days_since_category(history, c["category"], today)
    bonus = MAX_VARIETY_BONUS * min(gap, VARIETY_FULL_AFTER_DAYS) / VARIETY_FULL_AFTER_DAYS
    age = (today - d(c["published"])).days
    penalty = 0 if c.get("kind") == "evergreen" else AGE_PENALTY_PER_DAY * max(0, age - FRESH_GRACE_DAYS)
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
    recent_long = any(h.get("minutes", 0) >= LONG_READ_MINUTES and (today - d(h["date"])).days < LONG_READ_GAP_DAYS
                      for h in history)
    pool = [c for c in reg["candidates"]
            if c["category"] in CATEGORIES and not (recent_long and c.get("minutes", 0) >= LONG_READ_MINUTES)]
    ranked = sorted(pool, key=lambda c: score(c, history, today)[0], reverse=True)
    if not ranked:
        print("No eligible candidates")
        return 1

    for c in ranked[:6]:
        s, b, p = score(c, history, today)
        print(f"{s:5.2f}  impact {c['impact']:>2}  +{b} -{p}  [{c['category']}] {c['title'][:70]}")

    top = ranked[0]
    reg["history"] = history + [{"date": day, "url": top["url"], "title": top["title"],
                                 "category": top["category"], "minutes": top.get("minutes", 0)}]
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    ed_path = ROOT / "editions" / f"{day}.json"
    ed = json.loads(ed_path.read_text(encoding="utf-8"))
    fields = ("title", "source", "url", "why")
    ed["must_reads"] = [{k: top[k] for k in fields}]
    ed["must_read_backups"] = [{k: c[k] for k in fields} for c in ranked[1:3]]
    ed_path.write_text(json.dumps(ed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Picked: {top['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
