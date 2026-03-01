##### Timestamp 类
- 表示支持时区的日期时间，datetime.datetime 的替换
- [[Timestamp.创建]]
- Timestamp 属性
- Timestamp 方法
- [[Series.dt]]
```python
import pandas as pd

# 创建一个包含时间戳的 DataFrame
data = {'Event': ['Event_A', 'Event_B', 'Event_C'],
        'Timestamp': ['2022-03-08 12:00:00', '2022-03-09 15:30:00', '2022-03-10 09:45:00']}
df = pd.DataFrame(data)

# 将时间戳字符串转换为 pd.Timestamp 对象
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# 打印 DataFrame
print(df)

# 提取年份
df['Year'] = df['Timestamp'].dt.year

# 提取月份
df['Month'] = df['Timestamp'].dt.month

# 计算时间差
df['TimeDifference'] = df['Timestamp'].diff()

# 打印更新后的 DataFrame
print(df)


# 时区
ts = pd.Timestamp("2016-01-01", tz="UTC")
type(ts.tzinfo)
# datetime.timezone

# 东八区转UTC
ts = pd.Timestamp("2016-01-01", tz=datetime.timezone(datetime.timedelta(hours=8)))
# Timestamp('2016-01-01 00:00:00+0800', tz='UTC+08:00')
ts.tz_convert('UTC')
# Timestamp('2015-12-31 16:00:00+0000', tz='UTC')

# 北京时间转UTC
ts = pd.Timestamp("2016-01-01", tz='Asia/Shanghai')
# Timestamp('2016-01-01 00:00:00+0800', tz='Asia/Shanghai')
ts.tz_convert('UTC')
# Timestamp('2015-12-31 16:00:00+0000', tz='UTC')

```