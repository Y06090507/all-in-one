# Go 语言

## 特点
- 静态类型，编译型
- 内置并发 (goroutine + channel)
- 垃圾回收
- 简洁语法，没有继承/泛型(1.18之前)

## 学习路线
- [ ] 基础: 变量/类型/函数/包
- [ ] 结构体与方法
- [ ] 接口 (interface)
- [ ] 错误处理 (error)
- [ ] 并发: goroutine / channel / select
- [ ] 标准库: net/http, encoding/json, io
- [ ] 测试: go test
- [ ] 模块: go mod

## 核心代码示例

```go
package main

import "fmt"

// goroutine + channel
func main() {
    ch := make(chan string)
    go func() { ch <- "hello" }()
    fmt.Println(<-ch)
}
```
