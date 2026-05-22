# Rust 所有权 (Ownership)

Rust 最核心的概念，实现无 GC 的内存安全。

## 三条规则

1. **每个值有一个所有者**
2. **同一时刻只能有一个可变引用，或多个不可变引用**
3. **引用必须始终有效**

## 所有权转移

```rust
let s1 = String::from("hello");
let s2 = s1;              // s1 所有权转移给 s2
// println!("{}", s1);    // ❌ s1 已失效
println!("{}", s2);       // ✅
```

## 借用 (Borrowing)

不转移所有权，而是「借用」。

```rust
fn print_str(s: &String) {  // 不可变借用
    println!("{}", s);
}

fn modify_str(s: &mut String) {  // 可变借用
    s.push_str(" world");
}
```

## 生命周期

编译器保证引用不会悬空。

```rust
// 'a 表示返回值生命周期与两个参数中较短的那个相同
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

## 对比

| 概念 | Rust | C | Go/Java |
|------|------|---|---------|
| 内存管理 | 所有权+借用检查 | 手动 malloc/free | GC 自动 |
| 空指针 | Option<T> | NULL | null/nil |
| 数据竞争 | 编译期阻止 | 运行期难查 | 运行期难查 |
| 性能 | 零开销 | 零开销 | GC 开销 |
