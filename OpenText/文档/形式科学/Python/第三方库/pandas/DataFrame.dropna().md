##### `DataFrame.dropna(*, axis=0, how=_NoDefault.no_default, thresh=_NoDefault.no_default, subset=None, inplace=False, ignore_index=False)`
**功能简介:**
- 用于删除 DataFrame 中包含缺失值的行或列。

**参数说明:**
- `axis`：固定为 `0`，表示删除包含缺失值的行。
- `how`：可选，用于指定删除行的条件。默认为 `_NoDefault.no_default`，表示不指定条件。可以是 `'any'`（默认，任何缺失值）、`'all'`（所有值为缺失值）或 `None`（不指定）。
- `thresh`：可选，删除行时要求非缺失值的数量大于或等于 `thresh`。默认为 `_NoDefault.no_default`，表示不指定数量。
- `subset`：可选，要考虑的列的标签或标签列表，用于删除行或列中的缺失值。
- `inplace`：可选，如果为 `True`，则在原地修改 DataFrame，返回 `None`；如果为 `False`（默认），则返回一个新的 DataFrame，原 DataFrame 不变。
- `ignore_index`：可选，如果为 `True`，则重新索引删除后的 DataFrame。默认为 `False`。

**返回值:**
- 如果 `inplace=True`，则返回 `None`；如果 `inplace=False`，则返回一个新的 DataFrame。

**用法示例:**
```python
import pandas as pd
import numpy as np

# 创建一个含有缺失值的示例 DataFrame
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})

# 删除含有任何缺失值的行
df.dropna()
# 删除含有任何缺失值的列
df.dropna(axis=1)
# 删除缺少所有元素的行
df.dropna(how='all')
# 删除至少有 2 个非缺失值的行
df.dropna(thresh=2)
# 定义在哪些列中查找缺少的值
df.dropna(subset=['name', 'toy'])

```
