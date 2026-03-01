##### bytearray()
- `bytearray([source , encoding , errors )`
	- 创建[[py.字节数组|字节数组]]，元素可变
	- `source`：可选参数，用于初始化字节数组的数据。可以是整数序列、字符串、可迭代对象等。
	- `encoding`：可选参数，指定用于编码字符串时的字符集。
	- `errors`：可选参数，指定在编码过程中遇到错误时的处理方式。
```python
# 创建一个空的字节数组
empty_bytearray = bytearray()
print(empty_bytearray)  # 输出：bytearray(b'')

# 创建一个包含整数序列的字节数组
int_list = [65, 66, 67]
int_bytearray = bytearray(int_list)
print(int_bytearray)  # 输出：bytearray(b'ABC')

# 创建一个包含 ASCII 编码的字符串的字节数组
ascii_str = "hello"
ascii_bytearray = bytearray(ascii_str, encoding='ascii')
print(ascii_bytearray)  # 输出：bytearray(b'hello')

# 创建一个包含 UTF-8 编码的字符串的字节数组
utf8_str = "你好"
utf8_bytearray = bytearray(utf8_str, encoding='utf-8')
print(utf8_bytearray)  # 输出：bytearray(b'\xe4\xbd\xa0\xe5\xa5\xbd')

# 创建一个字节数组
byte_array = bytearray(b'hello')
# 修改字节数组的第一个字节
byte_array[0] = 104  # 修改为字节 'h' 的 ASCII 值
print(byte_array)  # 输出：bytearray(b'hello')

# 创建一个空的字节数组
empty_bytearray = bytearray()
print(empty_bytearray)  # 输出：bytearray(b'')

# 创建一个包含字节的字节数组
bytearray_with_data = bytearray(b'hello')
print(bytearray_with_data)  # 输出：bytearray(b'hello')

byte_array = bytearray(b'hello')
byte_array[0] = 72  # 修改第一个字节为 ASCII 值 72 (H)
byte_array[1:3] = b'XY'  # 修改索引 1 到 2 的字节为 XY
print(byte_array)  # 输出：bytearray(b'HXYlo')
```