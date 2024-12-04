##### Series 二元操作及运算符
- [[Series.combine()]]  通过指定的函数对相同索引位置的元素进行合并
```python
series + other
Series.add(other[, level, fill_value, axis])
Series.radd(other[, level, fill_value, axis])  # other + series
	# 按索引相加

series - other
Series.sub(other[, level, fill_value, axis])
Series.rsub(other[, level, fill_value, axis])  # other - series
	# 按索引相减

series * other
Series.mul(other[, level, fill_value, axis])
Series.rmul(other[, level, fill_value, axis])  # other * series
	# 按索引相乘

series / other
Series.div(other[, level, fill_value, axis])
Series.rdiv(other[, level, fill_value, axis])  # other / series
Series.truediv(other[, level, fill_value, axis])
Series.rtruediv(other[, level, fill_value, axis])  # other / series
	# 按索引相除

series // other
Series.floordiv(other[, level, fill_value, axis])
Series.rfloordiv(other[, level, fill_value, ...])  # other // series
	# 按索引整除

series % other
Series.mod(other[, level, fill_value, axis])
Series.rmod(other[, level, fill_value, axis])  # other % series
	# 按索引模运算

series ** other
Series.pow(other[, level, fill_value, axis])
Series.rpow(other[, level, fill_value, axis])  # other ** series
	# 按索引幂运算

series < other
Series.lt(other[, level, fill_value, axis])
series > other
Series.gt(other[, level, fill_value, axis])
series <= other
Series.le(other[, level, fill_value, axis])
series >= other
Series.ge(other[, level, fill_value, axis])
series != other
Series.ne(other[, level, fill_value, axis])
series == other
Series.eq(other[, level, fill_value, axis])
	# 按索引对比值，返回布尔值
	
series @ other
Series.dot(other)
	# 点积


Series.round([decimals])
	# 四舍五入
Series.product([axis, skipna, numeric_only, ...])
	# 沿轴累乘
Series.combine_first(other)
	# 通过用来自另一个 Series 的非空值填充一个 Series 中的空值来组合两个 Series 对象
```