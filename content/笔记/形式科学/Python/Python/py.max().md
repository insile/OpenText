##### max()
- `max(iterable, *args, key=None, default=None)`
	- 返回给定参数的最大值
	- `iterable` 要查找最大值的可迭代对象
	- `*args` 可选参数，用于比较多个可迭代对象的最大值
	- `key` 可选参数，用于指定一个函数，用于从每个元素中提取一个用于比较的键。默认为 None
	- `default` 可选参数，用于指定当可迭代对象为空时的默认值。如果没有提供此参数且可迭代对象为空，则会引发 `ValueError`
```python
# iterable
numbers = [5, 2, 8, 1, 10]
result = max(numbers)
print(result)  # 输出：10

numbers_tuple = (3.5, 1.5, 4.5)
result = max(numbers_tuple)
print(result)  # 输出：4.5

# *args
result = max(3, 7, 1, 9)
print(result)  # 输出：9

# key
words = ["apple", "banana", "cherry"]
result = max(words, key=len)
print(result)  # 输出："banana"

# default
empty_list = []
result = max(empty_list, default="No values")
print(result)  # 输出："No values"

```