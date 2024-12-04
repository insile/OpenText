##### frozenset()
- `frozenset( iterable )`
	- 从[[py.迭代器对象|可迭代对象]]返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
```python
# 创建一个空的不可变集合
empty_frozenset = frozenset()
print(empty_frozenset)  # 输出：frozenset()

# 创建一个包含元素的不可变集合
my_set = frozenset([1, 2, 3])
print(my_set)  # 输出：frozenset({1, 2, 3})

```