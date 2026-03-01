##### random 库
- 用于生成伪随机数的模块。它提供了多种随机数生成函数，可以用于各种应用场景，如随机数生成、随机选择、随机洗牌等
```python
import random
```
##### random 主要API
```python
# 随机数种子
random.seed()  # 相同的种子值调用随机数一样
# 整数用函数：
random.randint(a,b)  # ab之间的整数
random.randrange(m,n,k)  # mn间k步长整数
random.getrandbits(k)  # k比特长整数
# 序列用函数
random.choice(seq)  # 从序列中随机选择
random.shuffle(seq)  # 随机排序序列并返回
# 随机分布
random.random()  # 生成0-1随机浮点数
random.uniform(a, b)  # 返回一个在闭区间 [a, b] 内的随机浮点数 
random.triangular(low, high, mode)  # 三角分布的随机浮点数
	# low: 分布的下界，表示随机数生成的范围的最小值。
	# high: 分布的上界，表示随机数生成的范围的最大值。
	# mode: 分布的众数，表示分布的峰值位置。
random.betavariate(alpha, beta)  # Beta 分布的随机浮点数
random.expovariate(lambd)  # 指数分布
random.gammavariate(alpha, beta)  # Gamma 分布
random.gauss(mu=0.0, sigma=1.0)  # 正态分布
random.lognormvariate(mu, sigma)  # 对数正态分布

```