# Company and authority pages: R&D, manufacturing, FCO Schedule VI explainer.

# ---------------------------------------------------------------- R&D
rd_faq = [("Does Gujarat Bio Organics have in-house R&D?", "Yes. Our R&D team works on formulation, stability, compatibility and crop programmes, and on custom products for brands and importers."),
          ("Can your R&D team formulate a product for my market?", "Yes. Send the crop, market, application method and target specification, or your own formula. We propose a composition and make a sample batch."),
          ("Do you run field trials?", "Our crop programmes come from field work with growers. For brand owners we can support trials with samples and application guidance."),
          ("Can I get stability and specification data?", "Specification sheets and third-party test reports are available on request.")]
rd = hero("Research and development", "Twenty years of formulation work and field trials with growers, behind every grade we make and every product we build for your brand.", [("Research and development", None)])
rd += sec(answer("Gujarat Bio Organics' in-house R&D team develops and improves biostimulant, biofertiliser and specialty fertilizer formulations, checks their stability and compatibility, and builds crop programmes from field work with growers. The same team formulates custom products for private-label brands and importers.")
          + '<div class="kpis"><div><b>20 years</b><span>of R&amp;D and field work</span></div><div><b>36 + 11</b><span>biostimulant grades and biofertiliser types</span></div><div><b>3 forms</b><span>liquid, powder and granule</span></div><div><b>8 crops</b><span>with dedicated programmes</span></div></div>')
rd += sec('<div class="hub">' + "".join(f'<div class="hub-i"><h3>{t}</h3><p>{d}</p></div>' for t, d in [
    ("Formulation", "Turning raw materials into stable liquids, soluble powders and granules at the concentration each grade specifies."),
    ("Stability and shelf life", "Checking that products stay uniform and effective in storage, in heat and through transport."),
    ("Compatibility", "Testing how our products behave in the tank with fertilizers and other inputs, so the field advice we give holds up."),
    ("Crop programmes", "Combining nutrition, biostimulants and biologicals into stage-by-stage programmes for each crop."),
    ("Field work", "Working with growers on their farms to see what solves the problem they actually have."),
    ("Custom products", "Formulating to a brand's brief or an importer's registration specification."),
]) + "</div>", "What our R&amp;D team does")
rd += sec('<div class="prose">'
    "<p>Each product family rests on a different process, and getting the process right is what makes a grade consistent from batch to batch.</p>"
    "<h3>Humic and fulvic substances</h3><p>Humic acids are separated from humified organic material, and potassium humate is produced by neutralising humic acid with potassium so it dissolves in water. Fulvic fractions stay soluble across the pH range.</p>"
    "<h3>Seaweed and algae extracts</h3><p>Seaweed is processed to break open the cells and release soluble compounds, which are then concentrated to the specified extract content. Different species, Ascophyllum, Kappaphycus, Sargassum and Spirulina, give different profiles.</p>"
    "<h3>Protein hydrolysates and amino acids</h3><p>Proteins from plant or animal sources are broken down by hydrolysis into free amino acids and peptides. The source and the process shape the amino acid profile.</p>"
    "<h3>Granulation</h3><p>Granules carry biostimulants into the soil with basal fertilizer, so granule strength, size and dispersion in the field matter as much as the active content.</p>"
    "<h3>Biofertilisers</h3><p>Biofertilisers are produced by culturing selected micro-organisms and formulating them in liquid or on a carrier so they survive storage and work in the soil.</p>"
    "</div>", "The process families we work with", cls="tint")
rd += sec(faq_html(rd_faq) + links([("/custom-fertilizer-blends", "Custom blends", "Formulated to your brief"), ("/manufacturing-facility", "Manufacturing facility", ""),
                                     ("/quality-compliance", "Quality and compliance", ""), ("/crops", "Crop programmes", ""), ("/private-label-oem", "Private label and OEM", ""), ("/resources", "Knowledge centre", "")]), "R&amp;D questions")
page("/research-development", "In-House R&D: Biostimulant & Fertilizer Formulation | GBO",
     "Our in-house R&D team formulates biostimulants, biofertilisers and specialty fertilizers, tests stability and compatibility, and builds crop programmes.",
     rd + cta("Have a product idea?", "Send the brief. Our R&D team proposes a formulation and a sample.", "Hello Gujarat Bio Organics, I have a product idea for my market."),
     [("Research and development", None)], [faq_ld(rd_faq)], "0.7")
kw("/research-development", "biostimulant formulation company india", ["fertilizer r&d company", "biostimulant manufacturing process", "in house r&d biostimulants", "custom formulation biostimulants"], [q for q, _ in rd_faq], "Commercial / trust", "Brand owners, importers")

# ---------------------------------------------------------------- MANUFACTURING
mf_faq = [("Where is your factory?", f"Our plant is at {FACTORY}, India."),
          ("What is your production capacity?", "100 KL of liquid products and 2,500 tonnes of granular and solid products per month."),
          ("What pack sizes can you fill?", f"Liquids: {PACKS_L}. Solids: {PACKS_S}."),
          ("How fast can you dispatch?", "About one week from confirmed order, for regular grades."),
          ("Can I visit the plant or send an inspector?", "Yes. Plant visits and third-party sampling and testing can be arranged in advance.")]
mf = hero("Manufacturing facility, Shihor, Bhavnagar", "Liquid, powder, granule and biofertiliser production under one roof in GIDC Shihor, Gujarat, with packing from 250 mL bottles to 1000 L IBCs and jumbo bags.", [("Manufacturing", None)])
mf += sec(answer(f"Gujarat Bio Organics manufactures at its own plant at {FACTORY}. The plant has capacity for 100 KL of liquid and 2,500 tonnes of solid products each month, with in-house packing for retail, private-label and bulk orders.")
          + '<div class="kpis"><div><b>100 KL</b><span>liquid per month</span></div><div><b>2,500 t</b><span>solid and granular per month</span></div><div><b>1 week</b><span>typical dispatch</span></div><div><b>No MOQ</b><span>trial orders welcome</span></div></div>')
mf += sec('<div class="hub">' + "".join(f'<div class="hub-i"><h3>{t}</h3><p>{d}</p></div>' for t, d in [
    ("Liquid formulation and filling", "Seaweed, humic, fulvic, amino acid and blended liquids, filled from 250 mL bottles to 220 L drums and 1000 L IBCs."),
    ("Powder blending and packing", "Soluble humate, humic, amino and blended powders, packed in bags and buckets."),
    ("Granulation", "Humic, seaweed and protein granules for broadcast, from 1 kg buckets to 1000 kg jumbo bags."),
    ("Biofertiliser production", "Liquid and carrier-based biofertilisers and consortia."),
    ("Private-label packing", "Your label, your pack design, your carton, packed on our lines."),
    ("Quality control", "Batch checks in-house, with third-party sampling and testing available on request."),
]) + "</div>", "What happens in the plant")
mf += sec(spec([("Address", FACTORY), ("Liquid packs", PACKS_L), ("Solid packs", PACKS_S), ("Ports", "Pipavav, Kandla, Dahej, Mundra, JNPT and all Indian ports"),
                ("Incoterms", "FOB or CIF"), ("Documents", "Specification sheet, NOC copy and third-party test report on request")]) +
          '<div class="gal three" style="margin-top:2rem">' + img("granules-pile", "Pile of black humic granules", caption="Granules, loose. Illustrative.") +
          img("private-label-premium-enriched", "Retail bottles of seaweed and humic liquid", caption="Private-label retail packs. Illustrative.") +
          img("humic-acid-51-granular", "Humic acid granules", caption="Humic acid 51% granular. Illustrative.") + "</div>", "Plant and dispatch details", cls="tint")
mf += sec(faq_html(mf_faq) + links([("/research-development", "Research and development", ""), ("/quality-compliance", "Quality and compliance", ""), ("/bulk-supply", "Bulk supply", ""),
                                     ("/export", "Export", ""), ("/private-label-oem", "Private label", ""), ("/contact", "Arrange a visit", "")]), "Facility questions")
page("/manufacturing-facility", "Fertilizer & Biostimulant Manufacturing Plant, Gujarat | GBO",
     "Gujarat Bio Organics' plant in GIDC Shihor, Bhavnagar: 100 KL liquid and 2,500 t solid monthly capacity, granulation, biofertilisers and private-label packing.",
     mf + cta(), [("Manufacturing", None)], [faq_ld(mf_faq)], "0.7", "/assets/img/granules-pile.webp")
kw("/manufacturing-facility", "biostimulant manufacturing plant india", ["fertilizer manufacturing plant gujarat", "humic acid manufacturing plant", "third party fertilizer manufacturing", "contract manufacturing biostimulants"], [q for q, _ in mf_faq], "Commercial / trust", "Brand owners, importers")

# ---------------------------------------------------------------- FCO SCHEDULE VI
fco_faq = [("What is Schedule VI of the Fertiliser Control Order?", "Schedule VI is the part of India's Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985 that specifies biostimulants: the product, its composition and the standards it must meet before it can be sold."),
           ("When did biostimulants come under the FCO?", "Biostimulants were brought under the FCO by notification S.O. 882(E) dated 23 February 2021, which introduced a provisional registration period."),
           ("What happened to provisional registrations?", "Industry reports state that provisional registrations ended in June 2025 after several extensions, and that only biostimulants specified in Schedule VI may now be sold."),
           ("How many biostimulants are approved?", "Industry reporting from September 2025 put the number of fully approved products in Schedule VI at 146, with more than 9,000 provisional registrations cancelled. Check the latest Gazette notifications for the current list."),
           ("Which categories count as biostimulants?", "The FCO definition covers categories such as botanical extracts including seaweed extracts, bio-chemicals, protein hydrolysates and amino acids, vitamins, cell-free microbial products, antioxidants, anti-transpirants, humic and fulvic acids, and live micro-organisms other than biofertilisers and biopesticides."),
           ("Are biofertilisers covered by Schedule VI?", "No. Biofertilisers are specified separately in Schedule III of the FCO."),
           ("What should a distributor or brand check before buying?", "That the exact grade on the label is specified in Schedule VI, that the seller holds the state authorisation to sell it, and that specification sheets and test reports are available."),
           ("Which grades does Gujarat Bio Organics hold?", "Our No Objection Certificate from the Directorate of Agriculture, Government of Gujarat covers 36 Schedule VI biostimulant grades and 11 Schedule III biofertiliser types.")]
fco = hero("FCO Schedule VI biostimulants: what buyers need to know", "How India regulates biostimulants, what changed in 2025, and what distributors, brands and importers should check before they buy.", [("Knowledge centre", "/resources"), ("FCO Schedule VI", None)])
fco += sec('<div class="prose">' + answer("In India, biostimulants are regulated under Schedule VI of the Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985. Since provisional registrations ended in June 2025, only biostimulants specified in Schedule VI can be sold, so buyers should check that every grade they buy is a listed grade.") +
    '<p class="meta-line">By the Gujarat Bio Organics R&amp;D team. Updated October 2026.</p>'
    '<div class="toc"><strong>On this page</strong><ol><li><a href="#timeline">Timeline</a></li><li><a href="#categories">What counts as a biostimulant</a></li><li><a href="#buyers">What buyers should check</a></li><li><a href="#gbo">Our approved grades</a></li><li><a href="#sources">Sources</a></li></ol></div>'
    '<h2 id="timeline">Timeline</h2>' + table(["Date", "What happened"], [
        ["23 February 2021", "Notification S.O. 882(E) brings biostimulants under the Fertiliser Control Order and adds Clause 20C, with provisional registration (the G3 certificate) for existing products."],
        ["2023 to 2025", "Provisional registration is extended several times, to February 2023, February 2024, February 2025 and finally 16 June 2025."],
        ["26 May 2025", "A Gazette notification updates Schedule VI with approved biostimulant entries and their specifications."],
        ["17 June 2025", "Provisional registrations end. Industry reporting puts the number cancelled at 9,352."],
        ["September 2025", "Industry reporting puts the number of fully approved products listed in Schedule VI at 146."]]) +
    '<h2 id="categories">What counts as a biostimulant</h2><p>The FCO describes a biostimulant as a substance or micro-organism that stimulates physiological processes in plants, improving nutrient uptake, growth, yield, nutrition efficiency, crop quality or stress tolerance, regardless of its nutrient content. It covers categories such as:</p>' +
    ul(["Botanical extracts, including seaweed extracts", "Bio-chemicals", "Protein hydrolysates and amino acids", "Vitamins", "Cell-free microbial products",
        "Antioxidants", "Anti-transpirants", "Humic and fulvic acids and their derivatives", "Live micro-organisms other than biofertilisers and biopesticides"], "") +
    '<p>Biofertilisers are regulated separately under Schedule III, and pesticides under the Insecticides Act.</p>'
    '<h2 id="buyers">What distributors, brands and importers should check</h2>' +
    ul(["The exact grade name and concentration on the label matches an entry in Schedule VI", "The manufacturer or seller holds the state authorisation to sell that grade",
        "A specification sheet and a recent test report are available for the batch", "Label claims stay within what the grade is approved for",
        "For private label, the manufacturer can supply the grade under your brand within the rules"]) +
    '<h2 id="gbo">Our approved grades</h2><p>The Directorate of Agriculture, Government of Gujarat has issued Gujarat Bio Organics a No Objection Certificate covering <a href="/biostimulants-manufacturer-india">36 Schedule VI biostimulant grades</a> and <a href="/biofertilisers-manufacturer-india">11 Schedule III biofertiliser types</a>. Each grade has its own page on this site, and copies of the NOC are available on request.</p>'
    '<h2 id="sources">Sources</h2><ul><li><a href="https://www.global-agriculture.com/india-region/india-ends-provisional-registration-of-biostimulants-only-146-products-now-approved-under-fco-9352-products-cancelled/" rel="noopener">Global Agriculture: India ends provisional registration of biostimulants (September 2025)</a></li>'
    '<li><a href="https://sundayguardianlive.com/business/india-unveils-biostimulant-rules-sets-global-benchmark-136238/" rel="noopener">Sunday Guardian: India unveils biostimulant rules (July 2025)</a></li>'
    '<li><a href="https://www.global-agriculture.com/india-region/regulation-of-biostimulant-products-under-fertilizer-control-order-fco-1985/" rel="noopener">Global Agriculture: Regulation of biostimulant products under FCO 1985</a></li></ul>'
    '<p class="note-box">This page is a plain-language summary for buyers, not legal advice. Check the latest Gazette notifications or your state agriculture department for current rules.</p></div>')
fco += sec(faq_html(fco_faq) + links([("/biostimulants-manufacturer-india", "Our 36 biostimulant grades", ""), ("/quality-compliance", "Quality and compliance", ""), ("/zyme-granules-manufacturer", "Granules made from listed grades", ""),
                                       ("/resources/what-is-a-biostimulant", "What is a biostimulant?", "Guide"), ("/private-label-oem", "Private label within the rules", ""), ("/become-a-distributor", "Distributors", "")]), "Schedule VI questions", cls="tint")
page("/fco-schedule-vi-biostimulants", "FCO Schedule VI Biostimulants: Rules & Approved Grades | GBO",
     "How India regulates biostimulants under FCO Schedule VI, what changed when provisional registrations ended in June 2025, and what buyers should check.",
     fco + cta("Buy only listed grades.", "Ask for our NOC copy and the grade list.", "Hello Gujarat Bio Organics, please send your NOC copy and grade list."),
     [("Knowledge centre", "/resources"), ("FCO Schedule VI", None)], [faq_ld(fco_faq), article_ld("/fco-schedule-vi-biostimulants", "FCO Schedule VI biostimulants: what buyers need to know", "How India regulates biostimulants under FCO Schedule VI.")], "0.8")
kw("/fco-schedule-vi-biostimulants", "fco schedule vi biostimulants", ["biostimulant registration india", "biostimulant fco approval", "schedule vi biostimulant list", "provisional registration biostimulants cancelled", "biostimulant regulation india 2025", "approved biostimulants list india"], [q for q, _ in fco_faq], "Informational (GEO authority)", "Distributors, brands, importers, regulators")
