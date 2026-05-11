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
        // Pobierz endpoint Brevo z głównego formularza (jeśli skonfigurowany)
        var mainForm = document.querySelector('[data-newsletter-form][action]');
        var actionAttr = mainForm ? ' action="' + mainForm.getAttribute('action') + '" method="post"' : '';

        const div = document.createElement('div');
        div.className = 'exit-popup-backdrop show';
        div.innerHTML = `
            <div class="exit-popup" role="dialog" aria-labelledby="exit-title" aria-modal="true">
                <button type="button" class="exit-popup__close" aria-label="Zamknij">×</button>
                <h3 id="exit-title">Chwileczkę!</h3>
                <p>Zanim pójdziesz — odbierz <strong>cotygodniowy przegląd badań o zdrowiu</strong>. Konkret, zero spamu.</p>
                <form data-newsletter-form novalidate${actionAttr}>
                    <label for="exit-popup-email" style="display:block;font-size:0;width:1px;height:1px;overflow:hidden;position:absolute">Twój adres e-mail</label>
                    <input type="email" id="exit-popup-email" name="EMAIL" placeholder="twoj@email.pl" required autocomplete="email" inputmode="email" aria-label="Twój adres email">
                    <button type="submit" class="btn btn--primary">Zapisz</button>
                    <label style="display:flex;gap:0.5rem;align-items:flex-start;font-size:0.8rem;color:var(--color-text-muted);margin-top:0.75rem;line-height:1.4;cursor:pointer">
                        <input type="checkbox" name="OPT_IN" value="1" required aria-label="Zgoda na przetwarzanie danych" style="margin-top:0.15rem;flex-shrink:0">
                        <span>Wyrażam zgodę na przetwarzanie danych w celu otrzymywania newslettera. <a href="/polityka-prywatnosci.html#newsletter" style="color:var(--color-accent);border-bottom:1px solid currentColor">Szczegóły</a>.</span>
                    </label>
                    <p data-newsletter-status role="status" aria-live="polite" hidden style="margin-top:0.5rem;padding:0.5rem 0.75rem;border-radius:8px;font-size:0.85rem"></p>
                </form>
                <p style="font-size:0.75rem;color:var(--color-text-light);margin-top:0.75rem">Wypisujesz się jednym klikiem ze stopki każdego maila.</p>
            </div>`;
        document.body.appendChild(div);
        div.querySelector('.exit-popup__close').onclick = () => div.remove();
        div.addEventListener('click', (e) => { if (e.target === div) div.remove(); });
        // Auto-focus na email po otwarciu (a11y)
        setTimeout(function() { var inp = div.querySelector('input[type="email"]'); if (inp) inp.focus(); }, 100);
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

    // ─── Newsletter ─────────────────────────────────────────
    // Event delegation: jeden listener na document łapie też dynamicznie wstrzykiwane formy
    // (np. exit-popup, mobile-search). Działa dla każdego <form data-newsletter-form>.
    //
    // Strategia:
    //   1. Walidacja klient-side (email + zgoda RODO)
    //   2. Loading state (blokada double-submit)
    //   3. action="" → tryb "soft" (zapisujemy intencję lokalnie do czasu konfiguracji Brevo)
    //   4. action ustawione → POST classic do Brevo (double opt-in po stronie Brevo)
    //   5. GA4 'sign_up' + Meta Pixel 'Lead' (oba consent-aware przez wbudowane stuby gtag/fbq)
    function setNewsletterStatus(form, type, msg) {
        var el = form.querySelector('[data-newsletter-status]');
        if (!el) return;
        el.hidden = false;
        el.dataset.type = type;
        el.textContent = msg;
    }
    function clearNewsletterStatus(form) {
        var el = form.querySelector('[data-newsletter-status]');
        if (!el) return;
        el.hidden = true;
        el.textContent = '';
    }
    function setNewsletterLoading(form, loading) {
        var btn = form.querySelector('button[type="submit"]');
        if (!btn) return;
        btn.disabled = loading;
        if (loading) {
            btn.dataset.originalText = btn.dataset.originalText || btn.textContent;
            btn.textContent = 'Zapisujemy…';
        } else if (btn.dataset.originalText) {
            btn.textContent = btn.dataset.originalText;
        }
    }

    document.addEventListener('submit', function(e) {
        var form = e.target.closest('[data-newsletter-form]');
        if (!form) return;

        clearNewsletterStatus(form);
        var emailInput = form.querySelector('input[type="email"]');
        var consentInput = form.querySelector('input[type="checkbox"][required]');
        var email = (emailInput && emailInput.value || '').trim();

        if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            e.preventDefault();
            setNewsletterStatus(form, 'error', 'Sprawdź adres email — coś się nie zgadza.');
            if (emailInput) emailInput.focus();
            return;
        }
        if (consentInput && !consentInput.checked) {
            e.preventDefault();
            setNewsletterStatus(form, 'error', 'Zaznacz zgodę na przetwarzanie danych, żeby się zapisać.');
            consentInput.focus();
            return;
        }

        if (typeof window.gtag === 'function') {
            window.gtag('event', 'sign_up', { method: 'newsletter' });
        }
        if (typeof window.fbq === 'function') {
            window.fbq('track', 'Lead');
        }

        // Sprawdź czy jest backend URL (z meta tag <meta name="zf-backend">)
        var backendMeta = document.querySelector('meta[name="zf-backend"]');
        var backend = backendMeta ? backendMeta.content.replace(/\/$/, '') : '';

        if (backend) {
            // Backend dostępny → POST do naszego /api/newsletter (omijamy Brevo formularze)
            // Backend wysyła confirmation email przez Brevo Transactional API.
            e.preventDefault();
            setNewsletterLoading(form, true);

            fetch(backend + '/api/newsletter/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email: email,
                    consent: !!(consentInput && consentInput.checked),
                    name: null,
                    source: form.closest('.exit-popup') ? 'exit-popup' : 'form',
                })
            }).then(function(r) { return r.json().then(function(data) { return { status: r.status, data: data }; }); })
              .then(function(res) {
                  setNewsletterLoading(form, false);
                  if (res.status >= 200 && res.status < 300 && res.data.status !== 'error') {
                      setNewsletterStatus(form, 'ok', res.data.message || 'Sprawdź skrzynkę — wysłaliśmy email z linkiem aktywacyjnym.');
                      try { localStorage.setItem('zf_newsletter_subscribed', '1'); } catch(_) {}
                      form.reset();
                  } else {
                      setNewsletterStatus(form, 'error', res.data.message || 'Coś poszło nie tak — spróbuj ponownie za chwilę.');
                  }
              })
              .catch(function() {
                  setNewsletterLoading(form, false);
                  setNewsletterStatus(form, 'error', 'Nie udało się połączyć z serwerem. Sprawdź internet i spróbuj ponownie.');
              });
            return;
        }

        if (!form.getAttribute('action')) {
            // Brak backendu i brak action → soft mode (lokalne zapisanie intencji)
            e.preventDefault();
            setNewsletterLoading(form, true);
            setTimeout(function() {
                setNewsletterLoading(form, false);
                setNewsletterStatus(form, 'info', 'Newsletter ruszy lada moment — zapisaliśmy Twoje zainteresowanie.');
                try {
                    var pending = JSON.parse(localStorage.getItem('zf_newsletter_pending') || '[]');
                    pending.push({ email: email, ts: new Date().toISOString() });
                    localStorage.setItem('zf_newsletter_pending', JSON.stringify(pending));
                } catch(_) {}
                form.reset();
            }, 600);
            return;
        }

        // Action ustawione (Brevo formularz native) — Brevo zwraca JSON z redirectUrl,
        // więc robimy AJAX submission zamiast classic form POST.
        e.preventDefault();
        setNewsletterLoading(form, true);
        try { localStorage.setItem('zf_newsletter_subscribed', '1'); } catch(_) {}

        var formData = new FormData(form);
        // Brevo wymaga 'locale' field (en/pl/...) — dodaj jeśli brakuje
        if (!formData.has('locale')) formData.set('locale', 'pl');
        // Brevo śledzi pole 'email_address_check' (honeypot, zostaw puste)
        if (!formData.has('email_address_check')) formData.set('email_address_check', '');

        fetch(form.action, {
            method: 'POST',
            body: formData,
            mode: 'cors',
            credentials: 'omit',
        }).then(function(r) {
            return r.text().then(function(text) {
                var data = null;
                try { data = JSON.parse(text); } catch(_) {}
                return { status: r.status, data: data, raw: text };
            });
        }).then(function(res) {
            setNewsletterLoading(form, false);
            // Brevo response: {redirectUrl: "..."} (success) albo {status: "error", message: "..."}
            if (res.data && res.data.redirectUrl) {
                // Sukces — Brevo dał redirect URL na thanks page
                window.location.href = res.data.redirectUrl;
                return;
            }
            if (res.status >= 200 && res.status < 300) {
                setNewsletterStatus(form, 'ok',
                    'Sprawdź skrzynkę — wysłaliśmy email z linkiem aktywacyjnym (czasem ląduje w spam).');
                form.reset();
            } else {
                setNewsletterStatus(form, 'error',
                    'Coś poszło nie tak. Spróbuj ponownie za chwilę.');
            }
        }).catch(function(err) {
            setNewsletterLoading(form, false);
            // CORS error / offline / blocked → fallback na zdrowie.fit/dziekujemy.html
            // (Brevo prawdopodobnie i tak zapisał, mimo że JS nie zobaczy response)
            setNewsletterStatus(form, 'ok',
                'Sprawdź skrzynkę — wysłaliśmy email z linkiem aktywacyjnym (czasem ląduje w spam).');
            form.reset();
        });
    });

    // Wyczyść status gdy user zaczyna edytować po błędzie
    document.addEventListener('input', function(e) {
        var form = e.target.closest('[data-newsletter-form]');
        if (form && (e.target.type === 'email' || e.target.type === 'checkbox')) {
            clearNewsletterStatus(form);
        }
    });

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
    if (document.querySelector('.hero')) {
        const scrollCta = document.createElement('a');
        scrollCta.href = '#newsletter';
        scrollCta.className = 'scroll-cta';
        scrollCta.textContent = '✉ Zapisz się na newsletter';
        scrollCta.setAttribute('aria-label', 'Zapisz się na newsletter');
        scrollCta.hidden = true;
        document.body.appendChild(scrollCta);
        const hero = document.querySelector('.hero');
        const nl = document.getElementById('newsletter');
        let sticky = false;
        window.addEventListener('scroll', () => {
            const heroBottom = hero.getBoundingClientRect().bottom;
            const nlTop = nl ? nl.getBoundingClientRect().top : Infinity;
            const shouldShow = heroBottom < 0 && nlTop > window.innerHeight;
            if (shouldShow && !sticky) { scrollCta.hidden = false; scrollCta.classList.add('visible'); sticky = true; }
            else if (!shouldShow && sticky) { scrollCta.classList.remove('visible'); scrollCta.hidden = true; sticky = false; }
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

    // ─── Sticky CTA — dwa tryby: (a) po 60% scroll (default, np. artykuł),
    //                              (b) po wyjściu hero z viewportu (data-trigger="hero-out", np. money page) ─
    (function initStickyCta() {
        var cta = document.getElementById('sticky-cta');
        if (!cta) return;
        var dismissed = false;
        var DISMISS_KEY = 'sticky-cta-dismissed';
        // Respektuj wcześniejsze zamknięcie w tej sesji
        try { if (sessionStorage.getItem(DISMISS_KEY) === '1') dismissed = true; } catch (e) {}

        var show = function () {
            if (dismissed) return;
            cta.removeAttribute('hidden');
            cta.setAttribute('aria-hidden', 'false');
            requestAnimationFrame(function () { cta.setAttribute('data-visible', ''); });
        };

        var closeBtn = cta.querySelector('.sticky-cta__close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function () {
                cta.removeAttribute('data-visible');
                cta.setAttribute('hidden', '');
                dismissed = true;
                try { sessionStorage.setItem(DISMISS_KEY, '1'); } catch (e) {}
            });
        }

        var trigger = cta.getAttribute('data-trigger') || 'scroll-60';

        if (trigger === 'hero-out') {
            var hero = document.querySelector('.hero');
            if (hero && 'IntersectionObserver' in window) {
                var io = new IntersectionObserver(function (entries) {
                    entries.forEach(function (e) { if (!e.isIntersecting) show(); });
                }, { threshold: 0, rootMargin: '0px 0px -10% 0px' });
                io.observe(hero);
            } else {
                // Fallback: pokaż po 25% scroll
                window.addEventListener('scroll', function () {
                    if (window.scrollY > window.innerHeight * 0.6) show();
                }, { passive: true });
            }
        } else {
            window.addEventListener('scroll', function () {
                if (dismissed) return;
                var denom = document.documentElement.scrollHeight - window.innerHeight;
                if (denom <= 0) return;
                var scrollPercent = window.scrollY / denom;
                if (scrollPercent > 0.6) show();
            }, { passive: true });
        }
    })();

    // ─── Cite button (APA 7) ───────────────────────────────
    (function initCite() {
        var months = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca',
                      'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia'];
        document.addEventListener('click', function (e) {
            var btn = e.target.closest('[data-cite]');
            if (!btn) return;
            var author = btn.dataset.author || '';
            var title = btn.dataset.title || '';
            var site = btn.dataset.site || '';
            var url = btn.dataset.url || '';
            var date = btn.dataset.date || '';
            var year = date ? date.substring(0, 4) : String(new Date().getFullYear());
            var monthNum = date ? parseInt(date.substring(5, 7), 10) : 0;
            var day = date ? parseInt(date.substring(8, 10), 10) : 0;
            var dateStr = (day && monthNum) ? (day + ' ' + months[monthNum - 1] + ' ' + year) : year;
            // APA 7: Autor. (rok, data). Tytuł artykułu. Nazwa Serwisu. URL
            var citation = author + '. (' + dateStr + '). ' + title + '. ' + site + '. ' + url;
            var output = btn.nextElementSibling;
            if (output) {
                output.hidden = false;
                output.textContent = citation;
                output.style.userSelect = 'all';
            }
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(citation).catch(function () {});
            }
        });
    })();

    // ─── Share bar (article__share) ──────────────────────────
    (function initShare() {
        // Web Share API detection
        if (navigator.share) {
            document.querySelectorAll('[data-share="native"]').forEach(function(btn) {
                btn.hidden = false;
                btn.dataset.supported = '';
            });
        }

        document.addEventListener('click', function(e) {
            var btn = e.target.closest('[data-share]');
            if (!btn) return;

            var action = btn.dataset.share;

            if (action === 'copy') {
                e.preventDefault();
                var url = btn.dataset.url;
                navigator.clipboard.writeText(url).then(function() {
                    var label = btn.querySelector('.share-btn__label');
                    var copied = btn.querySelector('.share-btn__copied');
                    if (label && copied) {
                        label.hidden = true;
                        copied.hidden = false;
                        setTimeout(function() { label.hidden = false; copied.hidden = true; }, 2000);
                    }
                }).catch(function() {
                    // Fallback for older browsers
                    var ta = document.createElement('textarea');
                    ta.value = btn.dataset.url;
                    ta.style.position = 'fixed';
                    ta.style.opacity = '0';
                    document.body.appendChild(ta);
                    ta.select();
                    document.execCommand('copy');
                    document.body.removeChild(ta);
                });
            }

            if (action === 'native') {
                e.preventDefault();
                navigator.share({
                    title: btn.dataset.title,
                    text: btn.dataset.text,
                    url: btn.dataset.url
                }).catch(function() {}); // User cancelled
            }

            // Track share events via GA4
            if (action !== 'copy' && action !== 'native' && typeof gtag === 'function') {
                gtag('event', 'share', { method: action, content_type: 'article', item_id: window.location.pathname });
            }
        });
    })();
})();
