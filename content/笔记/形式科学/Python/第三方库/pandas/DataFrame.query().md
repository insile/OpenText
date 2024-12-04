##### `DataFrame.query(expr, *, inplace=False, **kwargs)`
**功能简介:**
- 用于从 DataFrame 中选择满足指定条件的行，返回一个新的 DataFrame。它通过传递一个表达式字符串来过滤数据。

**参数说明:**
- `expr`：要求满足的表达式字符串，用于筛选数据。
- `inplace`：可选，是否在原地修改 DataFrame，而不返回新的 DataFrame，默认为 `False`。
- `kwargs`：可选，关键字参数，用于传递额外的变量到表达式中。

**返回值:**
- 如果 `inplace=True`，则返回 `None`。如果 `inplace=False`，则返回一个新的 DataFrame，其中包含满足条件的行。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28]}
df = pd.DataFrame(data)

# 使用 query 方法筛选年龄大于 25 的行
filtered_df = df.query('Age > 25')  # df[df.Age>25]

print(filtered_df)


df = pd.DataFrame({'A': range(1, 6),
                   'B': range(10, 0, -2),
                   'C C': range(10, 5, -1)})
df.query('A > B')  # df[df.A > df.B]

```
