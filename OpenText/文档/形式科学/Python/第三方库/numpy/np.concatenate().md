##### `np.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")`
**功能简介：**
- 沿着现有轴连接一系列数组。

**参数说明：**
- `(a1, a2, ...)`：要连接的数组序列。可以使用逗号分隔传入多个数组。
- `axis`：用于指定在哪个轴上进行连接。默认为 0，即在行方向连接。
- `out`：可选参数，用于指定结果的输出数组。如果未提供，将创建一个新的数组。
- `dtype`：可选参数，用于指定结果数组的数据类型。
- `casting`：可选参数，用于指定数据类型强制转换的规则。

**返回值：**
- 返回连接后的新数组。

**两个用法实例：**
1. **在行方向连接一维数组：**
```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr)
# 输出：[1 2 3 4 5 6]
```
2. **在列方向连接二维数组：**
```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

concatenated_arr = np.concatenate((arr1, arr2.T), axis=1)
print(concatenated_arr)
# 输出：
# [[1 2 5]
#  [3 4 6]]
```

