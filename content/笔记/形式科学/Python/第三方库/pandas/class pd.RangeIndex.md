##### RangeIndex 类
- 用于表示默认的整数索引
- [[RangeIndex.创建]]
- RangeIndex 属性
- RangeIndex 方法
```python
import pandas as pd

# 创建一个 DataFrame，并使用定制的 RangeIndex 作为行索引
df = pd.DataFrame({'Column_A': [1, 2, 3], 
				   'Column_B': ['A', 'B', 'C']}, 
				   index=pd.RangeIndex(start=10, stop=13))
#     Column_A Column_B
# 10         1        A
# 11         2        B
# 12         3        C

```