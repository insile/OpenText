##### `np.copyto(dst, src, casting='same_kind', where=True)`
**功能简介：**
- 将源数组的值复制到目标数组中。

**参数说明：**
- `dst`：目标数组，用于接收复制的值。
- `src`：源数组，提供要复制的值。
- `casting`：可选参数，用于指定数据类型转换的规则，可取值为 'no'、'equiv'、'safe'、'same_kind'、'unsafe' 或 'auto'。
- `where`：可选参数，一个布尔数组或布尔表达式，指定哪些位置要进行复制。默认情况下，复制全部位置。

**返回值：**
- 无返回值。`dst` 数组被就地修改，其内容被替换为 `src` 数组的内容。

**用法示例：**
1. **复制指定条件下的元素**
```python
import numpy as np

dst = np.array([1, 2, 3, 4, 5])
src = np.array([10, 20, 30, 40, 50])
condition = src > 25

# 将 src 数组中大于 25 的元素复制到 dst 数组中相应的位置
np.copyto(dst, src, where=condition)
print(dst)  # Output: [ 1  2  3 40 50]
```
2. **使用不同的数据类型转换规则**
```python
import numpy as np

dst = np.array([1, 2, 3, 4, 5], dtype=np.uint8)
src = np.array([10, 20, 30, 40, 50], dtype=np.int32)

# 将 src 数组的值复制到 dst 数组中，进行数据类型转换
np.copyto(dst, src, casting='unsafe')
print(dst)  # Output: [10 20 30 40 50]
```