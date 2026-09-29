# Figma MCP 연결과 시연 절차

MCP는 Claude Code가 다른 프로그램(여기서는 Figma)과 주고받는 통로입니다.
실습③까지 끝낸 분만 선택 과제로 해 보세요. 막히면 바로 그만두고 기본 결과물에 집중합니다.

> 출처: [Figma MCP 서버 가이드](https://help.figma.com/hc/ko/articles/32132100833559), [원격 서버 설치 문서](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/). 2026-09-28에 확인했습니다. 요금제·좌석 조건과 사용량 한도는 바뀔 수 있으니 세션 전에 다시 확인하세요.

## 1. 어떤 서버에 연결하나
- **원격 서버** (`https://mcp.figma.com/mcp`): 가이드에 "모든 시트 및 요금제에서 사용할 수 있습니다"라고 적혀 있습니다. 이 세션은 원격 서버를 기준으로 합니다.
- **데스크톱 서버**: 가이드에 "데브 또는 풀 시트에서 모든 유료 요금제"라고 적혀 있습니다.
- **요청 한도**: 요금제·좌석별 사용량 한도는 Figma 개발자 문서에 따로 있습니다. 이 자료에는 숫자를 적지 않습니다(미확인).

## 2. Claude Code에 연결하기
터미널에서 둘 중 하나를 실행합니다.

```
claude plugin install figma@claude-plugins-official
```

또는

```
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

그다음 순서입니다.
1. Claude Code를 새로 시작합니다.
2. `/mcp`를 입력하고 **figma**를 고른 뒤 **Authenticate**를 누릅니다.
3. 브라우저 창에서 **Allow Access**를 누릅니다.
4. "Authentication successful. Connected to figma"가 보이면 연결된 것입니다. `/mcp`로 한 번 더 확인합니다.

## 3. 시연 두 방향

**① Figma 변수 → design-system.md (실습①)**
1. 변수(Variables)가 정의된 Figma 파일 링크를 복사합니다.
2. `advanced/prompts.md`의 "토큰 추출: Figma 파일에서" 프롬프트에 링크를 넣어 보냅니다.
3. `docs/design-system.md`의 색·간격 칸이 Figma 값으로 채워졌는지 확인합니다. Figma에 없는 값은 "(없음)"이어야 합니다.

**② 로컬 화면 → Figma 레이어 (실습③ 마지막)**
1. `index.html`을 로컬에서 띄웁니다.
2. "Figma로 보내기" 프롬프트에 대상 Figma 파일 링크를 넣어 보냅니다.
3. 가이드에 따르면 화면을 Figma로 캡처하는 기능은 원격 서버에서만, 그리고 일부 클라이언트(Claude Code 포함)에서만 됩니다.

## 4. 연결에 실패하면
- **인증 창이 뜨지 않거나 실패함:** 현장 와이파이 문제일 가능성이 큽니다. 휴대폰 핫스팟으로 한 번만 다시 시도하고, 그래도 안 되면 중단합니다.
- **권한·좌석 오류:** 요금제나 좌석 문제입니다. 현장에서는 해결할 수 없으니 중단합니다.
- **대안:** 진행자가 미리 찍어 둔 스크린샷(`demo/figma-roundtrip/`)으로 흐름만 보여줍니다. 스크린샷이 아직 없으면 이 문서의 3장을 말로 설명합니다.
- **변수 없이 하는 방법:** Figma 없이도 실습①의 "토큰 추출: 코드에서" 프롬프트로 같은 결과(토큰이 채워진 design-system.md)를 만들 수 있습니다.
