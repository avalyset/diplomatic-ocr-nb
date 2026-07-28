# Notat — Kocmi & Federmann (2023), *GEMBA-MQM: Detecting Translation Quality Error Spans with GPT-4*

**Notatversjon:** v1.0 · **Dato:** 2026-07-28 · **Forankrer:** referansefri QE er etablert (LLM-basert)
**PDF:** `KOCMI-2023-GEMBA-MQM.pdf`

## 1. Verifiserte bibliografiske data (fra dokumentet)

- **Tittel (tittelside):** «GEMBA-MQM: Detecting Translation Quality Error Spans with GPT-4»
- **Forfattere:** Tom Kocmi og Christian Federmann — Microsoft, Redmond
- **Venue / sidetall (trykt i bunn av s. 1):** «Proceedings of the Eighth Conference on Machine Translation (WMT), pages **768–775**, December 6–7, 2023. ©2023 Association for Computational Linguistics.» ACL Anthology **2023.wmt-1.64**.

**Avvik fra oppgitt data:** ingen — «WMT 2023, s. 768–775, Kocmi & Federmann — GEMBA-MQM» stemmer eksakt.

## 2. Passasjer som bærer påstanden (ordrett, s. 1, Abstract)

> «This paper introduces GEMBA-MQM, a GPT-based evaluation metric designed to detect translation quality errors, specifically for the quality estimation setting **without the need for human reference translations**. Based on the power of large language models (LLM), GEMBA-MQM employs a fixed three-shot prompting technique, querying the GPT-4 model to mark error quality spans.»

> «While preliminary results indicate that GEMBA-MQM achieves state-of-the-art accuracy for system ranking, we advise caution when using it in academic works to demonstrate improvements over other methods due to its dependence on the proprietary, black-box GPT model.»

## 3. Hva kilden IKKE sier

- Referansefri, men **ikke RTT/bakoversettelse** — dette er promptbasert feilspenn-deteksjon med GPT-4, en annen mekanisme.
- «State-of-the-art» gjelder **systemnivå-rangering** (WMT23 Metrics-oppgaven); forfatterne fraråder selv å bruke tallene til å påstå forbedring over andre metoder pga. den lukkede modellen.
- Ingen berøring med historisk tekst, intralingval oversettelse eller apparat. Relevansen for vårt spor er at referansefri kvalitetsvurdering er et bredt, aktivt felt — ikke at GEMBA gjelder kildeutgaver.
