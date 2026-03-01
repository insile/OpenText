##### `Series.expanding(min_periods=1, axis=0, method='single')`
**功能简介:**
- 用于计算扩展窗口的统计量，可以在 Series 上执行逐步扩展窗口的操作，如计算累积和、累积平均等。

**参数说明:**
- `min_periods`：指定在计算统计量时至少需要的非缺失值数量。
- `axis`：指定计算的轴。默认为 0，表示按行计算。
- `method`：指定统计量计算的方法，可选值为 'single'（默认）、'sum'、'mean' 等。

**返回值:**
- 返回一个 Expanding 对象，可以用于计算扩展窗口统计量。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# 计算扩展窗口的累积和
expanding_sum = series.expanding().sum()

print("Original Series:")
print(series)

print("\nExpanding Sum:")
print(expanding_sum)
```
