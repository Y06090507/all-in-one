# C++

## 特点
- C 的超集，零开销抽象
- 手动内存管理 + RAII
- 多重范式: 过程式/OOP/泛型/函数式
- 游戏引擎、高频交易、浏览器内核

## 学习路线
- [ ] C 基础: 指针/内存/结构体
- [ ] 类与对象: 构造/析构/拷贝/移动
- [ ] RAII: 资源获取即初始化
- [ ] 模板 (Template): 泛型编程
- [ ] STL: vector/map/set/algorithm
- [ ] 智能指针: unique_ptr / shared_ptr
- [ ] Lambda / 移动语义 (C++11)
- [ ] 并发: thread / mutex / atomic (C++11)

## 核心概念

### RAII — C++ 的精髓
```cpp
// 资源在构造时获取，析构时自动释放
class FileHandle {
    FILE* f;
public:
    FileHandle(const char* path) : f(fopen(path, "r")) {}
    ~FileHandle() { if (f) fclose(f); }
    // 禁止拷贝，允许移动
    FileHandle(const FileHandle&) = delete;
    FileHandle(FileHandle&& other) : f(other.f) { other.f = nullptr; }
};
```

### 智能指针
```cpp
auto p1 = std::make_unique<Widget>();   // 独占所有权
auto p2 = std::make_shared<Widget>();   // 共享所有权，引用计数
auto p3 = p2;  // 引用计数 +1
```

### 移动语义
```cpp
std::vector<int> v1 = {1, 2, 3};
std::vector<int> v2 = std::move(v1);  // 移动，不拷贝
// v1 现在为空，v2 拥有数据
```

## C++ vs Rust

| | C++ | Rust |
|---|-----|------|
| 安全 | 靠程序员 | 编译器强制 |
| 学习曲线 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 生态 | 30年积累 | 快速增长 |
| 编译速度 | 慢 | 慢 |
