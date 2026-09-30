#!/bin/zsh
# A/B 시연·예시 미리보기 생성기.
# 사용자 설정(CLAUDE.md, 훅, 플러그인, 메모리)이 섞이지 않게 빈 설정 폴더와 빈 작업 폴더에서 claude -p를 실행한다.
# "with" 조건은 claude.ai 프로젝트(프로젝트 지침 한 줄 + 프로젝트 지식 파일)를 시스템 프롬프트로 흉내 낸다.
# 사용법: tools/gen-demo.sh <이름> <prompt 키> [예시 md 경로]
set -e
ROOT=${0:A:h:h}
NAME=$1; KEY=$2; DS=$3
CLEAN=${CLEAN_DIR:-$TMPDIR/session02-clean}
mkdir -p $CLEAN/cfg $CLEAN/work/$NAME
OUT_SUFFIX="설명 없이 완성된 HTML 코드 하나만 출력해줘. 파일로 저장하지 말고 응답에 코드만."
case $KEY in
  web)    PROMPT="동네 반찬 구독 서비스 '골목찬장' 소개 웹페이지 한 장을 HTML 파일 하나로 만들어줘. 들어갈 내용: 한 줄 소개, 하는 일 3가지, 연락 방법. $OUT_SUFFIX" ;;
  slides) PROMPT="물류 관제 솔루션 '정시로' 도입 제안 발표 슬라이드 3장을 HTML 파일 하나로 만들어줘. 1장 제목, 2장 핵심 내용 3가지, 3장 다음 할 일. $OUT_SUFFIX" ;;
  detail) PROMPT="프로젝트에 올려둔 디자인 시스템을 따라 '골목찬장 주 5일 반찬 구독' 상세페이지를 가로 860px, 세로로 긴 한 장으로 만들어줘. 순서: 핵심 문구, 특징 3개, 사용 장면, 스펙 표, 구매 안내. 핵심 문구와 특징은 맨 위 3000px 안에 넣어줘. 상품 정보: 가격 [ ], 구성 하루 반찬 3가지와 국 1가지, 평일 아침 7시 전 문 앞 배송, 주문 마감 일요일 18시, 반찬은 배송 전날 저녁에 만든다, 다 먹은 용기는 다음 배송 때 회수. 사진이 들어갈 곳은 테두리만 있는 빈 네모에 '사진: 무엇'이라고 적어 둬. 후기, 별점, 판매량, 인증, 수치는 지어내지 말고 내가 적은 것만 써. 모르는 칸은 [ ]로 비워 둬. 디자인 시스템에 없는 요소는 추가하지 말고, 화면에 붙어 따라다니는 메뉴나 버튼은 쓰지 마. HTML 파일 하나로. $OUT_SUFFIX" ;;
  report) PROMPT="품질보증팀 주간 보고 서식을 HTML 파일 하나로 만들어줘. 구성: 제목, 요약 3줄, 표 1개, 다음 할 일. A4 한 장에 인쇄되게 해줘. $OUT_SUFFIX" ;;
esac
ARGS=(-p "$PROMPT" --output-format json --disallowedTools "Write,Edit,Bash,NotebookEdit,WebFetch,WebSearch")
if [[ -n $DS ]]; then
  SYS=$CLEAN/work/$NAME/project.txt
  { echo "프로젝트 지침: 모든 결과물은 프로젝트 지식의 design-system.md를 따른다. 문서에 없는 스타일은 쓰지 않는다."
    echo; echo "프로젝트 지식: design-system.md"; echo '"""'; cat $ROOT/$DS; echo '"""'; } > $SYS
  ARGS+=(--append-system-prompt-file $SYS)
fi
cd $CLEAN/work/$NAME
CLAUDE_CONFIG_DIR=$CLEAN/cfg claude "${ARGS[@]}" < /dev/null > $ROOT/demo/raw/$NAME.json
echo "$PROMPT" > $ROOT/demo/raw/$NAME.prompt.txt
