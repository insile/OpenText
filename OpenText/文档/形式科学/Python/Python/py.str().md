##### str()
- `str( object='' )`
	- 将对象转化为字符串, 没有参数返回 `''`
```python
# 将整数转换为字符串
num = 42
num_str = str(num)
print(num_str)  # 输出："42"

# 将浮点数转换为字符串
float_num = 3.14
float_str = str(float_num)
print(float_str)  # 输出："3.14"

# 将布尔值转换为字符串
bool_val = True
bool_str = str(bool_val)
print(bool_str)  # 输出："True"

# 将列表转换为字符串
my_list = [1, 2, 3]
list_str = str(my_list)
print(list_str)  # 输出："[1, 2, 3]"

```