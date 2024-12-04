##### `DataFrame.fillna(value=None, *, method=None, axis=None, inplace=False, limit=None, downcast=None)`
**功能简介:**
- 用于将 DataFrame 中的缺失值（NaN）替换为指定的值或使用特定的填充方法。

**参数说明:**
- `value`：要用于填充缺失值的值，可以是标量、字典、Series 或 DataFrame。默认为 `None`，表示不指定值。
- `method`：可选，用于指定填充方法，可以是 `'ffill'`（向前填充，使用前一个非缺失值）、`'bfill'`（向后填充，使用后一个非缺失值）或 `None`（不使用填充方法）。默认为 `None`。
- `axis`：可选，用于指定填充的轴，`0` 表示列，`1` 表示行。默认为 `None`，表示不指定轴。
- `inplace`：可选，如果为 `True`，则在原地修改 DataFrame，返回 `None`；如果为 `False`（默认），则返回一个新的 DataFrame，原 DataFrame 不变。
- `limit`：可选，指定每列或每行的连续填充的最大数量。
- `downcast`：可选，指定在填充后尝试将数据类型降低以减少内存使用。可以是 `'integer'`、`'signed'`、`'unsigned'` 或 `None`。

**返回值:**
- 如果 `inplace=True`，则返回 `None`；如果 `inplace=False`，则返回一个新的 DataFrame。

**用法示例:**
```python
import pandas as pd
import numpy as np

# 创建一个含有缺失值的示例 DataFrame
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, np.nan],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))

# 将所有缺失值填充为 0
df.fillna(0)

# 使用向前填充方法填充缺失值
df.fillna(method='ffill')

# “ A”、“ B”、“ C”和“ D”列中的所有缺失值分别替换为0、1、2和3。
values = {"A": 0, "B": 1, "C": 2, "D": 3}
df.fillna(value=values)

# 只替换第一个 NaN 元素
df.fillna(value=values, limit=1)

# 使用另一个 DataFrame 填充，按照相同的列名和相同的索引进行替换
df2 = pd.DataFrame(np.zeros((4, 4)), columns=list("ABCE"))
df.fillna(df2)
```
