##### class
- `class`
	- 用于[[py.类和对象|类和对象]]中定义类

```python
# 最简单的类定义形式
class 类名:
    # 代码块

# 简单的类
class Dog:
    name = "Candy"
dog = Dor()
print(dog.name)


# 带有父类和元类的定义形式
class 子类(父类, metaclass=元类):
    # 代码块

# type类创建类对象Person，通过type.__new__()
class Person(object, metaclass=type):  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def greet(self):  
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")  


# Person类创建实例对象person，通过object.__new__()
person = Person("Alice", 30)  
person.greet()  # 调用对象的方法  
```
