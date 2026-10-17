# Glossary (DefinedTermSet) and a consolidated FAQ page.

GLOSS = [
 ("Acetobacter", "An endophytic nitrogen-fixing bacterium, best known in sugarcane, used as a biofertiliser.", "/products/acetobacter-biofertiliser"),
 ("Alternate bearing", "A pattern in fruit trees such as mango where a heavy crop is followed by a light one."),
 ("Amino acid", "A building block of protein. Amino acid fertilizers supply free amino acids that crops can use directly, especially under stress.", "/amino-acid-protein-hydrolysate-manufacturer-india"),
 ("Anti-transpirant", "A biostimulant category under the FCO that reduces water loss from leaves."),
 ("Ascophyllum nodosum", "A cold-water brown seaweed from the North Atlantic, the most widely used seaweed in biostimulants.", "/products/ascophyllum-nodosum-15-liquid"),
 ("Azospirillum", "A root-associated nitrogen-fixing bacterium used as a biofertiliser in cereals, millets and sugarcane.", "/products/azospirillum-biofertiliser"),
 ("Azotobacter", "A free-living nitrogen-fixing soil bacterium used as a biofertiliser in non-legume crops.", "/products/azotobacter-biofertiliser"),
 ("Basal application", "Fertilizer or soil input applied at or before sowing or planting."),
 ("Biofertiliser", "A product containing living micro-organisms that supply or release nutrients. Regulated in India under FCO Schedule III.", "/biofertilisers-manufacturer-india"),
 ("Biostimulant", "A substance or micro-organism that stimulates plant processes to improve nutrient uptake, growth, quality or stress tolerance, regardless of nutrient content. Regulated in India under FCO Schedule VI.", "/resources/what-is-a-biostimulant"),
 ("Bulk supply", "Supply in large packs such as drums, IBCs or jumbo bags for formulation, repacking or distribution.", "/bulk-supply"),
 ("Carrier-based biofertiliser", "A biofertiliser in which micro-organisms are held on a solid carrier for seed and soil application."),
 ("Chelate", "A molecule (such as EDTA) that holds a metal nutrient in a soluble, available form.", "/micronutrient-fertilizer-manufacturer-india"),
 ("CIF", "Cost, Insurance and Freight: the seller pays freight and insurance to the destination port."),
 ("Consortia", "A biofertiliser that combines several compatible organisms, for example N, P and K microbes.", "/products/liquid-consortia-npk-biofertiliser"),
 ("Controlled-release fertilizer", "A fertilizer, usually polymer-coated, that releases nutrients at a rate set by the coating.", "/slow-release-fertilizer"),
 ("Custom blend", "A fertilizer or biostimulant formulated for a specific crop, soil or market.", "/custom-fertilizer-blends"),
 ("Customised fertilizer", "In India, a notified multi-nutrient product made for specific soils and crops on the basis of soil-test data."),
 ("Fertigation", "Applying fertilizers and soluble inputs through the irrigation system, usually drip."),
 ("FCO", "The Fertiliser (Inorganic, Organic or Mixed) (Control) Order 1985, India's main fertilizer regulation.", "/fco-schedule-vi-biostimulants"),
 ("FOB", "Free On Board: the seller delivers the goods loaded on the vessel at the Indian port; the buyer pays freight from there."),
 ("Foliar spray", "Applying a dilute solution directly to leaves."),
 ("FOM and PROM", "Fermented organic manure and phosphate-rich organic manure, organic fertilizers specified under the FCO.", "/organic-fertilizer-manufacturer-india"),
 ("Fulvic acid", "The smaller, fully soluble fraction of humic substances, suited to foliar and drip use.", "/resources/humic-acid-vs-fulvic-acid"),
 ("Humic acid", "The large-molecule fraction of humic substances, used to condition soil and hold nutrients.", "/humic-acid-manufacturer-india"),
 ("IBC", "Intermediate bulk container, usually 1000 litres, used for bulk liquids."),
 ("Jar test", "Mixing products in a jar in tank proportions to check compatibility before tank-mixing.", "/resources/can-humic-acid-be-mixed-with-fertilizers-and-pesticides"),
 ("Kappaphycus alvarezii", "A red seaweed farmed in tropical waters including India; its extract is a common biostimulant.", "/products/kappaphycus-alvarezii-24-liquid"),
 ("KMB", "Potash mobilising bacteria: biofertilisers that release potassium held in soil minerals.", "/products/potash-mobilising-bacteria"),
 ("Micronutrient", "A nutrient needed in small amounts: zinc, boron, iron, manganese, copper, molybdenum.", "/micronutrient-fertilizer-manufacturer-india"),
 ("MOQ", "Minimum order quantity. We have none."),
 ("Mycorrhiza", "A fungus that colonises roots and extends a network into the soil, helping uptake of phosphorus and water.", "/products/mycorrhizal-biofertiliser"),
 ("NOC", "No Objection Certificate. Ours, from the Directorate of Agriculture, Government of Gujarat, covers 36 biostimulant grades and 11 biofertiliser types.", "/quality-compliance"),
 ("OEM", "Original equipment manufacturer: we manufacture products that you sell under your own brand.", "/private-label-oem"),
 ("Potassium humate", "The water-soluble potassium salt of humic acid.", "/products/potassium-humate-49-powder"),
 ("Private label", "Products made by a manufacturer and sold under the buyer's brand.", "/private-label-oem"),
 ("Protein hydrolysate", "A mixture of free amino acids and peptides made by breaking down plant or animal protein.", "/amino-acid-protein-hydrolysate-manufacturer-india"),
 ("PSB", "Phosphate solubilising bacteria: biofertilisers that release bound soil phosphorus.", "/products/phosphate-solubilising-bacteria"),
 ("Rhizobium", "Bacteria that fix nitrogen in nodules on legume roots; strains are crop-specific.", "/products/rhizobium-biofertiliser"),
 ("Sargassum", "A tropical brown seaweed found along Indian coasts, used for liquid and granular extracts.", "/products/sargassum-tenerrimum-10-liquid"),
 ("Schedule III", "The part of the FCO that specifies biofertilisers.", "/biofertilisers-manufacturer-india"),
 ("Schedule VI", "The part of the FCO that specifies biostimulants.", "/fco-schedule-vi-biostimulants"),
 ("Seaweed extract", "A concentrate made from marine algae, used as a biostimulant.", "/seaweed-extract-manufacturer-india"),
 ("Slow-release fertilizer", "A fertilizer that releases nutrients gradually over weeks or months.", "/slow-release-fertilizer"),
 ("Water-soluble fertilizer", "A fully soluble NPK grade for drip and foliar feeding.", "/water-soluble-fertilizer-special-grades"),
 ("ZSB", "Zinc solubilising bacteria: biofertilisers that make soil zinc available.", "/products/zinc-solubilising-bacteria"),
 ("Zyme granules", "An Indian trade name for broadcast granules carrying biostimulants such as seaweed or humic acid.", "/zyme-granules-manufacturer"),
]

letters = sorted({t[0][0].upper() for t in GLOSS})
gl = '<div class="alpha">' + "".join(f'<a href="#l-{l}">{l}</a>' for l in letters) + "</div><dl class=\"gloss\">"
seen = set()
for t in GLOSS:
    term, d = t[0], t[1]
    l = term[0].upper()
    anchor = f' id="l-{l}"' if l not in seen else ""
    seen.add(l)
    more = f' <a href="{t[2]}">More</a>' if len(t) > 2 else ""
    gl += f'<dt{anchor}>{esc(term)}</dt><dd>{esc(d)}{more}</dd>'
gl += "</dl>"
gloss_ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Biostimulant and fertilizer glossary", "url": SITE + "/glossary",
            "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t[0], "description": t[1]} for t in GLOSS]}
page("/glossary", "Biostimulant & Fertilizer Glossary: Terms Explained | GBO", "Plain definitions of biostimulant, biofertiliser, humic acid, seaweed extract, chelate, Schedule VI, FOB, CIF and more.",
     hero("Glossary", "Biostimulant, fertilizer and trade terms, each explained in a line or two.", [("Knowledge centre", "/resources"), ("Glossary", None)]) + sec(f'<div class="prose">{gl}</div>') + cta(),
     [("Knowledge centre", "/resources"), ("Glossary", None)], [gloss_ld], "0.5")
kw("/glossary", "biostimulant glossary", ["fertilizer terms", "what is chelated fertilizer", "what is fertigation", "fob vs cif"], [], "Informational", "All")

# ---------------------------------------------------------------- FAQ
FAQ_GROUPS = [
 ("Company and supply", [
   ("Who is Gujarat Bio Organics?", "A manufacturer of organic fertilizers, biostimulants, biofertilisers and specialty fertilizers at Shihor, Bhavnagar, Gujarat, India, manufacturing since 2009."),
   ("Is there a minimum order quantity?", "No. We quote against your requirement, including small trial orders."),
   ("How long does dispatch take?", "About one week from confirmed order for regular grades."),
   ("Do you give free samples?", "Yes. Samples are free; freight or courier, customs duty and other charges are paid by the buyer."),
   ("What pack sizes do you offer?", f"Liquids: {PACKS_L}. Solids: {PACKS_S}.")]),
 ("Products", [
   ("What do you manufacture?", "Humic and fulvic acids, seaweed extracts, protein hydrolysates and amino acids, botanical and blended biostimulants (36 grades), 11 biofertiliser types, and micronutrient, water-soluble, slow-release and custom fertilizers made to order."),
   ("Do you make zyme granules?", "Yes, from Schedule VI listed granular grades: humic acid granules, Sargassum seaweed granules and humic plus seaweed granules."),
   ("Do you make crop-specific products?", "Yes. Our Immunity range has dedicated products for sugarcane, potato, mango, apple and banana, and programmes for cotton, citrus and coconut."),
   ("Do you publish prices?", PRICE_A)]),
 ("Compliance", [
   ("Are your biostimulants approved?", "Our No Objection Certificate from the Directorate of Agriculture, Government of Gujarat covers 36 Schedule VI biostimulant grades and 11 Schedule III biofertiliser types. Copies are on request."),
   ("Can you provide test reports?", "Yes. Specification sheets and third-party test reports are available, and third-party sampling can be arranged."),
   ("What changed for biostimulants in 2025?", "Provisional registrations ended in June 2025, and only biostimulants specified in Schedule VI can now be sold in India.")]),
 ("Private label, distribution and export", [
   ("Can you make products under my brand?", "Yes, with your label and pack design and no minimum order."),
   ("How do distributor margins work?", "We give you bulk prices and you set your own selling margin."),
   ("Which countries do you export to?", "GCC countries, Africa, the Russian Federation, Europe, North America and South America, FOB or CIF from Indian ports.")]),
]
all_faq = [qa for _, items in FAQ_GROUPS for qa in items]
fq = hero("Frequently asked questions", "Quick answers about our products, approvals, private label, distribution and export.", [("FAQ", None)])
fq += sec("".join(f'<h2>{esc(t)}</h2>{faq_html(items)}' for t, items in FAQ_GROUPS) + links([("/resources", "Knowledge centre", "Detailed guides"), ("/contact", "Contact us", ""), ("/products", "Products", ""), ("/export", "Export", "")], "More help"))
page("/faq", "FAQ: Products, Approvals, Private Label & Export | GBO", "Answers to common questions about Gujarat Bio Organics: MOQ, samples, packs, approvals, private label, distributor margins and export.",
     fq + cta(), [("FAQ", None)], [faq_ld(all_faq)], "0.6")
kw("/faq", "gujarat bio organics faq", ["biostimulant supplier faq", "private label fertilizer faq"], [q for q, _ in all_faq], "Navigational / informational", "All")

# ---------------------------------------------------------------- keyword targets for the original pages
for _p, _k, _s, _i, _a in [
 ("/", "organic fertilizer and biostimulant manufacturer india", ["biostimulant manufacturer gujarat", "organic fertilizer manufacturer in gujarat", "gujarat bio organics", "fertilizer manufacturer bhavnagar"], "Navigational / commercial", "All"),
 ("/products", "organic fertilizer products list", ["biostimulant products", "biostimulant products in agriculture", "bio fertilizer products"], "Commercial", "All"),
 ("/biostimulants-manufacturer-india", "biostimulant manufacturers in india", ["biostimulant companies in india", "fco approved biostimulants", "schedule vi biostimulant grades", "biostimulant manufacturer"], "Commercial", "Distributors, brands, importers"),
 ("/biofertilisers-manufacturer-india", "biofertilizer manufacturer india", ["bio fertilizer products", "liquid biofertilizer manufacturer", "npk consortia manufacturer", "biofertilizer supplier gujarat"], "Commercial", "Distributors, brands"),
 ("/private-label-oem", "private label fertilizer manufacturer india", ["private label fertilizer", "white label fertilizer", "private label liquid fertilizer", "third party biostimulant manufacturing", "oem fertilizer manufacturer"], "Commercial", "Brand owners"),
 ("/export", "biostimulant exporter india", ["humic acid exporter india", "seaweed extract exporter", "organic fertilizer exporter india"], "Commercial", "Importers"),
 ("/bulk-supply", "bulk humic acid supplier", ["wholesale biostimulants", "bulk seaweed extract", "bulk amino acid fertilizer"], "Commercial", "Formulators, repackers"),
 ("/become-a-distributor", "organic fertilizer dealership", ["fertilizer distributorship", "biostimulant distributor india", "agri input dealership"], "Commercial", "Dealers"),
 ("/field-solutions", "biostimulant for crop problems", ["soil health solution", "crop stress solution", "flower drop solution"], "Informational", "Growers"),
 ("/quality-compliance", "gujarat bio organics noc", ["fco approved biostimulant supplier", "biostimulant company documents"], "Trust", "Buyers"),
 ("/about", "gujarat bio organics", ["gujarat bio organics bhavnagar", "immunity brand fertilizer"], "Navigational", "All"),
 ("/contact", "gujarat bio organics contact", ["gujarat bio organics phone number", "biostimulant quote"], "Navigational", "All")]:
    kw(_p, _k, _s, [], _i, _a)
