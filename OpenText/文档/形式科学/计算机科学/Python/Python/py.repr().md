##### repr()
- `repr( object )`
	- 输出一个对象的“官方”字符串表示
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

# 使用 repr() 函数获取对象的详细字符串表示
repr_string = repr(person1)
print(repr_string)  # 输出：Person(name='Alice', age=28, gender='female')

```
