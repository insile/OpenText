##### Axes.pie()
```python
# 饼图
pie(x, explode=None, labels=None, autopct=None, 
　　 pctdistance=0.6, shadow=False, 
　　 labeldistance=1.1, startangle=None, 
　　 radius=None, counterclock=True, 
　　 wedgeprops=None, textprops=None, 
　　 center=(0, 0), frame=False, rotatelabels=False, 
　　 *, data=None) 

	# x ：表示扇形或楔形的数据。
	# explode ：表示扇形或楔形离开圆心的距离。
	# labels ：表示扇形或楔形对应的标签文本。
	# autopct ：表示控制扇形或楔形的数值显示的字符串，可通过格式字符串指定小数点后的位数。
	# pctdistance ：表示扇形或楔形对应的数值标签距离圆心的比例，默认为 0.6。
	# shadow ：表示是否显示阴影。
	# labeldistance ：表示标签文本的绘制位置（相对于半径的比例），默认为 1.1。
	# startangle ：表示起始绘制角度，默认从 x 轴的正方向逆时针绘制。
	# radius ：表示扇形或楔形的半径。
	# wedgeprops ：表示控制扇形或楔形属性的字典。例如，通过 wedgeprops = {'width': 0.7} 将楔形的宽度设为 0.7。
	# textprops ：表示控制图表中文本属性的字典。
	# center ：表示图表的中心点位置，默认为（0,0）。
	# frame ：表示是否显示图框。
```
##### 示例
```python
import matplotlib.pyplot as plt

# 创建一个 Figure 和 Axes 对象
fig, ax = plt.subplots()

# 数据
sizes = [30, 20, 15, 35]
labels = ['A', 'B', 'C', 'D']

# 创建饼图
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# 添加标题
ax.set_title('Pie Chart')

# 显示图形
plt.show()

```
![[Pasted image 20240314104002.png]]