##### classmethod()
- `@classmethod`
	- [[py.装饰器|装饰器]]， 声明一个类方法
	- 类方法可以直接被调用无需实例化，第一个参数需要是表示类自身类的`cls`参数
```python
class Person:
    total_count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Person.total_count += 1

    @classmethod
    def get_total_count(cls):  # 类方法
        return cls.total_count

# 创建 Person 类的实例
person1 = Person('Alice')
person2 = Person('Bob')

# 调用类方法，无需创建类的实例
count = Person.get_total_count()

print(count)  # 输出：2

```