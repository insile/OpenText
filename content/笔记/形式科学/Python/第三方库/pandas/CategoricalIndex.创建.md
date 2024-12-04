##### `pd.CategoricalIndex(data=None, categories=None, ordered=None, dtype=None, copy=False, name=None)`
**功能简介:**
- 用于表示基于分类数据的索引类。它用于将具有有限数量离散值的数据映射到整数标签，以便于分析和存储。

**参数说明:**
- `data`：要用作索引的数据，通常是包含分类数据的 Series、数组或其他可迭代对象。
- `categories`：指定可用的分类值。如果未提供，将从 `data` 参数中的唯一值自动提取。
- `ordered`：指定分类是否有顺序关系。默认为 None，表示不指定。
- `dtype`：指定索引的数据类型。
- `copy`：是否在创建索引时复制数据。默认为 False。
- `name`：索引的名称。

**返回值:**
- 返回一个新的 `CategoricalIndex` 对象，表示基于分类数据的索引。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series 包含分类数据
data = ['cat', 'dog', 'dog', 'cat', 'bird', 'dog']
categories = ['cat', 'dog', 'bird']
series = pd.Series(data, dtype="category", categories=categories)

# 创建一个 CategoricalIndex 对象
categorical_index = pd.CategoricalIndex(categories=categories)

# 输出创建的 CategoricalIndex 对象
print(categorical_index)
```


