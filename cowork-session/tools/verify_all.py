"""HANDOFF 8장 완료 기준 중 기계로 확인할 수 있는 것을 한 번에 돌린다.

실행: tools/.venv/bin/python tools/verify_all.py
화면 확인(장표 1920·1366 잘림, 실습 페이지 375px, 복사 버튼)은 브라우저로 따로 하고, 결과는 facilitator/verification.md에 적는다.
마지막에 [확인 필요]와 [진행자 기입] 목록을 뽑는다.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ['slides/index.html', 'practice-page/index.html', 'comms/cheat-sheet.html']
DOCS = ['facilitator/cue-sheet.md', 'facilitator/faq.md', 'facilitator/troubleshooting.md', 'facilitator/answer-keys.md',
        'comms/pre-session.md', 'comms/post-session.md']
PALETTE = {'#2e3532', '#f2f4f2', '#a9b2ae', '#ffffff', '#141414', '#d2261c'}
fails = []


def check(ok, msg):
    print(('통과 ' if ok else '실패 ') + msg)
    if not ok:
        fails.append(msg)


def text_of(path):
    s = (ROOT / path).read_text(encoding='utf-8')
    return re.sub(r'/\*FONTS-START\*/.*?/\*FONTS-END\*/', '', s, flags=re.S)


# 장표: 본 장표 20장, 장마다 노트와 예상 시간
s = text_of('slides/index.html')
slides = re.findall(r'<section class="slide" data-seg="(-?\d)" data-time="([^"]+)">(.*?)</section>', s, re.S)
main = [x for x in slides if x[0] != '-1']
check(len(main) == 20, f'본 장표 {len(main)}장, 부록 {len(slides) - len(main)}장')
check(all('class="notes"' in x[2] for x in slides), '모든 장에 발표자 노트')
mins = sum(int(re.match(r'\d+', t).group()) for _, t, _ in main)
check(mins <= 90, f'장표 예상 시간 합계 {mins}분 (90분 이내)')
check('function fit()' in s and "k === 'n'" in s and "k === 'f'" in s, '판 맞춤, N 노트, F 전체화면 코드')

# 색: 범례 밖의 색, 그라디언트, 둥근 모서리, 그림자
for h in HTML:
    t = text_of(h)
    css = ' '.join(re.findall(r'<style>(.*?)</style>', t, re.S)) + ' '.join(re.findall(r'style="([^"]*)"', t))
    colors = {c.lower() for c in re.findall(r'#[0-9a-fA-F]{6}\b', css)}
    check(colors <= PALETTE, f'{h}: 색 {sorted(colors)} 모두 범례 안')
    check('gradient' not in css, f'{h}: 그라디언트 없음')
    check(not re.search(r'border-radius\s*:\s*(?!0)', css), f'{h}: 둥근 모서리 없음')
    check(not re.search(r'box-shadow\s*:\s*(?!none)', css), f'{h}: 그림자 없음')
    check('prefers-reduced-motion' in css or h.endswith('cheat-sheet.html'), f'{h}: 동작 줄이기 설정 존중 (치트시트는 움직임 없음)')

# 실존 브랜드, 실제처럼 보이는 연락처
ALL = HTML + DOCS + ['PRODUCT.md', 'tools/sample_data.py', 'tools/gen_samples.py']
BRANDS = ['네이버', '카카오', '쿠팡', '배민', '배달의민족', '토스', '신한', '국민카드', '삼성카드', '현대카드', '스타벅스', '인스타그램',
          '유튜브', '구글', '노션', '슬랙', '당근마켓', '파리바게뜨', '뚜레쥬르']
for path in ALL:
    t = text_of(path)
    found = [b for b in BRANDS if b in t]
    check(not found, f'{path}: 실존 브랜드 이름 없음' + (f' (발견: {found})' if found else ''))
    phones = [p for p in re.findall(r'0\d{1,2}-\d{3,4}-\d{4}', t) if '-0000-' not in p]
    check(not phones, f'{path}: 가짜 형식이 아닌 전화번호 없음' + (f' (발견: {phones})' if phones else ''))
    biz = [b for b in re.findall(r'\b\d{3}-\d{2}-\d{5}\b', t) if not b.startswith('000-00-')]
    check(not biz, f'{path}: 가짜 형식이 아닌 사업자번호 없음' + (f' (발견: {biz})' if biz else ''))

# 큐시트 90분
rows = [l for l in (ROOT / 'facilitator/cue-sheet.md').read_text(encoding='utf-8').splitlines() if re.match(r'\| \d:\d\d \|', l)]
total = sum(int(l.split('|')[2]) for l in rows)
check(total <= 90, f'큐시트 합계 {total}분')

# 샘플과 정답지 교차 검증
r = subprocess.run([sys.executable, str(ROOT / 'tools/verify_samples.py')], cwd=ROOT / 'tools', capture_output=True, text=True)
check(r.returncode == 0, '샘플·정답지 교차 검증 (verify_samples.py): ' + r.stdout.strip().splitlines()[-1])

# [확인 필요]와 [진행자 기입] 목록
print('\n## 남은 표시 목록')
for mark in ['[확인 필요', '[진행자 기입', '[주소 진행자 기입]']:
    print(f'\n### {mark}')
    for path in HTML + DOCS + ['PRODUCT.md']:
        t = text_of(path)
        if path.endswith('.html'):
            t = re.sub(r'<[^>]+>', '', t)
        for i, line in enumerate(t.splitlines(), 1):
            if mark in line:
                print(f'- {path}:{i}: {line.strip()[:110]}')

print()
print('모두 통과' if not fails else f'실패 {len(fails)}건')
sys.exit(1 if fails else 0)
