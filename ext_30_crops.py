# Crop hub and crop pages. Farmer-facing: no doses, no yield promises; results framed as varying.

CH, CS, CA, CB = "/humic-acid-manufacturer-india", "/seaweed-extract-manufacturer-india", "/amino-acid-protein-hydrolysate-manufacturer-india", "/biofertilisers-manufacturer-india"
CM = "/micronutrient-fertilizer-manufacturer-india"

CROPS = [
 dict(slug="sugarcane", name="Sugarcane", special="Immunity Sugarcane Special",
  regions="Gujarat, Maharashtra, Karnataka, Tamil Nadu and Uttar Pradesh",
  story=("Immunity Sugarcane Special was developed with sugarcane growers in South Gujarat, where much of the land has been under cane for "
         "around five decades. Growers told us the same story: exhausted soil, more chemical fertilizer every season, falling yields and "
         "farms that no longer broke even. The programme rebuilds soil biology and structure alongside the grower's normal fertilizer schedule."),
  answer=("Sugarcane is a long-duration, heavy-feeding crop, so it needs a strong start at planting, steady nutrition through tillering and grand "
          "growth, and healthy soil to support ratoons. A good programme combines balanced NPK with humic acid for soil, biofertilisers such as "
          "Acetobacter and Azotobacter for nitrogen, PSB and KMB for phosphorus and potash, and seaweed extract for stress in the grand growth phase."),
  stages=[["Planting and germination", "Strong sett germination and early roots", f'Sett treatment with <a href="/products/acetobacter-biofertiliser">Acetobacter</a> and <a href="/products/phosphate-solubilising-bacteria">PSB</a>; <a href="{CH}">humic granules</a> in the furrow'],
          ["Tillering", "More productive tillers", f'<a href="{CH}">Humic acid</a> with the top dressing; <a href="{CA}">amino acids</a> if growth stalls'],
          ["Grand growth", "Cane elongation through heat and dry spells", f'<a href="{CS}">Seaweed extract</a> by drip or spray; <a href="/products/potash-mobilising-bacteria">KMB</a>'],
          ["Ratoon", "Reviving stubble and soil", f'<a href="{CH}">Humic acid</a> and <a href="{CB}">biofertiliser consortia</a> after harvest']],
  problems=["Soil exhausted after decades of continuous cane", "Poor germination and gappy stands", "Fewer millable canes", "Rising fertilizer bills with falling returns", "Weak ratoons"],
  faq=[("What is the best fertilizer for sugarcane?", "There is no single product. Sugarcane needs balanced NPK on a soil-test basis, plus inputs that keep soil productive: humic acid, nitrogen-fixing biofertilisers such as Acetobacter and Azotobacter, PSB and KMB, and seaweed extract in the grand growth phase."),
       ("Which fertilizer is best for sugarcane tillering?", "Tillering needs nitrogen at the right time and active roots. Growers commonly apply humic acid with the nitrogen top dressing, and amino acids if growth is held back by stress."),
       ("Which biofertilizer is used for sugarcane?", "Acetobacter (Gluconacetobacter diazotrophicus) is the best-known biofertiliser for sugarcane because it lives inside the cane. Azotobacter, Azospirillum, PSB and KMB are also widely used."),
       ("Is humic acid good for sugarcane?", "Humic acid is widely used in sugarcane to improve soil structure and nutrient holding, especially on land that has been under cane for many years."),
       ("What should be applied at sugarcane top dressing?", "The nitrogen and potash due by the soil-test recommendation, often with humic acid granules applied at the same time. Follow your local agriculture department's schedule."),
       ("How can I improve ratoon sugarcane?", "Manage stubble, apply balanced nutrition early, and use humic acid and biofertiliser consortia to revive soil biology after harvest.")],
  kw=("best fertilizer for sugarcane", ["best fertilizer for sugarcane growth", "best fertilizer for sugarcane in india", "best fertilizer for sugarcane tillering", "best fertilizer for sugarcane top dressing", "biofertilizer for sugarcane", "acetobacter for sugarcane", "humic acid for sugarcane", "immunity sugarcane special"])),
 dict(slug="potato", name="Potato", special="Immunity Potato Special",
  regions="Punjab, Haryana, Uttar Pradesh, West Bengal and Gujarat",
  story=("Immunity Potato Special was developed for potato growers in Punjab and Haryana who were facing falling yields, higher and higher "
         "fertilizer requirements, fewer and smaller tubers and weaker quality. It is built around strong early roots, even tuber initiation and "
         "steady bulking."),
  answer=("Potato needs fast early root growth, even tuber initiation and steady bulking. A good programme pairs balanced NPK, with potash for "
          "bulking and quality, with humic acid at planting, PSB and KMB to free soil phosphorus and potash, seaweed extract around tuber "
          "initiation, and amino acids after stress such as frost."),
  stages=[["Planting", "Seed tuber establishment and early roots", f'<a href="{CH}">Humic granules</a> with basal fertilizer; <a href="/products/phosphate-solubilising-bacteria">PSB</a>'],
          ["Emergence and vegetative", "Canopy and root growth", f'<a href="{CA}">Amino acids</a>; <a href="{CH}">humic liquid</a> by drip'],
          ["Tuber initiation", "Even stolon and tuber set", f'<a href="{CS}">Seaweed extract</a> spray'],
          ["Bulking", "Tuber size and dry matter", f'Potash on soil-test basis; <a href="/products/potash-mobilising-bacteria">KMB</a>; <a href="{CS}">seaweed</a>']],
  problems=["Falling yields despite more fertilizer", "Fewer tubers per plant", "Small or uneven tubers", "Weak quality and storability", "Frost and heat stress"],
  faq=[("What is the best fertilizer for potato tuber growth?", "Tuber bulking depends on adequate potash, healthy canopy and active roots. Potash on a soil-test basis, with seaweed extract at tuber initiation and KMB, is a common approach."),
       ("Which fertilizer increases potato size?", "No single product does. Size comes from good tuber set, a healthy canopy through bulking and adequate potash and water. Biostimulants such as seaweed extract are used to support the crop through these stages."),
       ("Is seaweed extract good for potato?", "Seaweed extract is commonly sprayed around tuber initiation and during bulking to support the crop through stress."),
       ("When should humic acid be applied to potato?", "Most growers apply humic granules with the basal fertilizer at planting, and humic liquid through drip in the vegetative phase."),
       ("Which biofertilizers are used in potato?", "PSB and KMB to release soil phosphorus and potash, and Azotobacter for nitrogen.")],
  kw=("fertilizer for potato crop", ["fertilizer for potato", "fertilizer for potato tubers", "fertilizer for potato growth", "best fertilizer for potato size", "seaweed for potato", "immunity potato special"])),
 dict(slug="mango", name="Mango", special="Immunity Mango Special",
  regions="Gujarat, Maharashtra, Andhra Pradesh, Karnataka, Uttar Pradesh and across India",
  story=("Immunity Mango Special was developed for mango growers across India dealing with tree decline and mortality, poor growth, alternate "
         "bearing, flower and fruit drop, small fruit and poor quality, often on orchards that no longer broke even. It is a season-long programme "
         "from post-harvest care to fruit development."),
  answer=("Mango needs post-harvest recovery, a healthy vegetative flush, good flowering, strong fruit set and steady fruit development. Growers "
          "combine balanced nutrition with humic acid and biofertilisers for the root zone, boron and zinc where deficient, seaweed extract and "
          "amino acids around flowering and fruit set, and potash during fruit development."),
  stages=[["Post-harvest and pruning", "Tree recovery and root health", f'<a href="{CH}">Humic acid</a>, <a href="/products/mycorrhizal-biofertiliser">mycorrhizae</a>, organic manure'],
          ["Vegetative flush", "Healthy new shoots", f'<a href="{CA}">Amino acids</a>; <a href="{CM}">zinc</a> if deficient'],
          ["Flowering", "Strong, even flowering", f'<a href="{CS}">Seaweed extract</a>; <a href="{CM}">boron</a> if deficient'],
          ["Fruit set and development", "Holding fruit and sizing", f'<a href="{CS}">Seaweed</a> and <a href="{CA}">amino acid</a> sprays; potash']],
  problems=["Tree decline and mortality", "Alternate (biennial) bearing", "Flower and fruit drop", "Small fruit and poor quality", "Orchards that no longer break even"],
  faq=[("What is the best fertilizer for mango trees during flowering?", "Mango at flowering mainly needs boron where it is deficient, and many growers use seaweed extract to support flowering and set. Avoid heavy nitrogen at this stage, which pushes leaf growth instead of flowers."),
       ("Which fertilizer should be used after mango flowering?", "After set, growers support fruit development with potash, seaweed extract and amino acid sprays, and keep the root zone moist and healthy."),
       ("How can I reduce fruit drop in mango?", "Fruit drop has many causes: water stress, nutrient gaps such as boron, heat, pests and disease. Steady irrigation, balanced nutrition and seaweed or amino acid sprays at set are common parts of a programme; persistent drop needs a field diagnosis."),
       ("Which organic fertilizer is best for mango trees?", "Well-rotted organic manure with humic acid and biofertilisers such as mycorrhizae, PSB and Azotobacter after harvest is a common organic base for mango."),
       ("Can alternate bearing in mango be corrected?", "Alternate bearing is influenced by variety, crop load and tree health. Good post-harvest nutrition and root health help trees carry a more regular crop, but it cannot be removed entirely by any input.")],
  kw=("fertilizer for mango tree", ["fertilizer for mango tree during flowering", "fertilizer for mango tree after flowering", "fertilizer for mango tree for flowering", "fertilizer for mango tree growth", "mango fruit drop solution", "organic fertilizer for mango tree", "immunity mango special"])),
 dict(slug="apple", name="Apple", special="Immunity Apple Special",
  regions="Himachal Pradesh, Jammu and Kashmir and Uttarakhand",
  story=("Immunity Apple Special was developed for apple growers in Himachal Pradesh and Jammu and Kashmir who were losing trees, seeing low "
         "production and poor fruit quality, and paying more for inputs every year, with no chemical answer to the decline. It focuses on root "
         "and soil health, recovery and fruit quality."),
  answer=("Apple orchards need healthy roots and soil, good spring flowering and set, steady fruit development and colour, and post-harvest "
          "recovery. Growers combine balanced nutrition with humic acid and mycorrhizae for the root zone, calcium and boron where needed, seaweed "
          "extract around flowering and fruit development, and amino acids after frost or hail."),
  stages=[["Dormancy and bud break", "Root activity and even bud break", f'<a href="{CH}">Humic acid</a>, <a href="/products/mycorrhizal-biofertiliser">mycorrhizae</a>, organic manure'],
          ["Flowering and fruit set", "Pollination and set", f'<a href="{CS}">Seaweed extract</a>; <a href="{CM}">boron</a> if deficient'],
          ["Fruit development", "Size, firmness and colour", f'<a href="{CS}">Seaweed</a>; calcium; <a href="{CA}">amino acids</a> after hail or frost'],
          ["Post-harvest", "Reserve building for next season", f'<a href="{CH}">Humic acid</a> and <a href="{CB}">biofertilisers</a>']],
  problems=["Tree decline and plant mortality", "Low production", "Poor size, colour and quality", "Frost and hail damage", "Rising input costs"],
  faq=[("What is the best fertilizer for apple trees?", "Apple needs balanced nutrition on a soil and leaf test basis, with attention to calcium and boron for fruit quality. Humic acid, mycorrhizae and seaweed extract are commonly added to support roots, flowering and fruit development."),
       ("Which fertilizer improves apple fruit size and colour?", "Fruit size and colour depend on crop load, sunlight, potash and calcium nutrition and tree health. Seaweed extract is commonly sprayed during fruit development as part of a quality programme."),
       ("What should apple growers apply after hail?", "After hail, growers commonly spray amino acids or seaweed extract to support recovery, alongside the crop-protection measures their local advisers recommend."),
       ("Why are apple trees dying in my orchard?", "Tree decline has many causes, including root diseases, waterlogging, poor soil health, nutrient imbalance and pests. Get a field diagnosis; root-zone health programmes are often part of the recovery plan.")],
  kw=("fertilizer for apple trees", ["best fertilizer for apple trees in india", "apple orchard nutrition himachal", "apple fruit size and colour fertilizer", "apple tree decline", "immunity apple special"])),
 dict(slug="banana", name="Banana", special="Immunity Banana Special",
  regions="Gujarat, Maharashtra, Tamil Nadu, Andhra Pradesh and Karnataka",
  story=("Immunity Banana Special was developed with banana growers in Central Gujarat working under heavy fungal disease pressure from Sigatoka "
         "leaf spot and Fusarium wilt, with plant mortality and poor growth, bunch weight and quality. It is a nutrition and soil-health programme "
         "that supports plant vigour; it is not a fungicide, and disease control needs its own crop-protection plan."),
  answer=("Banana is a fast-growing, heavy-feeding crop, especially for potash. A good programme pairs balanced fertigation with humic acid and "
          "biofertilisers in the root zone, seaweed extract and amino acids for vigour and stress, and potash through bunch development. Disease "
          "pressure needs a separate crop-protection plan."),
  stages=[["Planting", "Establishment of suckers or tissue-culture plants", f'<a href="{CH}">Humic acid</a>; <a href="{CB}">biofertiliser consortia</a>; <a href="/products/mycorrhizal-biofertiliser">mycorrhizae</a>'],
          ["Vegetative", "Pseudostem and leaf growth", f'<a href="{CA}">Amino acids</a>, <a href="{CS}">seaweed</a> by drip'],
          ["Shooting", "Bunch emergence", f'<a href="{CS}">Seaweed extract</a>; potash'],
          ["Bunch development", "Finger filling and weight", f'Potash; <a href="/products/potash-mobilising-bacteria">KMB</a>; <a href="{CS}">seaweed</a>']],
  problems=["Heavy Sigatoka and Fusarium pressure", "Plant mortality", "Slow growth and delayed shooting", "Low bunch weight", "Export-quality fruit is hard to reach"],
  faq=[("What is the best fertilizer for banana plants in India?", "Banana needs balanced nutrition with plenty of potash, usually through fertigation, plus humic acid and biofertilisers for the root zone and seaweed extract for vigour."),
       ("Which fertilizer increases banana bunch weight?", "Bunch weight depends on plant vigour, potash nutrition and water through bunch development. Potash with seaweed extract and KMB is a common approach."),
       ("Can biostimulants cure Fusarium wilt or Sigatoka in banana?", "No. Biostimulants are not fungicides. They support plant vigour, but disease control needs clean planting material and a crop-protection plan from your local adviser."),
       ("Which biofertilizers are used for banana?", "Mycorrhizae, Azospirillum, PSB and KMB, often as a consortium, applied at planting and through drip.")],
  kw=("fertilizer for banana plant in india", ["fertilizer for banana plant", "fertilizer for banana tree", "best fertilizer for banana", "banana bunch weight fertilizer", "biofertilizer for banana", "immunity banana special"])),
 dict(slug="cotton", name="Cotton", special="Immunity cotton programme",
  regions="Gujarat, Maharashtra, Telangana, Punjab, Haryana and Rajasthan",
  story=("Cotton growers come to us with the same questions every season: squares and flowers that drop, crops that stall in heat and dry spells, "
         "and bolls that do not fill. Our cotton programme combines humic acid and biofertilisers at sowing with seaweed, amino acid and boron at "
         "the reproductive stages."),
  answer=("Cotton needs a good start, steady growth into squaring, strong retention of squares, flowers and bolls, and boll filling. Growers "
          "combine balanced NPK with humic acid and biofertilisers at sowing, boron and other micronutrients where deficient, and seaweed extract "
          "and amino acids at squaring and flowering to support retention under stress."),
  stages=[["Sowing", "Even germination and roots", f'<a href="{CH}">Humic granules</a>; <a href="/products/azotobacter-biofertiliser">Azotobacter</a> and <a href="/products/phosphate-solubilising-bacteria">PSB</a> seed treatment'],
          ["Vegetative", "Balanced growth", f'<a href="{CA}">Amino acids</a> after stress'],
          ["Squaring and flowering", "Retaining squares and flowers", f'<a href="{CS}">Seaweed extract</a>; <a href="{CM}">boron</a> and micronutrients'],
          ["Boll development", "Boll filling and size", f'Potash; <a href="{CS}">seaweed</a>']],
  problems=["Square and flower shedding", "Stalling in heat and dry spells", "Boron and zinc deficiency", "Poor boll filling"],
  faq=[("What is the best fertilizer for cotton crop?", "Cotton needs balanced NPK by soil test, with attention to boron and zinc. Humic acid at sowing and seaweed extract at squaring and flowering are common additions."),
       ("Which micronutrient is important for cotton?", "Boron is especially important for flowering and boll retention, and zinc is often deficient. Apply on a soil or leaf test basis."),
       ("What foliar spray is used in cotton?", "Growers commonly spray boron and micronutrients, seaweed extract and amino acids at squaring and flowering, following a crop schedule."),
       ("How can I reduce flower drop in cotton?", "Flower and square shedding is caused by water stress, heat, nutrient gaps such as boron, and pests. Fix water and nutrition first; seaweed and amino acid sprays are commonly used to support retention.")],
  kw=("best fertilizer for cotton crop", ["fertilizer for cotton crop", "fertilizer for cotton plant in india", "micronutrient fertilizer for cotton", "foliar fertilizer for cotton", "fertilizer dose for cotton", "cotton flower drop solution"])),
 dict(slug="citrus", name="Citrus", special="Immunity citrus programme",
  regions="Maharashtra, Andhra Pradesh, Punjab, Madhya Pradesh and Gujarat",
  story=("Our citrus programme comes from field work with growers of sweet orange, mandarin and lime. The usual problems are tired trees, zinc and "
         "iron deficiency on alkaline soils, flower and fruit drop, and uneven fruit size."),
  answer=("Citrus trees need healthy roots, good flowering, fruit set and steady fruit development. Growers combine balanced nutrition with humic "
          "acid and mycorrhizae for the root zone, zinc, iron and manganese where deficient (common on alkaline soils), and seaweed extract and "
          "amino acids around flowering and fruit set."),
  stages=[["Post-harvest", "Tree recovery and roots", f'<a href="{CH}">Humic acid</a>, <a href="/products/mycorrhizal-biofertiliser">mycorrhizae</a>'],
          ["Flush", "Healthy new growth", f'<a href="{CM}">Zinc, iron, manganese</a> where deficient'],
          ["Flowering and set", "Set and holding fruit", f'<a href="{CS}">Seaweed extract</a>, <a href="{CA}">amino acids</a>'],
          ["Fruit development", "Size and quality", f'Potash; <a href="{CS}">seaweed</a>']],
  problems=["Zinc and iron deficiency on alkaline soils", "Flower and fruit drop", "Tree decline", "Uneven fruit size"],
  faq=[("What is the best fertilizer for citrus trees?", "Citrus needs balanced nutrition with close attention to zinc, iron and manganese, which are often deficient on alkaline soils. Humic acid and seaweed extract are common additions."),
       ("Why are citrus leaves turning yellow?", "Yellowing between veins on young leaves usually points to iron, zinc or manganese deficiency; general yellowing can mean nitrogen shortage or root problems. Confirm with a leaf test."),
       ("How can I reduce fruit drop in citrus?", "Steady irrigation, balanced nutrition and sprays at set are common parts of the answer; persistent drop needs a field diagnosis.")],
  kw=("fertilizer for citrus trees", ["best fertilizer for citrus", "citrus yellow leaves treatment", "citrus fruit drop", "zinc deficiency in citrus"])),
 dict(slug="coconut", name="Coconut", special="Immunity coconut programme",
  regions="Kerala, Tamil Nadu, Karnataka, Andhra Pradesh and Gujarat",
  story=("Our coconut programme comes from field work with growers whose palms were losing vigour, setting fewer nuts and dropping buttons. "
         "Coconut is a perennial that bears all year, so the programme focuses on the basin: organic matter, humic acid and biofertilisers, "
         "with balanced nutrition."),
  answer=("Coconut palms bear year-round, so they need steady nutrition and a healthy root basin. Growers apply organic manure with humic acid "
          "and biofertilisers in the basin, balanced NPK with plenty of potash, and boron and other micronutrients where deficient."),
  stages=[["Basin preparation", "Root activity and organic matter", f'Organic manure with <a href="{CH}">humic acid</a> and <a href="{CB}">biofertilisers</a>'],
          ["Main nutrient applications", "Steady nut set", 'Balanced NPK with potash on soil-test basis'],
          ["Through the year", "Button retention and nut filling", f'<a href="{CM}">Boron</a> if deficient; <a href="{CS}">seaweed</a> by root feeding or drip']],
  problems=["Loss of palm vigour", "Button shedding", "Fewer and smaller nuts", "Poor, sandy or tired basins"],
  faq=[("What is the best organic fertilizer for coconut trees?", "Well-rotted organic manure in the basin, with humic acid and biofertilisers such as Azospirillum, PSB and mycorrhizae, is a common organic base, alongside balanced NPK."),
       ("How do I use humic acid for coconut trees?", "Humic acid is usually applied in the basin around the palm with organic manure, or through drip. Follow the dose on the label."),
       ("Why are coconut buttons falling?", "Button shedding has many causes: water stress, poor pollination, nutrient gaps such as boron and potash, and pests. Fix water and nutrition first and get a field diagnosis if it continues.")],
  kw=("organic fertilizer for coconut tree", ["how to use humic acid for coconut tree", "fertilizer for coconut tree", "coconut button shedding solution", "best fertilizer for coconut"])),
]

def crop_page(c):
    p = f"/crops/{c['slug']}"
    trail = [("Crops", "/crops"), (c["name"], None)]
    body = hero(f"{c['name']} nutrition and biostimulant programme", f"How {c['name'].lower()} growers in {c['regions']} use humic acid, seaweed, amino acids and biofertilisers, and how our {c['special']} came about.", trail)
    body += sec(answer(c["answer"]) + f'<h2>Stage by stage</h2>' + table(["Stage", "What the crop needs", "Inputs growers use"], c["stages"]) + CLAIM_NOTE
                + quote_btns(f"Hello Gujarat Bio Organics, I grow {c['name'].lower()} in ___. Please suggest a programme."))
    body += sec(f'<div class="split"><div><h3>Problems growers bring to us</h3>{ul([esc(x) for x in c["problems"]])}</div>'
                f'<div><h3>{esc(c["special"])}</h3><p>{esc(c["story"])}</p><p>Distributors can carry this programme in territories where we do not yet have a presence, and brands can have it made under their own label.</p>'
                f'<div class="btn-row"><a class="btn btn-dark" href="/become-a-distributor">Become a distributor</a><a class="btn btn-ghost" href="/private-label-oem">Private label</a></div></div></div>',
                f"{c['name']} problems and our programme", cls="tint")
    rel = [("/crop-specific-fertilizers", "All crop-specific products", "Immunity range")] + [(f"/crops/{o['slug']}", o["name"], "") for o in CROPS if o["slug"] != c["slug"]][:5]
    body += sec(faq_html(c["faq"]) + links(rel), f"{c['name']} questions")
    body += cta(f"Tell us about your {c['name'].lower()} crop.", "Share your region, soil and problem. We recommend a programme and a trial.", f"Hello Gujarat Bio Organics, I grow {c['name'].lower()}. Please suggest a programme.")
    page(p, f"{c['name']} Fertilizer & Biostimulant Programme | GBO", f"{c['name']} nutrition by stage: humic acid, seaweed, amino acids, biofertilisers and the {c['special']}. For growers, distributors and brands.",
         body, trail, [faq_ld(c["faq"])], "0.7")
    kw(p, c["kw"][0], c["kw"][1], [q for q, _ in c["faq"]], "Informational / commercial", "Growers, distributors")

for c in CROPS:
    crop_page(c)

ch = hero("Crop programmes", "Sugarcane, potato, mango, apple, banana, cotton, citrus and coconut: what each crop needs, stage by stage.", [("Crops", None)])
ch += sec(answer("Gujarat Bio Organics builds crop programmes that combine nutrition, biostimulants and biofertilisers for each crop's stages and usual problems. The Immunity range has dedicated products for sugarcane, potato, mango, apple and banana.")
          + hub([(f"/crops/{c['slug']}", c["name"], c["problems"][0]) for c in CROPS]) + CLAIM_NOTE)
page("/crops", "Crop Programmes: Sugarcane, Potato, Mango, Apple & More | GBO", "Crop-wise nutrition and biostimulant programmes for sugarcane, potato, mango, apple, banana, cotton, citrus and coconut from Gujarat Bio Organics.",
     ch + cta(), [("Crops", None)], [itemlist_ld("Crop programmes", [(f"/crops/{c['slug']}", c["name"]) for c in CROPS])], "0.8")
kw("/crops", "crop wise fertilizer schedule", ["crop nutrition programme", "biostimulant for crops", "fertilizer schedule for crops"], [], "Informational", "Growers, distributors")
