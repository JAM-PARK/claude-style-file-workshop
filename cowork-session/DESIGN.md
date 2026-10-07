---
name: Cowork 입문 세션
description: 가게 유리문에 테이프로 붙인 A4 안내문. 장표, 실습 페이지, 치트시트가 함께 따르는 한 장의 규칙
colors:
  glass: "#2E3532"
  vinyl: "#F2F4F2"
  vinyl-dim: "#A9B2AE"
  paper: "#FFFFFF"
  ink: "#141414"
  red: "#D2261C"
  tape: "rgba(240, 238, 222, 0.72)"
typography:
  display-lead:
    fontFamily: '"CW Display", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "104px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.015em"
  display:
    fontFamily: '"CW Display", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "84px"
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  headline:
    fontFamily: '"CW Display", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "80px"
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  headline-portrait:
    fontFamily: '"CW Display", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "68px"
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  title:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "44px"
    fontWeight: 700
    lineHeight: 1.5
  body:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "42px"
    fontWeight: 400
    lineHeight: 1.6
  row:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "44px"
    fontWeight: 400
    lineHeight: 1.5
  row-title:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "48px"
    fontWeight: 800
    lineHeight: 1.5
  formula-label:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "42px"
    fontWeight: 800
    lineHeight: 1.4
  formula-value:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "46px"
    fontWeight: 700
    lineHeight: 1.4
  warning-row:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "52px"
    fontWeight: 800
    lineHeight: 1.4
  coupon:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "36px"
    fontWeight: 700
    lineHeight: 1.5
  label:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1.3
    fontFeature: '"tnum"'
  door:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "28px"
    fontWeight: 400
    lineHeight: 1.3
    fontFeature: '"tnum"'
  timer:
    fontFamily: '"CW Display", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "240px"
    fontWeight: 400
    lineHeight: 1
    fontFeature: '"tnum"'
  notes:
    fontFamily: '"CW Gothic", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif'
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.55
rounded:
  none: "0px"
spacing:
  hair: "4px"
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "32px"
  xl: "48px"
  2xl: "64px"
  sheet-x: "80px"
components:
  notice-sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "56px 80px 64px"
    width: "1400px"
    height: "968px"
  notice-sheet-portrait:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "48px 56px 56px"
    width: "660px"
    height: "952px"
  notice-sheet-small:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "56px 80px"
    width: "1000px"
    height: "700px"
  notice-head:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "0 0 16px"
  ink-plate:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "2px 16px 4px"
  ink-plate-block:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "16px 24px"
  tape:
    backgroundColor: "{colors.tape}"
    width: "168px"
    height: "48px"
  coupon:
    textColor: "{colors.ink}"
    typography: "{typography.coupon}"
    padding: "24px 0 0"
  formula-row:
    textColor: "{colors.ink}"
    typography: "{typography.formula-value}"
    padding: "12px 0"
    height: "100px"
  ruled-row:
    textColor: "{colors.ink}"
    typography: "{typography.row}"
    padding: "32px 0"
  warning-row:
    textColor: "{colors.ink}"
    typography: "{typography.warning-row}"
    padding: "32px 0"
  check-mark:
    textColor: "{colors.red}"
  tear-strip:
    textColor: "{colors.ink}"
    height: "312px"
    padding: "24px 12px 0"
  tear-strip-gone:
    backgroundColor: "{colors.glass}"
  door-schedule:
    textColor: "{colors.vinyl-dim}"
    typography: "{typography.door}"
    width: "320px"
  door-schedule-now:
    textColor: "{colors.vinyl}"
  break-timer:
    textColor: "{colors.ink}"
    typography: "{typography.timer}"
  break-timer-done:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    padding: "40px 32px"
  presenter-notes:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.notes}"
    padding: "20px 32px 24px"
---

# Design System: Cowork 입문 세션

## Overview

**Creative North Star: "가게 유리문 안내문"**

사장님이 가게 유리문 안쪽에 테이프로 붙여 두는 A4 안내문이 이 세계의 전부다. 짙은 녹회색 유리 위에 흰 종이가 한 장씩 붙고, 종이에는 먹 글씨로 오늘 할 일이 적힌다. 가져갈 문장은 전단 아래 칼집 낸 쪽지처럼 "뜯어가는" 모양으로 둔다. 유리 오른쪽에는 영업시간 시트지처럼 90분 진행표가 흰 글자로 붙어 있고, 지금 구간만 굵게 보인다.

화면은 강의 장표가 아니라 붙여 둔 공지처럼 읽혀야 한다. 제목은 왼쪽 위에서 시작하고, 내용은 괘선(종이에 그은 가로줄)으로 나눈다. 강조는 색이 아니라 먹을 뒤집은 검은 판 하나로 한다. 빨강은 "멈춰서 보라"는 뜻에만 남겨 둔다. 그림자, 둥근 모서리, 카드 격자, 가운데 정렬 큰 제목, 기술 행사 키노트 같은 장표는 이 세계에 없다.

이 문서는 다 만든 장표(`slides/index.html`)에서 실제로 쓴 값만 적었다. 아직 만들지 않은 실습 페이지와 치트시트에 대한 내용은 장표와 방향 계약이 뒷받침하는 만큼만 적고, 그런 문장에는 **(미검증: 아직 만들지 않음)** 표시를 붙인다. 이 표시는 제품 사실이 불확실하다는 뜻의 `[확인 필요]`와 다르다. `[확인 필요]`는 화면에 빨강으로 찍히는 내용 표시이고, (미검증)은 디자인 규칙이 아직 실제 화면으로 검증되지 않았다는 이 문서 안의 표시다.

용어: 이 문서에서 **토큰**은 색이나 크기 같은 디자인 값에 붙인 이름이다(예: `ink`는 #141414). 맨 위 YAML 머리말(`---` 사이의 기계용 목록)에 적힌 값이 기준이고, 본문은 그 값을 어디에 왜 쓰는지 설명한다. **px**은 화면 점 단위다. 장표의 px은 모두 1920×1080 판 기준이다(Layout 참고).

**Key Characteristics:**
- 짙은 녹회색 유리(바탕) 위에 흰 A4 종이, 먹 글씨. 종이 안의 색은 흰색, 먹, 빨강뿐이다.
- 강조는 먹을 뒤집은 검은 판 하나. 한 화면에 많아야 하나다.
- 빨강은 주의, 금지, `[확인 필요]`에만 쓴다.
- 모든 안내문 맨 위에 같은 세 칸짜리 머리 칸과 굵은 먹 괘선이 있다.
- 기울어지는 것은 반투명 테이프뿐이다. 종이와 글자는 수평이다.
- 그림자, 둥근 모서리, 카드가 없다. 깊이는 유리와 종이의 밝기 차이와 테이프가 겹친 자리로만 보인다.
- 점선은 "뜯는 선"과 "채울 자리"에만 쓴다.

## Colors

어두운 유리, 흰 종이, 먹, 그리고 아껴 쓰는 빨강 한 가지. 장식용 색은 없다.

### Primary
- **먹 (Ink)** (`ink`): 종이 위 모든 글씨, 괘선, 그리고 강조 판의 바탕. 이 세계의 주인공 색이다. 강조는 먹을 뒤집은 판(먹 바탕에 흰 글씨)으로 한다. 종이 대비 18.4:1.

### Semantic (주의 전용)
- **주의 빨강 (Warning Red)** (`red`): "브랜드 색"이나 강조색이 아니다. 주의, 금지, `[확인 필요]` 표시에만 쓴다. 장표에서는 `[확인 필요]` 글자, "맡기면 안 되는 일" 표의 4px 윗괘선과 X 표시가 전부다. 흰 종이 위 대비 5.21:1(WCAG AA 통과. WCAG AA는 글자가 바탕과 충분히 구분되는지 보는 국제 접근성 기준이다).

### Neutral
- **유리문 (Door Glass)** (`glass`): 모든 화면의 바탕. 짙은 녹회색이라 파랑·남색 계열로 읽히지 않는다. 표지·마무리의 뜯겨 나간 쪽지 자리에도 이 색이 보인다(종이가 뜯겨 유리가 비친 것).
- **종이 (Paper)** (`paper`): 안내문 종이, 진행자 노트 패널, 강조 판 위의 글씨.
- **시트지 흰색 (Vinyl White)** (`vinyl`): 유리에 붙은 진행표의 제목과 "지금 구간" 글자. 유리 대비 11.4:1.
- **흐린 시트지 (Faded Vinyl)** (`vinyl-dim`): 진행표의 지나갔거나 아직인 구간. 이 문서의 유일한 회색이며 유리 위에서만 쓴다. 유리 대비 5.78:1(AA).
- **테이프 (Tape)** (`tape`): 종이 귀퉁이를 붙인 반투명 테이프. 이 세계에서 유일하게 투명도가 있는 색이다. 실제로 보이는 색은 유리 위에서 약 #BABAAE, 종이 위에서 약 #F4F3E7이다(렌더링 결과일 뿐 따로 쓰는 토큰이 아니다).

### Named Rules
**The One Plate Rule (먹 판 하나).** 한 화면에 먹을 뒤집은 판은 많아야 하나다. 판이 없는 화면도 있다(휴식 타이머가 도는 동안). 공식 장표(9번, 16번)에서는 판이 단계를 따라 움직인다. 0단계에서는 첫 칸 이름("무엇을", "언제")에, 그다음엔 방금 채운 값에, 마지막엔 뜯어가는 문장에 판이 놓인다. 세로 안내문 두 장을 나란히 붙인 화면에서는 오른쪽 종이에만 판이 있다.

**The Red Means Stop Rule (빨강은 멈춤).** 빨강은 주의, 금지, `[확인 필요]`에만 쓴다. 제목 강조, 숫자 강조, 버튼, 링크에 빨강을 쓰지 않는다.

**The Gray Stays On Glass Rule (회색은 유리에만).** 종이 안에는 흰색, 먹, 빨강만 있다. 회색 글씨나 회색 괘선을 종이 안에 넣지 않는다. 흐린 시트지 색은 유리 위 진행표에서만 쓴다.

**The Seven Colors Rule (색은 일곱 개).** 머리말의 일곱 값만 쓴다. 디자인 도구용 부속 파일(`.impeccable/design.json`)에 있는 단계별 색 띠는 견본으로 보여 주는 용도일 뿐, 그 안의 중간 회색을 화면에 쓰면 안 된다.

## Typography

**Display Font:** CW Display (Black Han Sans의 서브셋, OFL 라이선스) / 대체: Apple SD Gothic Neo, Malgun Gothic, sans-serif
**Body Font:** CW Gothic (Nanum Gothic 400·700·800의 서브셋, OFL 라이선스) / 대체: 같음

**Character:** 굵고 단단한 간판 글씨(제목)와 반듯한 공문 글씨(본문)의 짝. 가게 앞 손글씨 대신 인쇄소에서 뽑은 안내문처럼 보인다.

서브셋은 장표에 실제로 쓰인 글자만 남겨 잘라 낸 폰트 파일이다. 장표는 인터넷 없이 열려야 해서 `tools/build.py`가 이 서브셋을 base64(파일을 글자로 바꿔 HTML 안에 넣는 방식)로 장표 안에 넣는다. 원본 폰트는 `tools/fetch-fonts.sh`가 받는다. OFL은 무료로 쓰고 고쳐 배포할 수 있는 폰트 라이선스다. Nanum Gothic의 OFL에는 예약 이름(Reserved Font Name) 조항이 있어, 잘라 낸 파일에 원래 이름을 쓸 수 없다. 그래서 "CW Gothic"으로 바꿨다. Black Han Sans의 OFL에는 예약 이름이 없지만, 두 서브셋의 이름을 맞추려고 "CW Display"로 바꿨다. 장표 글을 고친 뒤에는 반드시 다시 빌드한다.

### Hierarchy
아래 크기는 모두 1920×1080 장표 판 기준이다.
- **Display Lead** (CW Display 400, 104px, 줄간격 1.2, 자간 -0.015em): 한 장에 한 문장만 크게 거는 장(훅 질문, 결론 문장).
- **Display** (CW Display 400, 84px, 1.25): 표지 훅 제목, 휴식 장 제목.
- **Headline** (CW Display 400, 80px, 1.25, 아래 여백 48px): 보통 안내문의 제목. 세로 안내문에서는 68px(아래 여백 40px).
- **Title** (CW Gothic 700, 44px, 1.5): 큰 제목 아래 부제 한 줄.
- **Body** (CW Gothic 400, 42px, 1.6): 문단. 문단 사이 32px.
- **Row / Row Title** (CW Gothic 400 44px / 800 48px, 1.5): 괘선 줄 목록. 이름표 줄은 40px, 설명 줄은 38px까지 줄인다.
- **Formula Label / Value** (CW Gothic 800 42px / 700 46px, 1.4): 문장 공식 양식의 칸 이름과 채운 값.
- **Warning Row** (CW Gothic 800, 52px, 1.4): "맡기면 안 되는 일" 표.
- **Coupon** (CW Gothic 700, 36px, 1.5): 절취선 아래 뜯어가는 문장.
- **Label** (CW Gothic 700, 28px, 1.3, 숫자 폭 고정): 머리 칸, 쪽지 이름표. QR 설명도 같은 28px이지만 400(줄간격 1.4)이다. 장표에서 가장 작은 글자다.
- **Door** (CW Gothic 400, 28px, 1.3, 숫자 폭 고정): 유리 진행표. 지금 구간만 800. 진행표 제목은 CW Display 40px.
- **Timer** (CW Display 400, 240px, 1, 숫자 폭 고정): 휴식 타이머. 끝나면 120px "다시 시작합니다"로 바뀐다.
- **Notes** (CW Gothic 400, 24px, 1.55): 진행자 노트 패널. 진행자만 보는 패널이라 28px 기준의 예외다. 이 패널은 장표 판 밖에 있어 24px이 판 기준이 아니라 실제 화면 px이다(1366 화면에서도 줄지 않는다).

한국어 줄바꿈은 낱말 단위로 끊고(`word-break: keep-all`), 제목과 부제는 줄 길이를 고르게 맞춘다(`text-wrap: balance`).

### Named Rules
**The Two Voices Rule (목소리 둘).** CW Display는 제목, 한 줄 결론, 큰 숫자(줄 번호, 타이머)에만 쓴다. 문단, 머리 칸, 표, 쪽지는 CW Gothic이다. CW Display는 굵기가 하나뿐이니 굵게 만들지 않는다.

**The 28px Floor Rule (28px 바닥).** 참석자가 보는 장표 글자는 1920 판 기준 28px 이상이다. 1366×768 화면에서는 판 전체가 약 0.71배로 줄어 28px이 약 20px로 보인다. 그래서 28px보다 작게 만들 여유가 없다.

**The Bold Is 800 Rule (굵게는 800).** 본문 속 강조 낱말(`b`, `strong`)은 800으로 한다. 700은 부제, 머리 칸, 쪽지처럼 한 줄 전체가 굵은 자리에 쓴다.

## Layout

**장표 판.** 모든 장표는 1920×1080 판 하나로 그리고, 화면 크기에 맞춰 판 전체를 같은 비율로 줄이거나 늘린다(1366×768에서 약 0.71배). 글자가 다시 흐르지 않으니 두 해상도에서 줄바꿈이 같다. 바탕 유리는 화면 끝까지 채운다.

**유리 진행표.** 모든 장의 오른쪽 유리(x 1544px, 위 96px, 폭 320px)에 같은 진행표가 붙어 있다. 7개 구간과 "1:30 끝". 지금 구간만 시트지 흰색 800, 나머지는 흐린 시트지. 부록 장에서는 끝줄이 "부록: 질문 나올 때만"으로 바뀌고 굵은 줄이 없다.

**여백 리듬.** 기본은 8px 배수다(8, 16, 24, 32, 48, 64, 80). 괘선 두께와 판 안쪽 위아래 여백에는 4px 반 단계를 쓴다. 12px(공식 줄 위아래, 쪽지 옆), 20px(세로 안내문 머리 칸 간격), 28px(이름표 줄 위아래)이 몇 군데 있으나 반복 규칙은 아니다. 새 화면에서는 머리말의 spacing 값을 쓴다.

**정렬.** 모든 제목과 문단은 왼쪽 정렬, 한 단이다. 가운데 정렬은 세로쓰기 쪽지와 QR 자리 안 글씨뿐이다.

### 장표 레이아웃 다섯 가지 (만든 그대로)
1. **가로 안내문** (1400×968, 왼쪽 80px·위 56px, 안쪽 여백 56/80/64px): 기본 장. 테이프 네 귀퉁이. 머리 칸, 제목, 본문이나 줄 목록. 한 문장짜리 장은 Display Lead와 부제만 둔다. QR이 있는 장은 오른쪽에 260px 열을 두고 64px 띄운다.
2. **세로 안내문 두 장** (각 660×952, x 80px과 804px, 사이 64px, 안쪽 여백 48/56/56px): 비교 장(Chat과 Cowork, 맡기기 전과 후). 테이프는 바깥 위 귀퉁이 하나와 위 가운데 하나. 두 장 모두 머리 칸이 같고, 먹 판은 오른쪽 종이에만 있다. 사진 붙일 자리는 남은 높이를 채우는 점선 칸이다.
3. **작은 안내문과 휴식 타이머** (1000×700, 왼쪽 240px·위 180px): 휴식 장. 제목 아래 240px 타이머. 끝나면 타이머 자리가 먹 판("다시 시작합니다")으로 바뀐다. 소리는 없다.
4. **문장 공식 양식과 절취선 쪽지** (가로 안내문 안): 4px 먹 윗괘선 아래 네 줄. 왼쪽 360px 칸 이름("+"로 이어 붙임), 오른쪽은 3px 먹 밑줄이 그어진 빈칸. 화살표 키를 누를 때마다 한 칸씩 채워지고, 다 채우면 종이 맨 아래 절취선 쪽지가 나타난다.
5. **괘선 줄 목록** (가로 안내문 안): 번호 줄(왼쪽 104px에 CW Display 64px 숫자), 이름과 설명 줄, 이름표 줄(300px 이름 칸). 줄마다 2px 먹 윗괘선, 마지막 줄에 아랫괘선. 변형으로 **금지 표**가 있다. 윗괘선이 4px 빨강, 줄 앞에 빨강 X, 글자 52px 800.

표지와 마무리 장의 가로 안내문은 아래쪽에 뜯는 쪽지 줄을 두기 때문에 위 귀퉁이 테이프 둘만 붙인다.

### 다른 화면으로 옮길 때
아래는 장표와 방향 계약에서 끌어낸 번역이다. 실제 화면으로 확인하기 전까지는 모두 (미검증: 아직 만들지 않음)이다.

**실습 페이지** (`practice-page/index.html`, 휴대폰 375px 이상과 노트북) (미검증: 아직 만들지 않음)
- 페이지 바탕이 유리, 구간마다 흰 안내문 한 장. 안내문마다 장표와 같은 세 칸 머리 칸을 둔다.
- HANDOFF의 "미션 카드 4종"은 카드가 아니라 **안내문 네 장**으로 만든다. 각 장은 목표, 뜯어가는 문장(절취선 쪽지), 잘 됐는지 확인하는 법 순서다.
- 프롬프트는 모두 절취선 쪽지이고, 복사 버튼은 쪽지를 "뜯는" 동작이다. 누른 뒤 어떻게 보일지는 정하지 않았다.
- 장표의 px 숫자를 그대로 가져오지 않는다. 장표는 판째 줄어드는 화면이고, 실습 페이지는 글이 다시 흐르는 화면이다. 본문은 16px 이상, 375px 폭에서 가로 스크롤이 없어야 한다.
- 장표 테이프는 종이 밖으로 64px 삐져나온다. 휴대폰에 그대로 옮기면 가로 스크롤이 생긴다. 테이프를 어떻게 줄일지는 아직 풀지 않았다.
- 장표는 화면 밖을 잘라 고정한다(`overflow: hidden`). 스크롤하는 페이지에는 이 설정을 가져오지 않는다.
- 폰트는 Google Fonts 링크로 원래 이름(Black Han Sans, Nanum Gothic)을 불러오고 대체 폰트를 지정한다. "CW" 이름은 장표에 넣은 서브셋에만 쓴다.
- 진행표는 유리 위 시트지 글씨로 짧게 둘 수 있다. 위치는 정하지 않았다.

**치트시트** (`comms/cheat-sheet.html`, A4 한 장 인쇄) (미검증: 아직 만들지 않음)
- 유리 없이 종이 안내문 한 장이다. 인쇄면이 곧 종이다.
- 같은 머리 칸, 문장 공식 두 개(양식), 뜯어가는 문장 예시 세 개(절취선 쪽지), 맡기면 안 되는 일(금지 표).
- 테이프와 진행표는 유리에 속한 것이라 넣지 않는다.
- 색은 흰색, 먹, 빨강뿐이다. 인쇄용 글자 크기는 아직 정하지 않았다.

## Elevation & Depth

이 세계는 평평하다. 그림자도, 겹겹이 뜬 층도 없다. 깊이는 세 가지로만 보인다. 어두운 유리와 흰 종이의 밝기 차이, 종이 귀퉁이를 덮은 반투명 테이프, 그리고 표지·마무리의 쪽지가 뜯겨 유리가 비치는 빈칸이다. 진행자 노트 패널도 그림자 없이 4px 먹 윗괘선으로만 구분한다.

### Named Rules
**The Tape Is The Only Tilt Rule (기우는 건 테이프뿐).** 기울어지는 요소는 테이프뿐이다. 귀퉁이 테이프는 약 ±38도, 위 가운데 테이프는 0도에서 장마다 ±4도 안쪽으로 조금씩 다르게 붙는다(폭 150~186px, 같은 장은 늘 같은 모양). 종이, 제목, 판, 사진 자리는 기울이지 않는다.

**The No Shadow Rule (그림자 없음).** 종이가 유리에서 떠 보이게 하려고 그림자를 넣지 않는다. 테이프가 이미 "붙어 있다"는 사실을 말해 준다.

## Shapes

모든 모서리는 직각(0px)이다. 둥근 모서리는 어디에도 없다. 형태는 종이 사각형과 그 안의 가로 괘선으로 만든다.

선은 굵기마다 뜻이 있다.
- **4px 먹 실선:** 머리 칸 아래, 공식 양식 위, 진행자 노트 위. 구역의 시작을 알린다.
- **4px 빨강 실선:** 금지 표 위. 빨강 선은 이것 하나다.
- **3px 먹 실선:** 공식 양식의 빈칸 밑줄.
- **2px 먹 실선:** 줄 목록 사이 괘선.
- **4px 먹 점선:** 절취선, 쪽지 줄 위쪽 칼집.
- **3px 먹 점선:** 쪽지 사이 칼집, 진행자가 채울 빈칸 밑줄, 사진 붙일 자리, QR 자리.

### Named Rules
**The Dashed Means Cut-or-Fill Rule (점선은 뜯거나 채우거나).** 점선은 "여기를 뜯어 가세요"(절취선, 쪽지)와 "여기를 채울 겁니다"(진행자 기입 빈칸, 사진 자리, QR 자리)에만 쓴다. 장식용 점선은 없다.

**The Ruled Not Boxed Rule (상자 말고 괘선).** 종이 안에서 내용을 묶으려고 실선 상자를 두르지 않는다. 가로 괘선으로 나눈다. 종이 안에서 테두리가 있는 칸은 점선으로 된 "채울 자리"뿐이다.

## Components

### 안내문 종이 (Notice Sheet)
가로, 세로, 작은 크기 세 가지. 흰 종이, 직각, 그림자 없음, 귀퉁이에 테이프. 안쪽은 위에서부터 머리 칸, 제목, 내용 순서이고, 쪽지가 있으면 종이 맨 아래에 붙는다(남은 높이를 밀어내고 바닥에 닿는다).

### 머리 칸 (Notice Head)
모든 안내문의 같은 자리에 같은 세 칸이 있다. 왼쪽 세션 이름(700), 가운데 구간과 시간(400), 오른쪽 쪽 번호(700, 숫자 폭 고정). 28px, 아래 16px 띄우고 4px 먹 괘선, 그 아래 48px 띄운다. 변형은 둘이다. 표지는 가운데 칸이 진행자가 채울 점선 빈칸("일시·장소 [진행자 기입]")이고, 부록은 오른쪽 칸이 "질문 N"이다.

**The Same Three Cells Rule (같은 세 칸).** 머리 칸을 빼거나 칸 순서를 바꾸지 않는다. 참석자는 머리 칸만 보고 지금이 어느 구간 몇 쪽인지 안다.

### 먹 판 (Ink Plate)
먹 바탕, 흰 글씨, 직각. 글자 줄에 깔 때는 위아래 2/4px, 좌우 16px(공식 칸 이름에서는 12px)이고 줄이 바뀌어도 판이 끊기지 않는다. 문단 전체에 깔 때는 16/24px. 화면당 하나(The One Plate Rule).

### 절취선 쪽지 (Coupon)
4px 먹 점선 위에 "뜯어가는 문장"이나 "이렇게 말해 보세요" 이름표(28px 700, 흰 바탕으로 점선을 끊음)가 걸리고, 그 아래 36px 700 문장. 종이 맨 아래에 붙는다. 장표에서는 복사 기능이 없다. 실습 페이지에서 복사 버튼이 붙는 자리다(미검증: 아직 만들지 않음).

### 문장 공식 양식 (Formula Form)
4px 먹 윗괘선, 네 줄. 줄 높이는 최소 100px. 칸 이름은 42px 800, 둘째 줄부터 앞에 "+". 값 칸은 3px 먹 밑줄, 46px 700. 값은 단계마다 하나씩 나타나고 먹 판이 함께 움직인다.

### 괘선 줄 목록과 금지 표 (Ruled Rows, Warning Rows)
줄마다 2px 먹 괘선, 위아래 32px. 번호 줄은 순서가 있는 단계에만 쓴다. 금지 표는 4px 빨강 윗괘선과 줄 앞 48px 빨강 X를 쓴다. 이 X는 이 세계에서 유일하게 그려 넣은 표시이고, 금지 표에서만 쓴다. 다른 곳에 아이콘을 들이는 근거가 아니다.

### 뜯는 쪽지 줄 (Tear-off Strips)
표지와 마무리 장의 종이 맨 아래, 종이 폭 전체에 높이 312px로 10칸. 위쪽은 4px 먹 점선, 칸 사이는 3px 먹 점선. 칸마다 세로쓰기로 "실습 페이지"(30px 800)와 주소(28px 400). 몇 칸은 이미 뜯겨 나가 유리색이 보인다(표지 1칸, 마무리 3칸). 장식이 아니라 같은 주소의 반복이라, 화면 낭독기(글을 소리로 읽어 주는 프로그램)는 이 줄을 건너뛰게 해 두었다.

### 유리 진행표 (Door Schedule)
유리에 붙은 시트지 글씨. 제목 "진행 시간"은 CW Display 40px 시트지 흰색. 시간 열 96px, 28px, 줄 위아래 12px. 지금 구간만 시트지 흰색 800.

### 휴식 타이머 (Break Timer)
5:00부터 줄어드는 240px 숫자. Enter로 시작과 멈춤, R로 처음으로. 끝나면 먹 판 안 120px "다시 시작합니다"로 바뀐다. 소리는 없다.

### 표시 글자 (Check Mark, Blank)
`[확인 필요]`는 빨강 800, 줄바꿈 없이 붙인다. 진행자가 채울 값(`[진행자 기입]`)은 3px 먹 점선 밑줄과 700.

### 진행자 노트 (Presenter Notes)
N 키로 여닫는 화면 아래 패널. 흰 바탕, 4px 먹 윗괘선, 24px, 화면 높이의 42%까지. 첫 줄에 장 번호와 예상 시간을 굵게.

### 장 넘김과 단계
장을 넘기면 새 종이가 위에서 12px 내려오며 나타난다(180ms, 빠르게 시작해 천천히 멈춤). "안내문을 새로 붙이는" 짧은 동작이다. 운영체제의 "동작 줄이기" 설정이 켜져 있으면 이 동작을 없앤다. 단계(공식 칸 채우기, 4번 장 둘째 질문)는 동작 없이 바로 나타난다. 키보드: →, 스페이스, PageDown 다음 / ←, PageUp 이전 / Home, End / F 전체화면 / N 노트.

### 포커스
장표에는 키보드로 옮겨 다닐 버튼이나 링크가 없어 포커스 표시(키보드로 고른 요소를 보여 주는 테두리)를 정하지 않았다. 실습 페이지의 복사 버튼에는 꼭 필요하다. 먹은 유리 위에서 대비가 1.47:1밖에 안 되므로, 포커스 표시는 종이 위와 유리 위 양쪽에서 보여야 한다. 값은 아직 정하지 않았다(미검증: 아직 만들지 않음).

## Do's and Don'ts

### Do:
- **Do** 바탕은 유리(#2E3532), 내용은 그 위에 붙인 흰 종이 안에 둔다.
- **Do** 한 화면의 강조는 먹 판 하나로 하고, 공식 장에서는 판을 단계와 함께 옮긴다.
- **Do** 모든 안내문 맨 위에 같은 세 칸 머리 칸(세션 이름, 구간과 시간, 쪽 번호)과 4px 먹 괘선을 둔다.
- **Do** 가져갈 문장은 종이 맨 아래 4px 먹 점선 절취선 쪽지로 둔다.
- **Do** 내용은 가로 괘선(2px 먹)으로 나누고, 제목과 문단은 왼쪽 정렬로 둔다.
- **Do** 장표 글자는 1920 판 기준 28px 이상(진행자 노트 패널만 24px), 실습 페이지 본문은 16px 이상으로 한다.
- **Do** 글자 대비는 WCAG AA 이상으로 맞춘다(먹/종이 18.4, 빨강/종이 5.21, 흐린 시트지/유리 5.78).
- **Do** 장 넘김 동작은 운영체제의 동작 줄이기 설정을 따른다.
- **Do** 제목, 결론 문장, 큰 숫자는 CW Display, 나머지는 CW Gothic으로 쓴다.
- **Do** 장표 글을 고치면 `tools/build.py`로 폰트 서브셋을 다시 만든다.

### Don't:
- **Don't** 파랑, 남색, 보라 계열을 메인 컬러로 쓰지 않는다.
- **Don't** 보라에서 파랑으로 가는 그라디언트를 쓰지 않는다. 그라디언트 자체를 쓰지 않는다.
- **Don't** 둥근 카드, 그림자, 카드 격자를 쓰지 않는다. 모서리는 모두 직각이다.
- **Don't** 이모지나 아이콘을 쓰지 않는다. 금지 표의 빨강 X만 예외다.
- **Don't** 빨강을 강조나 장식에 쓰지 않는다. 주의, 금지, `[확인 필요]`에만 쓴다.
- **Don't** 회색을 종이 안에 넣지 않는다. 흐린 시트지 색은 유리 위 진행표에만 쓴다.
- **Don't** 한 화면에 먹 판을 둘 이상 두지 않는다.
- **Don't** 테이프 말고는 아무것도 기울이지 않는다.
- **Don't** 테이프 말고는 반투명 색을 쓰지 않는다. 장 넘김 때 종이가 잠깐 흐려졌다 나타나는 것은 동작이지 색이 아니라서 예외다.
- **Don't** 먹 글씨를 유리 위에 바로 쓰지 않는다(대비 1.47:1).
- **Don't** 가운데 정렬 큰 제목이나 기술 행사 키노트식 장표를 만들지 않는다.
- **Don't** 종이 안에서 실선 상자로 내용을 묶지 않는다. 점선 칸은 뜯거나 채울 자리에만 쓴다.
- **Don't** CW Display를 굵게 만들거나 문단에 쓰지 않는다.
- **Don't** 머리말의 일곱 색 말고 다른 색을 쓰지 않는다. 부속 파일의 색 띠는 견본일 뿐이다.
