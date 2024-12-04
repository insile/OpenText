##### datetime.UTC格式
- `fromisoformat()`
	- ISO字符串转时间
	- 类方法：`time`，`date`，`datetime`
- `isoformat()`
	- 时间转ISO字符串
	- 实例方法：`time`，`date`，`datetime`
##### ISO 8601 格式的时间字符串
- ISO 8601 是国际标准化组织（ISO）制定的日期和时间表示法标准，它的格式包括了日期、时间和时区信息。ISO 8601 格式的时间字符串具有以下常见的形式：
- **日期部分：** `YYYY-MM-DD`，表示年份、月份和日期。
- **时间部分：** `HH:MM:SS.ssssss`，表示小时、分钟、秒和微秒。
- **时区部分：** `Z`（表示 UTC）或 `±hh:mm`（表示偏移时区，例如 `+08:00` 表示东八区）。
- 下面是一些示例，展示了不同 ISO 8601 格式的时间字符串：
	- 只包含日期部分：`2023-08-06`
	- 只包含时间部分：`12:30:45.500000`
	- 包含日期和时间部分，但不包含时区：`2023-08-06T12:30:45.500000`
	- 包含日期、时间和偏移时区：`2023-08-06T12:30:45.500000+08:00`
	- 包含日期、时间和 UTC 时区：`2023-08-06T12:30:45.500000Z`
```python
import datetime

# 将日期时间对象格式化为 ISO 8601 格式的时间字符串
now = datetime.datetime.now()
iso_format_str = now.isoformat()
print("ISO 8601 Format:", iso_format_str)
# ISO 8601 Format: 2023-08-09T00:24:25.116662

# 将 ISO 8601 格式的时间字符串解析为日期时间对象
iso_string = "2023-08-06T12:30:45.500000"
parsed_datetime = datetime.datetime.fromisoformat(iso_string)
print("Parsed Datetime:", parsed_datetime)
# Parsed Datetime: 2023-08-06 12:30:45.500000

```