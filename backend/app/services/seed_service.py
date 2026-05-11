"""Seed database with default admin, categories, authors, products, and sample articles."""

from datetime import datetime
from slugify import slugify
from sqlalchemy.orm import Session

from app.core.auth import hash_password
from app.core.config import settings
from app.models.admin_user import AdminUser
from app.models.article import Article
from app.models.category import Category
from app.models.author import Author
from app.models.product import Product


def seed_all(db: Session) -> None:
    _seed_admin(db)
    cats = _seed_categories(db)
    authors = _seed_authors(db)
    _seed_products(db)
    _seed_articles(db, cats, authors)


def _seed_authors(db: Session) -> dict[str, Author]:
    if db.query(Author).count() > 0:
        return {a.slug: a for a in db.query(Author).all()}
    defs = [
        {
            "name": "Redakcja Zdrowie.fit",
            "bio_short": "Zespół redakcyjny tworzący treści oparte na badaniach naukowych.",
            "bio_long": "<p>Treści tworzone przez zespół redakcyjny przy współpracy z ekspertami dziedzinowymi. Każdy artykuł jest weryfikowany pod kątem zgodności z aktualnym stanem wiedzy medycznej.</p>",
            "credentials": "Redakcja",
            "specializations": "zdrowie,psychosomatyka,wellbeing",
            "sort_order": 99,
        }
    ]
    result: dict[str, Author] = {}
    for d in defs:
        slug = slugify(d["name"], max_length=200)
        author = Author(slug=slug, **d)
        db.add(author)
        db.flush()
        result[slug] = author
    db.commit()
    return result


def _seed_products(db: Session):
    if db.query(Product).count() > 0:
        return
    # Przykładowy produkt — podmienisz w adminie. Opisany żeby było widać jak działa lejek.
    example = Product(
        slug="nurio-przyklad",
        name="Nurio (przykładowy produkt)",
        brand="Nurio",
        tagline_short="Rozmawiaj z AI o swoim zdrowiu psychicznym",
        tagline_long="Wsparcie 24/7 bez oceniania. Odpowiedzi oparte na terapii poznawczo-behawioralnej.",
        description="<p>To jest przykładowy produkt. Edytuj go w panelu admina: <strong>/admin/products</strong>.</p>",
        cta_text="Wypróbuj bezpłatnie",
        target_url="https://nurio.example.com",
        target_category_slugs="psychiczne,zdrowie",
        target_tags="stres,lęk,sen,mindfulness,terapia",
        placement="end",
        is_active=False,  # WYŁĄCZONE domyślnie — user włącza i konfiguruje w adminie
        priority=80,
        kind="own",
    )
    db.add(example)
    db.commit()


def _seed_admin(db: Session):
    if db.query(AdminUser).first():
        return
    admin = AdminUser(
        username=settings.ADMIN_USERNAME,
        password_hash=hash_password(settings.ADMIN_PASSWORD),
    )
    db.add(admin)
    db.commit()


def _seed_categories(db: Session) -> dict[str, Category]:
    if db.query(Category).count() > 0:
        return {c.slug: c for c in db.query(Category).all()}

    # Slugi muszą być spójne z domains/zdrowie-fit.yaml (categories) — inaczej
    # build.py nie połączy artykułów z kategoriami i kategorie pozostaną puste.
    defs = [
        ("Zdrowie fizyczne", "fizyczne", "Trening, ruch, aktywność fizyczna, neurobiologia ciała", "🏃", "#4a7c59", 1),
        ("Zdrowie psychiczne", "psychiczne", "Mindfulness, stres, regulacja emocji, neuropsychologia", "🧠", "#5b8def", 2),
        ("Dieta i odżywianie", "dieta", "Mikrobiom, dieta śródziemnomorska, MIND, suplementacja", "🥗", "#d9724a", 3),
    ]
    cats = {}
    for name, slug, desc, icon, color, order in defs:
        cat = Category(name=name, slug=slug, description=desc, icon=icon, color=color, sort_order=order)
        db.add(cat)
        db.flush()
        cats[slug] = cat
    db.commit()
    return cats


def _seed_articles(db: Session, cats: dict[str, Category], authors: dict[str, Author] | None = None):
    default_author = next(iter((authors or {}).values()), None)
    if db.query(Article).count() > 0:
        return

    articles_data = [
        {
            "title": "Jak ruch wpływa na nastrój? Naukowe fakty",
            "excerpt": "Regularna aktywność fizyczna to nie tylko sylwetka – to potężne narzędzie do zarządzania stresem i poprawy zdrowia psychicznego.",
            "content": "<p>Badania jednoznacznie pokazują: już 30 minut umiarkowanego wysiłku dziennie znacząco podnosi poziom endorfin i serotoniny.</p><h2>Dlaczego to działa?</h2><ul><li><strong>Endorfiny</strong> – naturalne leki przeciwbólowe</li><li><strong>BDNF</strong> – białko wspierające neuroplastyczność</li><li><strong>Redukcja kortyzolu</strong> – niższy hormon stresu</li></ul><p>Nie musisz biegać maratonów. Spacer, joga, taniec – każda forma ruchu się liczy.</p><h2>Praktyczne wskazówki</h2><p>Zacznij od 10 minut dziennie. Wybierz aktywność, która sprawia Ci przyjemność. Połącz ruch z naturą.</p>",
            "category_slug": "fitness", "icon": "🏃", "tags": "ruch,endorfiny,stres,neuronauka",
            "reading_time": 6, "image_url": "https://picsum.photos/seed/mood-move/800/450",
        },
        {
            "title": "Sen: kiedy Twój mózg pracuje najciężej",
            "excerpt": "Podczas snu mózg nie odpoczywa – usuwa toksyny, konsoliduje pamięć i przygotowuje się na kolejny dzień.",
            "content": "<p>W trakcie głębokiego snu aktywowany jest system glymphatic – naturalny \"odkurzacz\" mózgu.</p><h2>Fazy snu a zdrowie</h2><ul><li><strong>NREM</strong> – regeneracja fizyczna</li><li><strong>REM</strong> – przetwarzanie emocji, kreatywność</li></ul><p>Brak snu &lt;7h zwiększa ryzyko lęku o 30%.</p><h2>Jak spać lepiej?</h2><p>Stała pora snu, ciemna sypialnia, brak ekranów 1h przed snem, temperatura 18-20°C.</p>",
            "category_slug": "zdrowie", "icon": "😴", "tags": "sen,regeneracja,mózg,pamięć",
            "reading_time": 8, "image_url": "https://picsum.photos/seed/sleep-brain/800/450",
        },
        {
            "title": "Co jesz, tym myślisz: dieta a funkcje poznawcze",
            "excerpt": "Mózg zużywa 20% energii ciała. To, co ląduje na talerzu, wpływa na koncentrację, pamięć i nastrój.",
            "content": "<p>Omega-3, antyoksydanty z jagód, probiotyki – dieta śródziemnomorska redukuje ryzyko depresji o 30%.</p><h2>Kluczowe składniki</h2><ul><li><strong>DHA</strong> – budulec neuronów (łosoś, orzechy)</li><li><strong>Polifenole</strong> – ochrona (jagody, kakao)</li><li><strong>Witaminy B</strong> – neuroprzekaźniki (jaja, strączkowe)</li></ul><p>Unikaj ultra-przetworzonej żywności.</p>",
            "category_slug": "odzywianie", "icon": "🥗", "tags": "dieta,mózg,omega-3,koncentracja",
            "reading_time": 10, "image_url": "https://picsum.photos/seed/brain-food/800/450",
        },
        {
            "title": "Mindfulness: 5 minut, które zmienią Twój dzień",
            "excerpt": "Praktyka uważności obniża kortyzol, poprawia koncentrację i wspiera układ odpornościowy – wystarczy 5 minut dziennie.",
            "content": "<p>Mindfulness to świadome kierowanie uwagi na chwilę obecną bez oceniania.</p><h2>Jak zacząć</h2><p>Usiądź wygodnie, zamknij oczy, skup się na oddechu. Gdy myśli odpłyną, łagodnie wróć do oddechu. 5 minut dziennie to dobry start.</p><h2>Efekty potwierdzone naukowo</h2><ul><li>Obniżenie kortyzolu o 15-25%</li><li>Obniżenie ciśnienia skurczowego o ~5 mmHg</li><li>Poprawa jakości snu</li></ul>",
            "category_slug": "psychiczne", "icon": "🧘", "tags": "mindfulness,medytacja,stres,uważność",
            "reading_time": 5, "image_url": "https://picsum.photos/seed/mindfulness/800/450",
        },
        {
            "title": "Shinrin-yoku: jak las leczy ciało i umysł",
            "excerpt": "Japońska kąpiel leśna ma solidne podstawy naukowe – 2 godziny w lesie zwiększają aktywność komórek NK o 50%.",
            "content": "<p>Shinrin-yoku (森林浴) to japońska praktyka powolnego, świadomego przebywania w lesie.</p><h2>Naukowe dowody</h2><p>Badania prof. Qing Li wykazały: 2h w lesie zwiększa komórki NK o 50%, obniża kortyzol o 12.4%.</p><h2>Jak praktykować</h2><ul><li>Wyłącz telefon</li><li>Idź wolno – 1-2 km w 2 godziny</li><li>Dotknij kory, poczuj zapach igliwia</li><li>Usiądź na 15 min z zamkniętymi oczami</li></ul>",
            "category_slug": "wellbeing", "icon": "🌿", "tags": "las,natura,shinrin-yoku,odporność",
            "reading_time": 7, "image_url": "https://picsum.photos/seed/forest/800/450",
        },
    ]

    now = datetime.utcnow()
    for i, data in enumerate(articles_data):
        cat = cats.get(data.pop("category_slug"))
        article = Article(
            slug=slugify(data["title"], max_length=300),
            category_id=cat.id if cat else None,
            author_id=default_author.id if default_author else None,
            is_published=True,
            is_featured=(i < 3),
            published_at=now,
            author=default_author.name if default_author else "Zdrowie Fit Team",
            **data,
        )
        db.add(article)
    db.commit()
