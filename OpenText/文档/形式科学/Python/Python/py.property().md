##### property()
- `@property`
	- [[py.装饰器|装饰器]]，把类的方法伪装成属性调用，Foo.func()的调用方法，变成Foo.func
	- 同时可以定义与之关联的 setter 方法（用于设置属性值）和 deleter 方法（用于删除属性）
- `property( fget , fset , fdel , doc )`
	- 创建属性
	- `fget`，调用 `实例.属性` 时自动执行的方法
	- `fset`，调用 `实例.属性 ＝ XXX`时自动执行的方法
	- `fdel`，调用 `del 实例.属性` 时自动执行的方法
	- `doc`，调用 `实例.属性.__doc__`的描述信息
```python
# 装饰器
class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @age.deleter
    def age(self):
        print("删除年龄数据！")

obj = People("jack", 18)
print(obj.age)  # 查询属性值 @property 
obj.age = 19  # 设置属性值 @age.setter
print("obj.age:  ", obj.age)
del obj.age  # 删除属性值 @age.deleter
```

```python
# 函数
class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    def del_age(self):
        print("删除年龄数据！")

    # 核心在这句
    age = property(get_age, set_age, del_age, "年龄")    
obj = People("jack", 18)
print(obj.age)
obj.age = 19
print("obj.age:  ", obj.age)
del obj.age
```

