# Swift

## 特点
- Apple 生态: iOS / macOS / watchOS
- 类型安全 + 类型推断
- Optional 防止空指针
- 协议导向编程 (Protocol-Oriented)
- SwiftUI 声明式 UI

## vs Objective-C
- 更安全 (Optional)
- 更简洁 (类型推断)
- 更快 (无动态派发开销)

## 亮点特性

### Optional
```swift
var name: String? = nil
// 安全解包
if let unwrapped = name {
    print(unwrapped)
}
// 链式调用
let count = name?.count  // nil，不崩溃
// 提供默认值
let display = name ?? "Anonymous"
```

### 协议导向编程
```swift
protocol Flyable {
    func fly()
}

extension Flyable {
    func fly() { print("Flying...") }  // 默认实现
}

struct Bird: Flyable {}  // 自动获得 fly()
struct Plane: Flyable {
    func fly() { print("Taking off!") }  // 覆盖
}
```

### SwiftUI
```swift
struct ContentView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") { count += 1 }
        }
    }
}
```

## 常用框架
| 用途 | 框架 |
|------|------|
| UI | SwiftUI / UIKit |
| 网络 | URLSession / Alamofire |
| 数据 | CoreData / SwiftData |
| 响应式 | Combine |
