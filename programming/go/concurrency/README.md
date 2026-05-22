# Go 并发编程

Go 的杀手级特性。

## goroutine

轻量级线程，一个程序可以轻松跑数十万个。

```go
// 启动 goroutine
go doSomething()
go func() {
    fmt.Println("anonymous goroutine")
}()
```

## Channel

goroutine 之间通信的管道。

```go
ch := make(chan string)

// 发送
go func() {
    ch <- "hello"  // 发送到 channel
}()

// 接收
msg := <-ch       // 从 channel 接收
fmt.Println(msg)  // hello
```

## Select

多路复用，同时等待多个 channel。

```go
select {
case msg1 := <-ch1:
    fmt.Println("from ch1:", msg1)
case msg2 := <-ch2:
    fmt.Println("from ch2:", msg2)
case <-time.After(1 * time.Second):
    fmt.Println("timeout")
}
```

## 并发模式

### Fan-Out / Fan-In
```
         ┌→ worker →┐
source → ├→ worker →├→ collector → result
         └→ worker →┘
```

### Pipeline
```
[generate] → [process] → [output]
     ch1         ch2
```

### Worker Pool
```go
jobs := make(chan Job, 100)
results := make(chan Result, 100)

for w := 0; w < 3; w++ {
    go worker(jobs, results)
}
```

## 金句

> Don't communicate by sharing memory;
> share memory by communicating.
