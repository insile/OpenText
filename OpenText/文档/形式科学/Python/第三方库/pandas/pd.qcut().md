##### `pd.qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise')`
**功能简介:**
- 用于将连续的数值变量划分为指定数量的分位数（quantile）。它可以用于创建等分的分组并对数据进行分析。

**参数说明:**
- `x`：要划分的连续数值变量，通常是一个 Series 或类似的数组。
- `q`：要创建的分位数的数量，也可以是一个列表，表示每个分位数的值。
- `labels`：用于替代每个分位数的标签。
- `retbins`：是否返回分位数的边界。默认为 `False`。
- `precision`：分位数的小数位数。
- `duplicates`：在出现重复分位数值时的处理方式，可以是 `'raise'`、`'drop'`、`'raise'`。

**返回值:**
- 返回一个包含每个数据点所在分位数的 Categorical 对象。

**用法示例:**
1. 划分数据为分位数：
```python
import pandas as pd

# 创建一个包含数值数据的 Series
data = pd.Series([10, 20, 25, 35, 40, 50, 60, 70, 80, 90])

# 使用 qcut 函数划分数据为分位数
quantiles = 3
quantile_labels = ['Low', 'Medium', 'High']
categories = pd.qcut(data, q=quantiles, labels=quantile_labels)

print(categories)
```
2. 返回分位数的边界：
```python
import pandas as pd

# 创建一个包含数值数据的 Series
data = pd.Series([10, 20, 25, 35, 40, 50, 60, 70, 80, 90])

# 使用 qcut 函数划分数据为分位数，并返回分位数的边界
quantiles = 3
categories, quantile_edges = pd.qcut(data, q=quantiles, retbins=True)

print(categories)
print(quantile_edges)
```
