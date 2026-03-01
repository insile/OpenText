##### pandas.轴
- Series 和 DataFrame 很多方法都有一个参数 axis 指示函数计算的方向
- 默认 0 一般不会修改该参数
- 与 ndarray 相同
- 很多 Series 和 DataFrame 相同的方法区别仅是从计算一列到多列
```python
df = pd.DataFrame({'one': pd.Series([1,2,3], index=['a','b','c']),
				   'two': pd.Series([1,2,3], index=['a','b','c']),
				   'three': pd.Series([1,2,3], index=['a','b','c'])})
#		one two three
#	a	1   1   1
#	b	2   2   2
#	c	3   3   3

# axis = 0 表示沿0轴（行）扩展的方向，a-b-c
# axis = 1 表示沿1轴（列）扩展的方向，one-two-three

df['one'].mean(axis=0)
	# 2.0

df.mean(axis=0) # 默认
	# 表示沿0轴计算均值
	# one   2
	# two   2
	# three 2

df.mean(axis=1)
	# 表示沿1轴计算均值
	# a   1
	# b   2
	# c   3
```
