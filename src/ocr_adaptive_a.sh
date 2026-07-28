#!/usr/bin/env bash
# ocr_adaptive_a.sh — metode A (adaptiv terskling). FORKASTET/ELIMINERT.
#
# Negativt resultat, tatt med for etterprøvbarhet (se docs/decisions/ADR-006).
# Hypotesen var at lokal adaptiv terskling (Sauvola-lignende, ImageMagick -lat)
# ville slå tesseracts egen gråtone-binarisering på fotografert typoskript.
# Den ble falsifisert: -lat lager speckle på Adobe Scan-foto som tesseract
# leser som ekstra tegn, og ordtellingen eksploderer.
#
# Målt på verstesiden p084 (baseline 36,0 % CER):
#   -lat 151x151+8%   -> CER  77,8 %
#   -lat 201x201+10%  -> CER 114,1 %
#   -lat 251x251+12%  -> CER 101,6 %
# Vinner der er vinner overalt; ingen vant, så A ble ikke kjørt på alle 8.
#
# Sidebildene (PNG) er IKKE en del av repoet (en museumssamling i Oslo).
#
# Bruk:  ./ocr_adaptive_a.sh <side.png> <vindu>   f.eks.  ./ocr_adaptive_a.sh p084.png 151x151+8%
set -euo pipefail

PNG="${1:?bruk: ocr_adaptive_a.sh <side.png> <vindu, f.eks. 151x151+8%>}"
WIN="${2:-151x151+8%}"
STEM="$(basename "${PNG%.*}")"
PROC="${STEM}_lat_${WIN//[^0-9]/_}.png"

magick "$PNG" -colorspace Gray -lat "$WIN" -deskew 40% "$PROC"
tesseract "$PROC" "${PROC%.png}" -l nor --psm 6
echo "Ord: $(wc -w < "${PROC%.png}.txt" | tr -d ' ')   (jf. ~262 ekte ord på p084)"
