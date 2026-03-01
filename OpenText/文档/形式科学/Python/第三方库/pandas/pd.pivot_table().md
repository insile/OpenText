##### `pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False, sort=True)`
**功能简介:**
- 用于从长格式数据创建一个透视表，类似于 Excel 中的数据透视表。透视表可以对数据进行聚合，并将行和列重新组织。

**参数说明:**
- `data`：要使用的长格式数据，通常是一个 DataFrame。
- `values`：要聚合的值，通常是一个数值列的列名或列索引。
- `index`：要放置在行上的行名或行索引。
- `columns`：要放置在列上的列名或列索引。
- `aggfunc`：用于聚合的函数，默认为 `'mean'`，可以是 `'sum'`、`'count'`、`'min'` 等。
- `fill_value`：用于替换缺失值的值。
- `margins`：是否显示汇总行和列。
- `dropna`：是否在计算之前删除包含缺失值的行或列。
- `margins_name`：汇总行和列的名称。
- `observed`：是否只使用观察到的值，用于处理类别变量。
- `sort`：是否对行和列标签进行排序。

**返回值:**
- 返回一个新的透视表（DataFrame）。

**用法示例:**
1. 从长格式数据创建透视表：
```python
import pandas as pd

# 创建一个长格式的 DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Score': [90, 85, 88, 92]}
df = pd.DataFrame(data)

# 使用 pivot_table 函数创建透视表
pivot_table = pd.pivot_table(data=df, values='Score', index='Name', columns='Subject', aggfunc='mean')

print(pivot_table)
```
2. 创建包含汇总行和列的透视表：
```python
import pandas as pd

# 创建一个更复杂的长格式 DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Type': ['Midterm', 'Midterm', 'Final', 'Final'],
        'Score': [90, 85, 88, 92]}
df = pd.DataFrame(data)

# 使用 pivot_table 函数创建透视表，包含汇总行和列
pivot_table = pd.pivot_table(data=df, values='Score', index=['Name', 'Type'], columns='Subject', aggfunc='mean', margins=True)

print(pivot_table)
```