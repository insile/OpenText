##### any()
- `any( iterable )`
	- 判断[[py.迭代器对象|可迭代对象]]是否有任何一个为 True，存在返回 True，否则返回 True
```python
# 判断列表中的任何一个元素是否为真
my_list = [False, True, False, False]
result = any(my_list)
print(result)  # 输出：True

# 判断元组中的任何一个元素是否为真
my_tuple = (0, 0, 0, 1)
result = any(my_tuple)
print(result)  # 输出：True

# 判断集合中的任何一个元素是否为真
my_set = {0, False, None, ''}
result = any(my_set)
print(result)  # 输出：False

```