---
name: 카드 뉴스·릴스 세션 자료
description: 초록 칠판에 분필 세 색과 페인트 오선으로 적은 세션 악보.
colors:
  board: "#1E3A2F"
  board-deep: "#142820"
  chalk: "#ECEFE6"
  chalk-dim: "rgba(236, 239, 230, 0.68)"
  paint: "rgba(236, 239, 230, 0.42)"
  yellow-chalk: "#F3D35B"
  yellow-chalk-hover: "#F7DF85"
  pink-chalk: "#F2A0A0"
  dim-on-yellow: "rgba(30, 58, 47, 0.78)"
  dim-on-pink: "rgba(30, 58, 47, 0.9)"
  paint-on-fill: "rgba(30, 58, 47, 0.45)"
typography:
  cover-display:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "112px"
    fontWeight: 900
    lineHeight: 1.12
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "84px"
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  rehearsal-letter:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "104px"
    fontWeight: 900
    lineHeight: 1
  diagram-node:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "72px"
    fontWeight: 900
    lineHeight: 1.1
  diagram-step:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "56px"
    fontWeight: 900
    lineHeight: 1.2
  lede:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "44px"
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "36px"
    fontWeight: 400
    lineHeight: 1.5
  row-label:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "36px"
    fontWeight: 700
    lineHeight: 1.5
  step:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "32px"
    fontWeight: 400
    lineHeight: 1.5
  table:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "30px"
    fontWeight: 400
    lineHeight: 1.45
  note:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "26px"
    fontWeight: 400
    lineHeight: 1.5
  prompt:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "24px"
    fontWeight: 400
  button:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "26px"
    fontWeight: 700
  strip-mark:
    fontFamily: "Slide Sans, Malgun Gothic, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "24px"
    fontWeight: 700
rounded:
  none: "0"
  bracket-hook: "16px"
  dot: "50%"
spacing:
  stage-x: "96px"
  stage-top: "196px"
  stage-bottom: "120px"
  strip-top: "84px"
  strip-height: "64px"
  foot-bottom: "44px"
  body-gap: "56px"
  column-gap: "72px"
  row-gap: "48px"
  row-pad: "24px 0 22px"
  prompt-indent: "44px"
components:
  slide:
    backgroundColor: "{colors.board}"
    textColor: "{colors.chalk}"
    padding: "196px 96px 120px"
    width: "1920px"
    height: "1080px"
  part-opener-yellow:
    backgroundColor: "{colors.yellow-chalk}"
    textColor: "{colors.board}"
  check-opener-pink:
    backgroundColor: "{colors.pink-chalk}"
    textColor: "{colors.board}"
  current-measure:
    backgroundColor: "{colors.yellow-chalk}"
    height: "60px"
  current-measure-on-fill:
    backgroundColor: "{colors.board}"
    height: "60px"
  copy-button:
    backgroundColor: "{colors.yellow-chalk}"
    textColor: "{colors.board}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "10px 30px"
  copy-button-hover:
    backgroundColor: "{colors.yellow-chalk-hover}"
    textColor: "{colors.board}"
  copy-button-done:
    backgroundColor: "{colors.chalk}"
    textColor: "{colors.board}"
  copy-button-small:
    backgroundColor: "{colors.yellow-chalk}"
    textColor: "{colors.board}"
    typography: "{typography.strip-mark}"
    padding: "6px 20px"
  slot:
    textColor: "{colors.yellow-chalk}"
  practice-mark:
    textColor: "{colors.yellow-chalk}"
  caution-text:
    textColor: "{colors.pink-chalk}"
  line-official:
    backgroundColor: "{colors.chalk}"
    height: "3px"
  line-reported:
    backgroundColor: "{colors.chalk-dim}"
    height: "1px"
  line-unsure:
    backgroundColor: "{colors.chalk-dim}"
    height: "2px"
  line-neutral:
    backgroundColor: "{colors.paint}"
    height: "2px"
  rehearsal-letter-opener:
    typography: "{typography.rehearsal-letter}"
    rounded: "{rounded.none}"
    size: "150px"
  rehearsal-letter-strip:
    typography: "{typography.strip-mark}"
    rounded: "{rounded.none}"
    size: "32px"
---

# Design System: 카드 뉴스·릴스 세션 자료

## Overview

**Creative North Star: "음악실 오선 칠판"**

초록 칠판 바탕에 분필 흰색 글자를 쓰고, 반투명 흰 페인트로 오선과 마디줄을 그은 세계예요. 진행 위치는 악보 기호로 읽어요: 지금 장표는 오선 띠의 칠한 마디, 실습 장표는 늘임표가 걸린 마디, 예약 작업처럼 매일 되풀이하는 구간은 도돌이표로 묶인 마디, 끝부분은 코다, 파트의 시작은 상자 문자 A~D예요. 기호에는 언제나 한글 이름이 붙어서, 악보를 읽을 줄 몰라도 "지금 어디쯤인지"를 읽을 수 있어요.

화면은 평평해요. 그림자, 그라디언트, 둥근 카드가 없고, 글자 묶음은 상자 안이 아니라 기준선 위에 앉아요. 순위와 의미는 선의 굵기와 모양, 그리고 분필 색 세 가지(흰색, 노랑, 분홍)로만 나눠요. 색은 역할이 정해져 있고, 역할 밖에서는 쓰지 않아요.

밀도는 "한 화면에 메시지 하나"를 따라요. 큰 제목(84px, 900) 하나, 그 아래 기준선 줄 몇 개나 프롬프트 단 하나가 기본이에요. 악보 기호는 모두 직접 그린 SVG이고, 아이콘 세트는 쓰지 않아요.

이 이름과 아래 색 이름은 이번 기록에서 붙인 것이고, 진행자가 바꿀 수 있어요.

**Key Characteristics:**
- 맨 위 오선 띠가 길잡이: 장표 수만큼의 마디, 지금 마디만 칠함
- 분필 세 색: 흰색은 글, 노랑은 "지금·바꿔 쓸 자리·누를 것", 분홍은 "하지 마세요"
- 선 모양 = 사실의 확실도 (굵은 실선, 가는 실선, 끊긴 선)
- 상자·카드·그림자 없이 기준선 위에 앉은 줄
- 프롬프트는 왼쪽 브래킷으로 묶은 악보 한 단, 오른쪽 위에 노란 복사 버튼
- Noto Sans KR 한 벌(400·700·900), 오프라인용으로 파일 안에 넣음

## Colors

어두운 초록 칠판 하나에 분필 세 색을 올린, 역할이 엄격한 팔레트예요.

### Primary
- **노랑 분필** (yellow-chalk): 지금 위치(오선 띠의 현재 마디 칸), 참석자가 바꿔 쓸 자리(`[대괄호]` 글자와 그 밑줄), 누를 버튼(복사 버튼 바탕), 고른 예시 탭의 밑줄, 실습 표시(제목 옆 늘임표와 "실습 10분", 띠 아래 늘임표)에 써요. 키보드 포커스 테두리(3px 실선, 4px 띄움)와 글자 선택 바탕도 노랑이에요. 파트 A·B·C·D 오프너와 코다 오프너는 장표 전체를 노랑으로 칠해요.
- **밝은 노랑 분필** (yellow-chalk-hover): 복사 버튼에 마우스를 올렸을 때만 써요.

### Secondary
- **분홍 분필** (pink-chalk): 금지와 주의에만 써요. "금지 표현", "유료 플랜에서만 돼요", 바꾸기 전 문구의 취소선 같은 곳이에요. 체크 파트 오프너(금지 표현 장표)는 장표 전체를 분홍으로 칠해요.

### Neutral
- **음악실 칠판** (board): 모든 장표의 바탕. 노랑·분홍 전면 장표에서는 글자색이 돼요.
- **칠판 그늘** (board-deep): 장표(16:9 무대) 바깥 여백에만 써요. 장표 안에는 쓰지 않아요.
- **분필 흰색** (chalk): 제목과 본문 글자, 공식 안내 선, 복사 완료 버튼 바탕, QR 바탕.
- **흐린 분필** (chalk-dim): 보조 글(주석, 쪽 번호 줄, 범례, 지난 리허설 마크), 보고·확인 필요 선.
- **페인트 선** (paint): 오선, 마디줄, 기준선 줄의 보통 선. 의미 없는 구분선은 모두 이 색이에요.
- **노랑 위 흐린 글** (dim-on-yellow), **분홍 위 흐린 글** (dim-on-pink), **전면 위 페인트** (paint-on-fill): 노랑·분홍 전면 장표에서 흐린 분필과 페인트 선을 대신해요. 칠판색을 투명하게 깔아 만든 값이에요.

### Named Rules
**The 세 분필 Rule.** 노랑은 지금 위치, 바꿔 쓸 자리, 누를 버튼, 실습 표시(그리고 포커스 테두리)에만 써요. 분홍은 금지와 주의에만 써요. 강조하고 싶다는 이유만으로 노랑이나 분홍을 쓰지 않아요. 강조는 흰색 700으로 해요.

**The 전면 오프너 Rule.** 파트를 여는 장표만 한 색으로 전면을 칠해요. A~D와 코다는 노랑, 체크 파트는 분홍. 전면 장표에서는 글자, 지금 마디 칸, 늘임표, 포커스 테두리가 모두 칠판색으로 뒤집혀요.

**The 브랜드 색은 손님 Rule.** 가상 브랜드 예시 카드(루미엘, 골목 한그릇)는 각 브랜드 자신의 색으로 그려요. 그 색들은 이 시스템의 팔레트가 아니라 내용물이고, 세션 화면의 다른 곳에 쓰지 않아요. 카드 뉴스·릴스 완성 예시 자체는 이 시스템 전체(색, 글꼴, 모양, 규칙) 밖에 있고 각 브랜드의 모습을 따라요.

## Typography

**Display Font:** Noto Sans KR 900 (화면에서는 "Slide Sans"라는 이름으로 넣고, 없으면 Malgun Gothic, Apple SD Gothic Neo 순)
**Body Font:** Noto Sans KR 400·700 (같은 글꼴)

**Character:** 한 벌의 고딕을 무게 셋(400, 700, 900)으로만 나눠 써요. 칠판 글씨처럼 굵고 또렷한 900 제목과 담담한 400 본문의 대비가 전부예요.

장표 글꼴은 쓰인 글자만 잘라 파일 안에 넣어서(`font-display: block`) 인터넷 없이 열려요. 모든 글에 `word-break: keep-all`을 걸어 한국어 낱말이 중간에서 끊기지 않아요. 아래 크기는 1920×1080 무대 기준이고, 화면 크기에 맞춰 무대 전체가 함께 줄어들어요.

### Hierarchy
- **Cover Display** (900, 112px, 1.12): 표지 제목 한 곳.
- **Headline** (900, 84px, 1.15, -0.01em): 모든 장표 제목. 오선 띠 바로 아래 왼쪽에 놓고, 위에 작은 라벨을 달지 않아요.
- **Rehearsal Letter** (900, 104px, 1): 파트 오프너 오른쪽 위 상자 안의 A~D.
- **Diagram Node / Step** (900, 72px / 56px): 세 칸 흐름 그림의 마디 이름. 밑에 4px 실선을 그어요.
- **Lede** (400, 44px, 1.45): 제목 아래 한두 문장 설명.
- **Body / Row Label** (400 / 700, 36px, 1.5): 본문과 기준선 줄의 왼쪽 이름.
- **Step** (400, 32px, 1.5): 번호 단계. 번호는 900, 36px.
- **Table** (400, 30px, 1.45): 괘선 표 칸. 머리글은 700, 26px, 흐린 분필.
- **Note** (400, 26px): 주석, "2026년 10월 기준" 같은 기준 표시.
- **Prompt / Label** (400, 24px): 프롬프트 본문(같은 고딕, 고정폭 글꼴 쓰지 않음), 쪽 번호 줄, 범례.
- **Button** (700, 26px): 복사 버튼.
- **Strip Mark** (700, 24px): 오선 띠 위 파트 이름과 작은 복사 버튼.

### Named Rules
**The 한 벌 Rule.** 글꼴은 Noto Sans KR 하나뿐이에요. 프롬프트도 고정폭이 아니라 같은 고딕으로 써요. 위계는 크기와 400·700·900 무게로만 나눠요.

## Layout

장표는 1920×1080 고정 무대에 그리고, 창 크기에 맞춰 비율을 지키며 통째로 줄이거나 늘려요. 좌우 여백은 96px, 위에서 84px에 오선 띠(높이 64px, 폭 1728px)가 있고, 본문은 196px에서 시작해 아래 120px을 비워요. 쪽 번호 줄("A 카드 뉴스 · 5~35분 · 10 / 33")은 오른쪽 아래 44px에 한 줄로 놓아요.

본문은 제목 아래 56px에서 시작해요. 두 단일 때는 왼쪽 단계 열과 오른쪽 프롬프트 단을 72px 간격으로 나누고, 기준선 줄은 왼쪽 이름 칸과 오른쪽 설명 칸을 48px 간격으로 나눠요. 줄 하나는 위 24px, 아래 22px 여백과 아래 선 하나로 이뤄져요.

### Named Rules
**The 기준선 Rule.** 글 묶음은 상자 안에 넣지 않고 기준선 위에 앉혀요. 줄과 줄은 아래 선 하나로 나눠요. 선의 모양이 그 줄의 의미예요(Components의 확실도 선 참고).

**The 한 장 한 페이지 Rule.** 인쇄하면 장표 한 장이 한 페이지(1920×1080, 여백 0)가 되고, 색은 화면 그대로 찍혀요. 복사 버튼과 화면 읽기 전용 글은 인쇄에서 숨기고, 지금 마디 칸은 움직임 없이 제자리에 찍혀요.

### 실습 페이지에 옮길 때

실습 페이지(`practice/index.html`)는 노트북과 휴대폰에서 스크롤하며 읽는 웹 페이지라서 16:9 무대가 아니에요. 아래는 장표에서 가져갈 것과 새로 정해야 할 것을 나눈 것이고, 새로 정할 값은 그 페이지를 만들기 전에 이 문서에 먼저 더해요.

**그대로 가져가요:** 칠판·분필 색과 색 역할(세 분필 규칙, 칠판 그늘은 바깥 여백에만. 단, 전면 장표용 흐린 색 dim-on-yellow·dim-on-pink는 1920 무대의 24px 이상 글자 전용이라 실습 페이지 본문에는 쓰지 않아요), 확실도 선 세 가지와 범례, 프롬프트 브래킷 단과 노랑 슬롯 표시, 복사 버튼의 모양·상태·실패 문구, 직각과 평평함(그림자 없음), Noto Sans KR 한 벌 400·700·900과 `word-break: keep-all`, 파트 문자 A~D와 한글 이름, 직접 그린 악보 기호, 노랑 포커스 테두리, 동작 줄이기 존중.

**새로 정해야 해요 (아직 값 없음):** 이 문서의 px 값은 모두 1920 무대를 통째로 줄이는 전제라 웹 페이지에 그대로 옮기면 안 돼요. 웹 글자 크기 단계(본문 16px 이상, PRODUCT.md), 375px 폭에서 가로 스크롤 없는 배치, 프롬프트 단과 복사 버튼의 좁은 화면 배치, 그리고 길잡이를 정해야 해요. 장표 한 장 = 마디 하나인 오선 띠는 스크롤 페이지에 그대로 맞지 않으니, 실습 단위로 어떻게 옮길지(또는 쓰지 않을지)를 정해 이 문서에 더해요. 전면 노랑·분홍 장표를 웹 구획에 쓸지도 정해지지 않았어요.

## Elevation & Depth

그림자와 그라디언트가 하나도 없는 완전히 평평한 칠판이에요. 깊이는 쓰지 않고, 구분은 선(굵기와 모양)과 분필 색, 그리고 노랑·분홍 전면 장표의 색면 전환으로만 만들어요.

### Named Rules
**The 칠판은 평평하다 Rule.** 그림자, 흐림, 빛 번짐, 그라디언트를 쓰지 않아요. 떠 보이게 하고 싶을 때는 선을 굵게 하거나 색면을 바꿔요.

## Shapes

모서리는 모두 직각이에요(0). 둥근 곳은 프롬프트 브래킷의 위아래 갈고리(16px 곡선)와 도돌이표의 점(원)뿐이에요. 테두리 상자는 의미가 있을 때만 그려요: 리허설 문자 상자, 체크 칸, 복사 버튼 색면, 카드 규격(4:5) 그림, QR 자리(배포 전에는 끊긴 선), 장면 계획표 칸, 가상 브랜드 예시 카드. 내용 줄을 담는 상자나 카드는 그리지 않아요.

## Components

### Buttons (복사 버튼)
누르면 바로 복사되는, 이 세계에서 유일하게 색면으로 칠한 부품이에요.
- **Shape:** 직각(0).
- **Primary:** 노랑 분필 바탕에 칠판색 글자, 700 26px, 안쪽 여백 10px 30px. 프롬프트 단 머리줄 오른쪽 끝에 놓아요.
- **Hover / Focus:** 마우스를 올리면 밝은 노랑. 키보드 포커스는 노랑 3px 테두리를 4px 띄워 둘러요.
- **Done:** 복사하면 1.8초 동안 분필 흰색 바탕에 "복사했어요"로 바뀌어요. 실패하면 4초 동안 "복사가 안 됐어요. 글자를 끌어 선택해 복사해 주세요"를 보여 줘요.
- **Small:** 한 줄짜리 고쳐 달라는 문장 옆에는 24px, 여백 6px 20px의 작은 복사 버튼을 써요.
- **Print:** 인쇄와 PDF에서는 숨겨요.

### 프롬프트 단 (Signature)
Claude에게 보낼 문장을 악보 한 단처럼 왼쪽 브래킷으로 묶어요.
- **Bracket:** 왼쪽에 7px 굵은 세로 막대, 위아래에 4px 선으로 그린 갈고리(26×14px, 바깥 모서리 16px 곡선). 색은 글자색을 따라가요. 글은 44px 들여 써요.
- **Header:** 왼쪽에 단 이름(700, 30px)과 흐린 설명(24px), 오른쪽에 복사 버튼.
- **Body:** 같은 고딕 400, 기본 24px(글이 짧으면 30px까지), 줄 높이 1.5, 줄바꿈 유지.
- **Slot:** 바꿔 쓸 `[대괄호]` 자리는 노랑 글자에 노랑 2px 밑줄. 단계 설명 안에서 같은 자리를 가리킬 때도 같은 모양이에요.
- **Stacking:** 단이 여러 개면 40px 간격으로 쌓아요.
- **예시 탭:** `[대괄호]`가 있는 단은 머리 줄에 글자 탭 두 개("빈칸", "예시: 골목 한그릇")를 두고 빈칸판과 예시판을 바꿔 봐요. 탭은 흐린 분필 24px 글자, 고른 탭은 글자색과 노랑 3px 밑줄(지금 위치 규칙). 예시판에서 채운 값은 대괄호 없이 slot과 같은 노랑 글자·밑줄이에요. 복사 버튼은 보이는 판을 복사하고, 키보드 E는 그 장표의 단을 모두 함께 바꿔요. 인쇄에서는 탭을 숨기고 빈칸판만 찍어요.

### 확실도 선 (Certainty Lines)
줄 아래 선의 모양이 사실이 얼마나 확실한지를 말해요. 굵은 실선, 가는 실선, 끊긴 선 세 가지예요.
- **공식 안내:** 3px 실선, 글자색(칠판에서는 분필 흰색, 전면 장표에서는 칠판색).
- **이런 보고가 있어요:** 1px 실선, 흐린 분필.
- **[확인 필요]:** 2px 끊긴 선, 흐린 분필. 문장 안의 `[확인 필요]` 글자에도 같은 끊긴 밑줄을 그어요.
- **보통 줄:** 의미 없는 구분은 2px 페인트 선이에요.
- **Legend:** 확실도 선을 쓴 장표에는 오른쪽 아래(쪽 번호 줄 왼쪽)에 48px 선 견본과 이름("공식 안내", "이런 보고가 있어요", "확인 필요")을 흐린 24px로 달아요. 표 칸에도 같은 선을 써요.
- **TODO:** 진행자가 확정할 자리는 흐린 26px 글에 2px 끊긴 밑줄로 남겨요.

### Navigation (오선 띠)
장표 수만큼의 마디로 그은 오선이 모든 장표 맨 위에 있어요. 마디를 누르면 그 장표로 가요.
- **Staff:** 페인트 2px 선 다섯 줄, 마디줄은 2px 페인트 선, 마지막 마디는 7px 겹세로줄(끝마침표).
- **Current:** 지금 마디는 노랑 분필로 칠한 칸(마디 폭 - 6px, 높이 60px). 전면 장표에서는 칠판색 칸이에요. 마디 위에 마우스를 올리면 칠판 장표에서는 분필 흰색 12%, 전면 장표에서는 칠판색 14% 칸이 비쳐요.
- **Rehearsal Marks:** 각 파트가 시작하는 마디 위에 2px 테두리 36px 상자 속 글자(A~D, 24px)와 한글 이름(700, 24px). 시작·체크에는 상자 없이 이름만, 마무리는 그린 코다 기호와 이름. 지난 파트의 마크는 흐린 분필로 바래요.
- **Fermata:** 실습 장표 마디 아래에 거꾸로 건 늘임표(30×18px), 노랑 분필. 실습 장표 제목 오른쪽에도 늘임표와 "실습 N분"을 노랑 700 36px로 달아요.
- **Repeat:** 매일 반복(예약 작업) 파트의 처음과 끝 마디에 도돌이표(6px 막대와 점 두 개).
- **Keyboard:** ←/→, PageUp/PageDown, 스페이스, Home/End로 넘기고 F로 전체 화면. 주소 끝 `#번호`로 그 장표를 열어요.
- **Motion:** 바로 옆 장표로 넘길 때만 지금 칸이 320ms 동안 한 마디 미끄러져요. 건너뛰기, 주소 이동, 동작 줄이기 설정에서는 즉시 옮겨요. 이 화면에서 움직이는 것은 이 칸 하나뿐이에요.

### 리허설 문자 (파트 오프너)
- 파트 오프너 오른쪽 위(위 192px, 오른쪽 96px)에 8px 테두리의 150px 정사각형, 안에 900 104px 글자. 코다 오프너는 테두리 없이 그린 코다 기호를 같은 크기로 놓아요.
- 같은 상자 문자가 크기만 바꿔 "오늘 만들 것" 목록(72px, 3px 테두리)과 마무리 체크 목록(52px, 3px 테두리)에 다시 나와요.

### 흐름 그림
세 칸을 화살표(직접 그린 SVG)로 잇고, 각 칸 이름 아래에 4px 실선을 그어요. 아이콘이나 상자 없이 굵은 글자와 선만으로 그려요.

## Do's and Don'ts

### Do:
- **Do** 모든 장표 맨 위에 오선 띠를 두고, 지금 마디만 노랑으로 칠해요.
- **Do** 파트에는 상자 문자 A~D와 한글 이름을 함께 붙여요. 기호(늘임표, 도돌이표, 코다)에도 처음 나올 때 한글 이름을 달아요.
- **Do** 사실의 확실도를 선 모양으로 나눠요: 공식 3px 실선, 보고 1px 흐린 실선, [확인 필요] 2px 흐린 끊긴 선. 그 장표에 범례를 달아요.
- **Do** 프롬프트는 왼쪽 브래킷 단에 넣고, 오른쪽 위에 노란 복사 버튼을, 바꿔 쓸 자리는 노랑 글자와 밑줄로 표시해요.
- **Do** 악보 기호와 화살표는 currentColor로 그린 SVG로 넣어요.
- **Do** 동작 줄이기 설정을 지키고, 인쇄에서는 한 장 한 페이지로, 복사 버튼은 숨겨요.

### Don't:
- **Don't** 노랑을 강조색으로 쓰지 마세요. 지금 위치, 바꿔 쓸 자리, 누를 버튼, 실습 표시, 포커스 테두리에만 써요.
- **Don't** 분홍을 금지·주의 밖에서 쓰지 마세요.
- **Don't** 내용 줄을 상자나 카드에 넣거나, 그림자·그라디언트를 쓰지 마세요. 버튼, 줄, 면의 모서리는 직각이에요. 곡선은 프롬프트 브래킷 갈고리와 악보 기호의 점·호에만 있어요.
- **Don't** 아이콘 세트, 이모지, 글리프 아이콘을 쓰지 마세요. 필요한 기호는 직접 그려요.
- **Don't** 제목 위에 작은 라벨(키커)을 달지 마세요.
- **Don't** 두 번째 글꼴(고정폭 포함)을 들이지 마세요.
