##### 内置特殊属性
- 对象属性
```python
object.__dict__
# 一个字典或其他类型的映射对象，用于存储对象的（可写）属性。
# object.__dict__
# mappingproxy({'__repr__': <slot wrapper '__repr__' of 'object' objects>, 
#				'__hash__': <slot wrapper '__hash__' of 'object' objects>, 
#				'__str__': <slot wrapper '__str__' of 'object' objects>...})
```
- 实例属性
```python
instance.__class__
# 类实例所属的类。
# object().__class__
# <class 'object'>
# object.__class__
# <class 'type'>
```
- 类属性
```python
class.__name__
# 类的名称。

class.__module__
# 类定义所在模块的名称。

class.__dict__
# 包含类命名空间的字典。

class.__bases__
# 由类对象的基类所组成的元组。
# type.__bases__
# (<class 'object'>,)

class.__mro__
# 此属性是由类组成的元组，在方法解析期间会基于它来查找基类。
# type.__mro__
# (<class 'type'>, <class 'object'>)

class.mro()
# 此方法可被一个元类来重载，以为其实例定制方法解析顺序。 它会在类实例化时被调用，其结果存储于 __mro__ 之中。

class.__subclasses__()
# 每个类都存有对直接子类的弱引用列表。本方法返回所有存活引用的列表。列表的顺序按照子类定义的排列。

class.__doc__
# 类的文档字符串，如果未定义则为 None。

class.__annotations__
# 包含在类体执行期间收集的 变量标注 的字典。 有关使用 __annotations__ 的最佳实践，请参阅 对象注解属性的最佳实践。
```
- 其他特殊属性
```python
definition.__name__
# 类、函数、方法、描述器或生成器实例的名称。

definition.__qualname__
# 类、函数、方法、描述器或生成器实例的 qualified name。
```