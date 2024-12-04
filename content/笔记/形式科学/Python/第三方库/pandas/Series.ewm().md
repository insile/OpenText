##### `Series.ewm(com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None, method='single')`
**功能简介:**
- 用于创建指数加权移动窗口

**参数说明:**
- `com`：用于计算移动平均的“层数”的参数。
- `span`：用于计算移动平均的“跨度”的参数。
- `halflife`：用于计算移动平均的“半衰期”的参数。
- `alpha`：用于计算移动平均的“平滑系数”的参数。
- `min_periods`：指定至少需要的非缺失值数量。
- `adjust`：是否进行调整以校正偏差。默认为 True。
- `ignore_na`：是否忽略缺失值。默认为 False。
- `axis`：指定计算的轴。默认为 0，表示按行计算。
- `times`：指定一个时间间隔序列，用于计算平滑参数。
- `method`：指定平滑参数计算的方法，可选值为 'single'（默认）、'mean'、'linear' 等。

**返回值:**
- 返回一个 EWM 对象，可以用于计算指数加权移动平均。您可以在 EWM 对象上调用各种方法，如 `mean`、`std`、`var` 等，以计算指数加权移动平均的不同统计量。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# 计算指数加权移动平均
ewma = series.ewm(span=2).mean()

print("Original Series:")
print(series)

print("\nEWMA:")
print(ewma)
```


