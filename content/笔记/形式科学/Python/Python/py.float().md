##### float()
- `float( x )`
	- 将整数和字符串转换成浮点数，没有参数返回0.0
```python
float('+1.23')  # 1.23
float('   -12345\n')  # -12345.0
float('1e-003')  # 0.001
float('+1E6')  # 1000000.0
float('-Infinity')  # -inf
float()  # 0.0
```