##### `numpy.interp(x, xp, fp, left=None, right=None, period=None)`
**功能简介：**
- 用于在一维数组中执行线性插值。它基于已知的数据点 (`xp` 和 `fp`)，在给定的插值点 (`x`) 处计算插值结果。

**参数说明：**
- `x`：插值点的一维数组。
- `xp`：已知数据点的一维数组，通常表示自变量。
- `fp`：已知数据点对应的函数值的一维数组，通常表示因变量。
- `left`：可选的左边界外插值值（当 `x < xp[0]` 时）。
- `right`：可选的右边界外插值值（当 `x > xp[-1]` 时）。
- `period`：可选的周期，如果数据在周期上连续，则应提供周期长度。

**返回值：**
- 返回一个一维数组，其中包含插值结果。

**两个用法实例：**
1. **一维数组的线性插值**
```python
import numpy as np

xp = np.array([1, 2, 3, 4])
fp = np.array([4, 7, 1, 9])
x = np.array([1.5, 2.5, 3.5])
interp_result = np.interp(x, xp, fp)
print(interp_result)  # Output: [5.5 4.  5. ]
```

2. **使用边界外插值值**
```python
import numpy as np

xp = np.array([1, 2, 3, 4])
fp = np.array([4, 7, 1, 9])
x = np.array([0.5, 4.5])
interp_result = np.interp(x, xp, fp, left=0, right=10)
print(interp_result)  # Output: [ 0. 10.]
```

