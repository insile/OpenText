##### 类的继承
- 类的继承
	- 继承是多个类之间的父子关系, 继承的类为子类, 被继承的类为父类或基类, 基类也可能指更高级别父类, [[py.object类|object类]] 是所有类的默认父类
		- 继承的形式为 `Class 子类 (父类1，父类2，…): `
		- 子类继承父类的所有公有和保护实例变量和方法
		- 子类可以继承多个父类
		- [[py.子类可以覆盖父类的属性和方法|子类可以覆盖父类的属性和方法]]
		- [[py.子类可以调用父类的属性和方法|子类可以调用父类的属性和方法]], 包括覆盖和未覆盖
		- 调用父类解析顺序MRO, 广度优先查找, 可使用子类[[py.内置特殊属性|内置特殊属性]] `__mro__` 查看
```python
# 动物类
class Animal:
    def __init__(self, name):
        self.name = name
# 狗类
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的初始化方法
        self.breed = breed

# 创建子类的实例
dog = Dog("Buddy", "Golden Retriever")

print(dog.name)   # 输出：Buddy
print(dog.breed)  # 输出：Golden Retriever
```