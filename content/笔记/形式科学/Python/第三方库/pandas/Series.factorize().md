##### `Series.factorize(sort=False, use_na_sentinel=True)`
**功能简介:**
- 用于将 Series 中的唯一值转换为连续的整数编码，以便进行分类或离散数据的编码。它可以用于将分类数据转换为数字标签，以便进行分析或建模。

**参数说明:**
- `sort`：控制是否对唯一值进行排序后再进行编码。默认为 False。
- `use_na_sentinel`：控制是否使用额外的哨兵编码来表示缺失值。默认为 True，表示使用 -1 表示缺失值。

**返回值:**
- 返回一个元组，包含两个元素。第一个元素是编码后的整数标签的数组，第二个元素是唯一值的数组。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series
data = ['cat', 'dog', 'dog', 'cat', 'bird', 'dog', 'bird', 'cat']
series = pd.Series(data)

# 使用 factorize 方法将分类数据编码为整数标签
labels, unique_values = series.factorize()

print("Original Series:")
print(series)

print("\nLabels:")
print(labels)

print("\nUnique Values:")
print(unique_values)
```
