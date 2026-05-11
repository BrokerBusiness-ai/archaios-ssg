---
title: "Audyt kryptografii — NIS2 art. 21(2)(h) + RODO art. 32 w praktyce"
slug: "audyt-kryptografii-nis2-rodo"
excerpt: "Szyfrowanie w spoczynku i tranzycie, zarządzanie kluczami, algorytmy bezpieczne 2026. Pełna metodyka audytu warstwy kryptograficznej zgodnej z NIS2 i RODO."
category_slug: "audyt-nis2-skanuj"
tags: "kryptografia, szyfrowanie, KMS, TLS, AES, post-quantum, NIS2, RODO, średniozaawansowany"
reading_time: 12
is_published: true
is_featured: false
meta_title: "Audyt kryptografii — NIS2 i RODO praktycznie (2026)"
meta_description: "Metodyka audytu szyfrowania w spoczynku i tranzycie, zarządzania kluczami, polityki kryptograficznej. Algorytmy bezpieczne 2026, post-quantum roadmap."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "audyt-nis2-art-21-krok-po-kroku-metodologia-audytora,audyt-rodo-art-32-bezpieczenstwo-techniczne,audyt-mfa-i-kontroli-dostepu-nis2,audyt-ciaglosci-dzialania-bcp-dr-nis2,audyt-incydentow-24-72h-rodo-nis2"
product_slugs: ""
---

Kryptografia w firmie z 2026 r. nie jest już opcjonalnym dodatkiem — jest fundamentem wszystkich pozostałych zabezpieczeń. Hasło bez kryptografii to nic. MFA bez TLS to teatr. Backup bez szyfrowania to ekspozycja. NIS2 art. 21 ust. 2 lit. h wymaga "polityk i procedur dotyczących stosowania kryptografii oraz, w odpowiednich przypadkach, szyfrowania". RODO art. 32 ust. 1 lit. a wprost wskazuje "szyfrowanie danych osobowych" jako jeden z czterech przykładowych środków technicznych.

Brzmi prosto: szyfrować dane. Realnie audyt kryptografii to jeden z najbardziej technicznych obszarów, w którym łatwo ulec deklaracji ("mamy szyfrowanie") bez weryfikacji rzeczywistości ("który algorytm, jaką długość klucza, kto ma klucze, jak są rotowane, czy nie używamy słabych szyfrów w TLS"). Audytor musi mieć kompetencje techniczne, by ocenić to merytorycznie.

Ten tekst jest pełną metodyką audytu kryptografii w średniej polskiej firmie 2026. Obejmuje pięć obszarów: szyfrowanie w spoczynku, szyfrowanie w tranzycie, zarządzanie kluczami, polityki i procedury, perspektywa post-quantum. Adresat: audytorzy NIS2/RODO z kompetencjami technicznymi, CISO, security architects, dyrektorzy IT.

## Obszar 1: Szyfrowanie w spoczynku (data at rest)

Dane przechowywane na dysku — czy zaszyfrowane?

**Co audytor szuka.**
- Lista baz danych z klasyfikacją (krytyczne / wrażliwe / standardowe)
- Dla każdej: czy szyfrowanie storage, jakim algorytmem, jak zabezpieczone klucze
- Polityka szyfrowania w spoczynku
- Konfiguracja Transparent Data Encryption (TDE) w SQL Server / PostgreSQL / Oracle / MySQL
- Konfiguracja szyfrowania w chmurze (AWS KMS, Azure Key Vault, Google Cloud KMS)

**Standardy 2026.**
- AES-256 jako standard. AES-128 jako minimum dopuszczalne dla danych nieklasyfikowanych jako wrażliwe.
- 3DES, DES, RC4 — niedopuszczalne. Wykrycie = ustalenie krytyczne.
- Szyfrowanie na poziomie storage (cały dysk lub volume) plus szyfrowanie na poziomie aplikacji dla danych szczególnie wrażliwych (PESEL, dane medyczne, dane finansowe).
- Klucze przechowywane oddzielnie od danych (idealnie w HSM lub cloud KMS).

**Typowe luki.**
- Baza produkcyjna zaszyfrowana, ale środowiska dev/test/staging niezaszyfrowane (z kopią danych produkcyjnych).
- Backupy w trzecim regionie chmury bez szyfrowania.
- Klucze hardcoded w plikach konfiguracyjnych.
- "Szyfrowanie" na poziomie pliku (.zip z hasłem) zamiast prawdziwego szyfrowania storage.

**Testy techniczne.**

*Test 1: weryfikacja realnego szyfrowania bazy.* Audytor prosi o dump pliku bazy danych. Jeśli można odczytać dane bezpośrednio z plików storage — brak szyfrowania, mimo deklaracji.

*Test 2: backup encryption.* Audytor prosi o pokazanie procedury przywrócenia backupu i pliki backupu. Czy są zaszyfrowane? Czy klucze są dostępne tylko uprawnionym?

*Test 3: separation of keys and data.* Czy klucze TDE/storage encryption są przechowywane razem z danymi (na tym samym serwerze)? Jeśli tak — brak szyfrowania w praktyce (atakujący z dostępem do serwera ma dane i klucze).

## Obszar 2: Szyfrowanie w tranzycie (data in transit)

**Co audytor szuka.**
- Wersja TLS używana w komunikacji zewnętrznej i wewnętrznej
- Konfiguracja TLS na serwerach webowych, API, bazach danych
- Polityka deprecation starych wersji TLS
- Szyfrowanie wewnętrznej komunikacji (server-to-server)

**Standardy 2026.**
- TLS 1.3 jako standard. TLS 1.2 jako minimum dopuszczalne (z silnymi suite szyfrów).
- TLS 1.0 i 1.1 — niedopuszczalne (od 2020 r. deprecated). Wykrycie = ustalenie krytyczne.
- SSL v2, v3 — niedopuszczalne.
- Cipher suites silne: ECDHE z AES-GCM lub ChaCha20-Poly1305. Słabe: cipher z RC4, MD5, anything export grade.
- HSTS (HTTP Strict Transport Security) jako standard dla portalów.
- Certyfikaty z aktualnych CA, automatyczna rotacja (np. Let's Encrypt z certbot, lub komercyjnych CA z automatic renewal).

**Testy techniczne.**

*Test 1: skan TLS portali zewnętrznych.* Audytor używa narzędzia (testssl.sh, SSL Labs, Qualys) na każdym portalu firmy. Sprawdza: wersje TLS akceptowane, cipher suites, problemy z certyfikatami, HSTS. Wynik poniżej grade B w SSL Labs = ustalenie.

*Test 2: komunikacja wewnętrzna.* Czy server-to-server komunikacja jest szyfrowana? Czy bazy danych dostępne tylko przez TLS? Częsta luka: aplikacja łączy się z bazą po niezaszyfrowanym połączeniu w wewnętrznej sieci ("LAN jest bezpieczna" — to jest myślenie z lat 2000).

*Test 3: API.* Czy wszystkie API endpointy wymagają HTTPS? Czy są jakieś legacy endpointy HTTP, które nadal działają?

*Test 4: VPN.* Czy VPN używa silnych protokołów (WireGuard, OpenVPN z OpenSSL, IPsec z modern crypto)? Czy słabe protokoły (PPTP, L2TP bez IPsec) są wyłączone?

## Obszar 3: Zarządzanie kluczami (Key Management)

Najtrudniejszy obszar audytu kryptografii. Nawet najsilniejsze szyfrowanie jest zerem, jeśli klucze są źle zabezpieczone.

**Co audytor szuka.**
- Polityka zarządzania kluczami (key management policy)
- Lista kluczy używanych w firmie (key inventory)
- Sposób generowania kluczy (cryptographically secure random)
- Sposób przechowywania (HSM, cloud KMS, software-based)
- Sposób rotacji (kiedy, jak często, kto)
- Sposób destrukcji (przy zakończeniu retencji)
- Lista osób uprawnionych do dostępu do kluczy

**Standardy 2026.**
- Hardware Security Modules (HSM) dla najbardziej krytycznych kluczy.
- Cloud KMS (AWS KMS, Azure Key Vault, GCP KMS) jako standard dla firmy chmurowej. BYOK (Bring Your Own Key) dla wzmocnionej kontroli.
- Software KMS (np. HashiCorp Vault) jako alternatywa dla on-premise.
- Rotacja kluczy: minimum raz w roku, częściej dla wrażliwych. Po incydencie — natychmiastowa rotacja.
- Separation of duties: osoba generująca klucz, osoba używająca klucza, osoba audytująca dostęp do klucza — różne osoby.
- Logi dostępu do kluczy retencjonowane minimum 12 miesięcy.

**Testy techniczne.**

*Test 1: gdzie są klucze?* Audytor prosi o pokazanie, gdzie konkretnie są przechowywane klucze do TDE bazy klientów. Jeśli odpowiedź to "w pliku na serwerze bazy" — krytyczne ustalenie.

*Test 2: kto ma dostęp?* Lista użytkowników z dostępem do klucza master (root key). Standard: 2–4 osoby z mechanizmem split-knowledge (m-of-n).

*Test 3: rotacja.* Kiedy ostatnio rotowano klucz do bazy klientów? Jeśli odpowiedź to "nigdy od wdrożenia (4 lata temu)" — ustalenie.

## Obszar 4: Polityka kryptograficzna

Wszystkie powyższe obszary wymagają formalnej polityki — dokumentu, który definiuje, co firma używa, czego nie, jak.

**Co audytor szuka w polityce.**
- Lista akceptowanych algorytmów (AES-256, RSA-2048+, ECDSA P-256+, SHA-256+)
- Lista odrzuconych algorytmów (DES, 3DES, MD5, SHA-1, RC4)
- Procedura wprowadzania nowych algorytmów (kto akceptuje, na podstawie czego)
- Procedura usuwania słabnących algorytmów (np. plan migracji z SHA-256 do SHA-3 lub do post-quantum)
- Standardy długości kluczy
- Standardy generowania (cryptographically secure random — nie Math.random!)
- Standardy retencji i destrukcji kluczy
- Mapa systemów z konkretnymi algorytmami używanymi w każdym

**Częste luki w politykach.**
- Polityka kryptograficzna nie istnieje formalnie (kryptografia jest w polityce bezpieczeństwa ogólnie, bez konkretów).
- Polityka jest, ale nieaktualizowana od momentu napisania (3+ lata).
- Polityka nie obejmuje cloud (firma używa AWS od 2 lat, polityka pochodzi z czasów on-premise).
- Brak mapy "algorytm → system, w którym jest używany".

## Obszar 5: Perspektywa post-quantum (PQC)

NIST w sierpniu 2024 r. opublikował pierwsze finalne standardy post-quantum cryptography (FIPS 203, 204, 205). Komputery kwantowe zdolne do złamania RSA-2048 i ECC są oczekiwane w horyzoncie 2030–2040. Krytyczne dane wymagające ochrony 10+ lat (medyczne, prawne, strategiczne) muszą rozważyć migrację już dziś.

**Co audytor sprawdza w 2026.**
- Czy firma ma świadomość PQC?
- Czy w polityce kryptograficznej jest plan crypto-agility (zdolność do szybkiej zmiany algorytmów)?
- Czy dane krytyczne z długim okresem retencji są przygotowane do migracji?
- Czy dostawcy chmury i kluczowi vendor'zy mają roadmap PQC?

Dla większości średnich polskich firm w 2026 r. PQC nie jest jeszcze wymaganiem operacyjnym, ale brak świadomości i planu = ustalenie informacyjne (nie krytyczne, ale powinno być w raporcie audytu jako rekomendacja strategiczna).

## Format ustaleń

> **Ustalenie KRYPT-02 (klasyfikacja: krytyczne):** TLS 1.0 i TLS 1.1 są nadal akceptowane na portalu klienckim panel.firma.pl. SSL Labs grade: C. Cipher suites zawierają RC4 i 3DES.
>
> **Dowody:** (1) Skan SSL Labs z dnia 2026-05-10 (URL raportu); (2) Skan testssl.sh — pełen log; (3) Konfiguracja nginx w /etc/nginx/sites-available/panel.conf.
>
> **Ryzyko prawne i operacyjne:** Naruszenie NIS2 art. 21(2)(h). TLS 1.0/1.1 są deprecated od 2020 r. (RFC 8996). RC4 podatne na ataki Bar-Mitzvah i znane od 2013 r. Ekspozycja: man-in-the-middle, downgrade attacks. Dane osobowe 23 000 użytkowników portalu narażone.
>
> **Rekomendacja korygująca:** (1) Włączenie wyłącznie TLS 1.2 i TLS 1.3 (wyłączenie TLS 1.0/1.1) w konfiguracji nginx; (2) Pozostawienie wyłącznie cipher suites z ECDHE + AES-GCM lub ChaCha20-Poly1305; (3) Włączenie HSTS z max-age=31536000; (4) Po wdrożeniu — re-test SSL Labs, target grade A lub A+. Termin: 14 dni. Odpowiedzialny: dyrektor IT + administrator nginx.

## Trzy pytania kontrolne przed audytem kryptografii

**Pierwsze.** Czy mam mapę "system → algorytm szyfrowania → lokalizacja kluczy"? Bez tej mapy audyt jest spekulacją.

**Drugie.** Kiedy ostatnio wykonano skan TLS portali zewnętrznych i z jakim wynikiem? Brak skanów regularnych = brak monitoringu skuteczności środków (art. 32 ust. 1 lit. d RODO).

**Trzecie.** Gdzie są klucze do szyfrowania bazy klientów? Konkretna odpowiedź (np. "AWS KMS region eu-central-1, customer-managed CMK z BYOK") = poziom 3+. "Gdzieś na serwerze" = poziom 1.

## Esencja

Audyt kryptografii obejmuje pięć obszarów: szyfrowanie w spoczynku, szyfrowanie w tranzycie, zarządzanie kluczami, polityka kryptograficzna, perspektywa post-quantum. Każdy wymaga osobnej metodyki dowodów i testów technicznych.

Standardy 2026 są jasne: AES-256 dla danych, TLS 1.2/1.3 dla komunikacji, hardware lub cloud KMS dla kluczy, formalna polityka z mapą algorytmów per system. Wszystko poniżej tych standardów to ustalenia.

Najczęstsze luki w polskich średnich firmach: TLS 1.0/1.1 nadal aktywne na portalach starszych, klucze przechowywane razem z danymi (jakby ich nie było), brak rotacji kluczy, środowiska dev/test/staging niezaszyfrowane z kopią produkcji.

Zarządzanie kluczami jest najtrudniejszym obszarem. Najsilniejsze szyfrowanie z słabym key management to dziurawe sito. HSM lub cloud KMS z separation of duties to standard 2026 dla podmiotu kluczowego.

Skan SSL Labs portali zewnętrznych jest najszybszym testem audytowym. 5 minut na portal, grade B lub niżej = automatyczne ustalenie. Każdy CISO w 2026 r. powinien mieć monitoring tego w czasie rzeczywistym.

PQC nie jest jeszcze operacyjnym wymaganiem dla większości firm, ale crypto-agility (zdolność do szybkiej zmiany algorytmów) staje się strategicznym tematem. Dane z retencją 10+ lat zaszyfrowane dziś RSA-2048 są kandydatem do "harvest now, decrypt later" przez aktorów państwowych.

---

<ul>
<li>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 (NIS2), art. 21 ust. 2 lit. (h). https://eur-lex.europa.eu/eli/dir/2022/2555/oj</li>
<li>Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 (RODO), art. 32 ust. 1 lit. (a). https://eur-lex.europa.eu/eli/reg/2016/679/oj</li>
<li>NIST FIPS 197 (2001). <em>Advanced Encryption Standard (AES)</em>. https://doi.org/10.6028/NIST.FIPS.197</li>
<li>NIST SP 800-57 Part 1 Rev. 5 (2020). <em>Recommendation for Key Management — Part 1: General</em>. https://doi.org/10.6028/NIST.SP.800-57pt1r5</li>
<li>NIST FIPS 203 (2024). <em>Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)</em>. Post-quantum standard. https://doi.org/10.6028/NIST.FIPS.203</li>
<li>NIST FIPS 204 (2024). <em>Module-Lattice-Based Digital Signature Algorithm (ML-DSA)</em>. https://doi.org/10.6028/NIST.FIPS.204</li>
<li>IETF RFC 8446 (2018). <em>The Transport Layer Security (TLS) Protocol Version 1.3</em>. https://datatracker.ietf.org/doc/html/rfc8446</li>
<li>IETF RFC 8996 (2021). <em>Deprecating TLS 1.0 and TLS 1.1</em>. https://datatracker.ietf.org/doc/html/rfc8996</li>
<li>Mozilla. <em>TLS Configuration Generator and Recommendations</em>. https://ssl-config.mozilla.org/</li>
<li>ENISA (2023). <em>Cryptographic protocols and algorithms — recommendations</em>. https://www.enisa.europa.eu/publications</li>
<li>Qualys SSL Labs. <em>SSL Server Test</em>. https://www.ssllabs.com/ssltest/</li>
</ul>
