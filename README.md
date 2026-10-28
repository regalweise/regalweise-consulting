# RegalWeise Consulting — Blog + Consulting site

- `/` — Blog home (generated)
- `/blog/*.html` — one page per article (generated)
- `/consulting/` — consulting practice: services, industries, contact
- `tools/articles_new.py` + `tools/articles_existing.json` — article sources
- `tools/build.py` — regenerates blog pages and sitemap

**Add a post:** append an entry to `NEW` in `tools/articles_new.py`, run `python3 tools/build.py`, commit and push.
Hosted on GitHub Pages (custom domain via `CNAME`).
