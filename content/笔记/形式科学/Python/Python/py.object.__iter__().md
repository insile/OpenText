##### `object.__iter__()`
- 此方法会在需要为一个容器创建迭代器时被调用。 此方法应当返回一个新的迭代器对象，它可以对容器中的所有对象执行迭代。 对于映射，它应当对窗口中的键执行迭代。
- 返回一个[[py.迭代器对象|迭代器对象]]对象，通常是类自己，实现了`__next__`方法
```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
```