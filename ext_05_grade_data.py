# Grade-level data for the 36 Schedule VI biostimulant grades and 11 biofertiliser types.
# Wording is deliberately factual: what the material is, how it is commonly used, how to buy.
# No doses or yield claims: doses come from the label / dose chart on request.

def grade_path(name, form):
    base = slug(name)
    if form == LAF:
        return f"/products/{base}"
    f = {"Liquid": "liquid", "Powder": "powder", "Granular": "granular", "Granules": "granules"}[form]
    return f"/products/{base}-{f}"

GROUP_INFO = {
 "humic": dict(
   cat="/humic-acid-manufacturer-india", cat_name="Humic and fulvic acid",
   what=("Humic substances are the stable, dark fraction of well-decomposed organic matter. Commercial humic acid is usually "
         "extracted from humified sources such as leonardite or lignite by an alkaline process, and potassium humate is its "
         "water-soluble potassium salt. Fulvic acids are the smaller, lighter fraction that stays dissolved across a wide pH range, "
         "which is why fulvic-rich grades suit foliar and drip use."),
   uses=["Soil conditioning in compact, low organic-matter or over-cropped soils",
         "Holding nutrients near the root zone so less is lost from the profile",
         "Complexing micronutrients and improving their availability",
         "Supporting early root development at sowing or transplanting",
         "Getting more value from the fertiliser already being applied"],
   methods=["Basal application mixed with fertiliser (granules and powders)", "Drip or fertigation (liquids and soluble powders)",
            "Soil drench around the root zone", "Foliar spray (fulvic and fully soluble grades)"],
   compat=("Humic grades mix with most fertilisers. Avoid tank-mixing with strongly acidic products or high-calcium solutions "
           "without a jar test, because humic acid can precipitate at low pH.")),
 "seaweed": dict(
   cat="/seaweed-extract-manufacturer-india", cat_name="Seaweed extract",
   what=("Seaweed extracts are made by breaking down the cell walls of marine algae and concentrating the soluble fraction. "
         "They carry naturally occurring polysaccharides such as alginates, mannitol, betaines, trace minerals and plant "
         "hormone-like compounds. Composition depends on the species: Ascophyllum nodosum is a cold-water brown alga, "
         "Kappaphycus alvarezii is a red alga farmed in warm coastal waters including India's south-east coast, and Sargassum "
         "is a tropical brown alga."),
   uses=["Helping crops cope with heat, drought and salt stress", "Supporting flowering, fruit set and fruit development",
         "Supporting root and shoot growth in the early crop", "Recovery after transplanting, hail or pest damage",
         "Quality-focused programmes in fruit and vegetable crops"],
   methods=["Foliar spray", "Drip or fertigation", "Seed or seedling dip", "Soil application (granular grades)"],
   compat=("Seaweed extracts mix with most foliar nutrients and many crop-protection products. Always run a jar test first and "
           "spray in the cooler part of the day.")),
 "botanical": dict(
   cat="/biostimulants-manufacturer-india", cat_name="Botanical extracts",
   what=("Botanical biostimulants are extracts of specific plants. Schedule VI of the Fertiliser Control Order lists them by plant "
         "species and concentration. Adhatoda vasica, known locally as adulsa or ardusi, is a shrub widely grown across India."),
   uses=["Botanical input for biostimulant formulations", "Foliar programmes where a plant-based input is preferred",
         "Blending with seaweed extracts (see our botanical plus seaweed grade)"],
   methods=["Foliar spray", "Formulation by brand owners and formulators"],
   compat="Run a jar test before mixing with other products. Ask for the technical sheet for handling and storage."),
 "blends": dict(
   cat="/biostimulants-manufacturer-india", cat_name="Blended biostimulants",
   what=("Blended grades combine two or more biostimulant materials, for example humic acid with seaweed extract, so one "
         "application covers more than one job. Each blend on this site is a listed grade under our Gujarat NOC, so it can be "
         "sold as supplied or packed under your brand."),
   uses=["One-pass programmes that cut the number of applications", "Combining soil action (humic) with stress support (seaweed)",
         "Ready-to-sell crop programmes for distributors and private-label brands"],
   methods=["Basal or broadcast (granules and powders)", "Drip or fertigation (liquids)", "Foliar spray (liquids)"],
   compat="Blends are designed to be stable as supplied. Jar-test before tank-mixing with other products."),
 "protein": dict(
   cat="/amino-acid-protein-hydrolysate-manufacturer-india", cat_name="Amino acid and protein hydrolysate",
   what=("Protein hydrolysates are mixtures of free amino acids and short peptides made by breaking down proteins with enzymes, "
         "acid or alkali. Plant-source grades start from vegetable proteins; animal-source grades start from animal proteins such "
         "as collagen, which gives a profile richer in glycine and proline. Amino acid grades are specified by their free amino "
         "acid content."),
   uses=["Supporting recovery after cold, heat, transplanting or pest damage", "Early growth and canopy development",
         "Flowering and fruit set programmes", "Complexing micronutrients in foliar formulations"],
   methods=["Foliar spray", "Drip or fertigation", "Formulation base for brand owners"],
   compat=("Amino acid products mix with most foliar nutrients and seaweed extracts. Jar-test before mixing with copper or "
           "strongly alkaline products.")),
 "other": dict(
   cat="/biostimulants-manufacturer-india", cat_name="Bio-chemical grades",
   what=("This is a bio-chemical grade listed under Schedule VI of the Fertiliser Control Order, used at very low concentration. "
         "It is supplied mainly to formulators and brand owners."),
   uses=["Low-dose bio-chemical input for formulations"], methods=["Formulation by brand owners and formulators"],
   compat="Ask for the technical sheet for handling, mixing and storage."),
}

GRADE_NOTE = {
 "Humic acid 5%|Powder": "A low-concentration humic powder that blends easily into fertiliser mixes, organic manures and soil-applied products.",
 "Potassium humate 49%|Powder": "The water-soluble potassium salt of humic acid. It dissolves fully, so it suits drip, drench and foliar use, and liquid formulation by brand owners.",
 "Humate and fulvates 22%|Liquid": "A ready-to-use liquid combining humates and fulvates, for drench and drip programmes without dissolving a powder on the farm.",
 "Humates 12.5%|Liquid": "A ready liquid humate for drip, drench and soil application, convenient for retail packs and farm use.",
 "Humic acid 51%|Granular": "A high-content humic granule for basal application, broadcast or mixed with fertiliser at sowing and top dressing.",
 "Humic acid 1.5%|Granules": "A low-dose humic granule made for easy broadcast with fertiliser, the kind of product farmers often buy as soil granules.",
 "Humic and fulvic acid 25.05%|Liquid": "A liquid with both humic and fulvic fractions, suited to drip, drench and, where the label allows, foliar programmes.",
 "Humic and fulvic acid 76%|Powder": "A concentrated soluble humic and fulvic powder for formulators, fertigation and high-value liquid products.",
 "Ascophyllum nodosum 15%|Liquid": "A concentrated extract of the North Atlantic brown seaweed Ascophyllum nodosum, the most widely used seaweed in biostimulants worldwide.",
 "Ascophyllum nodosum 7%|Liquid": "A lower-concentration Ascophyllum nodosum extract, a cost-effective choice for retail packs and regular foliar programmes.",
 "Kappaphycus alvarezii 24%|Liquid": "A concentrated extract of the red seaweed Kappaphycus alvarezii, which is farmed along India's south-east coast.",
 "Kappaphycus alvarezii 9.5%|Liquid": "A mid-strength Kappaphycus alvarezii extract for foliar and drip use in field and horticulture crops.",
 "Kappaphycus alvarezii 7.2%|Liquid": "A ready-to-dilute Kappaphycus alvarezii extract suited to retail packs and frequent foliar sprays.",
 "Sargassum tenerrimum 10%|Liquid": "A liquid extract of Sargassum tenerrimum, a tropical brown seaweed found along Indian coasts.",
 "Sargassum tenerrimum 2%|Granular": "Sargassum tenerrimum extract in granular form, so seaweed can go into the soil with basal fertiliser.",
 "Kappaphycus alvarezii + Sargassum swartzii (1:1)|Liquid": "Equal parts red seaweed (Kappaphycus) and brown seaweed (Sargassum) extract, combining two seaweed profiles in one liquid.",
 "Spirulina 10%|Liquid": "An extract of Spirulina, a blue-green micro-alga rich in protein, used as an algal biostimulant input.",
 "Adhatoda vasica|Powder": "Powdered Adhatoda vasica (adulsa), a botanical input for formulators and blended products.",
 "Adhatoda vasica extract 2%|Liquid": "A liquid extract of Adhatoda vasica at 2%, for foliar programmes and formulation.",
 "Humic acid + amino acid + vitamins + bio-chemicals|Powder": "A powder combining humic acid, amino acids, vitamins and bio-chemicals in one soluble product.",
 "Seaweed + algal extract|Liquid": "A liquid combining seaweed and algal extracts for foliar and drip programmes.",
 "Seaweed + humic and fulvic acid + amino acids + vitamins|Liquid": "An all-in-one liquid: seaweed, humic and fulvic acid, amino acids and vitamins in a single product.",
 "Humic acid + seaweed extract|Liquid": "Humic acid and seaweed extract in one liquid, for drip and drench programmes.",
 "Humic acid + seaweed extract|Powder": "Humic acid and seaweed extract as a soluble powder, convenient to store and ship.",
 "Humic acid + seaweed extract|Granules": "Humic acid and seaweed extract on a granule for basal and broadcast application, often sold as seaweed or zyme-type granules.",
 "Botanical extract + seaweed extract|Liquid": "A liquid combining a botanical extract with seaweed extract.",
 "Protein hydrolysate, animal source 36.04%|Liquid": "A liquid protein hydrolysate from animal protein, with a profile rich in glycine and proline.",
 "Protein hydrolysate, plant source 25%|" + LAF: "A plant-source protein hydrolysate at 25%, available as liquid, granule or powder.",
 "Protein hydrolysate, plant source 16.9%|" + LAF: "A plant-source protein hydrolysate at 16.9%, available as liquid, granule or powder.",
 "Protein hydrolysate, plant source 1.5%|" + LAF: "A low-concentration plant-source protein hydrolysate, suited to granules and ready-to-use packs.",
 "Protein hydrolysate, plant source 27%|" + LAF: "A higher-concentration plant-source protein hydrolysate at 27%, available as liquid, granule or powder.",
 "Amino acid 5%|" + LAF: "Free amino acids at 5%, available as liquid, granule or powder.",
 "Amino acid 10%|" + LAF: "Free amino acids at 10%, available as liquid, granule or powder.",
 "Amino acid 20%|" + LAF: "Free amino acids at 20%, our most concentrated amino acid grade, as liquid, granule or powder.",
 "Vinasse residue (glutamic acid 18%)|Liquid": "A liquid from the fermentation residue of glutamic acid production, carrying 18% glutamic acid and organic matter.",
 "2-Bromo-(1H)-indole-3-carboxaldehyde 1 ppm|Liquid": "A bio-chemical grade used at 1 ppm, supplied mainly to formulators.",
}
assert all(f"{n}|{f}" in GRADE_NOTE for _, n, f in GRADES), [f"{n}|{f}" for _, n, f in GRADES if f"{n}|{f}" not in GRADE_NOTE]

GRADE_IMG_MAP = {
 "Humic acid 51%|Granular": "humic-acid-51-granular", "Humic acid 1.5%|Granules": "humic-acid-1-5-granules",
 "Ascophyllum nodosum 15%|Liquid": "ascophyllum-15-liquid", "Ascophyllum nodosum 7%|Liquid": "ascophyllum-7-liquid",
 "Kappaphycus alvarezii 24%|Liquid": "kappaphycus-24-liquid", "Kappaphycus alvarezii 9.5%|Liquid": "kappaphycus-9-5-liquid",
 "Kappaphycus alvarezii 7.2%|Liquid": "kappaphycus-7-2-liquid", "Sargassum tenerrimum 10%|Liquid": "sargassum-10-liquid",
 "Amino acid 20%|" + LAF: "amino-20-liquid", "Humic acid + seaweed extract|Granules": "humic-seaweed-granules",
}

# ---- biofertilisers
BIO_INFO = {
 "Azotobacter": ("/products/azotobacter-biofertiliser", "A free-living, aerobic soil bacterium that fixes atmospheric nitrogen. It is used for non-legume crops such as cereals, vegetables, cotton and sugarcane.",
                 "Nitrogen fixing", ["Cereals and millets", "Vegetables", "Cotton", "Sugarcane"]),
 "Azospirillum": ("/products/azospirillum-biofertiliser", "A bacterium that lives in close association with plant roots and fixes nitrogen. It is widely used in cereals, millets, sugarcane and fodder grasses.",
                  "Nitrogen fixing", ["Paddy, wheat, maize and millets", "Sugarcane", "Fodder grasses"]),
 "Acetobacter": ("/products/acetobacter-biofertiliser", "An endophytic nitrogen-fixing bacterium (Gluconacetobacter diazotrophicus) best known for living inside sugarcane tissue, where it supplies nitrogen from within the plant.",
                 "Nitrogen fixing", ["Sugarcane", "Sugar beet and sweet sorghum"]),
 "Rhizobium": ("/products/rhizobium-biofertiliser", "Bacteria that form nodules on legume roots and fix nitrogen inside them. Strains are crop-specific, so the culture must match the legume being grown.",
               "Nitrogen fixing", ["Groundnut, soybean and pulses", "Chickpea, pigeon pea, green gram and black gram"]),
 "Phosphate solubilising bacteria": ("/products/phosphate-solubilising-bacteria", "Bacteria (PSB) that release organic acids and enzymes which convert bound, insoluble soil phosphorus into forms the crop can take up.",
                                     "Phosphorus", ["All field crops", "Vegetables", "Fruit crops"]),
 "Potash mobilising bacteria (KMB)": ("/products/potash-mobilising-bacteria", "Bacteria (KMB or KSB) that help release potassium held in soil minerals, so more of the soil's own potash reaches the crop.",
                                      "Potassium", ["All field crops", "Banana, potato and sugarcane", "Fruit crops"]),
 "Zinc solubilising bacteria": ("/products/zinc-solubilising-bacteria", "Bacteria (ZSB) that convert insoluble zinc compounds in the soil into available forms, useful where zinc deficiency is common.",
                                "Zinc", ["Paddy, wheat and maize", "Zinc-deficient soils generally"]),
 "Phosphate solubilising fungal biofertilisers": ("/products/phosphate-solubilising-fungi", "Soil fungi that release phosphorus from insoluble forms, used alongside or instead of phosphate solubilising bacteria.",
                                                  "Phosphorus", ["All field crops", "Acidic and calcareous soils"]),
 "Mycorrhizal biofertilisers": ("/products/mycorrhizal-biofertiliser", "Arbuscular mycorrhizal fungi that colonise roots and extend a fine network into the soil, helping the crop take up phosphorus, water and micronutrients.",
                                "Phosphorus and water", ["Fruit crops and nurseries", "Vegetables", "Field crops"]),
 "Carrier-based consortia": ("/products/carrier-based-consortia-biofertiliser", "A mix of compatible nitrogen-fixing, phosphate-solubilising and potash-mobilising organisms on a solid carrier, for soil and seed application.",
                             "NPK consortia", ["All crops", "Mixing with compost or organic manure"]),
 "Liquid consortia": ("/products/liquid-consortia-npk-biofertiliser", "A liquid formulation of compatible N, P and K organisms. Liquid forms keep a longer shelf life than carrier forms and suit drip application.",
                      "NPK consortia", ["All crops", "Drip-irrigated crops"]),
}
assert set(BIO_INFO) == set(BIOS)
