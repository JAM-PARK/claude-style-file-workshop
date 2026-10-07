---
version: 1
slug: "practice-page-index-html"
primary_target: "practice-page/index.html"
related_targets: []
---

# Cowork 세션 실습 페이지 (practice-page/index.html)

범위: 참석자가 QR로 여는 실습 안내 페이지. 휴대폰 375px 이상과 노트북. 모드 Read(따라 읽으며 프롬프트를 복사해 간다). 세계는 slides/index.html과 같고 DESIGN.md를 따른다.
청중: 코딩 경험 없는 참석자. 실습 중 노트북 Cowork 화면과 이 페이지를 오간다.
구성(사용자가 고른 구조, seed 91a0d3ec, "게시판 한 줄"): 순서, 시작 전 확인, 샘플 받기, 미션 A~D, 예약 작업 템플릿, 문장 공식, 맡기면 안 되는 일. 10장.
미결: 배포 주소, 샘플 zip을 같은 Vercel에 둘지(용량 2.7MB, 같은 폴더 상대 링크로 둠), Cowork 화면의 한국어 메뉴 이름.

## Direction contract
THESIS: 유리문에 같은 안내문이 위에서 아래로 이어 붙은 게시판. 참석자는 목차 띠로 자기 미션이나 템플릿으로 내려가 쪽지를 뜯어 간다. 카드 격자와 탭 대시보드를 거부한다.
OWN-WORLD: DESIGN.md 그대로. 유리 바탕, 흰 A4 종이, 먹, 빨강은 주의·금지·[확인 필요]뿐, 회색은 유리 위에만. 종이마다 세 칸 머리 칸. 휴대폰에서는 테이프를 종이 위 가운데 하나로만 붙여 가로로 삐져나오지 않게 한다. 먹 판은 종이 한 장에 많아야 하나.
STORY: 참석자는 시작 전 확인을 체크하고, 샘플을 받고, 미션 하나를 골라 문장을 복사해 Cowork에 붙이고, 확인법으로 결과를 점검한 뒤, 예약 템플릿 하나를 자기 일에 맞게 고쳐 등록한다.
FIRST VIEWPORT: 위에 고정된 유리 시트지 목차 띠(순서·준비·샘플·미션·예약·공식·주의, 지금 위치는 굵게와 밑줄). 그 아래 유리에 흰 글씨로 세션 제목, 이어서 첫 안내문 "오늘의 순서"가 시작되고 다음 안내문 "시작 전 확인"의 머리가 보인다. 서명 상호작용: 쪽지의 "복사하기"를 누르면 쪽지가 종이에서 아래로 떨어지며 사이로 유리가 비치고, 버튼은 "복사했어요"가 된 뒤 제자리로 돌아온다. 동작 줄이기면 글자만 바뀐다.
FORM: 게시판 한 줄(실습 페이지 구성 라운드 내 목록 3번). seed 91a0d3ec. 세계는 9820453f.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
