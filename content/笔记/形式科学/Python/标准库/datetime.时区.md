##### datetime.时区
```python
import datetime

# UTC 转 UTC+8 
# UTC+8 比 UTC 快8小时
# 2021/1/15 00:00 -> 2021/1/15 08:00
utc_timezone = datetime.timezone.utc  # UTC+0
utc_datetime = datetime.datetime(2021, 1, 15, tzinfo=utc_timezone)
local_datetime = utc_datetime.astimezone(timezone(datetime.timedelta(hours=8)))  # 调整到特定时区

# UTC 转 UTC-8
# UTC-8 比 UTC 慢8小时
# 2021/1/15 00:00 -> 2021/1/14 16:00
utc_timezone = datetime.timezone.utc  # UTC+0
utc_datetime = datetime.datetime(2021, 1, 15, tzinfo=utc_timezone)
local_datetime = utc_datetime.astimezone(timezone(datetime.timedelta(hours=8)))  # 调整到特定时区
```

| 时区     | 时区范围            | 时区中心线 |
| ------ | --------------- | ----- |
| UTC    | 7.5°W~7.5°E     | 0°    |
| UTC+1  | 7.5°E~22.5°E    | 15°E  |
| UTC+2  | 22.5°E~37.5°E   | 30°E  |
| UTC+3  | 37.5°E~52.5°E   | 45°E  |
| UTC+4  | 52.5°E~67.5°E   | 60°E  |
| UTC+5  | 67.5°E~82.5°E   | 75°E  |
| UTC+6  | 82.5°E~97.5°E   | 90°E  |
| UTC+7  | 97.5°E~112.5°E  | 105°E |
| UTC+8  | 112.5°E~127.5°E | 120°E |
| UTC+9  | 127.5°E~142.5°E | 135°E |
| UTC+10 | 142.5°E~157.5°E | 150°E |
| UTC+11 | 157.5°E~172.5°E | 165°E |
| 东西十二区  | 172.5°E~172.5°W | 180°  |
| UTC-11 | 172.5°W~157.5°W | 165°W |
| UTC-10 | 157.5°W~142.5°W | 150°W |
| UTC-9  | 142.5°W~127.5°W | 135°W |
| UTC-8  | 127.5°W~112.5°W | 120°W |
| UTC-7  | 112.5°W~97.5°W  | 105°W |
| UTC-6  | 97.5°W~82.5°W   | 90°W  |
| UTC-5  | 82.5°W~67.5°W   | 75°W  |
| UTC-4  | 67.5°W~52.5°W   | 60°W  |
| UTC-3  | 52.5°W~37.5°W   | 45°W  |
| UTC-2  | 37.5°W~22.5°W   | 30°W  |
| UTC-1  | 22.5°W~7.5°W    | 15°W  |
