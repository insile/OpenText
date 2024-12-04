##### numpy 函数式编程
```python
np.apply_along_axis(func1d, axis, arr, *args, ...)
	# 将函数应用于沿给定轴的1-D 切片。

np.apply_over_axes(func, a, axes)
	# 在多个轴上重复应用一个函数。

np.vectorize([pyfunc, otypes, doc, excluded, ...])
	# 返回一个类似 pyfunc 但以数组作为输入的对象。

np.frompyfunc(func, /, nin, nout, *[, identity])
	# 接受任意的 Python 函数并返回 NumPy ufunc。

np.piecewise(x, condlist, funclist, *args, **kw)
	# 计算分段定义的函数。
```