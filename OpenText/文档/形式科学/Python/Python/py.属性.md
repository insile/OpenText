##### 属性
- 属性
	- 属性是类中的数据成员, 用于描述类的特征或状态. 它们存储在类的实例中, 并可以通过点号 `.` 访问. 属性可以是任何数据类型, 例如整数, 字符串, 列表等. 在类的定义中, 可以使用构造函数 `__init__` 初始化属性
```python
# . 在下面的示例中,`name` 和 `age` 是 `Person` 类的属性, 用于存储人的姓名和年龄信息
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```