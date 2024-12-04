##### **`object.__bytes__(self)`**
- 用于返回对象的字节表示。这个方法与 `__str__()` 和 `__repr__()` 类似，但是它返回的是一个字节序列（bytes），而不是字符串, [[py.bytes()|bytes()]]
##### 自定义
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bytes__(self):
        # 使用 UTF-8 编码将对象信息转换为字节序列
        info = f"Person: {self.name}, {self.age} years old".encode('utf-8')
        return info

# 创建一个 Person 实例
person1 = Person(name="Alice", age=28)

# 调用 bytes() 函数将对象转换为字节序列
bytes_data = bytes(person1)
print(bytes_data)

```