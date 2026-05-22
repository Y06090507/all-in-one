# Kotlin 协程

## 概念
协程 = 轻量级线程。挂起不阻塞线程。

## 基础

```kotlin
// suspend 函数 — 可挂起的函数
suspend fun fetchData(): String {
    delay(1000)  // 挂起，不阻塞线程
    return "data"
}

// 启动协程
fun main() = runBlocking {
    launch {
        val data = fetchData()
        println(data)
    }
}
```

## 结构化并发

```kotlin
// 并行 — async
suspend fun loadPage() = coroutineScope {
    val user = async { fetchUser() }
    val posts = async { fetchPosts() }
    render(user.await(), posts.await())
    // scope 等所有子协程完成才返回
}

// 异常处理
suspend fun safe() = supervisorScope {
    launch { riskyOp1() }
    launch { riskyOp2() }
    // 一个失败不影响另一个
}
```

## 调度器

| 调度器 | 用途 |
|--------|------|
| Dispatchers.Main | UI 线程 (Android) |
| Dispatchers.IO | 网络/文件 |
| Dispatchers.Default | CPU 密集型 |
| Dispatchers.Unconfined | 不限制 |

## Flow — 冷数据流

```kotlin
fun fetchUsers(): Flow<User> = flow {
    for (i in 1..10) {
        delay(100)
        emit(api.getUser(i))
    }
}

fetchUsers()
    .filter { it.age > 18 }
    .map { it.name }
    .catch { e -> emit("Error: $e") }
    .collect { println(it) }
```

## vs 线程

| | 线程 | 协程 |
|---|------|------|
| 创建成本 | ~1MB 栈 | ~几KB |
| 切换成本 | 内核态 | 用户态 |
| 数量 | 数千 | 数十万 |
