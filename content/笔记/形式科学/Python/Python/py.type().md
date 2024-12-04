##### type()
- `class type(object)`
- `class type(name, bases, dict, **kwds)`
	- 传递一个对象 `object` 作为参数时，函数返回该对象的类型
	- 传递三个参数时，函数用于动态创建一个新的类。这是[[py.元类的定义与实例化|元类的实例化]]。`name` 新类的名称； `bases` 新类的父类元组， `dict` 包含新类属性和方法的字典
```python
# 查询对象的类型
x = 5
y = "Hello"
z = [1, 2, 3]

print(type(x))  # 输出： <class 'int'>
print(type(y))  # 输出： <class 'str'>
print(type(z))  # 输出： <class 'list'>

# class 语句
class MyClass:
    def __init__(self):
        self.x = 10
    def print_x(self):
        print(self.x)
obj = MyClass()
print(obj.x)          # 输出： 10
obj.print_x()         # 输出： 10
print(type(obj))      # 输出： <class '__main__.MyClass'>

# type() 元类
MyClass = type('MyClass', (object,), {'x': 10, 'print_x': lambda self: print(self.x)})
obj = MyClass()
print(obj.x)          # 输出： 10
obj.print_x()         # 输出： 10
print(type(obj))      # 输出： <class '__main__.MyClass'>

# type() 元类 更复杂的方法
def init_method(self, value):
    self.value = value

def print_value(self):
    print("Value:", self.value)

# 使用 type() 定义类
MyClass = type("MyClass", (object,), {
    "__init__": init_method,
    "print_value": print_value
})

# 创建实例并调用方法
obj = MyClass("Hello, World!")
obj.print_value()

```
