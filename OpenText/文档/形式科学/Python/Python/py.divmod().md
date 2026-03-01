##### divmod()
- `divmod( a , b )`
	- 返回一个包含商和余数的元组 ( a // b , a % b )
```python
result = divmod(10, 3)
print(result)  # 输出：(3, 1)

quotient, remainder = divmod(15, 4)
print(quotient)   # 输出：3
print(remainder)  # 输出：3

result = divmod(7, 2)
print(result)  # 输出：(3, 1)

```