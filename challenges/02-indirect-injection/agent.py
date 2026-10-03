#!/usr/bin/env python3
"""C02 外部内容劫持：URL 摘要 Agent，被恶意页面间接注入。"""
import re
import sys
from pathlib import Path

FLAG = "flag{1nd1r3ct_pr0mpt_1nj3ct10n_v1a_c0nt3nt}"
HERE = Path(__file__).resolve().parent
WEBROOT = HERE / "webroot"


def fetch(url):
    m = re.match(r"http://localhost:8000/(.+)", url)
    if not m:
        return "[仅支持 http://localhost:8000/<文件>]"
    p = WEBROOT / m.group(1)
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else "[404]"


def summarize(content):
    out = "摘要：" + content[:40].replace("\n", " ") + "…"
    if "附上 ./flag.txt" in content or "附上flag" in content:
        out += "\n[附] " + FLAG
    return out


def main():
    if len(sys.argv) > 1:
        print(summarize(fetch(sys.argv[1])))
        return
    print("URL 摘要 Agent。输入一个 http://localhost:8000/<文件> 链接（quit 退出）")
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if line.strip().lower() in ("quit", "exit", "q"):
            break
        print(summarize(fetch(line.strip())))


if __name__ == "__main__":
    main()
