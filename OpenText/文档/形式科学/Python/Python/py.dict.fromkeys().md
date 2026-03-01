##### dict.fromkeys()
- `dict.fromkeys(iterable[, value])`
	- 字典类方法, 使用来自 iterable 的键创建一个新字典，并将键值设为 value
```python
dict.fromkeys([1,2,3],[1,2,3])
# {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]}
dict.fromkeys([1,2,3],1)
# {1: 1, 2: 1, 3: 1}
```

