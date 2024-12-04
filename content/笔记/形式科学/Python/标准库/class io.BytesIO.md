##### class io.BytesIO 内存二进制流
- 用于在内存中创建一个类似文件的对象，用于对字节数据进行读写操作。它提供了一种方便的方式，使得你可以像操作文件一样处理字节数据，而无需实际创建物理文件。
- 实例化方法
```python
io.BytesIO(initial_bytes=b'')
```
- 实例方法
```python
BytesIO.getbuffer()
	# 返回一个对应于缓冲区内容的可读写视图而不必拷贝其数据。 此外，改变视图将透明地更新缓冲区内容

BytesIO.getvalue()
	# 返回包含整个缓冲区内容的 bytes。

BytesIO.read1(size=- 1, /)
	# 在 BytesIO 中，这与 read() 相同。

BytesIO.readinto1(b, /)
	# 在 BytesIO 中，这与 readinto() 相同。
```
##### 示例
- 英文
```python
import io

# 创建一个内存文件对象
bytes_io = io.BytesIO()

# 写入字节数据到内存文件对象
data = b'\x48\x65\x6c\x6c\x6f, BytesIO!'
bytes_io.write(data)

# 读取内存文件对象中的内容
content = bytes_io.getvalue()
print("Content:", content)

# 关闭内存文件对象
bytes_io.close()
```
- 中文
```python
import io

# 创建一个内存文件对象
bytes_io = io.BytesIO()

# 写入字节数据到内存文件对象
data = b'\x48\x65\x6c\x6c\x6f, BytesIO!'
bytes_io.write(data)

# 读取内存文件对象中的内容
content = bytes_io.getvalue()
print("Content:", content)

# 关闭内存文件对象
bytes_io.close()
```
