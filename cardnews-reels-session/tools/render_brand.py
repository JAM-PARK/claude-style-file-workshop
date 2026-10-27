#!/usr/bin/env python3
"""가상 브랜드(루미엘, 골목 한그릇)의 실습용 로고와 그림을 tools/brand-src/의 SVG에서 assets/로 그린다.

    tools/.venv/bin/python tools/render_brand.py

- 원본 SVG의 <text>는 Noto Sans KR·Noto Serif KR(OFL) 글자 윤곽선(path)으로 바꿔 그린다.
  설치된 폰트와 상관없이 똑같이 나온다. dominant-baseline="central"이면 y가 글자 높이의 가운데,
  text-anchor="middle"이면 x가 글자 너비의 가운데다(실제 윤곽 기준).
- <use href="부품파일.svg#id">는 다른 파일의 부품(병, 간판)을 그 자리에 복사해 넣는다.
  부품 안에는 id를 두지 않는다(여러 번 넣어도 겹치지 않게).
- 이름이 -logo.svg인 원본은 윤곽선으로 바꾼 SVG도 assets/에 내보낸다.
- PNG는 headless Chrome으로 그린다. 크기는 원본 SVG의 width·height를 따른다.
"""
import copy
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from fontTools import subset
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "brand-src"
OUT = ROOT / "assets"
FONTS = {
    "Noto Sans KR": ROOT / "tools" / "fonts-src" / "NotoSansKR[wght].ttf",
    "Noto Serif KR": ROOT / "tools" / "fonts-src" / "NotoSerifKR[wght].ttf",
}
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
BUDGET = 300 * 1024  # 참석자가 현장 와이파이로 받으므로 한 장에 300 KB 안쪽

# 그릴 원본 (assets/에 같은 이름의 .png가 생긴다)
JOBS = [
    "lumiel-logo.svg",
    "lumiel-toner.svg",
    "lumiel-pad.svg",
    "lumiel-drop.svg",
    "lumiel-shelf.svg",
    "golmok-logo.svg",
    "golmok-takeout.svg",
    "golmok-takeout-cup.svg",  # 실습 5 시연 원본 영상의 키 큰 컵에 맞춘 비율
    "golmok-gukbap.svg",
    "golmok-table.svg",
    "golmok-store.svg",
]

NS = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", NS)
ET.register_namespace("xlink", XLINK)
TEXT, USE, PATH, G = (f"{{{NS}}}{t}" for t in ("text", "use", "path", "g"))
HREFS = ("href", f"{{{XLINK}}}href")
# <text>에서 <path>로 옮겨 갈 그리기 속성
KEEP = ("fill", "fill-opacity", "opacity", "transform", "stroke", "stroke-width", "stroke-linejoin")


def num(v: float) -> str:
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


# ---------- 부품 넣기 ----------

_parts: dict[str, ET.Element] = {}


def part(ref: str) -> ET.Element:
    file, _, pid = ref.partition("#")
    if file not in _parts:
        _parts[file] = ET.parse(SRC / file).getroot()
    found = _parts[file].find(f".//*[@id='{pid}']")
    if found is None:
        sys.exit(f"{ref}: 부품을 찾을 수 없어요")
    el = copy.deepcopy(found)
    for e in el.iter():
        e.attrib.pop("id", None)
    return el


def inline_parts(node: ET.Element) -> None:
    for i, child in enumerate(list(node)):
        href = next((child.get(h) for h in HREFS if child.get(h)), "")
        if child.tag == USE and ".svg#" in href:
            g = ET.Element(G)
            moves = [child.get("transform", "")]
            if child.get("x") or child.get("y"):
                moves.append(f"translate({child.get('x', '0')} {child.get('y', '0')})")
            if " ".join(m for m in moves if m):
                g.set("transform", " ".join(m for m in moves if m))
            for k in ("opacity", "fill"):
                if child.get(k):
                    g.set(k, child.get(k))
            g.append(part(href))
            node.remove(child)
            node.insert(i, g)
            child = g
        inline_parts(child)


# ---------- 글자를 윤곽선으로 ----------


def text_of(el: ET.Element) -> str:
    return " ".join("".join(el.itertext()).split())


def font_key(el: ET.Element) -> tuple[str, int]:
    family = el.get("font-family", "Noto Sans KR").strip("'\"")
    if family not in FONTS:
        sys.exit(f"'{family}': 쓸 수 있는 글꼴은 {', '.join(FONTS)}예요")
    return family, int(el.get("font-weight", "400"))


def load_fonts(needs: dict[tuple[str, int], set[str]]) -> dict:
    fonts = {}
    for (family, weight), chars in needs.items():
        font = TTFont(FONTS[family])
        opts = subset.Options()
        opts.layout_features = []
        opts.hinting = False
        opts.notdef_outline = True
        sub = subset.Subsetter(opts)
        sub.populate(text="".join(sorted(chars | {" "})))
        sub.subset(font)
        font = instantiateVariableFont(font, {"wght": weight})
        cmap = font.getBestCmap()
        missing = sorted(c for c in chars if ord(c) not in cmap)
        if missing:
            sys.exit(f"{family} {weight}: 글꼴에 없는 글자 {missing}")
        fonts[(family, weight)] = (font.getGlyphSet(), cmap, font["hmtx"], font["head"].unitsPerEm)
    return fonts


def outline(el: ET.Element, fonts: dict) -> ET.Element:
    glyphs, cmap, hmtx, upm = fonts[font_key(el)]
    s = text_of(el)
    size = float(el.get("font-size", "16"))
    spacing = float(el.get("letter-spacing", "0"))
    scale = size / upm
    placed, pen_x = [], 0.0
    for i, ch in enumerate(s):
        name = cmap[ord(ch)]
        placed.append((name, pen_x))
        pen_x += hmtx[name][0] * scale + (spacing if i < len(s) - 1 else 0)

    def draw(pen, dx: float, dy: float) -> None:
        for name, gx in placed:
            glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, dx + gx, dy)))

    bounds = BoundsPen(glyphs)
    draw(bounds, 0, 0)
    x0, y0, x1, y1 = bounds.bounds
    x, y = float(el.get("x", "0")), float(el.get("y", "0"))
    anchor = el.get("text-anchor", "start")
    dx = {"start": 0.0, "middle": -(x0 + x1) / 2, "end": -pen_x}[anchor]
    dy = -(y0 + y1) / 2 if el.get("dominant-baseline") in ("central", "middle") else 0.0
    pen = SVGPathPen(glyphs, ntos=num)
    draw(pen, x + dx, y + dy)
    path = ET.Element(PATH, {"d": pen.getCommands()})
    for k in KEEP:
        if el.get(k):
            path.set(k, el.get(k))
    return path


def replace_texts(node: ET.Element, fonts: dict) -> None:
    for i, child in enumerate(list(node)):
        if child.tag == TEXT:
            node.remove(child)
            node.insert(i, outline(child, fonts))
        else:
            replace_texts(child, fonts)


# ---------- 그리기 ----------


def rasterize(svg: str, w: int, h: int, png: Path, tmp: Path) -> None:
    (tmp / "page.svg").write_text(svg, encoding="utf-8")
    (tmp / "page.html").write_text(
        "<!doctype html><meta charset=utf-8><style>html,body{margin:0;background:transparent;overflow:hidden}"
        f"img{{display:block}}</style><img src=page.svg width={w} height={h}>",
        encoding="utf-8",
    )
    cmd = [
        CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
        "--no-default-browser-check", "--disable-extensions", f"--user-data-dir={tmp / 'profile'}",
        "--force-device-scale-factor=1", "--default-background-color=00000000",
        f"--window-size={w},{h}", f"--screenshot={png}", (tmp / "page.html").as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def finish(png: Path, w: int, h: int) -> None:
    im = Image.open(png)
    if im.size != (w, h):
        sys.exit(f"{png.name}: 크기가 {im.size}로 나왔어요 ({w}x{h}이어야 해요)")
    im = im.convert("RGBA")
    if im.getextrema()[3][0] == 255:  # 투명한 곳이 없으면 RGB로
        im = im.convert("RGB")
    im.save(png, optimize=True)
    if png.stat().st_size > BUDGET:
        method = Image.Quantize.FASTOCTREE if im.mode == "RGBA" else Image.Quantize.MEDIANCUT
        im.quantize(256, method=method, dither=Image.Dither.NONE).save(png, optimize=True)


def process(names: list[str]) -> dict[str, ET.Element]:
    """원본 SVG에 부품을 넣고 글자를 윤곽선으로 바꾼다. 릴스 페이지(render_examples.py)도 쓴다."""
    missing = [p for p in FONTS.values() if not p.exists()]
    if missing:
        sys.exit("원본 폰트가 없어요. 먼저 tools/fetch-fonts.sh를 실행하세요.")
    trees = {}
    for name in names:
        root = ET.parse(SRC / name).getroot()
        inline_parts(root)
        trees[name] = root
    needs: dict[tuple[str, int], set[str]] = {}
    for root in trees.values():
        for el in root.iter(TEXT):
            needs.setdefault(font_key(el), set()).update(text_of(el))
    fonts = load_fonts(needs)
    for root in trees.values():
        replace_texts(root, fonts)
        ET.indent(root)
    return trees


def main() -> None:
    trees = process(JOBS)
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        for name, root in trees.items():
            svg = ET.tostring(root, encoding="unicode")
            w, h = int(float(root.get("width"))), int(float(root.get("height")))
            stem = name.removesuffix(".svg")
            if stem.endswith("-logo"):
                (OUT / name).write_text(svg + "\n", encoding="utf-8")
            png = OUT / f"{stem}.png"
            rasterize(svg, w, h, png, tmp)
            finish(png, w, h)
            print(f"assets/{png.name}: {w}x{h}, {png.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
