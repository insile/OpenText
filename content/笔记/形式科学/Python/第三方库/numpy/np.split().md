##### `np.split(ary, indices_or_sections, axis=0)`
**功能简介：**
- 用于沿指定轴将数组分割成多个子数组。

**参数说明：**
- `ary`：要分割的输入数组。
- `indices_or_sections`：分割点的指标。可以是整数，也可以是表示分割点的一维数组。
- `axis`：指定要沿其分割的轴。默认为 0，即在行方向分割。

**返回值：**
- 返回一个包含分割后子数组的列表。

**两个用法实例：**
1. **在一维数组中分割：**
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
split_indices = [2, 4]

subarrays = np.split(arr, split_indices)
print(subarrays)
# 输出：[array([1, 2]), array([3, 4]), array([5, 6])]
```

1. **在二维数组中沿行分割：**
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_sections = 2

subarrays = np.split(arr, num_sections)
print(subarrays)
# 输出：[array([[1, 2, 3], [4, 5, 6]]), array([[7, 8, 9]])]
```
