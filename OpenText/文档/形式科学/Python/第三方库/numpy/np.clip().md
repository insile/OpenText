##### `numpy.clip(a, a_min, a_max, out=None, **kwargs)`
**功能简介：**
- 用于将数组中的元素限制在给定的范围内。如果数组元素小于 `a_min`，则将其设置为 `a_min`；如果数组元素大于 `a_max`，则将其设置为 `a_max`。

**参数说明：**
- `a`：输入的数组。
- `a_min`：数组元素的下限，小于此值的元素将被设置为 `a_min`。
- `a_max`：数组元素的上限，大于此值的元素将被设置为 `a_max`。
- `out`：可选的输出数组，用于存储结果。
- `**kwargs`：其他可选关键字参数。

**返回值：**
- 返回一个新的数组，其中的元素已经被限制在给定范围内。

**两个用法实例：**
1. **限制一维数组的范围**
```python
import numpy as np

arr = np.array([1, 5, 8, 10, 3])
clipped_arr = np.clip(arr, a_min=3, a_max=8)
print(clipped_arr)  # Output: [3 5 8 8 3]
```

2. **在指定范围内限制二维数组**
```python
import numpy as np

matrix = np.array([[1, 9, 3], [5, 7, 2]])
clipped_matrix = np.clip(matrix, a_min=3, a_max=7)
print(clipped_matrix)
# Output:
# [[3 7 3]
#  [5 7 3]]
  ```

