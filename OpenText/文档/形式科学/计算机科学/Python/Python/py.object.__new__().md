##### **`object.__new__( cls [, ...] )`**
- 构造方法，静态方法，**调用以创建一个 `cls` 类的新实例**
- `__new__` 方法可以用于在创建对象之前执行一些额外的操作，或者根据特定条件来控制对象的创建过程。
- 如果 `__new__()` 未返回一个 `cls` 的实例，则新实例的 `__init__()` 方法就不会被执行。
##### 自定义
```python
# 单例模式
class MySingleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)  # 调用object方法__new__创建实例，并用类属性储存
        return cls._instance

# 创建实例
obj1 = MySingleton()
obj2 = MySingleton()

print(obj1 is obj2)  # 输出 True，两个变量引用同一个实例

```