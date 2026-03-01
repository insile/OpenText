##### `Series.align(other, join='outer', axis=None, level=None, copy=None, fill_value=None, method=None, limit=None, fill_axis=0, broadcast_axis=None)`
**功能简介:**
- 用于对齐两个 Series 对象的方法。它通过对两个 Series 进行索引的重新对齐，使它们的索引相同，从而方便进行数据操作和比较。这个方法允许您指定不同的对齐方式，填充缺失值等。

**参数说明:**
- `other`：另一个 Series 对象，用于与当前 Series 进行对齐。
- `join`：对齐时使用的连接方式，{‘outer’, ‘inner’, ‘left’, ‘right’}，默认 ‘outer’
- `axis`：指定对齐的轴。在 Series 对象中，默认为 None，表示对齐索引；在 DataFrame 中可以指定 'index' 或 'columns'。
- `level`：在多级索引情况下，指定对齐的级别。
- `copy`：是否复制数据，默认为 True。
- `fill_value`：在对齐时，用指定的值填充缺失的数据。
- `method`：对于缺失值的填充方法，可选值为 None（默认）、'ffill'、'bfill' 等。
- `limit`：填充时的最大填充次数。
- `fill_axis`：在 DataFrame 对象中，指定需要填充的轴。
- `broadcast_axis`：在 DataFrame 对象中，指定需要广播的轴。

**返回值:**
- 返回一个元组，包含两个对齐后的 Series。第一个 Series 是当前对象按照对齐规则重新对齐后的结果，第二个 Series 是传入的 `other` 对象按照相同规则重新对齐后的结果。

**用法示例:**
```python
import pandas as pd

# 创建两个示例 Series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

# 对齐两个 Series
aligned_s1, aligned_s2 = s1.align(s2, join='outer', fill_value=0)

print("Aligned Series 1:")
print(aligned_s1)

print("\nAligned Series 2:")
print(aligned_s2)

# s1
# a    1
# b    2
# c    3
# s2
# b    4
# c    5
# d    6
# 对齐后
# s1
# a    1.0
# b    2.0
# c    3.0
# d    0.0
# s2
# a    0.0
# b    4.0
# c    5.0
# d    6.0

```
