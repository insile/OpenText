##### class time.struct_time 结构化时间类
- `struct_time.实例化方法`
```python
time.gmtime()  # 当前 UTC 结构化时间，time.struct_time 对象
time.localtime()  # 当前 本地时区 结构化时间，time.struct_time 对象
time.strptime(string, format)  # 字符串 转 结构化时间，time.struct_time 对象
```
- `struct_time.实例属性`
```python
struct_time.tm_year
# 年份
struct_time.tm_mon
# 月份（1~12）
struct_time.tm_mday
# 日（1~31）
struct_time.tm_hour
# 小时（0~23）
struct_time.tm_min
# 分钟（0~59）
struct_time.tm_sec
# 秒（0~61，60和61用于闰秒）
struct_time.tm_wday
# 星期（0~6，0表示周一）
struct_time.tm_yday
# 年内的第几天（1~366）
struct_time.tm_isdst
# 是否为夏令时，值为正表示夏令时，0表示不是夏令时，负值表示夏令时信息不可用
```
