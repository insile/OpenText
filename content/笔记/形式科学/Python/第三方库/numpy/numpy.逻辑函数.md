##### 真值测试
```python
np.all(a, axis=None)
	# 测试沿给定轴的所有数组元素是否计算为 True。
np.any(a, axis=None)
	# 测试沿给定轴的任何数组元素的计算结果是否为 True。
```
##### 数组内容
```python
np.isfinite(x, /[, out, where, casting, order, ...])
	# 测试元素有限性(不是无穷大，也不是数字)。[ufunc]
np.isinf(x, /[, out, where, casting, order, ...])
	# 测试元素无穷大 [ufunc]
np.isnan(x, /[, out, where, casting, order, ...])
	# 测试元素不是数字 [ufunc]
np.isnat(x, /[, out, where, casting, order, ...])
	# 测试元素不是时间 [ufunc]
np.isneginf(x[, out])
	# 测试元素负无穷大 
np.isposinf(x[, out])
	# 测试元素正无穷大 
```
##### 数组类型
```python
np.iscomplex(x)
	# 检查一个数或数组元素是否是复数
np.iscomplexobj(x)
	# 检查对象是否具有复数类型
np.isfortran(a)
	# 检查数组是否以 Fortran（列优先）顺序存储在内存中
np.isreal(x)
	# 检查一个数或数组元素是否是实数
np.isrealobj(x)
	# 检查对象是否具有实数类型
np.isscalar(element)
	# 检查元素是否是标量
```
##### 逻辑运算
```python
np.logical_and(x1, x2, /[, out, where, …])	
	# 按元素计算x1和x2的真值。 [ufunc]
np.logical_or(x1, x2, /[, out, where, casting, …])	
	# 按元素计算x1或x2的真值。 [ufunc]
np.logical_not(x, /[, out, where, casting, …])	
	# 计算非x元素的真值。 [ufunc]
np.logical_xor(x1, x2, /[, out, where, …])	
	# 按元素计算x1 XOR x2的真值。 [ufunc]
```
##### 数组比较
```python
np.allclose(a, b[, rtol, atol, equal_nan])
	# 判断两个数组在一个公差内所有元素相等
np.isclose(a, b[, rtol, atol, equal_nan])
	# 判断两个数组在一个公差内按元素相等
np.array_equal(a1, a2[, equal_nan])
	# 判断两个数组具有相同的形状和元素
np.greater(x1, x2, /[, out, where, casting, ...])
	# x1 > x2 [ufunc]
np.greater_equal(x1, x2, /[, out, where, ...])
	# x1 >= x2 [ufunc]
np.less(x1, x2, /[, out, where, casting, ...])
	# x1 < x2 [ufunc]
np.less_equal(x1, x2, /[, out, where, casting, ...])
	# x1 <= x2 [ufunc]
np.equal(x1, x2, /[, out, where, casting, ...])
	# x1 == x2 [ufunc]
np.not_equal(x1, x2, /[, out, where, casting, ...])
	# x1 != x2 [ufunc]
```
