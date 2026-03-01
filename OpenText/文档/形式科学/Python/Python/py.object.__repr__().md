##### **`object.__repr__(self)`**
- 用于返回对象的“官方”字符串表示[[py.repr()|repr()]]。与 `__str__` 方法类似，`__repr__` 方法也可以用于生成对象的字符串表示，但它通常更偏向于提供详细和准确的信息，以便在调试和开发过程中使用。
- 当您在交互式环境中直接输入对象名并按下回车时，Python 会自动调用对象的 `__repr__` 方法来显示对象的字符串表示。此外，如果没有定义 `__str__` 方法，Python 会使用 `__repr__` 方法作为默认的字符串表示。
- 通常 `__repr__ == __str__`
##### 自定义

```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, gender='{self.gender}')"

# 创建一个 Person 实例
person1 = Person(name="Alice", age=28, gender="female")

# 在交互式环境中直接输入对象名
person1  # 输出：Person(name='Alice', age=28, gender='female')
# 使用 str() 函数将对象转换为字符串
print(str(person1))  # 输出：Person: Alice, 28 years old, female
# 使用 print() 函数
print(person1)  # 输出：Person: Alice, 28 years old, female
```