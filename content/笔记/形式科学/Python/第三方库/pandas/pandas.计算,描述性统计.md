##### Series 计算,描述性统计
- [[Series.factorize()]]  分类数据编码
```python
Series.abs()  # 绝对值
Series.clip([lower, upper, axis, inplace])  # 修剪值至[lower, upper]
Series.diff(periods=1)  # 每个元素与前periods个元素的差
Series.pct_change([periods, fill_method, ...])  # 每个元素与前periods个元素的变化百分比。

'''基本统计分析'''
Series.describe([percentiles, include, exclude])  # 描述统计
Series.count()  # 计数，非 NA/null 值
Series.value_counts([normalize, sort, ...])  # 返回一个包含每个唯一值及其计数
Series.kurt([axis, skipna, numeric_only])  # 无偏峰度
Series.max([axis, skipna, numeric_only])  # 最大值
Series.mean([axis, skipna, numeric_only])  # 平均值
Series.median([axis, skipna, numeric_only])  # 中位数
Series.min([axis, skipna, numeric_only])  # 最小值
Series.mode([dropna])  # 众数
Series.nlargest([n, keep])  # 最大的n个数
Series.nsmallest([n, keep])  # 最小的n个数
Series.skew([axis, skipna, numeric_only])  # 无偏斜
Series.std([axis, skipna, ddof, numeric_only])  # 标准差
Series.var([axis, skipna, ddof, numeric_only])  # 方差
Series.kurtosis([axis, skipna, numeric_only])  # 无偏峰度
Series.unique()  # 唯一值
Series.quantile([q, interpolation])  # 分位数
Series.rank([axis, method, numeric_only, ...])  # 排序(1到n)
Series.sem([axis, skipna, ddof, numeric_only])  # 平均值的无偏标准误差
Series.nunique([dropna])  # 返回 Series 对象的唯一值的数量，排除 NA 值

'''累计统计分析'''
Series.cummax([axis, skipna])  # 累积最大值
Series.cummin([axis, skipna])  # 累积最小值
Series.cumprod([axis, skipna])  # 到前元素的累积乘
Series.cumsum([axis, skipna])  # 到前元素的累积和
Series.sum([axis, skipna, numeric_only, ...])  # 求和
Series.prod([axis, skipna, numeric_only, ...])  # 累积乘

'''布尔判断'''
Series.all([axis, bool_only, skipna])  # 全真判断
Series.any(*[, axis, bool_only, skipna])  # 存在真判断
Series.between(left, right[, inclusive])  # left <= series <= right 判断
Series.is_unique  # 唯一判断，返回布尔值
Series.is_monotonic_increasing  # 单调递增判断，返回布尔值
Series.is_monotonic_decreasing  # 单调递减判断，返回布尔值
	
'''相关分析'''
Series.autocorr([lag])  # 计算滞后 N 自相关
Series.corr(other[, method, min_periods])  # 相关系数，不包括缺失值
Series.cov(other[, min_periods, ddof])  # 协方差，不包括缺失值
```