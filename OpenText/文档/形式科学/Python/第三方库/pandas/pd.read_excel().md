##### `pd.read_excel(io, sheet_name=0, *, header=0, names=None, index_col=None, usecols=None, dtype=None,...)`
**功能简介:**
- 用于从 Excel 文件中读取数据并创建一个 DataFrame。Excel 文件是一种常见的电子表格文件格式，用于存储表格数据和其他信息。

**参数说明:**
- `io`：Excel 文件的路径、URL、文件-like 对象或已打开的文件对象。
- `sheet_name`：要读取的工作表的名称、索引或列表。
- `header`：指定哪一行作为列名，可以是整数、列表、字符串 `'infer'`（自动推断）。
- `names`：指定列名列表。
- `index_col`：用作索引的列名或列编号。
- `usecols`：要读取的列的列表或列编号。
- `skiprows`：跳过的行数。
- `nrows`：读取的行数。
- `na_values`：要识别为缺失值的值的列表。
- `parse_dates`：要解析为日期时间的列的列表。
- `date_parser`：用于解析日期时间列的函数。
- `convert_float`：是否将整数列转换为浮点数。
- `converters`：用于转换列数据的函数字典。
- `dtype`：指定列的数据类型。
- `engine`：解析引擎，可以是 `'xlrd'`、`'openpyxl'` 等。
- `squeeze`：如果数据只有一列，返回 Series 而不是 DataFrame。
- `dtype`：指定数据类型。
- `keep_default_na`：是否保留默认的 NaN 值。
- 等等。

**返回值:**
- 返回一个 DataFrame，包含从 Excel 文件中读取的数据。

**用法示例:**
1. 从 Excel 文件读取数据并创建 DataFrame：
```python
import pandas as pd

# 从 Excel 文件读取数据
excel_filepath = 'data.xlsx'
dataframe = pd.read_excel(excel_filepath)

print(dataframe)
```
2. 指定工作表和列名：
```python
import pandas as pd

# 从 Excel 文件读取数据，指定工作表和列名
excel_filepath = 'data.xlsx'
dataframe = pd.read_excel(excel_filepath, sheet_name='Sheet1', usecols=['Name', 'Age'])

print(dataframe)
```