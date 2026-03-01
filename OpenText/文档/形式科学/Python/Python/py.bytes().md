##### bytes()
- `bytes( source , encoding , errors )`
	- 创建[[py.字节|字节]]
	- `source`：可选参数，用于初始化字节对象的数据。可以是整数序列、字符串、可迭代对象等。
	- `encoding`：可选参数，指定用于编码字符串时的字符集。
	- `errors`：可选参数，指定在编码过程中遇到错误时的处理方式。
```python
# 创建一个空的字节对象
empty_bytes = bytes()
print(empty_bytes)  # 输出：b''

# 创建一个包含整数序列的字节对象
int_list = [65, 66, 67]
int_bytes = bytes(int_list)
print(int_bytes)  # 输出：b'ABC'

# 创建一个包含 ASCII 编码的字符串的字节对象
ascii_str = "hello"
ascii_bytes = bytes(ascii_str, encoding='ascii')
print(ascii_bytes)  # 输出：b'hello'

# 创建一个包含 UTF-8 编码的字符串的字节对象
utf8_str = "你好"
utf8_bytes = bytes(utf8_str, encoding='utf-8')
print(utf8_bytes)  # 输出：b'\xe4\xbd\xa0\xe5\xa5\xbd'
```
