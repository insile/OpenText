##### datetime 库
- `datetime` 模块是 Python 中处理日期和时间的标准库之一。它提供了 `date`、`time`、`datetime`、`timedelta` 等类，以及丰富的方法来处理日期和时间
- [[datetime.自定义格式]]
- [[datetime.UTC格式]]
- [[datetime.时区]]
```python
import datetime
```
##### datetime 主要API
- [[class datetime.time]]  时间
- [[class datetime.date]] 日期
- [[class datetime.datetime]]  日期时间
- [[class datetime.timedelta]]  时间间隔
- [[class datetime.tzinfo]]  时区抽象基类
- [[class datetime.timezone]] 与UTC固定时差的时区
```python
# 继承关系
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime

# 感知型和简单型
# 感知型和简单型的区别在于是否包含时区信息
# date 对象都是简单型的
# time 或 datetime 对象可以是感知型或者简单型
# 感知型和简单型之间的区别不适用于 timedelta 对象
```