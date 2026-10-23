---
version: 1
slug: "practice-index-html"
primary_target: "practice/index.html"
related_targets: []
---

# 실습 가이드 (practice/index.html)

범위: 참석자가 노트북(가끔 폰)에 열어 두고 진행자 말에 맞춰 실습 1~5를 따라 하는 웹 페이지. 모드: Read(안내서). Vercel 배포, 인터넷 없이도 열림(폰트 내장). 세계는 DESIGN.md(음악실 오선 칠판) 그대로.
청중과 할 일: 진행자가 "실습 N 여세요" 하면 바로 그 실습으로 가서, 단계를 읽고 프롬프트를 빈칸판 또는 예시판으로 복사하고, 잘 됐는지 확인하고, 막히면 답을 찾는다.
제약: 프롬프트마다 복사 버튼과 빈칸/예시(골목 한그릇) 탭, [대괄호]는 노랑, 본문 18px 이상, 375px에서 가로 스크롤 없음, PRODUCT.md 사실과 진행자 확정 사항, 가격·크레딧 없음, 방향 계약 문장 넣지 않음.
미정: 내려받기 파일(③ 템플릿, ④ 체크리스트, ⑤ 에셋·완성 예시)은 다음 단계에서 채움. 배포 주소.

## Direction contract

THESIS: 실습 하나에 화면 하나. 왼쪽 세로 오선 레일에서 실습을 고르면 본문에 그 실습만 남는다. 긴 스크롤 안내서와 카드 격자 실습 페이지를 거부한다.

OWN-WORLD: DESIGN.md의 칠판·분필 세 색, 기준선 줄, 브래킷 프롬프트 단, 빈칸/예시 탭, 노란 복사 버튼을 웹 크기로 옮긴다. 레일은 세로로 세운 오선(가는 페인트 선)이고 지금 실습 칸만 노랑으로 칠한다.

STORY: 참석자는 레일을 보고 지금 몇 번 실습인지 알고, 목표→준비→단계→프롬프트→확인→막히면 순서로 내려가며 손을 움직인다.

FIRST VIEWPORT: 1440 폭에서 왼쪽 260px 레일(페이지 이름, 실습 1~5와 분, 유료 플랜 표시, 아래 내려받기), 오른쪽 본문에 실습 제목과 늘임표·분, 목표·준비 한 줄, 번호 단계, 열린 프롬프트 단(오른쪽 위 탭과 노란 복사). 폰에서는 레일이 위쪽 가로 마디 띠로 접힌다. 시그니처 상호작용: 레일에서 실습을 고르면 노란 칸이 그 실습으로 미끄러지고 주소가 #실습N으로 바뀐다(동작 줄이기면 즉시).

FORM: 실습 레일 + 한 번에 실습 하나, 구조 후보 2번. seed:632fafdcab51c4e2

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
