##### `object.__call__()`
- 可以让自定义类的实例成为可调用对象
```python
class Adder:
    def __init__(self, base):
        self.base = base

    def __call__(self, x):
        return self.base + x

# 创建一个可调用对象
add_five = Adder(base=5)

# 调用可调用对象
result = add_five(10)
print(result)  # 输出：15

```

