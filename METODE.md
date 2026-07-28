# METODE

Det som *er* målt, ingenting mer. Alle tall er reproduserbare fra
`src/measure_cer.py` mot `data/fasit_n8.json`. Baseline reproduserer
`results/aggregat.json → baseline` nøyaktig (bit for bit), noe som
forankrer resten.

Dokumentet dekker to caser. **Case 1 — Aars** (seksjon 1–8) er blindvalidert
med CER mot en menneskeskrevet fasit og står uendret. **Case 2 — Vigeland**
(nederst) er et materiale *uten* fasit; det føyer til det som faktisk skiller
casene og hviler på andre kontroller enn CER. Ingen sidebilder, intet bokmanus
og ingen redaksjonshistorie ligger i dette repoet — bare tallene og eksemplene.

---

## 1. Objektet

Anonymt typoskript, ett eksemplar, i en museumssamling i Oslo.
Transkribert fra Harald Aars' (1875–1945) håndskrevne dagbøker.
Ukjent hånd, ukjent tidspunkt. Manusside 1–237+, 14.10.1920 – nov. 1940.
Riksmål med ö. Skannet med Adobe Scan (iOS), 400 dpi.

**Proveniens uavklart** — hvem som skrev typoskriptet av, og når, er ikke
fastslått. Dette er en åpen luke i utgaven og skal stå som det.

Sidebildene og kildeteksten ut over de åtte fasitsidene er **ikke** en del
av dette repoet; objektet tilhører en museumssamling i Oslo og avklares med
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
2. *Overkorrigering den andre veien.* Den menneskelige fasiten har ö = 65,
   ø = 3, mens B har ö = 71, ø = 0 — B fant altså *færre* ø enn mennesket.
   B normaliserte ikke ö→ø (den fryktede retningen), men promptens eksplisitte
   «ö skal være ö, ikke ø» kan ha overkorrigert *motsatt* vei og gjort tre
   ekte ø til ö. Alternativt skrev fasitskriveren ø der kilden har ö — ikke
   avgjort her. Prompten ligger i repoet (`src/vision_ocr.py`), så en leser
   kan se den nøyaktige instruksjonen som kan ha forårsaket avviket. Uansett
   er det talt med i Bs 5,35 % CER.

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

---

# Case 2 — Vigeland: *Erindringer* (1918)

Samme spørsmål — diplomatarisk troskap — men et materiale som fjerner
grunnlaget for målemetoden i Case 1. Det som følger er hva forskjellen tvang
frem, og hva som er nytt. Utgaven selv (287 sider, ~128 000 ord) hører til
andre steder; her står bare tallene og eksemplene som skiller casene.

## 2.1 Ulik kildetype — og hva den tvinger frem

Case 1 er et typoskript med **kjent forelegg** (Aars' egen håndskrift) og en
**etablert blindfasit**. Case 2 er ett ledd lenger unna: en maskinskrevet
**transkripsjon fra 1949 av Vigelands håndskrevne manuskript**. Avskriveren —
ikke forfatteren — er den siste hånden på teksten, forelegget er ikke
tilgjengelig, og **ingen fasit finnes eller kan skrives** (å skrive en fasit
ville kreve nettopp den håndskriften avskriveren allerede tapte partier av).

Konsekvensen for metodevalg er absolutt: CER mot fasit er umulig. Troskap kan
ikke *måles mot en referanse*; den kan bare *overvåkes mot kildens egne
interne holdepunkter* — ö/ø-forholdet, ordantall mot en komparator,
arkmerkene, og kildens egen luke-konvensjon. Case 1 velger metode med et tall.
Case 2 må vokte en produksjon uten et slikt tall.

## 2.2 Populasjonsdekkende porter, ikke stikkprøve-CER

CER er riktig verktøy når **metoden velges**: Case 1 målte fire metoder på åtte
sider og fikk 5,35 % for vinneren. Det er feil verktøy når **produksjonen
overvåkes**: en stikkprøve på 8 av 287 sider sier ingenting om de 279 andre.
En metode som er trofast på gjennomsnittet kan kollapse på én side, og CER på
et tilfeldig utvalg vil sannsynligvis aldri se den.

Derfor: tre deterministiske porter på **alle 287 sider**, ikke et estimat på
et utvalg. Flagg, aldri rett. Tallene i tabellen er på **rå OCR** — den
utskriften portene overvåker, før dedup og modernisering.

| port | Case 2 — Vigeland, rå OCR (287 sider) | Case 1 — Aars, produksjon (114 sider, ADR-010) |
|--|--|--|
| **a — ö/ø** | ö = 5161, ø = 19; men 15 ø ligger i OCR-avslags-/håndskrift-metatekst — **4 ekte brödtekst-ø** (ark 204, 163, 235) | ö = 1081, ø = 5 (ø-andel 0,46 %) |
| **b — ordantall mot komparator** (< 60 %) | 2 sider ny-dropout; 97 ark gammel-dropout | ikke kjørt |
| **c — garble-markører** | 4 vokalløse ord, 0 ord > 25 tegn, 2 gjentatte linjer, 86 uventede tegn (mest aksenter) | ikke kjørt |

**Hvilket sett hvert tall stammer fra.** Aars-kolonnen er *produksjonen* (114
sider), ikke blindfasit-settet. Fasit-tallet ö = 71 / ø = 0 gjelder de **8
tilfeldig trukne sidene metoden ble valgt på** (§4) og skal ikke settes mot et
populasjonstall — å måle 287 sider mot 8 er nettopp feilen seksjonen advarer
mot. Produksjon mot produksjon: 1081/5 (Aars, 114 sider) og 5161/19 (Vigeland,
287 sider, rå OCR).

**Vigeland gjennom stadiene** (ö/ø): rå OCR 5161/19 → manusström etter dedup,
med dublett-ark og avslagssider ute, 5094/4 → ferdig EPUB inkl. kolofon
5095/11 (kolofonen er moderne bokmål og bidrar med ø). De 4 ekte brödtekst-ø
overlever hele veien; de 15 øvrige forsvinner med avslagssidene, **ikke ved
retting**.

Porten er ikke et kvalitetstall, men et *filter*: den løfter hver avvikende
side til øyet i stedet for å love at snittet er godt. Til kontrast hadde det
gamle EPUB-korpuset (port c, runde 1) 286 vokalløse ord i Del 3 og 357
gjentatte linjer i Del 4 — porten skiller de to kvalitetsklassene skarpt.

## 2.3 Den forkastede OCR-runden som diagnostisk instrument

Et eldre EPUB-korpus (tidligere OCR) var **ubrukelig som lesetekst** —
massivt teksttap, gjentatte avsnitt, korrupt tegnsetting. Det ble ikke brukt
som tekst. Men brukt som **komparator** i port b avdekket det dropout i begge
retninger: **97 ark** der den gamle hadde tapt tekst (ytterpunkt ark 113: ny
459 ord mot gammel 15 = 30,6×; ark 95: 21×), og **2 ark** der den nye OCR-en
slapp. Uten en uavhengig andre-måling ville ny-dropout på de to arkene ikke
hatt noe å slå ut mot.

Prinsipp: **kast aldri den dårlige transkripsjonen.** En verdiløs tekst er
fremdeles en uavhengig måling. Dens verdi lå ikke i ordene, men i at den var
laget separat og derfor kunne krysse den nye.

## 2.4 Arkmerket som data

Side↔ark ble rekonstruert fra de **trykte arkmerkene** i typoskriptet
(`- 93 -`, `— 93 —`, `258 a`), ikke fra aritmetikk (sidenummer + offset).
Merkene fanget det aritmetikken ikke kunne:

- **Drift** — en innskutt skannside (avslagstekst, ikke et nummerert ark) ga
  −1-forskyvning i resten av en del; merket, ikke telleren, avslørte det.
- **Innskutte a-ark** — 221a og 258a, ark uten eget heltallsnummer.
- **Falmede dubletter** — samme ark skannet to ganger: ark 115 (99,6 %
  identisk tekst), 226 (99,5 %), 258a (93,7 %). Aritmetikk teller dem som to.
- **Feiltelt hale** — runde 1s antatte «271–279» (ni numre på åtte sider) var
  en aritmetikkfeil; halen er 272–279, én-til-én, og **intet ark mangler**.

Hver gang aritmetikk og arkmerke var i konflikt, tok **aritmetikken feil**.
De reelle hullene (ark 172, defekt OCR-fil med skann i behold; ark 266,
nummerhopp) ble stående som luker nettopp fordi merkene, ikke tellingen,
avgjorde dem.

## 2.5 Kilden markerer sin egen stemme

Teksten har to lag som ikke skal blandes: **Vigelands tekst** (1. person,
«jeg husker …») og **transkripsjonens apparat** (redaksjonelt, tredje-
person/imperativ: «(I margen: flyttes frem.)»). De skilles på grammatisk
person og parentes-notasjon — et strukturelt signal i kilden selv, ikke en
skjønnsvurdering — og apparatet moderniseres aldri.

**Anførselstegn er en hard port mot retting:** et ord i anførsel er sitat
eller navn og røres ikke, uansett hvor «feil» det ser ut. Eksempel:
**«Tarrisken»** — et økenavn som spiller på «ta risken». En plausibilitets-
eller stavekorrektur ville delt det til to ord; anførselsporten forbyr det,
og navnet står. Kilden vet forskjellen på sin egen stemme og en feil; oppgaven
er å høre etter, ikke å overprøve.

## 2.6 Luke-klassifisering: falsifisering og revalidering

151 tomrom-luker i typoskriptet ble delt i **belagt** (ekte luke der
avskriveren ikke kunne tyde forelegget → merkes `[…]`) og **ubelagt** (rent
skrivemaskin-mellomrom → kollapser).

- **Opprinnelig kriterium** — belagt kun på snevre syntaktiske signaler
  (anførsel, manglende ord foran tegnsetting, preposisjon foran); resten
  antatt skrivemaskin.
- **Stikkprøven som felte det** — 10 tilfeldige fra den *ubelagte* gruppen
  lest mot sidebildet: **4 av 10 var ekte luker**. Kriteriet forkastet.
- **Revidert kriterium** — kun gap rett etter setningsslutt (`.`/`!`/`?`) *og*
  fulgt av stor forbokstav regnes som skrivemaskin; alt annet er belagt.
  Resultat: **93 belagt / 58 ubelagt**.
- **Revalidering på usett data** — 10 nye trukket fra de gapene som flyttet
  til belagt, lest mot bilde. Tre av de ti var allerede sett i den første
  stikkprøven, så **effektiv usett n = 7, ikke 10**. **7 av 7 var ekte luker.**

**Utraderingstest** (er tomrommene utraderinger, ikke luker?): på et utvalg
sider ble **50 gap** kontrastforsterket (normalisering, gamma, R/G/B-kanaler,
høypass) og målt mot en kontroll — interlinjen i samme kolonne, som fanger
papir og gjennomslag men aldri har hatt tekst. **50 av 50: ingen spor.**
Tolkningens grunnlag: en mekanisk utradering **lysner** — den sliper
papiroverflaten — mens gjennomslag og avsmitting **mörkner**. Sporene som
fantes i gapene var mörke (gjennomslag), aldri den lysende signaturen på
utradering. Tomrommene er luker.

## 2.7 Ærlige begrensninger (Case 2)

- **Ingen målt CER.** Ingen fasit finnes for Vigeland, og ingen kan skrives.
  Troskapen hviler på portene og ö/ø-forholdet i manuskript-brödteksten
  (5094 ö / 4 ø etter dedup; rå OCR fanget 19 ø, men 15 var avslagsmetatekst),
  ikke på en referanse. Dette er **svakere bevis** enn Case 1s blindmåling og
  skal leses som det: fravær av flagg er ikke det samme som en målt feilrate.
- **n = 2 caser.** To materialer, ingen populasjon. Ingenting generaliseres
  fra to punkter.
- **Luke-metoden lokaliserer bare brede gap automatisk.** Smale 2–3-tegns
  belagte gap skilles ikke fra vanlig setningsmellomrom ved skann-
  oppløsningen og må sjekkes for hånd. Utraderingstestens «50 av 50» gjelder
  det maskinelt lokaliserbare utvalget, ikke alle 93 belagte gap.
