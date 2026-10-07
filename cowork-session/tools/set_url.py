"""실습 페이지 주소가 정해지면 장표·치트시트·메시지의 주소 자리와 QR을 한 번에 채운다.

실행: tools/.venv/bin/python tools/set_url.py https://주소
- slides/index.html: QR 자리 두 곳에 QR 그림, "[주소 진행자 기입]"과 쪽지 줄의 주소를 실제 주소로
- comms/cheat-sheet.html, comms/pre-session.md, comms/post-session.md: 실습 페이지 주소 자리
- 주소는 tools/site-url.txt에도 적어 둔다
장표 글자가 바뀌므로 마지막에 tools/build.py로 폰트를 다시 넣는다.
"""
import pathlib
import re
import subprocess
import sys

import segno

ROOT = pathlib.Path(__file__).resolve().parent.parent


def qr_svg(url):
    q = segno.make(url, error='m')
    w, h = q.symbol_size(scale=1, border=0)
    svg = q.svg_inline(scale=1, border=0, dark='#141414', light='#ffffff')
    svg = re.sub(r'<svg[^>]*?>', f'<svg viewBox="0 0 {w} {h}" shape-rendering="crispEdges" role="img" aria-label="실습 페이지 QR">', svg, count=1)
    return svg


def main(url):
    short = re.sub(r'^https?://', '', url).rstrip('/')
    s = ROOT / 'slides/index.html'
    t = s.read_text(encoding='utf-8')
    t = t.replace('<div class="qr">QR 자리<br>[주소 진행자 기입]</div>', f'<div class="qr" style="border: 0; padding: 0">{qr_svg(url)}</div>')
    t = t.replace('[주소 진행자 기입]', short)
    # 세로 쪽지 칸에는 12자까지만 들어간다. 긴 주소는 QR 쪽으로 안내한다
    cover, rest = t.split('<!-- 20 마무리 -->', 1)
    fit = len(short) <= 12
    cover = cover.replace('<span>주소 [진행자 기입]</span>', f'<span>{short if fit else "마지막 장 QR"}</span>')
    rest = rest.replace('<span>주소 [진행자 기입]</span>', f'<span>{short if fit else "QR 옆 주소"}</span>')
    t = cover + '<!-- 20 마무리 -->' + rest
    s.write_text(t, encoding='utf-8')

    c = ROOT / 'comms/cheat-sheet.html'
    c.write_text(c.read_text(encoding='utf-8').replace('<div class="qr">QR 자리</div>', f'<div class="qr" style="border: 0">{qr_svg(url)}</div>'), encoding='utf-8')
    for path, old in [('comms/cheat-sheet.html', '<span class="blank">[진행자 기입: 주소]</span>'),
                      ('comms/pre-session.md', '[진행자 기입: 실습 페이지 주소]'),
                      ('comms/post-session.md', '[진행자 기입: 실습 페이지 주소]')]:
        p = ROOT / path
        p.write_text(p.read_text(encoding='utf-8').replace(old, short), encoding='utf-8')

    (ROOT / 'tools/site-url.txt').write_text(url + '\n', encoding='utf-8')
    subprocess.run([sys.executable, str(ROOT / 'tools/build.py')], check=True)
    left = [p for p in ['slides/index.html', 'comms/cheat-sheet.html'] if '진행자 기입: 주소' in (ROOT / p).read_text(encoding='utf-8')
            or '[주소 진행자 기입]' in (ROOT / p).read_text(encoding='utf-8')]
    print('주소를 채웠습니다:', short, '/ 남은 주소 자리:', left or '없음')


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].startswith('http'):
        sys.exit('사용법: tools/.venv/bin/python tools/set_url.py https://주소')
    main(sys.argv[1])
