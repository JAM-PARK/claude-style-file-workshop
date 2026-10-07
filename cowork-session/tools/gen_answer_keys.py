"""facilitator/answer-keys.md를 sample_data.py와 gen_samples.py의 정의로 만든다.

실행: tools/.venv/bin/python tools/gen_answer_keys.py
손으로 고치지 말고 데이터를 고친 뒤 다시 만든다. 교차 검증은 tools/verify_samples.py.
"""
import collections
import pathlib

import gen_samples as G
import sample_data as D

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'facilitator/answer-keys.md'


def won(n):
    return f'{n:,}원'


def receipts():
    uniq = [r for r in D.RECEIPTS if 'dup_of' not in r]
    dup = [r for r in D.RECEIPTS if 'dup_of' in r]
    by_id = {r['id']: r for r in D.RECEIPTS}
    total = sum(D.receipt_total(r) for r in uniq)
    cat = collections.OrderedDict()
    pay = collections.Counter()
    for r in sorted(uniq, key=lambda r: r['date']):
        cat[r['category']] = cat.get(r['category'], 0) + D.receipt_total(r)
        pay[r['pay']] += D.receipt_total(r)
    L = ['## 샘플 01: 영수증 → 지출표 (시연 1, 미션 A)', '',
         f'사진 {len(D.RECEIPTS)}장, 실제 영수증 {len(uniq)}건. 1건은 같은 영수증을 다시 찍은 사진이다.', '',
         '### 정답 지출표', '', '| 날짜 | 상호 | 분류 | 금액 | 결제수단 | 파일 |', '| --- | --- | --- | ---: | --- | --- |']
    for r in sorted(uniq, key=lambda r: r['date']):
        store = '택시' if r['kind'] == 'taxi' else r['store']
        L.append(f"| {r['date']} | {store} | {r['category']} | {won(D.receipt_total(r))} | {r['pay']} | {r['file']} |")
    L += ['', f'**합계 {won(total)}** (중복 사진은 빼고 계산)', '', '### 분류별 합계', '', '| 분류 | 합계 |', '| --- | ---: |']
    for k, v in sorted(cat.items(), key=lambda kv: -kv[1]):
        L.append(f'| {k} | {won(v)} |')
    L += ['', '### 결제수단별 합계', '', '| 결제수단 | 합계 |', '| --- | ---: |']
    for k, v in pay.most_common():
        L.append(f'| {k} | {won(v)} |')
    L += ['', '### 중복 의심']
    for r in dup:
        o = by_id[r['dup_of']]
        L.append(f"- `{r['file']}`는 `{o['file']}`와 같은 영수증이다 ({o['date']} {o['store']} {won(D.receipt_total(o))}). "
                 '사진 파일 날짜는 다르지만 상호·일시·금액이 같다. 중복을 빼지 않으면 합계가 '
                 f'{won(total + D.receipt_total(o))}이 나온다.')
    L += ['', '### 잘 됐는지 확인하는 법',
          f'- 행이 {len(uniq)}개인가 (사진 {len(D.RECEIPTS)}장이 아니라)',
          f'- 합계가 {won(total)}인가',
          '- 중복 의심 1건을 따로 알려 줬는가',
          '- 흐릿한 사진 2장(' + ', '.join(f"`{r['file']}`" for r in D.RECEIPTS if r.get('blur')) + ')의 금액을 맞게 읽었는가',
          '- 온라인 결제 캡처 3장(파일 이름이 Screenshot_으로 시작)도 포함했는가',
          '- 분류 이름은 참석자마다 달라도 된다. 금액과 건수가 맞으면 성공으로 본다.', '']
    return L, total


def downloads():
    L = ['## 샘플 02: 다운로드 폴더 정리 (미션 B)', '',
         f'파일 {len(G.DOWNLOADS)}개. 파일 이름만 봐서는 무엇인지 알 수 없는 것이 많아서 열어 봐야 분류할 수 있다.', '',
         '### 기대하는 폴더 구조', '', '```', '느린오븐_정리/']
    groups = collections.OrderedDict()
    for f in sorted(G.DOWNLOADS, key=lambda f: (f['project'], f['date'])):
        groups.setdefault(f['project'], []).append(f)
    for proj, items in groups.items():
        L.append(f'├── {proj}/ ({len(items)}개)')
    L += ['```', '', '폴더 이름과 나누는 방식은 달라도 된다. 프로젝트(일) 기준으로 묶었는지가 핵심이다.', '',
          '### 파일 이름 규칙 (예시)', '', '`날짜_프로젝트_문서종류_내용_버전.확장자` 예: `2026-09-06_추석선물세트_안내문구_v2.docx`', '',
          '### 파일별 정답', '', '| 원래 이름 | 실제 내용 | 폴더 | 새 이름 예시 | 메모 |', '| --- | --- | --- | --- | --- |']
    for proj, items in groups.items():
        for f in items:
            L.append(f"| {f['name']} | {f['doctype']} | {proj} | {f['newname']} | {f['note']} |")
    traps = [
        ('견적서(3).pdf', '홈페이지 견적이 아니라 리본 견적이다 (추석선물세트).'),
        ('다운로드.pdf', '위생교육 수료증이다.'),
        ('계약서_스캔.pdf', '계약서가 아니라 임대료 조정 안내문이다.'),
        ('최종.docx / 최종_진짜최종.docx', '이름과 달리 "최종.docx"가 구버전이다. 안의 가격과 세트 수로 구별한다.'),
        ('견적서(1).pdf / 견적서(2).pdf', '같은 상자 견적의 300개 판과 200개 판. 회의에서 200개로 정했다.'),
        ('가격표.xlsx / 메뉴판_수정.xlsx', '가격표.xlsx가 구버전이다 (버터쿠키 1,700원 → 2,200원).'),
        ('사진.zip', '압축 안에 신메뉴 사진 3장. 풀어서 메뉴판리뉴얼로 보내면 더 좋다.'),
    ]
    L += ['', '### 놓치기 쉬운 파일', ''] + [f'- `{a}`: {b}' for a, b in traps]
    L += ['', '### 잘 됐는지 확인하는 법',
          '- 원본을 지우지 않고 정리했는가 (복사본에서 작업하도록 안내)',
          '- 구버전과 최신본을 구별했는가 (위 표의 메모 칸)',
          '- 정리 보고서에 "옮긴 파일 목록"과 "판단이 애매한 파일"이 있는가',
          '- 파일을 영구 삭제하려 하면 Claude가 먼저 허락을 구한다. 이번 미션에서는 삭제하지 않는 것이 정답이다.', '']
    return L


def quotes():
    L = ['## 샘플 03: 견적서 비교 (미션 C)', '',
         f"비교 기준(`요청사항.txt`): {D.REQUEST['pages']}, {D.REQUEST['feature']}, {D.REQUEST['period']}", '',
         '### 겉으로 보이는 금액과 1년 실질 비용', '', '| 업체 | 첫 장에 크게 보이는 금액 | 1년 실질 비용 (VAT 포함) |', '| --- | --- | ---: |']
    totals = {}
    for q in D.QUOTES:
        t = D.quote_year_total(q)
        totals[q['id']] = t
        L.append(f"| {q['id']} {q['vendor']} | {won(D.quote_headline(q))} ({q['headline_note'].split('(')[-1].rstrip(')')}) | **{won(t)}** |")
    order = sorted(D.QUOTES, key=lambda q: totals[q['id']])
    L += ['', '순위 (싼 순): ' + ' < '.join(f"{q['id']} {q['vendor']} {won(totals[q['id']])}" for q in order), '',
          '겉 금액으로는 바른픽셀(150만 원)이 가장 싸 보이지만, 조건을 다 넣으면 네모난창 디자인이 가장 싸다.', '',
          '### 계산 내역']
    for q in D.QUOTES:
        L += ['', f"**{q['id']} {q['vendor']}** ({q['file']})", '', '| 항목 | 금액 | VAT | 1년 비용에 넣는 금액 |', '| --- | ---: | --- | ---: |']
        for name, amount, vat_in in q['year']:
            L.append(f"| {name} | {won(amount)} | {'포함' if vat_in else '별도 (+10%)'} | {won(amount if vat_in else round(amount * 1.1))} |")
        L.append(f"| **합계** | | | **{won(totals[q['id']])}** |")
    L += ['', '### 놓치기 쉬운 조건']
    for q in D.QUOTES:
        L += [f"- {q['vendor']}: " + '; '.join(q['hidden'])]
    L += ['', '### 잘 됐는지 확인하는 법',
          '- 세 업체의 항목 이름이 달라도 같은 줄에 맞춰 놓았는가 (제작, 예약 기능, 유지보수, 도메인·호스팅)',
          '- VAT 포함과 별도를 맞춰서 비교했는가',
          '- 각주(아래 작은 글씨)의 조건을 비용에 넣었는가',
          '- 계산 기준이 조금 달라도(예: 유지보수 기간을 다르게 본 경우) 이유를 적었다면 성공으로 본다.', '']
    return L, totals


def meeting():
    m = D.MEETING
    L = ['## 샘플 04: 회의 녹취 → 회의록 (미션 D, 예비용)', '',
         f"{m['date']} {m['place']}. 참석: " + ', '.join(f'{n}({r})' for n, r in m['people']) + '. 녹취 약 20분.', '',
         '### 결정 사항'] + [f'- {d}' for d in m['decisions']]
    L += ['', '### 할 일 표', '', '| 담당 | 할 일 | 기한 |', '| --- | --- | --- |']
    for who, what, due in sorted(m['actions'], key=lambda a: a[2]):
        L.append(f'| {who} | {what} | {due} |')
    L += ['', '### 보류'] + [f'- {p}' for p in m['pending']]
    L += ['', '### 후속 메일 초안 (예시)', '', '```',
          '제목: 9/5 추석 선물세트·홈페이지 회의 정리', '',
          '세린 님, 소이 씨, 오늘 회의 내용을 정리해 보냅니다.', '',
          '[결정]', '- 선물세트 2종: 쿠키 세트 28,000원, 파운드 세트 42,000원',
          '- 예약 마감 9/19(토), 매장 수령 9/22(화)~9/24(목)', '- 예약은 이번에는 SNS 메시지와 전화로 받고 표에 정리', '',
          '[할 일]'] + [f'- {who}: {what} ({due[5:].replace("-", "/")}까지)' for who, what, due in sorted(m['actions'], key=lambda a: a[2])] + [
          '', '[보류]'] + [f'- {p}' for p in m['pending']] + ['', '빠진 내용이 있으면 알려 주세요.', '윤하늘 드림', '```', '',
          '### 잘 됐는지 확인하는 법',
          f"- 할 일 {len(m['actions'])}개를 담당자와 기한까지 모두 뽑았는가",
          '- "보류"와 "결정"을 섞지 않았는가 (리본 색, 택배 여부)',
          '- 말버릇("음", "어", "그니까")과 잡담을 빼고 정리했는가',
          '- 녹취 속 날짜가 한글 숫자("십이일")로 되어 있어도 9/12처럼 바르게 옮겼는가', '']
    return L


def main():
    rl, rtotal = receipts()
    ql, qtotals = quotes()
    L = ['# 샘플 정답지', '',
         '> 이 파일은 `tools/gen_answer_keys.py`가 `tools/sample_data.py`로 만든다. 손으로 고치지 말고 데이터를 고친 뒤 다시 만든다.',
         '> 샘플과 숫자가 맞는지는 `tools/verify_samples.py`로 확인한다. 모든 이름·번호는 가상이다.', '',
         '| 샘플 | 핵심 정답 |', '| --- | --- |',
         f'| 01 영수증 | 17건 합계 {won(rtotal)}, 중복 의심 1건 |',
         f"| 02 다운로드 폴더 | {len(G.DOWNLOADS)}개 파일 → 프로젝트 {len({f['project'] for f in G.DOWNLOADS})}묶음, 구버전 {sum('구버전' in f['note'] for f in G.DOWNLOADS)}건 구별 |",
         '| 03 견적서 | 1년 실질 비용 ' + ', '.join(f"{q['id']} {won(qtotals[q['id']])}" for q in D.QUOTES) + ' |',
         f"| 04 회의녹취 | 결정 {len(D.MEETING['decisions'])}건, 할 일 {len(D.MEETING['actions'])}건, 보류 {len(D.MEETING['pending'])}건 |", '']
    L += rl + downloads() + ql + meeting()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text('\n'.join(L), encoding='utf-8')
    print(f'{OUT.relative_to(ROOT)}: 영수증 합계 {rtotal:,}, 견적 {qtotals}')


if __name__ == '__main__':
    main()
