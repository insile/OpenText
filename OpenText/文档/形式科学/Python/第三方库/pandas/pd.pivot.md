##### `pd.pivot(data, *, columns, index=typing.Literal[<no_default>], values=typing.Literal[<no_default>])`
**功能简介:**
- 从长格式（long format）的数据创建一个透视表，将其中的行和列进行重新组织，使得每个唯一值都成为一列，并且行索引和列索引都可以自定义。

**参数说明:**
- `data`：要使用的长格式数据，通常是一个 DataFrame。
- `columns`：要放置在列上的列名或列索引。
- `index`：要放置在行上的行名或行索引。默认为 `<no_default>`，意味着该参数是必需的。
- `values`：要填充透视表的值，通常是一个数值列的列名或列索引。

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

# 使用 pivot 函数创建透视表
pivot_table = pd.pivot(data=df, columns='Subject', index='Name', values='Score')

print(pivot_table)
```
2. 使用更多的数据创建透视表：
```python
import pandas as pd

# 创建一个更复杂的长格式 DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Type': ['Midterm', 'Midterm', 'Final', 'Final'],
        'Score': [90, 85, 88, 92]}
df = pd.DataFrame(data)

# 使用 pivot 函数创建透视表
pivot_table = pd.pivot(data=df, columns='Subject', index=['Name', 'Type'], values='Score')

print(pivot_table)
```
