# Changelog

All notable changes to Archaios SSG are documented here.
Format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning is [SemVer](https://semver.org/).

## [1.0.0] - 2026-04-25

First tagged release. Project renamed from `zdrowie-fit-generator` to `archaios-ssg`
to reflect its real scope: a multi-domain static-site engine powering the Archaios
satellite network (zdrowie.fit, psycho-edu.pl, testnis2.pl, and ~17 other domains).

### Added
- Multi-domain build (`python build.py --all` / `--domain <domain>`) with per-domain
  YAML config in `domains/*.yaml`.
- Image pipeline: WebP + thumbnail conversion in `optimize_image()`; auto OG images
  (1200×630 PNG + WebP) in `generate_og_image()` with `article["og_webp"]` flag.
- Performance: critical CSS inlined in `<head>`, CSS/JS/HTML minification in
  `copy_static()` / `render()`, self-hosted Inter + Fraunces woff2 (zero external
  font requests), `loading="lazy"` + explicit `width`/`height` on card images.
- SEO: sitemap image extensions (`image:title` / `image:caption`), category +
  author URL blocks, FAQPage schema auto-generated from article content, speakable
  spec, breadcrumb schema.
- Security: `.htaccess` generator with CSP, HSTS, X-Frame-Options, Referrer-Policy,
  Permissions-Policy, compression (mod_deflate), cache (mod_expires), HTTPS
  redirect, sensitive-file blocklist.
- 404 page + service worker.
- CI/CD: GitHub Actions workflow with matrix deploy — one job per domain, SFTP to
  `/home/bestios/domains/<domain>/public_html`, `workflow_dispatch` with domain
  input.

### Changed
- Font library bumped: Fraunces v31 → v38 (v31 URLs at `fonts.gstatic.com` started
  returning 404; `scripts/download_fonts.py` now uses v38, `src/static/css/fonts.css`
  references updated).
- `backend/app/core/config.py`: `APP_NAME` is now `Archaios SSG API`.

### Known follow-ups
- Filesystem directory rename (`zdrowie-fit-generator/` → `archaios-ssg/`) is
  deferred — touches local paths, IDE configs, and the Cyber_Folks deploy target
  structure. Track separately.
- `scripts/download_fonts.py` still uses hardcoded gstatic URLs; next bump will
  need another manual update. Consider refactoring to fetch from
  `gwfh.mranftl.com` API.
