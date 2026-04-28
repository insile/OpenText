##### 字节
- 字节 `<class 'bytes'>`
	- 字节是一种不可变的序列类型, 用于存储一个8bits字节数据. 字节对象是由一系列整数 (0-255) 组成的, 每个整数表示一个字节的值, 字节类型通常用于处理二进制数据, 例如文件读写, 网络通信, 加密等场景, 涉及[[py.字符编码|字符编码]]
- 创建字节
	- [[py.字符串前缀||b 前缀]]
	- [[py.bytes()|bytes()]]

```python
# ascii编码可直接现实字符

# 创建空字节
a = bytes()
a = b''

# 字符串转字节
a = b'abc'
a = 'abc'.encode('UTF-8')
[x for x in a] # [97, 98, 99]
# 指定编码方式
a = bytes('abc',encoding='ASCII')
# 字节转字符串
a = b'abc'.decode('UTF-8')
```

