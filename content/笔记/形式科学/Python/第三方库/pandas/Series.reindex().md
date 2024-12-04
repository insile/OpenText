##### `Series.reindex(index=None, *, axis=None, method=None, copy=None, level=None, fill_value=None, limit=None, tolerance=None)`
**功能简介:**
- 用于重新索引 Series，返回一个具有新索引的 Series。可以添加、删除或重新排列索引，同时可以使用不同的填充值来处理缺失的索引。

**参数说明:**
- `index`：可选，新的索引。可以是索引标签的列表、数组、Series 等。
- `axis`：可选，指定重新索引的轴，通常为 `None`（默认），表示索引轴。
- `method`：可选，插值（填充）方法，可以是 `'pad'`、`'ffill'`、`'bfill'`、`'backfill'` 等。
- `copy`：可选，是否创建副本，默认为 `None`。
- `level`：可选，多级索引的级别。
- `fill_value`：可选，用于填充缺失索引的值。
- `limit`：可选，对于插值方法，指定连续缺失值的最大数量。
- `tolerance`：可选，用于数值索引的容差。

**返回值:**
- 返回一个具有新索引的 Series。

**用法示例:**
```python
import pandas as pd

# 创建一个 Series
data = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(data)

# 创建新的索引
new_index = ['a', 'b', 'c', 'd']

# 重新索引 Series
s_reindexed = s.reindex(new_index)

print(s_reindexed)
```