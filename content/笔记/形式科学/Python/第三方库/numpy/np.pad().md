##### `np.pad(array, pad_width, mode='constant', **kwargs)`
**功能简介：**
- 用于在数组的边缘填充值，以扩展数组的尺寸。

**参数说明：**
- `array`：输入的数组，将在其边缘进行填充。
- `pad_width`：指定每个轴边缘的填充宽度，可以是一个整数、一个表示两个边缘的整数元组，或者表示每个轴两个边缘的元组的元组。
- `mode`：填充模式，用于指定填充值的生成方式。默认为 `'constant'`。
- `**kwargs`：其他关键字参数，用于指定特定填充模式的参数。`'constant'` 需要指定 `constant_values`

**返回值：**
- 返回一个填充后的新数组，原数组不会被修改。

**用法实例：**
1. **使用常数填充：**
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
pad_width = 1
padded_arr = np.pad(arr, pad_width, mode='constant')

print(padded_arr)
# 输出：
# [[0 0 0 0]
#  [0 1 2 0]
#  [0 3 4 0]
#  [0 0 0 0]]
```
2. **使用自定义填充值和填充模式：**
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
pad_width = ((1, 2), (2, 1))  # 指定每个轴的填充宽度
fill_value = 9
padded_arr = np.pad(arr, pad_width, mode='constant', constant_values=fill_value)

print(padded_arr)
# 输出：
# [[9 9 9 9 9]
#  [9 1 2 9 9]
#  [9 3 4 9 9]
#  [9 9 9 9 9]]
```
**`mode` 参数：**
- `mode` 参数用于指定填充模式，即在哪种方式下生成填充值。以下是可用的填充模式及其含义：

1. **'constant'（默认）：**
   在边缘填充指定的常数值。使用 `constant_values` 参数指定填充值。

2. **'edge'：**
   使用数组的边缘值来填充。

3. **'linear_ramp'：**
   根据边缘的线性斜率，从边缘值开始线性增加或减少填充值。

4. **'maximum' 和 'minimum'：**
   在填充宽度范围内使用数组边缘的最大值或最小值填充。

5. **'mean'：**
   使用数组边缘的均值来填充。

6. **'median'：**
   使用数组边缘的中值来填充。

7. **'reflect'：**
   对数组边缘进行反射，并使用反射后的值填充。

8. **'symmetric'：**
   对数组边缘进行对称扩展，并使用对称值填充。

9. **'wrap'：**
   将数组视为环形，使用循环中的值填充。

**用法示例：**
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
pad_width = 1

# 使用不同填充模式
padded_constant = np.pad(arr, pad_width, mode='constant', constant_values=0)
padded_edge = np.pad(arr, pad_width, mode='edge')
padded_symmetric = np.pad(arr, pad_width, mode='symmetric')

print("Constant mode:\n", padded_constant)
print("Edge mode:\n", padded_edge)
print("Symmetric mode:\n", padded_symmetric)

# Constant mode:  
#  [[0 0 0 0]  
#  [0 1 2 0]  
#  [0 3 4 0]  
#  [0 0 0 0]]  
# Edge mode:  
#  [[1 1 2 2]  
#  [1 1 2 2]  
#  [3 3 4 4]  
#  [3 3 4 4]]  
# Symmetric mode:  
#  [[1 1 2 2]  
#  [1 1 2 2]  
#  [3 3 4 4]  
#  [3 3 4 4]]
```
