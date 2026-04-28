##### 顺序统计量
```python
np.percentile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=False, *, interpolation=None)
	# 沿指定的轴计算数据 a 的第 q 百分位数。
np.quantile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=False)
	# 沿指定的轴计算数据 a 的 q 分位数。
```
##### 均值和方差
```python
np.average(a, axis=None, weights=None)
	# 均值
np.std(a, axis=None)
	# 标准差
np.var(a, axis=None)
	# 方差
```
##### 相关性
```python
np.corrcoef(x, y=None, rowvar=True, bias=<no value>, ddof=<no value>, *, dtype=None)
	# 皮尔逊相关系数矩阵，默认 rowvar 行变量
np.correlate(a, v, mode='valid')
	# 两个一维序列的互相关
np.cov(m, y=None, rowvar=True, bias=False, ddof=None, fweights=None, aweights=None, *, dtype=None)
	# 协方差矩阵，默认 rowvar 行变量
```
##### 直方图
```python
np.histogram(a, bins=10, range=None, density=None, weights=None)
	# 计算数据集的直方图。
np.histogram2d(x, y, bins=10, range=None, density=None, weights=None)
	# 计算两个数据样本的二维直方图
```