# ADR-003 — CER målt mot redigert utgave forkastet

Status: forkastet
Dato: 2026-07-16
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

Den enkleste tilgjengelige «fasiten» var den redigerte bokutgaven av samme
periode. Den fantes allerede; en blindfasit måtte skrives for hånd.

## Beslutning

Forkast CER målt mot den redigerte utgaven. Bruk blindfasit (ADR-002).

## Begrunnelse (falsifiserbar)

Måling mot den redigerte utgaven ga **25,2 %**, som dekomponert var:

- ~67 % ekte OCR-feil
- ~30 % tegnsettingsforskjeller (utgaven er renset)
- ~3 % modernisering (utgaven er modernisert til bokmål)

Bare den første komponenten er OCR-kvalitet. Tallet blander tre kilder og er
derfor ugyldig som mål på OCR. Falsifiserbart: den redigerte teksten er
dokumentert modernisert/renset; en trofast transkripsjon ville ikke hatt de to
siste komponentene.

## Alternativer vurdert

- **Bruke 25,2 % som «CER»** — avvist: måler tre ting samtidig.
- **Blindfasit** — valgt (ADR-002): 21,3 % mot rå OCR.

## Konsekvenser

Motiverte den kostbare blindtranskripsjonen. Illustrerer en fristende
metodefeil: å bruke en tekst som *finnes* i stedet for den som *måtte skrives*.
