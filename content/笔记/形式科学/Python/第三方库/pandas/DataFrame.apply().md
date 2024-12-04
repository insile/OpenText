##### `DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)`
**功能简介:**
- 用于在 DataFrame 上应用一个函数，对每一列或每一行进行操作。

**参数说明:**
- `func`：要应用的函数，可以是内置函数、自定义函数或匿名函数。
- `axis`：可选，指定要应用函数的轴，`0` 表示对每一列应用，`1` 表示对每一行应用。默认为 `0`。
- `raw`：可选，如果为 `True`，则将原始数据传递给函数，否则将每一列或每一行作为 Series 传递给函数。默认为 `False`。
- `result_type`：可选，指定返回结果的数据类型，可以是 `'expand'`（默认，返回 DataFrame）、`'reduce'`（返回 Series）或 `None`（返回与输入一样的数据类型）。
- `args`：可选，传递给函数的位置参数，以元组形式。
- `**kwargs`：可选，传递给函数的关键字参数。

**返回值:**
- 返回一个新的 DataFrame（默认情况下），或者一个新的 Series，或者一个与输入类型相同的结果，具体取决于 `result_type` 参数的设置。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# 对每一列应用 sum 函数
column_sums = df.apply(sum)

# 对每一行应用 max 函数
row_maxes = df.apply(max, axis=1)

print("原始 DataFrame:\n", df)
print("每列的和:\n", column_sums)
print("每行的最大值:\n", row_maxes)
```
