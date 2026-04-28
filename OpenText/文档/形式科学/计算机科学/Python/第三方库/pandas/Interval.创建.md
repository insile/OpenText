##### `pandas.Interval(left, right, closed='right')`
**功能简介:**
- 用于创建封闭区间（Interval）对象

**参数说明:**
- `left`：区间的左边界。
- `right`：区间的右边界。
- `closed`：指定区间的闭合方式，可以是 `'left'`、`'right'`、`'both'`、`'neither'`。默认为 `'right'`。

**返回值:**
- 返回一个 `pandas.Interval` 对象，表示一个封闭区间。

**用法示例:**
```python
import pandas as pd

# 创建封闭区间
interval = pd.Interval(left=0, right=10, closed='both')

print(interval)
```
