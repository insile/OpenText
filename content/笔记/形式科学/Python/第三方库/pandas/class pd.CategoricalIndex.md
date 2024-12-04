##### CategoricalIndex 类
- 用于表示基于分类数据的索引
- [[CategoricalIndex.创建]]
- CategoricalIndex 属性
- CategoricalIndex 方法
```python
import pandas as pd

# 创建包含分类数据的 DataFrame
data = {'Column_A': [1, 2, 3], 
		'Column_B': ['A', 'B', 'C']}
df = pd.DataFrame(data, index=pd.Categorical(['X', 'Y', 'Z']))

#    Column_A Column_B
# X         1        A
# Y         2        B
# Z         3        C
```

