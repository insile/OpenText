##### `np.extract(condition, arr)`
**功能简介：**
- 返回满足给定条件的数组元素，这些元素被提取成一个新的一维数组。

**参数说明：**
- `condition`：布尔数组或布尔表达式，用于指定要提取的元素的条件。
- `arr`：输入的数组。

**返回值：**
- 返回一个新的一维数组，其中包含满足条件的元素。

**用法示例：**
```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
condition = arr > 3
result = np.extract(condition, arr)
print(result)  # Output: [4 5 9 6]
```

