##### isinstance()
- `isinstance( object, classinfo )`
	- 测试对象 `object` 是否是某个类 `classinfo` 的实例
	- 函数还可以用于检查对象是否属于多个类之一，只需要将 `classinfo` 参数设置为包含多个类的元组。如果对象是其中任何一个类或其子类的实例，则函数返回 `True`，否则返回 `False`。
```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(isinstance(dog, Dog))      # 输出：True
print(isinstance(dog, Animal))   # 输出：True
print(isinstance(cat, Dog))      # 输出：False
print(isinstance(cat, Cat))      # 输出：True
print(isinstance(cat, Animal))   # 输出：True

print(isinstance(dog, (Dog, Cat)))  # 输出：True
print(isinstance(cat, (Dog, Cat)))  # 输出：True
```