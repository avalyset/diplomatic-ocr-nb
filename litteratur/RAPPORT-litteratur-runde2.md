# Litteraturforankring — runde 2

**Dato:** 2026-07-28 · **Spor:** forskning (E1) — ingenting herfra går i bokmanus.
**Metoderegel:** kun åpen tilgang. Betalingsmur = rapportert som blokkering, aldri omgått.
Bibliografiske data er verifisert **fra dokumentet** (eller fra Crossref/ACL Anthology der dokumentet ikke oppgir venue); avvik fra oppgitte snippets er notert i hver notatfil.

Én notatfil per kilde: `FORFATTER-AARSTALL-NOTAT-v1.0-2026-07-28.md`. PDF: `FORFATTER-AARSTALL-KORTTITTEL.pdf`.

---

## DEL A — de fem påstandene, kilde for kilde

| # | Påstand | Bærende kilde(r) | Styrke |
|---|---------|------------------|--------|
| 1 | Referansefri QE er et etablert felt, ikke et hull | **Sindhujan et al. 2025** (Information 16(10):916, i et **QE-temanummer**); **Kocmi & Federmann 2023** (GEMBA-MQM, WMT23); **Moon et al. 2020**; **Agrawal et al. 2022** | **Uangripelig** — flere fagfellevurderte kilder, egen delt oppgave (WMT QE), *et helt temanummer* viet QE (2025), definisjonen står ordrett |
| 2 | RTT med BLEU er svak; med semantiske embeddinger brukbar | **Moon et al. 2020** (primær); **Agrawal et al. 2022** (korroborerer + modererer) | Sterk på «BLEU svak»; **betinget** på «brukbar»: embeddinger løfter RTT, men Agrawal viser at BT alene fortsatt er *dårligere enn veiledet QE* og bare komplementerer det |
| 3 | Modernisering av historisk ortografi med nevrale modeller er etablert | **Tang et al. 2018** (COLING); **Bollmann 2019** (NAACL, «largest study»); **Ciambella 2024** (intralingval, AI) | Sterk — men med nyansen «no consensus on state-of-the-art» (Bollmann), og retningen er *normalisering*, motsatt av diplomatarisk bevaring |
| 4 | Kritisk apparat lar seg ennå ikke produsere automatisk | **Terras et al. 2024** (Scholarly Editing 41) | Middels-sterk, men **avgrenset**: gjelder HTR-plattformer «so far», rammet som nåværende hull med fremtidig mulighet — ikke prinsipiell umulighet |
| 5 | Sikkerhetsfiltre gir utransklaterte partier i historiske manuskripter | **Tekgürler 2025** (arXiv 2503.11898) — *funnet i Del B* | Tynn, men non-empty: ett tallfestet tilfelle (Gemini flagget 14–23 % av et 1700-talls manuskript), interlingval, ikke OCR |

**Referanse-/prøvesteinskilde:**
- **Ataman et al. 2025** (Information 16(9):723) — bred MT-survey i LLM-æraen, signert feltets tyngste (Koehn: Moses + standardverket om SMT; Cho: encoder–decoder-arkitekturen). **Ikke bare bakgrunn:** den naturlige «slik står feltet nå»-referansen og prøvesteinen for egne nyhetspåstander. Dens §5 «Current and Emerging Problems» korroborerer B1-negativfunnet (se under).

**Kontekstkilder (forankrer ingen av de fem, ført ærlig som bakgrunn):**
- **Riley et al. 2025** (arXiv 2510.24664) — MQM re-annotering; bakgrunn for evalueringsparadigmet GEMBA automatiserer.
- **Kutuzov et al. 2022** (NorDiaChange, LREC) — diakronisk semantisk endring for norsk; nordisk historisk-NLP finnes, men rører ikke tekstetablering.

**Tilgang i Del A:** de to MDPI-artiklene (Sindhujan, Ataman) er åpen tilgang (CC-BY). MDPI-serveren avviste automatisert henting (HTTP 403 / Cloudflare) i første omgang, så bib ble midlertidig hentet fra Crossref. **Oppdatert:** begge PDF-ene er nå skaffet (lå på skrivebordet, kopiert md5-verifisert til mappen), og bibliografien er **verifisert fra dokumentets s. 1** — se notatene (v1.1). Ett forbehold står igjen: **temanummer-navnet er ikke trykt i PDF-ene** (kun på tidsskriftets utgavesider, som er blokkert), så de oppgitte temanumrene er ikke dokumentbekreftet. Alle ti PDF-er ligger nå i mappen.

---

## DEL B — søk etter hullene

Fem søketema i ACL Anthology (dekker NoDaLiDa, EAMT, WMT, NAACL) og arXiv. **Treff med full referanse + relevanssetning, og — viktigst — hvor det IKKE finnes noe.**

### B1. Apparatus preservation / editorial markup i MT — **NEGATIVT FUNN (kjernen)**
Ingen CL/NLP-arbeid funnet som behandler maskinell bevaring eller generering av **kritisk apparat / redaksjonell markup som et eget redaksjonelt lag**. Det nærmeste er:
- *Inline-markup for lokalisering* (se B4) — behandler formattagger, ikke apparat-semantikk.
- **Terras et al. 2024** — sier eksplisitt at apparat *ikke* fasiliteres av dagens plattformer.

**Korroborert fra autoritativt hold:** ordsøk i hele **Ataman et al. 2025**-surveyen (feltets tyngste, se over) gir «markup» = 0, «apparatus» = 0, «editorial» = 0, «lacuna» = 0, «footnote» = 0. Dens §5 «Current and Emerging Problems» (s. 16–20) fører lavressursspråk, evaluering og hallusinasjon/**utelatelse** som sentrale åpne problemer, men nevner ikke med ett ord bevaring av apparat, markup, lakuner eller dokumentstruktur («structure» forekommer kun i lingvistisk forstand). Utelatelse behandles der kun som en *hallusinasjonstype* i MT mellom språk, ikke som en integritetsegenskap ved en kildeutgave.

→ **Apparat-integritet er et reelt hull.** Når feltets ledende survey ikke nevner det blant sine åpne problemer, er fraværet et sterkt signal — ikke et oversett hjørne.

### B2. Omission / hallucination detection i MT — **etablert (relevant for dropout, ikke apparat)**
- **«HalOmi: A Manually Annotated Benchmark for Multilingual Hallucination and Omission Detection in Machine Translation»**, EMNLP 2023, ACL `2023.emnlp-main.42`. — Relevans: **omission-deteksjon** er et etablert felt; parallelt til vår ordantall-port som fanget dropout, men gjelder MT mellom språk, ikke tekst-luker i kilde.
- Oppfølgende deteksjonsarbeid: `2024.emnlp-main.1033` (detector aggregation), `2023.tacl-1.32` (model introspection). — Relevans: viser at «tapt innhold» er målbart og studert, men ikke apparat-spesifikt.

### B3. Literary machine translation, evaluering — **etablert (tangentielt)**
- **Toral & Way, «What Level of Quality can Neural Machine Translation Attain on Literary Text?»**, arXiv:1801.04962. — Relevans: grunnleggende evaluering av litterær MT; viser at feltet finnes, men handler om interlingval roman-oversettelse, ikke kildeutgaver.
- Workshop-serien **«Qualities of Literary Machine Translation»**, ACL `W19-73`; dokumentnivå litterær MT `2022.emnlp-main.672`. — Relevans: litterær MT-evaluering er institusjonalisert; ingen berøring med diplomatarisk troskap.

### B4. Translation of TEI-encoded editions / markup — **kun lokaliserings-markup, ikke apparat**
- **«TransIns: Document Translation with Markup Reinsertion»**, EMNLP 2021 demos, ACL `2021.emnlp-demo.4`. — Relevans: bærer *inline-formattagger* gjennom MT.
- **Hanneman & Dinu, «How Should Markup Tags Be Translated?»**, WMT 2020, ACL `2020.wmt-1.138`. — Relevans: strategier for tagg-overføring (masking, reinsertion).
→ **Delvis negativt:** markup *kan* mekanisk føres gjennom MT, men ingen av disse behandler **TEI-kodede vitenskapelige utgaver** eller apparat som redaksjonell semantikk. Evnen til å flytte en `<tag>` er ikke evnen til å bevare et apparatlag.

### B5. Norsk/nordisk historisk tekst og oversettelse (NoDaLiDa m.m.) — **etablert nabofelt**
- **Duong, Hämäläinen & Hengchen, «An Unsupervised method for OCR Post-Correction and Spelling Normalisation for Finnish»**, NoDaLiDa 2021, ACL `2021.nodalida-main.24`. — Relevans: nordisk OCR-etterretting + normalisering; nærmeste metodiske nabo, men finsk og normaliserende.
- **«OCR Error Post-Correction with LLMs in Historical Documents: No Free Lunches»**, RESOURCEFUL 2025, ACL `2025.resourceful-1.8`. — Relevans: LLM-basert OCR-etterretting evaluert mot **diplomatarisk transkripsjonsmål** (bevarer lang-s, ligaturer) — direkte parallell til vår troskapsfilosofi.
- **«Comparative analysis of OCR methods for Sámi texts from the National Library of Norway»**, arXiv:2501.07300. — Relevans: norsk institusjonell OCR på historisk lavressursspråk.
→ Nordisk historisk-OCR og diplomatarisk transkripsjon er aktive; **ingen** av disse tar apparat-integritet eller populasjonsdekkende troskapsporter.

### Negativt hovedfunn, oppsummert
1. **Apparat-integritet i maskinell tekstbehandling er ikke et studert problem** (B1, B4). Det bekrefter at Vigeland-utgavens skille mellom Vigelands stemme og transkripsjonens apparat, ført maskinelt, ligger i et hull.
2. **Sikkerhetsfilter-hull i historisk materiale** har akkurat *ett* funn (Tekgürler 2025) — fenomenet er belagt, men knapt studert.
3. **Populasjonsdekkende troskapsporter (ö/ø, ordantall, garble) som produksjonsovervåkning** i stedet for stikkprøve-CER: ingen direkte parallell funnet i søket. Ført som **foreløpig** negativt funn — søket var ikke uttømmende nok til å utelukke det.

---

## DEL C — blokkert

- **Karas, «Archaization, Modernization …»**, i *Routledge Handbook of Intralingual Translation* (2024), **doi:10.4324/9781003188872-3**. — **Bak betalingsmur (Routledge/Taylor & Francis).** Rapportert som blokkering. Ingen omvei forsøkt; ingen preprint/åpen versjon lokalisert. Bør skaffes via bibliotek/institusjonstilgang om den skal siteres.

---

## Leveranse i `litteratur/`

**PDF-er (åpen tilgang, 12 stk):** Moon 2020, Agrawal 2022, Kocmi 2023, Tang 2018, Bollmann 2019, Ciambella 2024, Terras 2024, Kutuzov 2022, Riley 2025, Tekgürler 2025, **Sindhujan 2025 og Ataman 2025** (MDPI — nå skaffet, md5-verifisert, bib fra dokumentet).
**Notatfiler (12 stk):** én per kilde. Sindhujan og Ataman oppdatert til **v1.1** (dokumentverifisert bib; v1.0 fjernet, historikk i git).
**Blokkert:** Karas 2024 (betalingsmur). Temanummer-navnene for de to MDPI-artiklene er ikke dokumentbekreftet (tidsskriftets utgavesider er blokkert).
