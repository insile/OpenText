##### 元类的定义与实例化
- 元类的定义
	- 类的类就是元类 (metaclass), 用于控制类的创建和实例化过程. 在Python中, 类本身也是对象, 由元类来创建. 从类和对象的角度理解, 将一个类看作对象时, 元类是类的类, 生成类的类. [[py.type类|type类]]是所有类的默认元类, 所有的类是type类实例化后的对象, 包括[[py.object类|object类]]的类也是type类
	- 继承type类或其子类就可成为元类, 即 `class MyMeta(type):`, 本质上继承了 `type.__new__()`, 需要和 [[py.type()|type()]] 一样的参数 `name`，`bases`，`dict`
- 元类的实例化 (用元类创建一个类)
	- 内建元类的实例化使用 [[py.type()|type()]], 自定义元类的实例化有调用和 [[py.class|class]] 语句两种
	- 当创建一个类时, Python 首先会寻找该类是否有元类, 如果有, 它将使用元类的 ``__new__()`` 方法来创建类对象. 所以所有类默认继承object类 调用了[object.\_\_new\_\_()](py.object.__new__().md) 用于创建实例对象, 而type类继承并覆盖重写了 ``__new__()`` 方法来创建类对象
```python
# 自定义元类MyMeta，通过继承type
class MyMeta(type):
    def __new__(cls, name, bases, dict):  # 覆盖增加自定义操作
        # 在创建类之前可以进行一些自定义操作
        print("Creating class:", name)
        return super().__new__(cls, name, bases, dict)  # 调用type.__new__()


# 使用MyMeta来创建类MyClass
# 方法1 调用
MyClass = MyMeta('MyClass',(object,), {'x': 10, 'print_x': lambda self: print(self.x)})

# 方法2 metaclass参数传递元类
class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value


# 实例化类MyClass
obj = MyClass()
print("Instance value:", obj.value)
```