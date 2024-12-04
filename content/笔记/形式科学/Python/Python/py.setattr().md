##### setattr()
- `setattr( object, name, value )`
	- 设置属性值，允许动态地设置对象的属性，无论是已存在的属性还是新创建的属性
	- `object` 要设置属性的对象
	- `name` 属性的名称
	- `value` 要设置的属性值
```python
class Person:
    pass

person = Person()

# 设置对象的属性
setattr(person, 'name', 'Alice')
setattr(person, 'age', 30)

# 访问设置的属性
print(person.name)  # 输出：Alice
print(person.age)   # 输出：30

```