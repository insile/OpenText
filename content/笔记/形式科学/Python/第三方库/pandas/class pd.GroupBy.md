##### class pd.GroupBy
- 包括SeriesGroupBy和DataFrameGroupBy
##### GroupBy 方法
```python
# 索引迭代
GroupBy.__iter__()  # 按 (组名, Series/DataFrame) 迭代
GroupBy.groups  # 返回字典 {组名: [标签]}
GroupBy.indices  # 返回字典 {组名: [索引]}
GroupBy.get_group(name, obj=None)  # 使用组名查询组

# 函数应用
GroupBy.apply()
GroupBy.agg()
GroupBy.filter()

# 统计计算
GroupBy.count()
GroupBy.rank()
...

```
##### GroupBy 示例
```python
import pandas as pd

data = {'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'Product': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 120]}

df = pd.DataFrame(data)

# 按城市分组
grouped = df.groupby('City') 
grouped.groups  
# {'Los Angeles': [1, 3], 'New York': [0, 2]}
grouped.get_group('New York')
#	       City Product  Sales
#	0  New York       A    100
#	2  New York       A    200

# 对 Sales 执行聚合
city_sales = grouped['Sales'].agg(['mean', 'sum'])
print(city_sales)
#	              mean  sum
#	City                   
#	Los Angeles  135.0  270
#	New York     150.0  300

# 同时对不同列进行不同的聚合操作
aggregations = {'Sales': 'sum', 'Product': 'count'}
result = grouped.agg(aggregations)
print(result)
#	             Sales  Product
#	City                       
#	Los Angeles    270        2
#	New York       300        2

# 筛选分组均值大于 140
def high_sales(group):
    return group['Sales'].mean() > 140
high_sales_groups = grouped.filter(high_sales)
print(high_sales_groups)
#	       City Product  Sales
#	0  New York       A    100
#	2  New York       A    200

# 同时使用多个分组键：
multi_grouped = df.groupby(['City', 'Product'])
city_product_sales = multi_grouped['Sales'].sum()
print(city_product_sales)
#	City         Product
#	Los Angeles  B          270
#	New York     A          300
#	Name: Sales, dtype: int64


```

