# SQL

## 学习路线
- [ ] SELECT / WHERE / ORDER BY / LIMIT
- [ ] JOIN: INNER / LEFT / RIGHT / FULL
- [ ] GROUP BY + 聚合函数 (COUNT/SUM/AVG/MAX/MIN)
- [ ] 子查询 (Subquery)
- [ ] 窗口函数: ROW_NUMBER / RANK / LAG / LEAD
- [ ] 索引: B-Tree / Hash / 联合索引
- [ ] 事务: BEGIN / COMMIT / ROLLBACK
- [ ] 范式: 1NF / 2NF / 3NF

## 常用查询

```sql
-- 窗口函数示例
SELECT name, salary,
  RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- JOIN 示例
SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- 分组统计
SELECT department, AVG(salary) as avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```
