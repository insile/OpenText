##### numpy.三角函数
```python
np.sin(x, /[, out, where, casting, order, ...])
	# 计算给定角度的正弦值 [ufunc]
np.cos(x, /[, out, where, casting, order, ...])
	# 计算给定角度的余弦值 [ufunc]
np.tan(x, /[, out, where, casting, order, ...])
	# 计算给定角度的正切值 [ufunc]
np.arcsin(x, /[, out, where, casting, order, ...])
	# 计算给定正弦值的反正弦值 [ufunc]
np.arccos(x, /[, out, where, casting, order, ...])
	# 计算给定余弦值的反余弦值 [ufunc]
np.arctan(x, /[, out, where, casting, order, ...])
	# 计算给定正切值的反正切值 [ufunc]

np.hypot(x1, x2, /[, out, where, casting, ...])
	# 计算给定两个边长的直角三角形的斜边长度（欧几里得范数） [ufunc]
np.arctan2(x1, x2, /[, out, where, casting, ...])
	# 计算 x1 与 x2 的元素级别的反正切值，根据它们的符号和象限来选择合适的结果 [ufunc]
np.degrees(x, /[, out, where, casting, order, ...])
	# 将弧度转换为角度 [ufunc]
np.radians(x, /[, out, where, casting, order, ...])
	# 将角度转换为弧度 [ufunc]
np.unwrap(p[, discont, axis, period])
	# 通过计算与周期相关的差值来取消相位的不连续性。
np.deg2rad(x, /[, out, where, casting, order, ...])
	# 将角度从度数转换为弧度 [ufunc]
np.rad2deg(x, /[, out, where, casting, order, ...])
	# 将角度从弧度转换为度数 [ufunc]
```