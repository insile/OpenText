##### `pd.concat(objs, *, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=None)`
**功能简介:**
- 用于沿指定的轴（axis）将多个 DataFrame 或 Series 进行连接。它可以用于在行或列方向上组合数据。

**参数说明:**
- `objs`：要连接的 DataFrame 或 Series 对象的列表或元组。
- `axis`：连接的轴方向，可以是 `0`（默认，行方向）或 `1`（列方向）。
- `join`：连接时的方式，可以是 `'outer'`、`'inner'`。默认为 `'outer'`。
- `ignore_index`：是否重置连接后的索引。默认为 `False`。
- `keys`：用于层次化索引的键数组。
- `levels`：用于创建 MultiIndex 的层级。
- `names`：用于指定 MultiIndex 层级的名称。
- `verify_integrity`：是否在连接之前验证索引的唯一性。默认为 `False`。
- `sort`：是否在连接后对索引进行排序。默认为 `False`。
- `copy`：是否复制数据。默认为 `None`。

**返回值:**
- 返回一个新的连接后的 DataFrame 或 Series。

**用法示例:**
1. 沿行方向连接多个 DataFrame：
```python
import pandas as pd

# 创建两个 DataFrame
data1 = {'Name': ['Alice', 'Bob'],
         'Age': [25, 30]}
data2 = {'Name': ['Charlie', 'David'],
         'Age': [22, 28]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 使用 concat 函数连接两个 DataFrame
concatenated_df = pd.concat([df1, df2], axis=0)

print(concatenated_df)
```
2. 沿列方向连接多个 Series：
```python
import pandas as pd

# 创建两个 Series
s1 = pd.Series([10, 20], name='A')
s2 = pd.Series([30, 40], name='B')

# 使用 concat 函数连接两个 Series，沿列方向
concatenated_series = pd.concat([s1, s2], axis=1)

print(concatenated_series)
```
