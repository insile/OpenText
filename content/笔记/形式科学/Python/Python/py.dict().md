##### dict()
- `dict(**kwargs)`
- `dict(mapping, **kwargs)`
- `dict(iterable, **kwargs)`
	- 创建字典
	- `**kwargs`：关键字参数，用于指定键值对。
	- `mapping`：映射对象，可以是字典或其他支持映射协议的对象。
	- `iterable`：[[py.迭代器对象|可迭代对象]]，可以包含键值对的序列（如元组）。
```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
a == b == c == d == e == f  # True


```