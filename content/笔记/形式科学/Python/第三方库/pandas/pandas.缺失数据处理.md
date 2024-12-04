##### Series 缺失数据处理
- [[Series.fillna()]]  填充缺失值
- [[Series.interpolate()]]  插值
```python
Series.dropna(*[, axis, inplace, how, ...])
	# 返回一个删除了缺失值的新 Series
Series.isna()
	# 检测缺失值
Series.notna()
	# 检测非缺失值。
Series.replace([to_replace, value, inplace, ...])
	# 用 value 替换 to_replace 中给出的值
```
##### DataFrame 缺失数据处理
- [[DataFrame.dropna()]]  删除缺失值
- [[DataFrame.fillna()]]  填充缺失值