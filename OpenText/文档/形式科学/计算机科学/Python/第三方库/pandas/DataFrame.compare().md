##### `DataFrame.compare(other, align_axis=1, keep_shape=False, keep_equal=False, result_names=('self', 'other'))`
**功能简介:**
- 用于在两个 DataFrame 之间逐元素比较，并返回一个新的 DataFrame，显示元素之间的差异。

**参数说明:**
- `other`：另一个要比较的 DataFrame。
- `align_axis`：可选，指定在比较中对齐的轴。可以是 `0`（默认，按行对齐）或 `1`（按列对齐）。
- `keep_shape`：可选，如果为 `True`，则保持输出 DataFrame 的形状与原始 DataFrame 相同，通过填充 NaN 来对齐。如果为 `False`（默认），则输出 DataFrame 会根据比较结果进行重新构造。
- `keep_equal`：可选，如果为 `True`，则相等的值也会在结果中显示。如果为 `False`（默认），则只显示不相等的值。
- `result_names`：可选，一个包含两个元素的元组，用于指定结果 DataFrame 中两个 DataFrame 的名称。默认为 `('self', 'other')`。

**返回值:**
- 返回一个新的 DataFrame，其中显示了两个 DataFrame 之间逐元素的比较结果。

**用法示例:**
```python
import pandas as pd

# 创建两个示例 DataFrame 进行比较
df = pd.DataFrame(
    {
        "col1": ["a", "a", "b", "b", "a"],
        "col2": [1.0, 2.0, 3.0, np.nan, 5.0],
        "col3": [1.0, 2.0, 3.0, 4.0, 5.0]
    },
    columns=["col1", "col2", "col3"],
)
df2 = df.copy()
df2.loc[0, 'col1'] = 'c'
df2.loc[2, 'col3'] = 4.0


# 比较列上的差异
df.compare(df2)
# 结果赋值
df.compare(df2, result_names=("left", "right"))
# 将差异堆叠在行上
df.compare(df2, align_axis=0)
# 同时显示相同的值
df.compare(df2, keep_equal=True)
# 保留所有原始行和列
df.compare(df2, keep_shape=True)

```
