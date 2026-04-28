##### TimedeltaIndex 类
- 用于表示时间间隔的索引
- [[TimedeltaIndex.创建]]
- TimedeltaIndex 属性
- TimedeltaIndex 方法
```python
import pandas as pd

# 创建包含时间间隔数据的 DataFrame
data = {'Values': [10, 20, 30]}
df = pd.DataFrame(data, index=pd.to_timedelta(['1 days', '2 days', '3 days']))

#         Values
# 1 days      10
# 2 days      20
# 3 days      30
```