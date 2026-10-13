# 세션 전에 진행자가 할 일

자료는 다 만들어져 있다. 아래는 진행자만 채우거나 확인할 수 있는 것이다. 위에서부터 하면 된다.
남은 표시 전체 목록(파일과 줄 번호)은 `tools/.venv/bin/python tools/verify_all.py`를 돌리면 맨 아래에 나온다.

## 1. 일정 정보 채우기
- [ ] 세션 일시와 장소: 장표 1번 머리 칸(`slides/index.html`의 "일시·장소 [진행자 기입]"), `facilitator/cue-sheet.md` 맨 위
- [ ] 예상 인원: `facilitator/cue-sheet.md` 맨 위, `PRODUCT.md` 참석자 줄
- [ ] D-3 메시지의 요일, D-1 메시지의 일시와 장소: `comms/pre-session.md`

장표 글을 손으로 고친 뒤에는 `tools/.venv/bin/python tools/build.py`로 폰트를 다시 넣는다.

## 2. 실습 페이지 배포와 주소 채우기
배포 주소: https://session03-cowork.vercel.app (Vercel 프로젝트 `session03-cowork`, jampark's projects 팀)

- [x] `practice-page/cowork-samples.zip`이 `index.html` 옆에 있는지 본다. 없으면 `cd tools && ../tools/.venv/bin/python gen_samples.py`
- [x] `practice-page/` 폴더에서 `vercel deploy --prod`. 실습 페이지나 샘플을 고치면 다시 실행한다.
- [x] 배포 주소로 `tools/.venv/bin/python tools/set_url.py https://배포주소` 한 줄 실행. 장표 9번·19번 QR, 표지·마무리 쪽지 줄, 치트시트 QR, 두 안내 메시지의 주소가 한 번에 채워진다. (QR 세 개 모두 이 주소로 읽히는 것 확인)
- [ ] 휴대폰으로 장표 QR을 찍어 실습 페이지와 샘플 다운로드가 되는지 본다

## 3. 후기 받을 곳
- [ ] 후기 남길 곳(설문 링크나 채팅방): `comms/post-session.md`의 "[진행자 기입: 후기 남길 곳]"

## 4. 앱에서 확인할 제품 사실
자료 전체의 "확인 필요" 표시는 확인하지 않고 정리했다 (2026-10-13 결정). 무난한 문장만 남기거나 문장을 뺐다.
- 메뉴·버튼 이름은 적지 않는다. 현장에서는 화면에 보이는 그대로 읽는다.
- 앞의 대화를 기억하는지, 작업 여러 개를 동시에 돌릴 수 있는지, 플랜별 한도는 말하지 않는다. "필요한 건 문장에 직접 적기", "작게 써 보고 판단하기"로 안내한다.

현장에서 확인한 것이 있으면 `faq.md`와 `troubleshooting.md`에 덧붙인다.

## 5. 시연 준비
캡처는 넣지 않는다 (2026-10-13 결정). 7번 장표는 맡기기 전과 후를 글로 비교한다.
- [ ] 시연 1(샘플 01_영수증)을 미리 돌려 결과가 7번 장표의 숫자(17건, 294,200원, 중복 의심 1건)와 맞는지 본다. 샘플은 zip을 새로 풀어서 쓴다
- [ ] 시연 2(매일 아침 업계 브리핑)를 미리 등록하고 바로 한 번 실행해 본다
- [ ] 시연 1과 미션 A~D가 각각 몇 분 걸리는지 재어 둔다

## 6. 그 밖의 리허설
`facilitator/cue-sheet.md`의 "리허설 체크"를 따른다. 현장 노트북에서 장표 키 조작 확인, Windows에서 샘플 zip 풀기, USB 메모리에 샘플 준비, 다음 날 아침 8시 메시지 예약 발송이 들어 있다.
