##### numpy.linalg 范数, 行列式, 迹
```python
linalg.norm(x, ord=None, axis=None, keepdims=False)
	# 矩阵或向量范数
	=====  ============================  ==========================
	ord    norm for matrices             norm for vectors
	=====  ============================  ==========================
	None   Frobenius norm                2-norm
	'fro'  Frobenius norm                --
	'nuc'  nuclear norm                  --
	inf    max(sum(abs(x), axis=1))      max(abs(x))
	-inf   min(sum(abs(x), axis=1))      min(abs(x))
	0      --                            sum(x != 0)
	1      max(sum(abs(x), axis=0))      as below
	-1     min(sum(abs(x), axis=0))      as below
	2      2-norm (largest sing. value)  as below
	-2     smallest singular value       as below
	other  --                            sum(abs(x)**ord)**(1./ord)
	=====  ============================  ==========================

linalg.det(a)
	# 计算数组的行列式。

np.trace(a[, offset, axis1, axis2, dtype, out])
	# 迹 沿数组的对角线返回和。

linalg.matrix_rank(A[, tol, hermitian])
	# 用奇异值分解方法求阵列的矩阵秩



```
