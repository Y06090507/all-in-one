# C++11/14/17/20 现代特性

## C++11 — 革命性更新

```cpp
// auto 类型推断
auto x = 42;
auto it = map.begin();

// 范围 for
for (auto& v : vec) { ... }

// Lambda
auto add = [](int a, int b) { return a + b; };
sort(vec.begin(), vec.end(), [](int a, int b) { return a > b; });

// 智能指针
auto p = std::make_unique<Widget>();

// 移动语义
std::vector<int> v2 = std::move(v1);
```

## C++14 — 改进
```cpp
// 泛型 Lambda
auto add = [](auto a, auto b) { return a + b; };

// make_unique
auto p = std::make_unique<Widget>(arg1, arg2);
```

## C++17 — 实用更新
```cpp
// 结构化绑定
auto [name, age] = getPerson();

// if 初始化
if (auto it = map.find(key); it != map.end()) {
    use(it->second);
}

// std::optional
std::optional<int> findUser(int id) {
    if (exists(id)) return id;
    return std::nullopt;
}

// string_view — 零拷贝字符串视图
std::string_view sv = "hello world";
```

## C++20 — 四大特性
```cpp
// 1. Concepts — 约束模板
template<typename T>
concept Numeric = std::is_arithmetic_v<T>;

template<Numeric T>
T add(T a, T b) { return a + b; }

// 2. Ranges
auto result = vec | std::views::filter([](int x) { return x > 0; })
                  | std::views::transform([](int x) { return x * 2; });

// 3. Coroutines (异步)

// 4. Modules — 替代 #include
import std.core;
```
