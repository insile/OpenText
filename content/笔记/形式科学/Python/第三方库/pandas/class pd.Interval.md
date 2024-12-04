##### Interval 类
- 代表一个区间
- [[Interval.创建]]
- Interval 属性
- Interval 方法
```python
import pandas as pd

# 创建包含区间的 DataFrame
data = {'Event': ['Event_A', 'Event_B', 'Event_C'],
        'Interval': [pd.Interval(0, 5, closed='both'), pd.Interval(5, 10, closed='right'), pd.Interval(10, 15, closed='both')]}
df = pd.DataFrame(data)

# 打印 DataFrame
print(df)

```