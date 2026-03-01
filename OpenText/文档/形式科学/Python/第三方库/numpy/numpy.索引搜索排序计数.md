##### numpy 搜索
- [[np.where()]]  根据条件返回元素
- [[np.extract()]] 一维数组形式, 返回满足某些条件的元素。
- [[np.select()]]  根据条件选择值
```python
np.argmax(a[, axis, out, keepdims])
	# 返回沿轴的最大值的索引
np.nanargmax(a[, axis, out, keepdims])
	# 返回指定轴上最大值的索引，忽略 NaN 值。
np.argmin(a[, axis, out, keepdims])
	# 返回沿轴的最小值的索引。
np.nanargmin(a[, axis, out, keepdims])
	# 返回指定轴上最小值的索引，忽略 NaN 值。
np.argwhere(a)
	# 找到数组元素中非零的索引，按元素分组。
np.nonzero(a)
	# 返回非零元素的索引
np.flatnonzero(a)
	# 返回扁平化版本中非零的索引
np.searchsorted(a, v[, side, sorter])
	# 查找应插入元素以维持顺序的索引。
```
##### numpy 排序
```python
np.sort(a[, axis, kind, order])
	# 返回数组的排序副本。

np.lexsort(keys[, axis])
	# 使用一系列键执行间接稳定排序。

np.argsort(a[, axis, kind, order])
	# 返回将数组排序的索引。

np.sort_complex(a)
	# 首先按实部排序，然后按虚部排序的方式对复数数组进行排序。

np.partition(a, kth[, axis, kind, order])
	# 返回数组的分区副本。

np.argpartition(a, kth[, axis, kind, order])
	# 使用指定的算法沿给定轴执行间接分区。
```
