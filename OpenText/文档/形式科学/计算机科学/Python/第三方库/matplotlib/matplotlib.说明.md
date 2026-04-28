##### matplotlib.说明
- matplotlib 库由各种可视化类构成，内部结构复杂，受Matlab启发
- matplotlib 提供了两种API：隐式 API 和显式 API
	- [[matplotlib.pyplot]] 是绘制各类可视化图形的命令子库，相当于快捷方式 API
	- 对于复杂的绘图，建议使用显式的面向对象的 API，仅使用 pyplot 来创建图轴
- matplotlib 提供了两种绘图模式：非交互模式和交互模式
	- 在交互模式下，每输入一条命令图形即时变化，方便查看命令行每个命令的效果
	- 使用 [[matplotlib.后端管理]] 切换交互式后台，并使用[[matplotlib.pyplot|pyplot.ion()]] 启用交互模式
