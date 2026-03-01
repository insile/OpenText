##### numpy.ma 掩码数组创建转换
```python
ma.array(data, dtype=None, copy=False, order=None, mask=False, fill_value=None, keep_mask=True, hard_mask=False, shrink=True, subok=True, ndmin=0)
	# 创建一个带有掩码的数组（Masked Array），其中数组中的某些元素可以被标记为无效或缺失，并用特定的掩码值进行标记

ma.masked_where(condition, a[, copy])
	# 掩码数组中满足条件的值

ma.filled(a[, fill_value])
	# 以普通数组形式返回输入，用填充值替换被屏蔽的数据
	# 掩码数组对象具有同名方法 masked_array.filled()
```
