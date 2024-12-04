##### 序列操作符
- 序列操作符
	- `+` 连接; `*` 复制
```python
# + 运算符用于连接序列
# * 运算符用于复制序列

str1 = "Hello"
str2 = " World"
concatenated_str = str1 + str2
print("连接字符串:", concatenated_str)
repeated_str = str1 * 3
print("复制字符串:", repeated_str)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("连接列表:", concatenated_list)
repeated_list = list1 * 2
print("复制列表:", repeated_list)

tuple1 = (7, 8, 9)
tuple2 = (10, 11, 12)
concatenated_tuple = tuple1 + tuple2
print("连接元组:", concatenated_tuple)
repeated_tuple = tuple1 * 4
print("复制元组:", repeated_tuple)
```