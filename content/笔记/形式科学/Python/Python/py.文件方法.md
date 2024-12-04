##### 文件方法
- 文件方法
```python
file.close()
file.fileno()  # 返回一个整型的文件描述符, 可以用在如os模块的read方法等一些底层操作上。

file.read(size)  # 读入全部内容或前size长度
file.readline(size)  # 读入一行或前size长度
file.readlines(hint)  # 读入所有行或前hint行

file.write(s)  # 向文件写入字符串或字节流
file.writelines(lines)  # 将一个元素全为字符串的列表写入文件

file.seek(offset)  # 改变指针位置，0开头，1当前位置，2文件结尾
	
file.tell()  # 返回文件当前位置。

```
