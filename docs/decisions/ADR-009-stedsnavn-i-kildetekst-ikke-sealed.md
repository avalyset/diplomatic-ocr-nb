# ADR-009 — Stedsnavn i kildetekst er ikke sealed materiale; fasiten redigeres ikke

Status: akseptert
Dato: 2026-07-17
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

Repoet har en kompartmentaliseringsgrense: enkelte tema (patentspor,
redaksjonshistoriske hypoteser om en senere utgave, m.m.) skal aldri inn — i
verken arbeidstre eller historikk. En mekanisk «port» (git-grep før push)
håndhever grensen.

Ved bygging tripset porten på strengen «Törtberg» i `data/fasit_n8.json`
(side p084): «…ruvende på toppen av Törtberg.» Dette er stedsnavnet i Oslo, i
Aars' egen dagbokprosa — én av de åtte fasitsidene.

## Beslutning

1. **Stedsnavn og annet innhold i selve kildeteksten er ikke sealed
   materiale.** Det som er sealed, er tese-prosa og patentspor *om* materialet
   — ikke ord som forekommer i materialet.
2. **Fasiten redigeres ikke.** `data/fasit_n8.json` beholdes bit for bit slik
   den ble blindtranskribert.
3. Porten omskrives til å treffe tese-/patenttermer som bare finnes i
   prosa *om* utgaven, aldri i kildeteksten. Stedsnavnet fjernes fra
   grep-lista.

## Begrunnelse (falsifiserbar)

Fasiten er **målegrunnlaget**. Alle CER/WER-tall er Levenshtein mot nøyaktig
denne strengen. En redigert fasit gir andre tall enn de rapporterte:
baseline ville ikke lenger reprodusere 0.21317518833146337, og
integritetssjekken i `gen_results` ville feile. Å maskere «Törtberg» ville
altså ugyldiggjøre hele resultatkjeden for å skjule et offentlig stedsnavn.

Falsifiserbart: endre ett tegn i `data/fasit_n8.json` og kjør
`src/measure_cer.py` på baseline — tallet flytter seg, og reproduksjonen
mot `results/aggregat.json` bryter.

## Alternativer vurdert

- **Maskere «Törtberg» i repo-kopien** — avvist: bryter CER-reproduserbarheten
  (publisert fasit ≠ målt fasit) for å skjule et offentlig stedsnavn.
- **Holde fasiten helt ute** — avvist: fasit-transkripsjonen er nettopp det
  publiserbare artefaktet, uavhengig av sidebildene.

## Konsekvenser

Porten skiller nå mellom *innhold i kilden* (tillatt) og *prosa om kilden*
(sealed). Grep-lista treffer nøkkel-/patent-/tesetermer, ikke stedsnavn.
Sidebildene forblir utenfor repoet til avklaring med institusjonen.
