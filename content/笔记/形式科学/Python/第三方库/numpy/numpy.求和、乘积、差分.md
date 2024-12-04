##### numpy 求和、乘积、差分
- [[np.diff()]]  用于计算数组在给定轴上的差分
- [[np.ediff1d()]]  计算数组中相邻元素之间的差异
- [[np.gradient()]]  计算 N 维数组的梯度
- [[np.trapz()]]  使用复合梯形公式沿给定轴线积分
```python
np.prod(a[, axis, dtype, out, keepdims, ...])
	# 计算数组元素沿指定轴的乘积
np.sum(a[, axis, dtype, out, keepdims, ...])
	# 计算数组元素沿指定轴的和
np.nanprod(a[, axis, dtype, out, keepdims, ...])
	# 计算数组元素沿指定轴的乘积，将 NaN 视为 1 进行计算
np.nansum(a[, axis, dtype, out, keepdims, ...])
	# 计算数组元素沿指定轴的和，将 NaN 视为 0 进行计算
np.cumprod(a[, axis, dtype, out])
	# 计算数组元素沿指定轴的累积乘积
np.cumsum(a[, axis, dtype, out])
	# 计算数组元素沿指定轴的累积和
np.nancumprod(a[, axis, dtype, out])
	# 计算数组元素沿指定轴的累积乘积，将 NaN 视为 1 进行计算
np.nancumsum(a[, axis, dtype, out])
	# 计算数组元素沿指定轴的累积和，将 NaN 视为 0 进行计算

np.cross(a, b[, axisa, axisb, axisc, axis])
	# 计算两个向量的叉积
```