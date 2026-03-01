##### class io.StringIO 内存文本流
- 用于在内存中创建一个类似文件的对象，支持对字符串数据进行读写操作
- 实例化方法
```python
io.StringIO(initial_value='', newline='\n')
```
- 实例方法
```python
StringIO.getvalue()
	# 返回一个包含缓冲区全部内容的 str。 换行符会以与 read() 相同的方式被编码，但是流的位置不会被改变。
```
##### 示例
```python
import io

# 创建一个内存文件对象
string_io = io.StringIO()

# 写入字符串到内存文件对象
string_io.write("Hello, StringIO!")

# 读取内存文件对象中的内容
content = string_io.getvalue()
print("Content:", content)

# 关闭内存文件对象
string_io.close()


```
