# Testimonials — screeny z komunikatorów

Tu wrzucasz pliki PNG/JPG ze screenami z Messenger / WhatsApp / Signal.

## Konwencja nazw

`<komunikator>-<kolejny_numer>.png` — np. `messenger-01.png`, `whatsapp-02.png`, `signal-03.png`.

Dokładne ścieżki do plików deklarujesz w `domains/<slug>.yaml` w sekcji `testimonials.items[].image`.

## Wymagania techniczne

- Format: **WebP** (najlepiej) lub PNG/JPG
- Szerokość: **600–900 px** (wyświetlamy max ~360 px wysokości w karcie + lightbox do 78vh)
- Waga: **<150 KB** per plik (po kompresji TinyPNG / squoosh.app)
- Aspect ratio: portret (3:4 lub 4:5) — wygląda najlepiej w gridzie

## RODO — checklist przed publikacją

1. **Zgoda klienta** na publikację screena (mail/wiadomość zwrotna „zgadzam się na publikację" wystarczy — zachowaj w archiwum)
2. **Zamaż** (Photoshop / Paint.NET / GIMP, narzędzie blur lub solid fill):
   - Imiona i nazwiska klientów (chyba że klient się zgodził na pełne dane)
   - Numery telefonów
   - Avatary (jeśli rozpoznawalne osoby trzecie w tle)
   - Adresy e-mail
   - Treści wrażliwe (diagnozy, dane zdrowotne, dane finansowe)
3. **Sprawdź metadane EXIF** — usuń (np. ExifTool: `exiftool -all= file.png`)
4. **Anonimizacja w `name`** w yaml: użyj imienia + inicjału nazwiska („Anna K.") albo pseudonimu zaakceptowanego przez klienta

## Workflow dodania nowego testimoniala

1. Wrzuć plik do tego katalogu (`src/static/img/testimonials/`)
2. Dodaj wpis do `domains/<slug>.yaml` → `testimonials.items`:
   ```yaml
   - channel: "whatsapp"           # messenger | whatsapp | signal | sms | email
     image: "/img/testimonials/whatsapp-03.png"
     alt: "Opis dla a11y i SEO"
     name: "Imię N."
     role: "rola/zawód (opcjonalnie)"
     quote: "Krótki cytat dodający kontekst do screena (opcjonalnie)"
   ```
3. Rebuild: `python build.py --domain <domena> --clean`
4. Preview: `cd output/<slug> && python -m http.server 8766`
5. Push do main → GitHub Actions deployuje na Cyber_Folks

## Jak zamazywać szybko (Windows)

- **Paint.NET** (free): zaznacz prostokąt → `Effects → Blurs → Gaussian Blur → 30+`
- **paint.net + plugin Pixelate**: jeszcze lepsza ochrona dla nazwisk
- **PowerToys Image Resizer**: do zmiany wymiarów partami

## Jak zrobić zgrabne screeny z komunikatorów

- **Messenger Desktop**: `Win+Shift+S` (Wycinanie) → wybierz tylko bańkę wiadomości + datę
- **WhatsApp Web**: ten sam trick, ukryj nazwę kontaktu w sidebarze (Ctrl+Shift+] żeby zminimalizować) lub wytnij sam dymek
- **Signal Desktop**: `Win+Shift+S` lub plugin „SnipDo"
- Dorzuć **subtelny watermark** (logo domeny w rogu) — żeby ktoś nie wziął screena na inną stronę

## Pro tip

Najlepiej działają **3 screeny jednocześnie z 3 różnych komunikatorów** (Messenger + WhatsApp + Signal) — sygnał „klienci docierają do nas wieloma kanałami, autentyczne". Schema.org Review markup w template zwiększa szansę na rich result w Google.
