##### 闭包
- 闭包
	- 闭包指内层函数引用了外层函数的局部变量, 外层函数返回值为内层函数
	- 外层变量赋值需要使用[[py.nonlocal|nonlocal]]关键字
	- 返回函数不要引用任何循环变量, 或者后续会发生变化的变量
```python
# 外层函数
def sum_out(*args):  
	
	# 内层函数
    def sum_in():  
        ax = 0
		for n in args:  # 外层变量 args
            ax = ax + n  
        return ax  

	# 返回内层函数
	return sum_in

a = sum_out(1,2,3)
a() # 6
```