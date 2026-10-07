"""장표에 폰트를 넣는다.

slides/index.html에 쓰인 글자만 남긴 woff2 서브셋을 만들어
/*FONTS-START*/ 와 /*FONTS-END*/ 사이에 base64로 넣는다.
Nanum Gothic은 OFL 예약 이름이 있어 서브셋 이름을 CW Gothic으로 바꾼다.

실행: tools/.venv/bin/python tools/build.py
"""
import base64
import io
import pathlib
import re

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'tools/fonts-src'
TARGETS = ['slides/index.html']

FACES = [
    # (원본 파일, 서브셋 이름, 굵기)
    ('BlackHanSans-Regular.ttf', 'CW Display', 400),
    ('NanumGothic-Regular.ttf', 'CW Gothic', 400),
    ('NanumGothic-Bold.ttf', 'CW Gothic', 700),
    ('NanumGothic-ExtraBold.ttf', 'CW Gothic', 800),
]
START, END = '/*FONTS-START*/', '/*FONTS-END*/'


def used_chars(html):
    body = html.split(END, 1)[1] if END in html else html
    return set(body) | set(' 0123456789:/.,-')


def subset_font(path, family, chars):
    font = TTFont(path)
    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['*']
    opts.name_IDs = []  # 이름 표는 아래에서 새로 쓴다
    sub = subset.Subsetter(opts)
    sub.populate(text=''.join(chars))
    sub.subset(font)
    name = font['name']
    name.names = []
    for nid, val in [(1, family), (2, 'Regular'), (4, family), (6, family.replace(' ', '') + '-Subset')]:
        name.setName(val, nid, 3, 1, 0x409)
    buf = io.BytesIO()
    font.flavor = 'woff2'
    font.save(buf)
    return buf.getvalue()


def build(target):
    path = ROOT / target
    html = path.read_text(encoding='utf-8')
    chars = used_chars(html)
    rules = []
    for file, family, weight in FACES:
        data = subset_font(SRC / file, family, chars)
        print(f'{target}: {family} {weight} {len(data) // 1024} KB')
        b64 = base64.b64encode(data).decode()
        rules.append(f'@font-face {{ font-family: "{family}"; font-weight: {weight}; font-display: block; '
                     f'src: url(data:font/woff2;base64,{b64}) format("woff2"); }}')
    block = START + '\n' + '\n'.join(rules) + '\n' + END
    html = re.sub(re.escape(START) + '.*?' + re.escape(END), lambda _: block, html, count=1, flags=re.S)
    path.write_text(html, encoding='utf-8')


if __name__ == '__main__':
    for t in TARGETS:
        build(t)
