##### getattr()
- `getattr( object , name , default )`
	- 返回一个对象属性值，函数允许你动态地获取对象的属性，无论是已存在的属性还是不存在的属性
	- `object` 要获取属性的对象
	- `name` 属性的名称
	- `default` 可选参数，如果属性不存在，返回的默认值
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 30)

# 获取对象的属性
name = getattr(person, 'name')
age = getattr(person, 'age')

print(name)  # 输出：Alice
print(age)   # 输出：30

# 获取不存在的属性，默认返回 None
address = getattr(person, 'address', None)
print(address)  # 输出：None

```