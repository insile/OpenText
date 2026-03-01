##### `pd.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True)`
**功能简介:**
- 用于将连续的数值变量划分为离散的区间（bin）。它可以用于创建分组并对数据进行分析。

**参数说明:**
- `x`：要划分的连续数值变量，通常是一个 Series 或类似的数组。
- `bins`：用于划分的 bin 的边界。可以是整数表示 bin 的数量，也可以是一个数组表示 bin 的边界。
- `right`：每个 bin 的右边界是否是开区间。默认为 `True`。
- `labels`：用于替代每个 bin 的标签。
- `retbins`：是否返回 bin 的边界。默认为 `False`。
- `precision`：bin 边界的小数位数。
- `include_lowest`：是否将最低值包括在第一个 bin 内。
- `duplicates`：在出现重复 bin 边界时的处理方式，可以是 `'raise'`、`'drop'`、`'raise'`。
- `ordered`：是否对返回的 Categorical 对象进行排序。

**返回值:**
- 返回一个包含每个数据点所在 bin 的 Categorical 对象。

**用法示例:**
1. 划分数据为离散区间：
```python
import pandas as pd

# 创建一个包含数值数据的 Series
data = pd.Series([10, 20, 25, 35, 40, 50, 60, 70, 80, 90])

# 使用 cut 函数划分数据为离散区间
bins = [0, 30, 60, 90]
labels = ['Low', 'Medium', 'High']
categories = pd.cut(data, bins=bins, labels=labels)

print(categories)
```
2. 返回 bin 的边界：
```python
import pandas as pd

# 创建一个包含数值数据的 Series
data = pd.Series([10, 20, 25, 35, 40, 50, 60, 70, 80, 90])

# 使用 cut 函数划分数据为离散区间，并返回 bin 的边界
bins = [0, 30, 60, 90]
categories, bin_edges = pd.cut(data, bins=bins, retbins=True)

print(categories)
print(bin_edges)
```
