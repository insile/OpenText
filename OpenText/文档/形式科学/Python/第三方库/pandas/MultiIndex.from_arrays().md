##### `MultiIndex.from_arrays(arrays, sortorder=None, names=_NoDefault.no_default)`
**功能简介:**
- 用于从多个数组创建多级索引。这种方法是创建多级索引的一种便捷方式，其中每个数组代表一个级别。

**参数说明:**
- `arrays`：包含数组的列表，每个数组代表多级索引的一个级别。
- `sortorder`：一个包含每个级别的排序顺序的列表。
- `names`：一个包含每个级别名称的列表。默认为 `_NoDefault.no_default`，表示不指定级别名称。

**返回值:**
- 返回一个新的 `MultiIndex` 对象，表示从给定数组创建的多级索引。

**用法示例:**
1. 创建一个基于数组的多级索引：
```python
import pandas as pd

# 创建基于数组的多级索引
array1 = ['A', 'B', 'A', 'B']
array2 = [1, 2, 1, 2]
multi_index = pd.MultiIndex.from_arrays([array1, array2], names=['Letter', 'Number'])

print(multi_index)
```
2. 创建没有指定级别名称的多级索引：
```python
import pandas as pd

# 创建基于数组的多级索引
data = [[10, 20], [30, 40], [50, 60]]
multi_index = pd.MultiIndex.from_arrays(data)

print(multi_index)
```
