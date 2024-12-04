##### Axes.hist()
```python
# 频率直方图
hist(x, bins=None, range=None, 
	 density=False, weights=None, 
	 cumulative=False, bottom=None, histtype='bar', 
	 align='mid', orientation='vertical', rwidth=None, 
	 log=False, color=None, label=None, stacked=False, 
	 *, data=None, **kwargs)
	# x：表示 x 轴的数据，可以为单个数组或多个数组的序列。
	# bins：表示矩形条的个数，默认为 10。
	# range：表示数据的范围。默认数据范围为 (x.min(), x.max())。
	# cumulative ：表示是否计算累计频数或频率。
	# histtype ：表示直方图的类型，'bar' 为默认值，代表传统的直方图 ；'barstacked' 代表堆积直方图 ；'step' 代表未填充的线条直方图 ；'stepfilled' 代表填充的线条直方图。
	# align ：表示矩形条边界的对齐方式，可设置为 'left'、'mid' 或 'right'，默认为 'mid'。
	# orientation ：表示矩形条的摆放方式，默认为 'vertical'，即垂直方向。
	# rwidth ：表示矩形条宽度的百分比，默认为 0。若 histtype 的值为 'step' 或 'stepfilled'，则直接忽略 rwidth 参数的值。
	# stacked ：表示是否将多个矩形条以堆积形式摆放。
```
##### 示例
```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 生成一些随机数据
data = np.random.randn(1000)

# 创建直方图
ax.hist(data, bins=30, color='skyblue', alpha=0.7)

# 添加标题和标签
ax.set_title('Histogram')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# 显示图形
plt.show()

```
![[Pasted image 20240314103513.png]]