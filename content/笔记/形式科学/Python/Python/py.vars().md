##### vars()
- `vars( object )`
	- 返回模块、类、实例或任何其它对象的[[py.内置特殊属性|内置特殊属性]] `__dict__` 属性。
	- `object` 可选参数，要获取属性和值的对象
	- 如果不提供该参数，函数会返回[[py.作用域和命名空间|当前作用域]]的属性和值的字典，同[[py.locals()|locals()]]
	- 在[[py.作用域和命名空间|全局作用域]]与[[py.globals()|globals()]]，[[py.locals()|locals()]]相等
```python
# 对象的 __dict__  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vars = vars()

person = Person('Alice', 30)

# 获取对象的属性和值的字典
person_vars = vars(person)  # vars( object )
person_varss = person.vars  # 局部作用域 vars( )
person_dict = person.__dict__  # __dict__

print(person_vars)
print(person_varss)
print(person_dict)

person_vars == person_dict  # True
person_vars == person_varss  # False

# 全局作用域
vars() == locals() == globals()  # True
```
