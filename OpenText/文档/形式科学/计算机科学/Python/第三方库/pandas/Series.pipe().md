##### `Series.pipe(func, *args, **kwargs)`
**功能简介:**
- 在 Series 上应用一个或多个自定义函数，形成一个函数链。这可以在一系列操作中处理 Series，而不需要多次对同一 Series 进行显式的赋值。

**参数说明:**
- `func`：要应用于 Series 的函数，可以是一个或多个函数的组合。
- `*args`：位置参数，用于传递给函数的额外参数。
- `**kwargs`：关键字参数，用于传递给函数的额外关键字参数。

**返回值:**
- 返回函数链处理后的结果，可以是一个新的 Series 或其他对象。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# 定义自定义函数
def double(x):
    return x * 2

def add_ten(x):
    return x + 10

# 使用 pipe 方法构建函数链
result = series.pipe(double).pipe(add_ten)

print("Original Series:")
print(series)

print("\nProcessed Series:")
print(result)
```
