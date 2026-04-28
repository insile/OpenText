##### issubclass()
- `issubclass( class, classinfo )`
	- 判断一个类数 `class` 是否是另一个类 `classinfo` 的子类
	- 函数还可以用于检查一个类是否继承自多个类之一，只需要将 `classinfo` 参数设置为包含多个类的元组。如果类是其中任何一个类的子类，则函数返回 `True`，否则返回 `False`。
```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

print(issubclass(Dog, Mammal))          # 输出：True
print(issubclass(Dog, Animal))          # 输出：True
print(issubclass(Cat, Mammal))          # 输出：True
print(issubclass(Cat, Bird))            # 输出：False
print(issubclass(Dog, (Mammal, Bird)))  # 输出：True
print(issubclass(Cat, (Mammal, Bird)))  # 输出：True

```