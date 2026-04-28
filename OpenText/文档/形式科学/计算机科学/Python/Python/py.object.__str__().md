##### **`object.__str__(self)`**
- 用于返回对象的字符串表示。当您尝试使用 [[py.str()|str()]] [[py.print()|print()]] 函数将对象转换为字符串时，Python 会自动调用对象的 `__str__` 方法来生成对象的字符串表示。
- 您可以通过自定义 `__str__` 方法来控制对象的字符串表示，使其更加有意义和易读。下面是一个示例，展示了如何自定义 `__str__` 方法来定制对象的字符串表示
- 通常 `__repr__ == __str__`
##### 自定义
```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old, {self.gender}"

# 创建一个 Person 实例
person1 = Person(name="Alice", age=28, gender="female")


# 使用 str() 函数将对象转换为字符串
print(str(person1))  # 输出：Person: Alice, 28 years old, female
# 使用 print() 函数
print(person1)  # 输出：Person: Alice, 28 years old, female
# 在交互式环境中直接输入对象名
person1  # <__main__.Person at 0x1c114726220>
```