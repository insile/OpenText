##### with
- `with`
	- 用于[[py.上下文管理器对象|上下文管理器类型]], 提供了一种方便的方式来管理资源的获取和释放, 确保在代码块执行后, 资源得到适当的清理和释放, 初学可以简单理解 `with/as` 是对 `try/finally` 的一种替代方案
```python
# with 形式
'''
with 上下文管理器 as 变量:
	# 代码块
'''

# with/as
with open(r'a.log') as logfile:
    for line in logfile:
        print(line)
        ...more code here...

# try/finally
myfile = open(r'a.log')
try:
    for line in myfile:
        print(line)
        ...more code here...
finally:
    myfile.close()


```