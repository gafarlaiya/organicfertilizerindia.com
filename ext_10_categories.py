# Category (money) pages. Each targets one primary keyword cluster from the research.

def grade_rows(group):
    out = []
    for g, n, f in GRADES:
        if g == group:
            out.append([f'<a href="{grade_path(n, f)}">{esc(n)}</a>', esc(f), esc(GRADE_NOTE[f"{n}|{f}"])])
    return out

DIFF_SNIP = {
 "/humic-acid-manufacturer-india": "Our humic acid starts with a raw material chosen over about 20 years of field comparison and is extracted without the extreme pH and heat that damage its more fragile beneficial substances.",
 "/seaweed-extract-manufacturer-india": "Only a few of the world's seaweed species suit farming. We control each step from cultivation and harvest to storage and extraction so the extract keeps its minerals, amino acids and other active compounds.",
 "/amino-acid-protein-hydrolysate-manufacturer-india": "We choose the source, the hydrolysis method, the preservation and the formulation with care, and test each batch, so our amino acids are not just an imported powder made to a price.",
}


# Extra, keyword-matched content added to category pages (Ubersuggest competitor-gap work, Oct 2026).
EXTRA_INTRO = {
 "/organic-fertilizer-manufacturer-india": ('<p>Comparing an organic fertilizer company in India? Look for one that makes what it sells. '
   'We are a manufacturer, not a trader: our plant is at GIDC Shihor, Bhavnagar, and our biostimulant and biofertiliser grades are covered by a '
   'No Objection Certificate from the Directorate of Agriculture, Government of Gujarat. We quote against your specification, not a fixed catalogue.</p>'),
 "/humic-acid-manufacturer-india": ('<p>Looking for potassium humate in India? We make potassium humate 49% powder, a soluble grade for drip, drench and liquid products, '
   'at our own plant in Bhavnagar and supply it in bulk, under private label and for export. See <a href="/bulk-pricing-and-quotes">how bulk pricing works</a>.</p>'),
 "/seaweed-extract-manufacturer-india": ('<p>These are seaweed liquid fertilizer grades made at our own plant in Bhavnagar, Gujarat, for buyers in India and abroad. '
   'Pricing depends on the grade, pack and quantity: see <a href="/bulk-pricing-and-quotes">how bulk pricing works</a>.</p>'),
 "/amino-acid-protein-hydrolysate-manufacturer-india": ('<p>Searching for amino acid fertilizer price in India? Price depends on the grade, source, form and quantity. '
   'Read <a href="/bulk-pricing-and-quotes">how bulk pricing works</a>, then send us the grade and quantity for a quote.</p>'),
 "/micronutrient-fertilizer-manufacturer-india": ('<p>We are a micronutrient fertilizers manufacturer that makes to order: mixtures, chelated forms and biostimulant-fortified products, '
   'to the grade notified for your state or to your export specification.</p>'),
}
EXTRA_FAQ = {
 "/organic-fertilizer-manufacturer-india": [
   ("How do I choose an organic fertilizer company in India?", "Check four things with any supplier. First, the product category and its approval under the Fertiliser Control Order (organic, biofertiliser under Schedule III, or biostimulant under Schedule VI). Second, whether the company manufactures the product itself or trades it. Third, whether you can see a specification sheet and a test report. Fourth, the terms: pack sizes, minimum order and dispatch time. Ours are no minimum order quantity, dispatch in about one week, and free samples (the buyer pays freight, duty and other charges).")],
 "/humic-acid-manufacturer-india": [
   ("Where can I buy potassium humate in India?", "We manufacture potassium humate 49% powder at our plant in Shihor, Bhavnagar, Gujarat, and supply it across India and abroad in solid packs from 1 kg to 1000 kg jumbo bags. Send the quantity and destination for a quote."),
   ("What is the price of potassium humate per kg in India?", PRICE_A + " See also: how bulk pricing works.")],
 "/seaweed-extract-manufacturer-india": [
   ("Are you a seaweed liquid fertilizer manufacturer in India?", "Yes. We manufacture 9 seaweed and algae grades at our own plant in Bhavnagar: Ascophyllum nodosum (15% and 7%), Kappaphycus alvarezii (24%, 9.5% and 7.2%), Sargassum tenerrimum 10%, Kappaphycus with Sargassum swartzii 1:1 and Spirulina 10% in liquid form, and Sargassum tenerrimum 2% as granules."),
   ("Is seaweed extract fertilizer approved in India?", "In India, seaweed extract is regulated as a biostimulant under Schedule VI of the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985. Our No Objection Certificate from the Directorate of Agriculture, Government of Gujarat covers our seaweed and algae grades.")],
 "/micronutrient-fertilizer-manufacturer-india": [
   ("Are you a micronutrient fertilizers manufacturer or a trader?", "We are a manufacturer. Micronutrient products are made to order at our plant in Shihor, Bhavnagar, as mixtures, chelated forms or biostimulant-fortified products, to the grade notified for your state or to your export specification."),
   ("Do you supply chelated micronutrients in bulk?", "Yes, to order. Chelated micronutrients (EDTA and other chelates) can be made as powder or liquid. Tell us the nutrient, chelate, form, quantity and destination and we will quote.")],
}

def cat_page(d):
    p = d["path"]
    body = hero(d["h1"], d["lead"], [("Products", "/products"), (d["crumb"], None)])
    inner = answer(d["answer"]) + d.get("intro", "") + EXTRA_INTRO.get(p, "")
    if d.get("grades"):
        inner += f'<h2>{d.get("grades_title", "Grades we manufacture")}</h2>' + table(["Grade", "Form", "What it is"], d["grades"])
        inner += '<p class="mute" style="margin-top:1rem">Every grade above is covered by our Gujarat Directorate of Agriculture NOC under Schedule VI. Click a grade for its page.</p>'
    if d.get("forms"):
        inner += f'<h2>{d.get("forms_title", "What we make")}</h2>' + ul(d["forms"])
    inner += quote_btns(d["wa"])
    body += sec(inner)
    if p in DIFF_SNIP:
        body += sec(f'<div class="two"><div><h2>What makes ours different</h2><p>{DIFF_SNIP[p]}</p></div><div><a class="btn btn-dark" href="/why-gujarat-bio">Read why it matters</a></div></div>', cls="tint")
    if d.get("what"):
        body += sec(f'<div class="prose">{d["what"]}</div>', d.get("what_title", "How it works"), cls="tint")
    if d.get("uses"):
        body += sec(table(d["uses_head"], d["uses"]) + CLAIM_NOTE, d.get("uses_title", "Where it is used"))
    if d.get("methods"):
        body += sec(f'<div class="split"><div><h3>Application methods</h3>{ul(d["methods"])}</div><div><h3>Dose and timing</h3><p>{d.get("dose", "Dose depends on the grade, crop, growth stage and method. The dose is printed on every label, and we send a crop-wise dose chart with every quote.")}</p></div></div>', "How to use it", cls="tint")
    body += sec(f'<div class="split"><div><h3>Why buy from Gujarat Bio Organics</h3>{ul(d.get("why", WHY))}</div><div><h3>Buying terms</h3>{buy_block(d.get("liquid", True), d.get("solid", True))}</div></div>', "Manufacturer-direct supply")
    faqs = d["faq"] + EXTRA_FAQ.get(p, [])
    body += sec(faq_html(faqs) + links(d["related"]), "Questions buyers ask", cls="tint")
    body += cta(d.get("cta_t", "Tell us the grade, quantity and destination."), "We reply with a quote and a free sample.", d["wa"])
    sch = [faq_ld(faqs)]
    if d.get("grades"):
        sch.append(itemlist_ld(d["crumb"] + " grades", [(grade_path(n, f), f"{n} ({f})") for g, n, f in GRADES if g in d.get("groups", [])]))
    page(p, d["title"], d["desc"], body, [("Products", "/products"), (d["crumb"], None)], sch, "0.9", d.get("og"))
    kw(p, d["kw"][0], d["kw"][1], [q for q, _ in faqs], d.get("intent", "Commercial"), d.get("aud", "B2B buyers, distributors, importers"))

WHY = ["Our own plant at GIDC Shihor, Bhavnagar, Gujarat, manufacturing since 2009",
       "100 KL of liquid and 2,500 tonnes of solid products every month",
       "No minimum order quantity and dispatch in about one week",
       "In-house R&amp;D for formulation, stability and crop programmes",
       "Gujarat NOC for 36 biostimulant grades and 11 biofertiliser types",
       "Bulk, private label, export or our Immunity brand from one supplier"]

# =============================================================== HUMIC
cat_page(dict(
 path="/humic-acid-manufacturer-india", crumb="Humic acid",
 title="Humic Acid Manufacturer India: Granules, Powder, Liquid | GBO",
 desc="Humic acid, fulvic acid and potassium humate manufacturer in Gujarat. 8 grades in granules, powder and liquid. Bulk, private label and export. No MOQ.",
 h1="Humic acid manufacturer in India: granules, powder and liquid",
 lead="Eight humic and fulvic grades from our plant in Bhavnagar, Gujarat, from 1.5% soil granules to 76% soluble powder. Bulk, private label and export.",
 answer="Humic acid is the stable, dark fraction of decomposed organic matter, used in farming to condition soil, hold nutrients near the roots and support root growth. Gujarat Bio Organics manufactures 8 humic, fulvic and potassium humate grades in granular, powder and liquid form at Shihor, Bhavnagar.",
 grades=grade_rows("humic"), groups=["humic"],
 what=("<p>" + GROUP_INFO["humic"]["what"] + "</p><h3>Humic acid or fulvic acid?</h3><p>Both come from the same humified material. "
       "Humic acids are larger molecules that are not soluble in acid, so they work mainly in the soil. Fulvic acids are smaller and "
       "soluble at every pH, so they move more easily and suit foliar and drip use. Many products combine both. Read our "
       '<a href="/resources/humic-acid-vs-fulvic-acid">humic vs fulvic guide</a>.</p>'
       "<h3>Potassium humate or humic acid?</h3><p>Potassium humate is humic acid that has been neutralised with potassium, which makes it "
       'water-soluble. Choose potassium humate for drip, drench and liquid formulation, and humic granules for basal application. See '
       '<a href="/resources/potassium-humate-vs-humic-acid">potassium humate vs humic acid</a>.</p>'),
 what_title="Humic acid, fulvic acid and potassium humate",
 uses_head=["Crop stage", "Why humic is used", "Grades to ask for"],
 uses=[["Land preparation and sowing", "Soil conditioning, early root growth", "Humic acid 51% granular, 1.5% granules, 5% powder"],
       ["Vegetative growth", "Holding applied nutrients near the roots", "Potassium humate 49%, humates 12.5% liquid"],
       ["Drip and fertigation", "Soluble humic and fulvic with each irrigation", "Humic and fulvic acid 25.05% liquid, 76% powder"],
       ["Formulation and private label", "Base for liquid and granule products", "Potassium humate 49%, humic and fulvic acid 76%"]],
 methods=GROUP_INFO["humic"]["methods"], wa="Hello Gujarat Bio Organics, please quote humic acid. Grade: ___ Quantity: ___ Destination: ___",
 faq=[("What is humic acid used for in agriculture?", "Humic acid is used to improve soil structure, hold nutrients near the root zone, complex micronutrients and support root growth, so crops make better use of the fertiliser already applied. It is most useful in compact, over-cropped or low organic-matter soils."),
      ("What is the difference between humic acid and fulvic acid?", "Both are humic substances. Humic acid molecules are larger and work mainly in the soil. Fulvic acid molecules are smaller and dissolve at any pH, so they suit foliar and drip use."),
      ("Is potassium humate the same as humic acid?", "Potassium humate is humic acid neutralised with potassium, which makes it soluble in water. It is used where humic acid has to be dissolved, such as drip, drench and liquid products."),
      ("Humic acid granules or liquid: which is better?", "Granules suit basal application with fertiliser and broadcast. Liquids and soluble powders suit drip, drench and fertigation. Many growers use granules at sowing and a liquid later in the crop."),
      ("Can I mix humic acid with NPK fertiliser, urea or micronutrients?", "Humic acid mixes with most fertilisers, including NPK, urea and micronutrients. Avoid mixing with strongly acidic products or concentrated calcium solutions without a jar test, because humic acid can settle out at low pH."),
      ("What is the dose of humic acid per acre?", "Dose depends on the grade and concentration, so a 1.5% granule and a 51% granule are used at very different rates. Follow the label, or ask us for the crop-wise dose chart for the grade you buy."),
      ("What does 'humic acid 98' mean?", "It usually refers to high-solubility potassium humate flakes or powder sold on a total-content basis. Our listed grade for sale in India is potassium humate 49% powder. For export, send us the specification you need and we will quote."),
      ("What is the price of humic acid per kg in India?", PRICE_A),
      ("Do you make humic acid under private label?", "Yes. We pack any of our 8 humic grades under your brand, in liquid packs from 250 mL to 1000 L IBC and solid packs from 1 kg to 1000 kg jumbo bags.")],
 related=[("/products/potassium-humate-49-powder", "Potassium humate 49% powder", "Soluble humate grade"),
          ("/products/humic-acid-51-granular", "Humic acid 51% granular", "High-content granule"),
          ("/resources/humic-acid-uses-in-agriculture", "Humic acid uses in agriculture", "Guide"),
          ("/resources/can-humic-acid-be-mixed-with-fertilizers-and-pesticides", "Mixing humic acid with other inputs", "Compatibility guide"),
          ("/zyme-granules-manufacturer", "Zyme and soil granules", "Granular range"),
          ("/seaweed-extract-manufacturer-india", "Seaweed extract", "Pairs well with humic")],
 kw=("humic acid manufacturer in india", ["humic acid manufacturers in india", "humic acid supplier india", "humic acid granules", "humic acid powder", "humic acid liquid", "potassium humate 49 powder", "fulvic acid fertilizer", "humic acid fertilizer", "humic acid price", "humic acid granules price per kg", "humic acid uses", "humic acid for plants", "bulk humic acid exporter"]),
 og="/assets/img/humic-acid-51-granular.webp"))

# =============================================================== SEAWEED
cat_page(dict(
 path="/seaweed-extract-manufacturer-india", crumb="Seaweed extract",
 title="Seaweed Extract Manufacturer India: Liquid & Granules | GBO",
 desc="Ascophyllum nodosum, Kappaphycus alvarezii, Sargassum and Spirulina extracts from Gujarat. 9 seaweed grades in liquid and granules. Bulk, private label, export.",
 h1="Seaweed extract manufacturer in India: liquid and granules",
 lead="Nine seaweed and algae grades, Ascophyllum, Kappaphycus, Sargassum and Spirulina, made at our plant in Bhavnagar, Gujarat. Bulk, private label and export.",
 answer="Seaweed extract is a concentrate made from marine algae, used as a biostimulant to help crops cope with heat, drought and salt stress and to support flowering, fruit set and growth. Gujarat Bio Organics manufactures 9 seaweed and algae grades, Ascophyllum nodosum, Kappaphycus alvarezii, Sargassum and Spirulina, in liquid and granular form.",
 grades=grade_rows("seaweed"), groups=["seaweed"],
 what=("<p>" + GROUP_INFO["seaweed"]["what"] + "</p><h3>Which seaweed should you choose?</h3><p>Ascophyllum nodosum is the most widely used and "
       "studied seaweed for biostimulants worldwide. Kappaphycus alvarezii is a red seaweed farmed in India, and its extract (often called "
       "K-sap) is used widely in Indian field crops. Sargassum is a tropical brown seaweed found along Indian coasts. Blends combine profiles. "
       'Read <a href="/resources/kappaphycus-vs-ascophyllum-vs-sargassum">Kappaphycus vs Ascophyllum vs Sargassum</a>.</p>'
       "<h3>Liquid or granules?</h3><p>Liquid extracts suit foliar spray and drip. Seaweed granules carry the extract into the soil with basal fertiliser, "
       'which is why they are popular with farmers who broadcast. See our <a href="/zyme-granules-manufacturer">granules range</a>.</p>'),
 what_title="Ascophyllum, Kappaphycus, Sargassum and Spirulina",
 uses_head=["Situation", "Why seaweed is used", "Grades to ask for"],
 uses=[["Heat, drought or salinity", "Supporting stress tolerance", "Ascophyllum nodosum 15%, Kappaphycus alvarezii 24%"],
       ["Flowering and fruit set", "Supporting set and fruit development", "Ascophyllum nodosum 7%, Kappaphycus + Sargassum (1:1)"],
       ["Early growth and transplanting", "Root and shoot growth, recovery", "Kappaphycus alvarezii 9.5% or 7.2%, Spirulina 10%"],
       ["Basal soil application", "Seaweed with fertiliser at sowing", "Sargassum tenerrimum 2% granular, humic + seaweed granules"]],
 methods=GROUP_INFO["seaweed"]["methods"], wa="Hello Gujarat Bio Organics, please quote seaweed extract. Grade: ___ Quantity: ___ Destination: ___",
 faq=[("What is seaweed extract used for in agriculture?", "Seaweed extract is used to help crops tolerate heat, drought and salinity, to support flowering and fruit set, and to support root and shoot growth and recovery after stress. It is applied as a foliar spray, through drip or as granules in the soil."),
      ("What is the difference between Ascophyllum, Kappaphycus and Sargassum extracts?", "They come from different seaweeds. Ascophyllum nodosum is a North Atlantic brown alga, Kappaphycus alvarezii is a red alga farmed in tropical waters including India, and Sargassum is a tropical brown alga. Each has a different composition, so the best choice depends on crop and purpose."),
      ("What does 'Kappaphycus alvarezii 24 (liquid)' mean?", "It is the grade name as listed under Schedule VI of the Fertiliser Control Order: Kappaphycus alvarezii seaweed extract at 24% in liquid form. We also make the 9.5% and 7.2% Kappaphycus grades."),
      ("Seaweed granules or liquid seaweed: which should I use?", "Use granules for basal or broadcast application with fertiliser, and liquid for foliar sprays and drip. Many programmes use granules at sowing and liquid sprays at flowering."),
      ("Can seaweed extract be mixed with humic acid?", "Yes. Seaweed and humic acid are commonly applied together, and we make ready blends of humic acid plus seaweed extract in liquid, powder and granules."),
      ("What is the dose of seaweed extract per litre of water?", "It depends on the grade and concentration. Follow the label, or ask us for the dose chart for the grade you buy."),
      ("What is the price of seaweed extract fertilizer in India (25 kg or 25 L)?", PRICE_A),
      ("Do you export seaweed extract?", "Yes. We ship to GCC countries, Africa, the Russian Federation, Europe and the Americas, FOB or CIF from Indian ports, in drums, IBCs or your private-label packs.")],
 related=[("/products/kappaphycus-alvarezii-24-liquid", "Kappaphycus alvarezii 24% liquid", ""),
          ("/products/ascophyllum-nodosum-15-liquid", "Ascophyllum nodosum 15% liquid", ""),
          ("/products/sargassum-tenerrimum-2-granular", "Sargassum tenerrimum 2% granular", "Seaweed granules"),
          ("/resources/seaweed-extract-uses-in-agriculture", "Seaweed extract uses in agriculture", "Guide"),
          ("/resources/kappaphycus-vs-ascophyllum-vs-sargassum", "Which seaweed to choose", "Comparison"),
          ("/humic-acid-manufacturer-india", "Humic acid", "Common partner input")],
 kw=("seaweed extract manufacturers in india", ["seaweed extract supplier india", "seaweed extract liquid", "seaweed extract powder", "seaweed extract granules", "seaweed granules fertilizer", "kappaphycus alvarezii 24 liquid", "kappaphycus alvarezii 9.5 liquid", "ascophyllum nodosum 15 liquid", "ascophyllum nodosum 7 liquid", "seaweed extract fertilizer", "seaweed extract price", "seaweed extract 25 kg price", "seaweed extract uses in agriculture"]),
 og="/assets/img/kappaphycus-24-liquid.webp"))

# =============================================================== AMINO / PROTEIN
cat_page(dict(
 path="/amino-acid-protein-hydrolysate-manufacturer-india", crumb="Amino acid and protein hydrolysate",
 title="Amino Acid Fertilizer & Protein Hydrolysate Manufacturer | GBO",
 desc="Plant and animal source protein hydrolysate and amino acid fertilizer manufacturer in Gujarat. 9 grades, liquid, powder and granules. Bulk, private label, export.",
 h1="Amino acid fertilizer and protein hydrolysate manufacturer",
 lead="Nine grades from plant and animal protein, liquid, powder and granules, made at our plant in Bhavnagar, Gujarat.",
 answer="Protein hydrolysates and amino acid fertilizers supply free amino acids and peptides that crops use to recover from stress and keep growing. Gujarat Bio Organics manufactures 9 grades, plant-source and animal-source protein hydrolysates, amino acid 5%, 10% and 20%, and glutamic acid from vinasse residue, in liquid, powder and granular form.",
 grades=grade_rows("protein"), groups=["protein"],
 what=("<p>" + GROUP_INFO["protein"]["what"] + "</p><h3>Protein hydrolysate or amino acid?</h3><p>A protein hydrolysate contains both free amino "
       "acids and peptides; an amino acid grade is specified by its free amino acid content. In practice the two are used for similar jobs. "
       'Read <a href="/resources/protein-hydrolysate-vs-amino-acid">protein hydrolysate vs amino acid</a>.</p>'
       "<h3>Plant source or animal source?</h3><p>Animal-source hydrolysates (for example from collagen) are rich in glycine and proline. "
       "Plant-source hydrolysates have a broader profile and are preferred in some organic and export markets. Tell us your market and we "
       "will recommend the source.</p>"),
 what_title="Plant source, animal source and free amino acids",
 uses_head=["Situation", "Why amino acids are used", "Grades to ask for"],
 uses=[["After cold, heat, hail or transplanting", "Supporting recovery", "Protein hydrolysate plant source 25% or 27%, amino acid 20%"],
       ["Early growth", "Canopy and root development", "Amino acid 10%, protein hydrolysate plant source 16.9%"],
       ["Flowering and fruit set", "Supporting set in fruit and vegetables", "Protein hydrolysate animal source 36.04%, amino acid 20%"],
       ["Granular and retail products", "Low-dose ready products", "Protein hydrolysate plant source 1.5%, amino acid 5%"]],
 methods=GROUP_INFO["protein"]["methods"], wa="Hello Gujarat Bio Organics, please quote amino acid / protein hydrolysate. Grade: ___ Quantity: ___",
 faq=[("What is protein hydrolysate in agriculture?", "It is a biostimulant made by breaking proteins down into free amino acids and short peptides. Crops use these to recover from stress and support growth, flowering and fruit set."),
      ("What is the difference between protein hydrolysate and amino acid fertilizer?", "A protein hydrolysate contains free amino acids plus peptides. An amino acid fertilizer is specified by its free amino acid content. Both are used for recovery and growth."),
      ("Plant-based or animal-based amino acids: which is better?", "Neither is better for every case. Animal-source hydrolysates are rich in glycine and proline; plant-source hydrolysates have a broader profile and are preferred in some organic and export markets."),
      ("What are the uses of amino acid fertilizer?", "Supporting recovery after cold, heat, transplanting or pest damage, supporting early growth and canopy, supporting flowering and fruit set, and complexing micronutrients in foliar sprays."),
      ("What is the dose of amino acid fertilizer per acre?", "It depends on the grade and concentration. Follow the label, or ask us for the dose chart for the grade you buy."),
      ("Do you supply amino acid 80% soybean-based powder?", "Our grades listed for sale in India are shown above. For export or formulation, send us the specification you need and we will quote."),
      ("What is the amino acid fertilizer price in India (25 kg)?", PRICE_A),
      ("Can amino acids be mixed with seaweed extract?", "Yes. Amino acids and seaweed extract are commonly sprayed together. Run a jar test with any other product in the tank.")],
 related=[("/products/amino-acid-20", "Amino acid 20%", "Most concentrated amino grade"),
          ("/products/protein-hydrolysate-animal-source-36-04-liquid", "Protein hydrolysate, animal source 36.04%", ""),
          ("/products/protein-hydrolysate-plant-source-27", "Protein hydrolysate, plant source 27%", ""),
          ("/resources/protein-hydrolysate-vs-amino-acid", "Protein hydrolysate vs amino acid", "Guide"),
          ("/seaweed-extract-manufacturer-india", "Seaweed extract", "Common partner input"),
          ("/private-label-oem", "Private label and OEM", "Your brand, our plant")],
 kw=("amino acid fertilizer manufacturer india", ["protein hydrolysate manufacturer india", "protein hydrolysate fertilizer", "protein hydrolysate uses in agriculture", "protein hydrolysate powder", "protein hydrolysate liquid", "amino acid fertilizer uses", "amino acid fertilizer price", "amino acid fertilizer 25 kg price", "amino acid fertilizer powder", "plant based amino acid fertilizer", "amino acid fertilizer dose per acre"]),
 og="/assets/img/amino-20-liquid.webp"))

# =============================================================== ORGANIC FERTILIZERS
cat_page(dict(
 path="/organic-fertilizer-manufacturer-india", crumb="Organic fertilizers",
 title="Organic Fertilizer Manufacturer in Gujarat, India | GBO",
 desc="Organic fertilizer and bio-organic input manufacturer in Bhavnagar, Gujarat: humic, seaweed, amino, biofertilisers and organic granules. Bulk, private label, export.",
 h1="Organic fertilizer manufacturer in Gujarat, India",
 lead="Organic and bio-organic inputs for soil and crop health, made at our plant in Shihor, Bhavnagar, for growers, brands, distributors and importers.",
 answer="Organic fertilizers are made from natural, plant, animal or microbial sources and feed the soil as well as the crop. Gujarat Bio Organics manufactures organic and bio-organic inputs in Bhavnagar, Gujarat: humic and fulvic acids, seaweed extracts, protein hydrolysates, 11 biofertiliser types and organic granules, for bulk, private-label and export buyers.",
 forms=['<a href="/humic-acid-manufacturer-india">Humic and fulvic acid</a>: soil conditioners in granules, powder and liquid',
        '<a href="/seaweed-extract-manufacturer-india">Seaweed extracts</a>: Ascophyllum, Kappaphycus, Sargassum, Spirulina',
        '<a href="/amino-acid-protein-hydrolysate-manufacturer-india">Protein hydrolysates and amino acids</a>: plant and animal source',
        '<a href="/biofertilisers-manufacturer-india">Biofertilisers</a>: 11 types including NPK consortia',
        '<a href="/zyme-granules-manufacturer">Organic and biostimulant granules</a>: humic, seaweed and protein granules for broadcast',
        'Organic manure and bio-enriched organic granules made to your specification for bulk and private-label buyers'],
 forms_title="Our organic and bio-organic range",
 what=("<p>In India, organic fertilizers such as city compost, vermicompost, fermented organic manure (FOM), phosphate-rich organic manure "
       "(PROM) and bio-enriched organic manure are specified under the Fertiliser Control Order, alongside biofertilisers (Schedule III) "
       "and biostimulants (Schedule VI). Each category has its own standard.</p>"
       "<p>Organic inputs work differently from mineral fertilizers. Mineral fertilizers supply a fixed dose of nutrients quickly. Organic "
       "inputs build soil organic matter, feed soil life, hold nutrients and release them more slowly. Most profitable programmes use both: "
       "mineral fertilizer for the nutrient dose, and organic and biological inputs to make the soil use it well.</p>"
       '<p>Read <a href="/resources/biostimulant-vs-fertilizer-vs-biofertilizer">biostimulant vs fertilizer vs biofertilizer</a> for how the categories differ.</p>'),
 what_title="Organic fertilizers and how they work",
 uses_head=["Crop group", "Common organic inputs", "Where to start"],
 uses=[["Sugarcane and cotton", "Humic granules, biofertiliser consortia, Acetobacter for cane", '<a href="/crops/sugarcane">Sugarcane</a>, <a href="/crops/cotton">cotton</a>'],
       ["Fruit orchards", "Humic liquids, seaweed extract, mycorrhizae", '<a href="/crops/mango">Mango</a>, <a href="/crops/apple">apple</a>, <a href="/crops/citrus">citrus</a>'],
       ["Vegetables and potato", "Seaweed, amino acids, PSB and KMB", '<a href="/crops/potato">Potato</a>'],
       ["Plantation crops", "Humic, biofertilisers, organic granules", '<a href="/crops/coconut">Coconut</a>, <a href="/crops/banana">banana</a>']],
 methods=["Basal application with or before mineral fertilizer", "Mixing biofertilisers with compost or farmyard manure", "Drip and fertigation with soluble organics", "Foliar sprays of seaweed and amino acids"],
 wa="Hello Gujarat Bio Organics, I need organic fertilizers. Product: ___ Quantity: ___ Destination: ___",
 faq=[("What is organic fertilizer?", "An organic fertilizer is made from natural plant, animal or microbial material. It supplies nutrients more slowly than mineral fertilizer and builds soil organic matter and soil life."),
      ("What is the difference between organic and chemical fertilizer?", "Chemical (mineral) fertilizers supply a known dose of nutrients that is available quickly. Organic fertilizers release nutrients slowly and improve the soil itself. Most growers get the best result using both together."),
      ("Is humic acid an organic fertilizer?", "Humic acid is an organic soil conditioner. In India it is regulated as a biostimulant under Schedule VI of the Fertiliser Control Order, not as a nutrient fertilizer."),
      ("What is the best organic fertilizer for plants?", "There is no single best one. Match the input to the need: humic acid for tired soil, biofertilisers for nutrient supply, seaweed for stress and flowering, amino acids for recovery. Tell us your crop and we will recommend a programme."),
      ("Which organic fertilizer is used for coconut, paddy and vegetables?", "Coconut programmes commonly use humic products and biofertilisers; paddy uses Azospirillum, PSB and zinc solubilisers; vegetables use seaweed, amino acids and PSB and KMB. See our crop pages for detail."),
      ("Are you an organic fertilizer manufacturer in Gujarat?", "Yes. Our plant is at Plot No. 321, GIDC 2, Ghanghli Road, Shihor, Bhavnagar, Gujarat, and we supply across India and abroad."),
      ("Can you make organic fertilizer under my brand?", "Yes. We manufacture and pack under your private label, with no minimum order quantity.")],
 related=[("/biofertilisers-manufacturer-india", "Biofertilisers", "11 types"), ("/humic-acid-manufacturer-india", "Humic acid", "8 grades"),
          ("/crop-specific-fertilizers", "Crop-specific products", "Immunity range"), ("/resources/biostimulant-vs-fertilizer-vs-biofertilizer", "Biostimulant vs fertilizer vs biofertilizer", "Guide"),
          ("/become-a-distributor", "Become a distributor", ""), ("/private-label-oem", "Private label", "")],
 kw=("organic fertilizer manufacturer in india", ["organic fertilizer manufacturer in gujarat", "organic fertilizer manufacturer", "organic fertilizer supplier india", "bio organic fertilizer manufacturer", "organic fertilizer for plants", "organic fertilizer for coconut tree", "organic fertilizer for paddy", "organic fertilizer for vegetable plants", "organic manure manufacturer"]),
 aud="Distributors, brands, institutional buyers, growers"))

# =============================================================== MICRONUTRIENTS
cat_page(dict(
 path="/micronutrient-fertilizer-manufacturer-india", crumb="Micronutrient fertilizers",
 title="Micronutrient Fertilizer Manufacturer India | GBO",
 desc="Micronutrient fertilizer manufacturer in Gujarat. Chelated EDTA, zinc, boron, iron and state-grade mixtures, made to order. Bulk, private label and export.",
 h1="Micronutrient fertilizer manufacturer: chelated and mixtures",
 lead="Zinc, boron, iron, manganese, copper and molybdenum products, plain, chelated and combined with biostimulants, made to order for brands, distributors and importers.",
 answer="Micronutrients are nutrients crops need in small amounts, such as zinc, boron, iron, manganese, copper and molybdenum, whose deficiency limits yield even when NPK is sufficient. Gujarat Bio Organics makes micronutrient fertilizers to order, as mixtures, chelated forms and biostimulant-fortified products, for bulk, private-label and export buyers.",
 forms=["Micronutrient mixtures made to the grade notified for your state, or to your export specification",
        "Chelated micronutrients (EDTA and other chelates) as powder or liquid for foliar and drip use",
        "Single-nutrient products: zinc, boron, iron, manganese, copper, molybdenum",
        "Micronutrients fortified with humic acid, seaweed extract or amino acids",
        "Granular micronutrient products for basal application"],
 forms_title="What we make to order",
 what=("<p>Crops need micronutrients in grams rather than kilograms, but a shortage of one of them limits growth however much NPK is applied. "
       "Zinc deficiency is widespread in Indian soils, boron affects flowering and fruit set, and iron and manganese deficiency is common in "
       "high-pH and calcareous soils.</p><h3>Chelated or non-chelated?</h3><p>A chelate wraps the metal ion in an organic molecule such as EDTA, "
       "which keeps it soluble and available across a wider pH range and makes it suitable for foliar and drip use. Sulphate-based products cost "
       "less and suit soil application where pH is not limiting.</p><h3>Micronutrient mixture grades</h3><p>In India, state governments notify "
       "micronutrient mixture grades for their regions. We manufacture to the grade notified for your state, or to the specification of your export market.</p>"
       '<p>See <a href="/resources/micronutrient-deficiency-symptoms-in-crops">micronutrient deficiency symptoms in crops</a>.</p>'),
 what_title="Why micronutrients matter",
 uses_head=["Nutrient", "Common deficiency signs", "Commonly affected crops"],
 uses=[["Zinc", "Small leaves, shortened internodes, pale stripes or patches", "Paddy, wheat, maize, citrus, cotton"],
       ["Boron", "Poor flowering, flower and fruit drop, cracked or deformed fruit", "Cotton, groundnut, fruit crops, vegetables"],
       ["Iron", "Yellowing between veins on young leaves", "Crops on high-pH and calcareous soils"],
       ["Manganese", "Interveinal yellowing with spots on younger leaves", "Cereals, citrus, soybean"],
       ["Copper and molybdenum", "Dieback and leaf tip damage (Cu); pale, cupped leaves in legumes (Mo)", "Fruit crops (Cu), legumes and vegetables (Mo)"]],
 uses_title="Deficiencies we are asked about",
 methods=["Soil application with basal fertilizer", "Foliar spray (chelated and soluble forms)", "Drip and fertigation", "Seed treatment (selected nutrients)"],
 wa="Hello Gujarat Bio Organics, please quote micronutrient fertilizer. Nutrient or grade: ___ Quantity: ___",
 faq=[("What are micronutrient fertilizers?", "Products that supply zinc, boron, iron, manganese, copper or molybdenum, which crops need in small amounts but cannot grow well without."),
      ("What is the difference between chelated and non-chelated micronutrients?", "A chelate (such as EDTA) keeps the metal soluble and available across a wider pH range, so it works well in foliar and drip use. Non-chelated sulphates cost less and suit soil application."),
      ("What is chelated zinc EDTA 12%?", "Zinc chelated with EDTA, containing 12% zinc. It is a common foliar and drip zinc source."),
      ("What are micronutrient mixture grades?", "State governments in India notify micronutrient mixture grades for their regions. We make to the notified grade for your state or to your export specification."),
      ("Can micronutrients be mixed with humic acid or amino acids?", "Yes. Humic and amino acids can complex micronutrients and help keep them available. We make fortified products that combine them."),
      ("What is the price of micronutrient fertilizer (1 kg, 10 kg, 50 kg)?", PRICE_A),
      ("Do you make micronutrients under private label?", "Yes, with no minimum order quantity, in packs from 1 kg to 1000 kg jumbo bags and liquids from 250 mL to 1000 L IBC.")],
 related=[("/resources/micronutrient-deficiency-symptoms-in-crops", "Micronutrient deficiency symptoms", "Guide"),
          ("/water-soluble-fertilizer-special-grades", "Water-soluble special grades", ""), ("/custom-fertilizer-blends", "Custom blends", ""),
          ("/biofertilisers-manufacturer-india", "Zinc solubilising bacteria", "Biological zinc"), ("/private-label-oem", "Private label", ""), ("/export", "Export", "")],
 kw=("micronutrient fertilizer manufacturer india", ["micronutrient fertilizer", "micronutrient mixture fertilizer", "chelated micronutrients manufacturer", "chelated zinc edta 12", "chelated zinc fertilizer", "micronutrient fertilizer products list", "micronutrient fertilizer price", "micronutrient fertilizer liquid", "micronutrient fertilizer for cotton"])))

# =============================================================== WATER SOLUBLE / SPECIAL GRADES
cat_page(dict(
 path="/water-soluble-fertilizer-special-grades", crumb="Water-soluble and special grades",
 title="Water Soluble Fertilizer & Special Grade Fertilizers | GBO",
 desc="100% water-soluble NPK special grades and biostimulant-fortified fertilizers made to order in Gujarat for drip, foliar and private label. Bulk and export.",
 h1="Water-soluble fertilizers and special grade fertilizers",
 lead="Fully soluble NPK special grades for drip and foliar feeding, and special fortified grades that combine nutrients with humic, seaweed or amino acids, made to order.",
 answer="Water-soluble fertilizers (WSF) are 100% soluble NPK grades used in drip irrigation and foliar sprays to feed a crop at the exact stage it needs each nutrient. Gujarat Bio Organics makes special grade and fortified fertilizers to order for brands, distributors and importers, including blends with humic acid, seaweed extract and amino acids.",
 forms=["Fully water-soluble NPK special grades to your specification",
        "Special grades fortified with humic acid, seaweed extract or amino acids",
        "Stage-specific grades: starter, vegetative, flowering and fruit development",
        "Packs for retail (1 kg) through bulk (25 kg bags and jumbo bags)"],
 forms_title="What we make to order",
 what=("<p>Each water-soluble grade is named by its N:P:K ratio, and each ratio suits a different crop stage. Growers commonly use "
       "balanced grades such as 19:19:19 in vegetative growth, phosphorus-rich grades such as 12:61:0 at establishment, and potash-rich grades "
       "such as 13:0:45 or 0:0:50 at fruit development. Calcium and magnesium grades and micronutrient-fortified grades complete the range.</p>"
       "<p>Special grades become more useful when they carry a biostimulant. Humic acid and seaweed extract are commonly combined with soluble "
       "NPK so one application feeds the crop and supports root activity or stress tolerance.</p>"
       '<p>See <a href="/resources/slow-release-vs-water-soluble-fertilizer">slow-release vs water-soluble fertilizer</a>.</p>'),
 what_title="How special grades are chosen",
 uses_head=["Crop stage", "Commonly used grade type", "Typical purpose"],
 uses=[["Establishment and rooting", "Phosphorus-rich grades (for example 12:61:0)", "Root development"],
       ["Vegetative growth", "Balanced grades (for example 19:19:19)", "Canopy and growth"],
       ["Flowering", "Phosphorus and potash grades with boron", "Flowering and set"],
       ["Fruit development and quality", "Potash-rich grades (for example 13:0:45, 0:0:50)", "Size, colour and quality"]],
 uses_title="Common grades by crop stage",
 methods=["Drip and fertigation", "Foliar spray", "Hydroponics and protected cultivation"],
 wa="Hello Gujarat Bio Organics, please quote water-soluble special grade fertilizer. Grade: ___ Quantity: ___",
 faq=[("What is water-soluble fertilizer?", "A fertilizer that dissolves completely in water, so it can be applied through drip irrigation or as a foliar spray and is taken up quickly."),
      ("What are the common water-soluble fertilizer grades?", "Common grades include 19:19:19, 20:20:20, 12:61:0, 13:40:13, 13:0:45, 0:52:34, 0:0:50, calcium nitrate and magnesium sulphate. Each suits a different crop stage."),
      ("What is 19:19:19 fertilizer used for?", "It is a balanced NPK grade used mainly in vegetative growth through drip or foliar spray."),
      ("When should 13:0:45 and 0:52:34 be used?", "Potash-rich 13:0:45 is commonly used at fruit development; 0:52:34 supplies phosphorus and potash, commonly at flowering. Follow a crop-wise schedule."),
      ("What are special grade fertilizers?", "Grades formulated for a particular crop, stage or need, often fortified with micronutrients or biostimulants such as humic acid, seaweed or amino acids."),
      ("What is the price of water-soluble fertilizer (25 kg)?", PRICE_A),
      ("Can you make a water-soluble grade under my brand?", "Yes. We make special grades to your specification and pack under your private label.")],
 related=[("/custom-fertilizer-blends", "Custom blends", "Your formula"), ("/micronutrient-fertilizer-manufacturer-india", "Micronutrients", ""),
          ("/slow-release-fertilizer", "Slow-release fertilizers", ""), ("/resources/slow-release-vs-water-soluble-fertilizer", "Slow-release vs water-soluble", "Guide"),
          ("/seaweed-extract-manufacturer-india", "Seaweed extract", "Fortification"), ("/private-label-oem", "Private label", "")],
 kw=("water soluble fertilizer manufacturer india", ["special grade fertilizer", "water soluble fertilizer grades", "water soluble fertilizer grade list", "water soluble fertilizer price list", "19 19 19 fertilizer uses", "13 0 45 fertilizer uses", "0 52 34 fertilizer", "npk water soluble fertilizer", "water soluble fertilizer company list"]),
 liquid=False))

# =============================================================== CUSTOM BLENDS
cat_page(dict(
 path="/custom-fertilizer-blends", crumb="Custom fertilizer blends",
 title="Custom Fertilizer Blends & Customized Fertilizers for Crops | GBO",
 desc="Custom fertilizer and biostimulant blends made to your formula for crops, soils and markets. In-house R&D, sample batch, private label. Gujarat manufacturer.",
 h1="Custom fertilizer blends, formulated for your crops and markets",
 lead="Bring a formula, or bring a problem. Our R&amp;D team formulates nutrient, biostimulant and biological blends for your crop, soil and market, and we manufacture and pack them under your brand.",
 answer="A custom fertilizer blend is a product formulated for a specific crop, soil or market instead of a general grade. Gujarat Bio Organics formulates and manufactures custom blends of nutrients, humic acid, seaweed extract, amino acids and biofertilisers for brands, distributors and importers, from sample batch to full production.",
 forms=["Biostimulant blends: humic, seaweed, amino acid and botanical combinations",
        "Nutrient plus biostimulant blends for drip, foliar or basal use",
        "Granular blends for broadcast with basal fertilizer",
        "Crop programmes: one product per crop stage, packed as a kit",
        "Blends to the specification of your export market"],
 forms_title="What we can formulate",
 what=("<h3>How a custom blend is made</h3><ol><li><strong>Brief.</strong> Tell us the crop, soil, region, application method and target price, or send your formula.</li>"
       "<li><strong>Formulation.</strong> Our R&amp;D team proposes a composition, checks compatibility and stability, and picks the form (liquid, powder or granule).</li>"
       "<li><strong>Sample batch.</strong> We make a sample for your testing and field trial.</li><li><strong>Approval.</strong> You approve the product, label and pack.</li>"
       "<li><strong>Production.</strong> We manufacture and pack under your brand, usually about one week after approval.</li></ol>"
       "<h3>Customised fertilizers in India</h3><p>In India, 'customised fertilizers' are also a regulated category: multi-nutrient products made for "
       "specific soils and crops on the basis of soil-test data, notified by the Government. If your blend is to be sold in India, we check which "
       "Fertiliser Control Order category it falls under before production.</p>"),
 what_title="From brief to production",
 uses_head=["Who asks for custom blends", "What they usually need"],
 uses=[["Brand owners", "A differentiated product for their market, packed under their brand"],
       ["Distributors", "Crop programmes for the main crops of their territory"],
       ["Importers", "A blend that meets their country's registration specification"],
       ["Large farms and estates", "Programmes matched to their soil test and crop calendar"]],
 uses_title="Who we formulate for",
 methods=["Drip and fertigation blends", "Foliar blends", "Basal and broadcast granules", "Seed and seedling treatment"],
 wa="Hello Gujarat Bio Organics, I want a custom blend. Crop: ___ Purpose: ___ Market: ___",
 faq=[("What is a customized fertilizer?", "A product formulated for a specific crop, soil or region instead of a general grade. In India, 'customised fertilizers' are also a notified category based on soil-test data."),
      ("Can you make a blend to my own formula?", "Yes. Send the formula and we check compatibility, stability and the regulatory category, then make a sample batch."),
      ("Is there a minimum order quantity for custom blends?", "No fixed minimum. We quote against your requirement."),
      ("How long does a custom blend take?", "A sample batch is usually quick once the formula is agreed, and production is about one week after approval."),
      ("Will my formula be kept confidential?", "Yes. Your formula is used only for your orders. Ask us for a confidentiality agreement if you need one."),
      ("Can custom blends include biofertilisers?", "Yes, where the organisms are compatible with the other ingredients. Our R&D team checks compatibility before formulating.")],
 related=[("/research-development", "Research and development", "Our formulation team"), ("/private-label-oem", "Private label and OEM", ""),
          ("/water-soluble-fertilizer-special-grades", "Special grades", ""), ("/resources/how-to-start-a-fertilizer-brand-private-label", "How to start a fertilizer brand", "Guide"),
          ("/crop-specific-fertilizers", "Crop-specific products", ""), ("/manufacturing-facility", "Manufacturing facility", "")],
 kw=("custom fertilizer blends", ["customized fertilizer", "customized fertilizer manufacturer india", "custom fertilizer blend", "custom biostimulant formulation", "fertilizer formulation services", "customized fertilizer example", "crop specific blends"]),
 intent="Commercial", aud="Brand owners, distributors, importers, estates"))

# =============================================================== CROP-SPECIFIC (Immunity)
crop_list = [("sugarcane", "Sugarcane"), ("potato", "Potato"), ("mango", "Mango"), ("apple", "Apple"), ("banana", "Banana"), ("cotton", "Cotton"), ("citrus", "Citrus"), ("coconut", "Coconut")]
cat_page(dict(
 path="/crop-specific-fertilizers", crumb="Crop-specific products",
 title="Crop-Specific Fertilizers & Biostimulants: Immunity Range | GBO",
 desc="Immunity crop-specific products for sugarcane, potato, mango, apple, banana, cotton, citrus and coconut, built from field work with growers.",
 h1="Crop-specific fertilizers and biostimulants: the Immunity range",
 lead="Our own Immunity brand: products and programmes built crop by crop, from field work with growers who had run out of answers.",
 answer="Crop-specific fertilizers are products formulated for the needs of one crop and its usual problems, rather than general grades. Gujarat Bio Organics' Immunity range includes crop-specific products and programmes for sugarcane, potato, mango, apple and banana, with programmes for cotton, citrus and coconut, developed from field work with growers.",
 forms=[f'<a href="/crops/{s}">{n}</a>: ' + t for (s, n), t in zip(crop_list, [
        "Immunity Sugarcane Special, developed with growers in South Gujarat",
        "Immunity Potato Special, developed for potato growers in Punjab and Haryana",
        "Immunity Mango Special, for mango growers across India",
        "Immunity Apple Special, for orchards in Himachal Pradesh and Jammu and Kashmir",
        "Immunity Banana Special, developed with growers in Central Gujarat",
        "Crop programme for cotton", "Crop programme for citrus", "Crop programme for coconut"])],
 forms_title="Crops we have built products for",
 what=("<p>Every crop has its own calendar and its own failures. Sugarcane on land cropped for decades needs its soil rebuilt; apple and mango "
       "orchards fight tree decline and uneven bearing; banana fights disease pressure; potato needs strong early roots and even tuber set. "
       "A general grade does not answer these.</p><p>The Immunity range was built the other way round: start from the problem growers describe, "
       "combine nutrition, biostimulants and biologicals into a programme, test it in the field, and keep what works. That is also how we build "
       'crop programmes for <a href="/private-label-oem">private-label brands</a> and <a href="/become-a-distributor">distributors</a>.</p>'),
 what_title="Why crop-specific",
 uses_head=["Crop", "Problems growers bring to us", "Crop page"],
 uses=[["Sugarcane", "Exhausted soil after decades of cane, rising input costs", '<a href="/crops/sugarcane">Sugarcane</a>'],
       ["Potato", "Falling yields, small or few tubers, high fertilizer use", '<a href="/crops/potato">Potato</a>'],
       ["Mango", "Tree decline, alternate bearing, fruit drop, small fruit", '<a href="/crops/mango">Mango</a>'],
       ["Apple", "Plant mortality, low production and quality, rising costs", '<a href="/crops/apple">Apple</a>'],
       ["Banana", "Fungal disease pressure, mortality, uneven bunch weight", '<a href="/crops/banana">Banana</a>']],
 uses_title="What each programme was built for",
 methods=["Basal soil programme at planting or season start", "Drip and drench through the season", "Foliar sprays at key stages"],
 wa="Hello Gujarat Bio Organics, please share the Immunity range for my crop. Crop: ___ Region: ___",
 faq=[("What is a crop-specific fertilizer?", "A product or programme formulated for the needs and usual problems of one crop, rather than a general grade for all crops."),
      ("Which crops does the Immunity range cover?", "Sugarcane, potato, mango, apple and banana have dedicated Immunity Special products, and we have programmes for cotton, citrus and coconut."),
      ("Can I sell the Immunity range as a distributor?", "Yes, in territories where we do not yet have a presence. We give bulk prices and you set your own margin."),
      ("Can you make crop-specific products under my brand?", "Yes. We build crop programmes for private-label brands and distributors."),
      ("Do crop-specific products guarantee yield?", "No. Results depend on soil, weather and practice. We recommend a trial on part of the field first.")],
 related=[(f"/crops/{s}", f"{n}", "Crop page") for s, n in crop_list[:6]],
 kw=("crop specific fertilizer", ["crop specific fertilizers india", "crop specific biostimulant", "immunity sugarcane special", "best fertilizer for sugarcane", "fertilizer for mango tree", "fertilizer for potato crop", "fertilizer for banana plant in india"]),
 aud="Growers, distributors, brand owners", cta_t="Tell us your crop and region."))

# =============================================================== SLOW RELEASE
cat_page(dict(
 path="/slow-release-fertilizer", crumb="Slow-release fertilizers",
 title="Slow Release Fertilizer Manufacturer India: Granules | GBO",
 desc="Slow-release fertilizer granules made to order in Gujarat for field crops, horticulture and private label. How slow and controlled release work, and how to buy.",
 h1="Slow-release fertilizer granules, made to order",
 lead="Granules that feed the crop over weeks instead of days, for fewer applications and less nutrient loss. Formulated to your nutrient content and release period.",
 answer="A slow-release fertilizer releases its nutrients gradually over weeks or months instead of dissolving at once, which reduces leaching and volatilisation losses and the number of applications. Gujarat Bio Organics makes slow-release granular products to order for bulk and private-label buyers.",
 forms=["Slow-release granules to your nutrient content and release period", "Granules combining nutrients with humic and organic matter",
        "Slow-release products for horticulture, nurseries and field crops", "Private-label packs from 1 kg buckets to 1000 kg jumbo bags"],
 forms_title="What we make to order",
 what=("<p>Fertilizer that dissolves at once can be lost before the crop uses it: nitrogen leaches or escapes as gas, and phosphorus gets "
       "locked in the soil. Slow-release products spread the supply over time.</p><h3>Slow-release, controlled-release and stabilised</h3>"
       "<ul><li><strong>Slow-release</strong> products release nutrients gradually, but the rate depends on soil moisture, temperature and microbial activity.</li>"
       "<li><strong>Controlled-release</strong> products, usually polymer-coated, release at a rate set by the coating, mainly driven by temperature.</li>"
       "<li><strong>Stabilised</strong> products, such as neem-coated urea, slow down the conversion of nitrogen in the soil rather than coating it fully.</li></ul>"
       '<p>See <a href="/resources/slow-release-vs-water-soluble-fertilizer">slow-release vs water-soluble fertilizer</a>.</p>'),
 what_title="How slow release works",
 uses_head=["Use", "Why slow release helps"],
 uses=[["Long-duration crops such as sugarcane and banana", "Feeds over a long season with fewer top dressings"],
       ["Sandy and high-rainfall soils", "Reduces leaching losses"], ["Nurseries, pots and landscapes", "One application lasts for weeks"],
       ["Labour-scarce farms", "Fewer applications through the season"]],
 uses_title="Where it is used",
 methods=["Basal application at planting", "Side placement near the root zone", "Mixing into potting and nursery media"],
 wa="Hello Gujarat Bio Organics, I need slow-release fertilizer. Nutrient content: ___ Quantity: ___", liquid=False,
 faq=[("What is a slow-release fertilizer?", "A fertilizer that releases nutrients gradually over weeks or months, instead of dissolving all at once."),
      ("What is the difference between slow-release and controlled-release fertilizer?", "Slow-release products release gradually at a rate that depends on soil conditions. Controlled-release products, usually polymer-coated, release at a rate set by the coating."),
      ("What are examples of slow-release fertilizers?", "Coated and organic-matrix granules, low-solubility nitrogen compounds and organic fertilizers. Neem-coated urea is a stabilised product that slows nitrogen conversion."),
      ("Slow-release or water-soluble fertilizer: which should I use?", "Water-soluble fertilizer feeds a crop quickly at a precise stage through drip or foliar spray. Slow-release fertilizer gives a steady supply from one basal application. Many programmes use both."),
      ("Is neem-coated urea a slow-release fertilizer?", "It is usually described as a slow-release or stabilised nitrogen fertilizer, because the neem coating slows the conversion of urea nitrogen in the soil."),
      ("Can you make slow-release fertilizer under my brand?", "Yes. Tell us the nutrient content and release period you want and we propose a formulation and sample.")],
 related=[("/water-soluble-fertilizer-special-grades", "Water-soluble fertilizers", ""), ("/zyme-granules-manufacturer", "Biostimulant granules", ""),
          ("/custom-fertilizer-blends", "Custom blends", ""), ("/resources/slow-release-vs-water-soluble-fertilizer", "Slow-release vs water-soluble", "Guide"),
          ("/humic-acid-manufacturer-india", "Humic acid", ""), ("/private-label-oem", "Private label", "")],
 kw=("slow release fertilizer india", ["slow release fertilizer manufacturer", "slow release fertilizer granules", "slow release fertilizer npk", "slow release fertilizer examples", "controlled release fertilizer india", "slow release vs controlled release fertilizer"])))

# =============================================================== ZYME GRANULES
cat_page(dict(
 path="/zyme-granules-manufacturer", crumb="Zyme and biostimulant granules",
 title="Zyme Granules Manufacturer: Seaweed & Humic Granules | GBO",
 desc="Zyme granules from Schedule VI listed grades: humic, seaweed and protein granules in buckets, bags and jumbo bags. Bulk and private label.",
 h1="Zyme granules manufacturer: seaweed, humic and protein granules",
 lead="Broadcast-ready biostimulant granules made from grades listed under Schedule VI, in buckets, bags and jumbo bags, for distributors, brands and bulk buyers.",
 answer="Zyme granules is the trade name farmers in India use for broadcast granules that carry biostimulants such as seaweed extract, humic acid or protein hydrolysate. Gujarat Bio Organics makes these granules from grades listed under Schedule VI and covered by our Gujarat NOC: humic acid granules, Sargassum seaweed granules, humic plus seaweed granules and protein hydrolysate or amino acid granules.",
 grades=[[f'<a href="{grade_path(n, f)}">{esc(n)}</a>', esc(f if f != LAF else "Granules (also liquid, powder)"), esc(GRADE_NOTE[f"{n}|{f}"])] for g, n, f in GRADES
         if (f in ("Granular", "Granules")) or n in ("Protein hydrolysate, plant source 1.5%", "Amino acid 5%")],
 grades_title="Granular grades we manufacture", groups=["humic", "seaweed", "blends"],
 what=("<p>A granule makes a biostimulant easy to apply: the farmer broadcasts it with basal fertilizer or at earthing up, without "
       "spraying. In the Indian market these products are widely sold as zyme, seaweed or soil granules.</p><h3>Why the grade on the bag matters now</h3>"
       "<p>Biostimulants in India came under Schedule VI of the Fertiliser Control Order in 2021, with a provisional registration period. Industry "
       "reports say provisional registrations ended on 17 June 2025, after which only biostimulants specified in Schedule VI can be sold. "
       "Granules made from listed grades protect distributors and brands from stock that can no longer be sold. "
       'See our <a href="/fco-schedule-vi-biostimulants">Schedule VI guide</a>.</p><h3>What are zyme granules made of?</h3><p>Composition varies '
       "by maker. Most carry seaweed extract, humic acid, protein hydrolysate or a mix on a granular carrier. Ours carry the listed grade printed on the bag.</p>"),
 what_title="What zyme granules are, and what to check",
 uses_head=["Application point", "Granule to ask for"],
 uses=[["Basal with fertilizer at sowing or planting", "Humic acid 51% granular, humic + seaweed granules"],
       ["Earthing up and top dressing", "Humic acid 1.5% granules, Sargassum tenerrimum 2% granular"],
       ["Vegetables and horticulture beds", "Protein hydrolysate or amino acid granules"],
       ["Retail buckets for dealers", "Any granular grade in 1 to 20 kg buckets"]],
 methods=["Broadcast with basal fertilizer", "Band placement near the root zone", "At earthing up or top dressing"],
 wa="Hello Gujarat Bio Organics, please quote zyme / seaweed granules. Grade: ___ Pack: ___ Quantity: ___", liquid=False,
 faq=[("What are zyme granules?", "Broadcast granules that carry biostimulants such as seaweed extract, humic acid or protein hydrolysate. 'Zyme' is a trade term in India, not a regulated category."),
      ("What is the composition of zyme granules?", "It varies by manufacturer. Ours are made from Schedule VI listed grades such as humic acid 51% granular, Sargassum tenerrimum 2% granular and humic acid plus seaweed extract granules."),
      ("What are the uses of zyme granules?", "They are broadcast with basal fertilizer or at earthing up to support root growth and soil conditioning through the season."),
      ("What is the price of zyme granules per kg or per bucket?", PRICE_A),
      ("What pack sizes do you offer?", "1, 2, 4, 5, 8, 10 and 20 kg bags or buckets, 25 and 50 kg bags, and 600 kg and 1000 kg jumbo bags."),
      ("Are zyme granules legal to sell after June 2025?", "Biostimulants must be specified in Schedule VI of the Fertiliser Control Order to be sold in India. Check that the grade on the bag is a listed grade. Ours are."),
      ("Seaweed granules or humic granules: which is better?", "Humic granules mainly condition the soil and support roots; seaweed granules add stress support. Our humic plus seaweed granules combine both.")],
 related=[("/products/humic-acid-51-granular", "Humic acid 51% granular", ""), ("/products/sargassum-tenerrimum-2-granular", "Sargassum tenerrimum 2% granular", ""),
          ("/products/humic-acid-plus-seaweed-extract-granules", "Humic acid + seaweed extract granules", ""), ("/resources/what-are-zyme-granules", "What are zyme granules?", "Guide"),
          ("/fco-schedule-vi-biostimulants", "FCO Schedule VI explained", "Regulation"), ("/become-a-distributor", "Become a distributor", "")],
 kw=("zyme granules manufacturer", ["zyme granules", "zyme granules uses", "zyme granules composition", "zyme granules price per kg", "zyme granules bucket", "bio zyme granules", "seaweed granules fertilizer", "seaweed granules price", "humic granules manufacturer"]),
 og="/assets/img/humic-seaweed-granules.webp"))
