# diplomatic-ocr-nb

**Diplomatarisk troskap i OCR av norsk typoskript — blindvalidert metodesammenligning.**

En metodenotis med case: hvor trofast kan ulike OCR-metoder gjengi et norsk
typoskript fra 1920-årene (riksmål med ö) *uten stille å modernisere det*?
Fire metoder er målt mot en menneskeskrevet blindfasit på åtte tilfeldig
trukne sider.

| metode | CER | merknad |
|--|--|--|
| baseline (tesseract) | 21,3 % | referanse |
| adaptiv terskling (A) | ≥ 78 % | eliminert (falsifisert) |
| **vision (`claude-opus-4-8`)** | **5,35 %** | ö bevart 71/0; dom mot 5 %-terskel *uavgjort* |
| Adobe tekstlag (D) | — | død: fraværende/ö-korrupt |

Kjernebidraget er **ikke** at én modell slår en annen (trivielt, foreldet
innen året), men **måleprotokollen for diplomatarisk troskap**: ö/ø-rate og
arkaisk bevaringsratio, brukbar på hvilken som helst modell og hvilket som
helst historisk korpus. Se [`METODE.md`](METODE.md).

**Case 2 (Vigeland, *Erindringer* 1918)** føyer til et materiale *uten* fasit —
en transkripsjon fra 1949 av et håndskrevet manuskript — der troskap
overvåkes med populasjonsdekkende porter på alle sider i stedet for
stikkprøve-CER (rå OCR ö/ø 5161/19, 4 ekte brödtekst-ø), arkmerket brukes som
data mot aritmetikk, og
tomrom-luker klassifiseres med falsifisering, revalidering på usett data og en
utraderingstest. Se [`METODE.md` § Case 2](METODE.md).

## Struktur

```
METODE.md              det som er målt, ingenting mer
docs/decisions/        ADR-kjede (ADR-001 … ADR-010), alle retrospektive
data/
  fasit_n8.json        blindtranskripsjon, 8 sider (2 188 ord / 12 478 tegn)
  UTVALG.txt           trekket: seed 1930
src/
  measure_cer.py       CER/WER + bootstrap-KI (referanseimplementasjon)
  ocr_baseline.py      tesseract-pipeline (baseline)
  ocr_adaptive_a.sh    metode A (forkastet — negativt resultat)
  vision_ocr.py        metode B (leser nøkkel fra miljøvariabel, aldri hardkodet)
  transkriber.html     blindtranskripsjonsverktøyet (ingen OCR i fila)
results/
  n8_eksplorativ.tsv   CER/WER per side, alle målte metoder
  aggregat.json        aggregat + KI per metode
  forvekslinger_baseline.tsv   vanligste tegnforvekslinger (baseline)
  troskap.tsv          ö/ø + arkaiske former, B vs. fasit
```

## Reprodusere

Hypotesefilene (rå OCR, vision-utskrift) og sidebildene er **ikke** i repoet
— objektet tilhører Vigelandsmuseets samling (se *Omfang* under). Tallene i
`results/` er utledet av dem. Med din egen kopi av hypotesene:

```bash
python src/measure_cer.py --fasit data/fasit_n8.json \
    --hyp-dir /sti/til/txt --pattern 'Scan4Aars_p{n}.txt' --label baseline
```

Baseline reproduserer `results/aggregat.json → baseline` bit for bit
(CER = 0.21317518833146337, samme KI). Det forankrer resten av kjeden.

Metode B (krever egen API-nøkkel og egne bilder):

```bash
export ANTHROPIC_API_KEY=...      # aldri i repoet
python src/vision_ocr.py --png-dir /sti/til/png --glob 'Scan4_p*.png' --out-dir ut/
```

## Omfang og grenser

Ett språk, ett korpus, én modell, åtte sider. Ingen generaliserbare
påstander. Sidebildene publiseres ikke her; fasit-transkripsjonen kan
publiseres uavhengig av bildene (ADR-009). Proveniensen til typoskriptet er
uavklart og står som en åpen luke.

## Lisens

- **Kode** (`src/`): MIT — se [`LICENSE`](LICENSE).
- **Data og målinger** (`data/`, `results/`): CC BY 4.0 — se [`LICENSE-DATA`](LICENSE-DATA).

## Sitering

Se [`CITATION.cff`](CITATION.cff).
