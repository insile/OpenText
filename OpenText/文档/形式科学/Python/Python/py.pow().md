##### pow()
- `pow( x ,  y , z=None )`
	- 返回 x 的 y 次方的值
	- z 可选参数，用于指定模数（取模运算时使用）
```python
result = pow(2, 3)
print(result)  # 输出：8

result = pow(3, 4)
print(result)  # 输出：81

result = pow(2, 5, 10)  # 计算 (2 ** 5) % 10
print(result)  # 输出：2

```