##### Resampler 方法
```python
# 索引迭代
Resampler.__iter__()
Resampler.groups
Resampler.indices
Resampler.get_group(name[, obj])

# 函数应用
Resampler.apply([func])
Resampler.aggregate([func])
Resampler.transform(arg, *args, **kwargs)
Resampler.pipe(func, *args, **kwargs)

# 升采样填充
Resampler.ffill([limit])
Resampler.bfill([limit])
Resampler.nearest([limit])

# 降采样聚合
Resampler.count()
Resampler.mean([_method])
...
```
##### Resampler 示例
```python
import pandas as pd

# 创建示例时间序列数据
date_rng = pd.date_range(start='2023-08-01', periods=10, freq='D')
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ts = pd.Series(values, index=date_rng)
#	2023-08-01     10
#	2023-08-02     20
#	2023-08-03     30
#	2023-08-04     40
#	2023-08-05     50
#	2023-08-06     60
#	2023-08-07     70
#	2023-08-08     80
#	2023-08-09     90
#	2023-08-10    100
#	Freq: D, dtype: int64

# 每周平均重采样：
weekly_resampler = ts.resample('W')
weekly_mean = weekly_resampler.mean()
print(weekly_mean)

# 每月总和重采样：
monthly_resampler = ts.resample('M')
monthly_sum = monthly_resampler.sum()
print(monthly_sum)

# 每两天中的最大值重采样：
two_days_resampler = ts.resample('2D')
two_days_max = two_days_resampler.max()
print(two_days_max)

# 升采样和插值：
upsampled_resampler = ts.resample('H')
upsampled_mean = upsampled_resampler.mean()
print(upsampled_mean)

# 自定义聚合函数：
def weighted_average(series):
    weights = [0.1, 0.2, 0.3, 0.4]
    return (series * weights).sum() / sum(weights)

custom_resampler = ts.resample('W')
custom_mean = custom_resampler.apply(weighted_average)
print(custom_mean)
```