##### all()
- `all( iterable )`
	- 判断[[py.迭代器对象|可迭代对象]]中的所有元素是否都为TRUE，如果是返回True，否则返回False
	- 对于空的可迭代对象，all() 函数会返回 True
```python
# 判断列表中的所有元素是否都为真
my_list = [True, True, False, True]
result = all(my_list)
print(result)  # 输出：False
my_list = []
result = all(my_list)
print(result)  # 输出：True

# 判断元组中的所有元素是否都为真
my_tuple = (1, 2, 3, 4)
result = all(my_tuple)
print(result)  # 输出：True

# 判断集合中的所有元素是否都为真
my_set = {0, 1, 2, 3}
result = all(my_set)
print(result)  # 输出：False

```