# Kotlin

## 特点
- JVM 语言，100% 与 Java 互操作
- 简洁: 少写 40% 代码 vs Java
- 空安全: 编译期防止 NPE
- Android 官方推荐语言
- 协程 (Coroutine) 原生支持

## vs Java

```kotlin
// Java
public class User {
    private String name;
    public User(String name) { this.name = name; }
    public String getName() { return name; }
}

// Kotlin — 一行搞定
data class User(val name: String)
```

## 亮点特性

```kotlin
// 空安全
var name: String? = null  // 可空类型
name?.length              // 安全调用，返回 null 而非 NPE
name!!.length             // 强制非空，若空则抛异常

// 扩展函数 — 给已有类加方法
fun String.isEmail(): Boolean =
    contains("@") && contains(".")

// when 表达式 (超级 switch)
when (x) {
    in 1..10 -> "small"
    is String -> "a string"
    else -> "unknown"
}

// 作用域函数
user?.let { println(it.name) }    // 非空时执行
val config = Config().apply {     // 配置对象
    host = "localhost"
    port = 8080
}
```

## 协程

```kotlin
// 轻量级并发，非阻塞
suspend fun fetchUser(id: Int): User {
    return withContext(Dispatchers.IO) {
        api.getUser(id)
    }
}

// 并行请求
coroutineScope {
    val user = async { fetchUser(1) }
    val posts = async { fetchPosts(1) }
    render(user.await(), posts.await())
}
```
