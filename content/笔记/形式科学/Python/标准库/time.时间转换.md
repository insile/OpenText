##### time.时间转换
```python
import time

# 字符串 转 结构化时间对象
sttime1 = time.strptime('Tue Aug 08 21:36:07 2023') # 默认解析格式为 "%a %b %d %H:%M:%S %Y"
sttime2 = time.strptime('2023/08/01 21:00:00','%Y/%m/%d %H:%M:%S') # 自定义解析格式
print("sttime1:", sttime1)
print("sttime2:", sttime2)

# 结构化时间对象 转 字符串
custom_format = time.strftime("%Y-%m-%d %I:%M %p", time.localtime())
print("Custom Format:", custom_format)

# 结构化时间对象
current_time_struct = time.localtime() # 获取当前时间的 struct_time

# 打印 struct_time 属性
print(f"Year: {current_time_struct.tm_year}")
print(f"Month: {current_time_struct.tm_mon}")
print(f"Day: {current_time_struct.tm_mday}")
print(f"Hour: {current_time_struct.tm_hour}")
print(f"Minute: {current_time_struct.tm_min}")
print(f"Second: {current_time_struct.tm_sec}")
print(f"Weekday: {current_time_struct.tm_wday}")
print(f"Day of the Year: {current_time_struct.tm_yday}")
print(f"Is Daylight Saving Time: {current_time_struct.tm_isdst}")
```