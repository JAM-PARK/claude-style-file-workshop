#!/bin/zsh
# 장표에 넣을 원본 폰트(OFL)를 받는다. 결과는 tools/fonts-src/ (저장소에는 올리지 않음)
set -e
DIR=${0:A:h}/fonts-src
mkdir -p $DIR && cd $DIR
BASE=https://github.com/google/fonts/raw/main/ofl
curl -fsSLO $BASE/blackhansans/BlackHanSans-Regular.ttf
curl -fsSL -o OFL-BlackHanSans.txt $BASE/blackhansans/OFL.txt
for w in Regular Bold ExtraBold; do curl -fsSLO $BASE/nanumgothic/NanumGothic-$w.ttf; done
curl -fsSL -o OFL-NanumGothic.txt $BASE/nanumgothic/OFL.txt
# 샘플 영수증용 (samples/에만 쓰고 배포 HTML에는 넣지 않는다)
curl -fsSLO $BASE/nanumgothiccoding/NanumGothicCoding-Regular.ttf
curl -fsSLO $BASE/nanumgothiccoding/NanumGothicCoding-Bold.ttf
ls -la
