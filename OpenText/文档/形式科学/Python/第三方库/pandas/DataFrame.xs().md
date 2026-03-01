##### `DataFrame.xs(key, axis=0, level=None, drop_level=True)`
**功能简介:**
- 用于从多级索引的 DataFrame 中选择交叉部分的数据。

**参数说明:**
- `key`：要选择的索引值或值列表。可以是单个值或多个值的元组。
- `axis`：可选，指定要选择的轴，通常为 `0`（默认），表示按行选择。
- `level`：可选，指定要选择的级别，如果 DataFrame 有多个级别的索引。
- `drop_level`：可选，如果为 `True`，则从结果中删除指定的级别。默认为 `True`。

**返回值:**
- 返回一个新的 DataFrame，其中包含所选交叉部分的数据。

**用法示例:**
```python
import pandas as pd

# 创建一个示例多级索引 DataFrame
data = {'Date': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'Product': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 120]}

df = pd.DataFrame(data)
df.set_index(['Date', 'City', 'Product'], inplace=True)

# 使用 xs 方法选择特定索引值的数据
selected_data = df.xs(('2023-08-01', 'New York', 'A'))
print(selected_data)

selected_data2 = df.xs('New York', level='City')  # City=='New York'
print(selected_data2)
```