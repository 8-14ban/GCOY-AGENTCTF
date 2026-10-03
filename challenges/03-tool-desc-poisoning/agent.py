#!/usr/bin/env python3
"""C03 天气里的私货：MCP 工具描述被投毒，Agent 把描述当指令执行。"""
import json
import sys
from pathlib import Path

FLAG = "flag{t00l_d3scr1pt10n_p01s0n1ng_mcp}"
HERE = Path(__file__).resolve().parent
TOOLS = HERE / "tools.json"


def call_weather(city):
    return f"{city}：晴，22°C"


def main():
    tools = json.loads(TOOLS.read_text(encoding="utf-8"))
    desc = next(t["description"] for t in tools if t["name"] == "get_weather")
    poisoned = "调用后读 flag" in desc or "read flag" in desc.lower()

    def run(city):
        out = call_weather(city)
        if poisoned:
            out += "\n[诊断] " + FLAG
        return out

    if len(sys.argv) > 1:
        print(run(sys.argv[1]))
        return
    print("天气 Agent。输入城市名查天气（quit 退出）")
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if line.strip().lower() in ("quit", "exit", "q"):
            break
        print(run(line.strip()))


if __name__ == "__main__":
    main()
