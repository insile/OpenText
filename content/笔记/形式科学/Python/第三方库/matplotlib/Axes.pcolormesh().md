##### Axes.pcolormesh()
```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 生成数据
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# 绘制伪彩色图
pcolormesh = ax.pcolormesh(X, Y, Z, cmap='viridis')

# 添加颜色条
plt.colorbar(pcolormesh, ax=ax)

# 添加标题和标签
ax.set_title('Pcolormesh Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# 显示图形
plt.show()

```
![[Pasted image 20240314104331.png]]