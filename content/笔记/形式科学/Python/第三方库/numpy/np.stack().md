##### `np.stack(arrays, axis=0, out=None, *, dtype=None, casting='same_kind')`
**功能简介：**
- 用于在新轴上沿指定的轴堆叠数组序列。

**参数说明：**
- `arrays`：一个数组序列，表示要堆叠的输入数组。
- `axis`：用于指定在哪个轴上进行堆叠。默认为 0，即在新的零号轴上进行堆叠。
- `out`：可选参数，用于指定结果的输出数组。如果未提供，将创建一个新的数组。
- `dtype`：可选参数，用于指定结果数组的数据类型。
- `casting`：可选参数，用于指定数据类型强制转换的规则。

**返回值：**
- 返回一个包含堆叠后数组的新数组。

**两个用法实例：**
1. **沿新轴堆叠一维数组：**
```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

stacked_arr = np.stack((arr1, arr2))
print(stacked_arr)
# 输出：
# [[1 2 3]
#  [4 5 6]]
```

2. **沿现有轴堆叠二维数组：**
```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

stacked_arr = np.stack((arr1, arr2), axis=1)
print(stacked_arr)
# 输出：
# [[[1 2]
#   [5 6]]
#
#  [[3 4]
#   [7 8]]]
```
