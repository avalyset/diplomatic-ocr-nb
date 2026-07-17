# METODE

Det som *er* målt, ingenting mer. Alle tall er reproduserbare fra
`src/measure_cer.py` mot `data/fasit_n8.json`. Baseline reproduserer
`results/aggregat.json → baseline` nøyaktig (bit for bit), noe som
forankrer resten.

---

## 1. Objektet

Anonymt typoskript, ett eksemplar, i Vigelandsmuseets samling.
Transkribert fra Harald Aars' (1875–1945) håndskrevne dagbøker.
Ukjent hånd, ukjent tidspunkt. Manusside 1–237+, 14.10.1920 – nov. 1940.
Riksmål med ö. Skannet med Adobe Scan (iOS), 400 dpi.

**Proveniens uavklart** — hvem som skrev typoskriptet av, og når, er ikke
fastslått. Dette er en åpen luke i utgaven og skal stå som det.

Sidebildene og kildeteksten ut over de åtte fasitsidene er **ikke** en del
av dette repoet; objektet tilhører museets samling og avklares med
institusjonen før eventuell bildepublisering. Fasit-transkripsjonen av de
åtte sidene kan publiseres uavhengig av bildene (se ADR-009).

## 2. Blindprotokoll

Åtte sider, `random.seed(1930)`, `random.sample(range(1,105), 8)` fra Scan4
(manus 134–237): PDF-sidene 3, 27, 31, 51, 54, 79, 84, 100 (`data/UTVALG.txt`).

Fasit ble skrevet diplomatarisk i `src/transkriber.html` **før** noen
OCR-tekst var sett. Verktøyet inneholder ingen OCR — kun bilde-id og et
tekstfelt med `spellcheck="false"`, `autocorrect="off"`. Resultat:
**2 188 ord / 12 478 tegn** (etter whitespace-normalisering).

Terskler satt **før** måling: < 5 % CER = utgivbart, > 15 % = manuell
transkripsjon nødvendig.

## 3. Måling

CER = Levenshtein(tegn, hypotese, fasit) / referansetegn.
WER tilsvarende på ord. Whitespace normalisert på begge sider. Rene
sidetall-linjer (f.eks. «- 2 -») fjernet symmetrisk fra hypotesen (fasiten
har dem ikke): 34 tegn for baseline. KI: bootstrap over de åtte sidene,
10 000 resamplinger, `seed 1930`.

| metode | CER | WER | per side (CER) |
|--|--|--|--|
| **baseline** — tesseract 400 dpi gråtone, `-l nor --psm 6` | **21,3 %** (95 % KI 14,7–28,1) | 52,4 % (41,0–64,7) | 9,8 – 36,0 % |
| **A** — adaptiv terskling (ImageMagick `-lat`) | *se pkt. 5a* | — | — |
| **B** — `claude-opus-4-8` vision, diplomatarisk prompt | **5,35 %** (95 % KI 3,0–8,0) | 12,9 % (10,2–16,2) | 2,2 – 11,4 % |
| **D** — Adobe tekstlag | *død, se pkt. 5b* | — | — |

Per side og aggregat: `results/n8_eksplorativ.tsv`, `results/aggregat.json`.

**Dom mot terskel: UAVGJORT.** B bommet på 5 %-terskelen (punktestimat
5,35 %), men konfidensintervallet inkluderer 5 %. Rapporteres som uavgjort,
ikke som bestått. **Ingen post-hoc utvidelse av n.**

## 4. Diplomatarisk troskap — hovedfunnet

Metode B, over åtte sider (`results/troskap.tsv`):

- **ö = 71, ø = 0**
- efter bevart (etter = 0), skulde bevart (skulle = 0), nu = 8 (nå = 0)

Ingen umotivert modernisering målt. Dette er hovedfrykten ved LLM-basert OCR
på historisk materiale: stille normalisering som ikke oppdages fordi
resultatet *ser* korrekt ut. Under diplomatarisk prompt er den her målt til
null i den fryktede retningen (ö→ø).

**Forbehold, eksplisitt (to stykker):**

1. *Ingen kontrollarm.* Om prompten forårsaket troskapen, eller om modellen
   ville vært trofast uansett, er **ikke** målt. Ingen kausal påstand kan
   fremsettes fra disse dataene.
2. *Retningen den andre veien.* Den menneskelige fasiten har ö = 65, ø = 3,
   mens B har ö = 71, ø = 0. B normaliserte altså ikke ö→ø, men differansen
   (tre ø i fasit, null i B) betyr enten at B leste tre genuine ø som ö
   (en liten troskapsfeil, motsatt retning av den fryktede), eller at
   fasitskriveren skrev ø der kilden har ö. Ikke avgjort her. Uansett er
   avviket allerede talt med i Bs 5,35 % CER.

## 5. Forkastede metoder — negative resultater

Rapportert rett, ikke begravd.

### 5a. Adaptiv terskling (metode A) — falsifisert

Hypotesen: lokal adaptiv terskling (Sauvola-lignende, `-lat`) ville slå
tesseracts egen gråtone-binarisering på fotografert typoskript. Testet på
verstesiden **p084** (baseline 36,0 % CER), tre DPI-riktige vinduer:

| vindu | CER p084 |
|--|--|
| baseline (tesseracts binarisering) | **36,0 %** |
| `-lat 151x151+8%` | 77,8 % |
| `-lat 201x201+10%` | 114,1 % |
| `-lat 251x251+12%` | 101,6 % |

Vinner på verstesiden er vinner overalt; ingen vant, så A ble ikke kjørt på
alle åtte. `-lat` lager speckle på Adobe Scan-foto som tesseract leser som
ekstra tegn (hypotese-ordtelling 409/769/683 mot ~262 ekte ord). Motsatt av
hva litteraturen antyder for skygget materiale. **A eliminert.** (ADR-006)

### 5b. Adobe tekstlag (metode D) — død

- 3 av 4 skann (Scan1/2/4, «Adobe Scan for iOS») har **0 tegn** tekstlag.
  De åtte fasitsidene er alle Scan4 → D er ikke målbar mot fasiten.
- Det fjerde (Scan3, «Acrobat Paper Capture», 1925–27) har tekstlag, men
  **ö = 0, ø = 112** — normalisert. Adobe gjør stille nøyaktig det B ikke
  gjorde. Diskvalifisert uansett hvor lav en CER måtte være. (ADR-007)

Verdt å vite for alle som OCR-er norsk førkrigsmateriale med Acrobat.

### 5c. CER målt mot redigert utgave — ugyldig

Å måle OCR mot den *redigerte* bokutgaven (ikke en trofast transkripsjon) ga
et falskt 25,2 %, dekomponert til ~67 % OCR-feil / ~30 % tegnsetting / ~3 %
modernisering. Den redigerte teksten fantes; blindfasiten måtte skrives.
Fristende metodefeil. (ADR-003)

### 5d. difflib-strengmatch som ordforslag — forkastet

Ga *björnegruppen → barnegruppen* (ratio 0,88) og *ensartede → entartede*
(0,889). Tegnavstand måler ikke betydning. (ADR-004)

### 5e. Regelen «-ede → -et + konsonantdobling» — forkastet

Ga *rede → rett*, *lede → lett*, *træde → trett*. 3 feil av 42 rader = 7 %
feilrate på et verifiseringssett. (ADR-005)

## 6. Hva som *ikke* er et funn

At Claude slår tesseract. Det er trivielt, modellavhengig, og foreldet innen
året. Bidraget er **måleprotokollen for diplomatarisk troskap** — ö/ø-rate og
arkaisk bevaringsratio — som kan brukes på hvilken som helst modell og hvilket
som helst historisk korpus.

## 7. Omfang

Ett språk, ett korpus, én modell, åtte sider. Metodenotis med case.
Ingen generaliserbare påstander.

## 8. Verktøy og attribusjon

`claude-opus-4-8` er både verktøy under test (metode B) og verktøy i
utførelsen (kode skrevet med Claude Code). Fasiten er skrevet av et menneske
**uten** modellen i loopen — det er nettopp derfor blindprotokollen finnes.

Author/committer: Eirik Botten Nicolaysen. `Co-authored-by`-trailer der Claude
Code skrev kode.
