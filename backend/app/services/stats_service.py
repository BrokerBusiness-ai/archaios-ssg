"""StatsService — agregaty wyświetleń artykułów dla dashboard admin panelu.

Wszystkie zapytania wykorzystują indexy na ArticleView (article_slug, viewed_at, session_id).
Czas: UTC. Daty granicznych okresów: liczone od start-of-day w strefie Europe/Warsaw,
żeby dashboard pokazywał "dzisiaj" zgodnie z lokalną intuicją.
"""

from datetime import datetime, timedelta, timezone
from sqlalchemy import func, distinct
from sqlalchemy.orm import Session

from app.models.article import Article
from app.models.article_view import ArticleView


# Europe/Warsaw offset (uproszczone — DST ignorowany; akceptowalna granica błędu 1h)
def _now_warsaw():
    """Aktualny czas w UTC, ale z 'dniem' liczonym względem Warszawy."""
    return datetime.now(timezone.utc)


def _start_of_day_warsaw(dt: datetime) -> datetime:
    """Początek dnia (00:00) w strefie Warszawy, zwrócony jako UTC."""
    # Warsaw = UTC+1 (CET) lub UTC+2 (CEST). Approximate: UTC+1 caly rok dla statystyk.
    warsaw_offset = timedelta(hours=1)
    local = dt + warsaw_offset
    midnight_local = local.replace(hour=0, minute=0, second=0, microsecond=0)
    return midnight_local - warsaw_offset


# ── Top-level aggregates ──────────────────────────────────────────

def get_overview(db: Session) -> dict:
    """Zwraca komplet statystyk dla dashboard: live, today, week, month, year, all-time."""
    now = _now_warsaw()
    today_start = _start_of_day_warsaw(now)
    week_start = today_start - timedelta(days=now.weekday())  # poniedziałek
    month_start = today_start.replace(day=1)
    year_start = today_start.replace(month=1, day=1)
    five_min_ago = now - timedelta(minutes=5)

    def _count_pageviews(since: datetime) -> int:
        return db.query(func.count(ArticleView.id)).filter(ArticleView.viewed_at >= since).scalar() or 0

    def _count_unique_sessions(since: datetime) -> int:
        return db.query(func.count(distinct(ArticleView.session_id))).filter(
            ArticleView.viewed_at >= since,
            ArticleView.session_id.isnot(None),
        ).scalar() or 0

    return {
        # LIVE: ile unikalnych sesji w ostatnich 5 min
        "live_readers": _count_unique_sessions(five_min_ago),

        # Pageviews — surowe odsłony
        "today_views": _count_pageviews(today_start),
        "week_views": _count_pageviews(week_start),
        "month_views": _count_pageviews(month_start),
        "year_views": _count_pageviews(year_start),
        "all_time_views": db.query(func.count(ArticleView.id)).scalar() or 0,

        # Unique sessions (lepszy proxy dla "ile osób")
        "today_unique": _count_unique_sessions(today_start),
        "week_unique": _count_unique_sessions(week_start),
        "month_unique": _count_unique_sessions(month_start),
        "year_unique": _count_unique_sessions(year_start),
    }


# ── Wykres dzienny ────────────────────────────────────────────────

def get_daily_chart(db: Session, days: int = 30) -> list[dict]:
    """Zwraca listę {date, views, unique} dla ostatnich N dni (do wykresu)."""
    now = _now_warsaw()
    today_start = _start_of_day_warsaw(now)
    start = today_start - timedelta(days=days - 1)

    # SQLite nie ma natywnego DATE_TRUNC, używamy strftime
    rows = db.query(
        func.strftime("%Y-%m-%d", ArticleView.viewed_at).label("day"),
        func.count(ArticleView.id).label("views"),
        func.count(distinct(ArticleView.session_id)).label("unique_sessions"),
    ).filter(
        ArticleView.viewed_at >= start
    ).group_by("day").order_by("day").all()

    # Wypełnij brakujące dni zerami (frontend dostaje pełną serię)
    by_day = {row.day: row for row in rows}
    out = []
    for i in range(days):
        d = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        row = by_day.get(d)
        out.append({
            "date": d,
            "views": int(row.views) if row else 0,
            "unique": int(row.unique_sessions) if row else 0,
        })
    return out


# ── Top artykuły ──────────────────────────────────────────────────

def get_top_articles(db: Session, period: str = "month", limit: int = 10) -> list[dict]:
    """Top artykuły wg odsłon. period: today / week / month / year / all."""
    now = _now_warsaw()
    today_start = _start_of_day_warsaw(now)
    period_starts = {
        "today": today_start,
        "week": today_start - timedelta(days=now.weekday()),
        "month": today_start.replace(day=1),
        "year": today_start.replace(month=1, day=1),
        "all": datetime(2000, 1, 1, tzinfo=timezone.utc),
    }
    since = period_starts.get(period, today_start.replace(day=1))

    rows = db.query(
        ArticleView.article_slug,
        func.count(ArticleView.id).label("views"),
        func.count(distinct(ArticleView.session_id)).label("unique_sessions"),
    ).filter(
        ArticleView.viewed_at >= since
    ).group_by(ArticleView.article_slug).order_by(func.count(ArticleView.id).desc()).limit(limit).all()

    # Dociągnij tytuły z bazy artykułów
    slugs = [r.article_slug for r in rows]
    articles_by_slug = {a.slug: a for a in db.query(Article).filter(Article.slug.in_(slugs)).all()} if slugs else {}

    return [{
        "slug": r.article_slug,
        "title": articles_by_slug[r.article_slug].title if r.article_slug in articles_by_slug else r.article_slug,
        "views": int(r.views),
        "unique": int(r.unique_sessions),
    } for r in rows]


# ── Live readers — kto teraz czyta ────────────────────────────────

def get_live_readers(db: Session) -> list[dict]:
    """Lista artykułów z aktywnymi czytelnikami (ostatnie 5 min)."""
    now = _now_warsaw()
    five_min_ago = now - timedelta(minutes=5)

    rows = db.query(
        ArticleView.article_slug,
        func.count(distinct(ArticleView.session_id)).label("active_readers"),
    ).filter(
        ArticleView.viewed_at >= five_min_ago,
        ArticleView.session_id.isnot(None),
    ).group_by(ArticleView.article_slug).order_by(func.count(distinct(ArticleView.session_id)).desc()).all()

    slugs = [r.article_slug for r in rows]
    articles_by_slug = {a.slug: a for a in db.query(Article).filter(Article.slug.in_(slugs)).all()} if slugs else {}

    return [{
        "slug": r.article_slug,
        "title": articles_by_slug[r.article_slug].title if r.article_slug in articles_by_slug else r.article_slug,
        "active_readers": int(r.active_readers),
    } for r in rows]


# ── Per-artykuł szczegóły ─────────────────────────────────────────

def get_article_stats(db: Session, slug: str) -> dict:
    """Pełna statystyka pojedynczego artykułu."""
    now = _now_warsaw()
    today_start = _start_of_day_warsaw(now)
    week_start = today_start - timedelta(days=now.weekday())
    month_start = today_start.replace(day=1)
    year_start = today_start.replace(month=1, day=1)
    five_min_ago = now - timedelta(minutes=5)

    base = db.query(ArticleView).filter(ArticleView.article_slug == slug)

    return {
        "slug": slug,
        "live": db.query(func.count(distinct(ArticleView.session_id))).filter(
            ArticleView.article_slug == slug,
            ArticleView.viewed_at >= five_min_ago,
            ArticleView.session_id.isnot(None),
        ).scalar() or 0,
        "today": base.filter(ArticleView.viewed_at >= today_start).count(),
        "week": base.filter(ArticleView.viewed_at >= week_start).count(),
        "month": base.filter(ArticleView.viewed_at >= month_start).count(),
        "year": base.filter(ArticleView.viewed_at >= year_start).count(),
        "all_time": base.count(),
    }


# ── Sources / referrers ───────────────────────────────────────────

def get_referrers(db: Session, days: int = 30) -> list[dict]:
    """Top źródeł ruchu (Google, Facebook, direct itp.)."""
    now = _now_warsaw()
    since = now - timedelta(days=days)

    rows = db.query(
        ArticleView.referrer_host,
        func.count(ArticleView.id).label("views"),
    ).filter(
        ArticleView.viewed_at >= since
    ).group_by(ArticleView.referrer_host).order_by(func.count(ArticleView.id).desc()).limit(15).all()

    return [{
        "source": r.referrer_host or "direct",
        "views": int(r.views),
    } for r in rows]


# ── Devices ───────────────────────────────────────────────────────

def get_device_split(db: Session, days: int = 30) -> dict:
    """Podział mobile/tablet/desktop/bot."""
    now = _now_warsaw()
    since = now - timedelta(days=days)

    rows = db.query(
        ArticleView.device_type,
        func.count(ArticleView.id).label("views"),
    ).filter(
        ArticleView.viewed_at >= since
    ).group_by(ArticleView.device_type).all()

    total = sum(int(r.views) for r in rows) or 1
    return {
        (r.device_type or "unknown"): {
            "views": int(r.views),
            "percent": round(100 * int(r.views) / total, 1),
        }
        for r in rows
    }


# ── Public API: zapis odsłony ─────────────────────────────────────

def record_view(
    db: Session,
    *,
    article_slug: str,
    session_id: str | None = None,
    ip_hash: str | None = None,
    user_agent: str | None = None,
    referer: str | None = None,
) -> ArticleView:
    """Zapisz odsłonę. Wywoływane z public endpointu (JS ping)."""
    # Znajdź article_id (jeśli istnieje w bazie)
    article = db.query(Article).filter(Article.slug == article_slug).first()
    article_id = article.id if article else None

    # Detect device type z user-agent (proste heurystyki)
    device_type = _detect_device(user_agent or "")

    # Wyciągnij host z referera
    referrer_host = _extract_host(referer or "")

    view = ArticleView(
        article_id=article_id,
        article_slug=article_slug,
        session_id=session_id,
        ip_hash=ip_hash,
        device_type=device_type,
        referrer_host=referrer_host,
    )
    db.add(view)

    # Denormalizacja — zwiększ Article.views (fast read)
    if article:
        article.views = (article.views or 0) + 1

    db.commit()
    db.refresh(view)
    return view


def _detect_device(ua: str) -> str:
    ua_l = ua.lower()
    if any(b in ua_l for b in ("bot", "spider", "crawler", "headless", "lighthouse", "googlebot", "bingbot")):
        return "bot"
    if "tablet" in ua_l or "ipad" in ua_l:
        return "tablet"
    if any(m in ua_l for m in ("mobile", "android", "iphone", "ipod")):
        return "mobile"
    return "desktop"


def _extract_host(referer: str) -> str:
    if not referer:
        return "direct"
    try:
        from urllib.parse import urlparse
        host = urlparse(referer).hostname or "direct"
        # Skróć subdomeny (www. itp.) ale zostaw główne
        if host.startswith("www."):
            host = host[4:]
        # Generaliz: google.com / google.pl → "google" search
        for engine in ("google.", "bing.", "duckduckgo.", "yandex.", "yahoo."):
            if engine in host:
                return host.split(".")[0] + " search"
        return host
    except Exception:
        return "direct"
