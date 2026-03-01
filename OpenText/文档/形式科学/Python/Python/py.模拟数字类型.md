##### 模拟数字类型
- 模拟数字类型
	- 模拟数字类型, 例如整数或浮点数, 通过实现一些基本的运算方法, 例如加法, 减法, 乘法等, 以下是一个简单的示例, 演示了如何创建一个模拟整数的类
```python
class MyInteger:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):  # +
        if isinstance(other, MyInteger):
            return MyInteger(self.value + other.value)
        else:
            raise ValueError("Unsupported operand type for +")

    def __sub__(self, other):  # -
        if isinstance(other, MyInteger):
            return MyInteger(self.value - other.value)
        else:
            raise ValueError("Unsupported operand type for -")

    def __mul__(self, other):  # *
        if isinstance(other, MyInteger):
            return MyInteger(self.value * other.value)
        else:
            raise ValueError("Unsupported operand type for *")

    def __str__(self):  # str()
        return str(self.value)

    def __int__(self):  # int()
        return self.value

# 创建模拟整数
num1 = MyInteger(5)
num2 = MyInteger(10)

# 使用模拟整数的操作
sum_result = num1 + num2
print(sum_result)  # 输出：15

diff_result = num2 - num1
print(diff_result)  # 输出：5

prod_result = num1 * num2
print(prod_result)  # 输出：50

# 将模拟整数转换为 Python 内置整数
py_int = int(num1)
print(py_int)  # 输出：5

```

