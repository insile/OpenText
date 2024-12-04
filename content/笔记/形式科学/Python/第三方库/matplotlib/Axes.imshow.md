##### Axes.imshow
```python
# 图像
Axes.imshow(X, cmap=None, norm=None, *, aspect=None, interpolation=None, 
			alpha=None, vmin=None, vmax=None, origin=None, extent=None, 
			interpolation_stage=None, filternorm=True, filterrad=4.0, 
			resample=None, url=None, data=None, **kwargs)
	# X: array-like or PIL image
	# cmap: Colormap 
	# extentfloats: (left, right, bottom, top), optional
	# origin: upper，图像正常显示，原点位置在左上角，默认。lower， 图像倒着显示，原点位置在左下角。

```
##### 示例
```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 生成随机图像数据
np.random.seed(0)
image_data = np.random.rand(10, 10)

# 显示图像
ax.imshow(image_data, cmap='viridis')

# 添加标题
ax.set_title('Image')

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()

```
![[Pasted image 20240314104121.png]]