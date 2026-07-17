# ADR-005 — Regelen «-ede → -et + konsonantdobling» forkastet

Status: forkastet
Dato: 2026-07-16
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

En regelbasert modernisering av verbendelser ble vurdert for å redusere
mengden uavklarte former automatisk: «-ede → -et med konsonantdobling».

## Beslutning

Forkast regelen som automatisk modernisering.

## Begrunnelse (falsifiserbar)

Regelen ga betydningsendrende feil på et verifiseringssett:

- *rede → rett*
- *lede → lett*
- *træde → trett*

3 feil av 42 rader = **7 % feilrate**. En moderniseringsregel som endrer
betydning i 7 % av tilfellene kan ikke kjøres blindt. Falsifiserbart:
feilraten er målt på et konkret sett.

## Alternativer vurdert

- **Kjøre regelen med manuell etterkontroll** — avvist: kontrollen er like
  stor jobb som å avgjøre hver form for hånd.
- **Bare belagte moderniseringer** — valgt: hver form må være belagt i den
  verifiserte teksten.

## Konsekvenser

Ingen regelbasert modernisering kjøres uten belegg. Uavklarte former står.
