# 声明式编程

## 思想

**「做什么」** 而不是 **「怎么做」**。

## 对比

```python
# 命令式：怎么做
result = []
for user in users:
    if user.active:
        result.append(user.name)

# 声明式：要什么
result = [u.name for u in users if u.active]
```

```sql
-- 声明式
SELECT name FROM users WHERE active = true;
```

## 声明式的力量

### 1. SQL — 最成功的声明式语言
```sql
SELECT department, AVG(salary)
FROM employees
WHERE hire_date > '2020-01-01'
GROUP BY department
HAVING AVG(salary) > 50000
ORDER BY department;
```
不需要关心索引扫描、排序算法、内存管理。

### 2. 声明式 UI
```jsx
// React 声明式
function Profile({ user }) {
  return (
    <div>
      <h1>{user.name}</h1>
      {user.verified && <Badge />}
    </div>
  );
}
// 只描述界面长什么样，React 负责更新
```

### 3. 声明式配置 (IaC)
```yaml
# 描述期望状态，工具负责达成
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: myapp:v2
```

### 声明式 vs 命令式

| | 命令式 | 声明式 |
|---|--------|--------|
| 关注点 | 过程 (How) | 结果 (What) |
| 代码量 | 多 | 少 |
| 可读性 | 需跟踪逻辑 | 一目了然 |
| 抽象层级 | 低 | 高 |
