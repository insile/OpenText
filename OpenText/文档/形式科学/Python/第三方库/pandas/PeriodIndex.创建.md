##### `pd.PeriodIndex(data=None, ordinal=None, freq=None, dtype=None, copy=False, name=None, **fields)`
**功能简介:**
- 用于创建周期索引的对象。周期索引用于标识一系列时间段，通常由频率和序数组成。

**参数说明:**
- `data`：一个包含周期数据的列表、数组、Series 或其他可迭代对象。
- `ordinal`：周期的序数，用于指定周期的位置。如果提供 `data` 参数，则不需要提供 `ordinal` 参数。
- `freq`：周期的频率字符串或对象，用于指定周期索引的频率。
- `dtype`：指定索引的数据类型。
- `copy`：是否在创建索引时复制数据。默认为 False。
- `name`：索引的名称。
- `**fields`：周期的字段，如 `'year'`、`'month'`、`'day'` 等。

**返回值:**
- 返回一个新的 `PeriodIndex` 对象，表示从给定周期数据创建的周期索引。

**用法示例:**
1. 创建一个基于周期数据的索引：
```python
import pandas as pd

# 创建基于周期数据的索引
data = ['2023-08', '2023-09', '2023-10']
period_index = pd.PeriodIndex(data, freq='M')

print(period_index)
```
2. 创建具有周期字段的周期索引：
```python
import pandas as pd

# 创建具有周期字段的周期索引
data = ['2023-08', '2023-09', '2023-10']
period_index_fields = pd.PeriodIndex(data, freq='M', fields='year')

print(period_index_fields)
```