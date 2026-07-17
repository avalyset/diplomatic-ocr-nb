# ADR-004 — difflib-strengmatch som ordforslag forkastet

Status: forkastet
Dato: 2026-07-16
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

For å foreslå rettelser av OCR-former ble likhet mot en ordliste (fra en
verifisert tekst) vurdert, målt med `difflib.SequenceMatcher.ratio()`.

## Beslutning

Forkast tegnavstand/strenglikhet som mekanisme for ordforslag.

## Begrunnelse (falsifiserbar)

Høy strenglikhet ga betydningsendrende forslag:

- *björnegruppen → barnegruppen* (ratio 0,88)
- *ensartede → entartede* (ratio 0,889)

Tegnavstand måler ortografisk nærhet, ikke betydning. Et forslag med ratio
0,88 kan bytte ut et ord med et helt annet. Falsifiserbart: eksemplene over er
konkrete, reproduserbare motbevis.

## Alternativer vurdert

- **difflib-terskel høyere enn 0,88** — avvist: motbevisene ligger allerede
  på 0,88–0,89; å heve terskelen dropper også ekte treff.
- **Belegg i den redigerte teksten (ja/nei)** — valgt i stedet: en form
  aksepteres bare om den er belagt, ikke gjettet fra likhet.

## Konsekvenser

Ordforslag må hvile på belegg, ikke strengavstand. Uavklarte former står som
uavklarte.
