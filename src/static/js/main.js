// Zdrowie.fit — wspólny skrypt (menu, consent, newsletter, share, dark mode, exit-intent)
(function () {
    'use strict';

    // ─── Dark mode toggle ──────────────────────────────────
    const THEME_KEY = 'zf_theme';
    const root = document.documentElement;
    const savedTheme = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) root.classList.add('dark');
    const themeToggle = document.createElement('button');
    themeToggle.className = 'theme-toggle';
    themeToggle.setAttribute('aria-label', 'Przełącz tryb jasny/ciemny');
    themeToggle.innerHTML = root.classList.contains('dark') ? '☀' : '🌙';
    themeToggle.addEventListener('click', () => {
        root.classList.toggle('dark');
        const isDark = root.classList.contains('dark');
        localStorage.setItem(THEME_KEY, isDark ? 'dark' : 'light');
        themeToggle.innerHTML = isDark ? '☀' : '🌙';
    });
    document.body.appendChild(themeToggle);

    // ─── Exit-intent popup (desktop tylko) ─────────────────
    const EXIT_SHOWN_KEY = 'zf_exit_shown';
    const hasNewsletter = document.getElementById('newsletter');
    const isDesktop = window.matchMedia('(min-width: 781px)').matches;
    if (hasNewsletter && isDesktop && !sessionStorage.getItem(EXIT_SHOWN_KEY) && !localStorage.getItem('zf_newsletter_subscribed')) {
        const handleExit = (e) => {
            if (e.clientY < 10 && !document.querySelector('.exit-popup-backdrop')) {
                showExitPopup();
                sessionStorage.setItem(EXIT_SHOWN_KEY, '1');
                document.removeEventListener('mouseout', handleExit);
            }
        };
        setTimeout(() => document.addEventListener('mouseout', handleExit), 15000);  // po 15s od załadowania
    }
    function showExitPopup() {
        const div = document.createElement('div');
        div.className = 'exit-popup-backdrop show';
        div.innerHTML = `
            <div class="exit-popup" role="dialog" aria-labelledby="exit-title">
                <button type="button" class="exit-popup__close" aria-label="Zamknij">×</button>
                <h3 id="exit-title">Chwileczkę!</h3>
                <p>Zanim pójdziesz — odbierz <strong>cotygodniowy przegląd badań o zdrowiu</strong>. Konkret, zero spamu.</p>
                <form data-newsletter-form novalidate>
                    <input type="email" placeholder="twoj@email.pl" required>
                    <button type="submit" class="btn btn--primary">Zapisz</button>
                </form>
                <p style="font-size:0.75rem;color:var(--color-text-light);margin-top:0.75rem">Wypisujesz się jednym klikiem.</p>
            </div>`;
        document.body.appendChild(div);
        div.querySelector('.exit-popup__close').onclick = () => div.remove();
        div.addEventListener('click', (e) => { if (e.target === div) div.remove(); });
    }

    // ─── Mobile nav ────────────────────────────────────────
    const toggle = document.querySelector('.nav__toggle');
    const list = document.querySelector('.nav__list');
    if (toggle && list) {
        toggle.addEventListener('click', () => {
            const open = list.classList.toggle('active');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        // Zamknij menu po kliknięciu linka
        list.querySelectorAll('a').forEach(a => a.addEventListener('click', () => list.classList.remove('active')));
    }

    // ─── Cookie consent (RODO) ─────────────────────────────
    const CONSENT_KEY = 'zf_cookie_consent';
    const banner = document.getElementById('cookie-consent');
    const consent = localStorage.getItem(CONSENT_KEY);

    if (banner) {
        if (!consent) {
            banner.hidden = false;
        }
        banner.querySelectorAll('[data-consent]').forEach(btn => {
            btn.addEventListener('click', () => {
                const val = btn.getAttribute('data-consent');
                localStorage.setItem(CONSENT_KEY, val);
                localStorage.setItem(CONSENT_KEY + '_date', new Date().toISOString());
                banner.hidden = true;
                if (val === 'accept' && typeof window.gtag === 'function') {
                    window.gtag('consent', 'update', { analytics_storage: 'granted', ad_storage: 'granted' });
                }
                if (val === 'reject' && typeof window.gtag === 'function') {
                    window.gtag('consent', 'update', { analytics_storage: 'denied', ad_storage: 'denied' });
                }
            });
        });
    }

    // ─── Newsletter (klient-side fallback jeśli brak endpointu) ──
    const nlForm = document.querySelector('[data-newsletter-form]');
    if (nlForm) {
        nlForm.addEventListener('submit', (e) => {
            const email = nlForm.querySelector('input[type="email"]').value;
            const consent = nlForm.querySelector('input[type="checkbox"]');
            if (consent && !consent.checked) {
                e.preventDefault();
                alert('Zaznacz zgodę na przetwarzanie danych, aby się zapisać.');
                return;
            }
            if (!nlForm.getAttribute('action')) {
                e.preventDefault();
                alert('Newsletter zostanie uruchomiony wkrótce. Zapisaliśmy Twoje zainteresowanie.');
                // Można tu wywołać własny endpoint fetch('/api/newsletter', {method:'POST', body:...})
                console.log('[newsletter] zapis:', email);
                nlForm.reset();
            }
            // Jeśli action jest ustawione, formularz poleci klasycznym POST-em na endpoint Brevo/Mailchimp
        });
    }

    // ─── Copy URL button ─────────────────────────────────────
    document.querySelectorAll('[data-copy-url]').forEach(btn => {
        btn.addEventListener('click', async () => {
            const url = btn.getAttribute('data-copy-url');
            try {
                await navigator.clipboard.writeText(url);
                const original = btn.textContent;
                btn.textContent = '✓';
                setTimeout(() => btn.textContent = original, 1500);
            } catch (err) {
                console.warn('Clipboard niedostępne', err);
            }
        });
    });

    // ─── Sticky scroll CTA (pojawia się po opuszczeniu hero) ──
    const scrollCta = document.createElement('a');
    scrollCta.href = '#newsletter';
    scrollCta.className = 'scroll-cta';
    scrollCta.textContent = '✉ Zapisz się na newsletter';
    scrollCta.setAttribute('aria-label', 'Zapisz się na newsletter');
    // Pokaż tylko na index, po przescrollowaniu hero
    if (document.querySelector('.hero')) {
        document.body.appendChild(scrollCta);
        const hero = document.querySelector('.hero');
        const nl = document.getElementById('newsletter');
        let sticky = false;
        window.addEventListener('scroll', () => {
            const heroBottom = hero.getBoundingClientRect().bottom;
            const nlTop = nl ? nl.getBoundingClientRect().top : Infinity;
            const shouldShow = heroBottom < 0 && nlTop > window.innerHeight;
            if (shouldShow && !sticky) { scrollCta.classList.add('visible'); sticky = true; }
            else if (!shouldShow && sticky) { scrollCta.classList.remove('visible'); sticky = false; }
        }, { passive: true });
    }

    // ─── Mobile search overlay ──────────────────────────────
    const searchBtn = document.querySelector('[data-mobile-search]');
    if (searchBtn) {
        searchBtn.addEventListener('click', () => {
            let overlay = document.getElementById('mobile-search-overlay');
            if (!overlay) {
                overlay = document.createElement('div');
                overlay.id = 'mobile-search-overlay';
                overlay.className = 'mobile-search-overlay';
                overlay.innerHTML = `
                    <button type="button" class="mobile-search-overlay__close" aria-label="Zamknij">×</button>
                    <input type="search" placeholder="Szukaj artykułów..." aria-label="Szukaj">
                    <div class="mobile-search-overlay__results"></div>
                `;
                document.body.appendChild(overlay);
                overlay.querySelector('.mobile-search-overlay__close').onclick = () => overlay.classList.remove('active');
                const input = overlay.querySelector('input');
                const results = overlay.querySelector('.mobile-search-overlay__results');
                input.addEventListener('input', async () => {
                    const q = input.value.toLowerCase().trim();
                    if (q.length < 2) { results.innerHTML = ''; return; }
                    // Załaduj artykuły z /data/articles.json
                    if (!window.__zfArticles) {
                        try {
                            const r = await fetch('/data/articles.json');
                            window.__zfArticles = await r.json();
                        } catch(e) { window.__zfArticles = []; }
                    }
                    const hits = window.__zfArticles.filter(a =>
                        (a.title || '').toLowerCase().includes(q) || (a.excerpt || '').toLowerCase().includes(q)
                    ).slice(0, 8);
                    results.innerHTML = hits.length
                        ? hits.map(a => `<a href="/artykuly/${a.slug}.html"><strong>${a.title}</strong><br><small>${a.excerpt || ''}</small></a>`).join('')
                        : '<p style="padding:1rem;text-align:center;color:var(--color-text-muted)">Brak wyników</p>';
                });
                setTimeout(() => input.focus(), 100);
            }
            overlay.classList.add('active');
        });
    }

    // ─── Share event tracking (jeśli GA4 jest) ─────────────
    document.querySelectorAll('.sticky-box a[href*="facebook.com"], .sticky-box a[href*="twitter.com"], .sticky-box a[href*="linkedin.com"]').forEach(a => {
        a.addEventListener('click', () => {
            if (typeof window.gtag === 'function') {
                window.gtag('event', 'share', {
                    method: a.href.includes('facebook') ? 'Facebook' : a.href.includes('twitter') ? 'Twitter' : 'LinkedIn',
                    content_type: 'article'
                });
            }
        });
    });
})();
