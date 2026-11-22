#!/usr/bin/env bash
# Render PNG exports of the brand SVGs with headless Chrome. Run from the repo root.
set -euo pipefail
C="google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --allow-file-access-from-files --default-background-color=00000000 --virtual-time-budget=3000"
SRC="file://$PWD/tools/brand-src"
OUT="web/brand"
png(){ $C --window-size=$3,$4 --screenshot="$OUT/$2" "$SRC/png.html?f=$1&w=$3&h=$4" >/dev/null 2>&1; }
png logo-mark.svg logo-mark-512.png 512 512
png logo-mark.svg logo-mark-192.png 192 192
png logo-mark.svg apple-touch-icon.png 180 180
png favicon.svg favicon-32.png 32 32
png logo.svg logo-1200.png 1200 269
png logo-reversed.svg logo-reversed-1200.png 1200 269
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --allow-file-access-from-files --virtual-time-budget=3000 --window-size=1200,630 --screenshot="$OUT/og-image.png" "$SRC/og.html" >/dev/null 2>&1
ls -la "$OUT"
