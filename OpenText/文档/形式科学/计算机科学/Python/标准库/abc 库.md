##### abc 库
- 抽象基类（Abstract Base Class，简称 ABC）是 Python 中用于定义抽象接口和规范的一种机制。**抽象基类不是用来创建对象的**，而是为了**在子类中定义共同的接口和行为**。抽象基类的主要作用是强制子类实现特定的方法或属性，以确保一致的接口和行为。
- [[abc.图形抽象基类设计]]
- [[abc.产品抽象基类设计]]
```python
from abc import ABC, abstractmethod
```
##### abc 主要API
```python
class abc.ABCMeta
# 用于定义抽象基类 (ABC) 的元类

class abc.ABC
# 抽象基类 (ABC), 用于继承, 自定义抽象基类

@abc.abstractmethod 
# 用于声明抽象方法的装饰器，不需要实现
```

