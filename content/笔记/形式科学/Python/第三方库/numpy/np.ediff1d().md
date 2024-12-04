##### `np.ediff1d(ary, to_end=None, to_begin=None)`
**功能简介：**
- 用于计算数组中相邻元素之间的差异。它返回一个表示相邻元素差异的数组。

**参数说明：**
- `ary`：输入的数组。
- `to_end`：在数组末尾添加的值（可选）。
- `to_begin`：在数组开头添加的值（可选）。

**返回值：**
- 返回一个数组，其中包含了相邻元素的差异。

**两个用法实例：**
1. **计算相邻元素的差异**
```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])
diff_result = np.ediff1d(arr)
print(diff_result)  # Output: [3 5 7 9]
```

2. **添加起始和末尾的值**
```python
import numpy as np

arr = np.array([4, 9, 16])
diff_result = np.ediff1d(arr, to_begin=0, to_end=25)
print(diff_result)  # Output: [ 0  4  5  7  9 25]
```

