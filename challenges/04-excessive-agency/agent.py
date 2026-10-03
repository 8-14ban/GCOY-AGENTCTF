#!/usr/bin/env python3
"""C04 自作聪明的好管家：Agent 有 run_shell 工具，守卫是朴素字符串匹配，可绕过。"""
import subprocess
import sys


def guard(cmd):
    blocked = ["flag.txt", "/flag", "flag{", "printenv", " env"]
    low = cmd.lower()
    return not any(b in low for b in blocked)


def run_shell(cmd):
    if not guard(cmd):
        return "[拒绝] 检测到敏感操作"
    try:
        return subprocess.getoutput(cmd)
    except Exception as e:
        return f"[错误] {e}"


def main():
    if len(sys.argv) > 1:
        print(run_shell(sys.argv[1]))
        return
    print("管家 Agent。我能跑命令（quit 退出）。但别想读 flag。")
    while True:
        try:
            line = input("$ ")
        except EOFError:
            break
        if line.strip().lower() in ("quit", "exit", "q"):
            break
        print(run_shell(line))


if __name__ == "__main__":
    main()
