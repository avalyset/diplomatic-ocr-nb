# Notat — Tang, Cap, Pettersson & Nivre (2018), *An Evaluation of Neural Machine Translation Models on Historical Spelling Normalization*

**Notatversjon:** v1.0 · **Dato:** 2026-07-28 · **Forankrer:** modernisering av historisk ortografi med nevrale modeller er etablert
**PDF:** `TANG-2018-NMT-HistoricalSpellingNormalization.pdf` (arXiv-versjon)

## 1. Verifiserte bibliografiske data (fra dokumentet)

- **Tittel:** «An Evaluation of Neural Machine Translation Models on Historical Spelling Normalization»
- **Forfattere:** Gongbo Tang, Fabienne Cap, Eva Pettersson, Joakim Nivre — Uppsala University
- **Dokumentets identitet:** arXiv:1806.05210v2 [cs.CL], 4 Aug 2018 · Lisens: CC-BY 4.0 (trykt s. 1)
- **Venue:** *står ikke på arXiv-dokumentet.* Verifisert mot ACL Anthology: *Proceedings of the 27th International Conference on Computational Linguistics* (**COLING 2018**), Santa Fe — anthology-id **C18-1112**.

**Avvik fra oppgitt data:** oppgitt som «NMT on Historical Spelling Normalization» uten forfatter. Verket er **ikke anonymt**; forfatterne er navngitt (Tang, Cap, Pettersson, Nivre). Tilføyd venue COLING 2018.

## 2. Passasjer som bærer påstanden (ordrett, s. 1)

Abstract:
> «In this paper, we apply different NMT models to the problem of historical spelling normalization for five languages: English, German, Hungarian, Icelandic, and Swedish. … Our results show that NMT models are much better than SMT models in terms of character error rate.»

Innledning (at feltet er etablert, med tidligere arbeid):
> «Spelling normalization is the task of mapping a historical spelling to its modern spelling. It is usually used as a preprocessing step before feeding the historical text into modern NLP tools (Pettersson et al., 2013b; Bollmann, 2013; Sánchez-Martínez et al., 2013) …»
> «There are some papers in which neural machine translation (NMT) models are employed for the spelling normalization task. Korchagina (2017) utilizes a character-level NMT model for medieval German texts. Bollmann et al. (2017) apply an attention-based NMT model to historical German texts.»

## 3. Hva kilden IKKE sier

- Oppgaven er **normalisering** (historisk → moderne staving), evaluert med CER mot en normalisert fasit — retningen er **motsatt** av en diplomatarisk kildeutgave, som *bevarer* de historiske formene. Kilden belegger at nevral modernisering finnes og virker, ikke at bevaring er løst.
- Krever **annotert treningsdata** (historisk–moderne par); den svenske/islandske dekningen sier ingenting om norsk riksmål med ö.
- Ingen berøring med apparat, QE eller sikkerhetsfiltre.
