# 函数式编程深入

## 核心原则

### 纯函数 (Pure Function)
- 相同输入 → 相同输出
- 无副作用 (不修改外部状态)
- 可缓存、可并行、可测试

```python
# ❌ 非纯函数
total = 0
def add(n):
    global total
    total += n  # 副作用

# ✅ 纯函数
def add(a, b):
    return a + b
```

### 不可变数据 (Immutability)
```python
# ❌ 修改原数据
arr = [1, 2, 3]
arr.append(4)

# ✅ 返回新数据
arr = [1, 2, 3]
new_arr = [*arr, 4]
```

### 高阶函数
```python
# map: 对每个元素应用函数
list(map(str.upper, ['a', 'b', 'c']))  # ['A', 'B', 'C']

# filter: 保留满足条件的元素
list(filter(lambda x: x > 2, [1, 2, 3, 4]))  # [3, 4]

# reduce: 累积计算
from functools import reduce
reduce(lambda a, b: a * b, [1, 2, 3, 4])  # 24
```

### 柯里化 (Currying)
```javascript
// 普通函数
const add = (a, b) => a + b;

// 柯里化
const add = a => b => a + b;
const add5 = add(5);
add5(3); // 8
```

### Monad (Maybe / Result)
```python
# 避免 null 检查地狱
def get_user(id):
    return None  # nullable

# 函数式: 用 Result 类型
# Rust: Result<T, E>
# Haskell: Maybe / Either
```
