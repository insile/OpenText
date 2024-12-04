##### tuple()
- `tuple( iterable )`
	- 用于将一个[[py.迭代器对象|可迭代对象]]转换为元组类型
```python
# 将列表转换为元组
my_list = [1, 2, 3]
list_tuple = tuple(my_list)
print(list_tuple)  # 输出：(1, 2, 3)

# 将字符串转换为元组
my_string = "hello"
string_tuple = tuple(my_string)
print(string_tuple)  # 输出：('h', 'e', 'l', 'l', 'o')

# 将字典的键转换为元组
my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_keys_tuple = tuple(my_dict)
print(dict_keys_tuple)  # 输出：('a', 'b', 'c')

```