##### time 库
- 提供了各种与时间相关的函数
- [[time.时间转换]]
```python
import time
```
##### time 主要API
- [[class time.struct_time]] 结构化时间类
```python
time.time()  # 获取当前时间戳，浮点数
time.ctime()  # 易读时间，字符串
time.perf_counter() # 调用两次，获取差值测量时间，单位秒，浮点数
time.sleep(s)  # 让程序暂停指定秒数
time.strftime(format, struct_time)  # 结构化时间 转 字符串

# format 规则
# 年份 %Y(2023) %y(23)
# 月份 %m(08) %B(August) %b(Aug)
# 日数 %d(01)
# 星期 %A(Tuesday) %a(Tue) %w(0-6 周日-周六)
# 小时 %H(24) %I(12)
# 分钟 %M(59)
# 秒 %S(59)
# 上下午 %p(AM&PM) 
```