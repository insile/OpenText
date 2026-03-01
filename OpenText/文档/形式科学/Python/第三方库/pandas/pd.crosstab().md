##### `pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)`
**功能简介:**
- 函数用于创建交叉表（crosstab），也称为列联表。交叉表用于汇总和分析两个或多个分类变量之间的关系。

**参数说明:**
- `index`：用作行索引的列名或列索引。
- `columns`：用作列索引的列名或列索引。
- `values`：要聚合的值，通常是一个数值列的列名或列索引。
- `rownames`：行索引的名称。
- `colnames`：列索引的名称。
- `aggfunc`：用于聚合的函数，默认为 `None`，可以是 `'sum'`、`'count'`、`'mean'` 等。
- `margins`：是否显示汇总行和列。
- `margins_name`：汇总行和列的名称。
- `dropna`：是否在计算之前删除包含缺失值的行或列。
- `normalize`：是否对结果进行标准化，以显示相对频率。

**返回值:**
- 返回一个新的交叉表（DataFrame）。

**用法示例:**
1. 创建交叉表：
```python
import pandas as pd

# 创建一个包含分类数据的 DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Type': ['Midterm', 'Midterm', 'Final', 'Final'],
        'Score': [90, 85, 88, 92]}
df = pd.DataFrame(data)

# 使用 crosstab 函数创建交叉表
cross_tab = pd.crosstab(index=df['Name'], columns=df['Subject'], values=df['Score'], aggfunc='mean')

print(cross_tab)
```
2. 创建包含汇总行和列的交叉表：
```python
import pandas as pd

# 创建一个更复杂的分类数据的 DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Type': ['Midterm', 'Midterm', 'Final', 'Final'],
        'Score': [90, 85, 88, 92]}
df = pd.DataFrame(data)

# 使用 crosstab 函数创建交叉表，包含汇总行和列
cross_tab = pd.crosstab(index=df['Name'], columns=[df['Subject'], df['Type']], values=df['Score'], aggfunc='mean', margins=True)

print(cross_tab)
```