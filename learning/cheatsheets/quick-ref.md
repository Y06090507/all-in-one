# 速查表

## Python 常用

| 场景 | 代码 |
|------|------|
| 列表推导 | `[x*2 for x in range(10) if x%2==0]` |
| 字典推导 | `{k:v for k,v in d.items() if v>0}` |
| 文件读取 | `Path('file.txt').read_text()` |
| 文件写入 | `Path('file.txt').write_text(data)` |
| JSON 读写 | `json.loads(s)` / `json.dumps(obj, indent=2)` |
| 日期格式化 | `datetime.now().strftime('%Y-%m-%d %H:%M')` |
| 环境变量 | `os.getenv('KEY', 'default')` |
| 遍历枚举 | `for i, v in enumerate(items):` |
| 解包 | `a, *mid, b = range(5)` |
| 上下文管理 | `with open('f') as f:` |

## Git 常用

| 场景 | 命令 |
|------|------|
| 新建分支 | `git checkout -b feat/xxx` |
| 暂存 | `git add -A && git commit -m "msg"` |
| 推送 | `git push origin main` |
| 拉取 | `git pull --rebase` |
| 查看日志 | `git log --oneline -10` |
| 撤销提交 | `git reset --soft HEAD~1` |
| 贮藏 | `git stash` / `git stash pop` |
