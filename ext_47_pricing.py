# Bulk pricing and quotes page. No prices published: explains how a quote is built, what to send, and the terms.
_pq_faq = [
 ("Do you publish a price list?", "No. Price depends on the grade, concentration, form (liquid, powder or granular), pack size, quantity and destination, so we quote each enquiry. Send the details and our team replies with a written quote."),
 ("Is there a minimum order quantity?", "No. We supply from a single pack to full container loads. Larger quantities and repeat orders get better rates."),
 ("How quickly can you dispatch?", "Usually about one week from order confirmation. Made-to-order grades and private-label packing can take longer, and we confirm the date in the quote."),
 ("Do you give free samples?", "Yes. Samples are free; freight, duty and any other charges are paid by the buyer."),
 ("Which Incoterms and ports do you quote for export?", "FOB and CIF, shipped from Pipavav, Kandla, Dahej, Mundra and JNPT depending on the destination."),
 ("What should I send to get a quote?", "The product or grade, form, quantity per order and per year, pack size, destination (city or port), and whether you want bulk, your own private label or our Immunity brand."),
]
_pq = f'''<div class="prose">
<p>{NAME} is a fertilizer manufacturer, so we quote directly from the plant in Shihor, Bhavnagar, Gujarat. We do not publish a price list, because the same product changes in cost with the grade, concentration, form, pack and quantity. Tell us what you need and our team replies with a written quote.</p>
</div>
<h2>What decides the price</h2>
{ul(["Grade and concentration: for example the percentage of humic acid, seaweed extract or amino acids",
     "Form: liquid, powder, flake or granular",
     "Pack size: retail packs, drums, IBC totes or jumbo bags",
     "Quantity per order and expected yearly volume",
     "Destination: delivery within India, or FOB or CIF for export",
     "Branding: bulk unbranded, your private label, or our Immunity brand"])}
<h2>What to send for a quote</h2>
{ul(["Product or grade you want (or your crop and problem, and we will suggest one)",
     "Quantity per order and per year",
     "Pack size and form",
     "Destination city or port",
     "Your company name and a phone or WhatsApp number"])}
<h2>Terms in brief</h2>
{table(["Item", "What we do"], [
  ["Minimum order", "None"],
  ["Dispatch", "About one week from order confirmation, subject to grade and packing"],
  ["Samples", "Free; freight, duty and other charges paid by the buyer"],
  ["Export", "FOB or CIF from Pipavav, Kandla, Dahej, Mundra and JNPT"],
  ["Origin", f"{FACTORY}"]])}
<p>Related: <a href="/bulk-supply">Bulk supply</a>, <a href="/private-label-oem">Private label and OEM</a>, <a href="/export">Export</a>, <a href="/become-a-distributor">Become a distributor</a>.</p>'''
_pq_body = (page_hero("Bulk pricing and quotes", "How we quote, what to send us, and the terms for bulk, private-label and export orders.", "/bulk-pricing-and-quotes", "Bulk pricing and quotes")
            + sec(answer("We quote each order from the plant: there is no price list and no minimum order. Send the grade, form, quantity, pack size and destination, and we reply with a written quote.") + _pq)
            + sec(faq_html(_pq_faq), "Pricing and quote questions")
            + cta("Ask for a quote.", "Send the product, quantity and destination. We reply with a written quote.", "Hello Gujarat Bio Organics, please send me a quote. Product: / Quantity: / Destination:"))
page("/bulk-pricing-and-quotes", "Bulk Pricing & Quotes: Fertilizer Manufacturer India | GBO",
     "How to get a bulk quote from a fertilizer manufacturer in Gujarat: what decides price, what to send, no minimum order, free samples, FOB and CIF export.",
     _pq_body, [("Bulk pricing and quotes", None)], [faq_ld(_pq_faq)], "0.7")
kw("/bulk-pricing-and-quotes", "bulk fertilizer price india", ["organic fertilizer price", "fertilizer manufacturer quote", "biostimulant price per kg"], [q for q, _ in _pq_faq], "Commercial", "Distributors, brands, importers")
