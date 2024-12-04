##### print()
- `print( *objects, sep=' ', end='\n', file=sys.stdout, flush=False )`
	- 以字符串形式向控制台输出结果
	- `objects` 一个或多个要打印的对象。可以是字符串、数字、变量等
	- `sep` 可选参数，用于指定各个对象之间的分隔符。默认为一个空格字符
	- `end` 可选参数，用于指定打印结束时的字符。默认为换行符 `\n`
	- `file` 可选参数，用于指定输出的文件对象。默认为标准输出设备 `sys.stdout`
	- `flush` 可选参数，如果为 True，则立即将内容刷新到文件。默认为 False
```python
# 参数end，改变最后输出的信息
print('a',end='a')  # aa

# 加逗号输出为空格
print('1+2=''3')  # 1+2=3
print('1+2=','3')  # 1+2= 3

# 参数sep，改变参数间的逗号空格分隔符
print('1+2=','3'，sep='=')  # 1+2==3

# 引号
print('abc')  # abc
print('"abc"')  # "abc" 

a = 'abc'
print(a)  # abc 
print('a')  # a
print('"a"')  # "a"

# 三引号, 打印换行
print(
'''ab
cd'''
)

```
