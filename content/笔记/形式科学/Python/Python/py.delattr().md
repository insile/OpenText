##### delattr()
- `delattr( object , name )`
	- 删除属性，允许在运行时动态地删除对象的属性
	- `object` 要删除属性的对象
	- `name` 属性的名称
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 30)

# 删除对象的属性
delattr(person, 'age')

# 尝试访问已删除的属性将引发 AttributeError
print(person.name)  # 输出：Alice
print(person.age)   # 引发 AttributeError: 'Person' object has no attribute 'age'

```