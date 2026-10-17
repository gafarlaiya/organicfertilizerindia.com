# Shared helpers for the extended site. Loaded by build.py with exec(), so it sees
# render, esc, img, faq_html, faq_ld, cta, wa, WA_SVG, SITE, PAGES, GRADES, BIOS, etc.
import re as _re

KWMAP = []          # keyword map rows, written to keyword-map.json for the xlsx
TODAY = "2026-10-17"

def kw(path, primary, secondary=(), questions=(), intent="Commercial", audience="B2B buyers"):
    KWMAP.append({"path": path, "primary": primary, "secondary": list(secondary),
                  "questions": list(questions), "intent": intent, "audience": audience})

def slug(s):
    s = s.lower().replace("%", "").replace("+", " plus ").replace("&", " and ")
    s = _re.sub(r"[^a-z0-9.]+", "-", s).replace(".", "-")
    return _re.sub(r"-+", "-", s).strip("-")

PACKS_L = "250 mL, 500 mL, 1 L, 5 L, 10 L, 20 L, 25 L, 35 L, 50 L, 220 L drums and 1000 L IBC"
PACKS_S = "1, 2, 4, 5, 8, 10 and 20 kg bags or buckets, 25 and 50 kg bags, 600 kg and 1000 kg jumbo bags"

def hero(title, lead, trail):
    """trail: list of (name, url); last item is the current page (url may be None)."""
    parts = ['<a href="/">Home</a>'] + [
        (f'<a href="{u}">{esc(n)}</a>' if u and i < len(trail) - 1 else esc(n)) for i, (n, u) in enumerate(trail)]
    return f'''<section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb">{" / ".join(parts)}</nav>
<h1>{title}</h1><p>{lead}</p></div></section>'''

def trail_ld(path, trail):
    items = [("Home", "/")] + [(n, u or path) for n, u in trail]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def page(path, title, desc, body, trail, schemas=None, priority="0.6", og=None):
    ld = [trail_ld(path, trail)] + (schemas or [])
    kwargs = {"og_img": og} if og else {}
    render(path, title, desc, body, ld, None, **kwargs)
    PAGES.append((path, priority))

def sec(inner, title=None, sub=None, cls=""):
    head = ""
    if title:
        head = f'<div class="sec-head"><h2>{title}</h2>' + (f'<p>{sub}</p>' if sub else "") + '</div>'
    return f'<section class="section {cls}"><div class="wrap">{head}{inner}</div></section>'

def answer(t):
    return f'<div class="answer">{t}</div>'

def ul(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def spec(rows):
    return '<dl class="facts spec">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"

def table(head, rows, cls="grades data"):
    th = "".join(f"<th>{h}</th>" for h in head)
    import re as _r
    labels = [_r.sub("<[^>]+>", "", h) for h in head]
    tr = "".join("<tr>" + "".join(f'<td data-label="{esc(labels[i]) if i < len(labels) else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def links(items, title="Related pages"):
    """items: list of (url, label, note)."""
    lis = "".join(f'<li><a href="{u}">{esc(l)}</a>' + (f"<span>{esc(n)}</span>" if n else "") + "</li>" for u, l, n in items)
    return f'<div class="rel"><h2>{title}</h2><ul>{lis}</ul></div>'

def hub(items):
    """items: list of (url, title, line)."""
    return '<div class="hub">' + "".join(
        f'<a class="hub-i" href="{u}"><h3>{esc(t)}</h3><p>{esc(l)}</p></a>' for u, t, l in items) + "</div>"

def buy_block(liquid=True, solid=True):
    rows = [("Minimum order", "None. Trial quantities are quoted too."), ("Lead time", "About one week from confirmed order")]
    if liquid: rows.append(("Liquid packs", PACKS_L))
    if solid: rows.append(("Solid packs", PACKS_S))
    rows += [("Supply options", '<a href="/bulk-supply">Bulk</a>, <a href="/private-label-oem">private label / OEM</a>, <a href="/export">export</a> (FOB or CIF) or our Immunity brand'),
             ("Samples", "Free. Freight or courier, customs duty and other charges are paid by the buyer."),
             ("Documents", "Specification sheet, NOC copy and third-party test report on request")]
    return spec(rows)

PRICE_A = ("Price depends on the grade and concentration, the form (liquid, powder or granule), the pack size, the order quantity "
           "and, for export, the Incoterm and destination port. We do not publish a price list because bulk, private-label and retail "
           "packs are priced differently. Send the grade, quantity and destination and we reply with a quote, usually within one working day.")

def product_ld(path, name, desc, category):
    return {"@context": "https://schema.org", "@type": "Product", "name": name, "description": desc,
            "category": category, "url": SITE + path, "brand": {"@type": "Brand", "name": "Gujarat Bio Organics"},
            "manufacturer": {"@id": SITE + "/#org"}, "countryOfOrigin": "IN"}

def article_ld(path, title, desc):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
            "mainEntityOfPage": SITE + path, "datePublished": TODAY, "dateModified": TODAY,
            "author": {"@type": "Organization", "name": "Gujarat Bio Organics R&D team", "url": SITE + "/research-development"},
            "publisher": {"@type": "Organization", "name": NAME, "@id": SITE + "/#org", "logo": {"@type": "ImageObject", "url": SITE + "/assets/favicon.svg"}}}

def itemlist_ld(name, items):
    return {"@context": "https://schema.org", "@type": "ItemList", "name": name, "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": SITE + u, "name": n} for i, (u, n) in enumerate(items)]}

CLAIM_NOTE = ('<p class="note-box">Results vary with crop, soil, weather and practice. Follow the label, run a small trial first and '
              'scale what works on your farm. Nothing on this page is a guarantee of yield.</p>')

def quote_btns(msg):
    return (f'<div class="btn-row"><a class="btn btn-primary" href="/contact">Request a quote</a>'
            f'<a class="btn btn-wa" href="{wa(msg)}">{WA_SVG}Ask on WhatsApp</a></div>')
