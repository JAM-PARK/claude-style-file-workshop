"""배포 페이지(handout/index.html)의 내용 칸을 md 원본에서 다시 채운다. tools/build.py가 부른다.

원본이 바뀌면 이 스크립트만 다시 돌리면 된다. 배포 페이지 안의 글을 손으로 고치지 않는다.
"""
import base64, html, re

E = html.escape


# ---------- 작은 md 렌더러 (제목, 문단, 목록, 코드, 인용, 표, 굵게, 코드, 링크) ----------
def inline(s):
    s = E(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    return s


class Ids:
    n = 0
    @classmethod
    def next(cls):
        cls.n += 1
        return f'c{cls.n}'


def src_block(text, copy_text=None, label='복사'):
    cid = Ids.next()
    data = '' if copy_text is None else f' data-copy="{E(copy_text)}"'
    return (f'<div class="src-wrap"><button class="copy" type="button" data-target="{cid}"{data} aria-label="{label}">복사</button>'
            f'<pre class="src" id="{cid}">{E(text)}</pre></div>')


def md(text, shift=1):
    """md → html. shift만큼 제목 단계를 내린다."""
    out, lines, i = [], text.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            out.append(src_block('\n'.join(lines[i + 1:j])))
            i = j + 1; continue
        m = re.match(r'(#{1,6}) (.*)', l)
        if m:
            lvl = min(6, len(m.group(1)) + shift)
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>'); i += 1; continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            head, body = rows[0], rows[1:]
            out.append('<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>'
                       + ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in body) + '</tbody></table></div>')
            continue
        if l.startswith('> '):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i][1:].strip()); i += 1
            out.append('<p class="muted">' + '<br>'.join(inline(b) for b in buf if b) + '</p>'); continue
        if re.match(r'\s*[-*] ', l):
            items = []
            while i < len(lines) and re.match(r'\s*[-*] ', lines[i]):
                items.append(re.sub(r'\s*[-*] ', '', lines[i], count=1)); i += 1
            out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>'); continue
        if re.match(r'\d+\. ', l):
            items = []
            while i < len(lines) and (re.match(r'\d+\. ', lines[i]) or lines[i].startswith('   ')):
                if re.match(r'\d+\. ', lines[i]):
                    items.append([re.sub(r'\d+\. ', '', lines[i], count=1)])
                else:
                    items[-1].append(lines[i].strip())
                i += 1
            rendered = []
            for it in items:
                head, rest = it[0], it[1:]
                inner = inline(head)
                if rest and rest[0].startswith('```'):
                    code = [r for r in rest[1:] if not r.startswith('```')]
                    inner += src_block('\n'.join(code))
                elif rest:
                    subs = [x[2:] for x in rest if x.startswith('- ')]
                    inner += '<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in subs) + '</ul>'
                rendered.append(f'<li>{inner}</li>')
            out.append('<ol>' + ''.join(rendered) + '</ol>'); continue
        if l.strip() == '':
            i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'(#|```|\||> |\s*[-*] |\d+\. )', lines[i]):
            buf.append(lines[i]); i += 1
        out.append('<p>' + '<br>'.join(inline(b) for b in buf) + '</p>')
    return '\n'.join(out)


# ---------- 디자인 시스템 파일(템플릿·예시)을 칸 모양으로 보여주기 ----------
HINT = re.compile(r'\(([^()]*?)\)')


def blank(text):
    """템플릿의 '예:' 채움 예시를 지운 빈칸 원문 (복사용)."""
    def fix(m):
        inner = m.group(1)
        if '예:' not in inner:
            return m.group(0)
        kept = re.split(r'\.?\s*예:', inner)[0].strip()
        return f'({kept})' if kept else ''
    out = [HINT.sub(fix, l).rstrip() for l in text.split('\n')]
    return '\n'.join(out) + '\n'


def show_hints(line_html):
    return re.sub(r'\(([^()]*?예:[^()]*?)\)', r'<span class="hint">(\1)</span>', line_html)


def ds_card(text, copy_text=None, hints=False):
    lines = text.rstrip('\n').split('\n')
    title = lines[0].lstrip('# ').strip()
    secs, head_lines, curname = [], [], None
    for l in lines[1:]:
        if l.startswith('## '):
            curname = l[3:].strip(); secs.append([curname, []])
        elif curname is None:
            if l.strip():
                head_lines.append(l.lstrip('> ').strip())
        else:
            secs[-1][1].append(l)
    parts = [f'<div class="ds"><h3 class="ds-title">{E(title)}</h3>']
    if head_lines:
        parts.append('<p class="tag">' + '<br>'.join(E(h) for h in head_lines) + '</p>')
    for name, body in secs:
        body = [b for b in body]
        while body and not body[-1].strip():
            body.pop()
        esc = [E(b) for b in body]
        if hints:
            esc = [show_hints(b) for b in esc]
        if '쓰지 말 것' in name:
            items = ''.join(f'<li><span class="nostitch"></span><span>{e[2:] if e.startswith("- ") else e}</span></li>' for e in esc if e.strip())
            parts.append(f'<div class="ds-sec dont"><h4>{E(name.replace("← 가장 중요한 칸", "").strip())}<span class="tag"> 가장 중요한 칸</span></h4><ul>{items}</ul></div>')
        else:
            parts.append(f'<div class="ds-sec"><h4>{E(name)}</h4><pre class="ds-body">' + '\n'.join(esc) + '</pre></div>')
    parts.append('</div>')
    cid = Ids.next()
    raw = text if copy_text is None else copy_text
    return (f'<div class="src-wrap"><div class="actions"><button class="copy" type="button" data-target="{cid}" aria-label="파일 전체 복사">복사</button>'
            f'<button class="save" type="button" data-target="{cid}" data-name="design-system.md">파일로 받기</button></div>'
            + ''.join(parts) + f'<textarea hidden id="{cid}">{E(raw)}</textarea></div>')


SAVER = ('<div class="saver"><label class="tag" for="saver-code">결과물 코드 붙여 넣는 칸</label>'
         '<textarea id="saver-code" spellcheck="false" autocomplete="off" placeholder="&lt;!doctype html&gt; 로 시작하는 코드를 여기에 붙여 넣으세요"></textarea>'
         '<button class="save" type="button" data-target="saver-code" data-name="index.html">index.html로 받기</button></div>')


def chips(text):
    vals = []
    for l in text.split('\n'):
        m = re.match(r'(배경|카드·면|글자|보조 글자|강조|테두리):\s+(#[0-9A-Fa-f]{6})', l)
        if m:
            vals.append(m.group(2))
    return '<span class="chips" aria-hidden="true">' + ''.join(f'<i style="background:{v}"></i>' for v in vals) + '</span>'


def img(path, alt):
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f'<img src="data:image/webp;base64,{b64}" alt="{E(alt)}">'


def prompt_blocks(text):
    """prompts.md: '## 제목' + (설명 문단) + 코드 블록 → 카드들."""
    out = []
    for chunk in re.split(r'\n(?=## )', text):
        if not chunk.startswith('## '):
            continue
        title, _, rest = chunk.partition('\n')
        m = re.search(r'```\n(.*?)```', rest, re.S)
        if not m:
            continue
        desc = rest[:m.start()].strip()
        out.append(f'<h3>{inline(title[3:])}</h3>' + (f'<p class="muted">{inline(desc)}</p>' if desc else '') + src_block(m.group(1).rstrip('\n')))
    return '\n'.join(out)


def build(ROOT, between, qr_svg, site_url):
    r = lambda p: (ROOT / p).read_text(encoding='utf-8')
    doc = r('handout/index.html')
    Ids.n = 0
    why = r('template/why.md').split('\n', 2)[2]
    ab = ''.join(f'<figure><div class="swatch">{img(ROOT / p, alt)}</div><figcaption class="tag">{cap}</figcaption></figure>' for p, alt, cap in [
        ('slides/assets/ab-web-without.webp', '스타일 파일 없이 만든 반찬 구독 소개 웹페이지: 크림 배경, 가운데 정렬, 이모지 카드 3개, 주황 둥근 버튼', '파일 없이'),
        ('slides/assets/ab-web-with.webp', '예시 A 스타일 파일을 설정하고 만든 웹페이지: 흰 바탕, 왼쪽 정렬 명조 제목, 오미자색 버튼 하나', '예시 A 파일을 설정하고'),
    ])
    doc = between(doc, 'WHY', md(why, shift=1).replace('<p>[[AB]]</p>', ab))
    tpl = r('template/design-system.md')
    doc = between(doc, 'TEMPLATE', ds_card(tpl, copy_text=blank(tpl), hints=True))
    examples = [
        ('EXA', 'examples/a-banchan-subscription.md', 'handout/.previews/A.webp', '예시 A 파일을 설정하고 만든 반찬 구독 소개 웹페이지'),
        ('EXB', 'examples/b-logistics-b2b.md', 'handout/.previews/B.webp', '예시 B 파일을 설정하고 만든 물류 제안 슬라이드 첫 장'),
        ('EXC', 'examples/c-quality-report.md', 'handout/.previews/C.webp', '예시 C 파일을 설정하고 만든 품질 주간 보고 서식'),
    ]
    doc = between(doc, 'EXADIMG', img(ROOT / 'handout/.previews/A-detail.webp', '예시 A 파일을 설정하고 시작 3 프롬프트로 만든 반찬 구독 상세페이지 (가로 860px)'))
    for key, path, prev, alt in examples:
        t = r(path)
        doc = between(doc, key + 'CHIPS', chips(t))
        doc = between(doc, key + 'IMG', img(ROOT / prev, alt))
        doc = between(doc, key, ds_card(t))
    doc = between(doc, 'PROMPTS', prompt_blocks(r('prompts/prompts.md')))
    take = re.sub(r'<!--.*?-->\n', '', r('template/take-home.md').split('\n', 2)[2])  # md 원본용 주석은 빼고
    doc = between(doc, 'TAKEHOME', md(take, shift=1).replace('<p>[[SAVER]]</p>', SAVER))
    setup = r('template/README.md').split('\n', 2)[2]  # 첫 제목 줄 제외
    doc = between(doc, 'SETUP', md(setup, shift=1))
    guide = r('advanced/track-guide.md').split('\n', 2)[2]
    doc = between(doc, 'GUIDE', md(guide, shift=1))
    doc = between(doc, 'ADVCLAUDE', src_block(r('advanced/starter/CLAUDE.md').rstrip('\n')))
    doc = between(doc, 'ADVDS', src_block(r('advanced/starter/docs/design-system.md').rstrip('\n')))
    adv = r('advanced/prompts.md').split('\n', 2)[2]
    doc = between(doc, 'ADVPROMPTS', md(adv, shift=1))
    fig = r('advanced/figma-mcp.md').split('\n', 2)[2]
    doc = between(doc, 'FIGMA', md(fig, shift=1))
    doc = between(doc, 'QR', qr_svg(site_url()))
    doc = between(doc, 'URL', E(site_url()))
    (ROOT / 'handout/index.html').write_text(doc, encoding='utf-8')
    return doc
