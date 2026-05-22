# C#

## 特点
- 微软 .NET 平台主力语言
- 类似 Java 但更现代
- LINQ / async-await / 属性 / 事件
- Unity 游戏引擎脚本语言

## 学习路线
- [ ] 基础: 类型/OOP/属性/索引器
- [ ] 集合: List/Dictionary/LINQ
- [ ] 委托 (delegate) / 事件 (event)
- [ ] 异步: async / await / Task
- [ ] LINQ: 声明式数据查询
- [ ] Entity Framework (ORM)
- [ ] ASP.NET Core (Web)
- [ ] NuGet 包管理

## 亮点特性

### LINQ — C# 的杀手特性
```csharp
// 声明式链式查询
var result = users
    .Where(u => u.Age > 18)
    .OrderBy(u => u.Name)
    .Select(u => new { u.Name, u.Email });

// 查询语法
var result = from u in users
             where u.Age > 18
             orderby u.Name
             select new { u.Name, u.Email };
```

### async/await
```csharp
async Task<string> FetchDataAsync(string url)
{
    using var client = new HttpClient();
    var data = await client.GetStringAsync(url);
    return data;
}

// 并行执行
var task1 = FetchAsync(url1);
var task2 = FetchAsync(url2);
await Task.WhenAll(task1, task2);
```

## .NET 生态
- ASP.NET Core → Web API/MVC
- Blazor → C# 写前端 (Wasm)
- MAUI → 跨平台桌面/移动
- Unity → 游戏开发
