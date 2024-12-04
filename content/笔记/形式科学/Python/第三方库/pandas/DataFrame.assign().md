##### `DataFrame.assign(**kwargs)`
**功能简介:**
- 用于返回一个新的 DataFrame，其中包含现有 DataFrame 中的列以及通过指定的关键字参数添加的新列。

**参数说明:**
- `**kwargs`：关键字参数，每个参数的名称是新列的名称，值是要为新列分配的数据。

**返回值:**
- 返回一个新的 DataFrame，包含现有 DataFrame 中的列以及通过关键字参数指定的新列。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}

df = pd.DataFrame(data)

# 使用 assign() 方法添加新列 'C' 和 'D'
df_new = df.assign(C=[7, 8, 9], D=[10, 11, 12])

print("原始 DataFrame:\n", df)
print("添加新列后的 DataFrame:\n", df_new)
```