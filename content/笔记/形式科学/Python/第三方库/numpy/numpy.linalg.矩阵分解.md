##### numpy.linalg 矩阵分解
```python
linalg.cholesky(a)
	# Cholesky 分解，用于将一个正定的 Hermitian 矩阵分解为一个下三角矩阵和其共轭转置的乘积。

linalg.qr(a[, mode])
	# 计算矩阵的 QR 分解，将矩阵分解为一个正交矩阵乘以一个上三角矩阵。

linalg.svd(a[, full_matrices, compute_uv, ...])
	# 奇异值分解（Singular Value Decomposition，SVD），将一个矩阵分解为三个矩阵的乘积，包括一个左奇异向量矩阵、一个对角奇异值矩阵和一个右奇异向量矩阵的共轭转置。
```