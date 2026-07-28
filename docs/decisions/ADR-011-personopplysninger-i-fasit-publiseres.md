# ADR-011 — Personopplysninger i fasit publiseres; proveniens-etikett i kildeteksten redigeres ikke

Status: akseptert
Dato: 2026-07-28
Retrospektiv: nei (besluttet i forhåndskontrollen før Zenodo-DOI)

## Kontekst

Forhåndskontroll av hele git-historikken før en permanent Zenodo-DOI. To ting
ble funnet i `data/fasit_n8.json`, side `Scan4_p031` — en av de åtte
blindfasit-sidene:

1. **Personopplysninger.** Siden gjengir et helt brev signert «Christian
   Jensen. Fr. Stangs gt. 5.I.», med fødselsdato «20/4-1896» og opplysning om
   at han er «gift og har 3 at forsörge». Navn, fødselsdato og adresse til en
   navngitt privatperson.
2. **Institusjonsnavn i kildeteksten.** Samme brev nevner museet ved navn.
   Institusjonsnavnet er ellers fjernet fra utgavens kolofon og cover, og er i
   dette repoet generisert til «en museumssamling i Oslo» **i prosa om
   materialet** (9 steder: `.gitignore`, `LICENSE-DATA`, `METODE.md`,
   `README.md`, `src/*`).

## Beslutning

1. **`Scan4_p031` publiseres uendret.** Personopplysningene forblir i fasiten.
2. **Institusjonsnavnet der det står inne i kildeteksten (Aars' egen
   dagbokprosa) røres ikke.** Generiseringen gjelder kun proveniens-etiketter i
   prosa *om* materialet, aldri ord som forekommer *i* materialet.

## Begrunnelse (falsifiserbar)

- **Allerede offentlig utgitt.** Brevet står i Aars' dagbøker bind I–III, som
  dekker 1920–1940 sammenhengende og selges kommersielt. Å holde teksten
  tilbake fra det åpne forskningsartefaktet mens den ligger i en solgt bok er
  inkonsistent.
- **Avdød person.** Christian Jensen er født 1896 og for lengst død. GDPR
  gjelder ikke avdøde.
- **Fasiten er urørt av prinsipp** (jf. ADR-009). Den er målegrunnlaget; alle
  CER/WER-tall er Levenshtein mot nøyaktig denne strengen, og en redigert fasit
  gir andre tall enn de rapporterte. Å redigere kildetekst for å skjule en
  proveniensetikett ville dessuten være nøyaktig den *stille utelatelsen* vi
  ellers dokumenterer som en feilmodus (jf. litteratur/TEKGURLER-2025:
  sikkerhetsfiltre som etterlater utransklaterte partier i historiske
  manuskripter). Fasiten er fasit fordi den er urørt.

Falsifiserbart: endre ett tegn i `data/fasit_n8.json` og kjør
`src/measure_cer.py` på baseline — tallet flytter seg, og reproduksjonen mot
`results/aggregat.json` bryter.

## Alternativer vurdert

- **Maskere personopplysningene i p031** — avvist: bryter fasit-integriteten,
  og teksten er alt publisert i bokform.
- **Holde p031 helt ute** — avvist: inkonsistent med den kommersielle
  utgivelsen, og svekker målegrunnlaget (åtte sider → sju).
- **Fjerne institusjonsnavnet inne i brevet** — avvist: stille utelatelse i
  kildetekst; samme feilmodus vi kritiserer maskinelt andre steder.

## Konsekvenser

Skillet fra ADR-009 videreføres og skjerpes: **innhold i kilden** (stedsnavn,
personnavn, institusjonsnavn slik de står i Aars' prosa) er tillatt og røres
aldri; **prosa om kilden** (proveniens-etiketter, tese, patentspor) er sealed
eller generisert. Institusjonsnavnet er derfor borte fra all prosa om
materialet, men bevart der Aars selv skrev det.
