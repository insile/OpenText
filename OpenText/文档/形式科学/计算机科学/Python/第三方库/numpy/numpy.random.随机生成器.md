##### numpy.random 随机生成器
```python
# 实例化
np.random.default_rng(seed=None)
	# 创建Generator
```
##### numpy.random.Generator 方法
```python
Generator.integers(low, high=None, size=None, dtype=np.int64, endpoint=False)
	# 随机整数
	
Generator.random(size=None, dtype=np.float64, out=None)
	# 0-1随机数

Generator.choice(a, size=None, replace=True, p=None, axis=0, shuffle=True)
	# 随机抽样

Generator.binomial(n, p, size=None)
	# 二项分布
Generator.chisquare(df, size=None)
	# 卡方分布
Generator.normal(loc=0.0, scale=1.0, size=None)
	# 正态分布
Generator.poisson(lam=1.0, size=None)
	# 泊松分布
Generator.standard_normal(size=None, dtype=np.float64, out=None)
	# 标准正态分布
Generator.uniform(low=0.0, high=1.0, size=None)
	# 均匀分布
```