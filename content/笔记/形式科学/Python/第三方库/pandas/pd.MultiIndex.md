##### `pd.MultiIndex(levels=None, codes=None, sortorder=None, names=None, dtype=None, copy=False, name=None, verify_integrity=True)`
**功能简介:**
- 用于创建多级索引的对象。多级索引是在一个轴上使用多个级别的标签，用于处理具有多维结构的数据。

**参数说明:**
- `levels`：一个包含每个级别的标签的列表的列表。
- `codes`：一个包含每个级别标签索引的列表的列表。
- `sortorder`：一个包含每个级别的排序顺序的列表。
- `names`：一个包含每个级别名称的列表。
- `dtype`：指定索引的数据类型。
- `copy`：是否在创建索引时复制数据。默认为 False。
- `name`：索引的名称。
- `verify_integrity`：是否在创建索引时验证索引的一致性，默认为 True。

**返回值:**
- 返回一个新的 `MultiIndex` 对象，表示创建的多级索引。

**用法示例:**
1. 创建一个基本的多级索引：
```python
import pandas as pd

# 创建一个基本的 MultiIndex
levels = [['A', 'B'], [1, 2]]
codes = [[0, 0, 1, 1], [0, 1, 0, 1]]
multi_index = pd.MultiIndex(levels=levels, codes=codes, names=['Letter', 'Number'])

print(multi_index)
```
2. 创建带有级别名称的多级索引：
```python
import pandas as pd

# 创建带有级别名称的 MultiIndex
data = [(10, 20), (30, 40), (50, 60)]
index = pd.MultiIndex.from_tuples(data, names=['First', 'Second'])

print(index)
```

