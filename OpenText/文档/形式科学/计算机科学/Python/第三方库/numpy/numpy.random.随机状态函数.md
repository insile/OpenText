##### numpy.random 随机状态函数
- 随机状态提供对遗留生成器的访问，将不会有进一步的改进
```python
np.random.seed(seed=None)
	# 设置随机数种子
np.random.rand(shape)
	# 0到1之间的随机数
np.random.randn(shape)
	# 标准正态分布的随机数
np.random.randint(low, high=None, size=None, dtype=int)
	# 指定范围内的随机整数
np.random.normal(期望, 标准差, shape)
	# 正态分布
np.random.uniform(起始值, 终值, shape)
	# 均匀分布 
np.random.poisson(单位时间随机时间平均发生率, shape)
	# 泊松分布 
np.random.permutation(x) 
	# 随机排列 
	# 当参数为整数n时，它返[0，n)这n个整数的随机排列
	# 当参数为一个序列吋，它返冋一个随机排列之后的序列
np.random.shuffle(array)
	# 随机打乱顺序 
np.random.choice(a, size=None, replace=True, p=None)
	# 随机抽取样本 
	# size参数用于指定输出数组的形状
	# replace参数为True时，进行可重复抽取，而为False吋进行不重复取，默认值为True 
	# p参数指定每个元素对应的抽取概率，如果不指定，所有的元素被抽到的概率相同
```