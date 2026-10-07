# 세션 전에 진행자가 할 일

자료는 다 만들어져 있다. 아래는 진행자만 채우거나 확인할 수 있는 것이다. 위에서부터 하면 된다.
남은 표시 전체 목록(파일과 줄 번호)은 `tools/.venv/bin/python tools/verify_all.py`를 돌리면 맨 아래에 나온다.

## 1. 일정 정보 채우기
- [ ] 세션 일시와 장소: 장표 1번 머리 칸(`slides/index.html`의 "일시·장소 [진행자 기입]"), `facilitator/cue-sheet.md` 맨 위
- [ ] 예상 인원: `facilitator/cue-sheet.md` 맨 위, `PRODUCT.md` 참석자 줄
- [ ] D-3 메시지의 요일, D-1 메시지의 일시와 장소: `comms/pre-session.md`

장표 글을 손으로 고친 뒤에는 `tools/.venv/bin/python tools/build.py`로 폰트를 다시 넣는다.

## 2. 실습 페이지 배포와 주소 채우기
- [ ] `practice-page/cowork-samples.zip`이 `index.html` 옆에 있는지 본다. 없으면 `cd tools && ../tools/.venv/bin/python gen_samples.py`
- [ ] `practice-page/` 폴더에서 `vercel deploy --prod`
- [ ] 배포 주소로 `tools/.venv/bin/python tools/set_url.py https://배포주소` 한 줄 실행. 장표 10번·20번 QR, 표지·마무리 쪽지 줄, 치트시트 QR, 두 안내 메시지의 주소가 한 번에 채워진다.
- [ ] 휴대폰으로 장표 QR을 찍어 실습 페이지와 샘플 다운로드가 되는지 본다

## 3. 후기 받을 곳
- [ ] 후기 남길 곳(설문 링크나 채팅방): `comms/post-session.md`의 "[진행자 기입: 후기 남길 곳]"

## 4. 앱에서 확인할 제품 사실 (리허설)
확인 전까지 자료에는 `[확인 필요]`로 남아 있다. 확인하면 아래 파일을 고친다.

| 확인할 것 | 고칠 곳 |
| --- | --- |
| Cowork를 여는 위치 (탭인지, 입력창에서 고르는지) | `comms/pre-session.md`, 실습 페이지 "시작 전 확인", 장표 5번 노트, `troubleshooting.md` |
| 예약 작업 메뉴와 버튼의 한국어 이름 (새로 만들기, 바로 실행, 실행 기록, 멈추기·지우기) | 실습 페이지 "예약 작업" 1단계, 장표 15번 노트, `faq.md` 13·14번, `troubleshooting.md`, `comms/post-session.md` |
| Chat과 Cowork가 기억을 나누는지 | 장표 19번, 부록 질문 1, `faq.md` 1번 |
| 작업 여러 개를 동시에 돌릴 수 있는지, 그때 사용량 | 부록 질문 3, `faq.md` 3번 |
| 결과 파일 형식 (엑셀, CSV) | `faq.md` 11번 |
| 폴더 권한을 묻는 창의 동작 | `troubleshooting.md` |
| 결과 파일이 저장되는 위치 | `faq.md` 12번 |
| 플랜별 사용량 한도 | 확인되어도 숫자는 말하지 않는 것을 권한다 |

참석자가 보는 화면에 있는 `[확인 필요]`(장표 19번, 실습 페이지 두 곳)는 확인한 내용으로 바꿔서 지운다.

## 5. 시연 캡처
- [ ] 시연 1(샘플 01_영수증)을 미리 돌리고 결과 화면을 캡처해 장표 8번 "사진 붙일 자리" 두 곳에 넣는다 (맡기기 전 폴더, 맡긴 후 지출표)
- [ ] 시연 2(매일 아침 업계 브리핑)를 미리 등록하고 바로 실행해 결과를 캡처해 둔다
- [ ] 시연 1과 미션 A~D가 각각 몇 분 걸리는지 재어 둔다

## 6. 그 밖의 리허설
`facilitator/cue-sheet.md`의 "리허설 체크"를 따른다. 현장 노트북에서 장표 키 조작 확인, Windows에서 샘플 zip 풀기, USB 메모리에 샘플 준비, 다음 날 아침 8시 메시지 예약 발송이 들어 있다.
