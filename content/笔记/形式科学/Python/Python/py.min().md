##### min()
- `min( iterable, *args, key=None, default=None )`
	- 给定参数的最小值
	- `iterable` 要查找最小值的可迭代对象
	- `*args` 可选参数，用于比较多个可迭代对象的最小值
	- `key` 可选参数，用于指定一个函数，用于从每个元素中提取一个用于比较的键。默认为 None
	- `default` 可选参数，用于指定当可迭代对象为空时的默认值。如果没有提供此参数且可迭代对象为空，则会引发 `ValueError`
```python
# iterable
numbers = [5, 2, 8, 1, 10]
result = min(numbers)
print(result)  # 输出：1

numbers_tuple = (3.5, 1.5, 4.5)
result = min(numbers_tuple)
print(result)  # 输出：1.5

# *args
result = min(3, 7, 1, 9)
print(result)  # 输出：1

# key
words = ["apple", "banana", "cherry"]
result = min(words, key=len)
print(result)  # 输出："apple"

# default
empty_list = []
result = min(empty_list, default="No values")
print(result)  # 输出："No values"

```