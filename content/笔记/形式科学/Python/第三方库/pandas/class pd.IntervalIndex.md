##### IntervalIndex 类
- 用于表示基于区间的索引
- [[IntervalIndex.创建]]
- IntervalIndex 属性
- IntervalIndex 方法
```python
import pandas as pd

# 创建包含区间数据的 DataFrame
data = {'Values': [10, 20, 30], 
		'Intervals': pd.IntervalIndex.from_tuples([(0, 5), (5, 10), (10, 15)], closed='both')}
		
df = pd.DataFrame(data, index=data['Intervals'])

#           Values Intervals
# [0, 5]        10    [0, 5]
# [5, 10]       20   [5, 10]
# [10, 15]      30  [10, 15]


```