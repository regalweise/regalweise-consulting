#!/usr/bin/env python3
"""Generates the blog home (index.html), /blog/*.html and sitemap.xml.
Usage (from repo root):  python3 tools/build.py
Add a post: append a dict to NEW in tools/articles_new.py, then re-run."""
import json, re, html, os, sys
from datetime import datetime
sys.path.insert(0, os.path.dirname(__file__))
from articles_new import NEW

SITE = "https://regalweiseconsulting.in"
WA = "https://wa.me/919380237423"
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">'

# ---- existing articles (migrated) ----
OLD = json.load(open(os.path.join(os.path.dirname(__file__), "articles_existing.json"), encoding="utf-8"))
OLD_META = {  # slug: (filter category, emoji, ISO date)
 "bian": ("Banking Architecture", "🏗️", "2025-05"), "iso": ("Payments", "💳", "2025-04"),
 "ai": ("Agentic AI", "🤖", "2025-03"), "ifrs": ("Credit Risk", "📊", "2025-03"),
 "kyc": ("Compliance", "🔍", "2025-02")}

def strip(h): return html.unescape(re.sub(r"<[^>]+>", " ", h))
def desc_of(body):
    m = re.search(r'<p class="art-lead">(.*?)</p>', body, re.S)
    t = re.sub(r"\s+", " ", strip(m.group(1) if m else body)).strip()
    return t if len(t) < 190 else t[:187].rsplit(" ", 1)[0] + "…"
def mins(body): return max(3, round(len(strip(body).split()) / 200))
def pretty(d): y, m = d.split("-"); return f"{MONTHS[int(m)-1]} {y}"

posts = []
for k, a in OLD.items():
    c, e, d = OLD_META[k]
    posts.append(dict(slug=k if k not in ("ai","iso","bian","ifrs","kyc") else {
        "bian":"bian-first-architecture","iso":"iso-20022-deadline","ai":"agentic-ai-banking-scale",
        "ifrs":"ifrs9-audit-readiness","kyc":"next-gen-kyc-ai-onboarding"}[k],
        cat=c, emoji=e, date=d, title=a["title"], body=a["body"]))
for n in NEW:
    b = f'<p class="art-lead">{n["lead"]}</p><div class="art-divider"></div>'
    for h, p, bl in n["sections"]:
        b += f'<h2 class="art-h2">{h}</h2><p class="art-p">{p}</p><ul class="art-list">' + "".join(f"<li>{x}</li>" for x in bl) + "</ul>"
    b += f'<div class="art-conclusion"><h4>{n["end"][0]}</h4><p>{n["end"][1]}</p></div>'
    posts.append(dict(slug=n["slug"], cat=n["cat"], emoji=n["emoji"], date=n["date"], title=n["title"], body=b))
posts.sort(key=lambda p: p["date"], reverse=True)
for p in posts: p["desc"] = desc_of(p["body"]); p["mins"] = mins(p["body"])

def nav(prefix, active):
    a = lambda n: ' class="active"' if n == active else ""
    return f'''<nav><a class="logo" href="{prefix}"><img src="{prefix}assets/img/logo.jpg" alt="RegalWeise Consulting"></a>
<div class="nav-links"><a href="{prefix}"{a("blog")}>Blog</a><a href="{prefix}consulting/"{a("consulting")}>Consulting</a>
<a href="{prefix}consulting/#contact">Contact</a><a class="nav-cta" href="{WA}" target="_blank" rel="noopener">💬 Talk to Us</a></div></nav>'''

def footer(prefix):
    return f'''<footer><div>© {datetime.now().year} RegalWeise Consulting. All rights reserved.</div>
<div class="links"><a href="{prefix}">Blog</a><a href="{prefix}consulting/">Consulting</a><a href="{prefix}consulting/#contact">Contact</a></div></footer>'''

def band(prefix):
    return f'''<div class="band"><div class="eyebrow">RegalWeise Consulting</div><h2>Need Help Putting This Into <em>Practice</em>?</h2>
<p>Our consulting practice supports banks and financial institutions on architecture, payments, risk, digital assets and agentic AI.</p>
<a class="btn" href="{prefix}consulting/">Explore Consulting</a></div>'''

def head(title, desc, url, prefix, kind="website"):
    t, d = html.escape(title, True), html.escape(desc, True)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{SITE}{url}">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{SITE}{url}"><meta property="og:type" content="{kind}"><meta property="og:site_name" content="RegalWeise Consulting">
{FONTS}<link rel="stylesheet" href="{prefix}assets/css/site.css"></head><body>'''

def card(p, prefix, feature=False):
    return f'''<a class="card{" feature" if feature else ""}" data-cat="{html.escape(p["cat"],True)}" href="{prefix}blog/{p["slug"]}.html">
<div class="card-img">{p["emoji"]}</div><div class="card-body"><div class="cat">{p["cat"]}</div>
<div class="card-title">{p["title"]}</div><div class="card-desc">{html.escape(p["desc"])}</div>
<div class="meta">{p["mins"]} min read · {pretty(p["date"])}</div></div></a>'''

# ---- blog home ----
cats = sorted({p["cat"] for p in posts})
chips = '<button class="chip on" data-f="All">All</button>' + "".join(f'<button class="chip" data-f="{c}">{c}</button>' for c in cats)
home = head("RegalWeise Insights — Banking, Digital Assets & Agentic AI",
  "Practitioner insights on banking architecture, payments, stablecoins, DLT, digital assets, ServiceNow and agentic AI from RegalWeise Consulting.", "/", "")
home += nav("", "blog") + f'''<header class="hero"><div class="eyebrow">The RegalWeise Blog</div>
<h1>Insights on <em>Banking, Digital Assets</em> &amp; Agentic AI</h1>
<p>Practitioner-written perspectives on stablecoins, DLT, tokenization, ServiceNow, payments, risk and compliance — for people transforming financial services.</p></header>
<main class="wrap"><div class="filters">{chips}</div><div class="grid" id="grid">
{card(posts[0], "", True)}{"".join(card(p, "") for p in posts[1:])}</div></main>
{band("")}{footer("")}
<script>document.querySelectorAll('.chip').forEach(function(b){{b.onclick=function(){{document.querySelectorAll('.chip').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');var f=b.dataset.f;document.querySelectorAll('#grid .card').forEach(function(c){{c.style.display=(f==='All'||c.dataset.cat===f)?'':'none';c.classList.toggle('feature',f==='All'&&c===document.querySelector('#grid .card'))}})}}}});</script>
</body></html>'''
open("index.html", "w", encoding="utf-8").write(home)

# ---- article pages ----
os.makedirs("blog", exist_ok=True)
for f in os.listdir("blog"):
    if f.endswith(".html"): os.remove(os.path.join("blog", f))
for p in posts:
    rel = [r for r in posts if r is not p and r["cat"] == p["cat"]][:3]
    rel += [r for r in posts if r is not p and r not in rel][: 3 - len(rel)]
    page = head(p["title"] + " | RegalWeise", p["desc"], f"/blog/{p['slug']}.html", "../", "article")
    page += nav("../", "blog") + f'''<header class="art-head"><a class="back" href="../">← All Insights</a><div class="eyebrow">{p["cat"]}</div>
<h1>{p["title"]}</h1><div class="meta">{p["mins"]} min read · {pretty(p["date"])} · RegalWeise Consulting</div></header>
<article class="art-body">{p["body"]}</article>
<section class="related"><h3>Keep Reading</h3><div class="grid">{"".join(card(r, "../") for r in rel)}</div></section>
{band("../")}{footer("../")}</body></html>'''
    open(f"blog/{p['slug']}.html", "w", encoding="utf-8").write(page)

# ---- sitemap ----
urls = ["/", "/consulting/", "/regalweise-promo.html"] + [f"/blog/{p['slug']}.html" for p in posts]
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  "".join(f"  <url><loc>{SITE}{u}</loc><priority>{'1.0' if u=='/' else '0.8'}</priority></url>\n" for u in urls) + "</urlset>\n")
print(f"Built {len(posts)} posts")
