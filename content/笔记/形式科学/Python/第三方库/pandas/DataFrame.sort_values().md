##### `DataFrame.sort_values(by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)`
**功能简介:**
- 用于根据指定的列或多列对 DataFrame 进行排序。

**参数说明:**
- `by`：排序的列名或列名列表，如果是多列排序，按照列表中的顺序依次排序。
- `axis`：可选，指定要排序的轴，通常为 `0`（默认），表示按行排序，或 `1`，表示按列排序。
- `ascending`：可选，指定排序顺序，为 `True` 表示升序（默认），为 `False` 表示降序。
- `inplace`：可选，是否在原地修改 DataFrame，而不返回新的 DataFrame，默认为 `False`。
- `kind`：可选，排序算法的类型，可以是 `'quicksort'`、`'mergesort'`、`'heapsort'`，默认为 `'quicksort'`。
- `na_position`：可选，缺失值在排序中的位置，可以是 `'first'`、`'last'`，默认为 `'last'`。
- `ignore_index`：可选，是否忽略原有索引，使用默认的整数索引，默认为 `False`。
- `key`：可选，指定一个函数来生成排序键，可以是函数、方法或可调用对象。

**返回值:**
- 如果 `inplace=True`，则返回 `None`。如果 `inplace=False`，则返回一个新的排序后的 DataFrame。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}
df = pd.DataFrame(data)

# 根据 'Age' 列进行升序排序
sorted_df = df.sort_values(by='Age')

print(sorted_df)

#   col1  col2  col3 col4
# 0    A     2     0    a
# 1    A     1     1    B
# 2    B     9     9    c
# 3  NaN     8     4    D
# 4    D     7     2    e
# 5    C     4     3    F

df.sort_values(by=['col1']) # 按列一排序
df.sort_values(by=['col1', 'col2']) # 按列一列二依次排序
df.sort_values(by='col1', ascending=False) # 按列一降序
df.sort_values(by='col1', ascending=False, na_position='first') # NaN放在开头
df.sort_values(by='col4', key=lambda col: col.str.lower()) # 按列四降序,小写字母
```