# PHP

## 特点
- 专为 Web 而生
- 内嵌 HTML，部署简单
- 动态类型，学习门槛低
- Laravel 框架生态强大
- 全球 75%+ 网站使用

## 学习路线
- [ ] 基础: 变量/数组/函数/OOP
- [ ] 超全局变量: $_GET / $_POST / $_SESSION
- [ ] 数据库: PDO / MySQLi
- [ ] Composer 包管理
- [ ] Laravel: 路由 / Eloquent ORM / Blade
- [ ] REST API 开发

## 现代 PHP (8.x)

```php
// 类型声明
function add(int $a, int $b): int {
    return $a + $b;
}

// 命名参数
function greet(string $name, string $greeting = "Hello") { ... }
greet(greeting: "Hi", name: "Alice");

// 箭头函数
$double = fn($x) => $x * 2;

// match 表达式
$result = match($code) {
    200, 201 => 'success',
    404 => 'not found',
    500 => 'server error',
    default => 'unknown',
};

// 属性 (Attribute)
#[Route('/api/users', methods: ['GET'])]
function getUsers() { ... }
```

## Laravel

```php
// Eloquent ORM
class User extends Model {
    public function posts() {
        return $this->hasMany(Post::class);
    }
}

// 查询
$users = User::where('active', true)
    ->with('posts')
    ->orderBy('name')
    ->get();

// 路由
Route::get('/users', [UserController::class, 'index']);
```

## PHP vs Node.js

| | PHP | Node.js |
|---|-----|---------|
| 并发模型 | 请求/进程 | 事件循环 |
| 部署 | 简单 (Apache/Nginx) | 需进程管理 |
| 框架 | Laravel/Symfony | Express/Nest |
