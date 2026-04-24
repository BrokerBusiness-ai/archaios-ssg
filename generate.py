#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator strony "Zdrowie Fit" z Schema.org i systemem artykułów
"""

import os
import json
from datetime import datetime

# ================= KONFIGURACJA =================
PROJECT_NAME = "zdrowie-fit"
DOMAIN = "https://zdrowie-fit.pl"
AUTHOR = "Zdrowie Fit Team"
# ================================================

def create_folder_structure():
    """Tworzy strukturę folderów projektu"""
    folders = [
        PROJECT_NAME,
        f"{PROJECT_NAME}/css",
        f"{PROJECT_NAME}/js",
        f"{PROJECT_NAME}/articles",
        f"{PROJECT_NAME}/img",
        f"{PROJECT_NAME}/data"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print(f"✅ Utworzono strukturę folderów: {PROJECT_NAME}/")

def generate_schema_org_website():
    """Generuje JSON-LD dla całej strony"""
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Zdrowie Fit",
        "url": DOMAIN,
        "description": "Holistyczne podejście do zdrowia: połączenie zdrowia fizycznego i psychicznego",
        "publisher": {
            "@type": "Organization",
            "name": "Zdrowie Fit",
            "logo": {
                "@type": "ImageObject",
                "url": f"{DOMAIN}/img/logo.png"
            }
        },
        "potentialAction": {
            "@type": "SearchAction",
            "target": f"{DOMAIN}/search?q=" + "{search_term_string}",
            "query-input": "required name=search_term_string"
        }
    }

def generate_article_schema(title, description, date_published, image_url, author=AUTHOR):
    """Generuje JSON-LD dla pojedynczego artykułu"""
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "image": image_url,
        "datePublished": date_published,
        "dateModified": date_published,
        "author": {
            "@type": "Person",
            "name": author
        },
        "publisher": {
            "@type": "Organization",
            "name": "Zdrowie Fit",
            "logo": {
                "@type": "ImageObject",
                "url": f"{DOMAIN}/img/logo.png"
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"{DOMAIN}/articles/{title.lower().replace(' ', '-')}.html"
        }
    }

def generate_index_html():
    """Generuje główną stronę z listą artykułów i Schema.org"""
    schema_website = json.dumps(generate_schema_org_website(), ensure_ascii=False, indent=2)
    year = datetime.now().year

    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zdrowie Fit – Ciało i Umysł w Harmonii</title>
    <meta name="description" content="Odkryj połączenie zdrowia fizycznego i psychicznego. Praktyczne porady, badania i inspiracje dla holistycznego wellbeing.">

    <!-- Schema.org WebSite -->
    <script type="application/ld+json">
    {schema_website}
    </script>

    <!-- Open Graph -->
    <meta property="og:title" content="Zdrowie Fit – Ciało i Umysł w Harmonii">
    <meta property="og:description" content="Holistyczne podejście do zdrowia: fizyczne + psychiczne">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{DOMAIN}">

    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Skip to content -->
    <a href="#main-content" class="skip-link">Przejdź do treści</a>

    <!-- Header -->
    <header class="header" role="banner">
        <div class="container header__inner">
            <a href="/" class="logo" aria-label="Zdrowie Fit – strona główna">
                <span class="logo__text">Zdrowie<span class="logo__accent">Fit</span></span>
            </a>
            <nav class="nav" role="navigation" aria-label="Główna nawigacja">
                <ul class="nav__list">
                    <li><a href="/" class="nav__link nav__link--active">Start</a></li>
                    <li><a href="#about" class="nav__link">O nas</a></li>
                    <li><a href="articles.html" class="nav__link">Artykuły</a></li>
                    <li><a href="#contact" class="nav__link">Kontakt</a></li>
                </ul>
                <button class="nav__toggle" aria-label="Menu" aria-expanded="false">☰</button>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <main id="main-content">
        <section class="hero" aria-labelledby="hero-title">
            <div class="container hero__content">
                <h1 id="hero-title">Twoje ciało i umysł to <span class="highlight">jedno</span></h1>
                <p class="hero__subtitle">Odkryj, jak dbanie o formę fizyczną transformuje Twoje zdrowie psychiczne i odwrotnie. Holistyczne podejście do wellbeing.</p>
                <div class="hero__cta">
                    <a href="articles.html" class="btn btn--primary">Przeczytaj artykuły</a>
                    <a href="#synergy" class="btn btn--secondary">Dowiedz się więcej</a>
                </div>
            </div>
        </section>

        <!-- Synergy Section -->
        <section id="synergy" class="section" aria-labelledby="synergy-title">
            <div class="container">
                <h2 id="synergy-title">Synergia ciała i umysłu</h2>
                <div class="cards-grid">
                    <article class="card" itemscope itemtype="https://schema.org/Article">
                        <div class="card__icon">🏃</div>
                        <h3 itemprop="headline">Ruch a endorfiny</h3>
                        <p itemprop="description">Aktywność fizyczna stymuluje wydzielanie endorfin – naturalnych leków na stres. Regularny trening redukuje objawy lęku i depresji.</p>
                        <meta itemprop="datePublished" content="2026-01-15">
                        <a href="articles.html" class="card__link" itemprop="url">Czytaj więcej →</a>
                    </article>
                    <article class="card" itemscope itemtype="https://schema.org/Article">
                        <div class="card__icon">😴</div>
                        <h3 itemprop="headline">Sen a regeneracja</h3>
                        <p itemprop="description">Jakościowy sen to czas na naprawę mięśni i konsolidację pamięci. Brak snu osłabia odporność i zwiększa ryzyko wypalenia.</p>
                        <meta itemprop="datePublished" content="2026-01-20">
                        <a href="articles.html" class="card__link" itemprop="url">Czytaj więcej →</a>
                    </article>
                    <article class="card" itemscope itemtype="https://schema.org/Article">
                        <div class="card__icon">🥗</div>
                        <h3 itemprop="headline">Dieta a klarowność</h3>
                        <p itemprop="description">To, co jesz, wpływa na neuroprzekaźniki. Omega-3, antyoksydanty i probiotyki wspierają funkcje poznawcze i nastrój.</p>
                        <meta itemprop="datePublished" content="2026-02-01">
                        <a href="articles.html" class="card__link" itemprop="url">Czytaj więcej →</a>
                    </article>
                </div>
            </div>
        </section>

        <!-- Articles Preview -->
        <section class="section section--light" aria-labelledby="articles-title">
            <div class="container">
                <h2 id="articles-title">Najnowsze artykuły</h2>
                <div id="articles-preview" class="articles-preview" aria-live="polite">
                    <p class="loading">Ładowanie artykułów...</p>
                </div>
                <div class="text-center">
                    <a href="articles.html" class="btn btn--outline">Zobacz wszystkie artykuły</a>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="section" aria-labelledby="about-title">
            <div class="container about">
                <div class="about__content">
                    <h2 id="about-title">Dlaczego holistyczne podejście?</h2>
                    <p>Nie da się oddzielić zdrowia fizycznego od psychicznego. Nasz organizm działa jak system naczyń połączonych – stres wpływa na odporność, a brak ruchu na nastrój.</p>
                    <p>W <strong>Zdrowie Fit</strong> łączymy wiedzę z psychologii, dietetyki i fizjoterapii, aby dostarczać Ci praktycznych, opartych na badaniach wskazówek.</p>
                </div>
                <div class="about__stats">
                    <div class="stat">
                        <span class="stat__number">150+</span>
                        <span class="stat__label">Artykułów</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">30k</span>
                        <span class="stat__label">Czytelników</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">4.9★</span>
                        <span class="stat__label">Ocena</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer" role="contentinfo">
        <div class="container footer__inner">
            <div class="footer__brand">
                <span class="logo__text">Zdrowie<span class="logo__accent">Fit</span></span>
                <p>Ciało i umysł w harmonii – każdego dnia.</p>
            </div>
            <nav class="footer__nav" aria-label="Stopka">
                <a href="/">Start</a>
                <a href="articles.html">Artykuły</a>
                <a href="#about">O nas</a>
                <a href="#contact">Kontakt</a>
            </nav>
            <p class="footer__copyright">&copy; {year} Zdrowie Fit. Wszelkie prawa zastrzeżone.</p>
        </div>
    </footer>

    <script src="js/main.js"></script>
    <script>
        const breadcrumbSchema = {{
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [{{
                "@type": "ListItem",
                "position": 1,
                "name": "Start",
                "item": "{DOMAIN}"
            }}]
        }};
        const script = document.createElement('script');
        script.type = 'application/ld+json';
        script.textContent = JSON.stringify(breadcrumbSchema);
        document.head.appendChild(script);
    </script>
</body>
</html>'''

def generate_articles_html():
    """Generuje stronę z listą artykułów"""
    return '''<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artykuły – Zdrowie Fit</title>
    <meta name="description" content="Baza wiedzy o zdrowiu fizycznym i psychicznym. Praktyczne porady, badania naukowe i inspiracje.">

    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
            "@type": "ListItem",
            "position": 1,
            "name": "Start",
            "item": "https://zdrowie-fit.pl"
        }, {
            "@type": "ListItem",
            "position": 2,
            "name": "Artykuły",
            "item": "https://zdrowie-fit.pl/articles.html"
        }]
    }
    </script>

    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header" role="banner">
        <div class="container header__inner">
            <a href="/" class="logo">
                <span class="logo__text">Zdrowie<span class="logo__accent">Fit</span></span>
            </a>
            <nav class="nav" role="navigation">
                <ul class="nav__list">
                    <li><a href="/" class="nav__link">Start</a></li>
                    <li><a href="/#about" class="nav__link">O nas</a></li>
                    <li><a href="articles.html" class="nav__link nav__link--active">Artykuły</a></li>
                    <li><a href="/#contact" class="nav__link">Kontakt</a></li>
                </ul>
                <button class="nav__toggle" aria-label="Menu">☰</button>
            </nav>
        </div>
    </header>

    <main id="main-content">
        <section class="section section--page">
            <div class="container">
                <h1>Wszystkie artykuły</h1>
                <p class="section__subtitle">Eksploruj naszą bazę wiedzy o holistycznym zdrowiu</p>

                <div class="articles__filters">
                    <button class="filter-btn active" data-filter="all">Wszystkie</button>
                    <button class="filter-btn" data-filter="fizyczne">Fizyczne</button>
                    <button class="filter-btn" data-filter="psychiczne">Psychiczne</button>
                    <button class="filter-btn" data-filter="dieta">Dieta</button>
                </div>

                <div id="articles-grid" class="articles-grid" aria-live="polite">
                </div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container footer__inner">
            <span class="logo__text">Zdrowie<span class="logo__accent">Fit</span></span>
            <p>&copy; 2026 Zdrowie Fit. Wszelkie prawa zastrzeżone.</p>
        </div>
    </footer>

    <script src="js/main.js"></script>
    <script src="js/articles.js"></script>
</body>
</html>'''

def generate_article_template():
    """Szablon pojedynczego artykułu z pełnym Schema.org Article"""
    return '''<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} – Zdrowie Fit</title>
    <meta name="description" content="{{DESCRIPTION}}">

    <script type="application/ld+json" id="article-schema">
    {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{{TITLE}}",
        "description": "{{DESCRIPTION}}",
        "image": "{{IMAGE_URL}}",
        "datePublished": "{{DATE}}",
        "dateModified": "{{DATE}}",
        "author": {
            "@type": "Person",
            "name": "{{AUTHOR}}"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Zdrowie Fit",
            "logo": {
                "@type": "ImageObject",
                "url": "https://zdrowie-fit.pl/img/logo.png"
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": "https://zdrowie-fit.pl/articles/{{SLUG}}.html"
        }
    }
    </script>

    <link rel="stylesheet" href="../css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <div class="container header__inner">
            <a href="/" class="logo">
                <span class="logo__text">Zdrowie<span class="logo__accent">Fit</span></span>
            </a>
            <nav class="nav">
                <ul class="nav__list">
                    <li><a href="/" class="nav__link">Start</a></li>
                    <li><a href="/#about" class="nav__link">O nas</a></li>
                    <li><a href="../articles.html" class="nav__link nav__link--active">Artykuły</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main id="main-content" class="article-page">
        <article class="article" itemscope itemtype="https://schema.org/Article">
            <header class="article__header">
                <div class="container">
                    <nav class="breadcrumb" aria-label="Ścieżka nawigacji" itemscope itemtype="https://schema.org/BreadcrumbList">
                        <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                            <a href="/" itemprop="item"><span itemprop="name">Start</span></a>
                            <meta itemprop="position" content="1">
                        </span> /
                        <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                            <a href="../articles.html" itemprop="item"><span itemprop="name">Artykuły</span></a>
                            <meta itemprop="position" content="2">
                        </span> /
                        <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                            <span itemprop="name" id="article-title">{{TITLE}}</span>
                            <meta itemprop="position" content="3">
                        </span>
                    </nav>
                    <h1 itemprop="headline">{{TITLE}}</h1>
                    <div class="article__meta">
                        <time itemprop="datePublished" datetime="{{DATE}}">{{DATE_FORMATTED}}</time>
                        <span itemprop="author" itemscope itemtype="https://schema.org/Person">
                            Autor: <span itemprop="name">{{AUTHOR}}</span>
                        </span>
                        <span itemprop="articleSection">{{CATEGORY}}</span>
                    </div>
                </div>
            </header>

            <figure class="article__image">
                <img src="{{IMAGE_URL}}" alt="{{TITLE}}" itemprop="image">
            </figure>

            <div class="container article__content" itemprop="articleBody">
                {{CONTENT}}
            </div>

            <footer class="article__footer">
                <div class="container">
                    <div class="article__tags" itemprop="keywords">
                        {{TAGS}}
                    </div>
                    <div class="article__share">
                        <span>Udostępnij:</span>
                        <a href="#" class="share-btn" aria-label="Udostępnij na Facebooku">f</a>
                        <a href="#" class="share-btn" aria-label="Udostępnij na Twitterze">t</a>
                        <a href="#" class="share-btn" aria-label="Skopiuj link">🔗</a>
                    </div>
                </div>
            </footer>
        </article>

        <section class="section section--light">
            <div class="container">
                <h2>Przeczytaj także</h2>
                <div id="related-articles" class="cards-grid">
                </div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container footer__inner">
            <span class="logo__text">Zdrowie<span class="logo__accent">Fit</span></span>
            <p>&copy; 2026 Zdrowie Fit.</p>
        </div>
    </footer>

    <script src="../js/main.js"></script>
    <script src="../js/article.js"></script>
</body>
</html>'''

def generate_css():
    """Generuje kompletny, responsywny CSS"""
    return ''':root {
    --color-primary: #4a7c59;
    --color-primary-dark: #3a6347;
    --color-secondary: #7fb3a3;
    --color-accent: #e67e5a;
    --color-text: #2d3748;
    --color-text-light: #718096;
    --color-bg: #ffffff;
    --color-bg-alt: #f8fafc;
    --color-border: #e2e8f0;
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
    --radius: 12px;
    --transition: all 0.3s ease;
    --font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --container: 1200px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: var(--font-main); color: var(--color-text); background: var(--color-bg); line-height: 1.6; -webkit-font-smoothing: antialiased; }
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; text-decoration: none; transition: var(--transition); }
ul { list-style: none; }
button { font: inherit; cursor: pointer; border: none; background: none; }
.container { width: min(90%, var(--container)); margin-inline: auto; }
.skip-link { position: absolute; top: -40px; left: 0; background: var(--color-primary); color: white; padding: 8px 16px; z-index: 100; }
.skip-link:focus { top: 0; }
.text-center { text-align: center; }
.highlight { color: var(--color-accent); font-weight: 600; }
.section { padding: clamp(3rem, 8vw, 5rem) 0; }
.section--light { background: var(--color-bg-alt); }
.section--page { padding-top: 2rem; }
.section__subtitle { color: var(--color-text-light); margin-bottom: 1.5rem; }
.btn { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.875rem 1.5rem; border-radius: 50px; font-weight: 500; transition: var(--transition); }
.btn--primary { background: var(--color-primary); color: white; }
.btn--primary:hover { background: var(--color-primary-dark); transform: translateY(-2px); box-shadow: var(--shadow-md); }
.btn--secondary { background: white; color: var(--color-primary); border: 2px solid var(--color-primary); }
.btn--secondary:hover { background: var(--color-primary); color: white; }
.btn--outline { border: 2px solid var(--color-border); color: var(--color-text); }
.btn--outline:hover { border-color: var(--color-primary); color: var(--color-primary); }
.header { position: sticky; top: 0; z-index: 50; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-bottom: 1px solid var(--color-border); padding: 1rem 0; }
.header__inner { display: flex; justify-content: space-between; align-items: center; }
.logo__text { font-size: 1.5rem; font-weight: 700; }
.logo__accent { color: var(--color-accent); }
.nav__list { display: flex; gap: 2rem; align-items: center; }
.nav__link { font-weight: 500; color: var(--color-text-light); position: relative; }
.nav__link:hover, .nav__link--active { color: var(--color-primary); }
.nav__link--active::after { content: ''; position: absolute; bottom: -4px; left: 0; width: 100%; height: 2px; background: var(--color-primary); border-radius: 2px; }
.nav__toggle { display: none; font-size: 1.5rem; }
.hero { padding: clamp(4rem, 12vw, 8rem) 0; background: linear-gradient(135deg, var(--color-bg-alt) 0%, white 100%); text-align: center; }
.hero__content { max-width: 700px; margin-inline: auto; }
.hero h1 { font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 700; line-height: 1.2; margin-bottom: 1.5rem; }
.hero__subtitle { font-size: 1.25rem; color: var(--color-text-light); margin-bottom: 2rem; }
.hero__cta { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-top: 2rem; }
.card { background: white; padding: 2rem; border-radius: var(--radius); box-shadow: var(--shadow-sm); transition: var(--transition); border: 1px solid var(--color-border); }
.card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: var(--color-secondary); }
.card__icon { font-size: 2.5rem; margin-bottom: 1rem; }
.card h3 { font-size: 1.25rem; margin-bottom: 0.75rem; }
.card p { color: var(--color-text-light); margin-bottom: 1.25rem; }
.card__link { color: var(--color-primary); font-weight: 500; }
.articles__filters { display: flex; gap: 0.75rem; margin: 1.5rem 0 2rem; flex-wrap: wrap; }
.filter-btn { padding: 0.5rem 1.25rem; border-radius: 50px; border: 1px solid var(--color-border); background: white; font-weight: 500; transition: var(--transition); }
.filter-btn.active, .filter-btn:hover { background: var(--color-primary); color: white; border-color: var(--color-primary); }
.articles-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
.article-card { background: white; border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow-sm); border: 1px solid var(--color-border); transition: var(--transition); }
.article-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.article-card__image { height: 200px; background: linear-gradient(135deg, var(--color-secondary), var(--color-primary)); display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem; }
.article-card__content { padding: 1.5rem; }
.article-card__meta { display: flex; gap: 1rem; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.75rem; }
.article-card__category { background: var(--color-bg-alt); padding: 0.25rem 0.75rem; border-radius: 50px; font-weight: 500; }
.article-card h3 { font-size: 1.25rem; margin-bottom: 0.5rem; }
.article-card p { color: var(--color-text-light); margin-bottom: 1rem; }
.article-card__link { color: var(--color-primary); font-weight: 500; }
.article-page { padding-top: 2rem; }
.breadcrumb { display: flex; gap: 0.5rem; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 1.5rem; }
.breadcrumb a:hover { color: var(--color-primary); }
.article__header { margin-bottom: 2rem; }
.article__header h1 { font-size: clamp(1.75rem, 4vw, 2.5rem); margin-bottom: 1rem; }
.article__meta { display: flex; gap: 1.5rem; color: var(--color-text-light); font-size: 0.95rem; flex-wrap: wrap; }
.article__image { margin: 2rem 0; border-radius: var(--radius); overflow: hidden; }
.article__image img { width: 100%; height: auto; aspect-ratio: 16/9; object-fit: cover; }
.article__content { font-size: 1.125rem; line-height: 1.8; }
.article__content p { margin-bottom: 1.5rem; }
.article__content h2 { font-size: 1.5rem; margin: 2.5rem 0 1rem; }
.article__content ul { margin: 1rem 0; padding-left: 1.5rem; list-style: disc; }
.article__content li { margin-bottom: 0.5rem; }
.article__footer { border-top: 1px solid var(--color-border); padding: 2rem 0; margin-top: 3rem; }
.article__tags { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.article__tags span { background: var(--color-bg-alt); padding: 0.375rem 0.875rem; border-radius: 50px; font-size: 0.875rem; }
.article__share { display: flex; align-items: center; gap: 1rem; }
.share-btn { width: 40px; height: 40px; border-radius: 50%; background: var(--color-bg-alt); display: flex; align-items: center; justify-content: center; font-weight: 600; transition: var(--transition); }
.share-btn:hover { background: var(--color-primary); color: white; }
.about { display: grid; gap: 3rem; align-items: center; }
.about__stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; text-align: center; }
.stat__number { display: block; font-size: 2rem; font-weight: 700; color: var(--color-primary); }
.stat__label { color: var(--color-text-light); font-size: 0.95rem; }
.footer { background: var(--color-text); color: white; padding: 3rem 0 2rem; margin-top: 4rem; }
.footer__inner { display: flex; flex-direction: column; align-items: center; gap: 1.5rem; text-align: center; }
.footer__nav { display: flex; gap: 1.5rem; flex-wrap: wrap; }
.footer__nav a:hover { color: var(--color-secondary); }
.footer__copyright { color: var(--color-text-light); font-size: 0.9rem; }
.articles-preview { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 2rem; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.animate { animation: fadeInUp 0.5s ease forwards; }
@media (max-width: 768px) {
    .nav__list { position: absolute; top: 100%; left: 0; right: 0; background: white; flex-direction: column; padding: 1rem; gap: 0; border-bottom: 1px solid var(--color-border); clip-path: inset(0 0 100% 0); transition: clip-path 0.3s ease; }
    .nav__list.active { clip-path: inset(0 0 0 0); }
    .nav__toggle { display: block; }
    .nav__link { padding: 0.75rem 0; }
    .hero__cta { flex-direction: column; align-items: center; }
    .about { grid-template-columns: 1fr; }
    .article__meta { flex-direction: column; gap: 0.5rem; }
}
@media (max-width: 480px) { .about__stats { grid-template-columns: 1fr; } .articles__filters { justify-content: center; } }
:focus-visible { outline: 3px solid var(--color-accent); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } html { scroll-behavior: auto; } }
'''

def generate_main_js():
    """Generuje główny JavaScript"""
    return '''const navToggle = document.querySelector('.nav__toggle');
const navList = document.querySelector('.nav__list');
if (navToggle) {
    navToggle.addEventListener('click', () => {
        const expanded = navToggle.getAttribute('aria-expanded') === 'true';
        navToggle.setAttribute('aria-expanded', !expanded);
        navList.classList.toggle('active');
    });
}
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            if (navList) navList.classList.remove('active');
            if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
        }
    });
});
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
document.querySelectorAll('.card, .article-card, .stat').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
});
function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('pl-PL', { year: 'numeric', month: 'long', day: 'numeric' });
}
async function loadArticlesPreview(limit = 3) {
    const container = document.getElementById('articles-preview');
    if (!container) return;
    try {
        const response = await fetch('data/articles.json');
        const articles = await response.json();
        container.innerHTML = articles.slice(0, limit).map(a => `
            <article class="article-card">
                <div class="article-card__image" aria-hidden="true">${a.icon || '📝'}</div>
                <div class="article-card__content">
                    <div class="article-card__meta">
                        <time datetime="${a.date}">${formatDate(a.date)}</time>
                        <span class="article-card__category">${a.category}</span>
                    </div>
                    <h3><a href="articles/${a.slug}.html">${a.title}</a></h3>
                    <p>${a.excerpt}</p>
                    <a href="articles/${a.slug}.html" class="article-card__link">Czytaj więcej →</a>
                </div>
            </article>
        `).join('');
    } catch (e) { container.innerHTML = '<p>Nie udało się załadować artykułów.</p>'; }
}
document.addEventListener('DOMContentLoaded', () => { loadArticlesPreview(); });
'''

def generate_articles_js():
    """JavaScript do strony z listą artykułów"""
    return '''const filterBtns = document.querySelectorAll('.filter-btn');
const articlesGrid = document.getElementById('articles-grid');
let allArticles = [];
function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('pl-PL', { year: 'numeric', month: 'long', day: 'numeric' });
}
function renderArticles(articles) {
    if (!articlesGrid) return;
    if (articles.length === 0) { articlesGrid.innerHTML = '<p>Brak artykułów w tej kategorii.</p>'; return; }
    articlesGrid.innerHTML = articles.map(a => `
        <article class="article-card animate">
            <div class="article-card__image" aria-hidden="true">${a.icon || '📝'}</div>
            <div class="article-card__content">
                <div class="article-card__meta">
                    <time datetime="${a.date}">${formatDate(a.date)}</time>
                    <span class="article-card__category">${a.category}</span>
                </div>
                <h3><a href="${a.slug}.html">${a.title}</a></h3>
                <p>${a.excerpt}</p>
                <a href="${a.slug}.html" class="article-card__link">Czytaj więcej →</a>
            </div>
        </article>
    `).join('');
}
filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;
        renderArticles(filter === 'all' ? allArticles : allArticles.filter(a => a.category.toLowerCase().includes(filter)));
    });
});
async function loadArticles() {
    try {
        const response = await fetch('data/articles.json');
        allArticles = await response.json();
        renderArticles(allArticles);
    } catch (e) { if (articlesGrid) articlesGrid.innerHTML = '<p>Nie udało się załadować artykułów.</p>'; }
}
document.addEventListener('DOMContentLoaded', loadArticles);
'''

def generate_article_js():
    """JavaScript do pojedynczego artykułu"""
    return '''function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('pl-PL', { year: 'numeric', month: 'long', day: 'numeric' });
}
async function loadArticle(slug) {
    try {
        const response = await fetch('../data/articles.json');
        const articles = await response.json();
        const article = articles.find(a => a.slug === slug);
        if (!article) { document.querySelector('.article__content').innerHTML = '<p>Artykuł nie znaleziony.</p>'; return; }
        document.title = article.title + ' – Zdrowie Fit';
        const h1 = document.querySelector('.article__header h1');
        if (h1) h1.textContent = article.title;
        const meta = document.querySelector('meta[name="description"]');
        if (meta) meta.content = article.excerpt;
        const schema = document.getElementById('article-schema');
        if (schema) schema.textContent = JSON.stringify({
            "@context":"https://schema.org","@type":"Article","headline":article.title,
            "description":article.excerpt,"image":article.image,"datePublished":article.date,
            "dateModified":article.date,"author":{"@type":"Person","name":article.author},
            "publisher":{"@type":"Organization","name":"Zdrowie Fit","logo":{"@type":"ImageObject","url":"https://zdrowie-fit.pl/img/logo.png"}},
            "mainEntityOfPage":{"@type":"WebPage","@id":"https://zdrowie-fit.pl/articles/"+article.slug+".html"}
        });
        const img = document.querySelector('.article__image img');
        if (img) { img.src = article.image; img.alt = article.title; }
        const time = document.querySelector('.article__meta time');
        if (time) { time.datetime = article.date; time.textContent = formatDate(article.date); }
        const authorEl = document.querySelector('[itemprop="author"] [itemprop="name"]');
        if (authorEl) authorEl.textContent = article.author;
        const sectionEl = document.querySelector('[itemprop="articleSection"]');
        if (sectionEl) sectionEl.textContent = article.category;
        const content = document.querySelector('.article__content');
        if (content) content.innerHTML = article.content;
        const tags = document.querySelector('.article__tags');
        if (tags && article.tags) tags.innerHTML = article.tags.map(t => '<span>#'+t+'</span>').join('');
        loadRelated(article.category, article.slug);
    } catch (e) { console.error('Error:', e); }
}
async function loadRelated(category, currentSlug) {
    const container = document.getElementById('related-articles');
    if (!container) return;
    try {
        const response = await fetch('../data/articles.json');
        const articles = await response.json();
        const related = articles.filter(a => a.category === category && a.slug !== currentSlug).slice(0, 3);
        if (!related.length) { container.parentElement.style.display = 'none'; return; }
        container.innerHTML = related.map(a => '<article class="card"><div class="card__icon">'+
            (a.icon||'📝')+'</div><h3><a href="'+a.slug+'.html">'+a.title+'</a></h3><p>'+a.excerpt+
            '</p><a href="'+a.slug+'.html" class="card__link">Czytaj →</a></article>').join('');
    } catch (e) {}
}
document.addEventListener('DOMContentLoaded', () => {
    const slug = window.location.pathname.split('/').pop().replace('.html', '');
    if (slug && slug !== 'articles') loadArticle(slug);
});
'''

def generate_sample_articles():
    """Generuje przykładowe artykuły w formacie JSON"""
    return [
        {
            "slug": "jak-ruch-wplywa-na-nastroj",
            "title": "Jak ruch wpływa na nastrój? Naukowe fakty",
            "excerpt": "Regularna aktywność fizyczna to nie tylko sylwetka – to potężne narzędzie do zarządzania stresem i poprawy zdrowia psychicznego.",
            "content": "<p>Badania jednoznacznie pokazują: już 30 minut umiarkowanego wysiłku dziennie znacząco podnosi poziom endorfin i serotoniny.</p><h2>Dlaczego to działa?</h2><ul><li><strong>Endorfiny</strong> – naturalne leki przeciwbólowe</li><li><strong>BDNF</strong> – białko wspierające neuroplastyczność</li><li><strong>Redukcja kortyzolu</strong> – niższy hormon stresu</li></ul><p>Nie musisz biegać maratonów. Spacer, joga, taniec – każda forma ruchu się liczy.</p><h2>Praktyczne wskazówki</h2><p>Zacznij od 10 minut dziennie. Wybierz aktywność, która sprawia Ci przyjemność. Połącz ruch z naturą.</p>",
            "category": "Fizyczne",
            "tags": ["ruch", "endorfiny", "stres", "depresja", "neuronauka"],
            "author": "Zdrowie Fit Team",
            "date": "2026-01-15",
            "image": "https://picsum.photos/seed/mood-move/800/450",
            "icon": "🏃"
        },
        {
            "slug": "sen-regeneracja-mozgu",
            "title": "Sen: kiedy Twój mózg pracuje najciężej",
            "excerpt": "Podczas snu mózg nie odpoczywa – usuwa toksyny, konsoliduje pamięć i przygotowuje się na kolejny dzień.",
            "content": "<p>W trakcie głębokiego snu aktywowany jest system glymphatic – naturalny \"odkurzacz\" mózgu.</p><h2>Fazy snu a zdrowie</h2><ul><li><strong>NREM</strong> – regeneracja fizyczna, wzrost mięśni</li><li><strong>REM</strong> – przetwarzanie emocji, kreatywność</li></ul><p>Brak snu &lt;7h zwiększa ryzyko lęku o 30%.</p><h2>Jak spać lepiej?</h2><p>Stała pora snu, ciemna sypialnia, brak ekranów 1h przed snem, temperatura 18-20°C.</p>",
            "category": "Psychiczne",
            "tags": ["sen", "regeneracja", "mózg", "pamięć", "zdrowie"],
            "author": "Zdrowie Fit Team",
            "date": "2026-01-20",
            "image": "https://picsum.photos/seed/sleep-brain/800/450",
            "icon": "😴"
        },
        {
            "slug": "dieta-a-klarownosc-umyslu",
            "title": "Co jesz, tym myślisz: dieta a funkcje poznawcze",
            "excerpt": "Mózg zużywa 20% energii ciała. To, co ląduje na talerzu, wpływa na koncentrację, pamięć i nastrój.",
            "content": "<p>Omega-3 z ryb, antyoksydanty z jagód, probiotyki z kiszonek – dieta śródziemnomorska redukuje ryzyko depresji o 30%.</p><h2>Kluczowe składniki dla mózgu</h2><ul><li><strong>DHA</strong> – budulec neuronów (łosoś, orzechy)</li><li><strong>Polifenole</strong> – ochrona (jagody, kakao)</li><li><strong>Witaminy B</strong> – neuroprzekaźniki (jaja, strączkowe)</li></ul><p>Unikaj ultra-przetworzonej żywności – cukier i trans-tłuszcze zwiększają stan zapalny.</p>",
            "category": "Dieta",
            "tags": ["dieta", "mózg", "omega-3", "neurożywienie", "koncentracja"],
            "author": "Zdrowie Fit Team",
            "date": "2026-02-01",
            "image": "https://picsum.photos/seed/brain-food/800/450",
            "icon": "🥗"
        }
    ]

def generate_articles_json():
    """Zapisuje artykuły do JSON"""
    articles = generate_sample_articles()
    with open(f"{PROJECT_NAME}/data/articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f"✅ Wygenerowano {len(articles)} artykułów w data/articles.json")

def save_file(path, content):
    """Zapisuje zawartość do pliku"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Utworzono: {path}")

def main():
    print("🚀 Generowanie strony Zdrowie Fit...")
    create_folder_structure()
    save_file(f"{PROJECT_NAME}/index.html", generate_index_html())
    save_file(f"{PROJECT_NAME}/articles.html", generate_articles_html())
    save_file(f"{PROJECT_NAME}/article-template.html", generate_article_template())
    save_file(f"{PROJECT_NAME}/css/style.css", generate_css())
    save_file(f"{PROJECT_NAME}/js/main.js", generate_main_js())
    save_file(f"{PROJECT_NAME}/js/articles.js", generate_articles_js())
    save_file(f"{PROJECT_NAME}/js/article.js", generate_article_js())
    generate_articles_json()
    save_file(f"{PROJECT_NAME}/img/README.txt", "Umieść tutaj plik logo.png (zalecane wymiary: 200x60px)")
    print("\n✨ Gotowe! Strona Zdrowie Fit została wygenerowana.")
    print(f"📁 Otwórz folder: {PROJECT_NAME}/")
    print("🌐 Uruchom: otwórz index.html w przeglądarce")
    print("\n💡 Aby dodać nowy artykuł:")
    print("   1. Dodaj wpis do data/articles.json")
    print("   2. Skopiuj article-template.html do articles/nowy-art.html")
    print("   3. Zaktualizuj zmienne {{TITLE}}, {{CONTENT}} itd.")

if __name__ == "__main__":
    main()
