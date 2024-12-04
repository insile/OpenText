##### matplotlib.pyplot 
- 快速绘图接口
```python
pyplot.figure(num=None, figsize=[6.4, 4.8], dpi=100.0, **kwargs)
    # 创建返回Figure实例，kwargs详见figure.Figure
		# num：figure唯一标识符
		# figsize：[宽, 高]，英寸
		# dpi  # 每英寸点数

pyplot.subplots(nrows=1, ncols=1, 
	*, sharex=False, sharey=False, squeeze=True, 
	subplot_kw=None, gridspec_kw=None, **fig_kw)
	# 创建返回Figure和Axes实例
		# nrows、ncols：网格的行数和列数
		# sharex、sharex：共享坐标轴
		# subplot_kw: Figure.add_subplot 调用的关键字的字典
		# fig_kw：支持pyplot.figure的参数

pyplot.axes(dimensions, projection, sharex, sharey)
	# 将 Axes 添加到当前图形，并使其成为当前 Axes
	# 返回Axes，使用cartopy投影返回GeoAxesSubplot

pyplot.show(block=None)
	# 显示所有Figure

pyplot.ion()
	# 打开交互模式

pyplot.ioff()	
	# 关闭交互模式

pyplot.isinteractive()
	# 返回pyplot是否处于“交互模式”
```