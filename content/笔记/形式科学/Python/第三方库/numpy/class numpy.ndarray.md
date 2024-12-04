##### class numpy.ndarray
- `numpy.ndarray` 是 NumPy 库中的核心数据结构，表示多维数组
- [[ndarray.创建]]
- [[ndarray.属性]]
- [[ndarray.方法]]
- [[ndarray.索引与切片]]
```python
import numpy as np

# 创建一个一维数组
array_1d = np.array([1, 2, 3, 4, 5])

# 创建一个二维数组
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 打印数组
print("1D Array:")
print(array_1d)

print("\n2D Array:")
print(array_2d)

# 数组形状
print("\nShape of 2D Array:", array_2d.shape)

# 数组数据类型
print("\nData Type of 1D Array:", array_1d.dtype)

```