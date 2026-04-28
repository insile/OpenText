##### 从列表、元组等类型创建
```python
np.array(object，[dtype=None, # 元素类型
				 copy=True, # 默认深拷贝
				 order=None, 
				 ndmin=0, # 维数
				 subok=False # 默认返回一个与基类类型一致的数组 ])

arr = np.array([1,2,3], dtype=np.float32)
```
##### 使用函数创建
```python
np.arange(n) 
	# 类似range()，返回ndarray，元素0到n-1

np.empty(shape)
	# 根据shape生成一个空数组，shape是元组类型
np.ones(shape) 
	# 全1数组
np.zeros(shape) 
	# 全0数组
np.full(shape,val) 
	# 全val数组
np.empty_like(a)
	# 根据数组a的形状生成一个空数组
np.ones_like(a) 
	# 全1数组
np.zeros_like(a) 
	# 全0数组
np.full_like(a,val) 
	# 全val数组

np.eye(n)
	# 创建一个正方的n*n单位矩阵，对角线为1，其余为0
np.linspace(a,b,c,endpoint=f&t) 
	# 从a至b等间距地生成c个数据，判断是否包括c
np.logspace(a,b,c,endpoint=f&t)
	# 从a至b等比地生成c个数据，判断是否包括c
np.concatenate() 
	# 将两个或多个数组合并成一个新的数组

np.meshgrid(xarray,yarray)
	# 笛卡尔积，生成网格点坐标矩阵，以二维矩阵的形式表示xy坐标
np.ogrid[1:5,1:5:2]
	# 返回一个开放的（即未充实的）meshgrid网格
	# 产生两个不同维度的向量n行1列，1行n列
	# 步长可为复数如3j，即用3个数等分区间，含首位
np.mgrid[0:5, 0:5]
	# 直接产生了ogrid中两个向量广播后的矩阵，meshgrid
np.diag(v, k=0)
	# 提取对角线或构造对角线数组
				 
```
##### 从字节流创建
```python
np.fromstring(string, dtype=float, count=- 1, *, sep, like=None)
	# 从字符串中的文本数据初始化的新一维数组。
	# np.fromstring('1,2,3,4', dtype=int, sep=',')
```
##### 从文件中读取创建

