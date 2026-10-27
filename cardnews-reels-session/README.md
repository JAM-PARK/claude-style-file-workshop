# Claude로 카드 뉴스와 짧은 홍보 영상 만들기

AI 스터디 모임 초급 세션(2026년 10월 28일) 자료예요. 내용은 2026년 10월 기준이에요. Claude 기능과 플랜 조건은 자주 바뀌어요.

## 어디부터 열까요

1. **실습 페이지**: 오늘 쓴 프롬프트가 모두 있고, 복사 버튼으로 바로 가져갈 수 있어요. 주소는 https://cardnews-reels-practice.vercel.app 이고, 장표 1번과 32번의 QR로도 열 수 있어요. 파일로는 `practice/index.html`이에요.
2. **장표**: `slides/index.html`을 더블클릭하면 브라우저(크롬, 엣지)에서 열려요. 인터넷 없이도 열려요.
   - 넘기기: 키보드 ← →
   - 전체 화면: F
   - 프롬프트 예시판 보기: E
   - PDF로 저장: 브라우저 인쇄(Ctrl + P) → PDF로 저장. 한 장씩 나와요.

## 파일 안내

| 파일 | 내용 |
|---|---|
| `slides/index.html` | 강의 장표 33장 |
| `practice/index.html` | 실습 1~5를 하나씩 따라 하는 페이지 (프롬프트 복사 버튼) |
| `templates/instructions-cosmetics.md` | 프로젝트 지침 예시: 루미엘(가상 브랜드) 화장품 |
| `templates/instructions-restaurant.md` | 프로젝트 지침 예시: 골목 한그릇(가상 브랜드) 국밥집 |
| `templates/reels-brief.md` | 릴스 장면 계획표 (빈칸과 예시) |
| `templates/video-swap-decision.md` | 영상 속 제품을 바꿀 때 Claude와 영상 AI 중 무엇을 쓸지 고르는 표 |
| `checklists/before-posting.md` | 올리기 전에 확인할 것: 규격, 광고 표현, AI 표시 |
| `assets/` | 실습용 가상 브랜드 로고와 그림 (내 가게 사진이 없을 때 써요) |
| `examples/cardnews-lumiel/`, `examples/cardnews-golmok/` | 카드 뉴스 완성 예시 6장씩 |
| `examples/reels-golmok/index.html` | 15초 릴스 애니메이션 완성 예시 (브라우저로 열면 반복 재생) |
| `examples/copy.md` | 완성 예시에 쓴 문구 |
| `examples/practice5-source-fixed-shot.mp4`, `examples/practice5-source-handheld.mp4` | 실습 5 샘플 영상 10초 2개 (고정 샷, 손에 든 영상). Gemini로 만든 AI 영상이에요 |

`tools/`, `PRODUCT.md`, `DESIGN.md`, `CLAUDE.md`는 자료를 만들고 고칠 때 쓰는 파일이라 참석자는 보지 않아도 돼요.

## 알아 두세요

- 루미엘과 골목 한그릇은 실습용으로 만든 가상 브랜드예요. 실제 가게나 제품과 관계없어요.
- `.md` 파일은 메모장으로 열 수 있어요. 파일을 마우스 오른쪽 버튼으로 누르고 "연결 프로그램 → 메모장"을 골라요. 메모장에서는 `#`, `|` 같은 기호가 그대로 보일 수 있는데, 내용은 같고 그대로 복사해 Claude에 붙여 넣어도 돼요.
- 광고 표현 목록과 바꿔 쓰는 말은 예시예요. 실제 광고 전에는 식약처 기준으로 확인해요. 식품 광고 규정은 별도 확인이 필요해요.
- Claude가 검수해도 마지막 판단과 게시는 사람이 해요.

## 글꼴

장표, 실습 페이지, 릴스 예시에는 Noto Sans KR과 Noto Serif KR을 넣었어요. 두 글꼴 모두 SIL Open Font License 1.1이고, 라이선스 파일은 각 폴더의 `fonts/`에 있어요.
