# 🚀 Kickoff prompt — nowa satelita Archaios SSG

## Jak używać

1. **Skopiuj** poniższy blok (sekcja „PROMPT DO WKLEJENIA")
2. **Wypełnij** placeholdery `{{...}}` w sekcji INPUTS
3. **Wklej** do nowego czatu Claude (Chat / Code / Cowork)
4. AI odczyta `docs/SATELLITE_DEPLOYMENT_PROMPT.md` z repo i poprowadzi Cię fazami

---

## PROMPT DO WKLEJENIA

```
Tworzymy nową satelitę z rodziny Archaios SSG.

PEŁNA PROCEDURA + GOTCHY: docs/SATELLITE_DEPLOYMENT_PROMPT.md
TEMPLATE INPUTS: docs/SATELLITE_INPUTS_TEMPLATE.yaml
WZÓR DZIAŁAJĄCY: domains/zdrowie-fit.yaml

INPUTS dla tej satelity:

DOMAIN_FQDN: {{np. testnis2.pl}}
DOMAIN_SLUG: {{np. testnis2-pl}}
BRAND_NAME: {{np. Test NIS2}}
TAGLINE: {{np. Compliance NIS2 oparty na faktach}}
DESCRIPTION: {{1 zdanie 120-160 znaków, do meta description}}

LOGO_TEXT: {{np. Test}}
LOGO_ACCENT: {{terakotowa końcówka, np. NIS2}}

ROLE: {{satellite albo flagship}}
FUNNEL_TYPE: {{article_cta | lead_magnet | direct_sale | brand_awareness}}
MAIN_DOMAIN: {{flagowiec, np. archaios.ai}}

COLOR_PRIMARY: {{#hex}}
COLOR_ACCENT: {{#hex, terakotowy odcień}}
COLOR_TRUST: {{#hex, niebieski do "badania/źródła"}}

CONTACT_EMAIL: kontakt@{{DOMAIN_FQDN}}

KATEGORIE (2-5):
1. {{nazwa, slug, icon emoji, color}}
2. ...

PILLARS (4-6 klikalnych kafelków):
1. {{icon, title, desc 1 zdanie, link do /kategoria/{slug}.html}}
2. ...

PRODUCTS (1-3 affiliate/own dla CTAs w artykułach):
1. {{name, target_url z UTM, target_category_slugs, target_tags}}

DEPLOY_BACKEND: false  # true tylko gdy realna potrzeba API/webhooków

INSTRUKCJE DLA CIEBIE:

1. Przeczytaj docs/SATELLITE_DEPLOYMENT_PROMPT.md — to twój master plan
2. Prowadź mnie FAZAMI 0-7 (8 i 9 opcjonalne) — jedna faza = jedna wiadomość
3. Po każdej fazie pytaj o output (screenshot/PowerShell wynik) zanim ruszysz dalej
4. Gotchy z sekcji „COMMON GOTCHAS" znaj na pamięć — nie pozwól mi w nie wpaść
5. Gdy faza zakończona poprawnie, napisz „✅ Faza X done" i przejdź do następnej
6. Cel: ~2h całość (1.5h pracy + 30 min czekania na DNS)
7. Definition of Done: lista checkbox na końcu master prompta

Startujemy od FAZY 1 (DNS + domena Cyber_Folks). Daj mi step-by-step co klikam.
```

---

## Po wklejeniu — co Claude robi

1. **Czyta plik `docs/SATELLITE_DEPLOYMENT_PROMPT.md`** (ma pełną procedurę z bólu zdrowie.fit)
2. **Czyta `domains/zdrowie-fit.yaml`** jako wzór dla nowego YAML-a
3. **Czyta `docs/SATELLITE_INPUTS_TEMPLATE.yaml`** dla struktury inputów
4. **Prowadzi Cię fazami**, sprawdza outputy, zna gotchy

## Wskazówka — dla Claude Code w nowym worktree

```bash
cd "C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator"
git checkout -b satellite/{{DOMAIN_SLUG}}
# wklej prompt do Claude Code, uzupełnij INPUTS
# Claude działa w izolowanym branchu, nie ruszając zdrowie.fit
```

## Po sukcesie — checklist do commit

```bash
git add domains/{{DOMAIN_SLUG}}.yaml
git commit -m "Add satellite {{DOMAIN_FQDN}}"
git push origin satellite/{{DOMAIN_SLUG}}
# Merge do main przez PR (jeśli jesteś sam — git checkout main && git merge)
```

GitHub Actions z `.github/workflows/deploy.yml` automatycznie zdeployuje strona po push do `main`.
