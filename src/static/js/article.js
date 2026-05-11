// Zdrowie.fit — strona artykułu: reading progress + TOC + scroll spy + tracker
(function () {
    'use strict';

    const bar = document.getElementById('progress-bar');
    const article = document.querySelector('.article__content');
    const tocNav = document.getElementById('article-toc');

    // ─── Server-side view tracker (niezależny od GA4 / ad-blockerów) ───
    // Pinguje backend FastAPI raz na załadowanie strony artykułu.
    // - URL backendu z <meta name="zf-backend" content="https://api.zdrowie.fit">
    // - Jeśli meta nie ma → odpada cicho (na produkcji bez backendu)
    // - CORS errors / offline / backend down — silently fail (nie zepsuje strony)
    (function trackView() {
        const path = window.location.pathname;
        const match = path.match(/\/artykuly\/([^/]+)\.html$/);
        if (!match) return;
        const slug = match[1];

        const backendMeta = document.querySelector('meta[name="zf-backend"]');
        if (!backendMeta || !backendMeta.content) return;
        const backend = backendMeta.content.replace(/\/$/, '');

        // Ping po 1.5s — eliminuje pre-fetchery i instant bounce
        setTimeout(() => {
            try {
                fetch(backend + '/api/stats/view', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    keepalive: true,
                    body: JSON.stringify({
                        slug: slug,
                        referer: document.referrer || ''
                    })
                }).catch(() => {});
            } catch (_) {}
        }, 1500);
    })();

    // ─── TOC auto-generator ───────────────────────────────
    if (tocNav && article) {
        const headings = article.querySelectorAll('h2, h3');
        if (headings.length >= 2) {
            const ol = document.createElement('ol');
            const tree = []; // [{level, li, sub}]
            headings.forEach((h, i) => {
                // Dodaj id jeśli brak
                if (!h.id) {
                    h.id = 'h-' + (h.textContent || ('s-' + i)).toLowerCase()
                        .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60);
                }
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = '#' + h.id;
                a.textContent = h.textContent;
                a.dataset.target = h.id;
                li.appendChild(a);
                const level = h.tagName === 'H2' ? 2 : 3;
                if (level === 2) { ol.appendChild(li); tree.push({level:2, el:li, sub:null}); }
                else {
                    const parent = tree[tree.length - 1];
                    if (parent) {
                        if (!parent.sub) { parent.sub = document.createElement('ol'); parent.el.appendChild(parent.sub); }
                        parent.sub.appendChild(li);
                    } else { ol.appendChild(li); }
                }
            });
            tocNav.appendChild(ol);

            // Scroll spy
            const tocLinks = tocNav.querySelectorAll('a');
            const obs = new IntersectionObserver((entries) => {
                entries.forEach(e => {
                    if (e.isIntersecting) {
                        tocLinks.forEach(l => l.classList.toggle('toc-active', l.dataset.target === e.target.id));
                    }
                });
            }, { rootMargin: '-10% 0px -70% 0px' });
            headings.forEach(h => obs.observe(h));
        } else if (tocNav.parentElement) {
            tocNav.parentElement.style.display = 'none';
        }
    }

    if (!bar || !article) return;

    function updateProgress() {
        const rect = article.getBoundingClientRect();
        const total = article.offsetHeight - window.innerHeight;
        const scrolled = -rect.top;
        if (total <= 0) { bar.style.width = '100%'; return; }
        const pct = Math.max(0, Math.min(100, (scrolled / total) * 100));
        bar.style.width = pct + '%';
    }

    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(() => { updateProgress(); ticking = false; });
            ticking = true;
        }
    }, { passive: true });

    updateProgress();

    // ─── Analytics: trigger "scroll depth" dla 25/50/75/100% ──
    const fired = new Set();
    window.addEventListener('scroll', () => {
        const rect = article.getBoundingClientRect();
        const total = article.offsetHeight - window.innerHeight;
        const scrolled = -rect.top;
        const pct = Math.round((scrolled / total) * 100);
        [25, 50, 75, 100].forEach(threshold => {
            if (pct >= threshold && !fired.has(threshold)) {
                fired.add(threshold);
                if (typeof window.gtag === 'function') {
                    window.gtag('event', 'scroll_depth', { percent: threshold });
                }
                if (typeof window.fbq === 'function' && threshold === 75) {
                    window.fbq('track', 'ViewContent');
                }
            }
        });
    }, { passive: true });
})();
