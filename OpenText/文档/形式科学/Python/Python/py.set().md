##### set()
- `set( iterable )`
	- 从[[py.迭代器对象|可迭代对象]]创建集合
```python
# 创建一个空的集合
empty_set = set()
print(empty_set)  # 输出：set()

# 创建包含元素的集合
my_set = set([1, 2, 3])
print(my_set)  # 输出：{1, 2, 3}

# 创建包含重复元素的集合（重复元素会被自动去重）
duplicate_set = set([1, 2, 2, 3, 3, 3])
print(duplicate_set)  # 输出：{1, 2, 3}

# 使用字面值创建集合
literal_set = {4, 5, 6}
print(literal_set)  # 输出：{4, 5, 6}

```