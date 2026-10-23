#!/bin/sh
# 원본 폰트(OFL)를 tools/fonts-src/에 받는다.
# build.py는 장표에 쓰인 글자만 잘라 넣고, render_brand.py는 가상 브랜드 로고 글자를 윤곽선으로 바꾼다.
set -e
cd "$(dirname "$0")"
mkdir -p fonts-src
BASE=https://raw.githubusercontent.com/google/fonts/main/ofl
curl -fsSL -o "fonts-src/NotoSansKR[wght].ttf" "$BASE/notosanskr/NotoSansKR%5Bwght%5D.ttf"
curl -fsSL -o fonts-src/OFL-notosanskr.txt "$BASE/notosanskr/OFL.txt"
curl -fsSL -o "fonts-src/NotoSerifKR[wght].ttf" "$BASE/notoserifkr/NotoSerifKR%5Bwght%5D.ttf"
curl -fsSL -o fonts-src/OFL-notoserifkr.txt "$BASE/notoserifkr/OFL.txt"
ls -l fonts-src
