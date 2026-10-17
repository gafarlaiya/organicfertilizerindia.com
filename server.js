// Zero-dependency static server: clean URLs, 301 redirects, 404 page, caching.
const http = require('http'), fs = require('fs'), path = require('path');
const ROOT = __dirname, PORT = process.env.PORT || 3000;
const MIME = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'application/javascript; charset=utf-8','.svg':'image/svg+xml','.webp':'image/webp','.png':'image/png','.jpg':'image/jpeg','.xml':'application/xml','.txt':'text/plain; charset=utf-8','.json':'application/json','.ico':'image/x-icon'};
const REDIRECTS = {
"/sugarcane": "/crops/sugarcane",
"/sugarcane1": "/crops/sugarcane",
"/sugarcane-farming": "/crops/sugarcane",
"/sugarcane-farming1": "/crops/sugarcane",
"/sugarcane-hindi": "/crops/sugarcane",
"/sugarcane-gujarati": "/crops/sugarcane",
"/sugarcane-cultivation-guide": "/crops/sugarcane",
"/sugarcane-special": "/crops/sugarcane",
"/immunity-sugarcane-special": "/crops/sugarcane",
"/best-fertilizer-for-sugarcane-farming": "/crops/sugarcane",
"/sugarcane-production-in-india-current-scenario-and-way-ahead": "/crops/sugarcane",
"/sugarcane-blog-gujarati": "/crops/sugarcane",
"/sugarcane-blog-english": "/crops/sugarcane",
"/potato": "/crops/potato",
"/potato-copy": "/crops/potato",
"/potato-hindi-lp": "/crops/potato",
"/potato-farming-solution": "/crops/potato",
"/potato-cultivation-guide": "/crops/potato",
"/best-fertilizer-for-potato-farming": "/crops/potato",
"/blog-maximizing-potato-tuber-production": "/crops/potato",
"/immunity-potato-special-organic-fertilizer-1l": "/crops/potato",
"/mango": "/crops/mango",
"/mango-special": "/crops/mango",
"/mango-fertilizer-schedule": "/crops/mango",
"/best-fertilizer-for-mango-farming": "/crops/mango",
"/immunity-mango-special-organic-fertilizer-1l": "/crops/mango",
"/immunity-mango-special-recovery-kit": "/crops/mango",
"/apple": "/crops/apple",
"/best-fertilizer-for-apple-farming-root-rot": "/crops/apple",
"/immunity-apple-special-organic-fertilizer-1l": "/crops/apple",
"/blog-rootrot-understanding-rootrot": "/crops/apple",
"/blog-rootrot-effects-on-farmers": "/crops/apple",
"/blog-rootrot-economical-effects": "/crops/apple",
"/banana-farming": "/crops/banana",
"/blog-banana-farming-poor-soil": "/crops/banana",
"/immunity-banana-special-organic-fertilizer": "/crops/banana",
"/coconut": "/crops/coconut",
"/best-fertilizer-for-coconut-farming": "/crops/coconut",
"/citrus": "/crops/citrus",
"/immunity-citrus-special-organic-fertilizer-1l": "/crops/citrus",
"/cotton": "/crops/cotton",
"/blog-post27-cotton-5-mistakes-hn": "/crops/cotton",
"/store": "/crop-specific-fertilizers",
"/groundnut": "/crop-specific-fertilizers",
"/cumin": "/crop-specific-fertilizers",
"/cumin-aa": "/crop-specific-fertilizers",
"/best-fertilizer-for-cumin-farming": "/crop-specific-fertilizers",
"/immunity-cumin-special-organic-fertilizer-1l": "/crop-specific-fertilizers",
"/onions": "/crop-specific-fertilizers",
"/onion-special": "/crop-specific-fertilizers",
"/onion-special-en-copy": "/crop-specific-fertilizers",
"/best-fertilizer-for-onion-farming": "/crop-specific-fertilizers",
"/immunity-onion-special-organic-fertilizer-1l": "/crop-specific-fertilizers",
"/chili": "/crop-specific-fertilizers",
"/chili-blog-english": "/crop-specific-fertilizers",
"/tea-special": "/crop-specific-fertilizers",
"/vegetable-special": "/crop-specific-fertilizers",
"/vegetables": "/crop-specific-fertilizers",
"/immunity-vegetable-special-organic-fertilizer-1l": "/crop-specific-fertilizers",
"/dhanya-specoal": "/crop-specific-fertilizers",
"/immunity-fruit-special-organic-fertilizer-1l": "/crop-specific-fertilizers",
"/gold": "/crop-specific-fertilizers",
"/immunity-gold-1l": "/crop-specific-fertilizers",
"/horticulture-crops": "/crop-specific-fertilizers",
"/agri-crops": "/crop-specific-fertilizers",
"/agriculture-organic-fertilizers": "/organic-fertilizer-manufacturer-india",
"/horticulture-organic-fertilizers": "/organic-fertilizer-manufacturer-india",
"/blog-post-importance-of-composting": "/organic-fertilizer-manufacturer-india",
"/blog-composting-non-negotiable": "/organic-fertilizer-manufacturer-india",
"/blog-organic-farming-and-yields": "/organic-fertilizer-manufacturer-india",
"/granules": "/zyme-granules-manufacturer",
"/immunity-granules": "/zyme-granules-manufacturer",
"/immunity-granules-8-kg-bag": "/zyme-granules-manufacturer",
"/soil-detox": "/field-solutions",
"/nutrients-locked-in-soil": "/field-solutions",
"/is-your-fertilizer-a-waste-of-money": "/field-solutions",
"/blog-role-of-soil": "/field-solutions",
"/calculator": "/field-solutions",
"/fertilizer-dosage-calculator": "/field-solutions",
"/bog-n-p-k": "/resources/biostimulant-vs-fertilizer-vs-biofertilizer",
"/blog-bio-stimulants-potential": "/resources/what-is-a-biostimulant",
"/blog-post-bio-stimulants-reducing-dead-zones": "/resources/what-is-a-biostimulant",
"/blog-top-10-biofertilizer-manufacturers-of-india": "/biofertilisers-manufacturer-india",
"/bio-stimulants-manufacturer-in-india": "/biostimulants-manufacturer-india",
"/product": "/products",
"/products-list": "/products",
"/bio-stimulants-products": "/products",
"/bio-stimulants": "/products",
"/order": "/products",
"/order-place": "/products",
"/bio-stimulants-wholesale": "/bulk-supply",
"/dealer": "/become-a-distributor",
"/chili-contact": "/contact",
"/quote1": "/contact",
"/chili-thank-you": "/contact",
"/terms-and-conditions": "/contact",
"/shipping-policy": "/contact",
"/testimonials": "/about",
"/testimonials-1": "/about",
"/gallery": "/about",
"/downloads": "/about",
"/employees": "/about",
"/page": "/",
"/page12": "/",
"/111": "/",
"/mlp": "/",
"/classic-cap-hpeszv": "/",
"/deletion": "/",
"/services": "/",
"/services1": "/",
"/services2": "/",
"/services3": "/",
"/landing1": "/",
"/landing2": "/",
"/landing3": "/",
"/blog-post": "/"
};
function redirectFor(p) {
  if (REDIRECTS[p]) return REDIRECTS[p];
  const lang = p.match(/^\/(gu|hi)(\/.*)?$/);           // old Gujarati/Hindi copies
  if (lang) { const rest = lang[2] || '/'; return REDIRECTS[rest] || (/^\/blog-post/.test(rest) ? '/resources' : '/'); }
  if (/^\/blog-post\d*$/.test(p) || /^\/blog-/.test(p)) return '/resources';
  return null;
}
function send(res, code, file, extra) {
  fs.readFile(file, (e, buf) => {
    if (e) { res.writeHead(500); return res.end('Server error'); }
    const ext = path.extname(file);
    const h = Object.assign({'Content-Type': MIME[ext] || 'application/octet-stream', 'X-Content-Type-Options': 'nosniff'}, extra || {});
    h['Cache-Control'] = ext === '.html' ? 'public, max-age=300' : 'public, max-age=31536000, immutable';
    res.writeHead(code, h); res.end(buf);
  });
}
http.createServer((req, res) => {
  let p; try { p = decodeURIComponent(new URL(req.url, 'http://x').pathname); } catch (e) { res.writeHead(400); return res.end('Bad request'); }
  if (p.length > 1 && p.endsWith('/')) p = p.slice(0, -1);
  const to = redirectFor(p); if (to && to !== p) { res.writeHead(301, {Location: to}); return res.end(); }
  const full = path.normalize(path.join(ROOT, p));
  if (!full.startsWith(ROOT) || /(^|\/)\.|server\.js$|package\.json$|\.py$|\.md$|\.gs$|^\/lead-system/.test(p)) return send(res, 404, path.join(ROOT, '404.html'));
  fs.stat(full, (e, st) => {
    if (!e && st.isFile()) return send(res, 200, full);
    const idx = path.join(full, 'index.html');
    fs.stat(idx, (e2, st2) => (!e2 && st2.isFile()) ? send(res, 200, idx) : send(res, 404, path.join(ROOT, '404.html')));
  });
}).listen(PORT, () => console.log('Listening on ' + PORT));
