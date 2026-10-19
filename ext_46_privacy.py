# Privacy and cookies page. Plain facts about what the site and chat collect, who processes it, and how to opt out.
_pv = f'''<div class="prose">
<p><b>Last updated: 19 October 2026.</b> This page explains what {NAME} ("we") collects when you use b2b.gujaratbio.com, why, and the choices you have. Questions or requests: <a href="mailto:{MAIL}">{MAIL}</a>.</p>

<h2>What we collect</h2>
<ul>
<li><b>What you send us.</b> When you fill in an enquiry form or use the chat, we receive what you type: for example your name, company, phone or WhatsApp number, email, country, the products you want, quantity, and your message. The chat conversation is stored with your enquiry.</li>
<li><b>Where you came from.</b> The page you were on, the website or advert that sent you (including campaign tags and an advert click ID if you arrived from an advert), and your time zone. We keep this with your enquiry so we know which marketing works.</li>
<li><b>How the site is used.</b> If you allow analytics cookies, Google Analytics records pages viewed, buttons clicked and device and approximate location. If you allow advertising cookies, advertising measurement tags (for example Meta Pixel) may record that you visited or sent an enquiry.</li>
</ul>

<h2>Why we use it</h2>
<ul>
<li>To reply to your enquiry, send a quote or a sample, and follow up.</li>
<li>To understand which pages and advertisements bring genuine enquiries, and to improve the site.</li>
<li>To keep the site secure and stop spam.</li>
</ul>
<p>We do not sell your details.</p>

<h2>Who handles data for us</h2>
<p>We use these services to run the site. Each processes data on our behalf, in their own locations:</p>
<ul>
<li>Hostinger (website hosting)</li>
<li>Supabase (database where enquiries and chat records are stored)</li>
<li>Resend (sending email notifications and replies)</li>
<li>Anthropic (the AI model that writes the chat assistant's replies; your chat messages are sent to it)</li>
<li>Google (Analytics and Tag Manager) and, if we run adverts, Meta, only as described under cookies</li>
<li>Internal alert tools that tell our sales team a new enquiry has arrived</li>
</ul>
<p>The chat assistant is an AI. It cannot give prices or dosages, and our team confirms everything before you buy. Please do not type payment details, passwords or ID numbers into the chat or forms.</p>

<h2>Cookies and similar storage</h2>
{table(["Name", "Set by", "Purpose", "Kept for"], [
  ["_ga, _ga_*", "Google Analytics", "Counts visits and pages, measures what helps", "Up to 2 years"],
  ["_fbp, _fbc", "Meta Pixel (advertising)", "Measures whether advert clicks lead to enquiries", "Up to 90 days"],
  ["gbo_utm_*, gbo_ref, gbo_landing, gbo_gclid, gbo_fbclid", "This site (browser storage)", "Remembers where you first came from so we can attach it to your enquiry", "Until you clear your browser"],
  ["gbo_consent", "This site (browser storage)", "Remembers your cookie choice", "Until you clear your browser"],
  ["gbo_chat_*", "This site (session storage)", "Keeps your chat on screen while you browse", "Until you close the tab"]])}
<p>Visitors in Europe and the UK are asked before analytics and advertising cookies are used. Elsewhere they are on by default and you can switch them off at any time: <button type="button" class="linkbtn" style="color:#0f5d4f" data-cookie-settings>change your cookie choice</button>. Declining does not stop you using the site or sending an enquiry.</p>

<h2>How long we keep it</h2>
<p>We keep enquiry and chat records for as long as we need them to deal with you and for ordinary business records. You can ask us to delete them sooner.</p>

<h2>Your choices</h2>
<p>You can ask us to show you the details we hold, correct them, delete them, or stop contacting you, and you can withdraw cookie consent at any time. Email <a href="mailto:{MAIL}">{MAIL}</a> from the address you used and we will act on it. We aim to follow the data protection laws that apply to us, including India's Digital Personal Data Protection Act, 2023.</p>

<h2>Who we are</h2>
<p>{NAME}. Registered office: {REGOFF}. CIN {CIN}.</p>
</div>'''

page("/privacy-policy", "Privacy and Cookies | Gujarat Bio Organics",
     "What Gujarat Bio Organics collects through its website, enquiry forms and chat assistant, how cookies are used, and how to change your choices or ask us to delete your details.",
     page_hero("Privacy and cookies", "What we collect, why, and the choices you have.", "/privacy-policy", "Privacy and cookies") + sec(_pv),
     [("Privacy and cookies", None)], None, "0.2")
