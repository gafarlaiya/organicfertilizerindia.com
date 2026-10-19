# Tracking setup (b2b.gujaratbio.com)

**Site code** (already in the repo): consent defaults (Google Consent Mode v2), `dataLayer` events, ad-click-ID capture, cookie banner for Europe/UK visitors, `/privacy-policy`.
**Loads:** the GA4 tag directly until `GTM_ID` in `build.py` is set; then GTM only (never both).

## Event list (all pushed to `dataLayer`, names are GA4-style)
| Event | When | Parameters |
|---|---|---|
| `generate_lead` | Enquiry form saved, or chat saves a lead | form_name, lead_channel (website_form / chatbot), event_id, grades_count |
| `click_whatsapp` / `click_phone` / `click_email` | Any wa.me, tel: or mailto: link | link_location, link_text, event_id |
| `form_start` / `form_error` | First field focus / save failed | form_name |
| `begin_quote` | "Request a quote for these grades" bar | grades_count |
| `video_start` | Grower video played | video_id, video_provider, video_title |
| `chat_open` / `chat_start` | Chat opened / first message in a session | |
| `page_not_found` | 404 page viewed | page_path |
Every event also carries `page_type` (home, category, product, crop, article, lead_page, company, legal, 404, other).
Team visits: open any page with `?internal=1` once on each browser/phone to flag it as `traffic_type=internal` (use `?internal=0` to undo).

## GTM container
`gbo-gtm-container.json` (made by `make_container.py`): Google tag (GA4), one GA4 event tag for all events above, Meta Pixel base/Lead/Contact tags (only fire with advertising consent, skipped until the Pixel ID is set).
After import, edit the constant variable **Const - Meta Pixel ID**. **Const - GA4 Measurement ID** is prefilled.

## Leads table
New columns: gclid, fbclid, fbp, fbc, ga_client_id, event_id, consent. `event_id` matches the browser event so a later server-side Meta Conversions API send can de-duplicate.
