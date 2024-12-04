##### `DataFrame.update(other, join='left', overwrite=True, filter_func=None, errors='ignore')`
**功能简介:**
- 用于将一个 DataFrame 的值更新到另一个 DataFrame 中，根据索引或列的匹配进行更新。

**参数说明:**
- `other`：要用于更新的另一个 DataFrame。
- `join`：可选，用于指定在更新时使用的连接方式。可以是 `'left'`（默认，使用左 DataFrame 的索引或列）或 `'right'`（使用右 DataFrame 的索引或列）。
- `overwrite`：可选，如果为 `True`，则会将 `other` DataFrame 的值完全覆盖当前 DataFrame。如果为 `False`，则只会更新缺失的值。默认为 `True`。
- `filter_func`：可选，用于指定一个函数，根据返回值决定是否更新某个单元格的值。默认为 `None`。
- `errors`：可选，用于指定错误处理策略。可以是 `'raise'`（默认，抛出异常）、`'ignore'`（忽略错误）或 `'warn'`（在发生错误时发出警告）。

**返回值:**
- 无返回值，直接在当前 DataFrame 上进行更新。

**用法示例:**
```python
import pandas as pd

# 创建两个示例 DataFrame 进行更新
data1 = {'ID': [1, 2, 3],
         'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 22]}

data2 = {'ID': [2, 3],
         'Age': [28, 24]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 使用 update() 方法进行更新
df1.update(df2)

print("原始 DataFrame:\n", df1)
```
