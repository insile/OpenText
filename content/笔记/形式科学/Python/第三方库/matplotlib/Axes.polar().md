##### Axes.polar()
```python
# 极坐标图
polar(theta, r, **kwargs)
	# theta ：表示每个数据点所在射线与极径的夹角
	# r ：表示每个数据点到原点的距离
```
##### 示例
```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# 生成数据
theta = np.linspace(0, 2*np.pi, 100)
r = np.sin(2*theta)

# 创建极坐标图
ax.plot(theta, r, color='blue', linestyle='--', linewidth=2)

# 添加标题
ax.set_title('Polar Plot')

# 显示图形
plt.show()

```
![[Pasted image 20240314104031.png]]