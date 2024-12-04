##### MultiIndex 类
- 用于表示多层次的索引
- [[MultiIndex.创建]]
- MultiIndex 属性
- MultiIndex 方法
##### MultiIndex 多级索引
- 多级索引（MultiIndex）是 Pandas 中用于在 DataFrame 中创建具有多个层次的索引的工具。它允许你在数据中引入多个维度的分层结构，以便更方便地进行多维度的数据分析和操作。下面是一些多级索引的使用示例：

```python
import pandas as pd

data = {'Date': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'Product': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 120]}

df = pd.DataFrame(data)
#	         Date         City Product  Sales
#	0  2023-08-01     New York       A    100
#	1  2023-08-01  Los Angeles       B    150
#	2  2023-08-02     New York       A    200
#	3  2023-08-02  Los Angeles       B    120

# 将 'Date', 'City', 'Product' 作为一个多级索引
df.set_index(['Date', 'City', 'Product'], inplace=True)
print(df)
#	                                Sales
#	Date       City        Product       
#	2023-08-01 New York    A          100
#	           Los Angeles B          150
#	2023-08-02 New York    A          200
#	           Los Angeles B          120

df.index
#	MultiIndex([('2023-08-01',    'New York', 'A'),
#	            ('2023-08-01', 'Los Angeles', 'B'),
#	            ('2023-08-02',    'New York', 'A'),
#	            ('2023-08-02', 'Los Angeles', 'B')],
#	           names=['Date', 'City', 'Product'])

# 多级索引的级别
df.index.levels
# FrozenList([['2023-08-01', '2023-08-02'], ['Los Angeles', 'New York'], ['A', 'B']])

df.loc['2023-08-02']
#	                     Sales
#	City        Product       
#	New York    A          200
#	Los Angeles B          120
df.loc[('2023-08-01', 'New York', 'A')]
#	Sales    100

```
