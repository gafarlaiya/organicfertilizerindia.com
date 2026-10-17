# Impact / story page: two decades of field work, real-grower video testimony, and the mission.
import json as _json
_tj = _json.load(open(os.path.join(ROOT, "testimonials.json"), encoding="utf-8"))
VIDS = _tj.get("videos", [])

def _vid_card(v):
    t = esc(v.get("title", "Grower experience"))
    meta = " · ".join(x for x in [v.get("crop", ""), v.get("region", ""), v.get("farmer", "")] if x)
    meta_h = f'<p class="vmeta">{esc(meta)}</p>' if meta else ""
    if v.get("yt"):
        i = esc(v["yt"])
        return (f'<figure class="vid"><button type="button" class="yt" data-id="{i}" aria-label="Play video: {t}">'
                f'<img src="https://i.ytimg.com/vi/{i}/hqdefault.jpg" alt="" width="480" height="360" loading="lazy">'
                f'<span class="play" aria-hidden="true"></span></button><figcaption><b>{t}</b>{meta_h}</figcaption></figure>')
    if v.get("fb"):
        return (f'<figure class="vid fbv"><a class="fb-card" href="{esc(v["fb"])}" rel="noopener"><span class="play" aria-hidden="true"></span>'
                f'<span class="fb-t">Watch on Facebook</span></a><figcaption><b>{t}</b>{meta_h}</figcaption></figure>')
    return ""

_cards = "".join(_vid_card(v) for v in VIDS)
if _cards:
    vid_block = (f'<div class="vid-grid">{_cards}</div>'
                 f'<div class="btn-row"><a class="btn btn-dark" href="{YT}" rel="noopener">More on YouTube</a>'
                 f'<a class="btn btn-ghost" href="{FB}" rel="noopener">More on Facebook</a></div>')
else:
    vid_block = (f'<p>Growers speak about their own farms in our videos, in their own words and languages. '
                 f'Watch them on our channels, then ask us any question you like.</p>'
                 f'<div class="btn-row"><a class="btn btn-dark" href="{YT}" rel="noopener">Watch on YouTube</a>'
                 f'<a class="btn btn-ghost" href="{FB}" rel="noopener">Follow on Facebook</a></div>')

im_faq = [
    ("How long has Gujarat Bio Organics been working with growers?", "For about two decades. Our R&D team has worked with growers on their own farms across crops and regions, and every crop programme we offer comes from that work."),
    ("Which crops have you worked on?", "Sugarcane, potato, mango, apple, banana, citrus, coconut and cotton are the crops we have the most field experience with. See the crop pages for the programmes."),
    ("Can I see growers talking about their results?", "Yes. Growers share their own experience in videos on our YouTube channel and Facebook page. Those are individual experiences. Results vary with crop, soil, weather and practice."),
    ("What does it mean that the formula is open to the world?", "The products and know-how built over 20 years are available to importers, brand owners, distributors and growers in any country, with no minimum order, free samples and your own label if you want it."),
    ("Do your products replace all chemical inputs?", "No claim like that is made. Our aim is to help growers cut dependence on hazardous chemical inputs step by step, with trials first. Follow the label and run a small trial on your own farm."),
]

stories = [
    ("Apple", "Himachal Pradesh and Jammu and Kashmir", "Growers faced plant mortality, low production, poor fruit quality and rising input costs, with no chemical cure on offer. Thousands of apple growers have since used our programme.", "/crops/apple"),
    ("Potato", "Punjab and Haryana", "Declining yields, heavy fertiliser requirements, fewer and smaller tubers and weak quality. Thousands of potato growers have used our programme.", "/crops/potato"),
    ("Sugarcane", "South Gujarat", "Land under cane for about five decades, tired soil, rising chemical use and no break-even. Growers who adopted the programme told us it brought them back to break-even.", "/crops/sugarcane"),
    ("Mango", "Across India", "Tree mortality, poor growth, alternate bearing, fruit drop, small fruit and poor quality. Several thousand mango growers have used our programme.", "/crops/mango"),
    ("Banana", "Central Gujarat", "Sigatoka and Fusarium disease pressure, plant losses and weak bunches. Growers reported near-zero mortality and heavy, export-quality bunches.", "/crops/banana"),
    ("Citrus and coconut", "Multiple regions", "Thousands of citrus and coconut growers have used our products. Hear a coconut grower in his own words in our videos.", "/crops"),
]

body = hero("Two decades on real farms", "We have spent 20 years solving growers' burning problems in the field, across crops and regions. Now the formula is open to the world.", [("Our story", None)])
body += sec(answer("Gujarat Bio Organics has worked with growers on their own farms for about 20 years, across sugarcane, potato, mango, apple, banana, citrus, coconut and cotton in many regions of India. What we learned became our Immunity range, our R&amp;D and the grades we make for brands and importers. We now offer that proven formula to partners worldwide.")
            + '<div class="kpis"><div><b>20 years</b><span>of R&amp;D and field work</span></div><div><b>8 crops</b><span>with dedicated programmes</span></div><div><b>Many regions</b><span>from the Himalayas to South Gujarat</span></div><div><b>Thousands</b><span>of growers have used our products</span></div></div>')
body += sec('<div class="hub">' + "".join(
    f'<a class="hub-i" href="{u}"><h3>{c}</h3><p class="vmeta">{r}</p><p>{d}</p></a>' for c, r, d, u in stories) + "</div>"
    + CLAIM_NOTE, "Burning problems we have worked on", "Each programme started with a problem growers brought to us, often one with no chemical answer.")
body += sec(vid_block, "Hear it from growers", "Real farms, real growers, in their own words.", cls="tint")
body += '<span id="open-to-the-world"></span>'
body += sec('<div class="two"><div class="prose"><h3>Chemical-free farming that works for the grower</h3>'
            "<p>Our vision is a world where food is grown without hazardous chemicals, and where growing that way is easier, not harder. That means products a grower can trust to do real work on a real farm, and the support to use them well.</p>"
            "<p>For 20 years we tested ours in the field before we scaled them. Now we are opening them to the world so that more growers can farm sustainably, for generations to come.</p></div>"
            + '<div><h3>Partner with the formula</h3>' + ul([
                "<b>Importers and distributors:</b> bring a proven range to your market",
                "<b>Brand owners:</b> have us make it under <a href=\"/private-label-oem\">your label</a>",
                "<b>Bulk buyers:</b> <a href=\"/bulk-supply\">IBC, drum and bag supply</a>, no minimum order",
                "<b>Growers:</b> try the <a href=\"/products\">Immunity range</a> with a small trial first"])
            + quote_btns("Hello Gujarat Bio Organics, I would like to partner with you.") + "</div></div>",
            "Open to the world", "Our mission is to make hazardous-chemical-free, sustainable food cultivation easier for everyone.")
body += sec(faq_html(im_faq) + links([("/crops", "Crop programmes", ""), ("/research-development", "Research and development", ""), ("/manufacturing-facility", "Manufacturing facility", ""), ("/export", "Export", ""), ("/about", "About us", "")]), "Questions")

_ld = [faq_ld(im_faq)]
for v in VIDS:
    if v.get("yt"):
        _ld.append({"@context": "https://schema.org", "@type": "VideoObject", "name": v.get("title", "Grower experience"),
                    "description": "Grower experience with Gujarat Bio Organics products. " + v.get("crop", ""),
                    "thumbnailUrl": f"https://i.ytimg.com/vi/{v['yt']}/hqdefault.jpg", "uploadDate": TODAY,
                    "embedUrl": f"https://www.youtube-nocookie.com/embed/{v['yt']}", "contentUrl": f"https://www.youtube.com/watch?v={v['yt']}"})
page("/impact", "20 Years on Real Farms: Grower Results & Mission | GBO",
     "Gujarat Bio Organics has worked with growers for 20 years across sugarcane, potato, mango, apple, banana, citrus and coconut. Watch growers, then partner with us.",
     body + cta("Be part of a chemical-free future", "Send your market and crop. We reply with a quote and a free sample.", "Hello Gujarat Bio Organics, I would like to partner with you."),
     [("Our story", None)], _ld, "0.8")
kw("/impact", "organic fertilizer manufacturer with farmer results", ["biostimulant company field proven india", "farmer testimonials organic fertilizer", "chemical free farming india"],
   [q for q, _ in im_faq], "Trust / brand", "Importers, brand owners, growers")
