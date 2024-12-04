##### `Series.astype(dtype, copy=None, errors='raise')`
**功能简介:**
- 用于将 Series 中的元素转换为指定的数据类型。

**参数说明:**
- `dtype`：要转换为的目标数据类型。
- `copy`：是否创建副本。默认为 `None`。
- `errors`：在遇到无法转换的元素时的处理方式，可以是 `'raise'`（默认，抛出异常）和 `'ignore'`（忽略错误）。

**返回值:**
- 返回一个新的具有指定数据类型的 Series。

**用法示例:**
```python
import pandas as pd

# 创建一个 Series
data = [1, 2, 3, 4, 5]
s = pd.Series(data)

# 将元素转换为浮点型
s_float = s.astype(float)

print(s_float)
```