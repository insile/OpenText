##### zip()
- `zip(iterable1, iterable2, ...)`
	- 第 i 个元组包含的是每个可迭代对象参数的第 i 个元素，返回[[py.迭代器对象|迭代器对象]]
	- 逆操作：参数前加星号，用于转置
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# 使用 zip() 函数将姓名和分数进行配对
zipped_data = zip(names, scores)

# 转换为列表查看结果
result = list(zipped_data)
print(result)  # 输出：[('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# 转置还原
result2 = list(zip(*result))
print(result2)  # 输出：[('Alice', 'Bob', 'Charlie'), (85, 92, 78)]
```

