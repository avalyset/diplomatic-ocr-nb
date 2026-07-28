# Notat — Tekgürler (2025), *LLMs for Translation: Historical, Low-Resourced Languages and Contemporary AI Models*

**Notatversjon:** v1.0 · **Dato:** 2026-07-28 · **Forankrer:** sikkerhetsfiltre gir utransklaterte partier i historiske manuskripter
**Funnet i:** Del B-søk (ikke på den opprinnelige Del A-lista) — men forankrer en Del A-påstand direkte.
**PDF:** `TEKGURLER-2025-LLM-HistoricalTranslation.pdf` (arXiv-versjon)

## 1. Verifiserte bibliografiske data (fra dokumentet)

- **Tittel:** «LLMs for Translation: Historical, Low-Resourced Languages and Contemporary AI Models»
- **Forfatter:** Merve Tekgürler — Stanford University, Department of History and Program in Symbolic Systems
- **Dokumentets identitet:** arXiv:2503.11898v1 [cs.CL], 14 Mar 2025
- **Venue / DOI:** ingen publisert venue trykt på dokumentet (arXiv-preprint per marsmerkingen).

**Avvik fra oppgitt data:** kilden var **ikke** på Del A-lista; den ble funnet i Del B-søket på sikkerhetsfilter-påstanden. Den fyller det som ellers ville vært et negativt funn.

## 2. Passasjen som bærer påstanden (ordrett, s. 1, Abstract)

> «This paper examines Gemini's performance in translating an 18th-century Ottoman Turkish manuscript, *Prisoner of the Infidels: The Memoirs of Osman Agha of Timisoara*, into English. The manuscript recounts the experiences of Osman Agha … and includes his accounts of warfare and violence. **Our analysis reveals that Gemini's safety mechanisms flagged between 14% and 23% of the manuscript as harmful, resulting in untranslated passages. These safety settings, while effective in mitigating potential harm, hinder the model's ability to provide complete and accurate translations of historical texts.**»

Dette er et direkte, tallfestet belegg for at innholdsfiltre etterlater **hull i historiske manuskripter** — parallelt til avslags-/refusjonssidene i Vigeland-korpuset (part3_s011, part4_s002, part4_s014), der modellen nektet og etterlot tomrom.

## 3. Hva kilden IKKE sier

- Gjelder **interlingval** oversettelse (osmansk-tyrkisk → engelsk) med **Gemini**, ikke OCR/transkripsjon og ikke vår modell eller vårt språk. Mekanismen (sikkerhetsfilter → utelatt parti) er den samme; tallene 14–23 % er spesifikke for denne teksten og modellen.
- Ett manuskript, én modell — ikke en systematisk kartlegging av hvor ofte filtre slår inn på historisk materiale.
- Sier ingenting om ö/ø, apparat eller QE. Verdien er belegg for **fenomenet**, ikke en rate vi kan overføre.
