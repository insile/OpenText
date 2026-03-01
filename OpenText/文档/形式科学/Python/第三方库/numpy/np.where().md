##### `np.where(condition, x, y)`
**功能简介：**
- 根据给定的条件从两个输入数组 `x` 和 `y` 中选择元素，并返回一个新数组，其中元素来自于 `x` 或 `y`，取决于条件。

**参数说明：**
- `condition`：一个布尔数组或布尔表达式，用于指定选择元素的条件。
- `x`：可选参数，输入数组 `x`。
- `y`：可选参数，输入数组 `y`。
	- 如果仅提供 `condition` 参数，则返回满足条件的元素的索引。
	- 如果同时提供 `x` 和 `y` 参数，则返回一个新数组，其中满足条件的元素来自 `x`，不满足条件的元素来自 `y`。

**返回值：**
- 如果仅提供 `condition` 参数，则返回满足条件的元素的索引组成的元组，每个元素是一个数组，包含相应维度的索引。
- 如果同时提供 `x` 和 `y` 参数，则返回一个新数组，其中满足条件的元素来自 `x`，不满足条件的元素来自 `y`。

**用法示例：**
1. **返回满足条件的元素的索引**
```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
condition = arr > 3
indices = np.where(condition)
print(indices)  # Output: (array([2, 4, 5, 7]),)
```
2. **根据条件选择元素**
```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
condition = arr > 3
result = np.where(condition, arr, -1)
print(result)  # Output: [-1 -1  4 -1  5  9 -1  6]
```

