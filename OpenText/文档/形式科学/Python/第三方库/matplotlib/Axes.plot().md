##### Axes.plot()
```python
# 线图
plot(x, y, 
	 scalex=True, scaley=True, 
	 data=None, **kwargs)
		# linestyle：线风格
	# linewidth：线宽度
	# label：用于图例的标签
```
##### 示例
```python
import matplotlib.pyplot as plt

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 绘制一条线
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], linestyle='--', color='r', marker='o', label='Line 1')

# 添加标题和标签
ax.set_title('Line Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# 添加图例
ax.legend()

# 显示图形
plt.show()
```
![[Pasted image 20240314103357.png]]