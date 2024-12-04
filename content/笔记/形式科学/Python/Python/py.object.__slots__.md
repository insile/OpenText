##### `object.__slots__`
- 特殊类属性, 限制类实例能添加的属性
```python
class Person:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建一个 Person 实例
person = Person(name="Alice", age=25)

# 访问实例的属性
print(person.name)  # 输出：Alice
print(person.age)   # 输出：25

# 添加新属性会引发 AttributeError
# person.gender = 'female'  # AttributeError: 'Person' object has no attribute 'gender'

```