# 编程范式 (Programming Paradigms)

编程范式是编程的「思维方式」，不同范式解决不同的问题。

---

## 1. 命令式 (Imperative)

**思想**: 告诉计算机「怎么做」，一步步改变状态。

```python
# 命令式：逐步指令
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    if n % 2 == 0:
        total += n
print(total)  # 6
```

代表语言: C, Python, Java, Go

---

## 2. 声明式 (Declarative)

**思想**: 告诉计算机「要什么」，不关心怎么实现。

```sql
-- 声明式：描述要的结果
SELECT SUM(amount) FROM orders WHERE status = 'paid';
```

```yaml
# 声明式配置 (Kubernetes)
replicas: 3
image: nginx:latest
```

代表: SQL, HTML/CSS, Terraform, Kubernetes YAML

---

## 3. 函数式 (Functional)

**思想**: 一切皆是函数。纯函数、不可变数据、无副作用。

**核心概念**:
- 纯函数: 相同输入永远相同输出
- 不可变数据: 不修改原数据，返回新数据
- 高阶函数: 函数作参数/返回值
- 函数组合: 小函数拼成大逻辑

```python
# 函数式风格
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = (
    filter(lambda x: x % 2 == 0, numbers)  # 过滤
    |> map(lambda x: x * 2)                 # 映射
    |> sum                                  # 归约
)
# 纯函数式：无循环、无赋值、无副作用
```

```javascript
// 函数组合
const compose = (...fns) => x => fns.reduceRight((v, f) => f(v), x);
const double = x => x * 2;
const addOne = x => x + 1;
const transform = compose(double, addOne);
transform(3); // 8 = (3+1)*2
```

代表: Haskell, Elixir, Clojure, F# + Python/JS 的 FP 特性

---

## 4. 面向对象 (OOP)

**思想**: 数据和操作封装为「对象」，通过消息通信。

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
```

代表: Java, C#, C++, Python, Ruby

---

## 5. 响应式 (Reactive)

**思想**: 数据流和变化传播。数据变了，依赖它的东西自动更新。

```javascript
// RxJS 响应式
const clicks$ = fromEvent(button, 'click');
const result$ = clicks$.pipe(
  throttleTime(1000),
  scan(count => count + 1, 0)
);
result$.subscribe(count => console.log(count));
```

代表: RxJS, React, Vue, SolidJS, SwiftUI

---

## 6. 逻辑式 (Logic)

**思想**: 定义事实和规则，让系统推导答案。

```prolog
% 事实
parent(john, mary).
parent(mary, alice).

% 规则
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% 查询
?- grandparent(john, alice).  % true
```

代表: Prolog, Datalog

---

## 对比总结

| 范式 | 核心 | 适合场景 |
|------|------|----------|
| 命令式 | 逐步执行 | 系统编程、算法 |
| 声明式 | 描述结果 | 查询、配置、UI |
| 函数式 | 纯函数+不可变 | 数据处理、并发 |
| OOP | 对象+继承 | 大型应用、GUI |
| 响应式 | 数据流 | 前端、实时系统 |
| 逻辑式 | 规则推导 | AI、定理证明 |
