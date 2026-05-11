# sprawdzwypalenie.pl — pakiet design

Domena: wypalenie zawodowe (klaster NURIO, MOFU/BOFU). Charakter: konkretny, kliniczny, dla osób *aktywnie* podejrzewających u siebie wypalenie. Maslach jako fundament. Bezpośredni CTA do testu wypalenia w psychozdrowie.online.

## Tożsamość marki

**Nazwa:** Sprawdź Wypalenie
**Tagline:** Rozpoznaj i pokonaj wypalenie zawodowe
**Pozycjonowanie:** Diagnoza + profilaktyka + regeneracja, oparte na MBI Maslach.

## Paleta kolorów

| Rola | HEX | Użycie |
|---|---|---|
| Primary (deep amber/brąz) | `#7c5b3c` | nagłówki, znak |
| Primary dark | `#5a4129` | hover, ramki |
| Primary light | `#c4a882` | tła sekcji, "świece" |
| Accent (orange flame) | `#e8922d` | "Wypalenie", płomień, akcenty |
| Accent dark | `#c07824` | hover na akcent |
| Trust (sage regeneration) | `#7a9a6d` | linki regeneracji, iskry zieleni |
| Background ivory amber | `#f0e2c8` | tła sekcji |
| Text primary | `#3a2918` | nagłówki |
| Text body | `#5a5a5a` | akapity |

**Logika:** brąz = drewno świec, ciało wypalonego. Pomarańcz = płomień, energia, ogień. Zieleń = nowy pęd, regeneracja, możliwość. Trzy fazy energetyczne.

## Galeria artykułowa — 10 artykułów

### Konwencja stylu

**Estetyka:** "clinical workplace photography" — autentyczne biura, gabinety, szpitale. Prawdziwi profesjonaliści w stanach wyczerpania, ale bez melodramatu. Naturalne światło, ziemiste tony.

### Universal AI prompt suffix

```
... clinical workplace documentary photography, natural daylight, real
professionals in workplace settings, palette of warm earth tones (deep
amber #7c5b3c, orange flame #e8922d, sage green #7a9a6d), shallow depth
of field, magazine-quality, no text overlays, 16:9 aspect ratio
--ar 16:9 --style raw
```

Negative: `--no neon, fake smile, melodrama, plastic, instagram filter, hdr, american corporate stock, beauty influencer`

---

### #1 — Test Maslach (PILLAR) — `01-test-maslach-diagnostyka-wypalenia.md`
**Hero prompt:** `Editorial photo: professional at desk holding pen over questionnaire, expression of focused contemplation, warm desk lamp light, half-finished coffee, real workplace not staged. [+suffix]`
**Inline:** `01-trzy-wymiary-mbi.svg` — diagram 3 wymiary MBI: wyczerpanie emocjonalne / depersonalizacja / poczucie braku osiągnięć.

### #2 — Fazy wypalenia — `02-fazy-wypalenia-freudenberger-maslach.md`
**Hero:** `Documentary photo: professional walking from bright office to dim hallway, lighting transitioning from energizing to fatigued, conceptual but realistic. [+suffix]`
**Inline:** `02-12-faz-freudenberger.svg` — 12 faz Freudenbergera/Northa od kompulsywnego entuzjazmu do całkowitego załamania.

### #3 — Wypalenie w zawodach pomocowych — `03-wypalenie-zawody-pomocowe.md`
**Hero:** `Documentary photo: nurse/doctor at end of shift sitting on hospital corridor bench, scrubs visible, exhaustion authentic not theatrical, soft fluorescent light. [+suffix]`
**Inline:** `03-secondary-traumatic-stress.svg` — model STS + compassion fatigue + burnout w trzech kręgach.

### #4 — Wypalenie vs depresja — `04-wypalenie-vs-depresja-roznicowanie.md`
**Hero:** `Editorial split photo: same person in two contexts — left office (fatigue), right home (anhedonia). [+suffix]`
**Inline:** `04-mapa-roznicowania.svg` — tabela 8 kryteriów różnicujących burnout vs depresja kliniczna.

### #5 — Quiet quitting — `05-quiet-quitting-psychologia-zjawiska.md`
**Hero:** `Editorial photo: employee at desk doing minimum-required work, phone visible, neutral expression — neither engaged nor stressed. [+suffix]`
**Inline:** `05-quiet-quitting-vs-burnout.svg` — porównanie quiet quitting vs disengagement vs burnout.

### #6 — Powrót po wypaleniu (BOFU) — `06-powrot-po-wypaleniu-protokol.md`
**Hero:** `Documentary photo: person on park bench during lunch break, eating slowly, reading paper book, relaxed posture, soft afternoon light. [+suffix]`
**Inline:** `06-protokol-90-dni.svg` — plan 90-dniowy: stabilizacja / odbudowa / reintegracja.

### #7 — Rola przełożonego — `07-rola-przelozonego-w-wypaleniu-zespolu.md`
**Hero:** `Documentary photo: small team meeting, manager listening attentively to junior employee, warm office light, real engagement. [+suffix]`
**Inline:** `07-job-demands-resources.svg` — model JD-R Bakker-Demerouti.

### #8 — Work-life balance — `08-work-life-balance-evidence-based.md`
**Hero:** `Editorial photo: person closing laptop at end of workday, evening light, soft transition from work mode to home mode. [+suffix]`
**Inline:** `08-cztery-kwadranty-wlb.svg` — Stewart Friedman Total Leadership 4 obszary.

### #9 — Cornerstone: Fizjologia stresu chronicznego — `09-fizjologia-stresu-chronicznego.md`
**Hero:** `Conceptual photo: person checking smartwatch HRV display in morning light, contemplative not alarmed. [+suffix]`
**Inline:** `09-os-hpa-allostatic-load.svg` — model McEwen allostatic load + cykl HPA + cytokiny.

### #10 — Wypalenie w IT — `10-wypalenie-w-it-specyfika-branzy.md`
**Hero:** `Documentary photo: developer at home office at night, multiple monitors, posture of contemplative exhaustion not heroic crunch. [+suffix]`
**Inline:** `10-cykle-it-burnout.svg` — typowe cykle: deadline → crunch → recovery → kolejny crunch.

---

## Subtelne techniki przekierowania (BOFU)

sprawdzwypalenie.pl jest najbardziej BOFU domeną w klastrze NURIO. CTA:

1. **Test MBI** — bezpośrednie odniesienie do walidowanego narzędzia jako *konkretnego, mierzalnego* punktu startu.
2. **Frame**: "test daje liczbę, dzięki której rozmowa z lekarzem jest szybsza" — narzędzie pomocnicze.
3. **Bez sprzedażowego naciska** — psychologia BOFU u osób w wypaleniu *nie* działa przez agresywny CTA, działa przez *empatyczną walidację*.
4. **Numery pomocy w stopce** zawsze.
