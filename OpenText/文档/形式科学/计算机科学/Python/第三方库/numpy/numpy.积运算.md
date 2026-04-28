##### numpy 积运算
```python
np.dot(a, b, out=None)
	# 一维数组, 就是内积 np.inner
	# 二维数组, 是矩阵乘法 np.matmul or a @ b
	# 常量, 标量积 np.multiply or a * b
np.matmul(a, b) / @
	# 二维数组, 矩阵乘法, 前行乘后列
np.vdot(a, b)
	# 一维数组, 点积
np.inner(a, b)
	# 一维数组的内积, sum(a * b)
	# 多维数组, np.tensordot(a, b, axes=(-1, -1))
	# 常量, 标量积 
np.cross(a, b)
	# 二维数组, 三维数组, 叉乘
	# 与a,b垂直的向量
np.outer(a, b)
	# 一维数组, 外积, 矩阵乘法, 前行乘后列
np.tensordot(a， b， 轴=2)
	# 沿指定轴计算张量点积
	# 轴int, a的后N个轴 和 b的前N个轴
	# 轴array_like, 第一个序列应用于a, 然后b
	# a = np.arange(60.).reshape(3,4,5)
	# b = np.arange(24.).reshape(4,3,2)
	# c = np.tensordot(a,b, axes=([1,0],[0,1]))
	# c.shape
	# (5, 2)
	#		d = np.zeros((5,2))
	#	for i in range(5):
	#	  for j in range(2):
	#	    for k in range(3):
	#	      for n in range(4):
	#	        d[i,j] += a[k,n,i] * b[n,k,j]
```