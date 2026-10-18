# kindle-digest

Daily curated news feeds for KOReader, regenerated every morning by a scheduled Claude task.

| Feed | URL | KOReader setting |
|---|---|---|
| Morning Digest (summaries) | https://zachariasv.github.io/kindle-digest/digest.xml | `download_full_article = false` |
| Must-Reads (3 originals/day) | https://zachariasv.github.io/kindle-digest/mustreads.xml | `download_full_article = true` |

## KOReader setup

Add these to the News Downloader's `feed_config.lua` (Tools → News downloader → Settings → Edit feed list):

```lua
{ "https://zachariasv.github.io/kindle-digest/digest.xml", limit = 1, download_full_article = false, include_images = false, enable_filter = false },
{ "https://zachariasv.github.io/kindle-digest/mustreads.xml", limit = 3, download_full_article = true, include_images = true, enable_filter = false },
```

Then use "Download news" each morning.

## How it works

- `EDITORIAL.md`: the brief the daily task follows
- `editions/YYYY-MM-DD.json`: one file per day
- `build.py`: turns the last 7 editions into `digest.xml` and `mustreads.xml`
