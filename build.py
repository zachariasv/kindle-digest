"""Build the two KOReader feeds from the edition JSON files.

editions/YYYY-MM-DD.json  ->  digest.xml   (one item per day, full summary inside)
                          ->  mustreads.xml (the daily must-read link)

Run: python build.py
"""
import json
import pathlib
from datetime import datetime, timezone
from email.utils import format_datetime
from html import escape
from xml.sax.saxutils import escape as xml_escape

ROOT = pathlib.Path(__file__).parent
BASE_URL = "https://zachariasv.github.io/kindle-digest"
DAYS_KEPT = 7


def paragraphs(text):
    return "".join(f"<p>{escape(p.strip())}</p>" for p in text.split("\n\n") if p.strip())


def long_date(ed):
    return datetime.strptime(ed["date"], "%Y-%m-%d").strftime("%A %-d %B %Y")


def render_digest(ed):
    out = []
    if ed.get("intro"):
        out.append(paragraphs(ed["intro"]))
    if ed.get("must_reads"):
        m = ed["must_reads"][0]
        out.append("<h2>Today's must-read</h2>")
        out.append(f"<p><b>{escape(m['title'])}</b> ({escape(m['source'])})</p><p>{escape(m['why'])}</p>")
        if m.get("who"):
            out.append(f"<p><i>Who's behind it:</i> {escape(m['who'])}</p>")
    for sec in ed["sections"]:
        out.append(f"<h2>{escape(sec['heading'])}</h2>")
        for it in sec["items"]:
            out.append(f"<h3>{escape(it['title'])}</h3>")
            out.append(paragraphs(it.get("body", "")))
            if it.get("bullets"):
                out.append("<ul>" + "".join(f"<li>{escape(b)}</li>" for b in it["bullets"]) + "</ul>")
            if it.get("source"):
                out.append(f"<p><small><i>{escape(it['source'])}</i></small></p>")
    return "".join(out)


def pub_date(ed):
    d = datetime.strptime(ed["date"], "%Y-%m-%d").replace(hour=5, tzinfo=timezone.utc)
    return format_datetime(d)


def item(title, link, guid, date, html):
    return (
        "<item>"
        f"<title>{xml_escape(title)}</title>"
        f"<link>{xml_escape(link)}</link>"
        f'<guid isPermaLink="false">{xml_escape(guid)}</guid>'
        f"<pubDate>{date}</pubDate>"
        f"<description><![CDATA[{html}]]></description>"
        "</item>"
    )


def channel(title, desc, link, items):
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>'
        f"<title>{xml_escape(title)}</title><link>{link}</link>"
        f"<description>{xml_escape(desc)}</description><language>en</language>"
        + "".join(items)
        + "</channel></rss>\n"
    )


def main():
    files = sorted((ROOT / "editions").glob("*.json"), reverse=True)[:DAYS_KEPT]
    eds = [json.loads(f.read_text(encoding="utf-8")) for f in files]

    digest_items, must_items = [], []
    for ed in eds:
        date = pub_date(ed)
        digest_items.append(item(
            f"Morning Digest, {long_date(ed)}", f"{BASE_URL}/#{ed['date']}", f"digest-{ed['date']}", date, render_digest(ed)))
        for i, m in enumerate(ed.get("must_reads", [])):
            must_items.append(item(
                f"{m['title']} ({m['source']})", m["url"], f"must-{ed['date']}-{i}", date,
                f"<p>{escape(m['why'])}</p>"))

    (ROOT / "digest.xml").write_text(channel(
        "Morning Digest", "Daily curated news digest", BASE_URL, digest_items), encoding="utf-8")
    (ROOT / "mustreads.xml").write_text(channel(
        "Must-Reads", "One must-read a day", BASE_URL, must_items), encoding="utf-8")
    print(f"Built feeds from {len(eds)} edition(s)")


if __name__ == "__main__":
    main()
