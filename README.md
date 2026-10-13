# gujaratbio.com static site

Plain HTML/CSS/JS. No build step needed to publish: upload the folder contents.
- Vercel: import this folder; vercel.json handles clean URLs, redirects, caching.
- Hostinger shared hosting: upload everything into public_html (keep .htaccess).
- Edit text in build.py, then run `python3 build.py` to regenerate pages.

Before launch: set DNS, submit /sitemap.xml in Google Search Console, add 301s for any old URLs you keep (see vercel.json / .htaccess).
Enquiry forms open WhatsApp (+91 99787 91167) or email (sales@gujaratbio.com) with the details pre-filled. Connect a CRM/form backend later if you want lead tracking.
Images in /assets/img are illustrative renderings; swap with real photographs when available (same file names).
