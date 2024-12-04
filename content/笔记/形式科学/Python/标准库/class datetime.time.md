##### class datetime.time 时间
- 实例化方法
```python
class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)  
	# 所有参数都是可选的
	# tzinfo 可以是 None，或者是一个 tzinfo 子类的实例
	# 0 <= hour < 24
	# 0 <= minute < 60
	# 0 <= second < 60
	# 0 <= microsecond < 1000000
	# fold in [0, 1]
time.fromisoformat(time_string) # 返回ISO 8601格式的时间字符串对应的时间
```
- 类属性
```python
time.min # 最小的时间，time(0, 0, 0, 0)
time.max # 最大的时间，time(23, 59, 59, 999999)
time.resolution # 两个时间对象的最小间隔，timedelta(microseconds=1)
```
- 实例属性（只读）
```python
time.hour  # 取值范围是 range(24)
time.minute  # 取值范围是 range(60)
time.second  # 取值范围是 range(60)。
time.microsecond  # 取值范围是 range(1000000)。
time.tzinfo  # 作为 tzinfo 参数被传给 time 构造器的对象，如果没有传入值则为 None。
time.fold  # 取值范围是 [0, 1]。 用于在重复的时间段中消除边界时间歧义。 （当夏令时结束时回拨时钟或由于政治原因导致当明时区的 UTC 时差减少就会出现重复的时间段。） 取值 0 (1) 表示两个时刻早于（晚于）所代表的同一边界时间。
```
- 实例方法
```python
time1 < time2 # time1 在 time2 之前，则True

time.replace(hour=self.hour, minute=self.minute, 
			 second=self.second, microsecond=self.microsecond, 
			 tzinfo=self.tzinfo, *, fold=0)
	# 复制 time 实例，可通过关键字参数修改属性值
	# 可以通过指定 tzinfo=None 实现感知型转简单型 time
time.isoformat(timespec='auto') 
	# 返回 ISO 8601 格式的时间字符串
time.strftime(format)  
	# 返回时间格式化字符串

# 时区
time.tzname()  # 感知型返回 self.tzinfo.tzname(None) 时区名称
time.utcoffset()  # 感知型返回 self.tzinfo.utcoffset(None) 时区偏移量
time.dst()  # 感知型返回 self.tzinfo.dst(None) 夏令时偏移量

```