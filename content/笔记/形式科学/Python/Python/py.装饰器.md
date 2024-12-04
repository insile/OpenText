##### 装饰器
- 装饰器
	- 在代码运行期间动态增加功能的方式, 称之为“装饰器”, 属于[[py.闭包|闭包]], 使用函数修饰符 `@`, 例如[[py.property()|property()]]、[[py.staticmethod()|staticmethod()]]、[[py.classmethod()|classmethod()]]
	- 使用函数装饰器 funA 去装饰另一个函数 funB
		- 将 B 作为参数传给 A 函数
		- 将 A 函数执行完成的返回值反馈回  B
	- 原函数的属性失效
	- 当装饰器带有多个参数的时候, 装饰器函数就需要多加一层嵌套
	- 装饰器会修改函数名字, 导入[[functools 库]]还原，`@functools.wraps(func)`
```python
# 装饰器写法
def decorator(func):  
    def wrapper(*args, **kwargs):  
		pass # 附加功能
        return func(*args, **kwargs) # 原始功能
    return wrapper

# 一般用法
def funB():
	pass
funB = funA(funB)

# 使用修饰符@
@funA
def funB():
	pass

# 无参装饰器
def decorator(func):  
    def wrapper(*args, **kwargs):  
        print('123')  
        return func(*args, **kwargs)    
    return wrapper  
@decorator  
def say_hello():  
    print('同学你好')  
say_hello()

# 有参装饰器，再套一层传参
def info(value):  
    def decorator(func):  
        def wrapper(*args, **kwargs):  
            print(value)  
            return func(*args, **kwargs)  
        return wrapper  
    return decorator  

@info('456')  
def say_hello():  
    print('同学你好')  
    
say_hello()

# 还原函数名
import functools

def info(value):  
    def decorator(func):  
		@functools.wraps(func)
        def wrapper(*args, **kwargs):  
            print(value)  
            return func(*args, **kwargs)  
        return wrapper  
    return decorator  

```
