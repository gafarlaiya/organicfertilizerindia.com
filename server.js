// Zero-dependency static server: clean URLs, 301 redirects, 404 page, caching.
const http = require('http'), fs = require('fs'), path = require('path');
const ROOT = __dirname, PORT = process.env.PORT || 3000;
const MIME = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'application/javascript; charset=utf-8','.svg':'image/svg+xml','.webp':'image/webp','.png':'image/png','.jpg':'image/jpeg','.xml':'application/xml','.txt':'text/plain; charset=utf-8','.json':'application/json','.ico':'image/x-icon'};
const REDIRECTS = {
  '/bio-stimulants-manufacturer-in-india':'/biostimulants-manufacturer-india','/bio-stimulants-wholesale':'/bulk-supply','/dealer':'/become-a-distributor',
  '/product':'/products','/products-list':'/products','/bio-stimulants-products':'/products','/bio-stimulants':'/products','/chili-contact':'/contact','/quote1':'/contact'
};
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
  if (REDIRECTS[p]) { res.writeHead(301, {Location: REDIRECTS[p]}); return res.end(); }
  const full = path.normalize(path.join(ROOT, p));
  if (!full.startsWith(ROOT) || /(^|\/)\.|server\.js$|package\.json$|\.py$|\.md$|\.gs$|^\/lead-system/.test(p)) return send(res, 404, path.join(ROOT, '404.html'));
  fs.stat(full, (e, st) => {
    if (!e && st.isFile()) return send(res, 200, full);
    const idx = path.join(full, 'index.html');
    fs.stat(idx, (e2, st2) => (!e2 && st2.isFile()) ? send(res, 200, idx) : send(res, 404, path.join(ROOT, '404.html')));
  });
}).listen(PORT, () => console.log('Listening on ' + PORT));
