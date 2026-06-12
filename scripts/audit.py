#!/usr/bin/env python3
"""배포 전 감사 스크립트.

검사 항목:
  1. 타이틀·디스크립션 중복 (0건이어야 함)
  2. 디스크립션 길이 50~80자
  3. 색인 페이지 본문 2,000~2,500자 (요금 블록 제외)
  4. 페이지 간 8-gram 자카드 유사도 < 0.30
  5. 도어웨이 URL 패턴 (숫자 행정동, 역+테마 조합) 0건
  6. JSON-LD 파싱 오류 0건
  7. "출장마사지" 본문 5회 이하

사용법: python3 scripts/audit.py
"""
import html
import json
import os
import re
import sys
from collections import Counter
from itertools import combinations

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content import PAGES  # noqa: E402

errors = []
warnings = []


def text_of(body):
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


# 1. 타이틀·디스크립션 중복
for field in ("title", "desc"):
    dup = [v for v, c in Counter(p[field] for p in PAGES).items() if c > 1]
    for v in dup:
        errors.append(f"{field} 중복: {v}")

# 2~3, 7. 길이·키워드
for p in PAGES:
    path = p["path"] or "/"
    n = len(text_of(p["body"]))
    if not p.get("noindex"):
        if not (2000 <= n <= 2500):
            errors.append(f"본문 글자수 범위 밖({n}자): {path}")
        if not (50 <= len(p["desc"]) <= 80):
            warnings.append(f"desc {len(p['desc'])}자: {path}")
    kw = len(re.findall("출장마사지", p["body"]))
    if kw > 5:
        errors.append(f"'출장마사지' {kw}회: {path}")

# 4. 유사도 (8-gram 자카드) — 색인 페이지만
def ngrams(s, n=8):
    s = re.sub(r"\s+", "", s)
    return {s[i:i + n] for i in range(max(0, len(s) - n + 1))}

texts = {p["path"] or "/": ngrams(text_of(p["body"])) for p in PAGES if not p.get("noindex")}
worst = []
for (a, ta), (b, tb) in combinations(texts.items(), 2):
    inter = len(ta & tb)
    if not inter:
        continue
    j = inter / len(ta | tb)
    if j >= 0.30:
        errors.append(f"유사도 {j:.2f}: {a} ↔ {b}")
    elif j >= 0.20:
        worst.append((j, a, b))
for j, a, b in sorted(worst, reverse=True)[:5]:
    warnings.append(f"유사도 {j:.2f}(경계): {a} ↔ {b}")

# 5. 도어웨이 URL 패턴
BAD_PATTERNS = [
    r"\d-dong/",                    # 숫자 행정동 (yurim-1-dong 등)
    r"station/.+(swedish|aroma|thai|24)",  # 역+테마 조합
    r"(exit|chulgu)",               # 출구별
]
for p in PAGES:
    for pat in BAD_PATTERNS:
        if re.search(pat, p["path"]):
            errors.append(f"도어웨이 패턴({pat}): {p['path']}")

# 6. JSON-LD 파싱
for p in PAGES:
    head = p.get("extra_head", "")
    for m in re.finditer(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', head, re.S):
        try:
            json.loads(m.group(1))
        except json.JSONDecodeError as e:
            errors.append(f"JSON-LD 오류({e}): {p['path'] or '/'}")

print(f"페이지 {len(PAGES)}개 검사")
for w in warnings:
    print(f"  ⚠ {w}")
for e in errors:
    print(f"  ✗ {e}")
print(f"\n오류 {len(errors)}건 / 경고 {len(warnings)}건")
sys.exit(1 if errors else 0)
