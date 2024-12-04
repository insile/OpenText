##### numpy 其他数学功能
- [[np.clip()]]  将区间外的值剪切到区间边缘
- [[np.interp()]]  一维数组线性插值
```python
np.convolve(a, v[, mode])
	# 返回两个一维序列的离散线性卷积
np.absolute(x, /[, out, where, casting, order, ...])
	# 绝对值 [ufunc]
np.fabs(x, /[, out, where, casting, order, ...])
	# 绝对值 [ufunc]
np.sign(x, /[, out, where, casting, order, ...])
	# 符号指示，正1负-1 [ufunc]
np.nan_to_num(x[, copy, nan, posinf, neginf])
	# 将 NaN 替换为零，将正无穷替换为大的有限数（默认行为），或使用用户使用 nan、posinf 和/或 neginf 关键字定义的数字进行替换。
np.heaviside(x1, x2, /[, out, where, casting, ...])
	# 计算海维赛德阶跃函数 [ufunc]
```

