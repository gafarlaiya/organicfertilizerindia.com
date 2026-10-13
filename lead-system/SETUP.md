# Lead capture setup (about 5 minutes, free)

1. Create a new Google Sheet named "GBO Leads".
2. Extensions > Apps Script. Delete the sample code, paste all of `Code.gs`. Change OWNER_EMAIL if needed.
3. Select `testLead` in the function dropdown, click Run, and allow permissions. A test row and an alert email should appear.
4. Deploy > New deployment > type "Web app". Execute as: Me. Who has access: Anyone. Deploy and copy the Web app URL.
5. Open `assets/main.js`, set `var LEAD_ENDPOINT='<that URL>';`, rebuild the zip, and upload it again.
6. Submit a form on the live site. A row should appear in the Leads tab.

Notes
- The visitor still gets WhatsApp/email opened as before; the lead is saved at the same moment.
- Auto-reply email is sent only when the form collects an email address.
- Stages (dropdown), score, priority (Hot/Warm/Cold) and next follow-up date are filled automatically.
- Later, the same endpoint can be replaced by an n8n webhook without changing the site.
