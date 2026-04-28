##### `DataFrame.drop(labels=None, *, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')`
**功能简介:**
- 用于从 DataFrame 中删除指定的行或列。

**参数说明:**
- `labels`：要删除的行或列的标签或标签列表。
- `axis`：可选，指定要删除的轴，`0` 表示行，`1` 表示列，默认为 `0`。
- `index`：可选，要删除的行的标签或标签列表，用于代替 `labels` 参数。
- `columns`：可选，要删除的列的标签或标签列表，用于代替 `labels` 参数。
- `level`：可选，当 DataFrame 具有多级索引时，指定要删除的级别。
- `inplace`：可选，如果为 `True`，则在原地修改 DataFrame，返回 `None`；如果为 `False`（默认），则返回一个新的 DataFrame，原 DataFrame 不变。
- `errors`：可选，如果为 `'raise'`，则在指定的标签不存在时引发异常；如果为 `'ignore'`，则忽略不存在的标签。

**返回值:**
- 如果 `inplace=True`，则返回 `None`；如果 `inplace=False`，则返回一个新的 DataFrame。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# 删除列 'B'
df_dropped = df.drop(columns='B')

# 删除行索引为 1 的行
df_dropped_row = df.drop(index=1)

print("原始 DataFrame:\n", df)
print("删除列 'B' 后的 DataFrame:\n", df_dropped)
print("删除行索引为 1 的行后的 DataFrame:\n", df_dropped_row)


# 多级索引
midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
                             ['speed', 'weight', 'length']],
                     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                            [0, 1, 2, 0, 1, 2, 0, 1, 2]])
df = pd.DataFrame(index=midx, columns=['big', 'small'],
                  data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                        [250, 150], [1.5, 0.8], [320, 250],
                        [1, 0.8], [0.3, 0.2]])

# 删除索引为 ('falcon', 'weight') 的行
df.drop(index=('falcon', 'weight'))
# 删除 'small' 列 和 'cow' 行
df.drop(index='cow', columns='small')
# 删除 2 级索引 'length' 行
df.drop(index='length', level=1)


```

