# ADR-008 — Metodevalg: B (vision) for lesning av materialet

Status: akseptert
Dato: 2026-07-17
Retrospektiv: ja

> Retrospektiv. Beslutningen ble tatt før dette dokumentet.

## Kontekst

Etter at A (ADR-006) og D (ADR-007) falt, sto to metoder igjen: baseline
tesseract og B (`claude-opus-4-8` vision). Materialet skal leses trofast, med
ö og arkaisk ortografi intakt.

## Beslutning

Bruk **metode B** til å lese materialet. Baseline beholdes som referanse.

## Begrunnelse (falsifiserbar)

| metode | CER | ö/ø (B) |
|--|--|--|
| baseline | 21,3 % (KI 14,7–28,1) | — |
| **B** | **5,35 %** (KI 3,0–8,0) | ö = 71, ø = 0 |

B har lavere CER enn baseline med god margin (ikke-overlappende KI), og
bevarer ö (71/0), efter, skulde, nu (`results/troskap.tsv`).

**To eksplisitte forbehold:**

1. *Dom mot 5 %-terskelen er uavgjort.* Punktestimat 5,35 % bommer på
   terskelen; KI inkluderer 5 %. Rapporteres som uavgjort, ikke bestått. Ingen
   post-hoc utvidelse av n.
2. *Ingen kontrollarm.* Om prompten forårsaket troskapen, eller om modellen
   ville vært trofast uansett, er ikke målt. Ingen kausal påstand.

Nøkkelen leses fra miljøvariabel (`ANTHROPIC_API_KEY`, standardnavnet SDK-en
bruker), aldri hardkodet, aldri i repoet (`src/vision_ocr.py`).

## Alternativer vurdert

- **Baseline tesseract** — brukbar nødløsning (21,3 %), men firedobler
  feilraten og understøtter ikke ö like godt.
- **Manuell transkripsjon** — gullstandard, men skalerer ikke til 237+ sider.

## Konsekvenser

Materialet leses med B. Utgivelsesbeslutning per periode må ta høyde for det
uavgjorte terskelutfallet. Bidraget til metodelitteraturen er
måleprotokollen, ikke modellvalget (som er foreldet innen året).
