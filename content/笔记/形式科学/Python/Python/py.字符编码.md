##### 字符编码
- 字符编码
	- 文本转换为数字计算机才能处理, Python 以 UTF-8编码, 是一种将 Unicode 码点映射到字节序列的编码方式
		- 字符串 `'知'`
		- Unicode编码
			- 十进制：30693 
			- 二进制：0111/0111 11/100101
		- UTF-8编码 将二进制Unicode编码分成三段
			- 二进制：1110<u>0111</u> 10<u>011111</u> 10<u>100101</u>
			- 十六进制：E7 9FA5
- 编码：[[py.ord()|ord()]]、[[py.str.encode()|str.encode()]]
- 解码：[[py.chr()|chr()]]、[[py.bytes.decode()|bytes.decode()]]
```python
ord('知')  # 30693
chr(30693)  # 知

'知'.encode()  # b'\xe7\x9f\xa5'
b'\xe7\x9f\xa5'.decode()  # '知'

```