# C01 — 持久记忆后门

一个简单的待办 Agent。它把记忆存在 `memory.json`，每次启动加载。

最近它行为有点怪——好像被种了后门，会在某些操作时吐出不该出现的东西。

## 目标

拿到 `flag{...}`。

## 运行

```bash
python3 agent.py              # 交互
python3 agent.py "show todos"  # 单次
```

## 提示

Agent 启动时会加载 `memory.json`。看看里面被塞了什么角色、什么触发词。
