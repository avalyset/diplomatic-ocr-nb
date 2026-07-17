# ADR-002 — Blindfasit som eneste gyldige målestokk

Status: akseptert
Dato: 2026-07-16
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

OCR-kvaliteten måtte tallfestes for å avgjøre om den sammenstilte teksten var
utgivbar. En redigert bokutgave fantes, men er ikke en trofast transkripsjon.

## Beslutning

Skriv en **menneskelig blindtranskripsjon** av åtte tilfeldig trukne sider
**før** noen OCR-tekst er sett, og mål CER/WER mot den. Terskler settes før
måling: < 5 % CER = utgivbart, > 15 % = manuell transkripsjon.

## Begrunnelse (falsifiserbar)

- Å måle mot den redigerte utgaven ga et falskt lavt/uforståelig tall
  (25,2 %, se ADR-003) fordi utgaven er modernisert og renset.
- Trekk: `random.seed(1930)`, `random.sample(range(1,105), 8)` → PDF-sider
  3, 27, 31, 51, 54, 79, 84, 100 fra Scan4.
- Verktøyet (`src/transkriber.html`) inneholder **ingen** OCR-tekst;
  `spellcheck="false"`, `autocorrect="off"`. Fasit: 2 188 ord / 12 478 tegn.
- Terskler satt før måling for å hindre bevegelige målstenger.

Falsifiserbart: dersom fasitfila inneholdt OCR-forslag, eller terskler ble
satt etter at tallene var kjent, er protokollen brutt.

## Alternativer vurdert

- **Måle mot den redigerte utgaven** — forkastet (ADR-003).
- **Ingen måling** — avvist: utgivbarhet ville vært udokumentert.

## Konsekvenser

Alle CER/WER-tall i repoet hviler på `data/fasit_n8.json`. Fasiten kan derfor
ikke redigeres i ettertid uten å ugyldiggjøre tallene (se ADR-009).
