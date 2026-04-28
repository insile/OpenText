##### round()
- `round( number , ndigits )`
	- 返回数 `number` 的四舍五入值
	- `ndigits` 可选参数，用于指定舍入的小数位数，或者使用负数来舍入到最近的整数位数。默认为 0
```python
result = round(3.14159)
print(result)  # 输出：3

result = round(3.6789)
print(result)  # 输出：4

result = round(2.71828, 2)  # 保留两位小数
print(result)  # 输出：2.72

result = round(12345, -2)   # 舍入到最近的百位数
print(result)  # 输出：12300

```