##### sum()
- `sum( iterable , start=0 )`
	- 对[[py.迭代器对象|可迭代对象]]求和, 初始值为`start`
```python
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)  # 输出：15

numbers_tuple = (2.5, 3.5, 4.5)
result = sum(numbers_tuple)
print(result)  # 输出：10.5

numbers_set = {10, 20, 30}
result = sum(numbers_set)
print(result)  # 输出：60

result = sum(range(1, 6))
print(result)  # 输出：15

result = sum(range(1, 6), 10)  # 初始值为 10
print(result)  # 输出：25

```