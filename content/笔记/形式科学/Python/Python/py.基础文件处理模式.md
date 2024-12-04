##### 基础文件处理模式 
- 全文本操作
```python
# 一次读入，统一处理
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
txt = fo.read()
fo.close()

# 按数量读入，逐步处理
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
txt = fo.read(2)
whlie txt != '':
	txt = fo.read(2)
fo.close()
```
- 文件逐行操作
```python
# 一次读入，分行处理
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
for line in fo.readlines():
	print(line)
fo.close()
	
# 分行读入，逐行处理
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
for line in fo:
	print(line)
fo.close()
```
