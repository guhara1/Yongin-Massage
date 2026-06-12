#!/usr/bin/env python3
"""모듈 단위 본문 글자수 검사.

사용법: python3 scripts/count_chars.py areas_cheoin [stations_everline ...]

content 패키지의 __init__(전체 모듈 로딩)을 거치지 않고 지정 모듈만 로드하므로
다른 모듈이 작성 중이어도 독립적으로 검사할 수 있다.
요금 블록(<section class="pricing">)은 글자수 측정에서 제외한다(빌드와 동일 기준).
"""
import html
import importlib.util
import os
import re
import sys
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name):
    spec = importlib.util.spec_from_file_location(
        f"content.{name}", os.path.join(ROOT, "content", f"{name}.py")
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[f"content.{name}"] = mod
    spec.loader.exec_module(mod)
    return mod


def text_length(body: str) -> int:
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return len(re.sub(r"\s+", " ", text).strip())


def main():
    pkg = types.ModuleType("content")
    pkg.__path__ = [os.path.join(ROOT, "content")]
    sys.modules["content"] = pkg
    _load("site")
    _load("pricing")

    bad = 0
    for name in sys.argv[1:]:
        mod = _load(name)
        pages = getattr(mod, "PAGES", None)
        if pages is None:
            pages = [mod.PAGE]
        for p in pages:
            n = text_length(p["body"])
            if p.get("noindex"):
                status = "noindex(의도)"
            elif 2000 <= n <= 2500:
                status = "OK"
            else:
                status = "범위 밖 ⚠"
                bad += 1
            kw = len(re.findall("출장마사지", p["body"]))
            kw_flag = "" if kw <= 5 else f"  ⚠키워드 {kw}회"
            desc_flag = "" if len(p["desc"]) <= 80 else f"  ⚠desc {len(p['desc'])}자"
            print(f"{(p['path'] or '/'):52s} {n:5d}  {status}{kw_flag}{desc_flag}")
    print(f"\n범위 밖 {bad}건")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
