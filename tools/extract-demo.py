"""demo/raw/*.json(claude -p 결과)에서 HTML만 꺼내 demo/*.html로 저장한다. 내용은 고치지 않는다."""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
for raw in sorted((root / 'demo/raw').glob('*.json')):
    data = json.loads(raw.read_text())
    text = data.get('result', '')
    m = re.search(r'```(?:html)?\s*\n(.*?)```', text, re.S)
    html = (m.group(1) if m else text).strip()
    start = html.lower().find('<!doctype')
    if start < 0: start = html.lower().find('<html')
    html = html[start:] if start >= 0 else html
    out = root / 'demo' / (raw.stem + '.html')
    out.write_text(html + '\n')
    models = list((data.get('modelUsage') or {}).keys())
    print(f'{out.name}: {len(html)} chars, models={models}, cost=${data.get("total_cost_usd", 0):.2f}')
