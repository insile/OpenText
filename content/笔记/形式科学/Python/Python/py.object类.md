##### object类
- object类
	- 从[[py.类的继承|类的继承]]角度理解, object类是所有类的父类
	- 所有类都继承自object类, 都可使用一些通用的属性和方法, [[py.object 类方法|object 类方法]]
	- [[py.object()|object()]] 创建object类实例
```python
print(object)  # <class 'object'> object 类

object()  # object 实例
object().__class__  # object 实例的类是 object
object.__class__  # object 类的类是 type
object.__bases__  # object 类没有父类，object类是所有类的父类
```