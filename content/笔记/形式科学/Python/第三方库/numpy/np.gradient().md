##### `np.gradient(f, *varargs, axis=None, edge_order=1)`
**功能简介：**
- 用于计算 N 维数组的梯度。梯度是一个向量，表示函数在各个坐标轴方向的变化率。对于多维数组，可以在各个维度上计算梯度。

**参数说明：**
- `f`：输入的 N 维数组。
- `*varargs`：可选的参数，表示在哪个轴上计算梯度。每个维度上都可以指定一个轴。
- `axis`：用于指定计算梯度的轴。它可以是整数、元组或列表，用于确定在哪些轴上计算梯度（可选，默认为 None）。
- `edge_order`：用于确定在计算梯度时使用的边界条件的阶数（可选，默认为 1）。

**返回值：**
- 返回一个包含 N 维梯度数组的元组，每个元素对应于一个指定维度上的梯度。

**两个用法实例：**
1. **计算一维数组的梯度**
```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])
gradient_result = np.gradient(arr)
print(gradient_result)
# Output: [3. 4. 6. 8. 9.]
```

2. **计算二维数组在不同轴上的梯度**
  ```python
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
gradient_result_axis0 = np.gradient(matrix, axis=0)
print(gradient_result_axis0)
# Output:
# [array([[3., 3., 3.],
#         [3., 3., 3.],
#         [3., 3., 3.]])]

gradient_result_axis1 = np.gradient(matrix, axis=1)
print(gradient_result_axis1)
# Output:
# [array([[1., 1., 1.],
#         [1., 1., 1.],
#         [1., 1., 1.]])]
```
