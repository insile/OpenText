##### DatetimeIndex 类
- 用于表示日期时间的索引
- [[DatetimeIndex.创建]]
- DatetimeIndex 属性
- DatetimeIndex 方法
```python
import pandas as pd

# 创建包含日期时间数据的 DataFrame
data = {'Values': [10, 20, 30]}

df = pd.DataFrame(data, 
				  index=pd.to_datetime(['2022-01-01', '2022-02-01', '2022-03-01']))


#             Values
# 2022-01-01      10
# 2022-02-01      20
# 2022-03-01      30
```