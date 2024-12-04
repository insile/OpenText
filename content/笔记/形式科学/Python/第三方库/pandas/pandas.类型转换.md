##### Series 转换
- [[Series.astype()]]  数据类型转换
```python
Series.convert_dtypes([infer_objects, ...])
	# 自动转换最佳数据类型
Series.copy(deep=True)
	# 拷贝

Series.bool()
	# 转布尔类型
Series.to_numpy([dtype, copy, na_value])
	# 转ndarray
Series.to_list()
	# 转列表
Series.to_period([freq, copy])
	# DatetimeIndex 转 PeriodIndex.
Series.to_timestamp([freq, how, copy])
	# PeriodIndex 转 DatetimeIndex
```
##### DataFrame 转换
- [[DataFrame.astype()]]  类型转换