#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vision_ocr.py — diplomatarisk transkripsjon av typoskriptsider med Claude vision.

Metode B i sammenligningen. Sender hvert sidebilde til modellen med en
diplomatarisk prompt (bevar ö, arkaisk ortografi, skrivefeil, tegnsetting)
og lagrer råteksten. Måler ö/ø for å avdekke stille normalisering.

NØKKELEN LESES FRA MILJØVARIABEL — aldri hardkodet, aldri i repoet:
    export ANTHROPIC_API_KEY=...        # settes i skallet før kjøring
Scriptet inneholder ingen nøkkelverdi. Se docs/decisions/ADR-008.

Sidebildene (PNG) er IKKE en del av repoet — objektet tilhører
en museumssamling i Oslo. Pek --png-dir mot din egen kopi.

Bruk:
    export ANTHROPIC_API_KEY=...
    python vision_ocr.py --png-dir /sti/til/png --glob 'Scan4_p*.png' --out-dir ut/
"""
import argparse, base64, glob, json, os, re, subprocess, sys, urllib.request

MODELL = "claude-opus-4-8"

PROMPT = (
    "Transkriber denne siden fra et norsk typoskript fra 1920-årene. "
    "Trofast diplomatarisk avskrift. Skriv nøyaktig det som står. ö skal være ö, ikke ø. "
    "Behold gammel ortografi: efter, nu, sprog, ind, mig, skulde. Behold skrivefeil. "
    "Behold tegnsetting. Ikke moderniser. Ikke rett. Ikke forklar. Kun teksten."
)


def hent_noekkel():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("FEIL: miljøvariabelen ANTHROPIC_API_KEY er ikke satt. "
                 "Kjør:  export ANTHROPIC_API_KEY=...  (nøkkelen skal aldri i repoet)")
    return key


def transkriber(png, key, snd_jpg, maks_tokens=2500):
    # 1568 px lang kant = leverandørens optimale maks; styrer kvalitet/kostnad
    subprocess.run(["magick", png, "-resize", "1568x1568>", "-quality", "92", snd_jpg], check=True)
    img = base64.standard_b64encode(open(snd_jpg, "rb").read()).decode()
    body = json.dumps({
        "model": MODELL, "max_tokens": maks_tokens,
        "messages": [{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": img}},
            {"type": "text", "text": PROMPT}]}]
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=body,
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=180))
    return r["content"][0]["text"], r.get("stop_reason")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--png-dir", required=True)
    ap.add_argument("--glob", default="Scan4_p*.png")
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args(argv)

    key = hent_noekkel()
    os.makedirs(args.out_dir, exist_ok=True)
    pages = sorted(glob.glob(os.path.join(args.png_dir, args.glob)))
    if not pages:
        sys.exit(f"Ingen bilder matchet {args.glob} i {args.png_dir}")

    for f in pages:
        n = re.search(r"p(\d+)", os.path.basename(f)).group(0)   # p003
        snd = os.path.join(args.out_dir, f"{n}_snd.jpg")
        txt, stop = transkriber(f, key, snd)
        with open(os.path.join(args.out_dir, f"{n}.txt"), "w", encoding="utf-8") as fh:
            fh.write(txt)
        print(f"  {n}: {len(txt.split())} ord | ö={txt.count('ö')} ø={txt.count('ø')} | stop={stop}",
              flush=True)
    print("FERDIG")


if __name__ == "__main__":
    main()
