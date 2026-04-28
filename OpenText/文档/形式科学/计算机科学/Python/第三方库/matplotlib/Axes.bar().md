##### Axes.bar()
```python
# 柱状图
bar(x, height, width=0.8, bottom=None, 
	align='center', data=None, tick_label=None, 
	xerr=None, yerr=None, error_kw=None, **kwargs)

	# x ：表示柱形的 x 坐标值。
	# height ：表示柱形的高度。
	# width ：表示柱形的宽度，默认为 0.8。
	# bottom ：表示柱形底部的 y 坐标值，默认为 0。
	# align ：表示柱形的对齐方式，'center' 表示将柱形与刻度线居中对齐 ；'edge' 表示将柱形的左边与刻度线对齐。
	# tick_label ：表示柱形对应的刻度标签。
	# xerr，yerr ：水平 / 垂直误差棒。
	# error_kw ：表示误差棒的属性字典，字典的键对应 errorbar() 函数（2.10 节会介绍）的关键字参数。
```
##### 示例
```python
import matplotlib.pyplot as plt

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 数据
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# 创建柱状图
ax.bar(categories, values, color='skyblue', alpha=0.7)

# 添加标题和标签
ax.set_title('Bar Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# 显示图形
plt.show()

```
![[Pasted image 20240314103744.png]]