# ADR-006 — Adaptiv terskling (metode A) falsifisert

Status: forkastet
Dato: 2026-07-17
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

Hypotese: lokal adaptiv terskling (Sauvola-lignende, ImageMagick `-lat`) ville
slå tesseracts egen gråtone-binarisering på fotografert typoskript med myke
skygger fra Adobe Scan.

## Beslutning

Forkast metode A. Behold tesseracts egen binarisering (baseline).

## Begrunnelse (falsifiserbar)

Testet på verstesiden **p084** (baseline 36,0 % CER), tre DPI-riktige vinduer:

| vindu | CER p084 | hypotese-ordtelling |
|--|--|--|
| baseline | 36,0 % | ~262 (ekte) |
| `-lat 151x151+8%` | 77,8 % | 409 |
| `-lat 201x201+10%` | 114,1 % | 769 |
| `-lat 251x251+12%` | 101,6 % | 683 |

`-lat` lager speckle på Adobe Scan-foto som tesseract leser som ekstra tegn;
ordtellingen eksploderer og CER går over 100 %. Vinner på verstesiden er
vinner overalt — ingen vant, så A ble ikke kjørt på alle åtte.

Falsifiserbart: tallene er reproduserbare fra `results/n8_eksplorativ.tsv`
(radene `adaptiv_a[...]`) og `src/ocr_adaptive_a.sh`.

## Alternativer vurdert

- **Andre vindusstørrelser** — tre DPI-riktige vinduer dekket spennet; alle
  verre enn baseline.
- **A på alle åtte sider likevel** — avvist: ingen kandidat slo baseline på
  verstesiden.

## Konsekvenser

Negativt resultat, motsatt av hva litteraturen antyder for skygget materiale.
Verdt å publisere nettopp fordi det er kontraintuitivt.
