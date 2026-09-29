# 세션 ② 준비 자료

4차 AI 클로드코드 모임 세션 ② "매번 달라지는 AI 결과물, 클로드 설정으로 통일해보기"의 자료다. 명세는 `HANDOFF.md`에 있다. 내부 기획 문서라 저장소에는 올리지 않고 로컬에만 둔다.

## 여는 법
| 자료 | 파일 | 쓰는 곳 |
| --- | --- | --- |
| A. 세션 장표 | `slides/index.html` | 브라우저 전체화면. ← → 스페이스 이동, `N` 발표자 노트, 7번 `1` `2`, 15번 ↓ ↑ |
| B. 참가자 배포 페이지 | `handout/index.html` | 휴대폰 (QR). 파일 하나라 어디에 올려도 동작 |
| C. 심화 트랙 자료 | `advanced/` | 배포 페이지 심화 탭에 같은 내용 |
| D. A/B 시연 | `demo/` | 생성 기록은 `demo/README.md` |
| E. 러닝시트 | `runsheet/index.html` | A4 한 장 인쇄 |

세 HTML 모두 인터넷 없이 열린다. 폰트는 파일 안에 들어 있다. 폰트 라이선스(OFL)는 `slides/assets/fonts/`에 있다.

## 고치고 다시 만들기
배포 페이지와 장표 15번의 글은 md 원본에서 채워진다. HTML을 직접 고치지 말고 원본을 고친 뒤 다시 만든다.

처음 한 번은 준비가 필요하다.

```
python3 -m venv tools/.venv && tools/.venv/bin/pip install fonttools brotli segno
tools/fetch-fonts.sh
```

그다음부터는 이것만 실행한다.

```
tools/.venv/bin/python tools/build.py
```

- 원본: `slides/design-system.md`, `template/`, `examples/`, `prompts/prompts.md`, `advanced/`
- 배포 주소는 `tools/site-url.txt`에 있다 (현재 https://session02-handout.vercel.app). 바꾸면 다시 만든다. 장표 8번, 배포 페이지, 러닝시트의 QR이 함께 바뀐다.
- A/B 시연을 다시 만들려면 `tools/gen-demo.sh`를 쓴다. `demo/README.md`를 참고한다.

## Vercel 배포
`handout/`이 Vercel 프로젝트 jamparks-projects/session02-handout에 연결되어 있다 (`handout/.vercel/`, 저장소에는 올리지 않음). 새로 받은 저장소라면 `handout/`에서 `vercel link --project session02-handout --scope jamparks-projects`를 먼저 실행한다. 원본을 고치고 다시 만든 뒤 `handout/`에서 `vercel deploy --prod --scope jamparks-projects`를 실행한다.

## 디자인 규칙
장표, 배포 페이지, 러닝시트는 `slides/design-system.md` 한 장만 따른다. 고르게 된 과정은 `slides/design-review.md`에 있다.
