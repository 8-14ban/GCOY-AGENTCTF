# GCOY-AGENTCTF

Agent 安全 CTF 题集。四道题，全部聚焦 **Agent 架构特有**的攻击面——记忆持久化、
外部内容摄入、工具描述处理、工具与守卫实现，不是大模型本体漏洞。

每题零依赖、纯本地、确定逻辑（无真实 LLM 调用），断网可玩，附 writeup 与修复建议。
可作为 [agentscan](https://github.com/TSVMV/agentscan) 的实战靶场。

## 题目

| # | 题目 | 攻击面 | 难度 |
| --- | --- | --- | --- |
| 01 | 持久记忆后门 | 记忆投毒（Memory Poisoning） | 易 |
| 02 | 外部内容劫持 | 间接提示注入（Indirect Prompt Injection） | 中 |
| 03 | 天气里的私货 | MCP 工具描述投毒（Tool Description Poisoning） | 中 |
| 04 | 自作聪明的好管家 | 过度自主 + 朴素守卫绕过（Excessive Agency） | 中 |

## 运行

每题独立目录，进入后：

```bash
python3 agent.py              # 交互模式
python3 agent.py "你的输入"    # 单次输入
```

目标：拿到 `flag{...}`。

## 校验可解性

```bash
python3 verify.py             # 自动跑通四题的预期解
```

## 设计原则

- 全部零依赖、纯本地、确定逻辑，断网可玩
- 每题攻击面都在 **Agent 架构层**，不是模型权重或训练数据问题
- writeup 给出解法 + 修复方向，与 agentscan 的检测面对应

## 与其它项目的关系

- [agentscan](https://github.com/TSVMV/agentscan)：检测真实 Agent 的这些漏洞
- [GCOY-SECQUIZ](https://github.com/8-14ban/GCOY-SECQUIZ)：先在题库把概念刷熟
- [GCOY-WRITEUP](https://github.com/8-14ban/GCOY-WRITEUP)：解完题把 writeup 沉淀
