# "Why we are different": source, gentle process, proof. Positioning page for humic acid, seaweed extract and amino acids.
df_faq = [
    ("What makes Gujarat Bio Organics' humic acid different from other humic acid?", "Three things: the raw material we chose after about 20 years of comparing sources in the field, an extraction process that avoids extreme alkali and heat, and batch-by-batch quality control. Our R&D found that humic material holds beneficial substances that are easily damaged by high pH and high temperature, so we protect them."),
    ("Why do pH and temperature matter when making humic acid?", "Humic substances are a complex mixture. Our R&D found that some of the beneficial fractions are fragile, and that very high pH and very hot processing can damage them. A product can still test as humic acid on paper and carry less of what helps the plant."),
    ("Is all seaweed extract the same?", "No. Thousands of seaweed species exist and only a few suit agriculture. Cultivation, harvest timing, post-harvest handling, storage and extraction each affect what ends up in the bottle. A careless step can turn a rich extract into a plain seaweed powder."),
    ("Which seaweeds do you use?", "Our grades use Ascophyllum nodosum, Kappaphycus alvarezii, Sargassum and Spirulina, chosen for agricultural use. The grade pages list each one."),
    ("Which amino acid source is best for agriculture?", "It depends on the purpose, which is why we make both plant-source and animal-source grades. What matters as much is the hydrolysis method, preservation, formulation and quality control behind them."),
    ("Will you share your exact process and raw material?", "We keep our sources and process settings private because they are the result of 20 years of work. We do share specification sheets and third-party test reports, send free samples for your own lab or field trial, and welcome plant visits."),
    ("Do you promise higher yields?", "No. Results vary with crop, soil, weather and practice. We encourage a side-by-side trial on your own farm, and growers describe their own experience in our videos."),
]

def _why_card(anchor, t, items):
    return (f'<div class="hub-i" id="{anchor}"><h3>{t}</h3>' + ul(items) + '</div>')

dfb = hero("Why our products are not like the rest",
           "Humic acid, seaweed extract and amino acids can look the same in a drum. They do not behave the same in the field. The difference is decided by the raw material, the process and the proof behind each batch.",
           [("Why Gujarat Bio Organics", None)])
dfb += sec(answer("Gujarat Bio Organics' humic acid, seaweed extract and amino acid products differ from low-cost bulk powders in three ways. We chose our raw materials through about 20 years of field comparison. We extract gently, protecting fragile compounds from extreme pH and heat. And we control quality at every step so each batch carries the goodness the raw material started with.")
           + '<div class="hub">'
           + '<div class="hub-i"><h3>1. The right raw material</h3><p>Hundreds of sources exist. Two decades of work on real farms taught us what separates a good one from a bad one.</p></div>'
           + '<div class="hub-i"><h3>2. A gentle process</h3><p>Our extraction is designed to protect the delicate compounds that harsh, hot, high-pH processing damages.</p></div>'
           + '<div class="hub-i"><h3>3. Proof, batch by batch</h3><p>Protocols at every step, quality control, and documents and samples you can test yourself.</p></div></div>')

dfb += sec('<div class="prose">'
    '<p>There are hundreds of sources of humic raw material in the world, and they are far from equal. We have spent about 20 years working with growers to see, season after season, what separates a good source from a poor one. We use the source that proved itself in the field.</p>'
    '<p>Extraction matters just as much. Much low-cost bulk humic powder is made with strong alkali, very high pH and very high temperatures. Our research found that humic material contains beneficial substances that are still not fully identified by science, and that these are fragile against high pH and heat. We developed our extraction technology to protect them and to bring out the most benefit.</p>'
    '<p>The result is a humic acid made for what happens in the soil and around the root, not only for a number on a specification sheet.</p>'
    '</div>' + links([("/humic-acid-manufacturer-india", "Our humic acid grades", "Liquid, powder, granular"), ("/zyme-granules-manufacturer", "Zyme granules", "Humic, seaweed and protein granules")]),
    "Humic acid: source and gentle extraction")

dfb += sec('<div class="prose">'
    '<p>Thousands of seaweed species grow in the world. Only a few suit farming. Even fewer people know how to cultivate them, when to harvest, how to treat and store them after harvest, and how to extract them without losing what makes them valuable. A mistake at any one of these steps can ruin the extract.</p>'
    '<p>Good seaweed extract is not just alginic acid in a tea. It holds a complex mix of minerals, amino acids, colloids, phytochemicals, natural plant growth regulators, enzymes and other biochemicals. When handling is careless, all of that is lost and what is left is a plain coloured seaweed powder, black, brown, green or red, sold in bulk on price alone.</p>'
    '<p>We follow our own protocol at every step so that the goodness of the seaweed reaches the plant and the soil. Our grades use Ascophyllum nodosum, Kappaphycus alvarezii, Sargassum and Spirulina.</p>'
    '</div>' + links([("/seaweed-extract-manufacturer-india", "Our seaweed extract grades", "Ascophyllum, Kappaphycus, Sargassum, Spirulina")]),
    "Seaweed extract: species, handling and extraction", cls="tint")

dfb += sec('<div class="prose">'
    '<p>Amino acids and protein hydrolysates raise the same questions. Which source suits agriculture? Which hydrolysis method keeps the amino acids and peptides intact? How should the product be preserved, formulated and tested? We answer these through our own selection of sources, methods and quality control, and we make both plant-source and animal-source grades for different purposes.</p>'
    '<p>That is what stands our products apart from imported powders that are made to a price.</p>'
    '</div>' + links([("/amino-acid-protein-hydrolysate-manufacturer-india", "Our amino acid and protein hydrolysate grades", "Plant and animal source")]),
    "Amino acids: source, hydrolysis and preservation")

dfb += sec(table(["Question to ask any supplier", "Why it matters", "What we offer"], [
    ["Where does the raw material come from, and is it the same every batch?", "Source drives quality and consistency.", "Raw material chosen after about 20 years of field comparison"],
    ["How hot and how alkaline is the extraction?", "Heat and high pH can damage fragile compounds.", "A gentle process built to protect them. Settings kept private."],
    ["How is each batch tested?", "Paper claims are not proof.", "In-house batch checks and third-party testing on request"],
    ["Can I see a specification sheet and an independent test report?", "You should verify, not trust.", "Specification sheet and third-party report on request"],
    ["Can I test a sample and run a trial?", "Your crop and conditions decide.", "Free samples (buyer pays freight, duty and other charges)"],
    ["Can I visit the plant?", "Seeing is believing.", "Plant visits and third-party sampling arranged in advance"],
]) + '<p class="mute" style="margin-top:1rem">We do not publish our sources or process settings, because they are the result of two decades of work. We invite you to test the product instead.</p>',
    "Do not take our word for it. Ask these questions of every supplier.", "Compare on proof, not on price per tonne.", cls="tint")

dfb += sec('<div class="split"><div><h3>See it on real farms</h3><p>Our products were developed with growers over about 20 years, across crops and regions. Growers share their own experience in videos.</p>'
           '<div class="btn-row"><a class="btn btn-dark" href="/impact">The field record</a><a class="btn btn-ghost" href="/research-development">Our R&amp;D</a></div></div>'
           '<div><h3>Try it yourself</h3><p>Ask for a free sample. Test it in your lab, or run a side-by-side trial on your crop.</p>' + quote_btns("Hello Gujarat Bio Organics, I would like a free sample to compare with my current supplier.") + '</div></div>' + CLAIM_NOTE)
dfb += sec(faq_html(df_faq) + links([("/humic-acid-manufacturer-india", "Humic acid", ""), ("/seaweed-extract-manufacturer-india", "Seaweed extract", ""), ("/amino-acid-protein-hydrolysate-manufacturer-india", "Amino acids", ""), ("/research-development", "Research and development", ""), ("/quality-compliance", "Quality and compliance", "")]), "Questions about what makes us different")

page("/why-gujarat-bio", "Why Choose Our Humic Acid, Seaweed & Amino Acid | GBO",
     "Why Gujarat Bio Organics humic acid, seaweed extract and amino acids differ: field-chosen raw materials, gentle extraction, and proof you can test. Ask for a sample.",
     dfb + cta("Compare us with your current supplier", "Ask for a free sample and test it yourself. No minimum order.", "Hello Gujarat Bio Organics, I would like a free sample to compare with my current supplier."),
     [("Why Gujarat Bio Organics", None)], [faq_ld(df_faq), article_ld("/why-gujarat-bio", "Why Gujarat Bio Organics humic acid, seaweed extract and amino acids are different", "Raw material selection, gentle extraction and batch quality control.")], "0.9")
kw("/why-gujarat-bio", "best humic acid manufacturer in india", ["how is humic acid made", "good quality seaweed extract", "how to choose humic acid supplier", "seaweed extract quality", "high pH humic acid damage", "best amino acid for agriculture"],
   [q for q, _ in df_faq], "Commercial / differentiation", "Importers, brand owners, distributors")
