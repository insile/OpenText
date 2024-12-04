##### DataFrame.astype(dtype, copy=None, errors='raise')
**功能简介:**
- 用于将 DataFrame 中的数据类型转换为指定的数据类型。

**参数说明:**
- `dtype`：要转换成的数据类型，可以是数据类型对象、字符串（如 `'int'`、`'float'`、`'str'` 等）或字典形式的数据类型映射。
- `copy`：可选，如果为 `True`，则返回转换后的 DataFrame 的副本；如果为 `False`，则在原地修改 DataFrame。默认为 `None`，表示根据情况决定。
- `errors`：可选，指定对于无法转换的值的处理方式。默认为 `'raise'`，表示引发异常；还可以选择 `'ignore'`，表示忽略转换失败的值。

**返回值:**
- 如果 `copy=True`，则返回转换后的新 DataFrame。如果 `copy=False` 或 `None`，则在原地修改 DataFrame。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

# 全部转 int32
df.astype('int32').dtypes

# col1转int32，col2转int16
df.astype({'col1': 'int32',
		  'col2': 'int16'}).dtypes

print(df.dtypes)
```
