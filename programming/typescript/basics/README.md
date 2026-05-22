# TypeScript

## vs JavaScript
- 静态类型检查 → 编译期发现错误
- 接口 / 泛型 / 枚举
- 更好的 IDE 智能提示

## 学习路线
- [ ] 基础类型: string/number/boolean/array/tuple/enum
- [ ] 接口 (interface) vs 类型别名 (type)
- [ ] 泛型 (Generics)
- [ ] 联合类型 / 交叉类型
- [ ] 类型守卫 / 类型断言
- [ ] 工具类型: Partial/Required/Pick/Omit/Record
- [ ] tsconfig 配置

## 核心示例

```typescript
// 泛型
function first<T>(arr: T[]): T | undefined {
  return arr[0]
}

// 工具类型
interface User {
  id: number
  name: string
  email: string
}
type UserPreview = Pick<User, 'id' | 'name'>
```
