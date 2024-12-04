##### `Series.unstack(level=- 1, fill_value=None)`
**功能简介:**
- 用于将具有层次化索引的 Series 转换为 DataFrame。它可以将 Series 的索引中的一个级别转换为列，并创建一个新的 DataFrame。

**参数说明:**
- `level`：指定要移除的索引级别，并将其转换为列。默认为 -1，表示移除最内层的索引。
- `fill_value`：指定在转换过程中用于填充缺失值的值。

**返回值:**
- 返回一个新的 DataFrame，其中索引的一个级别被转换为了列。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series，具有多级索引
index = pd.MultiIndex.from_tuples([('A', 'X'), ('A', 'Y'), ('B', 'X'), ('B', 'Y')])
data = [10, 20, 30, 40]
series = pd.Series(data, index=index)

# 使用 unstack 方法将内层索引转换为列
unstacked_df = series.unstack()

print("Original Series:")
print(series)

print("\nUnstacked DataFrame:")
print(unstacked_df)
```
