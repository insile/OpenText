##### `np.diff(a, n=1, axis=-1, prepend=<no value>, append=<no value>)`
**功能简介：**
- 用于计算数组在给定轴上的差分。它计算数组中相邻元素之间的差值，并返回一个数组，表示在指定轴上的差分结果。

**参数说明：**
- `a`：输入的数组。
- `n`：差分的阶数，表示要对数组进行多少次差分（可选，默认为 1）。
- `axis`：指定在哪个轴上进行差分计算（可选，默认为 -1，即最后一个轴）。
- `prepend`：在数组前面添加的值（可选）。
- `append`：在数组末尾添加的值（可选）。

**返回值：**
- 函数返回计算后的差分数组。

**两个用法实例：**
1. **一维数组的差分**
```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])
diff_result = np.diff(arr)
print(diff_result)  # Output: [3 5 7 9]
```

2. **二维数组在不同轴上的差分**
```python
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diff_result_axis0 = np.diff(matrix, axis=0)
print(diff_result_axis0)
# Output:
# [[3 3 3]
#  [3 3 3]]

diff_result_axis1 = np.diff(matrix, axis=1)
print(diff_result_axis1)
# Output:
# [[1 1]
#  [1 1]
#  [1 1]]
```
