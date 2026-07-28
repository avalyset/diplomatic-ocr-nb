# Notat — Ataman, Birch, Habash, Federico, Koehn & Cho (2025), *Machine Translation in the Era of Large Language Models: A Survey of Historical and Emerging Problems*

**Notatversjon:** v1.1 · **Dato:** 2026-07-28 · **Rolle:** feltets naturlige «slik står det nå»-referanse og prøvestein for egne nyhetspåstander
**PDF:** `ATAMAN-2025-MT-LLM-SURVEY.pdf`

**Endret i v1.1:** PDF-en er nå hentet (lå på skrivebordet, md5-verifisert kopi) — teknisk-utilgjengelig-forbeholdet er fjernet. Bibliografi verifisert **fra dokumentets s. 1**. Nedgradert fra «bare kontekst» til referanse-/prøvesteinsrolle (se §2). Lagt til ordrett gjennomgang av §5 «Current and Emerging Problems» med det positive *og* det negative funnet (§3–4).

## 1. Verifiserte bibliografiske data (fra dokumentets s. 1)

- **Tittel:** «Machine Translation in the Era of Large Language Models: A Survey of Historical and Emerging Problems» (type: **Review**)
- **Forfattere med affiliasjon (trykt s. 1):**
  - Duygu Ataman ¹,\* — ¹ Department of Computer Science, New York University, New York, NY 10011, USA (korrespondanse: ataman@nyu.edu)
  - Alexandra Birch ² — ² School of Informatics, University of Edinburgh, EH8 9AB, UK
  - Nizar Habash ³ — ³ Department of Computer Science, New York University **Abu Dhabi**, UAE
  - Marcello Federico ⁴ — ⁴ **Amazon**, Madrid, Spain
  - Philipp Koehn ⁵ — ⁵ Department of Computer Science, **Johns Hopkins University**, Baltimore, MD, USA
  - Kyunghyun Cho ¹ — New York University
- **Tidsskrift:** *Information* **2025, 16, 723** (vol. 16, nr. 9, artikkel 723)
- **DOI:** 10.3390/info16090723 · **Lisens:** CC BY 4.0 · Academic Editor: Katsuhide Fujita
- **Datoer (s. 1):** mottatt 17 Jun 2025, revidert 20 Jul 2025, akseptert 21 Jul 2025, **publisert 25 Aug 2025**

**Avvik fra kjent/oppgitt data:** ingen. Forfatterrekke og affiliasjoner (NYU, Edinburgh, NYU Abu Dhabi, Amazon, Johns Hopkins) bekreftes; **Cho er også NYU** (affiliasjon 1, deler med Ataman). Type er *Review*.
- **Temanummer** «Human and Machine Translation — Recent Trends and Foundations»: **står ikke i selve PDF-en** (kun på tidsskriftets utgavesider, som MDPI blokkerer). Ført som oppgitt, flagget som ikke-dokumentbekreftet.

## 2. Hvorfor dette ikke bare er bakgrunn

Forfatterlista er feltets tyngste: **Philipp Koehn** (Moses-verktøykjeden og standardverket *Statistical Machine Translation*) og **Kyunghyun Cho** (encoder–decoder-arkitekturen som all nevral MT bygger på), sammen med Birch, Habash og Federico. En survey signert disse er derfor **den naturlige referansen for enhver «slik står feltet nå»-setning** — og prøvesteinen for egne nyhetspåstander: hvis noe *ikke* er nevnt blant deres «current and emerging problems», er det et sterkt signal om et faktisk hull, ikke et oversett hjørne.

## 3. Til det vi trenger — §5 «Current and Emerging Problems» (ordrett, med seksjon og side)

**§5.1 Applicability Across Languages (s. 16–17) — historiske/lavressursspråk:**
> «research has demonstrated a significant disparity in the performance of large language models (LLMs) between English and other languages [229]. While GPT-4 [127] approaches the performance of state-of-the-art fine-tuned models, it often fails to surpass them, particularly in languages that utilize non-Latin scripts and in low-resource languages.»

**§5.2 Evaluation (s. 17–18) — evaluering, herunder LLM-basert uten referansematching:**
> «A promising direction for evaluation involves leveraging LLMs to enhance translation assessment. Recent studies have proposed using LLMs to label translation errors [262], yet they currently lack the capability to consistently rank good vs. bad translations or sentences. Evaluating long-tail errors, which occur infrequently but may be critical in specific domains (e.g., named entity errors), presents another major challenge.»

**§5.3 Biases and Hallucinations (s. 18–20) — utelatelser som en form for hallusinasjon:**
> «Hallucinations in MT systems refer to outputs that may be fluent but semantically unfaithful to the source text. They manifest in various forms, including content fabrication (adding information to the output that is not in the source), **omission of key elements**, semantic drift where meaning subtly changes, and improper substitutions.»

## 4. Det negative funnet (like viktig)

Ordsøk i hele surveyen (verifisert på dokumentteksten):
- **«markup» = 0, «apparatus» = 0, «editorial» = 0, «lacuna» = 0, «footnote» = 0.**
- «reference-free»/«reference-less» = 0; «quality estimation» = 1 forekomst.
- Til kontrast: «low-resource» ≈ 57, «hallucination» ≈ 28, «historical» = 10 (mest «historically» / §2.1 «Historical Approaches» = SMT-historikk, ikke historiske *tekster*).
- «structure» ≈ 25, men **utelukkende** i lingvistisk forstand («structural generalization», «phrasal structures») — aldri dokumentstruktur eller markup.

**Konklusjon:** feltets tyngste survey fører lavressursspråk, evaluering og hallusinasjon/utelatelse som sentrale åpne problemer, men nevner **ikke med ett ord** bevaring av redaksjonell markup, kritisk apparat, lakuner eller dokumentstruktur. Utelatelse behandles kun som en *hallusinasjonstype* i MT mellom språk, ikke som en integritetsegenskap ved en kildeutgave. Det korroborerer B1-negativfunnet i samlerapporten fra autoritativt hold: apparat-integritet er et reelt hull, ikke et oversett hjørne.

## 5. Hva kilden IKKE sier (øvrig)

- Ingen empiri, ingen CER; en survey. Ingen norsk, intet ö/ø.
- Berører ikke sikkerhetsfiltre/refusjon som kilde til utelatte partier (jf. Tekgürler 2025).
- Referansefri QE som *navngitt* delfelt er fraværende i teksten, selv om §5.2 diskuterer LLM-basert feilmerking — et påfallende fravær gitt at samme tidsskrift utgir et helt QE-temanummer (Sindhujan et al. 2025, neste utgave).
