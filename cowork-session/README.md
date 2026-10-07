# Cowork 입문 세션 준비 자료

당근 AI 스터디 모임 세션 "퇴근 후에도 일하는 AI 직원 만들기: Cowork로 내 일 통째로 맡기기"의 자료다. 명세는 `HANDOFF.md`(로컬 전용), 제품 사실과 결정은 `PRODUCT.md`, 디자인 규칙은 `DESIGN.md`에 있다.

## 여는 법
| 자료 | 파일 | 상태 |
| --- | --- | --- |
| 진행용 장표 | `slides/index.html` | 완성 (리허설 후 캡처·QR·일시 채우기) |
| 샘플 파일 | `samples/` (배포용 묶음 `samples/cowork-samples.zip`) | 완성. 정답은 `facilitator/answer-keys.md` |
| 실습 페이지 | `practice-page/index.html` | 완성 (배포 주소 정해지면 장표 QR에 넣기) |
| 진행자 문서 | `facilitator/` | 완성: 세션 전 할 일(`before-session.md`), 큐시트, 정답지, FAQ, 문제 해결 |
| 안내 메시지·치트시트 | `comms/` | 완성: D-3·D-1 메시지(`pre-session.md`), 다음 날 아침 메시지(`post-session.md`), A4 치트시트(`cheat-sheet.html`) |

장표 조작: ← → 스페이스로 넘김, F 전체화면, N 발표자 노트, Home·End 처음·끝. 9번과 16번은 → 한 번에 빈칸이 하나씩 채워진다. 12번 휴식은 Enter로 타이머 시작·멈춤, R로 처음으로. 주소 뒤에 `#9`처럼 붙이면 그 장부터 연다.

## 고치고 다시 만들기
아래 명령은 모두 이 폴더(`cowork-session/`) 안에서 실행한다. 처음 한 번은 준비가 필요하다.

```
python3 -m venv tools/.venv && tools/.venv/bin/pip install fonttools brotli segno pillow python-docx openpyxl reportlab pypdf
tools/fetch-fonts.sh
```

장표 글을 고친 뒤에는 폰트를 다시 넣는다.

```
tools/.venv/bin/python tools/build.py
```

샘플은 손으로 고치지 않는다. 숫자와 내용은 `tools/sample_data.py`(영수증, 견적, 회의 결정)와 `tools/gen_samples.py`(다운로드 폴더, 녹취 본문)에 있다. 고친 뒤 셋을 차례로 실행한다.

```
cd tools
../tools/.venv/bin/python gen_samples.py       # samples/와 zip 다시 만들기
../tools/.venv/bin/python gen_answer_keys.py   # facilitator/answer-keys.md 다시 만들기
../tools/.venv/bin/python verify_samples.py    # 샘플 파일을 열어 정답지 숫자와 대조
```

## 실습 페이지 배포 (Vercel)
`practice-page/` 폴더 하나를 그대로 올린다. 샘플 묶음은 `gen_samples.py`가 `practice-page/cowork-samples.zip`으로 복사해 두므로 같은 폴더에서 받아진다 (저장소에는 올리지 않음).

```
cd practice-page
vercel deploy --prod
```

배포 주소가 정해지면 아래 한 줄로 장표 QR 두 곳, 쪽지 줄, 치트시트 QR, 안내 메시지의 주소를 한 번에 채운다. 장표 폰트도 다시 넣는다.

```
tools/.venv/bin/python tools/set_url.py https://배포주소
```

## 전체 점검
HANDOFF 8장 완료 기준 중 기계로 볼 수 있는 것(장표 장수와 노트, 범례 밖 색, 그라디언트·둥근 모서리·그림자, 실존 브랜드와 연락처 형식, 큐시트 90분, 샘플·정답지 교차 검증)을 한 번에 돌리고, 남은 `[확인 필요]`와 `[진행자 기입]` 목록을 뽑는다.

```
tools/.venv/bin/python tools/verify_all.py
```

폰트 라이선스(OFL)는 `slides/assets/fonts/`에 있다.
