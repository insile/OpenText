##### datetime.自定义格式
- `strftime`
	- 根据给定的格式将对象转换为字符串
	- 实例方法：`date`; `datetime`; `time`
	- `strftime(format)`
- `strptime`
	- 将字符串解析为给定相应格式的 `datetime` 对象
	- 类方法：`datetime`
	- `strptime(date_string, format)`
```python
import datetime

# 将日期时间对象格式化为字符串
now = datetime.datetime.now()
formatted_str = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted_str)

# 将字符串解析为日期时间对象
date_str = "2023-08-06 12:30:45"
parsed_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed:", parsed_datetime)

# 模板
%c
	# 本地化的适当日期和时间表示。
	# Tue Aug 16 21:30:00 1988 (en_US);
%x
	# 本地化的适当日期表示。
	# 08/16/88 (None);
	# 08/16/1988 (en_US);
%X
	# 本地化的适当时间表示。
	# 21:30:00 (en_US);
# 年
%Y 
	# 十进制数表示的带世纪的年份。
	# 0001, 0002, ..., 2013, 2014, ..., 9998, 9999
%y
	# 补零后，以十进制数表示的，不带世纪的年份。
	# 00, 01, ..., 99
# 月
%B
	# January, February, ..., December
%b
	# Jan, Feb, ..., Dec
# 日
%d 
	# 01, 02, ..., 31
%w 
	# 0, 1, ..., 6
%a 
	# Sun, Mon, ..., Sat
%A 
	# Sunday, Monday, ..., Saturday
# 时
%p
	# 本地化的 AM 或 PM 。
	# AM, PM (en_US);
	# am, pm (de_DE)
%H
	# 以补零后的十进制数表示的小时（24 小时制）。
	# 00, 01, ..., 23
%I
	# 以补零后的十进制数表示的小时（12 小时制）。
	# 01, 02, ..., 12
# 分
%M
	# 00, 01, ..., 59
# 秒
%S
	# 00, 01, ..., 59
# 时区
%Z 
	# 时区名称（如果对象为简单型则为空字符串）UTC, GMT
%z 
	# UTC 偏移量，格式为 ±HHMM[SS[.ffffff]] （如果是简单型对象则为空字符串）
```