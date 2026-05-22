# 响应式编程

## 核心思想

数据流 (Data Stream) + 自动传播变化。当数据源变了，所有依赖它的地方自动更新。

## 推 vs 拉

```
拉 (Pull / 命令式):
  UI → 读取数据 → 渲染

推 (Push / 响应式):
  数据 → 自动推送 → UI 更新
```

## RxJS 核心

```javascript
// Observable: 数据流
// Operator: 变换操作
// Subscription: 订阅消费

import { fromEvent } from 'rxjs';
import { debounceTime, map, switchMap } from 'rxjs/operators';

// 搜索框自动补全
const input$ = fromEvent(searchBox, 'input');
const results$ = input$.pipe(
  debounceTime(300),              // 防抖 300ms
  map(e => e.target.value),       // 取值
  switchMap(q => fetchResults(q)) // 取消旧请求
);
results$.subscribe(data => render(data));
```

## 响应式 UI 框架

| 框架 | 响应式方式 |
|------|-----------|
| React | State → 虚拟 DOM diff → 更新 |
| Vue | 响应式数据 + 模板编译 |
| SolidJS | 细粒度响应式 + 编译时 |
| Svelte | 编译时响应式 |
| SwiftUI | @State / @Binding |

## Signal 模式 (新一代)

```javascript
// Preact / Solid 风格
const [count, setCount] = createSignal(0);
const double = createMemo(() => count() * 2);

// count 变了 → double 自动重算
// 组件只更新用到的地方
```
