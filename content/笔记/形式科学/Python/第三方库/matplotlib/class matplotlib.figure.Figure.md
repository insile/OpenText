##### class matplotlib.figure.Figure 布局
- `Figure.创建`
```python
Figure(figsize=[6.4, 4.8],  # [宽, 高] 英寸
		dpi=100.0,  # 每英寸点数
		*, 
		facecolor=None,  # 背景色
		edgecolor=None,  # 边框色
		layout=None,  # 布局 {'constrained', 'compressed', 'tight', 'none', LayoutEngine, None}
		**kwargs)
# 同 pyplot
```
- `Figure.方法`
```python
# 添加gridspec
Figure.add_gridspec(nrows=2, ncols=2, **kwargs)  # 网格布局，返回GridSpec

# 添加axes
Figure.add_axes(dimensions, projection, sharex, sharey)  # 左, 底, 宽, 高
Figure.add_subplot(position, projection, sharex, sharey)  # 行, 列, 划分索引

# 输出
Figure.savefig(fname, *, transparent=None, **kwargs)
Figure.show(warn=True)

# 色带
Figure.colorbar(mappable=None, cax=None, ax=None, **kw)
	# mappable`：可映射的，要求是 `matplotlib.cm.ScalarMappable` 对象，能够向 colorbar 提供数据与颜色间的映射关系（即 colormap 和 normalization 信息）。主图中使用 `contourf`、`pcolormesh` 和 `imshow` 等二维绘图函数时返回的对象都属于 `ScalarMappable`。
	# cax：指定新的绘图区域axes
	# ax：当前现有绘图区域axes，可多个子图
	# **kw：支持axes和colorbar的属性
	# location：位置，None or {'left', 'right', 'top', 'bottom'}
	# orientation：方向，None or {'vertical', 'horizontal'}
	# fraction：float, default: 0.15
	# shrink：放大系数，float, default: 1.0
	# pad：与图距离，float, default: 0.05 if vertical, 0.15 if horizontal

	# cmap：颜色图
	# alpha：透明度
	# orientation：方向{'vertical', 'horizontal'}
	# ticklocation：刻度位置{'auto', 'left', 'right', 'top', 'bottom'}
	# ticks：刻度Locator or array-like of float，ticks=range(20, 360, 40)
```
