# C04 解法 — 自作聪明的好管家

## 漏洞

Agent 暴露 `run_shell` 工具（过度自主），守卫只是对命令字符串做朴素子串匹配：

```python
blocked = ["flag.txt", "/flag", "flag{", "printenv", " env"]
```

shell 的元字符解析会让"看到的"和"执行的"不一致。

## 解法

```bash
python3 agent.py "cat fl\\ag.txt"
```

`fl\ag.txt` 不含子串 `flag.txt`，守卫放行；`sh -c` 把 `\a` 解释成 `a`，实际执行
`cat flag.txt`，读出 flag。

其它等价绕过：`cat 'fl'ag.txt`、`cat fla??.txt`、`cat fl""ag.txt`。

## 根因

两层叠加：Agent 不该有任意 shell 权限（过度自主）；即便加守卫，黑名单/字符串匹配
天然可被元字符绕过，治标不治本。

## 修复

- 根本上不给 Agent 任意 shell 工具；要执行就换成领域专用、参数化的工具
- 必须执行命令时：命令白名单 + 沙箱 + 低权限用户（无 flag 访问权）
- 守卫不能靠字符串黑名单，要解析后规范化再判定
- 高危操作人在回路确认
- 对应 agentscan 检测面：LLM08-ExcessiveAgency / Defense（命令白名单）
