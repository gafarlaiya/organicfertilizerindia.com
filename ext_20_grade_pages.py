# One page per Schedule VI grade (36) and per biofertiliser type (11).

FORM_WORD = {"Liquid": "liquid", "Powder": "powder", "Granular": "granular", "Granules": "granules", LAF: "liquid, granule or powder"}

for g, n, f in GRADES:
    p = grade_path(n, f)
    gi = GROUP_INFO[g]
    note = GRADE_NOTE[f"{n}|{f}"]
    fw = FORM_WORD[f]
    display = f"{n} ({fw})"
    liquid = f in ("Liquid", LAF)
    solid = f in ("Powder", "Granular", "Granules", LAF)
    h1 = f"{esc(n)} {fw}: manufacturer and supplier" if f != LAF else f"{esc(n)}: liquid, granule or powder"
    trail = [("Products", "/products"), (gi["cat_name"], gi["cat"]), (n, None)]
    siblings = [(grade_path(n2, f2), f"{n2} ({FORM_WORD[f2]})", "") for g2, n2, f2 in GRADES if g2 == g and (n2, f2) != (n, f)][:6]
    faq = [
        (f"What is {n} used for?", f"{note} It is commonly used for: " + "; ".join(u.lower() for u in gi["uses"][:3]) + "."),
        (f"How is {n} applied?", "Common methods are " + ", ".join(m.lower() for m in gi["methods"]) + ". The dose is printed on the label, and we send a crop-wise dose chart with every quote."),
        (f"Is {n} an approved grade?", f"Yes. {n} ({fw}) is a grade specified in Schedule VI of the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985, and it is covered by the No Objection Certificate issued to Gujarat Bio Organics by the Directorate of Agriculture, Government of Gujarat."),
        (f"What is the price of {n}?", PRICE_A),
        (f"Can I buy {n} under my own brand?", "Yes. We manufacture and pack it under your private label with no minimum order quantity, in " + ("liquid packs from 250 mL to 1000 L IBC" if liquid else "") + (" and " if liquid and solid else "") + ("solid packs from 1 kg buckets to 1000 kg jumbo bags" if solid else "") + "."),
        (f"Do you export {n}?", "Yes. We ship FOB or CIF from Pipavav, Kandla, Dahej, Mundra, JNPT and other Indian ports to GCC countries, Africa, the Russian Federation, Europe and the Americas."),
    ]
    image = GRADE_IMG_MAP.get(f"{n}|{f}")
    pic = img(image, f"{n} {fw}, illustrative sample image", caption="Illustrative sample image, not a lab photograph.") if image else ""
    top = answer(f"{esc(n)} ({fw}) is a {gi['cat_name'].lower()} biostimulant grade listed under Schedule VI of India's Fertiliser Control Order. {esc(note)} "
                 f"Gujarat Bio Organics manufactures it at Shihor, Bhavnagar, Gujarat, for bulk, private-label and export buyers.")
    specs = spec([("Grade", esc(n)), ("Form", fw.capitalize()), ("Product family", f'<a href="{gi["cat"]}">{gi["cat_name"]}</a>'),
                  ("Regulatory", "Schedule VI listed grade, covered by our Gujarat Directorate of Agriculture NOC")])
    body = hero(h1, esc(note), trail)
    body += sec(f'<div class="split"><div>{top}{specs}{quote_btns(f"Hello Gujarat Bio Organics, please quote {n} ({fw}). Quantity: ___ Destination: ___")}</div><div>{pic or buy_block(liquid, solid)}</div></div>')
    body += sec(f'<div class="split"><div class="prose"><h3>What it is</h3><p>{gi["what"]}</p><h3>Typical uses</h3>{ul(gi["uses"])}</div>'
                f'<div><h3>How to use it</h3>{ul(gi["methods"])}<p>The dose depends on crop, stage and method. It is printed on the label, and we send a crop-wise dose chart with every quote.</p>'
                f'<h3>Mixing</h3><p>{gi["compat"]}</p></div></div>' + CLAIM_NOTE, f"About {esc(n)}", cls="tint")
    if pic:
        body += sec(buy_block(liquid, solid), "Buying terms")
    body += sec(faq_html(faq) + links(siblings + [(gi["cat"], f"All {gi['cat_name'].lower()} grades", "Category page")], "Related grades"), "Questions about this grade", cls="" if pic else "")
    body += cta(f"Need {esc(n)}?", "Send the quantity and destination. We reply with a quote and a free sample.", f"Hello Gujarat Bio Organics, please quote {n} ({fw}).")
    ft = fw.title() if f != LAF else "Liquid, Granule, Powder"
    title = next(t for t in (f"{n} {ft} Manufacturer India | GBO", f"{n} {ft} Manufacturer | GBO", f"{n} {ft} | GBO", f"{n} | GBO") if len(t) <= 62 or t == f"{n} | GBO")
    desc = f"{n} ({fw}) from Gujarat Bio Organics, Gujarat. Schedule VI grade under our Gujarat NOC. Bulk, private label, export. No MOQ."
    if len(desc) > 160:
        desc = f"{n} ({fw}): Schedule VI grade made in Gujarat. Bulk, private label and export. No MOQ."
    page(p, title, desc, body, trail, [product_ld(p, display, note, gi["cat_name"]), faq_ld(faq)], "0.7",
         f"/assets/img/{image}.webp" if image else None)
    base = n.lower().replace("%", "").replace("(", "").replace(")", "").replace(",", "")
    kw(p, f"{base} {fw if f != LAF else ''}".strip(), [f"{base} manufacturer", f"{base} price", f"{base} uses", f"{base} supplier india"],
       [q for q, _ in faq], "Commercial", "Formulators, brands, distributors, importers")

# ------------------------------------------------------------------ biofertilisers
for b in BIOS:
    p, desc_txt, role, crops = BIO_INFO[b]
    trail = [("Products", "/products"), ("Biofertilisers", "/biofertilisers-manufacturer-india"), (b, None)]
    liquid_note = "Available in liquid and carrier-based forms on request." if "consortia" not in b.lower() else ""
    faq = [
        (f"What is {b}?", desc_txt),
        (f"Which crops is {b} used for?", "Commonly: " + ", ".join(crops) + "."),
        (f"How is {b} applied?", "Common methods are seed treatment, seedling root dip, soil application mixed with compost or farmyard manure, and drip application for liquid forms. Follow the label for dose and method."),
        (f"Can {b} be mixed with chemical fertilizers or fungicides?", "Do not mix biofertilisers directly with chemical fungicides, bactericides or concentrated fertilizers, because they can kill the organisms. Apply them separately, a few days apart, or follow the label."),
        (f"How should {b} be stored?", "Store in a cool, shaded place away from direct sunlight and heat, and use within the shelf life printed on the pack."),
        (f"Is {b} an approved product?", f"Yes. {b} is among the 11 biofertiliser types specified in Schedule III of the Fertiliser Control Order that are covered by the No Objection Certificate issued to Gujarat Bio Organics by the Directorate of Agriculture, Government of Gujarat."),
        (f"What is the price of {b}?", PRICE_A),
    ]
    others = [(BIO_INFO[o][0], o, BIO_INFO[o][2]) for o in BIOS if o != b][:6]
    body = hero(f"{esc(b)} biofertiliser manufacturer", esc(desc_txt), trail)
    body += sec(f'<div class="split"><div>{answer(esc(desc_txt) + " Gujarat Bio Organics manufactures it at Shihor, Bhavnagar, Gujarat, for bulk, private-label and export buyers.")}'
                f'{spec([("Type", esc(b)), ("Role", role), ("Main crops", ", ".join(crops)), ("Regulatory", "Schedule III biofertiliser, covered by our Gujarat Directorate of Agriculture NOC")])}'
                f'<p class="mute" style="margin-top:1rem">{liquid_note}</p>{quote_btns(f"Hello Gujarat Bio Organics, please quote {b}. Form: ___ Quantity: ___")}</div>'
                f'<div>{buy_block(True, True)}</div></div>')
    body += sec(f'<div class="split"><div class="prose"><h3>How it works</h3><p>{esc(desc_txt)}</p><p>Biofertilisers work best in soil with organic matter, moisture and a near-neutral pH. They add to, rather than replace, a balanced fertilizer programme, and they take time to establish, so apply them early in the crop.</p></div>'
                f'<div><h3>Application methods</h3>{ul(["Seed treatment before sowing", "Seedling root dip before transplanting", "Soil application mixed with compost or farmyard manure", "Drip application (liquid forms)"])}'
                f'<h3>Handling</h3>{ul(["Store cool and shaded, away from sunlight", "Keep apart from chemical fungicides and bactericides", "Use within the printed shelf life"])}</div></div>' + CLAIM_NOTE, f"About {esc(b)}", cls="tint")
    body += sec(faq_html(faq) + links(others + [("/biofertilisers-manufacturer-india", "All biofertiliser types", "Category page"), ("/resources/types-of-biofertilizers", "Types of biofertilizers", "Guide")], "Other biofertilisers"), "Questions about this biofertiliser")
    body += cta(f"Need {esc(b)}?", "Tell us the form, pack and quantity.", f"Hello Gujarat Bio Organics, please quote {b}.")
    title = f"{b} Manufacturer India | GBO" if "biofertiliser" in b.lower() else f"{b} Biofertiliser Manufacturer | GBO"
    desc = f"{b} biofertiliser ({role.lower()}) made in Gujarat. Schedule III, Gujarat NOC. Bulk, private label and export."
    page(p, title, desc, body, trail, [product_ld(p, f"{b} biofertiliser", desc_txt, "Biofertiliser"), faq_ld(faq)], "0.6")
    bl = b.lower().replace("(kmb)", "").strip()
    kw(p, f"{bl} biofertilizer", [f"{bl} biofertilizer manufacturer", f"{bl} uses", f"{bl} for crops", f"liquid {bl}"],
       [q for q, _ in faq], "Commercial", "Distributors, brands, growers")
