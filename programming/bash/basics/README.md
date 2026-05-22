# Bash / Shell

## 基础语法

```bash
# 变量
name="world"
echo "Hello, $name"

# 条件判断
if [ -f "file.txt" ]; then
  echo "exists"
fi

# 循环
for i in 1 2 3; do
  echo $i
done

# 函数
greet() {
  echo "Hello, $1"
}
greet "Alice"
```

## 常用命令速查

| 场景 | 命令 |
|------|------|
| 查找文件 | `find . -name "*.py"` |
| 文本搜索 | `grep -r "pattern" .` |
| 管道 | `cat file \| grep x \| sort \| uniq` |
| 重定向 | `cmd > out.txt 2>&1` |
| 后台运行 | `cmd &` |
| 变量替换 | `${var:-default}` |

## 脚本模板

```bash
#!/bin/bash
set -euo pipefail  # 严格模式

main() {
  echo "Starting..."
  # your code here
}

main "$@"
```
