##### `pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)`
**功能简介:**
- 用于存储二维的带标签的数据表格。每个列可以包含不同的数据类型，并且 DataFrame 可以看作是多个 Series 按列排列而成的结构。

**参数说明:**
- `data`：用于构建 DataFrame 的数据。可以是多种数据类型，包括字典、列表、数组、Series、其他 DataFrame 等。默认为 None。
- `index`：用于指定数据表格的行标签（索引）。可以是列表、数组、索引对象等。默认为 None，将使用默认的整数索引。
- `columns`：用于指定数据表格的列标签。可以是列表、数组等。默认为 None，将使用默认的列名。
- `dtype`：指定 DataFrame 中数据的数据类型。默认情况下，pandas 会根据输入数据自动推断数据类型。
- `copy`：控制数据是否复制。True 表示复制数据，False 表示引用数据。默认为 None，由 pandas 自行决定。

**返回值:**
- 返回一个新的 pandas DataFrame 对象，包含了传递的数据、索引、列等信息。DataFrame 可用于进行数据操作、分析、聚合以及与其他数据结构的整合等各种操作。

**用法示例:**
1. 接受各种数据
```python
import pandas as pd
# '列表嵌套列表'嵌套一行数据
pd.DataFrame([['xiaowang',20], 
			  ['lily',30], 
			  ['anne', 40]])
# 	          0   1
#	0  xiaowang  20
#	1      lily  30
#	2      anne  40

# '列表嵌套字典'嵌套一行数据
pd.DataFrame([{'a':1, 'b':2}, 
			  {'a':5, 'b':10, 'c':20}])
#	   a   b     c
#	0  1   2   NaN
#	1  5  10  20.0

# '字典嵌套列表'嵌套一列数据
pd.DataFrame({'Name':['关羽', '刘备', '张飞', '曹操'], 
			  'Age':[28, 34, 29, 42]})
#	  Name  Age
#	0   关羽   28
#	1   刘备   34
#	2   张飞   29
#	3   曹操   42

# '字典嵌套Series'嵌套一列数据
pd.DataFrame({'one': pd.Series([1,2,3], index=['a','b','c']), 
			  'two': pd.Series([1,2,3,4], index=['a','b','c','d'])})
#	   one  two
#	a  1.0    1
#	b  2.0    2
#	c  3.0    3
#	d  NaN    4

```
