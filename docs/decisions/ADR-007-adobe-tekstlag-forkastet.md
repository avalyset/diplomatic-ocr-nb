# ADR-007 — Adobe tekstlag (metode D) forkastet

Status: forkastet
Dato: 2026-07-17
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

Om skann-PDF-ene allerede hadde et brukbart tekstlag, ville «midten» av
materialet være lest, og jobben copy-paste, ikke OCR. Verdt å måle før mer
vision-kjøring.

## Beslutning

Forkast metode D. Den er verken målbar mot fasiten eller trofast der den
finnes.

## Begrunnelse (falsifiserbar)

- **Scan1, Scan2, Scan4** («Adobe Scan for iOS»): **0 tegn** tekstlag. De åtte
  fasitsidene er alle Scan4 → D kan ikke måles mot fasiten i det hele tatt.
- **Scan3** («Acrobat Paper Capture», 1925–27): har tekstlag, men **ö = 0,
  ø = 112**. Adobe har normalisert ö→ø — nøyaktig den stille moderniseringen
  metode B ikke gjør. Diskvalifisert uansett hvor lav en CER måtte være.

Falsifiserbart: tegntellingen ö/ø i Scan3s tekstlag er reproduserbar; et
tekstlag med ö > 0 ville motbevist normaliseringen.

## Alternativer vurdert

- **Bruke Scan3s tekstlag for 1925–27** — avvist: ö er utradert; å gi ut det
  ville publisert Adobes modernisering som kilde.
- **Copy-paste der tekstlag finnes** — avvist: finnes bare på 1 av 4 skann,
  og det er korrupt.

## Konsekvenser

«Midten» er ikke allerede lest. Metode B (vision) står som eneste metode som
både er nøyaktig og bevarer ortografien (ADR-008).
