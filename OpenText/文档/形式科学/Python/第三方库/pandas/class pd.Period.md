##### Period 类
- 代表一段时间
- [[Period.创建]]
- Period 属性
- Period 方法
- [[Series.dt]]
```python
import pandas as pd

# 创建包含时期的 DataFrame
data = {'Event': ['Event_A', 'Event_B', 'Event_C'],
        'Period': [pd.Period('2022-03', freq='M'), pd.Period('2022-04', freq='M'), pd.Period('2022-05', freq='M')]}
df = pd.DataFrame(data)

# 打印 DataFrame
print(df)
```