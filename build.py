#!/usr/bin/env python3
"""Generates the static gujaratbio.com site. Run: python3 build.py  (writes pages next to this file)"""
import json, os, html as H

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://b2b.gujaratbio.com"
WA = "919978791167"
PHONE = "+91 99787 91167"
MAIL = "sales@gujaratbio.com"
GA4_ID = "G-HF0J0NF8G0"   # Google Analytics 4 measurement ID (public)
GTM_ID = "GTM-5JDXGL2S"  # Google Tag Manager container for b2b.gujaratbio.com. When set, GTM loads and the direct GA4 tag is dropped.
FB = "https://www.facebook.com/gujaratbio"
YT = "https://www.youtube.com/@Gujaratbio"
NAME = "Gujarat Bio Organics Pvt. Ltd."
CIN = "U24123GJ2009PTC058701"
GST = "24AADCG6029R1Z7"
FACTORY = "Plot No. 321, GIDC 2, Ghanghali Road, Shihor, Bhavnagar, Gujarat 364240"
REGOFF = "First Floor, 110 Shoppers Plaza, Parimal Chowk, Waghawadi Road, Bhavnagar, Gujarat 364002"

WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.8 2 6.8L3 29l6.6-2c1.9 1 4 1.6 6.3 1.6 7.2 0 13-5.7 13-12.8S23.100 3 16 3zm0 23.300c-2 0-3.900-.6-5.500-1.600l-.4-.2-3.900 1.200 1.300-3.800-.3-.4a10.200 10.200 0 0 1-1.600-5.500C5.600 10 10.300 5.400 16 5.400s10.400 4.600 10.400 10.300S21.700 26.300 16 26.300zm5.700-7.700c-.3-.2-1.800-.9-2.100-1-.3-.1-.5-.2-.7.200-.2.300-.8 1-1 1.200-.2.200-.4.200-.7.100-.3-.2-1.300-.5-2.500-1.500-.9-.8-1.500-1.800-1.700-2.100-.2-.3 0-.5.100-.6l.5-.5c.1-.2.200-.3.300-.5.100-.2 0-.4 0-.5l-1-2.300c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.100-.8.400-.3.300-1 1-1 2.400s1 2.800 1.200 3c.1.200 2 3.100 4.900 4.300 2.900 1.200 2.900.8 3.400.8.500 0 1.800-.7 2-1.400.3-.7.300-1.300.2-1.400-.1-.1-.3-.2-.6-.4z"/></svg>'
LOGO = '<svg viewBox="0 0 36 36" aria-hidden="true"><circle cx="18" cy="18" r="17" fill="#1f4d45"/><path d="M8 22c3-1 4 2 7 1s3-4 6-4 4 3 7 2" fill="none" stroke="#d89b21" stroke-width="2.4" stroke-linecap="round"/><path d="M8 27c3-1 4 2 7 1s3-4 6-4 4 3 7 2" fill="none" stroke="#d8e8de" stroke-width="2" stroke-linecap="round"/><path d="M18 17V8M18 12c-2 0-4-1-4.500-3 2.200-.2 4 .8 4.500 3zM18 13c2 0 4-1 4.500-3-2.200-.2-4 .8-4.500 3z" fill="none" stroke="#d8e8de" stroke-width="1.8" stroke-linecap="round"/></svg>'

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"

def esc(s): return H.escape(s, quote=True)

# ------------------------------------------------------------------ data
GROUPS = [("humic", "Humic and fulvic"), ("seaweed", "Seaweed and algae"), ("botanical", "Botanical"),
          ("blends", "Blends"), ("protein", "Protein hydrolysate and amino"), ("other", "Other")]
LAF = "Liquid, granule or powder"
GRADES = [
    ("humic", "Humic acid 5%", "Powder"), ("humic", "Potassium humate 49%", "Powder"),
    ("humic", "Humate and fulvates 22%", "Liquid"), ("humic", "Humates 12.5%", "Liquid"),
    ("humic", "Humic acid 51%", "Granular"), ("humic", "Humic acid 1.5%", "Granules"),
    ("humic", "Humic and fulvic acid 25.05%", "Liquid"), ("humic", "Humic and fulvic acid 76%", "Powder"),
    ("seaweed", "Ascophyllum nodosum 15%", "Liquid"), ("seaweed", "Ascophyllum nodosum 7%", "Liquid"),
    ("seaweed", "Kappaphycus alvarezii 24%", "Liquid"), ("seaweed", "Kappaphycus alvarezii 9.5%", "Liquid"),
    ("seaweed", "Kappaphycus alvarezii 7.2%", "Liquid"), ("seaweed", "Sargassum tenerrimum 10%", "Liquid"),
    ("seaweed", "Sargassum tenerrimum 2%", "Granular"),
    ("seaweed", "Kappaphycus alvarezii + Sargassum swartzii (1:1)", "Liquid"), ("seaweed", "Spirulina 10%", "Liquid"),
    ("botanical", "Adhatoda vasica", "Powder"), ("botanical", "Adhatoda vasica extract 2%", "Liquid"),
    ("blends", "Humic acid + amino acid + vitamins + bio-chemicals", "Powder"),
    ("blends", "Seaweed + algal extract", "Liquid"),
    ("blends", "Seaweed + humic and fulvic acid + amino acids + vitamins", "Liquid"),
    ("blends", "Humic acid + seaweed extract", "Liquid"), ("blends", "Humic acid + seaweed extract", "Powder"),
    ("blends", "Humic acid + seaweed extract", "Granules"), ("blends", "Botanical extract + seaweed extract", "Liquid"),
    ("protein", "Protein hydrolysate, animal source 36.04%", "Liquid"),
    ("protein", "Protein hydrolysate, plant source 25%", LAF), ("protein", "Protein hydrolysate, plant source 16.9%", LAF),
    ("protein", "Protein hydrolysate, plant source 1.5%", LAF), ("protein", "Protein hydrolysate, plant source 27%", LAF),
    ("protein", "Amino acid 5%", LAF), ("protein", "Amino acid 10%", LAF), ("protein", "Amino acid 20%", LAF),
    ("protein", "Vinasse residue (glutamic acid 18%)", "Liquid"),
    ("other", "2-Bromo-(1H)-indole-3-carboxaldehyde 1 ppm", "Liquid"),
]
assert len(GRADES) == 36, len(GRADES)
BIOS = ["Azotobacter", "Carrier-based consortia", "Azospirillum", "Liquid consortia", "Mycorrhizal biofertilisers",
        "Phosphate solubilising bacteria", "Potash mobilising bacteria (KMB)", "Acetobacter", "Rhizobium",
        "Zinc solubilising bacteria", "Phosphate solubilising fungal biofertilisers"]
assert len(BIOS) == 11

NAV = [("/products", "Products"), ("/crops", "Crops"), ("/private-label-oem", "Private label"), ("/export", "Export"),
       ("/bulk-supply", "Bulk supply"), ("/research-development", "R&amp;D"), ("/resources", "Knowledge")]

# ------------------------------------------------------------------ components
def img(name, alt, cls="", w=None, h=None, lazy=True, caption=None):
    a = f'<img src="/assets/img/{name}.webp" alt="{esc(alt)}"' + (' loading="lazy"' if lazy else '') + ' decoding="async"'
    if not w:
        try:
            from PIL import Image as _I
            w, h = _I.open(os.path.join(ROOT, "assets", "img", name + ".webp")).size
        except Exception:
            w = None
    if w: a += f' width="{w}" height="{h}"'
    a += (f' class="{cls}"' if cls else '') + '>'
    if caption:
        return f'<figure class="fig">{a}<figcaption>{esc(caption)}</figcaption></figure>'
    return a

def faq_html(items):
    out = '<div class="faq">'
    for q, a in items:
        out += f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
    return out + '</div>'

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def org_ld():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": SITE + "/#org",
            "name": "Gujarat Bio Organics Pvt. Ltd.", "legalName": "Gujarat Bio Organics Private Limited",
            "url": SITE + "/", "logo": SITE + "/assets/favicon.svg", "foundingDate": "2009-11-25",
            "description": "Gujarat Bio Organics Pvt. Ltd. manufactures biostimulants, biofertilisers and organic fertilizers in Bhavnagar, India. b2b.gujaratbio.com is the open, public B2B website of Gujarat Bio Organics. No login or dealer approval is needed to browse it: buyers request quotes and free samples directly.",
            "identifier": CIN, "taxID": GST, "email": MAIL, "telephone": "+919978791167",
            "slogan": "One manufacturer, three ways to buy: our Immunity brand, your private label, or bulk supply.",
            "address": {"@type": "PostalAddress", "streetAddress": "Plot No. 321, GIDC 2, Ghanghali Road, Shihor",
                        "addressLocality": "Bhavnagar", "addressRegion": "Gujarat", "postalCode": "364240", "addressCountry": "IN"},
            "areaServed": ["GCC countries", "Africa", "Russian Federation", "Europe", "North America", "South America", "India"],
            "knowsAbout": ["Organic fertilizers", "Biostimulants", "Humic acid", "Fulvic acid", "Potassium humate", "Seaweed extract",
                           "Protein hydrolysate", "Amino acids", "Biofertilisers", "Micronutrient fertilizers", "Water-soluble fertilizers",
                           "Slow-release fertilizers", "Custom fertilizer blends", "Crop-specific fertilizers", "Zyme granules",
                           "FCO Schedule VI", "Private label fertilizer manufacturing"],
            "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "telephone": "+919978791167",
                              "email": MAIL, "availableLanguage": ["English", "Hindi", "Gujarati"]}],
            "sameAs": [FB, YT]}

def crumbs_ld(path, title):
    items = [("Home", "/")]
    if path != "/": items.append((title, path))
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + (u if u != "/" else "/")} for i, (n, u) in enumerate(items)]}

def header(path):
    links = "".join(f'<a href="{u}"' + (' aria-current="page"' if path == u else '') + f'>{t}</a>' for u, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap hdr">
<a class="brand" href="/">{LOGO}<span>Gujarat Bio Organics<small>Organic fertilizers, biostimulants, biofertilisers</small></span></a>
<button class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main">{links}<a class="btn btn-primary" href="/contact">Request a quote</a></nav>
</div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="wrap"><div class="fgrid">
<div><h2 class="fh">{NAME}</h2><address>Factory: {FACTORY}<br><br>Registered office: {REGOFF}</address>
<p style="margin-top:1rem">CIN {CIN}<br>GSTIN {GST}</p></div>
<div><h2 class="fh">Products</h2><ul><li><a href="/organic-fertilizer-manufacturer-india">Organic fertilizers</a></li><li><a href="/biostimulants-manufacturer-india">Biostimulants</a></li><li><a href="/humic-acid-manufacturer-india">Humic acid</a></li><li><a href="/seaweed-extract-manufacturer-india">Seaweed extract</a></li><li><a href="/amino-acid-protein-hydrolysate-manufacturer-india">Amino acids</a></li><li><a href="/biofertilisers-manufacturer-india">Biofertilisers</a></li><li><a href="/micronutrient-fertilizer-manufacturer-india">Micronutrients</a></li><li><a href="/water-soluble-fertilizer-special-grades">Special grades</a></li><li><a href="/slow-release-fertilizer">Slow release</a></li><li><a href="/zyme-granules-manufacturer">Zyme granules</a></li><li><a href="/custom-fertilizer-blends">Custom blends</a></li><li><a href="/crop-specific-fertilizers">Crop-specific</a></li></ul></div>
<div><h2 class="fh">Company</h2><ul><li><a href="/about">About us</a></li><li><a href="/why-gujarat-bio">Why we are different</a></li><li><a href="/impact">Our story and grower videos</a></li><li><a href="/research-development">R&amp;D</a></li><li><a href="/manufacturing-facility">Manufacturing</a></li><li><a href="/quality-compliance">Quality and compliance</a></li><li><a href="/private-label-oem">Private label and OEM</a></li><li><a href="/bulk-supply">Bulk supply</a></li><li><a href="/export">Export</a></li><li><a href="/become-a-distributor">Become a distributor</a></li><li><a href="/contact">Contact</a></li></ul></div>
<div><h2 class="fh">Knowledge</h2><ul><li><a href="/resources">Knowledge centre</a></li><li><a href="/crops">Crop programmes</a></li><li><a href="/field-solutions">Field solutions</a></li><li><a href="/fco-schedule-vi-biostimulants">FCO Schedule VI</a></li><li><a href="/glossary">Glossary</a></li><li><a href="/faq">FAQ</a></li></ul></div>
<div><h2 class="fh">Talk to us</h2><ul><li><a href="https://wa.me/{WA}">WhatsApp {PHONE}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{FB}" rel="noopener">Facebook</a></li><li><a href="{YT}" rel="noopener">YouTube</a></li></ul></div>
</div><div class="fbot"><span>&copy; <span id="yr">2026</span> {NAME} Biostimulant and organic fertilizer manufacturer, Bhavnagar, Gujarat, India.</span><span>Open B2B site: no login needed. Request a quote or free sample directly. Product images are illustrative samples. <a href="/privacy-policy">Privacy and cookies</a> <button type="button" class="linkbtn" data-cookie-settings>Cookie settings</button></span></div></div></footer>
<aside aria-label="Chat"><button type="button" class="chat-launch" id="chat-open" aria-controls="chat-panel" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/></svg><span>Ask our sales team</span></button><a class="wa-float" href="https://wa.me/{WA}" aria-label="Chat on WhatsApp">{WA_SVG}<span>WhatsApp us</span></a></aside>'''

def cta(title="Tell us what you need. We reply with a quote and a free sample.", sub="No minimum order quantity. Dispatch in about one week.", msg="Hello Gujarat Bio Organics, I would like a quote."):
    return f'''<section class="cta"><div class="wrap"><div><h2>{title}</h2><p>{sub}</p></div>
<div class="btn-row" style="margin:0"><a class="btn btn-primary" href="/contact">Request a quote</a><a class="btn btn-wa" href="{wa(msg)}">{WA_SVG}WhatsApp {PHONE}</a></div></div></section>'''

def page_hero(title, lead, path, crumb):
    return f'''<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="/">Home</a> / {esc(crumb)}</div>
<h1>{title}</h1><p>{lead}</p></div></section>'''

def field(name, label, typ="text", req=False, opts=None, ph=""):
    r = " required" if req else ""
    if typ == "select":
        o = "".join(f'<option value="{esc(x)}">{esc(x)}</option>' for x in [""] + opts)
        return f'<div class="field"><label for="f-{name}">{label}</label><select id="f-{name}" name="{name}" data-label="{label}"{r}>{o}</select></div>'
    if typ == "textarea":
        return f'<div class="field"><label for="f-{name}">{label}</label><textarea id="f-{name}" name="{name}" data-label="{label}"{r}></textarea></div>'
    return f'<div class="field"><label for="f-{name}">{label}</label><input id="f-{name}" name="{name}" type="{typ}" data-label="{label}" placeholder="{esc(ph)}"{r}></div>'

def form(title, subject, fields, note=None):
    return f'''<div class="form-box" id="enquiry"><h3>{title}</h3><p class="mute" style="font-size:.95rem;margin-bottom:1rem">Fill this in and press send. Our team replies within one working day.</p>
<form data-enquiry data-subject="{esc(subject)}" novalidate>{"".join(fields)}
<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="form-actions"><button class="btn btn-wa" type="submit">Send enquiry</button></div>
<p class="note">{note or "Free samples. Freight or courier, customs duty and other charges are paid by the buyer."}</p>
<p class="form-msg" role="status" aria-live="polite"></p></form></div>'''


EEA_GB_CH = ["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE","IT","LV","LT","LU","MT","NL","PL","PT","RO","SK","SI","ES","SE","IS","LI","NO","GB","CH"]

def page_type(path):
    if path == "/": return "home"
    if path == "/404": return "404"
    if path.startswith("/products/"): return "product"
    if path.startswith("/crops/"): return "crop"
    if path.startswith("/resources/") or path.startswith("/glossary/"): return "article"
    if path in ("/contact", "/bulk-supply", "/export", "/private-label-oem", "/become-a-distributor"): return "lead_page"
    if path in ("/impact", "/why-gujarat-bio", "/about", "/research-development", "/manufacturing-facility", "/quality-compliance"): return "company"
    if path == "/privacy-policy": return "legal"
    if path.endswith("-india") or path in ("/products", "/slow-release-fertilizer", "/zyme-granules-manufacturer", "/crop-specific-fertilizers", "/custom-fertilizer-blends", "/field-solutions", "/crops", "/resources", "/faq", "/glossary", "/fco-schedule-vi-biostimulants", "/water-soluble-fertilizer-special-grades"): return "category"
    return "other"

def tracking_head(path):
    """Consent defaults first, then either GTM or the direct GA4 tag. Runs before anything else on the page."""
    pt = page_type(path)
    gtm = GTM_ID.strip()
    js = ("window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
          "(function(){var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}"
          "var eu=/^(Europe\\/|Atlantic\\/(Canary|Madeira|Azores|Faroe|Reykjavik))/.test(tz),c='',q=location.search,i='';"
          "try{c=localStorage.getItem('gbo_consent')||'';if(/[?&]internal=1/.test(q))localStorage.setItem('gbo_internal','1');"
          "if(/[?&]internal=0/.test(q))localStorage.removeItem('gbo_internal');i=localStorage.getItem('gbo_internal')?'internal':''}catch(e){}"
          "var v=c||(eu?'denied':'granted');window.GBO_CONSENT=v;window.GBO_NEEDS_CHOICE=!c&&eu;window.GBO_PT='" + pt + "';window.GBO_GTM=" + ("true" if gtm else "false") + ";"
          "function cs(s){return{ad_storage:s,ad_user_data:s,ad_personalization:s,analytics_storage:s}}"
          "if(!c){var r=cs('denied');r.region=" + json.dumps(EEA_GB_CH) + ";gtag('consent','default',r)}"
          "var d=cs(v);d.wait_for_update=500;gtag('consent','default',d);"
          "var p={page_type:'" + pt + "'};if(i)p.traffic_type=i;")
    if gtm:
        js += ("dataLayer.push(p);(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
               "var f=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i;f.parentNode.insertBefore(j,f)})"
               "(window,document,'script','dataLayer','" + gtm + "')})();")
        return "<script>" + js + "</script>"
    js += "gtag('js',new Date());gtag('config','" + GA4_ID + "',p)})();"
    return f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script><script>' + js + "</script>"

def tracking_noscript():
    g = GTM_ID.strip()
    return f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={g}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>' if g else ""

def render(path, title, desc, body, schemas=None, crumb=None, noindex=False, og_img="/assets/img/private-label-premium-enriched.webp"):
    url = SITE + (path if path != "/" else "/")
    ld = [org_ld()] if path == "/" else []
    if path == "/":
        ld.append({"@context": "https://schema.org", "@type": "WebSite", "url": SITE + "/", "name": NAME, "publisher": {"@id": SITE + "/#org"}})
    elif crumb:
        ld.append(crumbs_ld(path, crumb))
    ld += (schemas or [])
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    out = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">{tracking_head(path)}<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}{og_img}">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#143630">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONT_URL}" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="{FONT_URL}"></noscript>
<style>{INLINE_CSS}</style>{ldh}</head>
<body>{tracking_noscript()}{header(path)}<main id="main">{body}</main>{footer()}<script>window.GBO_CHAT_V="{JS_VER}"</script><script src="/assets/main.js?v={JS_VER}" defer></script></body></html>'''
    d = ROOT if path == "/" else os.path.join(ROOT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(out)
    return path

PAGES = []  # (path, priority)
import hashlib as _hl
JS_VER = _hl.md5(open(os.path.join(ROOT, "assets", "main.js"), "rb").read() + open(os.path.join(ROOT, "assets", "chat.js"), "rb").read()).hexdigest()[:8]
FONT_URL = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap"
import re as _re0
INLINE_CSS = _re0.sub(r"\s*([{};:,>])\s*", r"\1", _re0.sub(r"/\*.*?\*/", "", open(os.path.join(ROOT, "assets", "styles.css"), encoding="utf-8").read(), flags=_re0.S)).replace(";}", "}").strip()
for _f in ("ext_00_helpers.py", "ext_05_grade_data.py"):
    exec(open(os.path.join(ROOT, _f), encoding="utf-8").read())

CAT_HUB = [("/organic-fertilizer-manufacturer-india", "Organic fertilizers", "Organic and bio-organic inputs for soil and crop health."),
           ("/biostimulants-manufacturer-india", "Biostimulants", "36 Schedule VI grades: humic, seaweed, amino, botanical, blends."),
           ("/humic-acid-manufacturer-india", "Humic acid and fulvic acid", "8 grades, granules, powder and liquid, incl. potassium humate."),
           ("/seaweed-extract-manufacturer-india", "Seaweed extracts", "Ascophyllum, Kappaphycus, Sargassum and Spirulina."),
           ("/amino-acid-protein-hydrolysate-manufacturer-india", "Amino acids and protein hydrolysates", "Plant and animal source, 9 grades."),
           ("/biofertilisers-manufacturer-india", "Biofertilisers", "11 types: N fixers, PSB, KMB, ZSB, mycorrhizae, consortia."),
           ("/micronutrient-fertilizer-manufacturer-india", "Micronutrients", "Zinc, boron, iron and more, chelated and mixtures, made to order."),
           ("/water-soluble-fertilizer-special-grades", "Special grade fertilizers", "Water-soluble NPK and fortified grades, made to order."),
           ("/slow-release-fertilizer", "Slow-release fertilizers", "Granules that feed over weeks, made to order."),
           ("/zyme-granules-manufacturer", "Zyme granules", "Humic, seaweed and protein granules from listed grades."),
           ("/custom-fertilizer-blends", "Custom blends", "Formulated by our R&D team for your crop and market."),
           ("/crop-specific-fertilizers", "Crop-specific products", "The Immunity range for sugarcane, potato, mango, apple, banana.")]

# ------------------------------------------------------------------ HOME
home_faq = [
    ("Who is Gujarat Bio Organics?", "Gujarat Bio Organics Pvt. Ltd. is a biostimulant and organic fertilizer manufacturer based in Shihor, Bhavnagar, Gujarat, India. We make humic and fulvic acid, seaweed extract, protein hydrolysate, amino acid and biofertiliser products, and supply them under our Immunity brand, under your private label, or in bulk."),
    ("Is there a minimum order quantity?", "No. We quote against your requirement, including small trial orders."),
    ("Do you supply private label and OEM?", "Yes. We formulate, manufacture and pack under your brand, label and pack design."),
    ("Which countries do you supply?", "We supply GCC countries, Africa, the Russian Federation, Europe, North America and South America, and all of India. Export terms are FOB or CIF from Indian ports."),
    ("Do you give samples?", "Yes. Samples are free. Freight or courier, customs duty and other charges are paid by the buyer."),
    ("How long does an order take?", "Typically about one week."),
    ("Are your biostimulants approved?", "The Directorate of Agriculture, Government of Gujarat has issued No Objection Certificates to us for 36 biostimulant grades (Schedule VI) and 11 biofertiliser types (Schedule III) under the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985. Copies are on request."),
]
home = f'''
<section class="hero"><div class="wrap"><div>
<h1>Biostimulants and organic inputs, made in Gujarat. Supplied under your brand or ours.</h1>
<p class="lead">Organic fertilizers, humic acid, seaweed extract, amino acids, biofertilisers, micronutrients and custom blends from our own plant in GIDC Shihor, Bhavnagar. Built on 20 years of in-house R&amp;D and field work. No minimum order quantity. Dispatch in about one week.</p>
<div class="btn-row"><a class="btn btn-primary" href="/contact">Request a quote</a><a class="btn btn-wa" href="{wa("Hello Gujarat Bio Organics, I would like a free sample.")}">{WA_SVG}Request a free sample</a></div>
</div>
<div class="label" role="group" aria-label="Supply terms at a glance"><div class="label-top"><span>Supply terms</span><span>Batch ready</span></div>
<dl>
<div class="row"><dt>Minimum order</dt><dd>None</dd></div>
<div class="row"><dt>Liquid capacity</dt><dd>100 KL a month</dd></div>
<div class="row"><dt>Solid capacity</dt><dd>2,500 tonnes a month</dd></div>
<div class="row"><dt>Liquid packs</dt><dd>250 mL to 1000 L IBC</dd></div>
<div class="row"><dt>Solid packs</dt><dd>1 kg to 1000 kg jumbo</dd></div>
<div class="row"><dt>Lead time</dt><dd>About 1 week</dd></div>
<div class="row"><dt>Incoterms</dt><dd>FOB or CIF</dd></div>
<div class="row"><dt>Samples</dt><dd>Free</dd></div>
</dl><div class="label-bot"><span>Shihor, Bhavnagar, Gujarat, India</span><span class="barcode" aria-hidden="true"></span></div></div>
</div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><h2>One manufacturer, three ways to buy</h2>
<p class="answer" style="margin-bottom:0">Gujarat Bio Organics manufactures biostimulants and biofertilisers in Bhavnagar, India. You can buy our Immunity range, have us make a private-label line for you, or buy bulk volumes for your own formulation or distribution.</p></div>
<div class="paths">
<div class="path"><h3>Buy the Immunity range</h3><p>Crop-specific products for sugarcane, potato, mango, apple and more, built from field work with growers.</p><a class="more" href="/products">See products</a></div>
<div class="path"><h3>Launch your own brand</h3><p>Private label and OEM. We formulate, manufacture and pack under your name, with your label and pack design.</p><a class="more" href="/private-label-oem">Private label and OEM</a></div>
<div class="path"><h3>Bulk and export supply</h3><p>IBC, drum and retail packs, liquids and solids, shipped from Pipavav, Kandla, Dahej, Mundra and JNPT.</p><a class="more" href="/bulk-supply">Bulk supply</a> &nbsp;&middot;&nbsp; <a class="more" href="/export">Export</a></div>
</div></div></section>

<section class="section dark"><div class="wrap"><div class="sec-head"><h2>Why our products are not like the rest</h2>
<p class="answer" style="margin-bottom:0">Many humic acid, seaweed and amino acid powders are made to a price. Ours are made to protect what works: the right raw material, a gentle process, and proof you can test.</p></div>
<div class="hub">
<a class="hub-i" href="/why-gujarat-bio"><h3>Humic acid</h3><p>The best source out of hundreds, found over 20 years in the field, and extracted without the harsh, hot, high-pH processing that damages fragile compounds.</p></a>
<a class="hub-i" href="/why-gujarat-bio"><h3>Seaweed extract</h3><p>Only a few of thousands of species suit farming. Every step from cultivation to extraction is protocol-controlled, so the extract stays rich, not a plain powder.</p></a>
<a class="hub-i" href="/why-gujarat-bio"><h3>Amino acids</h3><p>Chosen source, careful hydrolysis, preservation and quality control, not an imported powder made to a price.</p></a></div>
<div class="btn-row"><a class="btn btn-primary" href="/why-gujarat-bio">See what makes us different</a><a class="btn btn-wa" href="{wa("Hello Gujarat Bio Organics, I would like a free sample to compare with my current supplier.")}">{WA_SVG}Compare with a free sample</a></div></div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><h2>Everything we make, in one plant</h2><p>Organic fertilizers, biostimulants, biofertilisers and specialty fertilizers, developed by our in-house R&amp;D team and made at our plant in Shihor, Bhavnagar.</p></div>
{hub(CAT_HUB)}
<div class="btn-row"><a class="btn btn-dark" href="/research-development">Our R&amp;D</a><a class="btn btn-ghost" href="/manufacturing-facility">Manufacturing facility</a></div>
</div></section>

<section class="section"><div class="wrap"><div class="prose"><h2>A fertilizer manufacturing company in Bhavnagar, Gujarat</h2>
<p>We are a manufacturer, not a trader. Our own plant at GIDC Shihor, Bhavnagar, has capacity for 100 KL of liquid and 2,500 tonnes of solid products every month, and our in-house R&amp;D team formulates for crops and markets. Buyers choose us for bulk supply, private label or export, with no minimum order quantity. Read <a href="/about">about the company</a>, tour <a href="/manufacturing-facility">the manufacturing facility</a>, or see <a href="/bulk-pricing-and-quotes">how bulk pricing works</a>.</p></div></div></section>

<section class="section story"><div class="wrap"><div class="two"><div><h2>Twenty years on real farms</h2>
<p>We have spent two decades solving growers' burning problems in sugarcane, potato, mango, apple, banana, citrus and coconut, in regions from the Himalayas to South Gujarat. Growers share their own experience in videos on YouTube and Facebook.</p>
<div class="btn-row"><a class="btn btn-primary" href="/impact">See the field record</a></div></div>
<div><h2>Open to the world</h2><p>Hazardous-chemical-free, sustainable food cultivation should be easy for everyone, for generations to come. The formula we proved in the field is now open to importers, brand owners, distributors and growers worldwide.</p>
<div class="btn-row"><a class="btn btn-dark" href="/impact#open-to-the-world">Partner with us</a></div></div></div></div></section>

<section class="section tint"><div class="wrap">
<div class="sec-head"><h2>Our core biostimulant families</h2><p>Three material families, each in several grades. Every grade listed is covered by our Gujarat Directorate of Agriculture No Objection Certificate.</p></div>
<div class="materials">
<div class="mat"><a href="/biostimulants-manufacturer-india#humic">{img("humic-acid-51-granular","Humic acid 51% granules in a glass bowl")}<h3>Humic and fulvic</h3><div class="forms">8 grades &middot; liquid, powder, granular</div><p>Soil conditioners that support structure, nutrient holding and root development.</p></a></div>
<div class="mat"><a href="/biostimulants-manufacturer-india#seaweed">{img("kappaphycus-24-liquid","Kappaphycus alvarezii 24% liquid seaweed extract in a beaker")}<h3>Seaweed and algae</h3><div class="forms">9 grades &middot; Ascophyllum, Kappaphycus, Sargassum, Spirulina</div><p>Extracts used to help crops through stress, flowering and fruit set.</p></a></div>
<div class="mat"><a href="/biostimulants-manufacturer-india#protein">{img("amino-20-liquid","Amino acid 20% liquid in a beaker")}<h3>Protein hydrolysate and amino</h3><div class="forms">9 grades &middot; plant and animal source</div><p>Amino acid products that support recovery and growth after stress.</p></a></div>
</div>
<p class="also">Also: 7 blended grades, 2 botanical grades and <a href="/biofertilisers-manufacturer-india">11 biofertiliser types</a>.</p>
</div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><h2>Built around real field problems</h2><p>Twenty years of R&amp;D and on-field work taught us that growers do not buy a grade, they solve a problem. Hard soil. Heat and salt stress. Poor flowering. Fertiliser that does not get taken up.</p></div>
<div class="two"><div><h3>Start from the problem</h3><p>Our Field solutions page sets out the common problems we are asked about, what each product family is used for, and which grades to ask for. Share your crop and region and we will recommend a trial.</p><div class="btn-row"><a class="btn btn-dark" href="/field-solutions">See field solutions</a></div></div>
<figure class="fig">{img("granules-in-hand","Black humic granules held in an open hand")}<figcaption>Humic granules. Illustrative sample image.</figcaption></figure></div>
</div></section>

<section class="section dark"><div class="wrap">
<div class="sec-head"><h2>How a private-label order runs</h2><p>Four steps, from idea to dispatch. Typical time from approval to dispatch is about one week.</p></div>
<div class="steps">
<div class="step"><h3>Brief</h3><p>Tell us your crops, market and product idea, or choose from our existing grades.</p></div>
<div class="step"><h3>Sample</h3><p>We recommend a grade or formulate to your brief and send a free sample.</p></div>
<div class="step"><h3>Approve</h3><p>You approve the sample and your label and pack design.</p></div>
<div class="step"><h3>Dispatch</h3><p>We manufacture, pack under your brand and ship, FOB or CIF.</p></div>
</div>
<div class="btn-row"><a class="btn btn-primary" href="/private-label-oem">See private label and OEM</a></div></div></section>

<section class="section"><div class="wrap"><div class="markets"><div>
<h2>Shipping worldwide</h2><p>We supply importers, distributors and brand owners in these regions, and across India.</p>
<ul class="regions"><li>GCC countries</li><li>Africa</li><li>Russian Federation</li><li>Europe</li><li>North America</li><li>South America</li></ul></div>
<div><h3>Loading ports</h3><ul class="ports"><li>Pipavav</li><li>Kandla</li><li>Dahej</li><li>Mundra</li><li>JNPT</li><li>All Indian ports</li></ul>
<dl class="facts" style="margin-top:2rem"><div><dt>Incoterms</dt><dd>FOB or CIF</dd></div><div><dt>Samples</dt><dd>Free. Buyer pays freight, duty and other charges.</dd></div><div><dt>Testing</dt><dd>Third-party testing and sampling available</dd></div><div><dt>Company</dt><dd>CIN {CIN}</dd></div></dl>
<div class="btn-row"><a class="btn btn-dark" href="/export">Export terms</a></div></div></div></div></section>

<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Common questions</h2></div>{faq_html(home_faq)}</div></section>
{cta()}'''
render("/", "Organic Fertilizer & Biostimulant Manufacturer India | GBO",
       "Organic fertilizers, humic acid, seaweed extract, amino acids, biofertilisers and custom blends made in Gujarat. Private label, bulk and export.",
       home, [faq_ld(home_faq)])
PAGES.append(("/", "1.0"))

# ------------------------------------------------------------------ PRODUCTS HUB
prod_faq = [("What product types do you manufacture?", "Humic and fulvic acid, seaweed and algae extracts, protein hydrolysates and amino acids, blended biostimulants, botanical extracts and biofertilisers, in liquid, powder and granular forms."),
            ("Can I see which grades are approved?", "Yes. The Biostimulants page lists all 36 grades covered by our Gujarat Directorate of Agriculture NOC, and the Biofertilisers page lists 11 types.")]
prods = f'''{page_hero("Biostimulants and biofertilisers from one manufacturer", "Choose a family below, or tell us your crop and we will recommend a grade.", "/products", "Products")}
<section class="section"><div class="wrap">
<div class="answer">Gujarat Bio Organics manufactures organic fertilizers, 36 biostimulant grades, 11 biofertiliser types, and micronutrient, water-soluble, slow-release and custom fertilizers at its plant in Shihor, Bhavnagar, Gujarat. Each is available in bulk, under your private label, or under our Immunity brand.</div>
<p>Gujarat Bio Organics is a fertilizer manufacturer, so every family below is made at our own plant rather than bought in. Humic and fulvic acid, seaweed and algae extracts, amino acids and protein hydrolysates are the core biostimulants. Biofertilisers cover nitrogen fixers, phosphate and potash mobilisers and other beneficial microbes. Micronutrients, water-soluble and slow-release fertilizers and custom blends complete the range. Choose a family to see its grades, uses and questions, or send us your crop and we will recommend one.</p>
<h2>Product families</h2>
{hub(CAT_HUB)}
<h2 style="margin-top:3.4rem">Ways to buy</h2>
<ul class="checks"><li><a href="/bulk-supply">Bulk supply</a>: IBC, drums and jumbo bags, no minimum order</li><li><a href="/private-label-oem">Private label and OEM</a>: your brand, our plant</li><li><a href="/export">Export</a>: FOB or CIF from Indian ports</li><li><a href="/become-a-distributor">Distributor</a>: bulk prices, you set your margin</li></ul>
</div></section>{cta()}'''
render("/products", "Products: Organic Fertilizers, Biostimulants & More | GBO",
       "Organic fertilizers, humic acid, seaweed, amino acids, 11 biofertilisers, micronutrients, special grades and custom blends from Gujarat. Bulk, private label, export.", prods, [faq_ld(prod_faq)], "Products")
PAGES.append(("/products", "0.9"))

# ------------------------------------------------------------------ BIOSTIMULANTS (grade explorer)
GRADE_IMG = [
    ("humic", "humic-acid-51-granular", "Humic acid 51% granular"), ("humic", "humic-acid-1-5-granules", "Humic acid 1.5% granules"),
    ("seaweed", "ascophyllum-15-liquid", "Ascophyllum nodosum 15% liquid"), ("seaweed", "ascophyllum-7-liquid", "Ascophyllum nodosum 7% liquid"),
    ("seaweed", "kappaphycus-24-liquid", "Kappaphycus alvarezii 24% liquid"), ("seaweed", "kappaphycus-9-5-liquid", "Kappaphycus alvarezii 9.5% liquid"),
    ("seaweed", "kappaphycus-7-2-liquid", "Kappaphycus alvarezii 7.2% liquid"), ("seaweed", "sargassum-10-liquid", "Sargassum tenerrimum 10% liquid"),
    ("protein", "amino-20-liquid", "Amino acid 20% liquid"), ("blends", "humic-seaweed-granules", "Humic acid + seaweed extract granules"),
]
chips = '<button class="chip" data-g="all" aria-pressed="true">All <small>36</small></button>' + "".join(
    f'<button class="chip" data-g="{k}" aria-pressed="false">{n} <small>{sum(1 for g in GRADES if g[0]==k)}</small></button>' for k, n in GROUPS)
rows = ""
gn = dict(GROUPS)
for i, (g, n, f) in enumerate(GRADES, 1):
    rows += f'<tr data-g="{g}" data-name="{esc(n)}" data-form="{esc(f)}"><td class="n">{i}</td><td><a href="{grade_path(n, f)}">{esc(n)}</a></td><td class="f"><span>{esc(f)}</span></td><td>{gn[g]}</td><td class="s"><input type="checkbox" aria-label="Select {esc(n)} ({esc(f)})"></td></tr>'
gal = '<div class="gal three">' + "".join(img(n, c, caption=c + ". Illustrative sample.") for _, n, c in GRADE_IMG[:6]) + '</div>'
bs_faq = [("What is a biostimulant under Indian law?", "In India, biostimulants are regulated under Schedule VI of the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985. Each product needs an approved grade. Our No Objection Certificate from the Directorate of Agriculture, Government of Gujarat covers 36 grades."),
          ("What is the difference between Ascophyllum, Kappaphycus and Sargassum extracts?", "They are different seaweeds. Ascophyllum nodosum is a cold-water brown alga, Kappaphycus alvarezii is a red alga farmed in warm waters, and Sargassum is a tropical brown alga. Each gives a different composition, so the right grade depends on your crop and use."),
          ("Can I buy a single grade in small quantity?", "Yes. There is no minimum order quantity. Tick the grades you want and send the list on WhatsApp for a quote."),
          ("Do you make liquid and granular versions?", "Several grades are available in more than one form. The table shows the form for each grade. Ask us if you need a form that is not listed.")]
bs = f'''{page_hero("Biostimulant manufacturer in India: 36 approved grades", "Humic and fulvic acid, seaweed extract, protein hydrolysate, amino acid, botanical and blended grades. Tick the grades you need and send one quote request.", "/biostimulants-manufacturer-india", "Biostimulants")}
<section class="section"><div class="wrap">
<div class="answer">Gujarat Bio Organics holds a Gujarat Directorate of Agriculture No Objection Certificate for 36 biostimulant grades under Schedule VI of the Fertiliser Control Order. All are made at our plant in Shihor, Bhavnagar and are available in bulk, private label or retail packs.</div>
<div id="humic"></div><div id="seaweed"></div><div id="protein"></div>
<div class="chips" role="group" aria-label="Filter grades by group">{chips}</div>
<div class="tbl-wrap"><table class="grades" id="grades"><thead><tr><th>#</th><th>Grade</th><th>Form</th><th>Group</th><th>Select</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="note-box">Select any grades and a bar appears to send your list to us on WhatsApp. Form is shown as supplied; ask us if you need another form.</p>
</div></section>
<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Sample presentation</h2><p>Samples are free. These images show how our grades look in the beaker. They are illustrative renderings, not lab photographs.</p></div>{gal}</div></section>
<section class="section"><div class="wrap"><div class="sec-head"><h2>Questions about biostimulants</h2></div>{faq_html(bs_faq)}</div></section>
<div class="bar" id="bar" role="region" aria-label="Selected grades"><div class="wrap"><span id="bar-count">0 grades selected</span><span><button class="linkbtn" id="bar-clear">Clear</button> <button class="btn btn-wa" id="bar-send">Request a quote for these grades</button></span></div></div>
{cta()}'''
render("/biostimulants-manufacturer-india", "Biostimulant Manufacturer India: 36 FCO Grades | GBO",
       "Humic, fulvic, seaweed, amino and protein hydrolysate biostimulants from Bhavnagar, Gujarat. 36 grades under Gujarat NOC. Bulk, private label, export.", bs, [faq_ld(bs_faq)], "Biostimulants")
PAGES.append(("/biostimulants-manufacturer-india", "0.9"))

# ------------------------------------------------------------------ BIOFERTILISERS
bf_img = [("acetobacter", "Acetobacter biofertiliser sample"), ("phosphate-solubilising-bacteria", "Phosphate solubilising bacteria sample"),
          ("potash-mobilising-bacteria", "Potash mobilising bacteria sample"), ("zinc-solubilising-bacteria", "Zinc solubilising bacteria sample"),
          ("azospirillum", "Azospirillum biofertiliser sample")]
bf_faq = [("What are biofertilisers?", "Biofertilisers are products that contain living microorganisms. Applied to seed, soil or plant, they help supply nutrients such as nitrogen and phosphorus, or make nutrients already in the soil easier for the crop to take up."),
          ("Which biofertiliser types do you make?", "Azotobacter, Azospirillum, Acetobacter, Rhizobium, phosphate solubilising bacteria, potash mobilising bacteria, zinc solubilising bacteria, phosphate solubilising fungi, mycorrhizal biofertilisers, and carrier-based and liquid consortia."),
          ("Are biofertilisers approved?", "The Directorate of Agriculture, Government of Gujarat has issued us a No Objection Certificate for 11 biofertiliser types under Schedule III of the Fertiliser Control Order."),
          ("Do you supply liquid and carrier-based forms?", "Yes, liquid and carrier-based consortia are both on our list. Tell us the form and pack you need."),
          ("Is it biofertilizer or biofertiliser?", "They are the same word in American and British spelling. Both mean a product that contains living microorganisms to help crops take up nutrients."),
          ("What should I check before choosing a biofertilizer manufacturer in India?", "Check that the company makes the product itself, that the product type is covered by approval under Schedule III of the Fertiliser Control Order, that the form and shelf life are printed on the pack, and that the terms are clear: pack sizes, minimum order and dispatch time. Ours are no minimum order quantity, dispatch in about one week and free samples, with freight, duty and other charges paid by the buyer."),
          ("Do you offer private label for bio fertilizer companies and brand owners?", "Yes. We manufacture any of the 11 types under your brand, in liquid and carrier-based packs, with no minimum order quantity.")]
bf = f'''{page_hero("Biofertiliser manufacturer in India: 11 approved types", "Nitrogen fixers, phosphate, potash and zinc solubilisers, mycorrhizae and consortia, in liquid and carrier-based forms.", "/biofertilisers-manufacturer-india", "Biofertilisers")}
<section class="section"><div class="wrap">
<div class="answer">Gujarat Bio Organics makes 11 types of biofertiliser at Shihor, Bhavnagar, covered by our Gujarat Directorate of Agriculture NOC under Schedule III. Available in bulk, private label or under our brand. Biofertilizer and biofertiliser are two spellings of the same word.</div>
<ul class="bio">{"".join(f'<li><a href="{BIO_INFO[b][0]}">{b}</a></li>' for b in BIOS)}</ul>
<div class="btn-row"><a class="btn btn-wa" href="{wa("Hello Gujarat Bio Organics, please quote these biofertilisers: ")}">{WA_SVG}Ask for a quote</a><a class="btn btn-dark" href="/private-label-oem">Make it under my brand</a></div>
</div></section>
<section class="section tint"><div class="wrap"><div class="prose"><h2>A bio fertilizer manufacturing company, not a trader</h2>
<p>If you are comparing bio fertilizer companies in India, ask each one where the product is made. We manufacture all 11 types ourselves at our plant in Shihor, Bhavnagar, Gujarat, in liquid and carrier-based forms, and we supply them in bulk, under your private label or under our Immunity brand.</p>
<ul class="checks"><li>Own plant and in-house R&amp;D, one manufacturer from formulation to pack</li><li>Gujarat Directorate of Agriculture NOC for 11 types under Schedule III</li><li>No minimum order quantity and dispatch in about one week</li><li>Free samples, with freight, duty and other charges paid by the buyer</li></ul>
<p><a href="/bulk-pricing-and-quotes">How bulk pricing works</a> &middot; <a href="/private-label-oem">Private label and OEM</a> &middot; <a href="/export">Export</a></p></div></div></section>
<section class="section"><div class="wrap"><div class="sec-head"><h2>Sample presentation</h2><p>Illustrative renderings of selected biofertiliser samples.</p></div>
<div class="gal three">{"".join(img(n, c, caption=c + ". Illustrative.") for n, c in bf_img)}</div></div></section>
<section class="section"><div class="wrap"><div class="sec-head"><h2>Questions about biofertilisers</h2></div>{faq_html(bf_faq)}</div></section>{cta()}'''
render("/biofertilisers-manufacturer-india", "Biofertilizer Manufacturer India: 11 Types | GBO",
       "Biofertilizer (biofertiliser) manufacturer in Bhavnagar, Gujarat: Azotobacter, Azospirillum, PSB, KMB, ZSB, Rhizobium, mycorrhizae and consortia. 11 types under Gujarat NOC. Bulk and private label.", bf, [faq_ld(bf_faq)], "Biofertilisers")
PAGES.append(("/biofertilisers-manufacturer-india", "0.8"))

# ------------------------------------------------------------------ PRIVATE LABEL
pl_faq = [("Is there a minimum order quantity?", "No. Tell us your requirement and we will quote."),
          ("Can you make a custom formulation?", "Yes. Share the target crops and composition."),
          ("Can you pack under my brand?", "Yes, with your label and pack design."),
          ("Do you give samples?", "Yes, samples are free. Freight or courier, customs duty and other charges are borne by the buyer."),
          ("How long does an order take?", "Typically one week."),
          ("Can I export under my brand?", "Yes. See our Export page."),
          ("Can the product be tested by a third party?", "Yes, third-party testing and sampling are available.")]
pl_form = form("Tell us about your brand", "private label enquiry",
    [field("name", "Your name", req=True), field("company", "Company or brand"), field("place", "Country or state"),
     field("interest", "Product interest", "select", opts=["Humic and fulvic", "Seaweed", "Protein hydrolysate and amino", "Blend", "Biofertiliser", "Custom formulation"]),
     field("volume", "Expected volume"), field("phone", "Phone or WhatsApp", "tel", req=True), field("email", "Email (for our reply)", "email")])
pl = f'''{page_hero("Private label and OEM biostimulant manufacturing in India", "You have the market. We have the plant. We supply biostimulants and organic inputs under your brand name, label and packaging.", "/private-label-oem", "Private label and OEM")}
<section class="section"><div class="wrap"><div class="cols"><div>
<div class="answer">Gujarat Bio Organics offers private-label and contract manufacturing of biostimulants and biofertilisers from its own plant in Bhavnagar, Gujarat. No minimum order. Free sample. Typical dispatch in one week.</div>
<h2>What we make for your brand</h2>
<ul class="checks"><li>Humic and fulvic products: liquid, powder, granular</li><li>Seaweed extracts: Ascophyllum nodosum, Kappaphycus alvarezii, Sargassum</li><li>Protein hydrolysates and amino acid products, plant and animal source</li><li>Blends: humic + seaweed, seaweed + botanical, humic + amino acid + vitamins</li><li>Biofertilisers: Azotobacter, Azospirillum, PSB, KMB, Rhizobium, mycorrhizal, consortia</li><li>Custom formulations on request</li></ul>
<h2>Packing options</h2>
<p><strong>Liquids:</strong> 1000 L IBC, 220 L drum, and 50, 35, 25, 20, 10, 5 and 1 L, 500 mL and 250 mL packs.<br><strong>Solids:</strong> 1, 2, 4, 5, 8, 10 and 20 kg bags or buckets, 25 and 50 kg bags, 600 kg and 1000 kg jumbo bags.</p>
<h2>Why brands choose us</h2>
<ul class="checks"><li>No minimum order: test a market before you scale</li><li>100 KL liquid and 2,500 tonnes solid capacity every month</li><li>One manufacturer from formulation to packing</li><li>Third-party testing and sampling on request</li><li>Gujarat Directorate of Agriculture NOC for our biostimulant grades</li><li>Registered company since 2009 (CIN {CIN})</li></ul>
</div><div>{pl_form}</div></div></div></section>
<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Your brand on the pack</h2><p>Illustrative mockups of how a private-label line can look in 1 L and 5 L packs. Your name, your design.</p></div>
<div class="gal three">{img("private-label-premium-enriched","Seaweed and humic liquid in 1 litre and 5 litre private label packs",caption="Seaweed + humic + amino + vitamins, 1 L and 5 L")}{img("private-label-b-grade","Private label B grade seaweed blend in 1 litre and 5 litre packs",caption="B grade blend, 1 L and 5 L")}{img("private-label-a-grade","Private label A grade seaweed blend in 1 litre and 5 litre packs",caption="A grade blend, 1 L and 5 L")}{img("private-label-humates-soil","Humates 12.5% liquid soil grade private label packs",caption="Humates 12.5% liquid, soil grade")}{img("private-label-humate-fulvate-spray","Humate and fulvate liquid spray grade private label packs",caption="Humate and fulvates, spray grade")}{img("private-label-humic-fulvic-regular","Humic and fulvic acid 25.05% liquid private label packs",caption="Humic and fulvic acid 25.05%")}</div></div></section>
<section class="section dark"><div class="wrap"><div class="sec-head"><h2>How it works</h2></div><div class="steps">
<div class="step"><h3>Brief</h3><p>Tell us your crops, market and product idea, or pick an existing grade.</p></div>
<div class="step"><h3>Sample</h3><p>We recommend a grade or formulate to your brief and send a free sample.</p></div>
<div class="step"><h3>Approve</h3><p>You approve the sample, your label and your pack design.</p></div>
<div class="step"><h3>Dispatch</h3><p>We manufacture, pack under your brand and ship, typically within one week.</p></div></div></div></section>
<section class="section"><div class="wrap"><div class="sec-head"><h2>Private label questions</h2></div>{faq_html(pl_faq)}</div></section>{cta("Ready to launch your brand?", "Send your brief. We reply with a quote and a free sample.", "Hello Gujarat Bio Organics, I want to launch my own brand.")}'''
render("/private-label-oem", "Private Label Biostimulant Manufacturer India | OEM | GBO",
       "Launch your own biostimulant or organic fertilizer brand. Gujarat Bio Organics offers contract manufacturing, custom formulation and your-brand packing. No MOQ.",
       pl, [faq_ld(pl_faq)], "Private label and OEM")
PAGES.append(("/private-label-oem", "0.9"))

# ------------------------------------------------------------------ EXPORT
ex_faq = [("Do you accept small trial orders?", "Yes. There is no minimum order quantity."), ("Can you export under my brand?", "Yes. See private label and OEM."),
          ("Which Incoterms do you offer?", "FOB and CIF."), ("Which ports do you ship from?", "Pipavav, Kandla, Dahej, Mundra, JNPT and all Indian ports."),
          ("Do you send samples?", "Yes, free. Courier, customs duty and other charges are paid by the buyer."), ("Can a third party test the product?", "Yes, third-party testing and sampling are available.")]
ex_form = form("Request an export quote", "export enquiry",
    [field("name", "Your name", req=True), field("company", "Company"), field("country", "Country", req=True),
     field("product", "Product or grade"), field("qty", "Quantity"), field("brand", "Own brand?", "select", opts=["Yes, under my brand", "No, under Gujarat Bio brand"]),
     field("phone", "Phone or WhatsApp", "tel", req=True), field("email", "Email (for our reply)", "email")])
ex = f'''{page_hero("Export biostimulants and organic fertilizers from India", "We supply importers, distributors and brand owners with biostimulants and organic inputs manufactured in Bhavnagar, Gujarat.", "/export", "Export")}
<section class="section"><div class="wrap"><div class="cols"><div>
<div class="answer">Gujarat Bio Organics exports humic acid, seaweed extract, amino acid, protein hydrolysate and biofertiliser products from Gujarat, India. FOB or CIF from Pipavav, Kandla, Dahej, Mundra and JNPT. No minimum order. Free samples.</div>
<h2>Where we supply</h2><ul class="regions" style="margin-bottom:2rem"><li>GCC countries</li><li>Africa</li><li>Russian Federation</li><li>Europe</li><li>North America</li><li>South America</li></ul>
<h2>Export terms</h2>
<dl class="facts"><div><dt>Incoterms</dt><dd>FOB or CIF</dd></div><div><dt>Ports</dt><dd>Pipavav, Kandla, Dahej, Mundra, JNPT and all Indian ports</dd></div><div><dt>Minimum order</dt><dd>None</dd></div><div><dt>Lead time</dt><dd>About one week</dd></div><div><dt>Capacity</dt><dd>100 KL liquid and 2,500 tonnes solid per month</dd></div><div><dt>Samples</dt><dd>Free. Freight or courier, customs duty and other charges are borne by the buyer.</dd></div><div><dt>Quality checks</dt><dd>Third-party testing and sampling available</dd></div></dl>
<h2 style="margin-top:2.4rem">Products for export</h2>
<ul class="checks"><li>Humic and fulvic acid: liquid, powder, granular, and potassium humate</li><li>Seaweed extracts: Ascophyllum, Kappaphycus, Sargassum</li><li>Protein hydrolysate and amino acid</li><li>Spirulina and botanical extracts</li><li>Blended biostimulants and biofertilisers</li></ul>
<h2>Supply options</h2>
<ul class="checks"><li>Bulk liquids in 1000 L IBC or 220 L drums</li><li>Bulk solids in 600 kg or 1000 kg jumbo bags and 25 or 50 kg bags</li><li>Retail packs from 250 mL to 50 L and 1 to 20 kg under our Immunity brand</li><li>Private label under your brand</li></ul>
<p>Importers may ask for an NDA reference. We can arrange this on request.</p>
</div><div>{ex_form}</div></div></div></section>
<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Questions from importers</h2></div>{faq_html(ex_faq)}</div></section>{cta("Request an export quote", "Share product, quantity and destination port.", "Hello Gujarat Bio Organics, I need an export quote.")}'''
render("/export", "Biostimulant & Organic Fertilizer Exporter from India | GBO",
       "Export humic acid, seaweed extract, amino acid and biofertiliser products from Gujarat, India. FOB/CIF from Mundra, Kandla, Pipavav, Dahej, JNPT. Free samples.",
       ex, [faq_ld(ex_faq)], "Export")
PAGES.append(("/export", "0.9"))

# ------------------------------------------------------------------ BULK
bk_form = form("Get bulk pricing", "bulk pricing enquiry",
    [field("name", "Your name", req=True), field("company", "Company"), field("grades", "Grades needed", "textarea"),
     field("qty", "Quantity per order"), field("dest", "Destination"), field("phone", "Phone or WhatsApp", "tel", req=True), field("email", "Email (for our reply)", "email")])
bk = f'''{page_hero("Bulk biostimulant supply for distributors and formulators", "Buy direct from the manufacturer. Bulk and wholesale volumes from our own plant, with no minimum order.", "/bulk-supply", "Bulk supply")}
<section class="section"><div class="wrap"><div class="cols"><div>
<div class="answer">Gujarat Bio Organics supplies bulk and wholesale humic acid, seaweed extract, amino acid and biofertilisers from Bhavnagar, India: 100 KL liquid and 2,500 tonnes solid per month, no minimum order.</div>
<h2>Buying terms</h2>
<dl class="facts"><div><dt>Minimum order</dt><dd>None</dd></div><div><dt>Liquids</dt><dd>1000 L IBC, 220 L drums, and smaller packs down to 250 mL</dd></div><div><dt>Solids</dt><dd>600 or 1000 kg jumbo bags, 25 or 50 kg bags, 1 to 20 kg bags or buckets</dd></div><div><dt>Dispatch</dt><dd>About one week</dd></div><div><dt>Samples</dt><dd>Free</dd></div><div><dt>Testing</dt><dd>Third-party testing available</dd></div><div><dt>Export</dt><dd>FOB or CIF</dd></div></dl>
<h2 style="margin-top:2.4rem">Pick your grades</h2><p>Use the grade list to tick what you need, then send it to us for pricing.</p>
<div class="btn-row"><a class="btn btn-dark" href="/biostimulants-manufacturer-india">Open the grade list</a><a class="btn btn-ghost" style="color:var(--ink)" href="/biofertilisers-manufacturer-india">Biofertilisers</a></div>
</div><div>{bk_form}</div></div></div></section>
<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Solid products</h2><p>Granular and powder products for bulk buyers. Illustrative sample images.</p></div>
<div class="gal">{img("humic-acid-51-granular","Humic acid 51% granules",caption="Humic acid 51% granular")}{img("humic-acid-1-5-granules","Humic acid 1.5% granules",caption="Humic acid 1.5% granules")}{img("humic-seaweed-granules","Humic acid and seaweed extract granules",caption="Humic acid + seaweed granules")}{img("granules-pile","Pile of black humic granules",caption="Granules, loose")}</div></div></section>{cta("Get bulk pricing", "Send grades, quantity and destination.", "Hello Gujarat Bio Organics, I need bulk pricing.")}'''
render("/bulk-supply", "Bulk Biostimulant & Humic Acid Supplier India | Wholesale | GBO",
       "Bulk and wholesale humic acid, seaweed extract, amino acid and biofertilisers from our Gujarat plant. No MOQ. 100 KL liquid and 2,500 t solid monthly capacity.",
       bk, None, "Bulk supply")
PAGES.append(("/bulk-supply", "0.9"))

# ------------------------------------------------------------------ DISTRIBUTOR
ds_faq = [("How do margins work?", "We give you bulk prices. You set your own selling margin."),
          ("Which territories are open?", "Territories where Gujarat Bio Organics does not yet have a presence. Tell us your district and state."),
          ("Can I carry a private-label line?", "Yes. We can make a line under your own brand for your territory.")]
ds_form = form("Apply for your territory", "distributor application",
    [field("name", "Your name", req=True), field("shop", "Shop or company"), field("place", "Town, district and state", req=True),
     field("crops", "Main crops in your area"), field("years", "Years in agri trade"), field("phone", "Phone or WhatsApp", "tel", req=True), field("email", "Email (for our reply)", "email")],
    note="We reply on WhatsApp.")
ds = f'''{page_hero("Become a GBO distributor in your territory", "We are opening territories where Gujarat Bio Organics does not yet have a presence.", "/become-a-distributor", "Become a distributor")}
<section class="section"><div class="wrap"><div class="cols"><div>
<div class="answer">If you run an agri-input shop, a distribution business or a farmer network, you can carry the Immunity range or a private-label line made for you by us. We provide bulk prices and you set your own margin.</div>
<h2>What you get</h2>
<ul class="checks"><li>Crop-specific products for your region's main crops</li><li>Product handbills, application guides and dosage charts</li><li>Marketing material and farmer videos</li><li>Direct support from the manufacturer</li><li>Bulk prices from us. You set your own selling margin.</li></ul>
<h2>Who should apply</h2><p>Agri-input retailers, existing distributors, FPOs, farmer groups, and dealers adding a biostimulant line.</p>
<p>Growers in areas we do not yet serve can also message us on WhatsApp to find the nearest supply point.</p>
<div class="btn-row"><a class="btn btn-wa" href="{wa("Hello Gujarat Bio Organics, I want to become a distributor.")}">{WA_SVG}WhatsApp {PHONE}</a></div>
</div><div>{ds_form}</div></div></div></section>
<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Distributor questions</h2></div>{faq_html(ds_faq)}</div></section>'''
render("/become-a-distributor", "Become a GBO Distributor | Organic Fertilizer Dealership India",
       "Distributor and dealer opportunity for Immunity biostimulants and organic fertilizers in territories without a GBO network. Apply online or on WhatsApp.",
       ds, [faq_ld(ds_faq)], "Become a distributor")
PAGES.append(("/become-a-distributor", "0.8"))

# ------------------------------------------------------------------ FIELD SOLUTIONS
PROBS = [
 ("Hard, tired soil that holds little water or nutrient", "Repeated chemical use and low organic matter can leave soil compact, with poor structure and weak nutrient holding.", "Humic and fulvic products are used to support soil structure, nutrient holding and root development.", "Humic acid granular (basal), humate and fulvate liquids (drench or fertigation)", "Soil conditioning"),
 ("Heat, drought and salt stress", "Crops stall in hot spells, dry spells or on saline patches.", "Seaweed extracts are used to support crop tolerance to abiotic stress.", "Ascophyllum nodosum, Kappaphycus alvarezii and Sargassum grades", "Stress tolerance"),
 ("Poor flowering and fruit set", "Flowers drop or set is uneven in fruit, vegetable and cotton crops.", "Seaweed and amino acid products are used around flowering to support set and development.", "Seaweed + amino acid blends, seaweed + humic blends", "Flowering and fruit set"),
 ("Slow recovery after stress or transplanting", "Crops look pale and slow after cold, pest damage, hail or transplanting.", "Amino acids and protein hydrolysates are used to support recovery and early growth.", "Amino acid and plant or animal source protein hydrolysate grades", "Recovery"),
 ("Fertiliser that is not taken up well", "Applied nutrients are lost or locked in the soil, so the crop uses less than the bag promises.", "Biofertilisers help supply or release nitrogen, phosphorus, potash and zinc, and humic products help hold nutrients near roots.", "Azotobacter, Azospirillum, PSB, KMB, ZSB, consortia, with humic acid", "Nutrient uptake"),
 ("Weak root systems in the first weeks", "Poor early rooting leads to uneven stand and slow canopy.", "Humic and fulvic products and rhizosphere biofertilisers are used at sowing or transplanting to support root growth.", "Humic liquids, Azospirillum, mycorrhizal biofertilisers", "Root growth"),
]
probs_html = '<div class="probs">' + "".join(
    f'<div class="prob"><h3>{t}</h3><p>{p}</p><dl><dt>What it is used for</dt><dd>{s}</dd><dt>Grades to ask for</dt><dd>{g}</dd></dl></div>' for t, p, s, g, _ in PROBS) + '</div>'
fs_faq = [("Do your products guarantee a yield increase?", "No. Results depend on crop, soil, weather and how the product is used. We describe what each product family is used for and recommend a small trial before wider use."),
          ("How do I choose a grade for my crop?", "Share your crop, region, soil type and the problem you see. We recommend a grade, a dose and a timing, and can send a free sample for a trial."),
          ("Can distributors and brands use this information?", "Yes. We can help you build crop-wise recommendations for your own brand and territory.")]
fs = f'''{page_hero("Field solutions: start from the problem", "Twenty years of R&amp;D, product innovation and on-field work, turned into a plain list of what growers ask us and which grades we recommend.", "/field-solutions", "Field solutions")}
<section class="section"><div class="wrap">
<div class="answer">Biostimulants and biofertilisers are tools for specific problems: soil structure, stress, flowering, recovery and nutrient uptake. Match the problem to the product family, run a small trial, and scale only what works on your farm.</div>
<h2>Common problems and what growers use</h2>{probs_html}
<p class="note-box">Results vary with crop, soil, weather and practice. Run a small trial first. These notes describe common uses and are not a guarantee of yield.</p>
<div class="btn-row"><a class="btn btn-wa" href="{wa("Hello Gujarat Bio Organics, my crop is ___ in ___ and the problem is ___. Please suggest a product.")}">{WA_SVG}Describe your problem on WhatsApp</a><a class="btn btn-dark" href="/biostimulants-manufacturer-india">See all grades</a></div>
</div></section>
<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Questions from growers and buyers</h2></div>{faq_html(fs_faq)}</div></section>{cta("Tell us your crop and your problem", "We recommend a grade and send a free sample for a trial.", "Hello Gujarat Bio Organics, please recommend a product for my crop.")}'''
render("/field-solutions", "Biostimulant Solutions for Crop Problems | Gujarat Bio Organics",
       "Soil, stress, flowering, recovery and nutrient uptake: which biostimulant or biofertiliser grade to ask for, from 20 years of R&D and field work.",
       fs, [faq_ld(fs_faq)], "Field solutions")
PAGES.append(("/field-solutions", "0.8"))

# ------------------------------------------------------------------ QUALITY
q_faq = [("Do you have regulatory approval?", "The Directorate of Agriculture, Government of Gujarat has issued No Objection Certificates for 36 biostimulant grades (Schedule VI) and 11 biofertiliser types (Schedule III) under the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985. Copies are available on request."),
         ("Can I get a third-party test?", "Yes. Third-party testing and sampling are available."),
         ("Can I get specification sheets?", "Yes, on request.")]
qc = f'''{page_hero("Quality, compliance and company details", "Who we are, where we make it, and what we are approved to sell.", "/quality-compliance", "Quality and compliance")}
<section class="section"><div class="wrap"><div class="proof"><div>
<h2>Company details</h2>
<dl class="facts"><div><dt>Legal name</dt><dd>Gujarat Bio Organics Private Limited</dd></div><div><dt>CIN</dt><dd>{CIN}</dd></div><div><dt>GSTIN</dt><dd>{GST}</dd></div><div><dt>Incorporated</dt><dd>25 November 2009</dd></div><div><dt>Factory</dt><dd>{FACTORY}</dd></div><div><dt>Registered office</dt><dd>{REGOFF}</dd></div><div><dt>Email</dt><dd>{MAIL}</dd></div><div><dt>Phone</dt><dd>{PHONE}</dd></div></dl></div>
<div><h2>Regulatory</h2><p>The Directorate of Agriculture, Government of Gujarat has issued No Objection Certificates to Gujarat Bio Organics for the sale of:</p>
<ul class="checks"><li>Biostimulants specified in Schedule VI of the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985: <a href="/biostimulants-manufacturer-india">36 grades</a></li><li>Biofertilisers specified in Schedule III: <a href="/biofertilisers-manufacturer-india">11 types</a></li></ul>
<h2>Quality</h2><p>Third-party testing and sampling are available. Product specification sheets are available on request.</p>
<h2>On request</h2><ul class="checks"><li>NOC grade list</li><li>Certificate of incorporation</li><li>GST registration</li><li>Specification sheets</li></ul>
<div class="btn-row"><a class="btn btn-wa" href="{wa("Hello Gujarat Bio Organics, please send your NOC copies and company documents.")}">{WA_SVG}Request documents</a></div></div></div></div></section>
<section class="section tint"><div class="wrap"><div class="sec-head"><h2>Compliance questions</h2></div>{faq_html(q_faq)}</div></section>{cta()}'''
render("/quality-compliance", "Quality, Compliance & Company Details | Gujarat Bio Organics",
       "Company registration, factory address, Directorate of Agriculture NOC and approved product grades of Gujarat Bio Organics Pvt. Ltd., Shihor, Bhavnagar.",
       qc, [faq_ld(q_faq)], "Quality and compliance")
PAGES.append(("/quality-compliance", "0.7"))

# ------------------------------------------------------------------ ABOUT
ab = f'''{page_hero("About Gujarat Bio Organics", "A Bhavnagar manufacturer of biostimulants and biofertilisers, built on R&amp;D and field work.", "/about", "About")}
<section class="section"><div class="wrap"><div class="cols"><div>
<div class="answer">Gujarat Bio Organics Pvt. Ltd. manufactures biostimulants and biofertilisers at Shihor, Bhavnagar, Gujarat. We combine 20 years of R&amp;D, product innovation and hard on-field work with growers.</div>
<p>This is our open B2B website. No login or dealer approval is needed. Request a quote or a free sample directly, by form, WhatsApp or email.</p>
<p>We make humic and fulvic acid, seaweed extract, protein hydrolysate, amino acid and biofertiliser products, and supply them three ways: under our Immunity brand, under your private label, or in bulk.</p>
<p>Two decades of field work with growers across crops and regions sit behind every product. <a href="/impact">See the field record and hear growers</a>.</p>
<p>Our plant has capacity for 100 KL of liquid and 2,500 tonnes of solid products every month. We ship worldwide, with no minimum order and free samples.</p>
<h2>A fertilizer manufacturing company in India, not a trader</h2>
<p>Gujarat Bio Organics is a fertilizer manufacturing company with its own plant at {FACTORY}. We formulate, manufacture and pack in one place, and our biostimulant and biofertiliser grades are covered by a No Objection Certificate from the Directorate of Agriculture, Government of Gujarat. <a href="/manufacturing-facility">See the manufacturing facility</a> and <a href="/quality-compliance">our compliance details</a>.</p>
<h2>How we work</h2>
<ul class="checks"><li>Start from the farmer's problem, not the product</li><li>Trial first, scale what works</li><li>One manufacturer from formulation to packing</li><li>Plain terms: no MOQ, free samples, FOB or CIF</li></ul>
<div class="btn-row"><a class="btn btn-primary" href="/contact">Contact us</a><a class="btn btn-dark" href="/quality-compliance">Company and compliance details</a></div>
</div><div>{img("private-label-premium-enriched","Seaweed and humic liquid products in 1 litre and 5 litre packs",caption="Illustrative sample image")}</div></div></div></section>'''
render("/about", "Fertilizer Manufacturing Company in India | About GBO",
       "Gujarat Bio Organics is a fertilizer manufacturing company in Shihor, Bhavnagar, Gujarat. Biostimulants and biofertilisers, 20 years of R&D and field work. Own brand, private label and bulk.", ab, None, "About")
PAGES.append(("/about", "0.5"))

# ------------------------------------------------------------------ CONTACT
ct_form = form("Send an enquiry", "enquiry",
    [field("name", "Your name", req=True), field("company", "Company"), field("place", "Country or state"),
     field("type", "I am a", "select", opts=["Importer or exporter", "Brand owner (private label)", "Distributor or dealer", "Farmer or grower", "Other"]),
     field("msg", "What do you need?", "textarea"), field("phone", "Phone or WhatsApp", "tel", req=True), field("email", "Email (for our reply)", "email")])
ct = f'''{page_hero("Contact Gujarat Bio Organics", "WhatsApp is the fastest way to reach us. Or send the form and we reply by email or WhatsApp.", "/contact", "Contact")}
<section class="section"><div class="wrap"><div class="cols"><div>
<h2>Contact details</h2><dl class="facts"><div><dt>WhatsApp</dt><dd><a href="https://wa.me/{WA}">{PHONE}</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div><div><dt>Factory</dt><dd>{FACTORY}</dd></div><div><dt>Registered office</dt><dd>{REGOFF}</dd></div><div><dt>Facebook</dt><dd><a href="{FB}" rel="noopener">facebook.com/gujaratbio</a></dd></div><div><dt>YouTube</dt><dd><a href="{YT}" rel="noopener">youtube.com/@Gujaratbio</a></dd></div></dl>
<div class="btn-row"><a class="btn btn-wa" href="https://wa.me/{WA}">{WA_SVG}Chat on WhatsApp</a><a class="btn btn-dark" href="https://www.google.com/maps/search/?api=1&amp;query=Gujarat+Bio+Organics+Shihor+Bhavnagar" rel="noopener">Open map</a></div>
</div><div>{ct_form}</div></div></div></section>'''
ct_ld = [{"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact", "mainEntity": {"@id": SITE + "/#org"}}]
render("/contact", "Contact Gujarat Bio Organics | Quote, Sample, Distributor Enquiry",
       "Contact Gujarat Bio Organics in Shihor, Bhavnagar. WhatsApp +91 9978791167, email sales@gujaratbio.com. Quotes, free samples and distributor enquiries.", ct, ct_ld, "Contact")
PAGES.append(("/contact", "0.7"))

# ------------------------------------------------------------------ 404
nf = f'''{page_hero("Page not found", "That page has moved or never existed. Try one of these.", "/404", "Not found")}
<section class="section"><div class="wrap"><ul class="checks"><li><a href="/products">Products</a></li><li><a href="/private-label-oem">Private label and OEM</a></li><li><a href="/export">Export</a></li><li><a href="/bulk-supply">Bulk supply</a></li><li><a href="/contact">Contact</a></li></ul></div></section>'''
render("/404", "Page not found | Gujarat Bio Organics", "Page not found.", nf, None, None, noindex=True)
os.replace(os.path.join(ROOT, "404", "index.html"), os.path.join(ROOT, "404.html"))
os.rmdir(os.path.join(ROOT, "404"))

# ------------------------------------------------------------------ extended content
for _f in ("ext_10_categories.py", "ext_20_grade_pages.py", "ext_30_crops.py", "ext_40_company.py", "ext_42_difference.py", "ext_45_impact.py", "ext_46_privacy.py", "ext_47_pricing.py", "ext_50_resources.py", "ext_60_glossary_faq.py"):
    exec(open(os.path.join(ROOT, _f), encoding="utf-8").read())
json.dump(KWMAP, open(os.path.join(ROOT, ".keyword-map.json"), "w"), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ SEO files
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'<url><loc>{SITE}{p if p != "/" else "/"}</loc><priority>{pr}</priority></url>\n' for p, pr in PAGES) + '</urlset>\n'
open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: Googlebot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: Google-Extended\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: GPTBot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: OAI-SearchBot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: ChatGPT-User\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: ClaudeBot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: Claude-User\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: Claude-SearchBot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: PerplexityBot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: Perplexity-User\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: Applebot-Extended\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: CCBot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: Bingbot\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nUser-agent: *\nAllow: /\nDisallow: /team/\nDisallow: /chat-kb.txt\n\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(ROOT, "llms.txt"), "w").write(f"""# Gujarat Bio Organics Pvt. Ltd.
> Manufacturer of organic fertilizers, biostimulants (humic acid, seaweed extract, amino acids), biofertilisers and specialty fertilizers (micronutrients, water-soluble special grades, slow-release, custom blends, zyme granules) in Shihor, Bhavnagar, Gujarat, India, with in-house R&D. Supplies under its Immunity brand, under buyers' private labels, and in bulk. Exports worldwide.

## Key facts
- About this site: b2b.gujaratbio.com is the open, public B2B website of Gujarat Bio Organics. No login or dealer approval is needed to browse it: buyers request quotes and free samples directly. It is not a login-restricted dealer portal and has no shopping cart; orders start from a quote request or WhatsApp.
- Legal name: Gujarat Bio Organics Private Limited. CIN {CIN}. GSTIN {GST}. Incorporated 25 Nov 2009.
- Factory: {FACTORY}
- Capacity: 100 KL liquid and 2,500 tonnes solid per month. No minimum order quantity. Lead time about one week.
- Approvals: Gujarat Directorate of Agriculture NOC for 36 biostimulant grades (Schedule VI) and 11 biofertiliser types (Schedule III), Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985.
- Export: FOB or CIF from Pipavav, Kandla, Dahej, Mundra, JNPT. Markets: GCC, Africa, Russian Federation, Europe, North America, South America. Free samples; buyer pays freight, duty and other charges.
- Contact: WhatsApp {PHONE}, {MAIL}

## Products
{chr(10).join(f"- [{t}]({SITE}{u}): {d}" for u, t, d in CAT_HUB)}

## Approved grades (one page each)
{chr(10).join(f"- {SITE}{grade_path(n, f)}" for g, n, f in GRADES)}
{chr(10).join(f"- {SITE}{BIO_INFO[b][0]}" for b in BIOS)}

## Crops
{chr(10).join(f"- {SITE}/crops/{c['slug']}: {c['name']} programme ({c['special']})" for c in CROPS)}

## Company
- {SITE}/about
- {SITE}/why-gujarat-bio
- {SITE}/impact
- {SITE}/research-development
- {SITE}/manufacturing-facility
- {SITE}/quality-compliance
- {SITE}/private-label-oem
- {SITE}/bulk-supply
- {SITE}/bulk-pricing-and-quotes
- {SITE}/export
- {SITE}/become-a-distributor
- {SITE}/contact

## Guides
- [FCO Schedule VI biostimulants]({SITE}/fco-schedule-vi-biostimulants): how India regulates biostimulants
{chr(10).join(f"- [{t}]({SITE}{u}): {d}" for u, t, d in ARTICLES)}
- {SITE}/glossary
- {SITE}/faq
""")

# ------------------------------------------------------------------ CHATBOT KNOWLEDGE BASE
_kb = f"""COMPANY
Gujarat Bio Organics Pvt. Ltd. (GBO), Bhavnagar, Gujarat, India. Brand: Immunity. About 20 years of in-house R&D and field work with growers.
Factory: {FACTORY}. Registered office: {REGOFF}.
Contact: WhatsApp {PHONE} (https://wa.me/{WA}), email {MAIL}. Facebook {FB}. YouTube {YT}.
Capacity: 100 KL liquid and 2,500 tonnes solid/granular per month. No minimum order quantity (trial quantities quoted). Lead time about one week from confirmed order.
Samples: free; buyer pays freight or courier, customs duty and other charges.
Ways to buy: (1) Immunity brand products, (2) private label / OEM under the buyer's brand (we formulate, make and pack), (3) bulk supply (IBC, drums, bags). Export, FOB or CIF. Ports: Pipavav, Kandla, Dahej, Mundra, JNPT and all Indian ports. Export regions: GCC, Africa, Russian Federation countries, Europe, North America, South America, and all of India.
Liquid packs: {PACKS_L}. Solid packs: {PACKS_S}.
Third-party testing and sampling available on request. Documents on request: specification sheet, NOC copy, certificate of incorporation, GST registration, third-party test report. Plant visits can be arranged in advance.
Approvals: Gujarat Directorate of Agriculture has issued No Objection Certificates for 36 biostimulant grades (FCO Schedule VI) and 11 biofertiliser types (Schedule III) under the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985. Copies on request.
Distributors: GBO gives bulk prices, distributors set their own margins.
Website: b2b.gujaratbio.com is the open public B2B site; no login or dealer approval needed; no shopping cart, orders start from a quote or WhatsApp.\nPricing: no public price list. Price depends on grade, concentration, form, pack size, quantity and, for export, Incoterm and destination port. A quote usually follows within one working day.
DIFFERENCE (page: {SITE}/why-gujarat-bio): Humic acid: raw material chosen after about 20 years of field comparison; extraction avoids very high pH and very high temperatures because our R&D found beneficial humic substances are fragile against them. Seaweed: only a few of thousands of species suit agriculture; cultivation, harvest timing, post-harvest handling, storage and extraction protocols protect the extract; species used: Ascophyllum nodosum, Kappaphycus alvarezii, Sargassum, Spirulina. Amino acids: source, hydrolysis, preservation, formulation and QC; plant and animal source grades. We do not disclose exact raw materials or process settings; we share specification sheets, third-party test reports, free samples, plant visits. Do not name or accuse other companies or countries.
Vision: make food cultivation hazardous-chemical-free and sustainable for generations; the field-proven formula is open to importers, brand owners, distributors and growers worldwide.

PRODUCT CATEGORIES (page URLs)
{chr(10).join(f"- {t}: {SITE}{u} ({d})" for u, t, d in CAT_HUB)}

BIOSTIMULANT GRADES (36). Format: group | grade | form | page
{chr(10).join(f"- {g} | {n} | {f} | {SITE}{grade_path(n, f)}" for g, n, f in GRADES)}

BIOFERTILISERS (11)
{chr(10).join(f"- {b}: {BIO_INFO[b][2]}. {SITE}{BIO_INFO[b][0]}" for b in BIOS)}

CROP PROGRAMMES
{chr(10).join(f"- {c['name']}: {c['special']}; regions {c.get('regions','')}. {SITE}/crops/{c['slug']}" for c in CROPS)}
Also worked with: citrus, coconut, cotton.

OTHER PAGES
- Private label / OEM {SITE}/private-label-oem ; Bulk supply {SITE}/bulk-supply ; How we quote (no price list, no minimum order) {SITE}/bulk-pricing-and-quotes ; Export {SITE}/export ; Distributor {SITE}/become-a-distributor
- R&D {SITE}/research-development ; Manufacturing {SITE}/manufacturing-facility ; Quality {SITE}/quality-compliance ; Field record and grower videos {SITE}/impact ; Contact {SITE}/contact ; FCO Schedule VI explainer {SITE}/fco-schedule-vi-biostimulants

FAQ
{chr(10).join(f"Q: {q} A: {a}" for q, a in home_faq)}
"""
open(os.path.join(ROOT, "chat-kb.txt"), "w", encoding="utf-8").write(_kb)
print("built", len(PAGES) + 1, "pages")
