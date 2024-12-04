##### `DataFrame.insert(loc, column, value, allow_duplicates=_NoDefault.no_default)`
**功能简介:**
- 用于在指定位置插入一个新的列到 DataFrame 中。

**参数说明:**
- `loc`：要插入的列的位置，可以是整数索引或列标签。
- `column`：要插入的列的名称。
- `value`：要插入的列的数据值，可以是标量、数组、Series 等。
- `allow_duplicates`：可选，是否允许插入重复列名，默认为不允许。

**返回值:**
- 无，原地修改了 DataFrame。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}
df = pd.DataFrame(data)

# 插入新的列 'Gender' 到索引位置 1
df.insert(1, 'Gender', ['Female', 'Male', 'Male'])

print(df)
```
