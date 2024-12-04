##### 类的定义与实例化
- 类的定义
	- 类的定义使用 [[py.class|class]] 保留字
- 类的实例化
	- 实例化类是指创建类的对象, 通常是将类看作一个函数去调用 `object = Classname(args)`. 实例化通过构造方法 [object.\_\_new\_\_()](py.object.__new__().md) 和初始化方法 [object.\_\_init\_\_()](py.object.__init__().md) 来创建一个实例
```python
# 定义了一个 Person 类
# 它具有两个属性 name 和 age, 以及一个方法 greet()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# 创建一个 Person 对象
person1 = Person("Alice", 30)
person1.greet()  # 调用对象的方法

# 创建另一个 Person 对象
person2 = Person("Bob", 25)
person2.greet()
```


