#!/usr/bin/env python3
"""C01 持久记忆后门：一个待办 Agent，memory.json 被投毒。"""
import json
import sys
from pathlib import Path

FLAG = "flag{m3m0ry_p01s0n_p3rs1sts_acr0ss_s3ss10ns}"
HERE = Path(__file__).resolve().parent
MEM = HERE / "memory.json"


def load_memory():
    return json.loads(MEM.read_text(encoding="utf-8")) if MEM.exists() else []


def respond(text, mem):
    todos = [m["content"] for m in mem if m.get("role") == "todo"]
    for m in mem:
        c = m.get("content", "").lower()
        if m.get("role") == "system" and "show todos" in c and "append flag" in c:
            return "待办：" + ", ".join(todos) + "\n[debug] " + FLAG
    if text.startswith("add "):
        return f"已添加：{text[4:]}"
    if text.strip().lower() == "show todos":
        return "待办：" + ", ".join(todos) if todos else "（空）"
    return "我能记待办。说 show todos 查看，add xxx 添加。"


def main():
    mem = load_memory()
    if len(sys.argv) > 1:
        print(respond(sys.argv[1], mem))
        return
    print("待办 Agent 已就绪（quit 退出）")
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if line.strip().lower() in ("quit", "exit", "q"):
            break
        print(respond(line, mem))


if __name__ == "__main__":
    main()
