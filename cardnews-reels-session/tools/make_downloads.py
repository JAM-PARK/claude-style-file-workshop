#!/usr/bin/env python3
"""실습 가이드의 내려받기 파일을 practice/downloads/에 만든다.

    tools/.venv/bin/python tools/make_downloads.py

templates/, checklists/, assets/의 원본을 복사하고 실습용 그림 묶음(zip)을 만든다.
배포 전에 다시 실행한다. downloads/는 만들어지는 폴더라 저장소에 올리지 않는다.
"""
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "practice" / "downloads"
COPIES = [
    "templates/instructions-cosmetics.md",
    "templates/instructions-restaurant.md",
    "templates/reels-brief.md",
    "templates/video-swap-decision.md",
    "checklists/before-posting.md",
]
ZIP_NAME = "practice-assets.zip"
# Windows 탐색기에서 이름이 깨지지 않도록 zip 안 파일 이름은 영문만 쓴다
ZIP_README = """실습용 그림 묶음

루미엘(가상 브랜드)과 골목 한그릇(가상 브랜드)의 로고와 그림이에요.
내 가게 로고나 사진이 없을 때 실습 2, 4, 5에서 Claude에 첨부해 써요.

- lumiel-*: 루미엘 진정 토너 (화장품)
- golmok-*: 골목 한그릇 (동네 국밥집)
- lumiel-toner.png, golmok-takeout.png: 배경을 지운 제품 그림 (실습 5)
- golmok-takeout-cup.png: 같은 포장 용기의 키 큰 컵 모양 (영상 속 용기가 컵 모양일 때)

실습용으로 만든 가상 브랜드라 실제 가게나 제품과 관계없어요.
"""


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for rel in COPIES:
        shutil.copy2(ROOT / rel, OUT / Path(rel).name)

    files = sorted(p for p in (ROOT / "assets").iterdir() if p.suffix in {".png", ".svg"})
    if not files:
        print("assets/에 그림이 없어요. 먼저 tools/render_brand.py를 실행하세요.")
        return 1
    bad = [p.name for p in files if not p.name.isascii()]
    if bad:
        print(f"zip에 넣을 파일 이름은 영문만 써요: {', '.join(bad)}")
        return 1
    with zipfile.ZipFile(OUT / ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as z:
        # 메모장이 한글을 바로 읽도록 BOM을 붙인다
        z.writestr("README.txt", ("\ufeff" + ZIP_README).encode("utf-8"))
        for p in files:
            z.write(p, p.name)

    for p in sorted(OUT.iterdir()):
        print(f"{p.relative_to(ROOT)}  {p.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
