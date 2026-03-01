##### class pd.Series
- `pandas.Series` 是 Pandas 库中的一个核心数据结构，用于表示一维标签化数据。`Series` 可以看作是由一维数组（包含数据）和与之相关联的标签（包含索引）组成的数据结构。每个元素都有一个唯一的标签，可以通过标签进行访问和操作。
- [[Series.创建]]
- [[Series.属性]]
- [[Series.索引与切片]]
- [[pandas.方法|Series.方法]]
```python
data = {'New York': 8623000, 
		'Los Angeles': 3990456, 
		'Chicago': 2716000, 
		'Houston': 2328000}
population_series = pd.Series(data, name='Population')
# data为字典时，键可用于索引

print(population_series)
# New York       8623000
# Los Angeles    3990456
# Chicago        2716000
# Houston        2328000
# Name: Population, dtype: int64

population_series.index
# 行索引
# Index(['New York', 'Los Angeles', 'Chicago', 'Houston'], dtype='object')
```