##### Axes.barh()
```python
# 条形图
barh(y, width, height=0.8, left=None,
	 *, align='center', **kwargs)
	# y ：表示条形的 y 坐标值。
	# width ：表示条形的宽度，默认值为 0.8。
	# height ：表示条形的高度。
	# left ：条形左侧的 x 坐标，默认为 0。
	# align ：表示条形的对齐方式，有 'center' 和 'edge' 两个取值，其中 'center' 表示将条形与刻度线居中对齐 ；'edge' 表示将条形的底边与刻度线对齐。
```
##### 示例
```python
import matplotlib.pyplot as plt

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 数据
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# 创建水平柱状图
ax.barh(categories, values, color='skyblue', alpha=0.7)

# 添加标题和标签
ax.set_title('Horizontal Bar Chart')
ax.set_xlabel('Values')
ax.set_ylabel('Categories')

# 显示图形
plt.show()

```
![[Pasted image 20240314103839.png]]