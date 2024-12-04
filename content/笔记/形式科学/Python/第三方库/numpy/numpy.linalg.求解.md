##### numpy.linalg 求解
```python
linalg.solve(a, b)
	# 解一个线性矩阵方程，或线性标量方程组。
linalg.tensorsolve(a, b[, axes])
	# 用于求解张量方程 a x = b，其中 x 是待求解的张量。
linalg.lstsq(a, b[, rcond])
	# 计算线性矩阵方程的最小二乘解。
linalg.inv(a)
	# 计算矩阵的乘法逆。
linalg.pinv(a[, rcond, hermitian])
	# 计算矩阵的伪逆（Moore-Penrose 伪逆）。
linalg.tensorinv(a[, ind])
	# 计算 N 维数组的“逆”。
```