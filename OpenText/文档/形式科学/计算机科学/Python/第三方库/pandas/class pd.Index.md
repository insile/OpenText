##### class pd.Index
- `pandas.Index` 是 Pandas 库中的一个核心数据结构，用于表示轴标签的不可变序列。`Index` 可以被视为一维数组，其中的元素是唯一的标签，可以用于标识和访问数据中的行或列。
- [[Index.创建]]  自定义索引
- [[Index.属性]]
- [[Index.方法]]
```python
df = pd.DataFrame([['xiaowang',20], 
				   ['lily',30], 
				   ['anne', 40]])
# 	          0   1
#	0  xiaowang  20
#	1      lily  30
#	2      anne  40
df.index
# RangeIndex(start=0, stop=3, step=1) 默认行索引
df.columns
# RangeIndex(start=0, stop=2, step=1) 默认列索引

df = pd.DataFrame({'one': pd.Series([1,2,3], index=['a','b','c']), 'two': pd.Series([1,2,3,4], index=['a','b','c','d'])})
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
##### pandas.Index 子类
- [[class pd.RangeIndex]]  数字索引，默认索引
- [[class pd.CategoricalIndex]]  分类索引
- [[class pd.MultiIndex]]  多级索引
- [[class pd.IntervalIndex]]  区间索引
- [[class pd.DatetimeIndex]]  时间索引
- [[class pd.TimedeltaIndex]]  时间差索引
- [[class pd.PeriodIndex]]  周期索引
##### pandas 索引示例
```python
import pandas as pd

# 创建一个示例的 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Country': ['USA', 'Canada', 'UK']
}
df = pd.DataFrame(data)

# 使用默认整数索引
# RangeIndex(start=0, stop=3, step=1)
print("Default Index:")
print(df)

# 使用自定义标签索引
# Index(['a', 'b', 'c'], dtype='object')
df.index = ['a', 'b', 'c']
print("\nCustom Label Index:")
print(df)

# 使用列作为索引  
# Index(['Alice', 'Bob', 'Charlie'], dtype='object', name='Name')
df.set_index('Name', inplace=True)
print("\nColumn 'Name' as Index:")
print(df)

# 重置索引为默认整数索引
# RangeIndex(start=0, stop=3, step=1)
df.reset_index(inplace=True)
print("\nReset Index:")
print(df)

# 使用 MultiIndex 创建多级索引
# MultiIndex([('USA', 25), ('Canada', 30), ('UK', 22)], names=['Country', 'Age'])
df.set_index(['Country', 'Age'], inplace=True)
print("\nMultiIndex:")
print(df)

# 使用 date_range 创建时间索引
# DatetimeIndex(['2023-08-01', '2023-08-02', '2023-08-03'], dtype='datetime64[ns]', freq='D')
df.index = pd.date_range(start='2023-08-01', end='2023-08-3', freq='D')
```