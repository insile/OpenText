##### `np.append(arr, values, axis=None)`
**功能简介：**
- 用于将元素追加到数组的末尾，可以沿指定轴进行操作。

**参数说明：**
- `arr`：输入数组，要将元素追加到它的末尾。
- `values`：要追加到数组中的元素，可以是单个元素、列表、元组或其他类似数组的对象。
- `axis`：指定要追加的轴。默认为 `None`，即将元素展平后追加到数组中。

**返回值：**
- 返回一个新数组，其中包含原数组与追加的元素。原数组不会被修改。

**用法实例：**
1. **追加单个元素：**
```python
import numpy as np

arr = np.array([1, 2, 3])
new_element = 4

new_arr = np.append(arr, new_element)
print(new_arr)
# 输出：[1 2 3 4]
```
2. **沿指定轴追加数组：**
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
new_row = np.array([7, 8, 9])

new_arr = np.append(arr, [new_row], axis=0)
print(new_arr)
# 输出：
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
```
