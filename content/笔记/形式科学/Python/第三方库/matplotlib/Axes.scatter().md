##### Axes.scatter()
```python
# 散点图
scatter(x, y, s=None, c=None, 
		marker=None, cmap=None, norm=None, 
		vmin=None, vmax=None, alpha=None, 
		linewidths=None, verts=None, 
		edgecolors=None, *, plotnonfinite=False, 
		data=None, **kwargs)

	# x，y ：表示数据点的位置。
	# s ：表示数据点的大小。
	# c ：表示数据点的颜色。
	# marker ：表示数据点的样式，默认为圆形。
	# cmap ：表示数据点的颜色映射表，仅当参数 c 为浮点数组时才使用。
	# norm ：表示数据亮度，可以取值为 0 ～ 1。
	# vmin，vmax ：表示亮度的最小值和最大值。若传入了 norm 参数，则忽略 vmin 和vmax 参数。
	# alpha ：表示透明度，可以取值为 0 ～ 1。
	# linewidths ：表示数据点边缘的宽度。
	# edgecolors ：表示数据点边缘的颜色。
```
##### 示例
```python
import matplotlib.pyplot as plt

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建散点图
ax.scatter(x, y, s=100, c='skyblue', marker='o', label='Data Points')

# 添加标题和标签
ax.set_title('Scatter Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# 添加图例
ax.legend()

# 显示图形
plt.show()

```
![[Pasted image 20240314103912.png]]