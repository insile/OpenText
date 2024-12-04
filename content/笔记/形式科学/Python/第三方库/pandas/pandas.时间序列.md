##### Series 时间序列
- [[Series.asfreq()]]  将时间序列转换为指定频率
- [[Series.shift()]]  平移时间索引
- [[Series.resample()]]  重采样 [[class pd.Resampler|返回Resampler对象]]
```python
Series.tz_convert(tz[, axis, level, copy])
	# 切换时区
Series.tz_localize(tz[, axis, level, copy, ...])
	# 将 Series 或 DataFrame 的 tz 初始索引本地化为目标时区。
Series.at_time(time[, asof, axis])
	# 在一天中的特定时间选择值(例如，上午9:30)。
Series.between_time(start_time, end_time[, ...])
	# 选择一天中特定时间之间的值(例如，上午9:00-9:30)。
```