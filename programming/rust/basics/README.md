# Rust 语言

## 特点
- 零成本抽象，无 GC
- 所有权系统 → 内存安全无惧
- 强类型 + 模式匹配
- 并发 fearless concurrency

## 学习路线
- [ ] 基础: 变量/类型/函数/控制流
- [ ] 所有权 (Ownership) / 借用 (Borrowing) / 生命周期
- [ ] 结构体 / 枚举 / 模式匹配
- [ ] 泛型 / Trait
- [ ] 错误处理: Result / Option
- [ ] 集合: Vec / HashMap
- [ ] 并发: thread / Arc / Mutex / Channel
- [ ] Cargo: 包管理 / 测试

## 核心概念

```
所有权规则:
  1. 每个值有唯一所有者
  2. 同一时刻只能有一个可变引用或多个不可变引用
  3. 引用必须始终有效
```
