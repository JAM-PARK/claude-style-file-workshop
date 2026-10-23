#!/bin/sh
# 장표에 넣을 원본 폰트(OFL)를 tools/fonts-src/에 받는다. build.py가 쓰인 글자만 잘라 넣는다.
set -e
cd "$(dirname "$0")"
mkdir -p fonts-src
BASE=https://raw.githubusercontent.com/google/fonts/main/ofl
curl -fsSL -o "fonts-src/NotoSansKR[wght].ttf" "$BASE/notosanskr/NotoSansKR%5Bwght%5D.ttf"
curl -fsSL -o fonts-src/OFL-notosanskr.txt "$BASE/notosanskr/OFL.txt"
ls -l fonts-src
