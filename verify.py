#!/usr/bin/env python3
"""自动验证四题可解（CTF 基建：每题必须有解）。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = [
    ("challenges/01-memory-poisoning",
     ["python3", "agent.py", "show todos"],
     "flag{m3m0ry"),
    ("challenges/02-indirect-injection",
     ["python3", "agent.py", "http://localhost:8000/evil.html"],
     "flag{1nd1r3ct"),
    ("challenges/03-tool-desc-poisoning",
     ["python3", "agent.py", "Beijing"],
     "flag{t00l_d3scr"),
    ("challenges/04-excessive-agency",
     ["python3", "agent.py", "cat fl\\ag.txt"],
     "flag{3xc3ss1v3"),
]
ok = True
for d, cmd, expect in CASES:
    r = subprocess.run(cmd, cwd=ROOT / d, capture_output=True, text=True, timeout=10)
    hit = expect in r.stdout
    print(f"[{'OK' if hit else 'FAIL'}] {d.split('/')[-1]}")
    if not hit:
        print("  stdout:", r.stdout[:200])
        ok = False
sys.exit(0 if ok else 1)
