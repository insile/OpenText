##### class io.TextIOWrapper 文本文件读写
- `TextIOWrapper`是对文本文件进行I/O操作的类。提供了对文本文件进行高效读写的接口。通常使用`open()`函数打开文本文件时，会得到一个`TextIOWrapper`对象。
```python
file_path = 'example.txt'
with open(file_path,encoding='utf8') as file:
	print(file)
# <_io.TextIOWrapper name='example.txt' mode='r' encoding='utf8'>
```
