# 카드 뉴스·릴스 세션 준비 자료: 이 폴더의 규칙

세션 "[초급] Claude로 카드 뉴스와 짧은 홍보 영상 만들기"(2026-10-28)의 장표, 실습 가이드, 템플릿, 체크리스트, 가상 브랜드 에셋, 완성 예시, 진행자 노트를 만든다.
전체 명세는 `HANDOFF.md`(로컬 전용)이고, 제품 사실과 확정한 결정은 `PRODUCT.md`에 있다. 둘이 다르면 `PRODUCT.md`의 확정 결정을 따른다.

## 작업 규칙
- 모든 텍스트는 한국어, 공지와 같은 친절한 존댓말("~해요", "~해 보세요"). 전문 용어는 처음 나올 때 쉬운 말로 풀어 쓴다.
- 제품 사실은 `PRODUCT.md` 표의 범위 안에서만 쓴다. 표에 없는 기능·가격·수치는 `[확인 필요]`로 표시한다. 신뢰도가 서드파티·업계 해석·진행자 제공인 항목은 "~라는 보고가 있어요"처럼 단정하지 않는다. 제품 기능, 플랜 조건, 소요 시간에는 "2026년 10월 기준"을 붙인다.
- 가격·크레딧 수치는 `speaker-notes.md`에만 쓴다. 이 파일은 공개 저장소라 로컬에만 둔다(`.gitignore`).
- `PRODUCT.md`의 "쓰면 안 되는 설명"에 있는 문장은 어디에도 쓰지 않는다.
- 실습용 브랜드는 가상 브랜드 루미엘(화장품)과 골목 한그릇(국밥집)만 쓰고, 처음 나올 때 "(가상 브랜드)"라고 표시한다. 실존 브랜드명과 참석자 개인 정보는 쓰지 않는다.
- 진행자가 강의 전에 확인할 것은 자료에 `TODO`로 남기고, 작업이 끝날 때 목록을 따로 보고한다.
- 산출물은 HANDOFF 4장 순서대로 하나씩 만들고, 하나 끝날 때마다 진행자 확인을 받는다.

## 디자인
- impeccable 스킬 절차를 따른다. 제품 문맥은 `PRODUCT.md`, 장표의 방향 계약은 `.impeccable/surfaces/slides-index-html.md`(음악실 오선 칠판)에 있다.
- `DESIGN.md`는 장표를 다 만들고 검수한 뒤 실제 결과에서 기록한다. 그 뒤에 만드는 화면(실습 가이드 등)은 `DESIGN.md`를 따르고, 없는 색이나 부품이 필요하면 `DESIGN.md`부터 고친다.
- 카드 뉴스·릴스 완성 예시는 세션 디자인이 아니라 각 가상 브랜드의 모습으로 만든다.
- 다른 세션 폴더의 디자인 규칙이나 파일을 가져다 쓰지 않는다.

## 기술
- 산출물마다 단일 HTML 파일. CSS·JS 인라인, 외부 빌드 없음.
- 장표는 인터넷 없이 열린다. 폰트는 `tools/build.py`가 쓰인 글자만 잘라 base64로 넣는다. 장표 글을 고친 뒤에는 다시 빌드한다.
- 장표는 세션 뒤 참석자에게 메일로 나간다. 발표자 노트, 가격, 크레딧, 방향 계약 문장을 장표 파일 안에 넣지 않는다(숨김 요소 포함).
- 실습 가이드는 Vercel에 배포하고 주소와 QR을 장표에 넣는다. 주소는 https://cardnews-reels-practice.vercel.app (jamparks-projects 계정).
  다시 배포: `tools/.venv/bin/python tools/build.py slides/index.html practice/index.html`(글자를 고쳤으면) → `tools/.venv/bin/python tools/verify.py` → `tools/.venv/bin/python tools/make_downloads.py` → `vercel deploy practice --prod --scope jamparks-projects`. `vercel link`가 만드는 `practice/.env.local`은 지우고, `practice/.vercelignore`를 지킨다.
  Vercel 프로젝트의 Git 연결은 끊어 두었다(2026-10-27). 저장소 루트로 자동 배포되면 주소가 404가 되기 때문이다. 배포는 위 명령으로만 한다. `vercel link`를 다시 하면 Git이 다시 연결될 수 있으니 `vercel git disconnect`로 끊는다.
- 보조 스크립트는 `tools/`, 파이썬 의존성은 `tools/.venv`에 둔다.
- impeccable 스킬은 저장소 루트 `.claude/`에 설치돼 있고 저장소에는 올리지 않는다. 다시 받을 때는 저장소 루트에서 `npx impeccable install --providers=claude --scope=project --no-hooks`.
