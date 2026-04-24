// Service Worker — offline-first for static assets, network-first for HTML
const CACHE_NAME = '{{ site.name | lower | replace(" ", "-") }}-v{{ now.strftime("%Y%m%d%H%M") }}';
const STATIC_ASSETS = [
    '/',
    '/css/fonts.css',
    '/css/style.css',
    '/css/domain-colors.css',
    '/js/main.js',
    '/favicon.svg',
    '/img/logo.png',
    '/manifest.json',
];

// Install: cache static assets
self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(STATIC_ASSETS))
            .then(() => self.skipWaiting())
    );
});

// Activate: clean old caches
self.addEventListener('activate', (e) => {
    e.waitUntil(
        caches.keys().then(keys =>
            Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
        ).then(() => self.clients.claim())
    );
});

// Fetch strategy:
// - Static assets (css, js, fonts, images): cache-first
// - HTML pages: network-first with cache fallback
// - API/analytics: network-only
self.addEventListener('fetch', (e) => {
    const url = new URL(e.request.url);

    // Skip non-GET and external analytics
    if (e.request.method !== 'GET') return;
    if (url.hostname.includes('google') || url.hostname.includes('facebook')) return;

    // Static assets: cache-first
    if (url.pathname.match(/\.(css|js|woff2|png|webp|jpg|svg|ico)$/)) {
        e.respondWith(
            caches.match(e.request).then(cached => cached || fetch(e.request).then(r => {
                const clone = r.clone();
                caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
                return r;
            }))
        );
        return;
    }

    // HTML: network-first
    if (e.request.headers.get('accept')?.includes('text/html')) {
        e.respondWith(
            fetch(e.request)
                .then(r => {
                    const clone = r.clone();
                    caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
                    return r;
                })
                .catch(() => caches.match(e.request).then(cached => cached || caches.match('/')))
        );
        return;
    }
});
