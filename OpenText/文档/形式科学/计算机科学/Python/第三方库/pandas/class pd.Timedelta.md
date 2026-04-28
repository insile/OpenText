##### timedelta 类
- 表示时间差，datetime.timedelta 的替换
- [[Timedelta.创建]]
- Timedelta 属性
- Timedelta 方法
- [[Series.dt]]
```python
import pandas as pd

# 创建一个包含时间间隔的 DataFrame
data = {'Event': ['Event_A', 'Event_B', 'Event_C'],
        'Duration': [pd.Timedelta(days=1), pd.Timedelta(hours=3), pd.Timedelta(minutes=30)]}
df = pd.DataFrame(data)

# 增加时间间隔
df['End_Time'] = pd.Timestamp('2022-03-08 12:00:00') + df['Duration']

# 打印更新后的 DataFrame
print(df)

```