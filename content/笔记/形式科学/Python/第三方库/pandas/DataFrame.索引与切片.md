##### DataFrame 索引与切片
```python
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Boston']
}
df = pd.DataFrame(data, index=['a','b','c','d','e'])
#       Name  Age         City  
# 0    Alice   25     New York  
# 1      Bob   30  Los Angeles  
# 2  Charlie   22      Chicago  
# 3    David   28      Houston  
# 4    Emily   35       Boston
```
##### DataFrame 索引
```python
# 行索引
	DataFrame.loc[label] 
		# DataFrame.loc['行标签'] 返回 Series 一行
			print(df.loc['a']) 
		# DataFrame.loc['行标签'，'列标签']
			print(df.loc['a','Name'])
		# DataFrame.loc[['行标签', '行标签']，
		# 				['列标签', '列标签']]
			print(df.loc[['a','b'],['Name','Age']]) 
	DataFrame.iloc[position]
		# 同上
# 列索引
	DataFrame[label]
		# DataFrame['行标签'] 
			print(df['Name'])
		# DataFrame[['行标签', '行标签', '行标签']] # 返回 DataFrame 多列 
			print(df[['Name','Age']])
		# DataFrame['行标签']['列标签']
			print(df['Name']['a'])
		# 使用DataFrame['列标签']=value，添加新数据列
```
##### DataFrame 切片
```python
# 按行切片
DataFrame.loc[]
	print(df.loc['a':'c'])  # a-c行，所有字段
	print(df.loc['a':'c','Name']) # a-c行，Name字段
	print(df.loc['a':'c','Name':'City']) # a-c行，Name-City字段
DataFrame.iloc[]
	# 同上
DataFrame[]
	print(df['Name']['a':'c']) # a-c行，Name字段
```
##### 示例
```python
df = pd.DataFrame({
	'one': pd.Series([1,2,3], index=['a','b','c']), 
	'two': pd.Series([1,2,3,4], index=['a','b','c','d'])
})

'''
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
'''

df['one']  # one 列
df[['one','two']]  # one,two 列

df['one']['c']  # one 列 c 行
df['one'][2]  # one 列 2 行

df.loc['a']  # a 行
df.loc[['a','b']]  # a b 行
df.loc['a', 'one']  # a 行 one 列

df.iloc[0]  # 第 0 行
df.iloc[[0, 1]]  # 第 0 1 行
df.iloc[0, 0]  # 第 0 行 0 列
```
