# Knowledge centre: answer-first guides for AEO/GEO. Each opens with a 40-70 word direct answer.

ARTICLES = []

def art(s, h1, title, desc, ans, sections, faq, related, kwp, kws, aud="Growers, buyers, distributors"):
    p = f"/resources/{s}"
    trail = [("Knowledge centre", "/resources"), (h1, None)]
    toc = '<div class="toc"><strong>On this page</strong><ol>' + "".join(f'<li><a href="#{i}">{h}</a></li>' for i, h, _ in sections) + "</ol></div>"
    body_html = "".join(f'<h2 id="{i}">{h}</h2>{c}' for i, h, c in sections)
    body = hero(h1, desc, trail)
    body += sec(f'<div class="prose">{answer(ans)}<p class="meta-line">By the Gujarat Bio Organics R&amp;D team &middot; Updated October 2026</p>{toc}{body_html}</div>')
    body += sec(faq_html(faq) + links(related, "Read next"), "Frequently asked questions", cls="tint")
    body += cta()
    page(p, title, desc, body, trail, [article_ld(p, h1, desc), faq_ld(faq)], "0.6")
    kw(p, kwp, kws, [q for q, _ in faq], "Informational", aud)
    ARTICLES.append((p, h1, desc))

# 1 ------------------------------------------------------------------
art("what-is-a-biostimulant", "What is a biostimulant? Meaning, types and uses", "What Is a Biostimulant? Meaning, Types & Uses in Agriculture",
 "A plain explanation of biostimulants: what they are, the main types, how they differ from fertilizers, and how they are regulated in India.",
 "A biostimulant is a substance or micro-organism applied to plants, seeds or soil to stimulate the plant's own processes, improving nutrient uptake, growth, quality or tolerance to stress, regardless of its nutrient content. Common types are humic and fulvic acids, seaweed extracts, protein hydrolysates and amino acids, botanical extracts and beneficial micro-organisms.",
 [("meaning", "Biostimulant meaning", "<p>A fertilizer feeds the crop: it supplies nitrogen, phosphorus, potassium or other nutrients. A biostimulant helps the crop use what it has: it supports root growth, nutrient uptake and the plant's response to heat, drought, salinity or transplanting shock. Many programmes use both.</p>"),
  ("types", "Main types of biostimulants", table(["Type", "What it is", "Typical role"], [
      ['<a href="/humic-acid-manufacturer-india">Humic and fulvic acids</a>', "Stable fraction of decomposed organic matter", "Soil conditioning, nutrient holding, roots"],
      ['<a href="/seaweed-extract-manufacturer-india">Seaweed extracts</a>', "Concentrates of marine algae", "Stress tolerance, flowering and fruit set"],
      ['<a href="/amino-acid-protein-hydrolysate-manufacturer-india">Protein hydrolysates and amino acids</a>', "Broken-down plant or animal proteins", "Recovery after stress, growth"],
      ["Botanical extracts", "Extracts of specific plants", "Varies by plant"],
      ["Beneficial micro-organisms", "Live microbes other than biofertilisers", "Root zone activity"]])),
  ("how", "How biostimulants work", "<p>Biostimulants act on plant physiology rather than supplying nutrients in bulk. Humic substances improve the soil environment around roots; seaweed extracts carry compounds that influence growth and stress responses; amino acids are building blocks the plant can use directly instead of making them, which saves energy under stress.</p>"),
  ("india", "How biostimulants are regulated in India", '<p>Biostimulants are regulated under Schedule VI of the Fertiliser Control Order. Since June 2025, only biostimulants specified in Schedule VI can be sold. See our <a href="/fco-schedule-vi-biostimulants">Schedule VI guide</a>.</p>'),
  ("use", "How to use biostimulants well", ul(["Match the product to a problem: soil, stress, flowering, recovery", "Apply at the right stage, before stress where you can", "Keep your normal fertilizer programme; biostimulants do not replace it", "Run a trial strip and compare before scaling up"], ""))],
 [("What is the difference between a biostimulant and a fertilizer?", "A fertilizer supplies nutrients. A biostimulant stimulates the plant's own processes to use nutrients better and cope with stress, regardless of its nutrient content."),
  ("What is the difference between a biostimulant and a biofertilizer?", "A biofertilizer contains living micro-organisms that supply or release nutrients, such as nitrogen fixers and phosphate solubilisers. A biostimulant works on plant processes. In India they are regulated in different schedules of the FCO."),
  ("Is a biostimulant a plant growth regulator?", "No. Plant growth regulators are synthetic or natural hormones regulated as pesticides. Biostimulants are regulated separately under the FCO."),
  ("What are examples of biostimulants?", "Humic acid, fulvic acid, seaweed extract (Ascophyllum, Kappaphycus, Sargassum), protein hydrolysates, amino acids and botanical extracts."),
  ("What is biostimulant in Hindi?", "In Hindi it is often called jaiv uttejak (जैव उत्तेजक): a product that stimulates the plant's own growth processes.")],
 [("/resources/biostimulant-vs-fertilizer-vs-biofertilizer", "Biostimulant vs fertilizer vs biofertilizer", ""), ("/biostimulants-manufacturer-india", "Our 36 biostimulant grades", ""), ("/fco-schedule-vi-biostimulants", "FCO Schedule VI explained", ""), ("/resources/humic-acid-uses-in-agriculture", "Humic acid uses", "")],
 "what is a biostimulant", ["biostimulant meaning", "biostimulant meaning in hindi", "biostimulant products in agriculture", "types of biostimulants", "biostimulant examples", "biostimulant fertilizer"])

# 2 ------------------------------------------------------------------
art("biostimulant-vs-fertilizer-vs-biofertilizer", "Biostimulant vs fertilizer vs biofertilizer: the difference", "Biostimulant vs Fertilizer vs Biofertilizer: Key Differences",
 "How biostimulants, fertilizers, biofertilizers and plant growth regulators differ, with examples and how to combine them.",
 "A fertilizer supplies nutrients; a biofertilizer contains living micro-organisms that supply or release nutrients; a biostimulant stimulates the plant's own processes to use nutrients better and cope with stress. Plant growth regulators are hormones regulated as pesticides. The best programmes use fertilizers for the nutrient dose and biologicals to make that dose work harder.",
 [("table", "Side by side", table(["", "Fertilizer", "Biofertilizer", "Biostimulant"], [
     ["What it does", "Supplies nutrients", "Supplies or releases nutrients through microbes", "Stimulates plant processes"],
     ["Examples", "Urea, DAP, MOP, NPK, water-soluble grades", "Azotobacter, Rhizobium, PSB, KMB, mycorrhizae", "Humic acid, seaweed extract, amino acids"],
     ["Regulated in India under", "FCO Schedule I and others", "FCO Schedule III", "FCO Schedule VI"],
     ["Works on", "The nutrient supply", "The soil and root zone biology", "The plant's physiology and the soil environment"]])),
  ("pgr", "What about plant growth regulators?", "<p>Plant growth regulators (PGRs) such as gibberellic acid are hormones that directly switch plant processes on or off. In India they are regulated as pesticides, not under the FCO, and they are a different category from biostimulants.</p>"),
  ("combine", "How to combine them", ul(["Base the fertilizer dose on a soil test", "Add biofertilisers at sowing or planting, apart from chemical fungicides", "Use biostimulants at the stages where the crop is under pressure: establishment, stress, flowering", "Check compatibility before tank-mixing"], ""))],
 [("Can biostimulants replace fertilizers?", "No. Biostimulants help the crop use nutrients and cope with stress, but they do not supply nutrients in the amounts a crop removes."),
  ("Is humic acid a fertilizer or a biostimulant?", "In India humic and fulvic acids are regulated as biostimulants under Schedule VI of the FCO."),
  ("Can biofertilizers and chemical fertilizers be used together?", "Yes, in the same programme, but do not mix biofertilisers directly with concentrated chemical fertilizers or fungicides. Apply them separately."),
  ("What is the difference between amino acids and biostimulants?", "Amino acid products are one type of biostimulant, alongside humic substances, seaweed extracts and others.")],
 [("/resources/what-is-a-biostimulant", "What is a biostimulant?", ""), ("/resources/types-of-biofertilizers", "Types of biofertilizers", ""), ("/organic-fertilizer-manufacturer-india", "Organic fertilizers", ""), ("/fco-schedule-vi-biostimulants", "FCO Schedule VI", "")],
 "difference between biostimulant and fertilizer", ["difference between biostimulant and biofertilizer", "difference between biostimulant and pgr", "biostimulant vs fertilizer", "difference between amino acid and biostimulant", "difference between micronutrients and biostimulants"])

# 3 ------------------------------------------------------------------
art("humic-acid-vs-fulvic-acid", "Humic acid vs fulvic acid: differences, uses and which to choose", "Humic Acid vs Fulvic Acid: Differences & Uses in Agriculture",
 "How humic and fulvic acids differ in molecule size, solubility and use, and when to choose each for soil, drip or foliar application.",
 "Humic and fulvic acids are both humic substances from decomposed organic matter. Humic acids are larger molecules that do not dissolve in acid and work mainly in the soil, improving structure and nutrient holding. Fulvic acids are smaller, dissolve at any pH and move more easily, so they suit foliar and drip use. Many products combine both.",
 [("diff", "The key differences", table(["", "Humic acid", "Fulvic acid"], [
     ["Molecule size", "Larger", "Smaller"], ["Solubility", "Soluble in alkaline conditions, not in acid", "Soluble at all pH"],
     ["Colour", "Dark brown to black", "Yellow to golden brown"], ["Main role", "Soil structure, nutrient holding, roots", "Nutrient transport, foliar and drip use"],
     ["Best application", "Basal, granules, soil drench", "Foliar, drip, fertigation"]])),
  ("choose", "Which should you choose?", "<p>For tired, compact or low organic-matter soil, start with humic acid, usually as granules at sowing or as a soluble humate through drip. For foliar programmes and fertigation where solubility matters, choose fulvic-rich grades. For most farms a combined humic and fulvic product covers both jobs.</p>"),
  ("our-grades", "Our humic and fulvic grades", ul([f'<a href="{grade_path(n, f)}">{esc(n)} ({f.lower()})</a>' for g, n, f in GRADES if g == "humic"], ""))],
 [("Is fulvic acid better than humic acid?", "Neither is better overall. Fulvic acid suits foliar and drip use because it dissolves at any pH; humic acid does more for soil structure."),
  ("Can humic and fulvic acid be used together?", "Yes. They come from the same material and are often sold together, as in our humic and fulvic acid 25.05% liquid and 76% powder."),
  ("What is fulvic acid used for in plants?", "Fulvic acid is used to help move nutrients into the plant and in foliar and drip programmes, often together with micronutrients."),
  ("Where do humic and fulvic acids come from?", "Commercial products are usually extracted from humified organic sources such as leonardite or lignite.")],
 [("/humic-acid-manufacturer-india", "Humic acid manufacturer", ""), ("/resources/potassium-humate-vs-humic-acid", "Potassium humate vs humic acid", ""), ("/resources/humic-acid-uses-in-agriculture", "Humic acid uses", ""), ("/products/humic-and-fulvic-acid-76-powder", "Humic and fulvic acid 76% powder", "")],
 "humic acid vs fulvic acid", ["humic acid and fulvic acid", "difference between humic and fulvic acid", "fulvic acid uses", "fulvic acid for plants", "fulvic acid fertilizer", "what is humic acid and fulvic acid"])

# 4 ------------------------------------------------------------------
art("humic-acid-uses-in-agriculture", "Humic acid uses in agriculture: what it does and how to apply it", "Humic Acid Uses in Agriculture: Benefits, Application & Timing",
 "What humic acid does for soil and crops, which form to use when, how it is applied by crop, and common mistakes to avoid.",
 "Humic acid is used in agriculture to improve soil structure, hold nutrients near the roots, make micronutrients more available and support root growth, so crops make better use of fertilizer. It is applied as granules with basal fertilizer, as soluble humate through drip or drench, and in fulvic-rich forms as a foliar spray.",
 [("does", "What humic acid does", ul(["Improves soil structure and water holding in compact or sandy soils", "Increases the soil's ability to hold nutrients (cation exchange)", "Complexes micronutrients so they stay available", "Supports root growth and soil life", "Reduces losses of applied fertilizer"], "")),
  ("forms", "Which form to use", table(["Form", "Use it for", "Our grades"], [
      ["Granules", "Basal and broadcast with fertilizer", '<a href="/products/humic-acid-51-granular">51% granular</a>, <a href="/products/humic-acid-1-5-granules">1.5% granules</a>'],
      ["Soluble powder", "Drip, drench, formulation", '<a href="/products/potassium-humate-49-powder">Potassium humate 49%</a>, <a href="/products/humic-and-fulvic-acid-76-powder">76% powder</a>'],
      ["Liquid", "Drip and drench, ready to use", '<a href="/products/humates-12-5-liquid">Humates 12.5%</a>, <a href="/products/humic-and-fulvic-acid-25-05-liquid">25.05%</a>']])),
  ("timing", "When to apply", "<p>The most useful timings are at sowing or planting (with basal fertilizer), at top dressing, and through drip during active growth. In orchards, apply after harvest and before the main flush. Follow the label dose for the grade you buy.</p>"),
  ("mistakes", "Common mistakes", ul(["Mixing humic acid with strongly acidic products, which makes it settle out", "Comparing products by price per kg without checking concentration", "Expecting humic acid to replace fertilizer", "Applying on bone-dry soil with no follow-up irrigation"], ""))],
 [("What is humic acid made of?", "Commercial humic acid is usually extracted from humified organic material such as leonardite or lignite. Potassium humate is humic acid neutralised with potassium."),
  ("How do I use humic acid for plants?", "Use granules with basal fertilizer, or dissolve soluble humate for drip or drench. Follow the label dose."),
  ("How do I use humic acid granules?", "Broadcast them with basal fertilizer or at top dressing, then irrigate."),
  ("Can humic acid be used for paddy?", "Yes. Humic granules are commonly broadcast in paddy with basal fertilizer or at the first top dressing."),
  ("What does humic acid do (humic acid kya kaam karta hai)?", "It improves the soil, holds nutrients near the roots and supports root growth, so the crop uses fertilizer better.")],
 [("/humic-acid-manufacturer-india", "Humic acid manufacturer", ""), ("/resources/can-humic-acid-be-mixed-with-fertilizers-and-pesticides", "Mixing humic acid", ""), ("/resources/humic-acid-vs-fulvic-acid", "Humic vs fulvic", ""), ("/crops/sugarcane", "Humic acid in sugarcane", "")],
 "humic acid uses in agriculture", ["humic acid uses", "humic acid for plants", "what is humic acid used for", "how to use humic acid for plants", "how to use humic acid granules", "humic acid benefits", "humic acid kya kam karta hai", "humic acid uses in hindi"])

# 5 ------------------------------------------------------------------
art("potassium-humate-vs-humic-acid", "Potassium humate vs humic acid: what is the difference?", "Potassium Humate vs Humic Acid: Difference, Uses & Grades",
 "Potassium humate is soluble humic acid. Here is how the two differ, what grades like 49% and 98% mean, and which to use.",
 "Potassium humate is humic acid that has been neutralised with potassium, which makes it soluble in water. Humic acid itself is insoluble in acid and is usually applied to soil as granules or powder. Choose potassium humate for drip, drench, foliar and liquid formulation, and humic acid granules for basal application.",
 [("diff", "The difference", table(["", "Humic acid", "Potassium humate"], [["Solubility", "Low in water", "High in water"], ["Typical forms", "Granules, powder", "Powder, flakes, liquid"], ["Best for", "Basal soil application", "Drip, drench, foliar, formulation"], ["Our grades", "Humic acid 51% granular, 5% powder, 1.5% granules", "Potassium humate 49% powder"]])),
  ("numbers", "What 49% and 98% mean", "<p>The percentage on a label describes content, but different labels measure different things: humic acid content, total humic and fulvic content, or solubility. That is why a '98%' product and a '49%' product cannot be compared on the number alone. In India, sell and buy the grade exactly as specified in Schedule VI. Our listed grade is potassium humate 49% powder.</p>"),
  ("use", "How potassium humate is used", ul(["Dissolved for drip and fertigation", "Soil drench around the root zone", "Mixed into liquid fertilizers and biostimulants by brand owners"], ""))],
 [("Is potassium humate the same as humic acid?", "It is humic acid in its soluble potassium salt form."),
  ("What is potassium humate 98?", "It usually means high-solubility potassium humate flakes or powder sold on a total-content basis. Compare specifications, not just the number."),
  ("What are the uses of potassium humate 49 powder?", "Drip, drench and foliar programmes, and as a soluble humic base for liquid formulations."),
  ("Is potassium humate a fertilizer?", "In India it is regulated as a biostimulant grade under Schedule VI, not as a potash fertilizer.")],
 [("/products/potassium-humate-49-powder", "Potassium humate 49% powder", ""), ("/humic-acid-manufacturer-india", "All humic grades", ""), ("/resources/humic-acid-vs-fulvic-acid", "Humic vs fulvic", "")],
 "potassium humate vs humic acid", ["potassium humate 98", "potassium humate 49 powder", "potassium humate uses", "potassium humate fertilizer", "potassium humate price", "potassium humate flakes"])

# 6 ------------------------------------------------------------------
art("seaweed-extract-uses-in-agriculture", "Seaweed extract uses in agriculture: benefits and how to apply", "Seaweed Extract Uses in Agriculture: Benefits & How to Apply",
 "What seaweed extract does for crops, liquid vs granules, when to apply, and what to check when buying.",
 "Seaweed extract is used in agriculture to help crops cope with heat, drought and salinity, to support flowering and fruit set, and to support root and shoot growth and recovery after stress. Liquid extracts are applied as foliar sprays or through drip; seaweed granules are broadcast with basal fertilizer.",
 [("benefits", "What growers use it for", ul(["Getting through heat waves, dry spells and saline patches", "Flowering, fruit set and fruit development", "Root growth after sowing and transplanting", "Recovery after hail, frost or pest damage", "Quality in fruit and vegetable crops"], "")),
  ("forms", "Liquid, powder or granules", "<p>Liquid extracts are the most common and suit foliar spray and drip. Powders are convenient to store and ship and dissolve for spraying. Granules carry seaweed into the soil with basal fertilizer, which suits farmers who broadcast rather than spray.</p>"),
  ("timing", "When to apply", "<p>Seaweed works best before or at the start of stress, and at key stages: establishment, the start of flowering, fruit set and early fruit development. Spray in the cooler part of the day.</p>"),
  ("buy", "What to check when buying", ul(["The seaweed species and the extract percentage", "That the grade is specified in Schedule VI if sold in India", "A specification sheet and test report", "The dose per acre for the concentration you are paying for"], ""))],
 [("What are the benefits of seaweed extract for plants?", "It supports tolerance to heat, drought and salinity, flowering and fruit set, root and shoot growth, and recovery after stress."),
  ("How is seaweed extract made?", "Seaweed is processed to break open the cells and release soluble compounds, which are concentrated to the specified extract content."),
  ("Can seaweed extract be mixed with humic acid?", "Yes. They are often applied together, and we make ready humic plus seaweed blends."),
  ("Is seaweed extract organic?", "It is derived from natural seaweed. Whether a product is permitted in certified organic farming depends on the certifying standard and the processing used."),
  ("What are seaweed granules used for?", "Broadcasting with basal fertilizer or at top dressing to bring seaweed into the root zone.")],
 [("/seaweed-extract-manufacturer-india", "Seaweed extract manufacturer", ""), ("/resources/kappaphycus-vs-ascophyllum-vs-sargassum", "Which seaweed to choose", ""), ("/zyme-granules-manufacturer", "Seaweed granules", "")],
 "seaweed extract uses in agriculture", ["seaweed extract for plants", "seaweed extract benefits", "seaweed extract fertilizer uses", "how is seaweed extract made", "seaweed granules uses", "seaweed extract and humic acid"])

# 7 ------------------------------------------------------------------
art("kappaphycus-vs-ascophyllum-vs-sargassum", "Kappaphycus vs Ascophyllum vs Sargassum: which seaweed extract?", "Kappaphycus vs Ascophyllum vs Sargassum Seaweed Extract",
 "How the three main seaweeds used in biostimulants differ, what grades like Kappaphycus alvarezii 24 (liquid) mean, and how to choose.",
 "Ascophyllum nodosum is a cold-water brown seaweed from the North Atlantic and the most widely used in biostimulants worldwide. Kappaphycus alvarezii is a red seaweed farmed in tropical waters including India. Sargassum is a tropical brown seaweed found along Indian coasts. Each gives a different extract profile, so choice depends on crop, purpose, price and market.",
 [("compare", "Side by side", table(["", "Ascophyllum nodosum", "Kappaphycus alvarezii", "Sargassum"], [
     ["Type", "Brown seaweed", "Red seaweed", "Brown seaweed"], ["Where it grows", "Cold North Atlantic coasts", "Farmed in tropical waters, including India's south-east coast", "Tropical and warm coasts, including India"],
     ["Our grades", "15% and 7% liquid", "24%, 9.5% and 7.2% liquid", "S. tenerrimum 10% liquid and 2% granular"],
     ["Commonly chosen for", "Stress and quality programmes, export markets", "Field crops and cost-effective Indian programmes", "Liquid and granular soil programmes"]])),
  ("grade-names", "What the grade names mean", '<p>Names such as "Kappaphycus alvarezii 24 (liquid)" or "Ascophyllum nodosum 15 (liquid)" are grade entries as specified under Schedule VI of India\'s Fertiliser Control Order: species, extract percentage and form. Buy the exact listed grade.</p>'),
  ("choose", "How to choose", ul(["Start from the crop stage and problem", "Compare cost per acre at the label dose, not cost per litre", "For export, check which species your market expects", "Consider blends such as Kappaphycus + Sargassum (1:1)"], ""))],
 [("Which seaweed extract is best?", "There is no single best. Ascophyllum is the most studied worldwide; Kappaphycus is widely used in Indian field crops; Sargassum suits liquid and granular soil use. Choose by crop, purpose and market."),
  ("What is Kappaphycus alvarezii used for in agriculture?", "Its extract is used as a biostimulant in foliar and drip programmes for field and horticultural crops."),
  ("What is the common name of Kappaphycus alvarezii?", "It is a red seaweed often called elkhorn sea moss; its sap is sometimes called K-sap in India."),
  ("What does Ascophyllum nodosum 15 (liquid) mean?", "It is a Schedule VI grade: Ascophyllum nodosum extract at 15% in liquid form.")],
 [("/products/kappaphycus-alvarezii-24-liquid", "Kappaphycus alvarezii 24% liquid", ""), ("/products/ascophyllum-nodosum-15-liquid", "Ascophyllum nodosum 15% liquid", ""), ("/products/sargassum-tenerrimum-10-liquid", "Sargassum tenerrimum 10% liquid", ""), ("/seaweed-extract-manufacturer-india", "All seaweed grades", "")],
 "kappaphycus vs ascophyllum", ["kappaphycus alvarezii uses in agriculture", "kappaphycus alvarezii 24 liquid", "ascophyllum nodosum 15 liquid", "ascophyllum nodosum uses", "sargassum seaweed extract", "kappaphycus alvarezii common name"])

# 8 ------------------------------------------------------------------
art("protein-hydrolysate-vs-amino-acid", "Protein hydrolysate vs amino acid fertilizer: the difference", "Protein Hydrolysate vs Amino Acid Fertilizer: Difference & Uses",
 "How protein hydrolysates and amino acid fertilizers differ, plant vs animal source, and how they are used.",
 "A protein hydrolysate is a mixture of free amino acids and short peptides made by breaking down plant or animal protein; an amino acid fertilizer is specified by its free amino acid content. Both are biostimulants used to support recovery after stress, growth, flowering and fruit set, mostly as foliar sprays or through drip.",
 [("diff", "The difference", table(["", "Protein hydrolysate", "Amino acid grade"], [["Contains", "Free amino acids and peptides", "Specified free amino acid content"], ["Made from", "Plant or animal protein by hydrolysis", "Hydrolysis or fermentation"], ["Our grades", "Plant source 1.5%, 16.9%, 25%, 27%; animal source 36.04%", "Amino acid 5%, 10%, 20%"]])),
  ("source", "Plant source or animal source", "<p>Animal-source hydrolysates, such as those made from collagen, are rich in glycine and proline. Plant-source hydrolysates have a broader amino acid profile and are preferred in some organic and export markets.</p>"),
  ("use", "How they are used", ul(["Foliar sprays after cold, heat, hail or transplanting", "With micronutrients in foliar sprays", "Through drip in early growth", "As a base for brand formulations"], ""))],
 [("Which is better, protein hydrolysate or amino acid?", "Both are used for similar jobs. Choose by concentration, source and cost per acre at the label dose."),
  ("What are the uses of protein hydrolysate in agriculture?", "Supporting recovery after stress, early growth, flowering and fruit set, and complexing micronutrients in sprays."),
  ("Is amino acid fertilizer organic?", "Plant-source products may be accepted in organic programmes depending on the standard; check with your certifier.")],
 [("/amino-acid-protein-hydrolysate-manufacturer-india", "Amino acid manufacturer", ""), ("/products/amino-acid-20", "Amino acid 20%", ""), ("/products/protein-hydrolysate-plant-source-25", "Protein hydrolysate, plant source 25%", "")],
 "protein hydrolysate and amino acid", ["protein hydrolysate uses in agriculture", "amino acid fertilizer uses", "amino acid fertilizer benefits", "plant based vs animal based amino acids", "protein hydrolysate for plants"])

# 9 ------------------------------------------------------------------
art("what-are-zyme-granules", "What are zyme granules? Composition, uses and what to check", "What Are Zyme Granules? Composition, Uses & Price Factors",
 "Zyme granules explained: what they contain, how farmers use them, and what distributors should check after the 2025 biostimulant rules.",
 "Zyme granules are broadcast granules that carry biostimulants such as seaweed extract, humic acid or protein hydrolysate on a granular carrier. Farmers apply them with basal fertilizer or at earthing up to support roots and soil. 'Zyme' is a trade name in India, not a regulated category, so buyers should check the actual grade on the bag.",
 [("contain", "What they contain", "<p>Composition varies widely between brands. Most carry seaweed extract, humic acid, protein hydrolysate or a mix. Since June 2025, biostimulants sold in India must be specified in Schedule VI, so the grade printed on the bag matters.</p>"),
  ("use", "How farmers use them", ul(["Broadcast with basal fertilizer at sowing or planting", "At earthing up or top dressing", "In vegetable and horticulture beds", "Then irrigate to move the material into the root zone"], "")),
  ("price", "What decides the price", "<p>Active content and concentration, the carrier and granule quality, the pack (buckets cost more than bags) and the order size. Compare cost per acre at the label dose, not just the price per kg.</p>"),
  ("ours", "Our granular grades", ul([f'<a href="{grade_path(n, f)}">{esc(n)} ({f.lower()})</a>' for g, n, f in GRADES if f in ("Granular", "Granules")], ""))],
 [("What is the composition of zyme granules?", "It varies by brand: commonly seaweed extract, humic acid or protein hydrolysate on a granular carrier."),
  ("What are zyme granules used for?", "Broadcasting with fertilizer to support root growth and soil conditioning."),
  ("Are zyme granules a fertilizer?", "They are sold as biostimulants rather than nutrient fertilizers, and in India must be a Schedule VI listed grade."),
  ("What is the dose of zyme granules per acre?", "It depends on the grade and concentration. Follow the label.")],
 [("/zyme-granules-manufacturer", "Zyme granules manufacturer", ""), ("/fco-schedule-vi-biostimulants", "FCO Schedule VI", ""), ("/products/humic-acid-plus-seaweed-extract-granules", "Humic + seaweed granules", "")],
 "what are zyme granules", ["zyme granules uses", "zyme granules composition", "zyme granules price", "bio zyme granules", "zyme granules dose per acre"])

# 10 -----------------------------------------------------------------
art("slow-release-vs-water-soluble-fertilizer", "Slow-release vs water-soluble fertilizer: which to use when", "Slow Release vs Water Soluble Fertilizer: Differences & Uses",
 "How slow-release and water-soluble fertilizers differ, where each fits in a crop programme, and how to combine them.",
 "Water-soluble fertilizers dissolve completely and feed the crop quickly through drip or foliar spray, so they suit precise, stage-by-stage feeding. Slow-release fertilizers release nutrients gradually over weeks or months from one basal application, which reduces losses and labour. Many programmes use slow-release as the base and water-soluble grades to fine-tune key stages.",
 [("compare", "Side by side", table(["", "Water-soluble", "Slow-release"], [["Release", "Immediate", "Gradual, over weeks or months"], ["Applied by", "Drip, foliar, fertigation", "Basal or side placement"], ["Strength", "Precise stage feeding", "Fewer applications, lower losses"], ["Watch out for", "Needs frequent application", "Less control over timing"]])),
  ("combine", "Using both", "<p>A practical approach is a slow-release or basal base at planting, then water-soluble grades or fortified special grades through drip at flowering and fruit development.</p>"),
  ("links", "Our ranges", ul(['<a href="/slow-release-fertilizer">Slow-release fertilizers</a>', '<a href="/water-soluble-fertilizer-special-grades">Water-soluble and special grades</a>', '<a href="/custom-fertilizer-blends">Custom blends</a>'], ""))],
 [("What are examples of slow-release fertilizers?", "Coated and organic-matrix granules, low-solubility nitrogen compounds and organic fertilizers."),
  ("Is water-soluble fertilizer better than granular?", "Neither is better overall. Water-soluble grades give precise, fast feeding; granular and slow-release products give a steady base with fewer applications.")],
 [("/slow-release-fertilizer", "Slow-release fertilizers", ""), ("/water-soluble-fertilizer-special-grades", "Water-soluble grades", "")],
 "slow release vs water soluble fertilizer", ["slow release fertilizer examples", "water soluble fertilizer grades", "slow release fertilizer granules", "controlled release fertilizer"])

# 11 -----------------------------------------------------------------
art("can-humic-acid-be-mixed-with-fertilizers-and-pesticides", "Can humic acid be mixed with fertilizers and pesticides?", "Can Humic Acid Be Mixed With NPK, Urea, Fungicide? Guide",
 "A practical compatibility guide for humic acid, seaweed and amino acids with NPK, urea, micronutrients, calcium, fungicides and biofertilisers, with a jar test method.",
 "Humic acid can be mixed with most fertilizers, including NPK, urea, micronutrients and seaweed extract. Avoid mixing it with strongly acidic products or concentrated calcium solutions, which can make it settle out, and always run a jar test before tank-mixing with pesticides. Keep biofertilisers away from chemical fungicides and bactericides.",
 [("table", "Quick guide", table(["Mixing humic acid with", "Usually", "Note"], [
     ["NPK and urea", "Compatible", "Common practice in soil and drip"], ["Micronutrients", "Compatible", "Humic can help keep them available"], ["Seaweed extract and amino acids", "Compatible", "Often sold as ready blends"],
     ["Calcium nitrate and high-calcium solutions", "Caution", "Can flocculate; jar test or apply separately"], ["Strong acids and acidic products", "Avoid", "Humic acid precipitates at low pH"],
     ["Fungicides and insecticides", "Jar test", "Depends on the formulation"], ["Trichoderma and biofertilisers", "Generally compatible with humic", "Never mix biologicals with chemical fungicides"]])),
  ("jar", "How to do a jar test", '<ol><li>Fill a clear jar with water from the source you will spray with, in the same proportion as the tank.</li><li>Add products in the label order, mixing after each.</li><li>Wait 15 to 30 minutes.</li><li>If you see clumps, a layer, sludge or heat, do not mix them in the tank.</li></ol>'),
  ("tips", "Tips", ul(["Fill the tank half with water before adding products", "Spray the mix the same day", "Follow label directions of every product"], ""))],
 [("Can I mix humic acid with NPK?", "Yes. Humic acid is commonly applied with NPK fertilizers."), ("Can I mix humic acid with urea?", "Yes. Humic acid is commonly applied with urea in soil and drip programmes."),
  ("Can I mix humic acid with fungicide?", "Sometimes. It depends on the fungicide formulation, so always run a jar test first."), ("Can I mix humic acid with micronutrients?", "Yes, and humic acid can help keep micronutrients available."),
  ("Can I mix humic acid with calcium nitrate?", "Use caution: high calcium can cause humic acid to flocculate. Jar-test or apply separately."), ("Can humic acid be mixed with Trichoderma?", "Humic acid is generally compatible with Trichoderma and biofertilisers; chemical fungicides are not.")],
 [("/humic-acid-manufacturer-india", "Humic acid manufacturer", ""), ("/resources/humic-acid-uses-in-agriculture", "Humic acid uses", "")],
 "can i mix humic acid with npk", ["can i mix humic acid with urea", "can i mix humic acid with fungicide", "can i mix humic acid with micronutrients", "can i mix humic acid with seaweed extract", "can we mix humic acid with calcium nitrate", "can we mix humic acid with trichoderma"])

# 12 -----------------------------------------------------------------
art("how-to-start-a-fertilizer-brand-private-label", "How to start your own fertilizer brand with private label", "How to Start a Fertilizer Brand: Private Label Guide India",
 "A step-by-step guide to launching an organic fertilizer or biostimulant brand without building a factory: products, compliance, packaging and costs.",
 "You can start a fertilizer or biostimulant brand without a factory by working with a private-label manufacturer: choose products and grades, get the authorisations needed to sell in your market, approve samples and label design, and have the manufacturer produce and pack under your brand. In India, biostimulants must be Schedule VI listed grades.",
 [("steps", "Step by step", '<ol><li><strong>Choose your market and crops.</strong> Who will buy, where, and what problem you solve.</li><li><strong>Pick products.</strong> Start with three to five proven grades, for example humic, seaweed and amino acid.</li><li><strong>Check compliance.</strong> In India, selling fertilizers and biostimulants needs state authorisation under the FCO, and biostimulants must be listed grades. Abroad, check your country\'s registration rules.</li><li><strong>Get samples and test.</strong> Run field trials and lab checks.</li><li><strong>Design labels and packs.</strong> Include the grade, batch, dates and manufacturer details your rules require.</li><li><strong>Place the first order.</strong> With no minimum order, start small.</li><li><strong>Build demand.</strong> Field demonstrations, farmer meetings and dealer networks.</li></ol>'),
  ("cost", "What it costs", "<p>The main costs are product, packaging and label printing, registration or authorisation fees, and marketing. Starting with existing listed grades avoids development cost and speeds up launch.</p>"),
  ("partner", "Choosing a manufacturer", ul(["Holds approvals for the grades you want", "Accepts small first orders", "Can pack in the sizes your market buys", "Gives specification sheets and test reports", "Has R&amp;D to build custom products later"], ""))],
 [("Do I need a licence to sell fertilizer under my brand in India?", "Yes. Selling fertilizers and biostimulants needs authorisation from the state agriculture department under the Fertiliser Control Order. Check current requirements with your state department."),
  ("What is the minimum order for private label?", "With us there is no fixed minimum order quantity."), ("How long does a private-label launch take?", "Once samples, label and pack are approved, production is about one week."),
  ("What is white label fertilizer?", "Another term for private label: a manufacturer's product sold under your brand.")],
 [("/private-label-oem", "Private label and OEM", ""), ("/custom-fertilizer-blends", "Custom blends", ""), ("/resources/choosing-a-biostimulant-manufacturer-checklist", "Manufacturer checklist", "")],
 "how to start fertilizer brand", ["private label fertilizer", "white label fertilizer", "private label liquid fertilizer", "third party fertilizer manufacturing india", "fertilizer label requirements", "start organic fertilizer business"], "Entrepreneurs, brand owners, distributors")

# 13 -----------------------------------------------------------------
art("how-to-import-biostimulants-from-india", "How to import biostimulants and fertilizers from India", "How to Import Biostimulants From India: Steps & Documents",
 "A practical guide for importers: sampling, registration, quotes and Incoterms, documents and shipping from Indian ports.",
 "To import biostimulants from India, shortlist a manufacturer, test samples, register the product in your country if required, agree the price and Incoterm (usually FOB or CIF), and receive the goods with a commercial invoice, packing list, certificate of origin, test report or certificate of analysis, safety data sheet and bill of lading.",
 [("steps", "Steps", '<ol><li>Shortlist manufacturers and request specification sheets.</li><li>Order free samples and test them.</li><li>Register the product in your country if required.</li><li>Agree price, packing, Incoterm and payment terms; receive a proforma invoice.</li><li>Production and pre-shipment testing; third-party inspection if you need it.</li><li>Shipment from the Indian port with export documents.</li></ol>'),
  ("docs", "Documents usually needed", ul(["Commercial invoice and packing list", "Certificate of origin", "Certificate of analysis or test report", "Safety data sheet (SDS/MSDS)", "Bill of lading or airway bill", "Any import permit or registration your country requires"], "")),
  ("ports", "Ports and Incoterms", "<p>We ship from Pipavav, Kandla, Dahej, Mundra, JNPT and other Indian ports, FOB or CIF. Liquids travel in drums or IBCs, solids in bags or jumbo bags, or in your private-label retail packs.</p>")],
 [("Do you supply samples to importers?", "Yes, free. Freight or courier, customs duty and other charges are paid by the buyer."), ("Which countries do you export to?", "GCC countries, Africa, the Russian Federation, Europe, North America and South America."),
  ("Can you pack under my brand for export?", "Yes. We pack under your private label in the sizes your market buys.")],
 [("/export", "Export terms", ""), ("/private-label-oem", "Private label", ""), ("/quality-compliance", "Quality and documents", "")],
 "import biostimulants from india", ["humic acid supplier india export", "seaweed extract exporter india", "biostimulant exporter india", "fertilizer import documents"], "Importers")

# 14 -----------------------------------------------------------------
art("types-of-biofertilizers", "Types of biofertilizers: names, examples and uses", "Types of Biofertilizers: Names, Examples & Uses",
 "A list of biofertilizer types, Azotobacter, Rhizobium, Azospirillum, Acetobacter, PSB, KMB, ZSB and mycorrhizae, with what each does and how to apply them.",
 "Biofertilizers are products containing living micro-organisms that supply or release nutrients. The main types are nitrogen fixers (Azotobacter, Azospirillum, Acetobacter, Rhizobium), phosphate solubilisers (PSB and fungi), potash mobilisers (KMB), zinc solubilisers (ZSB), mycorrhizal fungi and consortia that combine several of them.",
 [("list", "Biofertilizer names and uses", table(["Biofertilizer", "What it does", "Main crops"], [[f'<a href="{BIO_INFO[b][0]}">{esc(b)}</a>', BIO_INFO[b][2], ", ".join(BIO_INFO[b][3])] for b in BIOS])),
  ("apply", "How to apply", ul(["Seed treatment before sowing", "Seedling root dip before transplanting", "Soil application mixed with compost or farmyard manure", "Drip application for liquid forms"], "")),
  ("tips", "Getting results", ul(["Use fresh product within shelf life", "Store cool and out of sunlight", "Keep away from chemical fungicides and bactericides", "Apply into moist soil with organic matter"], ""))],
 [("What is a biofertilizer?", "A product containing living micro-organisms that supply nutrients such as nitrogen or make soil nutrients easier for the crop to take up."), ("What are examples of biofertilizers?", "Azotobacter, Azospirillum, Rhizobium, Acetobacter, phosphate solubilising bacteria, potash mobilising bacteria, zinc solubilising bacteria and mycorrhizae."),
  ("What is biofertilizer in Hindi?", "It is called jaivik khad or jaiv urvarak (जैव उर्वरक)."), ("Is liquid biofertilizer better than carrier-based?", "Liquid forms usually keep a longer shelf life and suit drip; carrier forms suit seed and soil application with compost.")],
 [("/biofertilisers-manufacturer-india", "Biofertiliser manufacturer", ""), ("/resources/biostimulant-vs-fertilizer-vs-biofertilizer", "Biostimulant vs biofertilizer", "")],
 "types of biofertilizers", ["bio fertilizer names list", "bio fertilizer example", "bio fertilizer meaning", "bio fertilizer in hindi", "bio fertilizer products", "liquid biofertilizer"])

# 15 -----------------------------------------------------------------
art("micronutrient-deficiency-symptoms-in-crops", "Micronutrient deficiency symptoms in crops: a field guide", "Micronutrient Deficiency Symptoms in Crops: Zinc, Boron, Iron",
 "How to recognise zinc, boron, iron, manganese, copper and molybdenum deficiency in crops, and what growers do about it.",
 "Micronutrient deficiencies show as specific leaf and fruit symptoms: zinc causes small leaves and shortened internodes, boron causes flower drop and deformed fruit, iron and manganese cause yellowing between veins on young leaves. Symptoms on young leaves point to immobile nutrients. Confirm with a soil or leaf test before treating.",
 [("table", "Symptoms by nutrient", table(["Nutrient", "Where it shows", "Typical symptoms"], [["Zinc", "Young leaves", "Small leaves, short internodes, pale stripes or patches"], ["Boron", "Growing points, flowers, fruit", "Flower and fruit drop, hollow or cracked fruit, dieback of tips"], ["Iron", "Young leaves", "Yellowing between veins, veins stay green"], ["Manganese", "Young and middle leaves", "Interveinal yellowing with small dead spots"], ["Copper", "Young leaves and shoots", "Dieback, distorted young leaves"], ["Molybdenum", "Older leaves, legumes", "Pale, cupped leaves; poor nodulation in legumes"]])),
  ("mobile", "Young leaves or old leaves?", "<p>Nutrients that cannot move within the plant, such as iron, zinc, manganese, copper, boron and calcium, show deficiency first on young growth. Mobile nutrients such as nitrogen, phosphorus, potassium and magnesium show first on older leaves.</p>"),
  ("fix", "What growers do", ul(["Confirm with a soil or leaf test", "Correct soil pH where it locks nutrients up", "Use chelated forms for foliar and drip on high-pH soils", "Apply humic acid to help keep micronutrients available"], ""))],
 [("Which micronutrient deficiency is most common in India?", "Zinc deficiency is the most widespread, followed by boron, iron and manganese in many regions."), ("How can micronutrient deficiency be corrected?", "Confirm with a test, then apply the right micronutrient to soil, by foliar spray or by drip, using chelated forms where pH limits availability.")],
 [("/micronutrient-fertilizer-manufacturer-india", "Micronutrient fertilizers", ""), ("/products/zinc-solubilising-bacteria", "Zinc solubilising bacteria", "")],
 "micronutrient deficiency symptoms", ["zinc deficiency symptoms in plants", "boron deficiency in plants", "iron deficiency in plants", "micronutrient fertilizer uses"])

# 16 -----------------------------------------------------------------
art("choosing-a-biostimulant-manufacturer-checklist", "Choosing a biostimulant manufacturer: a buyer's checklist", "How to Choose a Biostimulant Manufacturer in India: Checklist",
 "Twelve questions distributors, brands and importers should ask before choosing a biostimulant or organic fertilizer manufacturer.",
 "Choose a biostimulant manufacturer that holds approvals for the exact grades you want, runs its own plant, shares specification sheets and test reports, accepts trial orders, packs in the sizes your market buys, and has R&D to develop products with you. Visit the plant or arrange third-party inspection before large orders.",
 [("list", "The checklist", '<ol><li>Does it hold approval for each grade (in India, Schedule VI listing and state authorisation)?</li><li>Does it own the plant, or is it a trader?</li><li>What is its monthly capacity?</li><li>Will it share specification sheets and recent test reports?</li><li>Will it allow third-party sampling and testing?</li><li>Is there a minimum order quantity?</li><li>Which pack sizes can it fill?</li><li>What is the lead time?</li><li>Can it pack under your brand?</li><li>Does it have R&amp;D for custom products?</li><li>Can it export with the documents your country needs?</li><li>Are its company details (CIN, GST, address) verifiable?</li></ol>'),
  ("us", "How we answer it", '<p>Our answers are on the <a href="/quality-compliance">Quality and compliance</a>, <a href="/manufacturing-facility">Manufacturing</a> and <a href="/research-development">R&amp;D</a> pages.</p>')],
 [("What is the difference between a manufacturer and a trader?", "A manufacturer owns the plant and controls formulation and quality; a trader buys from manufacturers. Ask for the factory address and visit if you can."),
  ("Why do Schedule VI approvals matter?", "Since June 2025 only Schedule VI listed biostimulants can be sold in India, so stock of unlisted products cannot be sold.")],
 [("/quality-compliance", "Quality and compliance", ""), ("/manufacturing-facility", "Manufacturing facility", ""), ("/fco-schedule-vi-biostimulants", "FCO Schedule VI", "")],
 "biostimulant manufacturers in india", ["biostimulant companies in india", "biostimulant manufacturing companies", "organic fertilizer manufacturer india", "how to choose fertilizer supplier"], "Distributors, brands, importers")

# ---------------------------------------------------------------- RESOURCES HUB
rh = hero("Knowledge centre", "Plain answers to the questions growers, distributors, brands and importers ask us about biostimulants, organic fertilizers and biofertilisers.", [("Knowledge centre", None)])
rh += sec(answer("Our knowledge centre explains biostimulants, organic and specialty fertilizers and biofertilisers in plain language: what they are, how they differ, how to use them and how to buy them, written by the Gujarat Bio Organics R&D team.")
          + "<p>Start with the guide that matches your question. If you are new to the category, read what a biostimulant is and how it differs from a fertilizer. If you are comparing materials, the humic acid, seaweed extract, amino acid and biofertiliser guides explain what each does in the field and what to check on a label. If you are buying, the guides on choosing a manufacturer, private label and the FCO Schedule VI rules cover what to ask a supplier before you order. Each guide is written in plain language and links to the product pages and crop programmes where the material is used. The glossary and FAQ answer short questions in a line or two.</p>"
          + "<h2>Guides</h2>" + hub([(p, h, d) for p, h, d in ARTICLES] + [("/fco-schedule-vi-biostimulants", "FCO Schedule VI biostimulants", "How India regulates biostimulants and what buyers should check."),
                                                       ("/glossary", "Glossary", "Terms from biostimulant to Schedule VI, explained in a line or two."),
                                                       ("/faq", "Frequently asked questions", "The most common questions in one place.")]))
page("/resources", "Knowledge Centre: Biostimulants, Humic Acid, Seaweed | GBO", "Guides on biostimulants, humic acid, seaweed extract, amino acids, biofertilisers, micronutrients and private-label fertilizer brands from Gujarat Bio Organics.",
     rh + cta(), [("Knowledge centre", None)], [itemlist_ld("Guides", [(p, h) for p, h, _ in ARTICLES])], "0.8")
kw("/resources", "biostimulant guide", ["humic acid guide", "seaweed extract guide", "organic fertilizer knowledge"], [], "Informational", "All")
