# ADR-010 — Produksjonskjøring av metode B på det uvaliderte korpuset

Status: akseptert
Dato: 2026-07-18
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

Metode B (vision, `claude-opus-4-8`) ga 5,35 % CER målt mot blindfasiten —
men fasiten er trukket fra **Scan4** alene (1928–1936). Materialet som skulle
leses, «midten» (22.10.1921 → 9.02.1930), ligger i Scan2 og Scan3, som er
eldre og kan være annen skrivemaskin eller tilstand. Kvaliteten der var
**uvalidert**. Det finnes ingen blindfasit for midten.

## Beslutning

Kjør metode B **uendret** på hele midten, etter en pilot først. Bruk
kvalitetsport på det som kan måles uten fasit (ö/ø-rate, arkaisk
bevaringsratio, tegn/side, datokronologi), ikke CER.

## Begrunnelse (falsifiserbar, med tall)

**Pilot (8 sider, Scan2/Scan3, `random.seed(1933)`):** ö = 80, ø = 0. Alle
sider 1497–1775 tegn, `stop=end_turn`, datoer innenfor forventet spenn. Åtte
sider kan være flaks.

**Produksjon (114 sider: Scan2 p24–73, Scan3 p1–23, Scan4 p1–41):**

- **Troskap: ö = 1081, ø = 5 — ø-andel 0,46 %.** Hundre sider er ikke flaks.
  Troskapen er en egenskap ved metoden på dette korpuset, ikke et tilfelle.
- Arkaiske former bevart: efter 57, nu 114, skulde 94, sig 220, mig 139.
- Tegn/side: median 1666. Tre sider under 1000 — alle er ekte korte/blanke
  sider (bekreftet mot uavhengig sidetelling), ingen uleste sider.
- Datokronologi monoton i sidefølge, ett trivielt 2-dagers avvik (én
  datolinje lest 23. mot 25. okt. 1927). Spenn 22.10.1921 → 9.02.1930.

Falsifiserbart: kjør samme metode på de samme sidene og tell ø. Stiger
ø-andelen vesentlig over 0,46 %, faller påstanden.

**Metoden ble holdt uendret** — samme prompt ordrett, samme modell, farge
(`pdftoppm -r 400 -png`, ikke gråtone), samme 1568 px / kvalitet 92, ett
ferskt kall per bilde. Enhver endring av prompt eller rendering ville gjort
5,35 %-målingen ugyldig som referanse for produksjonen. Gråtone ble derfor
avvist (piloten validerte farge), og nøkkelen leses fra standard
miljøvariabel.

## Alternativer vurdert

- **Justere prompten for Scan2/3** — avvist: ville løsrevet produksjonen fra
  den målte 5,35 %-referansen.
- **Gråtone-rendering** (opprinnelig spesifisert) — avvist: piloten og
  blindtesten kjørte farge; gråtone er et uvalidert avvik.
- **Kutte startsiden på instruert side** — avvist: den første hull-innførselen
  (9. nov. 1921) spenner tre sider, og en for sen start ville kuttet den. Se
  under.

## Konsekvenser

Midten er lest. To eksplisitte forbehold:

1. **Ingen CER for produksjonen.** Uten blindfasit for Scan2/3/4-midten er
   5,35 % fortsatt et Scan4-spesifikt tall. Kvalitetsporten måler troskap og
   lesbarhet, ikke tegnfeilrate. Å hevde 5,35 % for midten ville vært å
   overføre et tall utenfor sitt målegrunnlag.
2. **Fem ø.** 0,46 % er lavt, men ikke null. De fem ø-ene ligger på fire
   sider og er kandidater for samme overkorrigering som ADR-008 beskriver —
   verdt å kontrollere mot bildet, ikke å bortforklare.

**Startgrense:** kjøringen ble utvidet bakover til første rene
innførselsåpning (22.10.1921) for å fange den første hull-innførselen hel.
Overlappen mot den allerede utgitte 1920–1922-teksten trimmes ved redigering;
et selvpåført hull ville ikke kunne repareres.

Produksjonsteksten er bokmanus og ligger forseglet utenfor dette repoet. Her
står bare metodebeslutningen og aggregattallene — ingen kildetekst.
