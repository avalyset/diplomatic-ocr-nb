# METHOD

English counterpart to `METODE.md`. The two are **equivalent, not summaries of
each other**: every section, table, number and caveat in the Norwegian document
has its match here. Where they diverge, that is an error — report it.

What was *measured*, nothing more. All figures reproduce from
`src/measure_cer.py` against `data/fasit_n8.json`. The baseline reproduces
`results/aggregat.json → baseline` exactly, bit for bit, which anchors the rest.

The document covers two cases. **Case 1 — Aars** (sections 1–8) is blind-validated
with CER against a human-written ground truth and stands unchanged. **Case 2 —
Vigeland** (below) is material *without* ground truth; it adds what actually
separates the cases and rests on controls other than CER. No page images, no
book manuscript and no editorial history are in this repository — only the
figures and the examples.

---

## 1. The object

An anonymous typescript, single copy, in a museum collection in Oslo.
Transcribed from Harald Aars' (1875–1945) handwritten diaries.
Unknown hand, unknown date. Manuscript pages 1–237+, 14 Oct 1920 – Nov 1940.
Riksmål with ö. Scanned with Adobe Scan (iOS), 400 dpi.

**Provenance unresolved** — who typed the transcript, and when, is not
established. This is an open lacuna in the edition and is to stand as one.

The page images and the source text beyond the eight ground-truth pages are
**not** part of this repository; the object belongs to a museum collection in
Oslo and image publication is subject to clearance with the institution. The
ground-truth transcription of the eight pages can be published independently of
the images (see ADR-009).

## 2. Blind protocol

Eight pages, `random.seed(1930)`, `random.sample(range(1,105), 8)` from Scan4
(manuscript 134–237): PDF pages 3, 27, 31, 51, 54, 79, 84, 100
(`data/UTVALG.txt`).

The ground truth was written diplomatically in `src/transkriber.html` **before**
any OCR text had been seen. The tool contains no OCR — only an image id and a
text field with `spellcheck="false"`, `autocorrect="off"`. Result:
**2,188 words / 12,478 characters** (after whitespace normalisation).

Thresholds set **before** measurement: < 5 % CER = publishable, > 15 % = manual
transcription required.

## 3. Measurement

CER = Levenshtein(characters, hypothesis, ground truth) / reference characters.
WER likewise on words. Whitespace normalised on both sides. Bare page-number
lines (e.g. «- 2 -») removed symmetrically from the hypothesis (the ground truth
has none): 34 characters for the baseline. CI: bootstrap over the eight pages,
10,000 resamples, `seed 1930`.

| method | CER | WER | per page (CER) |
|--|--|--|--|
| **baseline** — tesseract 400 dpi greyscale, `-l nor --psm 6` | **21.3 %** (95 % CI 14.7–28.1) | 52.4 % (41.0–64.7) | 9.8 – 36.0 % |
| **A** — adaptive thresholding (ImageMagick `-lat`) | *see 5a* | — | — |
| **B** — `claude-opus-4-8` vision, diplomatic prompt | **5.35 %** (95 % CI 3.0–8.0) | 12.9 % (10.2–16.2) | 2.2 – 11.4 % |
| **D** — Adobe text layer | *dead, see 5b* | — | — |

Per page and aggregate: `results/n8_eksplorativ.tsv`, `results/aggregat.json`.

**Verdict against threshold: UNDECIDED.** B missed the 5 % threshold (point
estimate 5.35 %), but the confidence interval includes 5 %. Reported as
undecided, not as passed. **No post-hoc extension of n.**

## 4. Diplomatic fidelity — the principal finding

Method B, across eight pages (`results/troskap.tsv`):

- **ö = 71, ø = 0**
- *efter* preserved (*etter* = 0), *skulde* preserved (*skulle* = 0), *nu* = 8 (*nå* = 0)

No unmotivated modernisation measured. This is the principal fear in LLM-based
OCR of historical material: silent normalisation that goes undetected because
the result *looks* correct. Under a diplomatic prompt it is measured here at
zero in the feared direction (ö→ø).

**Two explicit caveats:**

1. *No control arm.* Whether the prompt caused the fidelity, or whether the
   model would have been faithful regardless, is **not** measured. No causal
   claim can be made from these data.
2. *Over-correction in the other direction.* The human ground truth has ö = 65,
   ø = 3, while B has ö = 71, ø = 0 — B therefore found *fewer* ø than the human
   did. B did not normalise ö→ø (the feared direction), but the prompt's explicit
   «ö is to be ö, not ø» may have over-corrected the *opposite* way and turned
   three genuine ø into ö. Alternatively the ground-truth writer wrote ø where
   the source has ö — not settled here. The prompt is in the repository
   (`src/vision_ocr.py`), so a reader can see the exact instruction that may
   have caused the divergence. Either way it is counted in B's 5.35 % CER.

## 5. Rejected methods — negative results

Reported straight, not buried.

### 5a. Adaptive thresholding (method A) — falsified

The hypothesis: local adaptive thresholding (Sauvola-like, `-lat`) would beat
tesseract's own greyscale binarisation on photographed typescript. Tested on the
worst page **p084** (baseline 36.0 % CER), three DPI-correct windows:

| window | CER p084 |
|--|--|
| baseline (tesseract's binarisation) | **36.0 %** |
| `-lat 151x151+8%` | 77.8 % |
| `-lat 201x201+10%` | 114.1 % |
| `-lat 251x251+12%` | 101.6 % |

A winner on the worst page is a winner everywhere; none won, so A was not run on
all eight. `-lat` produces speckle on Adobe Scan photographs that tesseract reads
as extra characters (hypothesis word counts 409/769/683 against ~262 real words).
The opposite of what the literature suggests for shadowed material.
**A eliminated.** (ADR-006)

### 5b. Adobe text layer (method D) — dead

- 3 of 4 scans (Scan1/2/4, «Adobe Scan for iOS») have **0 characters** of text
  layer. The eight ground-truth pages are all Scan4 → D is not measurable against
  the ground truth.
- The fourth (Scan3, «Acrobat Paper Capture», 1925–27) has a text layer, but
  **ö = 0, ø = 112** — normalised. Adobe silently does exactly what B did not.
  Disqualified regardless of how low a CER might be. (ADR-007)

Worth knowing for anyone running OCR over Norwegian pre-war material with
Acrobat.

### 5c. CER measured against an edited edition — invalid

Measuring OCR against the *edited* book edition (not a faithful transcription)
gave a false 25.2 %, decomposing into ~67 % OCR error / ~30 % punctuation / ~3 %
modernisation. The edited text existed; the blind ground truth had to be written.
A tempting methodological error. (ADR-003)

### 5d. difflib string matching as word suggestion — rejected

Gave *björnegruppen → barnegruppen* (ratio 0.88) and *ensartede → entartede*
(0.889). Character distance does not measure meaning. (ADR-004)

### 5e. The rule «-ede → -et + consonant doubling» — rejected

Gave *rede → rett*, *lede → lett*, *træde → trett*. 3 errors in 42 rows = 7 %
error rate on a verification set. (ADR-005)

## 6. What is *not* a finding

That Claude beats tesseract. That is trivial, model-dependent, and obsolete
within the year. The contribution is **the measurement protocol for diplomatic
fidelity** — ö/ø rate and archaic preservation ratio — which can be applied to
any model and any historical corpus.

## 7. Scope

One language, one corpus, one model, eight pages. A method note with cases.
No generalisable claims.

## 8. Tools and attribution

`claude-opus-4-8` is both the tool under test (method B) and a tool in the
execution (code written with Claude Code). The ground truth was written by a
human **without** the model in the loop — which is precisely why the blind
protocol exists.

Author/committer: Eirik Botten Nicolaysen. `Co-authored-by` trailer where Claude
Code wrote code.

---

# Case 2 — Vigeland: *Erindringer* (1918)

The same question — diplomatic fidelity — but material that removes the basis for
the Case 1 measurement method. What follows is what that difference forced, and
what is new. The edition itself (287 pages, ~128,000 words) belongs elsewhere;
only the figures and examples that separate the cases stand here.

## 2.1 A different source type — and what it forces

Case 1 is a typescript with a **known exemplar** (Aars' own hand) and an
**established blind ground truth**. Case 2 is one link further away: a typed
**1949 transcription of Vigeland's handwritten manuscript**. The transcriber —
not the author — is the last hand on the text, the exemplar is not available, and
**no ground truth exists or can be written** (writing one would require precisely
the handwriting of which the transcriber already lost passages).

The consequence for method choice is absolute: CER against ground truth is
impossible. Fidelity cannot be *measured against a reference*; it can only be
*monitored against the source's own internal anchors* — the ö/ø ratio, word count
against a comparator, the sheet marks, and the source's own lacuna convention.
Case 1 selects a method with a number. Case 2 must guard a production without
one.

## 2.2 Population-wide gates, not sampled CER

CER is the right tool when **the method is being chosen**: Case 1 measured four
methods on eight pages and got 5.35 % for the winner. It is the wrong tool when
**production is being monitored**: a sample of 8 of 287 pages says nothing about
the other 279. A method that is faithful on average can collapse on a single page,
and CER on a random sample will most likely never see it.

Hence: three deterministic gates across **all 287 pages**, not an estimate on a
sample. Flag, never correct. The figures in the table are on **raw OCR** — the
output the gates monitor, before de-duplication and modernisation.

| gate | Case 2 — Vigeland, raw OCR (287 pages) | Case 1 — Aars, production (114 pages, ADR-010) |
|--|--|--|
| **a — ö/ø** | ö = 5161, ø = 19; but 15 ø sit in OCR-refusal / handwriting metatext — **4 genuine body-text ø** (sheets 204, 163, 235) | ö = 1081, ø = 5 (ø share 0.46 %) |
| **b — word count against comparator** (< 60 %) | 2 pages new-dropout; 97 sheets old-dropout | not run |
| **c — garble markers** | 4 vowel-less words, 0 words > 25 characters, 2 repeated lines, 86 unexpected characters (mostly accents) | not run |

> **ERRATUM 2026-07-30 — ö/ø on raw OCR.** The figure `5161/19` **does not
> reproduce** from `tekst/` as the directory now stands.
>
> | measurement | ö | ø |
> |---|---:|---:|
> | all 287 page files in `tekst/` | 5,153 | 14 |
> | the 280 pages that actually enter the manuscript stream | 5,094 | 4 |
> | manuscript stream after de-duplication *(published figure, reproduces)* | 5,094 | 4 |
> | finished EPUB including colophon *(published figure, reproduces)* | 5,095 | 11 |
>
> The two later stages reproduce exactly. The first does not.
>
> **What 5161/19 was measured on is not established, and has not been guessed.**
> A plausible hypothesis is an OCR state predating the correction commits, but
> that is a hypothesis, not a finding, and is not recorded as one. The figure
> therefore stands in the text as published, with this caveat.
>
> Note also what the row shows: the ö count is **identical** before and after
> modernisation (5,094 in both). That is expected — modernisation never touches
> ö — but it means the ö/ø gate operates **between OCR and manuscript stream**,
> not after.

**Which set each figure comes from.** The Aars column is *production* (114 pages),
not the blind ground-truth set. The ground-truth figure ö = 71 / ø = 0 applies to
the **8 randomly drawn pages the method was selected on** (§4) and must not be set
against a population figure — measuring 287 pages against 8 is exactly the error
this section warns about. Production against production: 1081/5 (Aars, 114 pages)
and 5161/19 (Vigeland, 287 pages, raw OCR).

**Vigeland through the stages** (ö/ø): raw OCR 5161/19 → manuscript stream after
de-duplication, with duplicate sheets and refusal pages excluded, 5094/4 →
finished EPUB including colophon 5095/11 (the colophon is modern bokmål and
contributes ø). The 4 genuine body-text ø survive all the way; the other 15
disappear with the refusal pages, **not by correction**.

The gate is not a quality figure but a *filter*: it lifts every deviant page to
the eye instead of promising that the average is good. By contrast the old EPUB
corpus (gate c, round 1) had 286 vowel-less words in Part 3 and 357 repeated
lines in Part 4 — the gate separates the two quality classes sharply.

## 2.3 The rejected OCR round as a diagnostic instrument

An older EPUB corpus (earlier OCR) was **unusable as reading text** — massive text
loss, repeated paragraphs, corrupt punctuation. It was not used as text. But used
as a **comparator** in gate b it revealed dropout in both directions: **97 sheets**
where the old one had lost text (extreme case sheet 113: new 459 words against old
15 = 30.6×; sheet 95: 21×), and **2 sheets** where the new OCR slipped. Without an
independent second measurement, new-dropout on those two sheets would have had
nothing to register against.

Principle: **never discard the bad transcription.** A worthless text is still an
independent measurement. Its value lay not in the words but in having been made
separately, and therefore being able to cross the new one.

## 2.4 The sheet mark as data

Page↔sheet was reconstructed from the **printed sheet marks** in the typescript
(`- 93 -`, `— 93 —`, `258 a`), not from arithmetic (page number + offset). The
marks caught what arithmetic could not:

- **Drift** — an interleaved scan page (refusal text, not a numbered sheet) caused
  a −1 shift through the rest of a part; the mark, not the counter, revealed it.
- **Interleaved a-sheets** — 221a and 258a, sheets without an integer number of
  their own.
- **Faded duplicates** — the same sheet scanned twice: sheet 115 (99.6 % identical
  text), 226 (99.5 %), 258a (93.7 %). Arithmetic counts them as two.
- **Miscounted tail** — round 1's assumed «271–279» (nine numbers on eight pages)
  was an arithmetic error; the tail is 272–279, one-to-one, and **no sheet is
  missing**.

Every time arithmetic and sheet mark conflicted, **the arithmetic was wrong**. The
real gaps (sheet 172, a defective OCR file with the scan intact; sheet 266, a
number jump) stood as lacunae precisely because the marks, not the count, decided
them.

## 2.5 The source marks its own voice

The text has two layers that must not be mixed: **Vigeland's text** (first person,
«jeg husker …») and **the transcription's apparatus** (editorial, third
person/imperative: «(I margen: flyttes frem.)»). They are separated on grammatical
person and parenthesis notation — a structural signal in the source itself, not a
judgement call — and the apparatus is never modernised.

**Quotation marks are a hard gate against correction:** a word in quotation marks
is a citation or a name and is not touched, however «wrong» it may look. Example:
**«Tarrisken»** — a nickname punning on «ta risken» (take the risk). A plausibility
or spelling correction would have split it into two words; the quotation gate
forbids that, and the name stands. The source knows the difference between its own
voice and an error; the task is to listen, not to overrule.

## 2.6 Lacuna classification: falsification and revalidation

155 whitespace lacunae in the typescript were divided into **attested** (a genuine
lacuna where the transcriber could not read the exemplar → marked `[…]`) and
**unattested** (plain typewriter spacing → collapses).

- **Original criterion** — attested only on narrow syntactic signals (quotation,
  missing word before punctuation, preposition before); the rest assumed to be
  typewriter spacing.
- **The sample that felled it** — 10 random items from the *unattested* group read
  against the page image: **4 of 10 were genuine lacunae**. Criterion rejected.
- **Revised criterion** — only a gap directly after a sentence end (`.`/`!`/`?`)
  *and* followed by a capital letter counts as typewriter spacing; everything else
  is attested. Result: **93 attested / 62 unattested**. *(Corrected 2026-07-30
  from «58»; see the erratum note below.)*
- **Revalidation on unseen data** — 10 new items drawn from the gaps that moved to
  attested, read against the image. Three of the ten had already been seen in the
  first sample, so **effective unseen n = 7, not 10**. **7 of 7 were genuine
  lacunae.**

> **ERRATUM 2026-07-30 — the lacuna counts.** The published version gave
> «93 attested / 58 unattested», total 151. **The unattested figure was wrong.**
>
> Recounted in code against the manuscript stream (`skript/kjerne.py`, the same
> gap criterion the modernisation step uses):
>
> | measurement | gaps | attested | unattested |
> |---|---:|---:|---:|
> | raw manuscript stream | 160 | **98** | **62** |
> | after apparatus stashing (as `moderniser.py` does first) | 155 | **93** | **62** |
>
> The attested figure **93 reproduces** for the reading stream. The unattested
> figure is **62**, not 58, and the total is **155**, not 151. The text above is
> corrected.
>
> The 98 − 93 difference is exactly the **five gaps that lie inside `(( ))`
> apparatus blocks**: the modernisation step stashes the apparatus before it
> counts, so those five vanish into the placeholder. Both figures are correct for
> their object — 98 = all attested lacunae, 93 = attested lacunae in reading text.
> **Always state which surface a figure applies to.**
>
> What produced 58 and 151 is **not established** and has not been guessed.

**Erasure test** (are the blanks erasures rather than lacunae?): on a selection of
pages **50 gaps** were contrast-enhanced (normalisation, gamma, R/G/B channels,
high-pass) and measured against a control — the interlinear space in the same
column, which captures paper and show-through but has never held text. **50 of 50:
no trace.** The basis for the interpretation: a mechanical erasure **lightens** —
it abrades the paper surface — whereas show-through and offset **darken**. The
traces present in the gaps were dark (show-through), never the lightening signature
of erasure. The blanks are lacunae.

## 2.7 Honest limitations (Case 2)

- **No measured CER.** No ground truth exists for Vigeland, and none can be
  written. Fidelity rests on the gates and on the ö/ø ratio in the manuscript body
  text (5094 ö / 4 ø after de-duplication; raw OCR caught 19 ø, but 15 were refusal
  metatext), not on a reference. This is **weaker evidence** than Case 1's blind
  measurement and is to be read as such: absence of flags is not the same as a
  measured error rate.
- **n = 2 cases.** Two materials, no population. Nothing is generalised from two
  points.
- **The lacuna method locates only wide gaps automatically.** Narrow 2–3-character
  attested gaps are not distinguished from ordinary sentence spacing at the scan
  resolution and must be checked by hand. The erasure test's «50 of 50» applies to
  the mechanically locatable selection, not to all 93 attested gaps.

---

## Equivalence with `METODE.md`

This document is the English half of a bilingual pair. Both halves carry the same
sections, tables, figures and caveats. The two correction notes in §2.2 and §2.6
are present in both, in the same places. A divergence between the halves is a
defect and is to be recorded in the finding register, not silently reconciled.
