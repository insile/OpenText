##### `pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)`
**功能简介:**
- 用于将 DataFrame 从宽格式（wide format）转换为长格式（long format）。这个函数将多列合并为两列，其中一列包含变量名称，另一列包含变量的值。

**参数说明:**
- `frame`：要转换的 DataFrame。
- `id_vars`：要保留的列名，这些列将作为标识变量（id variables）。
- `value_vars`：要转换的列名，这些列将作为值变量（value variables）。
- `var_name`：新生成的变量名称列的名称。
- `value_name`：新生成的值列的名称。
- `col_level`：如果 DataFrame 的列是多层索引的，可以指定列层级。
- `ignore_index`：是否忽略生成的索引。

**返回值:**
- 返回一个新的 DataFrame，包含从宽格式转换为长格式的数据。

**用法示例:**
1. 从宽格式转换为长格式：
```python
import pandas as pd

# 创建一个宽格式的 DataFrame
data = {'Name': ['Alice', 'Bob'],
        'Math': [90, 85],
        'Science': [88, 92]}
df = pd.DataFrame(data)

# 将 DataFrame 从宽格式转换为长格式
melted_df = pd.melt(df, id_vars='Name', value_vars=['Math', 'Science'], var_name='Subject', value_name='Score')

print(melted_df)
```
2. 处理多层索引的 DataFrame：
```python
import pandas as pd

# 创建一个多层索引的 DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Score': [90, 85, 88, 92]}
df = pd.DataFrame(data)
df = df.set_index(['Name', 'Subject'])

# 将多层索引的 DataFrame 从宽格式转换为长格式
melted_df = pd.melt(df, col_level=0, ignore_index=False, var_name='Exam', value_name='Score')

print(melted_df)
```

在这个示例中，通过设置多层索引，将 DataFrame 从宽格式转换为长格式，并保留多层索引的层级信息。

请注意，以上示例假设您已经安装了 pandas 库。您可以使用 `pip install pandas` 命令来安装它。