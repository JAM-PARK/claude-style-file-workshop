"""세션 ② 자료를 한 번에 다시 만든다. 외부 번들러 없이 파일 안의 표시 사이만 갈아 끼운다.

    tools/.venv/bin/python tools/build.py

1. slides/index.html  15번 원문(<!--DS-->), QR(<!--QR-->), 주소(<!--URL-->)
2. handout/index.html md 원문 블록(data-src), 미리보기 이미지, QR, 인라인 폰트(/*FONTS*/)
3. runsheet/index.html QR, 인라인 폰트
4. 세 파일에 쓰인 글자만 남긴 woff2 서브셋 → slides/assets/fonts/

배포 주소는 tools/site-url.txt 한 줄만 바꾸고 다시 실행한다.
"""
import base64, html, io, pathlib, re
import segno
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_FONTS = ROOT / 'tools/fonts-src'
OUT_FONTS = ROOT / 'slides/assets/fonts'
FONTS = [  # (파일, 패밀리, 굵기)
    ('GothicA1-Regular.ttf', 'Gothic A1', 400),
    ('GothicA1-Medium.ttf', 'Gothic A1', 500),
    ('GothicA1-Bold.ttf', 'Gothic A1', 700),
    # OFL 예약 이름(Nanum)이 있어 서브셋은 다른 이름으로 배포한다
    ('NanumGothicCoding-Regular.ttf', 'S2 Mono', 400),
]


def read(p): return (ROOT / p).read_text(encoding='utf-8')
def write(p, s): (ROOT / p).write_text(s, encoding='utf-8')


def between(text, name, content, html_comment=True):
    a, b = (f'<!--{name}:start-->', f'<!--{name}:end-->') if html_comment else (f'/*{name}:start*/', f'/*{name}:end*/')
    pat = re.compile(re.escape(a) + '.*?' + re.escape(b), re.S)
    if not pat.search(text):
        return text
    return pat.sub(lambda _: a + content + b, text)


def site_url():
    return read('tools/site-url.txt').strip()


def qr_svg(url):
    q = segno.make(url, error='m')
    buf = io.BytesIO()
    q.save(buf, kind='svg', dark='#1E1E1C', light='#FFFFFF', border=2, xmldecl=False, svgns=True, nl=False, omitsize=True)
    svg = buf.getvalue().decode()
    return svg.replace('<svg ', '<svg role="img" aria-label="배포 페이지 QR 코드" ', 1)


def ds_columns():
    lines = read('slides/design-system.md').rstrip('\n').split('\n')
    return ''.join(f'<div class="ln">{html.escape(l) or " "}</div>' for l in lines)


def build_slides():
    s = read('slides/index.html')
    s = between(s, 'DS', ds_columns())
    s = between(s, 'QR', qr_svg(site_url()))
    s = between(s, 'URL', html.escape(site_url()))
    write('slides/index.html', s)
    return s


def visible_text(doc):
    strings = ' '.join(re.findall(r"'([^'\n]*)'", ' '.join(re.findall(r'<script[^>]*>(.*?)</script>', doc, flags=re.S))))
    doc = re.sub(r'<(script)[^>]*>.*?</\1>', ' ', doc, flags=re.S) + ' ' + strings
    doc = re.sub(r'<svg.*?</svg>', ' ', doc, flags=re.S)
    doc = re.sub(r'<[^>]+>', ' ', doc)
    return html.unescape(doc)


def rename(font, family):
    """수정본(서브셋)에서 예약 글꼴 이름을 지운다. 저작권(0)과 라이선스(13, 14) 기록은 그대로 둔다."""
    ps = family.replace(' ', '') + '-Regular'
    names = {1: family, 2: 'Regular', 3: ps + '-subset', 4: family + ' Regular', 6: ps}
    table = font['name']
    table.names = [r for r in table.names if r.nameID not in (16, 17, 18, 21, 22)]
    for r in table.names:
        if r.nameID in names:
            r.string = names[r.nameID]
    if 'CFF ' in font:
        font['CFF '].cff.fontNames = [ps]


def subset_fonts(text):
    OUT_FONTS.mkdir(parents=True, exist_ok=True)
    chars = set(text) | set(' 0123456789:/.,()-+%#·"\'!?')
    out = {}
    for fname, family, weight in FONTS:
        f = TTFont(SRC_FONTS / fname)
        opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = ['*']
        sub = subset.Subsetter(opts); sub.populate(text=''.join(chars)); sub.subset(f)
        if family == 'S2 Mono':
            rename(f, family)
        stem = family.replace(' ', '') if family == 'S2 Mono' else fname.split('-')[0]
        dest = OUT_FONTS / f'{stem}-{weight}.woff2'
        opts2 = opts
        subset.save_font(f, str(dest), opts2)
        out[(family, weight)] = dest
    return out


def font_face_inline(paths, families=None):
    css = []
    for (family, weight), p in paths.items():
        if families and (family, weight) not in families:
            continue
        b64 = base64.b64encode(p.read_bytes()).decode()
        css.append(f'@font-face{{font-family:"{family}";font-weight:{weight};font-display:swap;src:url(data:font/woff2;base64,{b64}) format("woff2")}}')
    return ''.join(css)


def main():
    docs = {'slides': build_slides()}
    handout_mod = None
    if (ROOT / 'tools/build_handout.py').exists():
        import importlib.util
        spec = importlib.util.spec_from_file_location('bh', ROOT / 'tools/build_handout.py')
        handout_mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(handout_mod)
    if handout_mod and (ROOT / 'handout/index.html').exists():
        docs['handout'] = handout_mod.build(ROOT, between, qr_svg, site_url)
    if (ROOT / 'runsheet/index.html').exists():
        r = read('runsheet/index.html')
        r = between(r, 'QR', qr_svg(site_url()))
        r = between(r, 'URL', html.escape(site_url()))
        write('runsheet/index.html', r); docs['runsheet'] = r
    text = ''.join(visible_text(d) for d in docs.values()) + read('slides/design-system.md')
    paths = subset_fonts(text)
    only = {'slides': None, 'handout': None, 'runsheet': {('Gothic A1', 400), ('Gothic A1', 700)}}
    for name in ('slides', 'handout', 'runsheet'):
        if name in docs:
            p = f'{name}/index.html'
            write(p, between(read(p), 'FONTS', font_face_inline(paths, only[name]), html_comment=False))
    for (fam, w), p in paths.items():
        print(f'{fam} {w}: {p.stat().st_size // 1024} KB')
    print('glyphs:', len(set(text)))


if __name__ == '__main__':
    main()
