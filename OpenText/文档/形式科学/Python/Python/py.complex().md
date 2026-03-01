##### complex()
- `complex( real , imag )`
	- 创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
```python
# 创建一个复数
z1 = complex(3, 4)
print(z1)  # 输出：(3+4j)

# 创建一个纯虚数
z2 = complex(0, 2)
print(z2)  # 输出：2j

# 不指定虚部，默认为 0
z3 = complex(5)
print(z3)  # 输出：(5+0j)

# 不指定实部和虚部，默认为 0
z4 = complex()
print(z4)  # 输出：0j

```