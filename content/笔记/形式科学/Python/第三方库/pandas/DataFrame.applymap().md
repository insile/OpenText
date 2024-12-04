##### `DataFrame.applymap(func, na_action=None, **kwargs)`
**功能简介:**
- 用于在 DataFrame 的每个元素上应用一个函数。

**参数说明:**
- `func`：要应用的函数，可以是内置函数、自定义函数或匿名函数。
- `na_action`：可选，用于控制处理缺失值的行为。可以是 `'error'`（默认，引发异常）、`'ignore'`（忽略）或 `None`（保留缺失值）。
- `**kwargs`：可选，传递给函数的关键字参数。

**返回值:**
- 返回一个新的 DataFrame，其中的每个元素都经过函数处理。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# 使用 lambda 函数将每个元素加倍
doubled_df = df.applymap(lambda x: x * 2)

print("原始 DataFrame:\n", df)
print("每个元素加倍后的 DataFrame:\n", doubled_df)
```
