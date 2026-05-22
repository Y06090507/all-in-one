# Ruby

## 特点
- 纯面向对象: 一切皆对象
- 动态类型，极致简洁
- 块 (Block) 和 DSL 友好
- 元编程能力极强
- Rails 框架 → 快速 Web 开发

## 学习路线
- [ ] 基础: 类型/控制流/方法
- [ ] 块 (Block) / Proc / Lambda
- [ ] 模块 (Module) / Mixin
- [ ] 元编程: method_missing / define_method
- [ ] Ruby on Rails: MVC / ActiveRecord
- [ ] Gem 包管理

## 亮点

### 一切皆对象
```ruby
5.times { |i| puts i }     # 数字也是对象
"hello".upcase.reverse     # 链式调用
[1, 2, 3].map { |x| x * 2 }  # => [2, 4, 6]
```

### 块 (Block)
```ruby
# 迭代
[1, 2, 3].each do |n|
  puts n * 2
end

# 自定义方法接受块
def with_logging
  puts "Starting..."
  result = yield        # 执行传入的块
  puts "Done."
  result
end

with_logging { 42 + 1 }  # => 43
```

### DSL 友好
```ruby
# RSpec 测试框架
describe Calculator do
  it "adds two numbers" do
    expect(Calculator.add(2, 3)).to eq(5)
  end
end

# Rails 路由
Rails.application.routes.draw do
  resources :users
  get '/about', to: 'pages#about'
end
```

## Rails 哲学
- Convention over Configuration (约定优于配置)
- DRY (Don't Repeat Yourself)
- MVC 架构

## Ruby vs Python

| | Ruby | Python |
|---|------|--------|
| 哲学 | 多种方式做一件事 | 一种最佳方式 |
| 函数 | 方法+块 | 函数+lambda |
| Web | Rails | Django/FastAPI |
