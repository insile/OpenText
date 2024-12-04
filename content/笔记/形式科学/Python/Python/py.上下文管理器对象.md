##### 上下文管理器对象
- 上下文管理器对象 `ContextManager`
	- 通过定义一个类, 并实现`__enter__()`和`__exit__()`方法, 那么这个类就可以被称为上下文管理器, 通过[[py.with|with]]调用
	- `__enter__()`: 返回一个值, 可以将它赋值给as后面的对象
	- `__exit__()`: with...as 语句退出或者发送异常时会执行这个方法
```python
# 基于类的上下文管理器
class FileContextManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def __enter__(self):
        """
        with...as..语句的返回值
        :return:
        """
        self.file = open(self.file_path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        with...as 语句退出或者发送异常时会执行这个方法
        :param exc_type: 异常类型
        :param exc_val: 异常信息
        :param exc_tb: 异常栈
        :return: with...as...语句内抛出的异常将以exc_type, exc_val, exc_tb这三个参数传入,
        返回False时这个异常还会向上抛出,也就是抛出给main,返回True时将不会再向外抛出,被抑制
        """
        self.file.close()
        return False


if __name__ == '__main__':
    with open("./router.py") as f:
        print(f.readlines())
    #等价于
    with FileContextManager("./router.py") as file:
        print(file.readlines())

    # FileContextManager __init__
    # FileContextManager __enter__
    # print(file.readlines())
    # FileContextManager __exit__


# 基于生成器的上下文管理器
from contextlib import contextmanager

@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()
        
with file_manager('test.txt', 'w') as f:
    f.write('hello world')
    
# with...as...语句执行碰到yield关键字时返回f,暂停
# with语句结束时继续执行yield关键字后面的内容,finally最后执行
```

