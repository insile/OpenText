##### staticmethod()
- `@staticmethod`
	- [[py.装饰器|装饰器]]，声明一个静态方法
	- 静态方法可以直接被调用无需实例化，没有`self`参数
```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# 调用静态方法，无需创建类的实例
result1 = MathUtils.add(5, 3)
result2 = MathUtils.multiply(4, 6)

print(result1)  # 输出：8
print(result2)  # 输出：24

```