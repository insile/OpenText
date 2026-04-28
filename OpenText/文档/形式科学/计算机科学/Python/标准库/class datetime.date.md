##### class datetime.date 日期
- 实例化方法
```python
class datetime.date(year, month, day)  # 构造方法
	# 所有参数都是必要的
	# MINYEAR <= year <= MAXYEAR
	# 1 <= month <= 12
	# 1 <= day <= 给定年月对应的天数
date.today()  # 返回当前的本地日期
date.fromisoformat(date_string)  # 返回ISO 8601格式的日期字符串对应的日期
date.fromtimestamp(timestamp)  # 返回时间戳对应的日期
date.fromordinal(ordinal)  # 返回格列高利历序号对应的日期，其中公元1年1月1日的序号为1，
date.fromisocalendar(year, week, day)  #  返回ISO历法对应的日期
```
- 类属性
```python
date.min # 最小的日期，date(1, 1, 1)
date.max # 最大的日期，date(9999, 12, 31)
date.resolution # 两个日期对象的最小间隔，timedelta(days=1)
```
- 实例属性（只读）
```python
date.year # 在 MINYEAR 和 MAXYEAR 之间，包含边界。
date.month # 1 至 12（含）
date.day # 返回1到指定年月的天数间的数字。
```
- 实例方法
```python
date2 = date1 + timedelta  # date2 为 date1 后 timedelta.days 天
date2 = date1 - timedelta  # date2 为 date1 前 timedelta.days 天
timedelta = date1 - date2  # 间隔 timedelta.days 天
date1 < date2 # date1 在 date2 之前，则True

date.replace(year=self.year, month=self.month, day=self.day)  # 复制 date 实例，可通过关键字参数修改属性值
date.timetuple()  # 返回一个time.struct_time
date.toordinal()  # 返回日期对应的格列高利历序号
date.weekday()  # 返回整数，星期一为0，星期天为6
date.isoweekday()  # 返回整数，星期一为1，星期天为7
date.isocalendar()  # 返回tuple，(year, week, weekday)
date.isoformat()  # 返回iso字符串，'YYYY-MM-DD'
date.ctime()  # 返回字符串，'Tue May  3 00:00:00 2022'
date.strftime(format)  # 返回格式化日期字符串
```