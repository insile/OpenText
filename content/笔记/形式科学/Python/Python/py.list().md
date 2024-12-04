##### list()
- `list( iterable )`
	- 用于将一个[[py.迭代器对象|可迭代对象]]转换为列表类型
```python
# 将元组转换为列表
my_tuple = (1, 2, 3)
tuple_list = list(my_tuple)
print(tuple_list)  # 输出：[1, 2, 3]

# 将字符串转换为列表
my_string = "hello"
string_list = list(my_string)
print(string_list)  # 输出：['h', 'e', 'l', 'l', 'o']

# 将字典的键转换为列表
my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_keys_list = list(my_dict)
print(dict_keys_list)  # 输出：['a', 'b', 'c']

```