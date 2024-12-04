##### Categorical 类
- 代表分类变量
- [[Categorical.创建]]
- Categorical 属性
- Categorical 方法
- [[Series.cat]]
```python
import pandas as pd

# 创建包含分类数据的 DataFrame
data = {'Event': ['Event_A', 'Event_B', 'Event_C', 'Event_A'],
        'Category': pd.Categorical(['A', 'B', 'C', 'A'])}
df = pd.DataFrame(data)

# 打印 DataFrame
print(df)


df.Category.unique()

# 获取分类的唯一值
df.Category.unique()

# 获取分类的频率统计
df.Category.value_counts()

# 将分类转换为 codes（整数编码）
df.Category.cat.codes
```