# Notat — Agrawal, Mehandru, Salehi & Carpuat (2022), *Quality Estimation via Backtranslation at the WMT 2022 Quality Estimation Task*

**Notatversjon:** v1.0 · **Dato:** 2026-07-28 · **Forankrer:** referansefri QE er etablert · RTT/BLEU svak, embeddinger brukbar (korroborerende, med nyanse)
**PDF:** `AGRAWAL-2022-QE-Backtranslation.pdf`

## 1. Verifiserte bibliografiske data (fra dokumentet)

- **Tittel:** «Quality Estimation via Backtranslation at the WMT 2022 Quality Estimation Task»
- **Forfattere (s. 1, «* equal contribution»):** Sweta Agrawal (University of Maryland), Nikita Mehandru (UC Berkeley), Niloufar Salehi (UC Berkeley), Marine Carpuat (University of Maryland)
- **Venue:** *Proceedings of the Seventh Conference on Machine Translation* (WMT 2022) — ACL Anthology **2022.wmt-1.54**; også speilet på statmt.org
- **Sidetall / DOI:** eksakt sidespenn står ikke på den hentede PDF-ens s. 1; anthology-posten (2022.wmt-1.54) er autoritativ.

**Avvik fra oppgitt data:** ingen — «WMT 2022: Quality Estimation via Backtranslation (statmt.org)» stemmer. Forfatterne var ikke oppgitt; tilføyd.

## 2. Passasjer som bærer påstanden (ordrett, s. 1)

Abstract:
> «We find that even the best-performing backtranslation-based scores perform substantially worse than supervised QE systems, including the organizers' baseline. However, combining backtranslation-based metrics with off-the-shelf QE scorers improves correlation with human judgments, suggesting that they can indeed complement a supervised QE system.»

Innledning (om RTT/BLEU-historikken og Moon 2020):
> «In early rule-based and statistical MT systems, Somers (2005) shows that, when using automatic evaluation methods (e.g., BLEU), backtranslation cannot discriminate good MT systems from bad ones … This led him to conclude that "round trip translation [is] good for nothing". Recently, Moon et al. (2020) revisited the use of backtranslation for QE with neural systems for MT and with embedding-based similarity metrics to enable a more sophisticated comparison of the backtranslation with the source. They obtained strong results on the WMT 2019 QE task, outperforming the YISI-2 metric (Lo, 2019) on system-level evaluations, but exhibited rather low correlations on the segment-level task …»

## 3. Hva kilden IKKE sier

- **Modererer Moon (2020):** selv embedding-basert bakoversettelse er «substantially worse than supervised QE» **alene** — den *komplementerer* et veiledet QE-system, den erstatter det ikke. Moons sterke resultat var **systemnivå**; på segmentnivå var korrelasjonen lav.
- Bekrefter at referansefri QE er et etablert felt (delt oppgave, veiledede QE-systemer, arrangørens baseline), men understreker at RTT/BT ikke er state-of-the-art i seg selv.
- Ingen kobling til historisk tekst, diplomatarisk troskap eller apparat; MT-QE mellom språk, ikke intralingval kildeetablering.
