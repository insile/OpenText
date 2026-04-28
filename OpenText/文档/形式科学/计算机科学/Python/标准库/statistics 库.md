##### statistics 库
- 该模块提供了用于计算数字 (Real-valued) 数据的数理统计量的函数
```python
import statistics
```
##### statistics 主要API
```python
# data 为序列或迭代器
# 集中趋势
statistics.mean(data)  # 数据的算术平均数（“平均数”）
statistics.fmean(data, weights=None)  # 快速，浮点数算术平均值，可选加权
statistics.geometric_mean(data)  # 数据的几何平均数
statistics.harmonic_mean(data, weights=None)  # 数据的调和均值
statistics.median(data)  # 数据的中位数（中间值）
statistics.median_low(data)  # 数据的低中位数
statistics.median_high(data)  # 数据的高中位数
statistics.median_grouped(data, interval=1)  # 分组数据的中位数，即第50个百分点。
statistics.mode(data)  # 离散的或标称的数据的单个众数（出现最多的值）。
statistics.multimode(data)  # 离散的或标称的数据的众数（出现最多的值）列表。
statistics.quantiles(data)  # 将数据以相等的概率分为多个间隔。

# 离散趋势
statistics.pstdev(data, mu=None)  # 数据的总体标准差
statistics.pvariance(data, mu=None)  # 数据的总体方差
statistics.stdev(data, xbar=None)  # 数据的样本标准差
statistics.variance(data, xbar=None)  # 数据的样本方差

# 变量关系
statistics.covariance(x, y)  # 两个变量的样本协方差。
statistics.correlation(x, y)  # 两个变量的皮尔逊相关系数。
statistics.linear_regression(x, y)  # 简单线性回归的斜率和截距。
```