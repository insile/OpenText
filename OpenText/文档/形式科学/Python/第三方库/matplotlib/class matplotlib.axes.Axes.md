##### class matplotlib.axes.Axes 图表
- `Axes.绘图方法`
	- [[Axes.plot()]] 折线图
	- [[Axes.hist()]] 频率直方图
	- [[Axes.bar()]] 柱状图
	- [[Axes.barh()]] 条形图
	- [[Axes.scatter()]] 散点图
	- [[Axes.pie()]] 饼图
	- [[Axes.polar()]] 极坐标图
	- [[Axes.imshow]] 图像
	- [[Axes.contour()]] 等高线图
	- [[Axes.contourf()]] 填充的等高线图
	- [[Axes.pcolormesh()]] 伪彩色图
- `Axes.图标元素方法`
```python
# 标题与图例
Axes.set_title(label, fontdict=None, loc=None, pad=None, 
			   *, y=None, **kwargs)
Axes.legend(loc="lower left", *args, **kwargs)

# xy轴标签
Axes.set_xlabel(xlabel, fontdict=None, labelpad=None, 
				*, loc=None, **kwargs)
Axes.set_ylabel(ylabel, fontdict=None, labelpad=None, 
				*, loc=None, **kwargs)

# 限制xy轴的值
Axes.set_xlim((left, right))
Axes.set_ylim((bottom, top))

# xy轴非线性刻度
Axes.set_xscale({"linear", "log", "symlog", "logit"}, **kwargs)
Axes.set_yscale({"linear", "log", "symlog", "logit"}, **kwargs)

# xy轴刻度
Axes.set_xticks(ticks, labels=None, *, minor=False, **kwargs)
Axes.set_yticks(ticks, labels=None, *, minor=False, **kwargs)

# 反转xy轴
Axes.invert_xaxis()
Axes.invert_yaxis()

# 图表元素设置
Axes.set(xlabel='x轴标签', ylabel='y轴标签', title='标题')

# 网格线
Axes.grid(visible=None, which='major', axis='both', 
		  linestyle="风格",color="颜色"
		  **kwargs)

# 指向与无指向注释
Axes.annotate(string,xy='被注释位置坐标',xytext='注释位置坐标',
			 weight="bold", color="b", 
			 # arrowprops：箭头属性字典
			 arrowprops=dict(arrowstyle="->",
							 connectionstyle="arc3",
							 color="b"))
Axes.text(x,y,string,weight="bold",color="b")

# xy轴参考线
Axes.axhline(y=0.0,c="r",ls="--",lw=2)
Axes.axvline(y=0.0,c="r",ls="--",lw=2)

# xy轴参考区域
Axes.axhspan(xmin=1.0,xmax=2.0,facecolor="y",alpha=0.3)
Axes.axvspan(xmin=1.0,xmax=2.0,facecolor="y",alpha=0.3)

# 返回xy轴实例
Axes.get_xaxis()
Axes.get_yaxis()

# xy轴等比例
Axes.set_aspect(1)
```