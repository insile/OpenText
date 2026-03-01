##### np.select(condlist, choicelist, default=0)
**功能简介：**
- 根据一组条件列表和对应的选择列表，在每个条件成立时从选择列表中选择值，最终返回一个由这些选择值构成的数组。

**参数说明：**
- `condlist`：条件列表，包含布尔数组或布尔表达式。
- `choicelist`：选择列表，包含与条件列表相对应的值，可以是数组或标量。
- `default`：可选参数，用于指定默认值，当所有条件都不成立时使用。

**返回值：**
- 返回一个数组，其中的每个元素由条件列表中的第一个成立的条件所对应的选择值给出。如果没有条件成立并且提供了默认值，则使用默认值。

**用法示例：**
```python
import numpy as np

condlist = [np.array([True, False, True, False]),
            np.array([False, True, False, True])]
choicelist = [np.array([1, 2, 3, 4]),
              np.array([5, 6, 7, 8])]

result = np.select(condlist, choicelist, default=-1)
print(result)  # Output: [1 6 3 8]

x = np.arange(6)
condlist = [x<3, x>3]
choicelist = [x, x**2]
result2 = np.select(condlist, choicelist, 42)
print(result2)
# array([ 0,  1,  2, 42, 16, 25])
```


