##### `pd.RangeIndex(start=None, stop=None, step=None, dtype=None, copy=False, name=None)`
**功能简介:**
- 用于表示连续整数范围的索引类。它是一种特殊类型的索引，用于表示连续的整数标签，常用于创建默认索引或整数索引。

**参数说明:**
- `start`：索引的起始值，默认为 0。
- `stop`：索引的结束值（不包括），必须提供。
- `step`：索引值之间的步长，默认为 1。
- `dtype`：指定索引的数据类型。
- `copy`：是否在创建索引时复制数据。默认为 False。
- `name`：索引的名称。

**返回值:**
- 返回一个新的 `RangeIndex` 对象，表示创建的连续整数范围索引。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 RangeIndex
index = pd.RangeIndex(start=0, stop=5, step=1)

# 访问 RangeIndex 的属性和方法
print("RangeIndex:")
print(index)
print("Index Name:", index.name)
print("Index Data Type:", index.dtype)
print("Is Unique:", index.is_unique)
print("Location of 3:", index.get_loc(3))
```
