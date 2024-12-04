##### 异常处理
- 异常处理
	- 异常处理涉及[[py.异常类型|异常类型]]和[[py.异常调用栈|异常调用栈]]
	- [[py.try|try]]、[[py.except|except]]、[[py.else|else]]、[[py.finally|finally]]
	- [[py.raise|raise 语句]]、[[py.assert|assert 语句]]
```python
异常处理形式
'''
try:
	语句块1
except 异常类型名称 as e: # 用变量e保存错误信息
	语句块2
else:
	语句块3（正常完成的奖励）
finally:
	语句块4（始终执行的语句）
'''
try:
    # 代码块，可能会引发异常
    result = 10 / 0
except ZeroDivisionError as e:
    # 捕获除零异常
    print(f"Error: {e}")
except Exception as e:
    # 捕获其他异常
    print(f"Unexpected error: {e}")
else:
    # 没有异常发生时执行
    print("No error occurred.")
finally:
    # 无论是否发生异常都执行
    print("Finally block executed.")
```
