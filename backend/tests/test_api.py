"""API integration tests."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base, get_db
from app.main import app

engine = create_engine("sqlite:///./test_zf.db", connect_args={"check_same_thread": False})
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_db
client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def _login() -> dict:
    # Seed admin via startup event won't fire in tests, create manually
    from app.core.auth import hash_password
    db = TestSession()
    from app.models.admin_user import AdminUser
    db.add(AdminUser(username="admin", password_hash=hash_password("admin123")))
    db.commit()
    db.close()
    r = client.post("/api/auth/login", json={"username": "admin", "password": "admin123"})
    assert r.status_code == 200
    token = r.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


# ── Auth ──

class TestAuth:
    def test_login_success(self):
        headers = _login()
        r = client.get("/api/auth/me", headers=headers)
        assert r.status_code == 200
        assert r.json()["username"] == "admin"

    def test_login_fail(self):
        r = client.post("/api/auth/login", json={"username": "x", "password": "y"})
        assert r.status_code == 401

    def test_protected_without_token(self):
        r = client.post("/api/articles/", json={"title": "x"})
        assert r.status_code == 401


# ── Categories ──

class TestCategories:
    def test_crud(self):
        h = _login()
        # create
        r = client.post("/api/categories/", json={"name": "Fitness", "icon": "💪"}, headers=h)
        assert r.status_code == 201
        cid = r.json()["id"]
        assert r.json()["slug"] == "fitness"

        # list
        r = client.get("/api/categories/")
        assert len(r.json()) == 1

        # update
        r = client.put(f"/api/categories/{cid}", json={"name": "Sport"}, headers=h)
        assert r.json()["name"] == "Sport"
        assert r.json()["slug"] == "sport"

        # delete
        r = client.delete(f"/api/categories/{cid}", headers=h)
        assert r.status_code == 204

    def test_public_list(self):
        r = client.get("/api/categories/")
        assert r.status_code == 200


# ── Articles ──

class TestArticles:
    def _create_with_category(self, h):
        client.post("/api/categories/", json={"name": "Zdrowie"}, headers=h)
        cats = client.get("/api/categories/").json()
        cid = cats[0]["id"]
        r = client.post("/api/articles/", json={
            "title": "Testowy artykuł",
            "excerpt": "Opis",
            "content": "<p>Treść</p>",
            "category_id": cid,
            "tags": "test,zdrowie",
            "is_published": True,
        }, headers=h)
        assert r.status_code == 201
        return r.json()

    def test_create_and_get(self):
        h = _login()
        art = self._create_with_category(h)
        assert art["slug"] == "testowy-artykul"

        # get by id
        r = client.get(f"/api/articles/{art['id']}")
        assert r.json()["title"] == "Testowy artykuł"

        # get by slug
        r = client.get(f"/api/articles/slug/{art['slug']}")
        assert r.json()["id"] == art["id"]

    def test_list_and_search(self):
        h = _login()
        self._create_with_category(h)
        client.post("/api/articles/", json={"title": "Drugi artykuł", "is_published": True}, headers=h)

        # list published
        r = client.get("/api/articles/?published_only=true")
        assert r.json()["total"] == 2

        # search
        r = client.get("/api/articles/?search=Testowy")
        assert r.json()["total"] == 1

        # filter by category
        cats = client.get("/api/categories/").json()
        r = client.get(f"/api/articles/?category={cats[0]['slug']}")
        assert r.json()["total"] == 1

    def test_update(self):
        h = _login()
        art = self._create_with_category(h)
        r = client.put(f"/api/articles/{art['id']}", json={"title": "Zmieniony tytuł"}, headers=h)
        assert r.json()["title"] == "Zmieniony tytuł"
        assert r.json()["slug"] == "zmieniony-tytul"

    def test_delete(self):
        h = _login()
        art = self._create_with_category(h)
        r = client.delete(f"/api/articles/{art['id']}", headers=h)
        assert r.status_code == 204

    def test_toggle_publish(self):
        h = _login()
        art = self._create_with_category(h)
        r = client.post(f"/api/articles/{art['id']}/toggle-publish", headers=h)
        assert r.json()["is_published"] == False
        r = client.post(f"/api/articles/{art['id']}/toggle-publish", headers=h)
        assert r.json()["is_published"] == True

    def test_toggle_featured(self):
        h = _login()
        art = self._create_with_category(h)
        r = client.post(f"/api/articles/{art['id']}/toggle-featured", headers=h)
        assert r.json()["is_featured"] == True

    def test_pagination(self):
        h = _login()
        for i in range(5):
            client.post("/api/articles/", json={"title": f"Art {i}", "is_published": True}, headers=h)
        r = client.get("/api/articles/?per_page=2&page=1")
        data = r.json()
        assert data["per_page"] == 2
        assert data["pages"] == 3
        assert len(data["items"]) == 2

    def test_view_counter(self):
        h = _login()
        art = self._create_with_category(h)
        client.get(f"/api/articles/slug/{art['slug']}")
        client.get(f"/api/articles/slug/{art['slug']}")
        r = client.get(f"/api/articles/{art['id']}")
        assert r.json()["views"] == 2


# ── Admin panel ──

class TestAdminPanel:
    def test_login_page(self):
        r = client.get("/admin/login")
        assert r.status_code == 200
        assert "Zaloguj" in r.text

    def test_dashboard_requires_login(self):
        r = client.get("/admin/", follow_redirects=False)
        assert r.status_code == 302

    def test_health(self):
        r = client.get("/api/health")
        assert r.json()["status"] == "ok"
