# OOP 深入

## 四大支柱

### 封装
隐藏内部实现，暴露公开接口。

```python
class BankAccount:
    def __init__(self):
        self._balance = 0  # 私有

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    @property
    def balance(self):
        return self._balance
```

### 继承
子类复用父类的属性和方法。

```python
class Vehicle:
    def start(self): ...

class Car(Vehicle):
    def start(self):
        super().start()
        print("Engine started")
```

### 多态
同一接口，不同行为。

```python
def make_sound(animal: Animal):
    print(animal.sound())

# Dog, Cat 各自实现 sound() → 不同行为
```

### 抽象
只定义接口，不暴露细节。

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount): ...

class WeChatPay(Payment):
    def pay(self, amount):
        print(f"WeChat: {amount}")
```

## 设计原则

| 原则 | 含义 |
|------|------|
| DRY | Don't Repeat Yourself |
| KISS | Keep It Simple, Stupid |
| YAGNI | You Aren't Gonna Need It |
| 组合优于继承 | has-a > is-a |
| 面向接口编程 | 依赖抽象而非具体 |

## 常见反模式

- 上帝类 (God Class) — 一个类干了所有事
- 过度继承 — 继承链太长
- 贫血模型 — 只有数据没有行为的对象
