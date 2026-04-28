##### if 语句
- if 语句
	- 分支语句，由判断条件决定程序运行方向
	- [[py.if|if]] : 主要判断条件
	- [[py.elif|elif]] : 备选判断条件
	- [[py.else|else]] : 不满足条件执行语句
```python
# if 语句形式
'''
if 判断条件1:
	执行语句1
elif 判断条件2:
	执行语句2
elif 判断条件3:
	执行语句3
else: 
	执行语句4
'''

num = 10
if num > 0:
    print("Number is positive.")
elif num < 0:
    print("Number is negative.")
else:
    print("Number is zero.")
# 输出: Number is positive.
```