##### `np.trapz(y, x=None, dx=1.0, axis=-1)`
**功能简介：**
- 使用复合梯形法则在指定轴上积分数组。它通过在相邻数据点之间的线段下方绘制梯形来估计积分值。

**参数说明：**
- `y`：输入的一维或多维数组，表示要积分的数据。
- `x`：可选的一维数组，表示数据点的 x 坐标。如果未提供，则默认为等距间隔的索引。
- `dx`：用于计算梯形的步长（可选，默认为 1.0）。
- `axis`：指定在哪个轴上进行积分（可选，默认为 -1，即最后一个轴）。

**返回值：**
- 返回一个数组，其中每个元素是在指定轴上的积分结果。

**两个用法实例：**
1. **对一维数组进行积分**
```python
import numpy as np

y = np.array([1, 2, 3, 4])
integral = np.trapz(y)
print(integral)  # Output: 7.5
```
2. **对二维数组在指定轴上进行积分**
```python
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
integral_axis0 = np.trapz(matrix, axis=0)
print(integral_axis0)  # Output: [2.5 3.5 4.5]

integral_axis1 = np.trapz(matrix, axis=1)
print(integral_axis1)  # Output: [ 4. 10.]
  ```

