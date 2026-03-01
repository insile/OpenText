##### 属性与方法
- [[py.属性|属性]]
	- 类属性，直接在类中定义属性
	- 实例属性，在初始化中定义
	- 公有属性，公有类和实例属性无格式要求
	- 私有属性，双下划线开头（半保护，单下划线开头）
	- [[py.内置特殊属性|内置特殊属性]]，双下划线开头双下划线结尾
- [[py.方法|方法]]
	- 实例方法，实例调用
	- 类方法，类调用，[[py.classmethod()|classmethod()]]
	- 静态方法，类调用，[[py.staticmethod()|staticmethod()]]
```python
class Person:
    # 类属性
    species = "Human"

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
        self._protected_attribute = "This is a protected attribute"
        self.__private_attribute = "This is a private attribute"

    # 公有实例方法
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I am a {self.species}.")

    # 私有实例方法
    def __private_method(self):
        print("This is a private method.")

    # 类方法
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

    # 静态方法
    @staticmethod
    def static_example():
        print("This is a static method.")

# 创建一个 Person 实例
person1 = Person(name="Alice", age=28)

# 访问实例属性和类属性
print(person1.name)  # 实例属性
print(Person.species)  # 类属性

# 调用实例方法、类方法和静态方法
person1.introduce()  # 公有实例方法
Person.change_species("Homo Sapiens")  # 类方法
print(Person.species)  # 更新后的类属性
person1.static_example()  # 静态方法

```