##### `np.insert(arr, obj, values[, axis])`
**功能简介：**
- 用于在数组的指定位置插入值。

**参数说明：**
- `arr`：输入数组，在其中插入值。
- `obj`：表示插入位置的标量或数组。它指示在 `arr` 的哪些索引位置插入值。
- `values`：要插入的值。可以是单个值，也可以是与 `obj` 形状兼容的数组。
- `axis`：可选参数，指定在哪个轴上执行插入操作。默认为 `None`，表示将数组展平后执行插入操作。

**返回值：**
- 返回一个新的数组，其中包含插入值后的结果。原数组不会被修改。

**两个用法实例：**
1. **在一维数组中插入值：**
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
insert_index = 2
value_to_insert = 5

new_arr = np.insert(arr, insert_index, value_to_insert)
print(new_arr)
# 输出：[1 2 5 3 4]
```

1. **在多维数组中插入行或列：**
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
row_to_insert = np.array([5, 6])

new_arr = np.insert(arr, 1, row_to_insert, axis=0)
print(new_arr)
# 输出：
# [[1 2]
#  [5 6]
#  [3 4]]
   ```
