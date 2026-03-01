##### class datetime.datetime 日期时间
- 实例化方法
```python
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)  # 构造方法
	# year, month 和 day 参数是必须的
	# tzinfo 可以是 None 或者是一个 tzinfo 子类的实例
	# MINYEAR <= year <= MAXYEAR,
	# 1 <= month <= 12,
	# 1 <= day <= 指定年月的天数,
	# 0 <= hour < 24,
	# 0 <= minute < 60,
	# 0 <= second < 60,
	# 0 <= microsecond < 1000000,
	# fold in [0, 1].
datetime.today()  # 当前地方日期时间，没有时区
datetime.utcnow()  # UTC日期时间，没有时区
datetime.now(tz=None)  # 指定时区的日期时间，没有时区等于datetime.today()
datetime.fromtimestamp(timestamp, tz=None)  # 返回指定时区时间戳对应的日期时间
datetime.utcfromtimestamp(timestamp) # 返回UTC时间戳对应的日期时间
datetime.combine(date, time, tzinfo=self.tzinfo)  # 结合date time tzinfo为日期时间
datetime.fromisoformat(date_string)  # 返回ISO 8601格式的日期时间字符串对应的日期时间
datetime.strptime(date_string, format) # 返回一个格式字符串对应的日期时间
```
- 类属性
```python
datetime.min  # 最早的可表示 datetime，datetime(1, 1, 1, tzinfo=None)。
datetime.max  # 最晚的可表示 datetime，datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=None)。
datetime.resolution # 两个不相等的 datetime 对象之间可能的最小间隔，timedelta(microseconds=1)
```
- 实例属性（只读）
```python
datetime.year # 在 MINYEAR 和 MAXYEAR 之间，包含边界。
datetime.month # 1 至 12（含）
datetime.day # 返回1到指定年月的天数间的数字。
datetime.hour  # 取值范围是 range(24)
datetime.minute  # 取值范围是 range(60)
datetime.second  # 取值范围是 range(60)。
datetime.microsecond  # 取值范围是 range(1000000)。
datetime.tzinfo  # 作为 tzinfo 参数被传给 time 构造器的对象，如果没有传入值则为 None。
datetime.fold  # 取值范围是 [0, 1]。 用于在重复的时间段中消除边界时间歧义。 （当夏令时结束时回拨时钟或由于政治原因导致当明时区的 UTC 时差减少就会出现重复的时间段。） 取值 0 (1) 表示两个时刻早于（晚于）所代表的同一边界时间。
```
- 实例方法
```python
datetime2 = datetime1 + timedelta  # datetime2 为 datetime1 后 timedelta 时间
datetime2 = datetime1 - timedelta  # datetime2 为 datetime1 前 timedelta 时间
timedelta = datetime1 - datetime2  # 间隔 timedelta 时间
datetime1 < datetime2 # datetime1 在 datetime2 之前，则True

datetime.date()  # 返回具有同样 year, month 和 day 值的 date 对象。
datetime.time()  # 返回具有同样 hour, minute, second, microsecond 和 fold 值的 time 对象。 tzinfo 值为 None
datetime.timetz()  # 返回具有同样 hour, minute, second, microsecond, fold 和 tzinfo 属性性的 time 对象
datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0) # 复制 datetime 实例，可通过关键字参数修改属性值

datetime.utcoffset()  # 时区偏移量
datetime.dst()  # 夏令时偏移量
datetime.tzname()  # 时区名称

datetime.timetuple()  # 返回一个time.struct_time
datetime.toordinal()  # 返回日期对应的格列高利历序号
datetime.timestamp()  # 时间戳
datetime.weekday()  # 返回整数，星期一为0，星期天为6
datetime.isoweekday()  # 返回整数，星期一为1，星期天为7
datetime.isocalendar()  # 返回tuple，(year, week, weekday)

datetime.isoformat(sep='T', timespec='auto')  # 返回一个以 ISO 8601 格式表示的日期和时间字符串
datetime.strftime(format)  # 返回格式化日期字符串

```