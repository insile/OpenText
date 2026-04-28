##### ndarray.方法
```python
ndarray.reshape(shape) 
	# 不改变元素，返回shape形状数组，原数组不变
ndarray.resize(shape) 
	# 同reshape，但改变原数组
ndarray.swapxes(ax1, ax2) 
	# 将数组n维度中两个维度调换
ndarray.flatten(order='C') 
	# 按指定顺序降成一维，原数组不变 (复制操作)
ndarray.astyle(new_type) 
	# 改变元素类型，并新创建数组
ndarray.tolist() 
	# 数组转列表
ndarray.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
	# 数组的副本，强制转换为指定类型

```