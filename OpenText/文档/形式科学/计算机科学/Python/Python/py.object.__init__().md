##### **`object.__init__( self [, ...] )`**
- 用于初始化化对象的属性，**增加实例属性并设置其值**
- 当[object.\_\_new\_\_()](py.object.__new__().md)创建一个对象实例时，`__init__` 方法会在对象创建后自动调用，用于设置对象的初始状态。
##### 自定义
```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I am a {self.gender}.")

# 创建一个 Person 实例，并初始化属性
person1 = Person(name="Alice", age=28, gender="female")

# 调用实例方法来操作对象
person1.introduce()  # 输出：Hi, I'm Alice, 28 years old, and I am a female.


```