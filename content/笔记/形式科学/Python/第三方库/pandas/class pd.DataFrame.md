##### class pd.DataFrame
- `pandas.DataFrame` 是 Pandas 库中的一个核心数据结构，用于表示二维标签化数据表格。`DataFrame` 可以看作是由行和列组成的二维表格，每一列可以是不同的数据类型，而且每一行都有一个唯一的标签。
- [[DataFrame.创建]]
- [[DataFrame.属性]]
- [[DataFrame.索引与切片]]
- [[pandas.方法|DataFrame.方法]]
```python
data = {'one': pd.Series([1,2,3], index=['a','b','c']), 
		'two': pd.Series([1,2,3,4], index=['a','b','c','d'])}
df = pd.DataFrame(data)

print(df)
#	   one  two
#	a  1.0    1
#	b  2.0    2
#	c  3.0    3
#	d  NaN    4

df.index
# Index(['a', 'b', 'c', 'd'], dtype='object') 自定义索引
df.columns
# Index(['one', 'two'], dtype='object') 自定义索引
```
