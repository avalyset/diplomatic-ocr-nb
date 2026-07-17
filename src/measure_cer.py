#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
measure_cer.py — CER/WER for OCR-hypoteser mot en blindtranskribert fasit.

Referanseimplementasjon brukt i den diplomatariske metodesammenligningen.
Måler tegn- og ord-feilrate (Levenshtein) mellom en OCR-hypotese og fasiten,
med bootstrap-95 %-konfidensintervall over de 8 sidene.

Preprosessering (symmetrisk, dokumentert — ingen annen rensing):
  * sidetall-linjer fjernes fra hypotesen (fasiten inneholder dem ikke),
  * whitespace normaliseres på begge sider.

Determinisme: random.seed(1930) settes før bootstrap. Samme input gir
identiske tall hver gang. Baseline (rå tesseract-OCR i txt/) reproduserer
results/aggregat.json -> "baseline" nøyaktig.

Hypotesefilene (rå OCR / vision-utskrift) og sidebildene er IKKE en del av
dette repoet — objektet tilhører Vigelandsmuseets samling. Tallene i results/
er utledet av dem. Kjør selv ved å peke --hyp-dir mot din egen kopi.

Bruk:
  python measure_cer.py --fasit ../data/fasit_n8.json \\
      --hyp-dir /sti/til/txt --pattern 'Scan4Aars_p{n}.txt' --label baseline
"""
import argparse, json, os, random, re, collections, sys


# ---- Levenshtein (tegn) med backtrace for forvekslingsstatistikk ----
def lev(a, b):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        ai = a[i - 1]; Di = D[i]; Dp = D[i - 1]
        for j in range(1, m + 1):
            Di[j] = min(Dp[j] + 1, Di[j - 1] + 1,
                        Dp[j - 1] + (0 if ai == b[j - 1] else 1))
    # backtrace -> liste av (lest, faktisk)-ops for forvekslingstabellen
    i, j = n, m; ops = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i - 1][j - 1] + (0 if a[i - 1] == b[j - 1] else 1):
            if a[i - 1] != b[j - 1]:
                ops.append((a[i - 1], b[j - 1]))
            i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i - 1][j] + 1:
            ops.append((a[i - 1], '∅')); i -= 1
        else:
            ops.append(('∅', b[j - 1])); j -= 1
    return D[n][m], ops


# ---- Levenshtein (ord) ----
def wlev(a, b):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1,
                          D[i - 1][j - 1] + (0 if a[i - 1] == b[j - 1] else 1))
    return D[n][m]


def strip_pagenum(t):
    """Fjern rene sidetall-linjer (f.eks. '- 2 -', '|130|'). Fasiten har dem ikke."""
    out = []; stripped = 0
    for ln in t.split('\n'):
        core = re.sub(r'[-=–—.\s|]', '', ln)
        if core.isdigit() and 1 <= len(core) <= 4:
            stripped += len(ln); continue
        out.append(ln)
    return '\n'.join(out), stripped


def norm(t):
    return re.sub(r'\s+', ' ', t).strip()


def measure(fasit, load_hyp, seed=1930, resamples=10000):
    """
    fasit: dict {sidenøkkel: fasittekst}
    load_hyp: funksjon sidenøkkel -> hypotesetekst (rå)
    Returnerer resultatdict (samme skjema som results/aggregat.json-oppføringene).
    """
    random.seed(seed)
    keys = sorted(fasit)
    per = []; conf = collections.Counter(); tot_strip = 0
    for k in keys:
        ref = norm(fasit[k])
        hyp_raw, st = strip_pagenum(load_hyp(k)); tot_strip += st
        hyp = norm(hyp_raw)
        dist, ops = lev(hyp, ref)            # hyp = lest, ref = fasit
        wd = wlev(hyp.split(), ref.split())
        per.append({'k': k, 'refchars': len(ref), 'refwords': len(ref.split()),
                    'cdist': dist, 'wdist': wd,
                    'cer': dist / len(ref), 'wer': wd / len(ref.split())})
        for a, b in ops:
            conf[(a, b)] += 1

    TC = sum(p['refchars'] for p in per); TW = sum(p['refwords'] for p in per)
    CD = sum(p['cdist'] for p in per); WD = sum(p['wdist'] for p in per)
    CER = CD / TC; WER = WD / TW

    def boot(metric):
        vals = []
        for _ in range(resamples):
            s = [random.choice(per) for _ in range(len(per))]
            if metric == 'cer':
                vals.append(sum(x['cdist'] for x in s) / sum(x['refchars'] for x in s))
            else:
                vals.append(sum(x['wdist'] for x in s) / sum(x['refwords'] for x in s))
        vals.sort(); return vals[250], vals[9750]
    cer_lo, cer_hi = boot('cer'); wer_lo, wer_hi = boot('wer')

    return {'CER': CER, 'CER_KI': [cer_lo, cer_hi],
            'WER': WER, 'WER_KI': [wer_lo, wer_hi],
            'reftegn': TC, 'reford': TW, 'per_side': per,
            'sidetall_fjernet_tegn': tot_strip,
            'forvekslinger': conf.most_common(40)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--fasit', required=True, help='sti til fasit_n8.json')
    ap.add_argument('--hyp-dir', required=True, help='mappe med OCR-hypoteser')
    ap.add_argument('--pattern', default='Scan4Aars_p{n}.txt',
                    help="filnavnmønster; {n} = 3-sifret sidetall (default baseline)")
    ap.add_argument('--label', default='hypotese')
    ap.add_argument('--out', help='skriv resultatdict som JSON hit')
    args = ap.parse_args(argv)

    with open(args.fasit, encoding='utf-8') as f:
        fasit = json.load(f)

    def load_hyp(key):
        n = key.split('_p')[1]              # 'Scan4_p003' -> '003'
        path = os.path.join(args.hyp_dir, args.pattern.format(n=n))
        with open(path, encoding='utf-8') as fh:
            return fh.read()

    res = measure(fasit, load_hyp)
    print(f"════ {args.label}: CER/WER mot blindfasit (n={len(res['per_side'])}) ════")
    print(f"  CER = {res['CER']*100:.2f} %   (95% KI {res['CER_KI'][0]*100:.2f}–{res['CER_KI'][1]*100:.2f})")
    print(f"  WER = {res['WER']*100:.2f} %   (95% KI {res['WER_KI'][0]*100:.2f}–{res['WER_KI'][1]*100:.2f})")
    print(f"  {res['reftegn']} referansetegn, {res['reford']} referanseord")
    print(f"  {'side':13}{'reftegn':>8}{'CER%':>7}{'WER%':>7}")
    for p in sorted(res['per_side'], key=lambda x: x['cer']):
        print(f"  {p['k']:13}{p['refchars']:>8}{p['cer']*100:>7.1f}{p['wer']*100:>7.1f}")

    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            json.dump(res, fh, ensure_ascii=False, indent=1)
        print(f"\n-> {args.out}")
    return res


if __name__ == '__main__':
    main()
