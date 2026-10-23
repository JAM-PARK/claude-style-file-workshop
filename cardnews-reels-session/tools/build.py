#!/usr/bin/env python3
"""HTML에 쓰인 글자만 잘라 Noto Sans KR(OFL)을 base64 woff2로 넣는다.

각 파일의 /* FONTS:BEGIN */ ~ /* FONTS:END */ 사이를 다시 쓴다. 글을 고친 뒤 다시 실행한다.
    tools/.venv/bin/python tools/build.py              # 기본: slides/index.html
    tools/.venv/bin/python tools/build.py practice/index.html
EXTRA에 적은 파일에는 Noto Serif KR 같은 글꼴을 따로 이름 붙여 더 넣는다.
"""
import base64
import io
import re
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "fonts-src" / "NotoSansKR[wght].ttf"
DEFAULT_TARGETS = ["slides/index.html"]
WEIGHTS = (400, 700, 900)
FAMILY = "Slide Sans"
SERIF = ROOT / "tools" / "fonts-src" / "NotoSerifKR[wght].ttf"
# 파일별로 더 넣을 글꼴: (원본, 글꼴 이름, 굵기, 이름, 라이선스 파일)
EXTRA = {
    "examples/reels-golmok/index.html": [(SERIF, "Brand Serif", 900, "Noto Serif KR", "OFL-notoserifkr.txt")],
}
BEGIN, END = "/* FONTS:BEGIN */", "/* FONTS:END */"
BLOCK = re.compile(re.escape(BEGIN) + ".*?" + re.escape(END), re.S)


def used_chars(html: str) -> str:
    """파일 전체 글자(스크립트 속 문구 포함)와 기본 ASCII를 모은다."""
    chars = set(BLOCK.sub("", html))
    chars |= {chr(c) for c in range(0x20, 0x7F)}
    return "".join(sorted(c for c in chars if c == " " or c.isprintable()))


def face(weight: int, text: str, src: Path = SRC, family: str = FAMILY) -> str:
    font = TTFont(src)
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.hinting = False
    opts.layout_features = ["*"]
    sub = subset.Subsetter(opts)
    sub.populate(text=text)
    sub.subset(font)
    static = instantiateVariableFont(font, {"wght": weight})
    static.flavor = "woff2"
    buf = io.BytesIO()
    static.save(buf)
    data = base64.b64encode(buf.getvalue()).decode("ascii")
    return (
        f'@font-face {{ font-family: "{family}"; font-weight: {weight}; font-style: normal; '
        f"font-display: block; src: url(data:font/woff2;base64,{data}) format(\"woff2\"); }}"
    )


def build(rel: str) -> None:
    path = ROOT / rel
    html = path.read_text(encoding="utf-8")
    if not BLOCK.search(html):
        sys.exit(f"{rel}: {BEGIN} ~ {END} 블록이 없어요")
    text = used_chars(html)
    faces = "\n".join(face(w, text) for w in WEIGHTS)
    note = "/* Noto Sans KR, SIL Open Font License 1.1 (fonts/OFL-notosanskr.txt) */"
    for src, family, weight, name, ofl in EXTRA.get(rel, []):
        faces += "\n" + face(weight, text, src, family)
        note += f"\n/* {name}, SIL Open Font License 1.1 (fonts/{ofl}) */"
    html = BLOCK.sub(lambda _: f"{BEGIN}\n{note}\n{faces}\n{END}", html, count=1)
    path.write_text(html, encoding="utf-8")
    print(f"{rel}: 글자 {len(text)}개, {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    if not SRC.exists():
        sys.exit("원본 폰트가 없어요. 먼저 tools/fetch-fonts.sh를 실행하세요.")
    for target in sys.argv[1:] or DEFAULT_TARGETS:
        build(target)
