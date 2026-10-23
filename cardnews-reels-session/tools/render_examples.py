#!/usr/bin/env python3
"""완성 예시(카드 뉴스 12장, 릴스 페이지)를 examples/copy.md 문구로 만든다. 문구는 copy.md에서만 읽는다.

    tools/.venv/bin/python tools/render_examples.py

- 카드 뉴스: tools/brand-src/cards.html 틀에 문구와 assets/ 그림을 넣어 headless Chrome으로 그린다.
  examples/cardnews-lumiel/01~06.png, examples/cardnews-golmok/01~06.png (1080x1350)
  제목은 한 줄, 본문은 copy.md 한 줄이 한 줄. Chrome에서 덩어리마다 줄 수를 재고, 넘치면 그리지 않고 멈춘다.
- 릴스: tools/brand-src/reels-golmok.html 틀에 문구와 그림(SVG)을 넣고 build.py로 글꼴을 넣는다.
  examples/reels-golmok/index.html, examples/reels-golmok/fonts/(OFL)
그림을 바꿨다면 먼저 tools/render_brand.py를 실행한다.
"""
import base64
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

import build
import render_brand

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "brand-src"
ASSETS = ROOT / "assets"
EXAMPLES = ROOT / "examples"
W, H = 1080, 1350
BRANDS = {
    "lumiel": ("카드 뉴스: 루미엘", [(build.SRC, build.FAMILY, w) for w in (300, 400)]),
    "golmok": ("카드 뉴스: 골목 한그릇", [(build.SRC, build.FAMILY, w) for w in (500, 700)] + [(build.SERIF, "Brand Serif", 900)]),
}
REELS = "릴스: 골목 한그릇"
REELS_PAGE = "examples/reels-golmok/index.html"
BOOKMARK = '<svg viewBox="0 0 30 40" aria-hidden="true"><path d="M 2 4 Q 2 0 6 0 H 24 Q 28 0 28 4 V 38 L 15 29 L 2 38 Z" fill="currentColor"/></svg>'


def parse_copy() -> dict[str, list[list[tuple[str, str]]]]:
    """'## 묶음' 아래 '### 장' 마다 '항목: 값' 줄을 순서대로 모은다."""
    sections: dict[str, list[list[tuple[str, str]]]] = {}
    cur = None
    for line in (EXAMPLES / "copy.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            cur = sections.setdefault(line[3:].strip(), [])
        elif line.startswith("### ") and cur is not None:
            cur.append([])
        elif cur and ": " in line:
            key, _, value = line.partition(": ")
            cur[-1].append((key.strip(), value.strip()))
    return sections


def chrome(page: Path, tmp: Path, *args: str) -> str:
    cmd = [
        render_brand.CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
        "--no-default-browser-check", "--disable-extensions", f"--user-data-dir={tmp / 'profile'}",
        "--force-device-scale-factor=1", "--virtual-time-budget=10000", *args, page.as_uri(),
    ]
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def svg_inline(svg: str) -> str:
    return re.sub(r"<!--.*?-->", "", svg, flags=re.S).strip()


def img(name: str) -> tuple[str, bool]:
    path = ASSETS / name
    if not path.exists():
        sys.exit(f"{name}: assets/에 없어요. 먼저 tools/render_brand.py를 실행하세요.")
    with Image.open(path) as im:
        cutout = im.mode == "RGBA"
    return f"data:image/png;base64,{base64.b64encode(path.read_bytes()).decode('ascii')}", cutout


def card_html(brand: str, n: int, total: int, rows: list[tuple[str, str]]) -> str:
    titles = [v for k, v in rows if k == "제목"]
    bodies = [v for k, v in rows if k == "본문"]
    pics = [v for k, v in rows if k == "그림"]
    if len(titles) != 1 or not 1 <= len(bodies) <= 2 or len(pics) != 1:
        sys.exit(f"{brand} {n}장: 제목 1개, 본문 1~2개, 그림 1개여야 해요")
    kind = "hook" if n == 1 else "cta" if n == total else "body"
    pic = None if pics[0] == "없음" else pics[0]
    if (kind == "cta") != (pic is None):
        sys.exit(f"{brand} {n}장: 그림은 마지막 장에만 '없음'이어야 해요")
    e = html.escape
    logo = svg_inline((ASSETS / f"{brand}-logo.svg").read_text(encoding="utf-8"))
    mark = '<span class="mark">LUMIEL</span>' if brand == "lumiel" else f'<span class="mark">{logo}</span>'
    top = f'<div class="top">{"" if kind == "cta" else mark}<span class="page">{n}/{total}</span></div>'
    accent = '<div class="rule"></div>' if brand == "lumiel" else '<div class="bar"></div>'
    if kind == "cta":
        return (f'<section class="card {brand} cta">{top}<div class="logo">{logo}</div>{accent}'
                f'<h1 data-line="제목">{e(titles[0])}</h1>'
                f'<p class="save">{BOOKMARK}<span data-line="본문">{e(bodies[0])}</span></p></section>')
    src, cutout = img(pic)
    art = f'<figure class="art{" cutout" if cutout else ""}"><img src="{src}" alt=""></figure>'
    copy = (f'<div class="copy">{accent}<h1 data-line="제목">{e(titles[0])}</h1><div class="body">'
            + "".join(f'<p data-line="본문">{e(b)}</p>' for b in bodies) + "</div></div>")
    inner = top + (copy + art if kind == "hook" else art + copy)
    return f'<section class="card {brand} {kind}">{inner}</section>'


def render_cards(sections: dict, tmp: Path) -> list[str]:
    results = []
    template = (SRC / "cards.html").read_text(encoding="utf-8")
    for brand, (section, faces) in BRANDS.items():
        cards = sections[section]
        if len(cards) != 6:
            sys.exit(f"{section}: 6장이어야 해요 ({len(cards)}장)")
        body = "\n".join(card_html(brand, i + 1, len(cards), rows) for i, rows in enumerate(cards))
        page = template.replace("<!-- CARDS -->", body)
        text = build.used_chars(page)
        css = "\n".join(build.face(w, text, src, fam) for src, fam, w in faces)
        page = build.BLOCK.sub(lambda _: f"{build.BEGIN}\n{css}\n{build.END}", page, count=1)
        path = tmp / f"cards-{brand}.html"
        path.write_text(page, encoding="utf-8")

        # 1) 줄 수 재기: 제목·본문 덩어리마다 1줄이어야 하고 카드 안에 들어가야 한다
        dom = chrome(path, tmp, "--dump-dom")
        m = re.search(r'data-report="([^"]*)"', dom)
        if not m:
            sys.exit(f"{brand}: Chrome에서 줄 수를 재지 못했어요")
        report = json.loads(html.unescape(m.group(1)))
        unloaded = [f for f in report["faces"] if not f.endswith("loaded")]
        if unloaded:
            sys.exit(f"{brand}: 글꼴이 안 불러졌어요 {unloaded}")
        bad = [it for it in report["items"] if it["rects"] != 1 or it["byHeight"] != 1 or not it["inside"] or it["overflow"]]
        for it in report["items"]:
            results.append(f"{brand} {it['card']}/6 {it['kind']}: {it['rects']}줄 (높이로 {it['byHeight']}줄) {it['text']}")
        if bad:
            for it in bad:
                print(f"넘침: {brand} {it['card']}장 {it['kind']} '{it['text']}' {it['rects']}줄, 카드 안 {it['inside']}")
            sys.exit(f"{brand}: 줄이 넘친 글자가 있어서 그리지 않았어요")
        expected = [v for rows in cards for k, v in rows if k in ("제목", "본문")]
        if [it["text"] for it in report["items"]] != expected:
            sys.exit(f"{brand}: 카드에 그려진 제목·본문이 copy.md와 달라요")

        # 2) 그리기: 6장을 세로로 이어 한 번에 찍고 잘라 낸다
        shot = tmp / f"cards-{brand}.png"
        chrome(path, tmp, f"--window-size={W},{H * len(cards)}", f"--screenshot={shot}")
        sheet = Image.open(shot).convert("RGB")
        if sheet.size != (W, H * len(cards)):
            sys.exit(f"{brand}: 찍힌 크기가 {sheet.size}예요")
        out = EXAMPLES / f"cardnews-{brand}"
        out.mkdir(parents=True, exist_ok=True)
        for i in range(len(cards)):
            png = out / f"{i + 1:02d}.png"
            sheet.crop((0, i * H, W, (i + 1) * H)).save(png, optimize=True)
            render_brand.finish(png, W, H)
            print(f"{png.relative_to(ROOT)}: {W}x{H}, {png.stat().st_size // 1024} KB")
    return results


def render_reels(sections: dict) -> None:
    scenes = sections[REELS]
    rows = [r for scene in scenes for r in scene]
    hook, feats, cta, pic, logo = ([v for k, v in rows if k == key] for key in ("훅", "특징", "행동 요청", "그림", "로고"))
    if len(scenes) != 3 or len(hook) != 1 or len(feats) != 2 or len(cta) != 1:
        sys.exit(f"{REELS}: 장면 3개, 훅 1개, 특징 2개, 행동 요청 1개여야 해요")
    if pic != ["golmok-gukbap.png"] or logo != ["golmok-logo.png"]:
        sys.exit(f"{REELS}: 그림·로고 파일이 바뀌었어요 ({pic}, {logo}). 이 스크립트의 SVG 연결을 고쳐요")
    trees = render_brand.process(["golmok-gukbap.svg", "golmok-logo.svg"])
    svg = {k: ET.tostring(v, encoding="unicode") for k, v in trees.items()}
    e = html.escape
    page = (SRC / "reels-golmok.html").read_text(encoding="utf-8")
    for marker, value in (("<!--HOOK-->", e(hook[0])), ("<!--F1-->", e(feats[0])), ("<!--F2-->", e(feats[1])),
                          ("<!--CTA-->", e(cta[0])), ("<!--ART-->", svg_inline(svg["golmok-gukbap.svg"])),
                          ("<!--LOGO-->", svg_inline(svg["golmok-logo.svg"]))):
        if page.count(marker) != 1:
            sys.exit(f"reels-golmok.html: {marker} 자리가 1개여야 해요")
        page = page.replace(marker, value)
    out = ROOT / REELS_PAGE
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    build.build(REELS_PAGE)
    fonts = out.parent / "fonts"
    fonts.mkdir(exist_ok=True)
    for ofl in ("OFL-notosanskr.txt", "OFL-notoserifkr.txt"):
        shutil.copy2(ROOT / "tools" / "fonts-src" / ofl, fonts / ofl)


def main() -> None:
    sections = parse_copy()
    with tempfile.TemporaryDirectory() as t:
        results = render_cards(sections, Path(t))
    render_reels(sections)
    print("\n줄 수 점검 (Chrome에서 잰 값, 모두 1줄)")
    for line in results:
        print(" ", line)


if __name__ == "__main__":
    main()
