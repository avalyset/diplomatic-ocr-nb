# ADR-012 — ISBN-sjekksiffer for Aars bind II omgått: regelen fantes, men tallet ble antatt verifisert

Status: erkjent (feil bekreftet, retting ikke utført)
Dato: 2026-07-29
Retrospektiv: ja

> Retrospektiv. Feilen ble innført tidligere; dette dokumentet registrerer
> funnet og omfanget, og forklarer hvorfor kontrollen ble omgått. Selve
> rettingen er ikke gjort ennå (omfanget skulle ses først).

## Kontekst

ISBN-13 for Aars bind II (*Dagbok om Gustav Vigeland 1922–1930*) er registrert
som **978-82-694238-7-8**. Sjekksifferet er ugyldig.

Kontrollsifferet regnet i kode (vekt 1/3, `(10 − sum mod 10) mod 10`):

```
prefiks 978-82-694238-7-  →  978826942387
9·1 + 7·3 + 8·1 + 8·3 + 2·1 + 6·3 + 9·1 + 4·3 + 2·1 + 3·3 + 8·1 + 7·3 = 133
kontroll = (10 − 133 mod 10) mod 10 = (10 − 3) mod 10 = 7
```

Korrekt ISBN er **978-82-694238-7-7** (uten bindestreker `9788269423877`).
De tre andre bindene i serien er gyldige (Erindringer …6-0, bind I …8-4,
bind III …9-1 — alle bekreftet i kode).

Prosjektregelen fantes allerede, ordrett i `UTGIVELSER-prosjekt.md`:

> **Sjekksiffer regnes alltid, aldri gjettes.**

Regelen ble likevel omgått. To skjerpende funn:

1. Samme linje som siterer regelen oppgir en «uten bindestreker»-form
   `9788269423778`. Den har *gyldig* sjekksiffer, men er et **annet nummer**
   enn det korrekte (sifferombytting i publikasjons-/kontrollområdet). En form
   som passerer en naiv «ser gyldig ut»-test kan altså fremdeles være feil bok.
2. Den kanoniske uten-bindestrek-formen av den gale ISBN-en (`9788269423878`)
   finnes ingen steder — bare den bindestreksatte `978-82-694238-7-8` og den
   valid-men-feil `9788269423778`. Feilen er altså spredt i to ulike gale
   former, ikke én.

## Hvorfor kontrollen ble omgått

Tallet **978-82-694238-7-8 var selv en tidligere rettelse**. Fordi det hadde
vært «rettet», ble det behandlet som allerede verifisert, og sjekksifferet ble
ikke regnet på nytt på den rettede verdien. Regelen «regn alltid» ble i
praksis lest som «regn ved førstegangsføring» — ikke «regn på hver verdi som
faktisk skal brukes, også rettelser». En rettelse er en ny verdi og må gjennom
samme kontroll som en førstegangsverdi; det var akkurat dette steget som falt
bort. Verdien forplantet seg deretter uendret til kolofon, byggemetadata,
sitering og levering, fordi ingen av de nedstrøms kopiene regnet sjekksifferet
selv.

## Beslutning

1. Behandle **enhver** ISBN-verdi som uverifisert til sjekksifferet er regnet i
   kode på nøyaktig den verdien som skal brukes — også når verdien er en
   rettelse eller er «arvet» fra en kilde som antas korrekt.
2. «Tidligere rettet» gir **ikke** verifisert-status. Provenienstillit
   erstatter ikke beregning.
3. Ingen visuell/«ser riktig ut»-godkjenning: `9788269423778` demonstrerer at
   et gyldig sjekksiffer ikke er bevis for riktig nummer.

Retting av de faktiske forekomstene er ikke en del av denne ADR-en; omfanget
(under) skulle ses før noe endres.

## Omfang (forekomster av det gale ISBN-et, ikke rettet)

Prosjektdokumenter (Vault):
- `Utgivelser/UTGIVELSER-prosjekt.md:43` — `978-82-694238-7-8` (bindtabell)
- `Utgivelser/UTGIVELSER-prosjekt.md:57` — `978-82-694238-7-8` **og**
  `9788269423778` (samme linje som siterer regelen)

Sitering / OCR-repo:
- `diplomatic-ocr-nb/CITATION.cff:45` — `978-82-694238-7-8`

Byggeskript/-metadata for bind II (`Vault/Aars_ocr2/midten_build/`):
- `midten_epub.md:21` — `ISBN 978-82-694238-7-8`
- `metadata.yaml:8` — `text: 978-82-694238-7-8`
- `metadata_sample.yaml:8` — `text: 978-82-694238-7-8`
- `midten_sample.md:21` — `ISBN 978-82-694238-7-8`

EPUB-kilder (6 kopier; hver med treff i `content.opf`, `toc.ncx`,
`text/ch001.xhtml`-kolofon):
- `Vault/Aars_ocr2/midten_build/Dagbok_om_Gustav_Vigeland_1922-1930.epub` (+ `_SAMPLE`)
- `Vault/Utgivelser/aars-dagbok/bind2_1922-1930/…1922-1930.epub` (+ `_SAMPLE`)
- `Desktop/Master Dok./Aars/…1922-1930.epub` (+ `_SAMPLE`)

Leveringsfil:
- `Desktop/levering/AARS-BIND2-PLIKTAVLEVERING-v1.0-2026-07-29.pdf` — gal ISBN
  gjengitt i kolofonen (arvet fra EPUB-en ved konvertering)

Rene (kontrollert, ingen forekomst): `METODE.md`,
`vigeland-memoarer/analyse/PREREGISTRATION-v1.0-2026-07-29.md`, og
`vigeland-memoarer` for øvrig (kun Erindringers gyldige …6-0).

## Alternativer vurdert

- **Rette kun kolofon/levering, la byggekilden stå** — avvist: kilden ville
  regenerert feilen ved neste bygg.
- **Stole på at «rettet» = riktig** — dette *var* feilmekanismen; avvist.
- **Automatisk sjekksiffer-gate i bygg og CI** — anbefalt oppfølging (egen
  sak): en test som regner sjekksiffer for hver ISBN i metadata/kolofon og
  feiler bygget ved avvik. Ville fanget både `…7-8` og den valid-men-feil
  `9788269423778`? Den siste passerer sjekksiffer, så gaten må dessuten
  sammenligne mot én kanonisk kilde per bind, ikke bare validere isolert.

## Konsekvenser

- Bind II må omregistreres til **978-82-694238-7-7** overalt før avlevering og
  publisering; leveringens PDF og alle EPUB-kilder må bygges på nytt.
- En ISBN som allerede er «i omløp» (levert, sitert, bygget) kan være ugyldig;
  proveniens («det ble rettet før») er ikke bevis. Hver verdi regnes i kode på
  brukstidspunktet.
- Den valid-men-feil formen `9788269423778` viser at sjekksiffer-validering
  alene er utilstrekkelig; kanonisk kilde per bind trengs i tillegg.
