#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ocr_baseline.py — baseline-OCR (metode «baseline» i sammenligningen).

Pipelinen som produserte råtekst-hypotesene (txt/): tesseracts egen
gråtone-binarisering, ingen adaptiv terskling. Dette er referansen alle
andre metoder måles mot.

    pdftoppm -r 400 -gray          rasteriser 400 dpi gråtone
    ImageMagick -deskew 40% -normalize
    tesseract -l nor --psm 6       norsk, anta én sammenhengende tekstblokk

Ingen stavekontroll, ingen normalisering, ingen rensing — rå OCR.
Kilde-PDF-ene er IKKE en del av repoet (en museumssamling i Oslo).

Bruk:
    python ocr_baseline.py --pdf "/sti/Scan4Aars.pdf" --stem Scan4Aars --out-dir txt/
"""
import argparse, glob, os, subprocess, sys


def antall_sider(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
    for ln in out.stdout.splitlines():
        if ln.startswith("Pages:"):
            return int(ln.split()[1])
    raise RuntimeError("Fant ikke sidetall via pdfinfo")


def ocr_side(pdf, side, stem, out_dir):
    pre = os.path.join(out_dir, f"_{stem}_p{side:03d}")
    subprocess.run(["pdftoppm", "-f", str(side), "-l", str(side),
                    "-r", "400", "-gray", "-png", pdf, pre], check=True)
    raw = sorted(glob.glob(pre + "*.png"))[0]
    proc = pre + "_proc.png"
    subprocess.run(["magick", raw, "-deskew", "40%", "-normalize", proc], check=True)
    base = os.path.join(out_dir, f"{stem}_p{side:03d}")
    subprocess.run(["tesseract", proc, base, "-l", "nor", "--psm", "6"],
                   check=True, stderr=subprocess.DEVNULL)
    os.remove(raw); os.remove(proc)
    return base + ".txt"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--stem", required=True, help="filstamme, f.eks. Scan4Aars")
    ap.add_argument("--out-dir", default="txt")
    args = ap.parse_args(argv)

    os.makedirs(args.out_dir, exist_ok=True)
    n = antall_sider(args.pdf)
    for side in range(1, n + 1):
        path = ocr_side(args.pdf, side, args.stem, args.out_dir)
        print(f"  {os.path.basename(path)} OK", flush=True)
    print(f"FERDIG — {n} sider fra {os.path.basename(args.pdf)}")


if __name__ == "__main__":
    main()
