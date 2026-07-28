# Notat — Sindhujan, Kanojia & Orăsan (2025), *Reference-Less Evaluation of Machine Translation: Navigating Through the Resource-Scarce Scenarios*

**Notatversjon:** v1.1 · **Dato:** 2026-07-28 · **Forankrer:** referansefri QE er et etablert felt, ikke et hull
**PDF:** `SINDHUJAN-2025-REFERENCE-LESS-QE.pdf`

**Endret i v1.1:** PDF-en er nå hentet (lå på skrivebordet, md5-verifisert kopi) — forbeholdet om teknisk utilgjengelighet er fjernet. Bibliografiske data er nå verifisert **fra dokumentets s. 1**, ikke fra Crossref. Lagt til: temanummer-argumentet (styrker påstand 1) og de faktiske QE-systemene til portvalget.

## 1. Verifiserte bibliografiske data (fra dokumentets s. 1)

- **Tittel:** «Reference-Less Evaluation of Machine Translation: Navigating Through the Resource-Scarce Scenarios» (type: *Article*)
- **Forfattere med affiliasjon (trykt s. 1):**
  - Archchana Sindhujan ¹,² — ¹ Surrey Institute for People-Centred AI (PAI), Guildford GU2 7XH, UK; ² Department of Computer Science and Electronic Engineering, University of Surrey, Guildford GU2 7JN, UK
  - Diptesh Kanojia ¹,² — samme to
  - Constantin Orăsan ³,\* — ³ Centre for Translation Studies, University of Surrey, Guildford GU2 7XH, UK · korrespondanse: c.orasan@surrey.ac.uk
- **Tidsskrift:** *Information* **2025, 16, 916** (vol. 16, nr. 10, artikkel 916)
- **DOI:** 10.3390/info16100916 · **Lisens:** CC BY 4.0 · Academic Editor: Marjan Mernik
- **Datoer (s. 1):** mottatt 29 Aug 2025, revidert 3 Oct 2025, akseptert 5 Oct 2025, **publisert 18 Oct 2025**

**Avvik fra kjent/oppgitt data:** ingen. «Sindhujan, Kanojia, Orăsan (University of Surrey) · Information 2025, 16(10), 916 · doi:10.3390/info16100916 · publisert 18.10.2025» bekreftes i sin helhet mot dokumentet. Alle tre er University of Surrey (PAI + informatikk for de to første, Centre for Translation Studies for Orăsan).
- **Temanummer** «Machine Translation Quality Estimation — Advances and Emerging Challenges»: **står ikke i selve PDF-en** (verifiserbart kun på tidsskriftets utgavesider, som MDPI blokkerer for automatisert henting). Ført som oppgitt, men flagget som ikke-dokumentbekreftet.

## 2. Passasjer som bærer påstanden (ordrett, s. 1, Abstract)

> «Reference-less evaluation of machine translation, or Quality Estimation (QE), is vital for low-resource language pairs where high-quality references are often unavailable. In this study, we investigate segment-level QE methods comparing encoder-based models such as MonoTransQuest, CometKiwi, and xCOMET with various decoder-based methods (Tower+, ALOPE, and other instruction-fine-tuned language models).»

> «Results indicate that while fine-tuned encoder-based models remain strong performers across most low-resource language pairs, decoder-based Large Language Models (LLMs) show clear improvements when adapted through instruction tuning. Importantly, the ALOPE framework further enhances LLM performance beyond standard fine-tuning, demonstrating its effectiveness in narrowing the gap with encoder-based approaches …»

**Temanummer-argumentet:** artikkelen inngår i et temanummer viet nettopp QE-forskning. Et *helt temanummer* om referansefri kvalitetsvurdering i 2025 er sterkere belegg for at feltet er etablert enn én enkelt artikkel — det gjør påstand 1 i samlerapporten uangripelig: referansefri QE er ikke et hull, det er et felt med egne temanumre, delte oppgaver (WMT QE) og et modent systemlandskap.

## 3. Til portvalget — hvilke systemer, og hva som vinner

- **Sammenlignede QE-systemer:** encoder-baserte **MonoTransQuest, CometKiwi, xCOMET** mot decoder-baserte **Tower+, ALOPE** og andre instruksjons-finjusterte LLM-er. Åtte lavressurs-språkpar (engelsk på kilde- eller målsiden).
- **Best på lavressurs-par:** **finjusterte encoder-baserte modeller** (CometKiwi/xCOMET/MonoTransQuest-klassen) er de robuste vinnerne; ALOPE-rammeverket smalner gapet for LLM-baserte QE, men slår dem ikke gjennomgående.
- **Relevans for oss:** i ressursknappe scenarioer (som vårt: ingen fasit) er referansefrie, *finjusterte encoder-baserte* QE-metoder det litteraturen peker på som mest pålitelige. Vår egen tilnærming bruker **deterministiske porter** (ö/ø, ordantall, garble), ikke en lært QE-modell — koblingen er analog (referansefri kvalitetsvokting finnes og er kartlagt), ikke en direkte adopsjon.

## 4. Hva kilden IKKE sier

- Gjelder **MT mellom språk for lavressurs-par**, ikke intralingval modernisering eller diplomatarisk troskap.
- Sier ingenting om historisk tekst, apparat, lakuner eller ö/ø-troskap.
- Overføringen fra «QE uten referanse for lavressurs-MT» til «vokte en kildeutgave uten fasit» er vår analogi, ikke kildens påstand.
