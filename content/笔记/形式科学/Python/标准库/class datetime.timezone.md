##### class datetime.timezone 与UTC固定时差的时区
- 实例化方法
```python
class datetime.timezone(offset, name=None)
	# offset 参数必须指定为一个 timedelta 对象，表示本地时间与 UTC 的时差。它必须严格限制于-timedelta(hours=24)和timedelta(hours=24) 之间，否则会引发 ValueError。
	# name 参数是可选的。 如果指定则必须为一个字符串，它将被用作datetime.tzname() 方法的返回值。
```
- 类属性
```python
timezone.utc  # UTC 时区，timezone(timedelta(0)) UTC+0
```
- 实例方法
```python
timezone.utcoffset(dt)  # 返回当 timezone 实例被构造时指定的固定值, 时区偏移量
timezone.tzname(dt)  # 返回当 timezone 实例被构造时指定的固定值, 时区名称
timezone.dst(dt)  # 夏令时偏移量总是返回 None
```
##### 说明
- Python 标准库中的 `datetime.timezone` 对象是用来表示固定偏移量的时区，而无法表示具体的地理时区（例如东八区）。因此，使用 `datetime.timezone` 对象来表示东八区时区是不准确的。如果你想要表示具体的地理时区，可以使用第三方库 `pytz`，它提供了更丰富的时区信息和支持