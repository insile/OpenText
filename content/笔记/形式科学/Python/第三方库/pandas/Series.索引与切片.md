##### Series 索引与切片
```python
import pandas as pd
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series1 = pd.Series(data, index=index)  # 字符串标签
series2 = pd.Series(data, index=data)  # 整数标签
series3 = pd.Series(data)  # 自动整数位置标签
```
##### Series 索引
```python
Series.loc[label]
	# 标签和布尔数组索引
	print(series1.loc['a'])  # 输出 10
	print(series2.loc[20])  # 输出 20
	print(series3.loc[2])  # 输出 30
	print(series1.loc[series > 20])  # 输出Series 含大于 20 的元素
Series.iloc[position]
	# 位置索引
	print(series1.iloc[0])  # 输出 10
	print(series2.iloc[1])  # 输出 20
	print(series3.iloc[2])  # 输出 30
	print(series1.iloc[[0, 2, 4]])  # 输出索引为 0、2、4 的元素
Series[label_or_position]
	# 位置或标签索引
	# 标签存在数值则不能用位置取值，只能标签
	# 索引可为为负数
	# 索引不存在会报错
	# 可添加新的索引与值
	# 新增不同类型索引，索引类型自动变化
	# Series[[ , , , ]] 可索引多值,返回新Series
```
##### Series 切片
```python
Series.loc[start_label:stop_label:step]
	# 标签切片，首尾包含
	print(series1.loc['a':'c'])  # 输出索引从 'a' 到 'c' 的元素，包括 'a' 和 'c'
	print(series2.loc[10:30])  # 输出索引从 10 到 30 的元素，包括 10 和 30
	print(series3.loc[0:2])  # 输出索引从 0 到 2 的元素，包括 0 和 2
Series.iloc[start_position:stop_position:step]
	# 位置切片，不包含尾端
	print(series1.iloc[0:2])  # 输出索引从 0 到 2 的元素，不含 2
	print(series2.iloc[0:2])  # 输出索引从 0 到 2 的元素，不含 2
	print(series3.iloc[0:2])  # 输出索引从 0 到 2 的元素，不含 2
Series[]
	# 位置或标签切片
```

