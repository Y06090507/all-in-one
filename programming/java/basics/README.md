# Java

## 特点
- 静态类型，JVM 运行
- 一次编写到处运行
- 强大生态: Spring, Hadoop, Android
- 企业级开发首选

## 学习路线
- [ ] 基础: 类型/控制流/OOP
- [ ] 集合框架: List/Set/Map/Queue
- [ ] 异常处理: try-catch-finally / throws
- [ ] IO 流: InputStream / Reader / NIO
- [ ] 泛型 (Generics)
- [ ] 注解 (Annotation) / 反射 (Reflection)
- [ ] 多线程: Thread / ExecutorService / synchronized
- [ ] Stream API + Lambda (Java 8+)
- [ ] Maven / Gradle 构建

## 核心代码

```java
// Stream + Lambda
List<String> names = users.stream()
    .filter(u -> u.getAge() > 18)
    .map(User::getName)
    .sorted()
    .collect(Collectors.toList());

// 多线程
ExecutorService executor = Executors.newFixedThreadPool(4);
Future<String> future = executor.submit(() -> {
    return heavyComputation();
});
String result = future.get();
```

## JVM 生态

```
源码(.java) → 编译 → 字节码(.class) → JVM 执行
                         ↑
              Kotlin / Scala / Groovy 也编译到字节码
```
