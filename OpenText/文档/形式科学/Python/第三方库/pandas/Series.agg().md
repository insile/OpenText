##### `Series.agg(func=None, axis=0, *args, **kwargs)`
**功能简介:**
- 用于对 Series 中的元素应用一个或多个聚合函数，以计算汇总统计量。这允许您在 Series 上进行自定义的聚合操作，并返回一个包含计算结果的新 Series。

**参数说明:**
- `func`：要应用于 Series 的聚合函数或函数列表。可以是内置的聚合函数（如 'sum'、'mean'）或自定义的函数。
- `axis`：指定应用聚合函数的轴。默认为 0，表示应用于列方向。
- `*args`：位置参数，用于传递给聚合函数的额外参数。
- `**kwargs`：关键字参数，用于传递给聚合函数的额外关键字参数。

**返回值:**
- 返回一个新的 Series，其中包含应用给定聚合函数后的计算结果。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series
data = [10, 15, 20, 25, 30]
series = pd.Series(data)

# 使用 agg 方法计算多个统计量
agg_results = series.agg(['sum', 'mean', 'max', 'min'])

print("Original Series:")
print(series)

print("\nAggregation Results:")
print(agg_results)

# 传递自定义的聚合函数
def custom_agg(x):
    return x.max() - x.min()

custom_result = series.agg(custom_agg)
print("\nCustom Aggregation Result:")
print(custom_result)
```