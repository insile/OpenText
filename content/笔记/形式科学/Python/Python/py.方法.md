##### 方法
- 方法
	- 方法是类中的[[py.函数类型|函数]]成员, 用于描述类的行为或操作. 它们定义在类的内部, 可以对类的属性进行操作, 方法也是一种类型. 方法可以接受参数, 并且可以返回一个值. 在方法内部, 通过 `self` 参数可以访问类的属性和其他方法
- 实例方法
	- 在实例方法中, `self` 是一个特殊的参数, 用于**引用类的实例自身**. 它在方法的定义中作为第一个参数, 通常命名为 `self`, 但这只是约定, 您也可以使用其他名称. 通过 `self`, 可以访问类的属性和其他方法, 以及在方法内部操作实例的数据
- 类方法
	- 在类方法中, `cls` 是一个特殊的参数, 用于**引用类自身**. 它通常作为类方法的第一个参数传递, 用于操作类属性或调用其他类方法. 与 `self` 一样, `cls` 也是一个约定俗成的名称, 您可以选择其他名称, 但通常保持一致性会更好
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age} years old.")
	# self 在 __init__ 初始化函数 introduce 方法和 birthday 方法中都被使用
	# 使得我们可以在方法内部访问类的属性 name 和 age 并通过 self.age 对 age 属性进行增加操作。

# 创建 Person 类的实例
person = Person("Alice", 25)

# 调用 introduce() 方法
print(person.introduce())  # 输出：Hello, my name is Alice and I am 25 years old.

# 调用 birthday() 方法
person.birthday()
print(person.introduce())  # 输出：Hello, my name is Alice and I am 26 years old.

```