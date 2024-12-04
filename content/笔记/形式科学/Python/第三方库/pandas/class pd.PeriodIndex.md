##### PeriodIndex 类
- 用于表示周期（时间段）的索引
- [[PeriodIndex.创建]]
- PeriodIndex 属性
- PeriodIndex 方法
```python
import pandas as pd

# 创建包含周期数据的 DataFrame
data = {'Values': [10, 20, 30]}
df = pd.DataFrame(data, index=pd.period_range(start='2022-01', periods=3, freq='M'))

#          Values
# 2022-01      10
# 2022-02      20
# 2022-03      30
```