#!/usr/bin/env python3
"""HANDOFF 13장 완료 기준 중 기계로 볼 수 있는 것을 한 번에 점검한다.

    tools/.venv/bin/python tools/verify.py

참석자에게 나가는 파일(장표, 실습 가이드, 템플릿, 체크리스트, README)을 훑는다.
진행자 노트(speaker-notes.md)는 가격·크레딧이 들어가도 되므로 금지 문장만 본다.
마지막에 남은 TODO와 [확인 필요] 목록을 뽑는다.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = re.compile(r"/\* FONTS:BEGIN \*/.*?/\* FONTS:END \*/", re.S)

# 참석자 자료: 있으면 검사하고, 아직 없으면 건너뛴다
ATTENDEE = [
    "slides/index.html",
    "practice/index.html",
    "README.md",
    *[str(p.relative_to(ROOT)) for p in sorted((ROOT / "templates").glob("*.md"))],
    *[str(p.relative_to(ROOT)) for p in sorted((ROOT / "checklists").glob("*.md"))],
]
NOTES = "speaker-notes.md"

# PRODUCT.md "쓰면 안 되는 설명"
BANNED = [
    r"Windows라서",
    r"다섯 번",
    r"영상을 생성해",
    r"공짜로",
    r"유료면 다",
    r"영어라서",
    r"인기가 많아",
    r"꼭 켜세요",
]
# 가격·크레딧 수치 (진행자 노트에만)
PRICE = re.compile(r"\d[\d,]*\s?(?:크레딧|원\b|달러)|크레딧\s?\d|\$\s?\d|월\s?[\d,]+\s?원")
EXTERNAL = re.compile(r"""(?:src|href)\s*=\s*["'](?:https?:)?//""")


def text_of(rel: str) -> str:
    return FONTS.sub("", (ROOT / rel).read_text(encoding="utf-8"))


def main() -> int:
    problems: list[str] = []
    todos: list[str] = []
    files = [f for f in ATTENDEE if (ROOT / f).exists()]
    for rel in files + ([NOTES] if (ROOT / NOTES).exists() else []):
        body = text_of(rel)
        for pat in BANNED:
            for m in re.finditer(pat, body):
                problems.append(f"{rel}: 쓰면 안 되는 설명 '{m.group(0)}'")
        if rel != NOTES:
            for m in PRICE.finditer(body):
                problems.append(f"{rel}: 가격·크레딧 수치 '{m.group(0)}' (진행자 노트에만)")
        for line_no, line in enumerate(body.splitlines(), 1):
            for m in re.finditer(r"TODO[^<\n]*|\[확인 필요[^\]]*\]", line):
                todos.append(f"{rel}:{line_no}: {m.group(0).strip()}")

    # 장표와 실습 가이드: 인터넷 없이 열림, 복사 버튼 수
    for rel in ("slides/index.html", "practice/index.html"):
        if not (ROOT / rel).exists():
            continue
        body = text_of(rel)
        if rel == "slides/index.html":
            for m in EXTERNAL.finditer(body):
                problems.append(f"{rel}: 외부 주소를 불러와요 ({m.group(0)})")
            for word in ("speaker", "발표자 노트", "Direction contract", "seed:"):
                if word in body:
                    problems.append(f"{rel}: 장표에 들어가면 안 되는 '{word}'")
        pres = len(re.findall(r'<div class="sys"', body))
        copies = len(re.findall(r'<div class="sys-h">.*?class="copy', body))
        if pres != copies:
            problems.append(f"{rel}: 프롬프트 {pres}개, 복사 버튼 {copies}개")
        print(f"{rel}: 프롬프트 {pres}개, 복사 버튼 {copies}개")

    # 가상 브랜드 첫 등장 표시
    for rel in files:
        body = re.sub(r"<[^>]+>", "", text_of(rel))
        for brand in ("루미엘", "골목 한그릇"):
            i = body.find(brand)
            if i >= 0 and "가상 브랜드" not in body[i : i + 40]:
                problems.append(f"{rel}: '{brand}' 첫 등장에 (가상 브랜드) 표시가 없어요")

    print(f"\n점검한 파일: {', '.join(files)}")
    if problems:
        print(f"\n고칠 것 {len(problems)}건")
        for p in problems:
            print(" -", p)
    else:
        print("\n고칠 것 없음")
    print(f"\n남은 TODO·[확인 필요] {len(todos)}건")
    for t in todos:
        print(" -", t)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
