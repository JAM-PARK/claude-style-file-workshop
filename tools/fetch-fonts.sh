#!/bin/zsh
# tools/build.py가 서브셋을 만들 때 쓰는 원본 폰트(OFL)를 받는다. 저장소에는 올리지 않는다(약 20MB).
set -e
DIR=${0:A:h}/fonts-src
mkdir -p $DIR && cd $DIR
BASE=https://raw.githubusercontent.com/google/fonts/main/ofl
for f in gothica1/GothicA1-Regular.ttf gothica1/GothicA1-Medium.ttf gothica1/GothicA1-Bold.ttf \
         nanumgothiccoding/NanumGothicCoding-Regular.ttf; do
  curl -sfLO "$BASE/$f"
done
ls -la
