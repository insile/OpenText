##### hasattr()
- `hasattr( object , name )`
	- 查询是否存在属性
	- `object` 要检查属性的对象
	- `name` 属性的名称
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 30)

# 检查对象是否具有指定的属性
has_name = hasattr(person, 'name')
has_age = hasattr(person, 'age')
has_address = hasattr(person, 'address')

print(has_name)     # 输出：True
print(has_age)      # 输出：True
print(has_address)  # 输出：False

```