# Notat — Moon, Cho & Park (2020), *Revisiting Round-Trip Translation for Quality Estimation*

**Notatversjon:** v1.0 · **Dato:** 2026-07-28 · **Forankrer:** referansefri QE er etablert · RTT med BLEU svak, med semantiske embeddinger brukbar
**PDF:** `MOON-2020-RTT-QualityEstimation.pdf` (arXiv-versjon)

## 1. Verifiserte bibliografiske data (fra dokumentet)

- **Tittel (fra tittelsiden):** «Revisiting Round-Trip Translation for Quality Estimation»
- **Forfattere:** Jihyung Moon, Hyunchang Cho, Eunjeong L. Park — alle Naver Papago
- **Dokumentets identitet:** arXiv:2004.13937v1 [cs.CL], 29 Apr 2020
- **Lisens (trykt på s. 1):** «© 2020 The authors. This article is licensed under a Creative Commons 3.0 licence, no derivative works, attribution, CC-BY-ND.»
- **Venue / sidetall / DOI:** *står ikke på arXiv-dokumentet.* Verifisert mot ACL Anthology (autoritativt register): publisert i *Proceedings of the 22nd Annual Conference of the European Association for Machine Translation* (EAMT 2020), Lisboa, **s. 91–104**, anthology-id **2020.eamt-1.11**.

**Avvik fra oppgitt data:** ingen — «arXiv:2004.13937 / Moon, Cho, Park» stemmer. Tilføyd: publisert venue (EAMT 2020), som ikke fremgår av preprintet.

## 2. Passasjer som bærer påstanden (ordrett, s. 1, Abstract)

> «Quality estimation (QE) is the task of automatically evaluating the quality of translations without human-translated references.»

> «Calculating BLEU between the input sentence and round-trip translation (RTT) was once considered as a metric for QE, however, it was found to be a poor predictor of translation quality. Recently, various pretrained language models have made breakthroughs in NLP tasks by providing semantically meaningful word and sentence embeddings. In this paper, we employ semantic embeddings to RTT-based QE. Our method achieves the highest correlations with human judgments, compared to previous WMT 2019 quality estimation metric task submissions.»

Tabell 1 (s. 1) tallfester forskjellen på ett WMT19-eksempel: RTT-**sentBLEU** rangert 1947/1997, mens RTT-**SBERT** rangert 1001/1997 og RTT-**BERTScore** 1033/1997 — semantiske embeddinger løfter RTT-QE fra bunnen til øvre halvdel.

## 3. Hva kilden IKKE sier

- Gjelder **setnings-/systemnivå MT-QE på WMT19**, ikke historisk tekst, ikke intralingval oversettelse, ikke apparat.
- Påstanden er relativ: «highest correlations *compared to previous WMT 2019 QE metric task submissions*» — ikke en absolutt påstand om at RTT-QE er beste QE-metode.
- Abstraktet noterer selv en svakhet: bakoveroversettelses-systemet «can be a drawback when using RTT» (avbøtes ved semantiske metrikker, men er ikke eliminert).
- Sier **ingenting** om at referansefri QE lar seg overføre til å vokte en diplomatarisk kildeutgave; koblingen til vårt bruk er analogi, ikke belegg.
