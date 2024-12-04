##### 滑动窗口方法
```python 
Rolling.sum()
Rolling.mean()
Rolling.var()
Rolling.sum()
Rolling.std()
Rolling.min()
Rolling.max()
Rolling.apply(func, raw=False, engine=None, engine_kwargs=None, args=None, kwargs=None)
	#传入对应窗口的Series进行func计算
```
##### 扩张窗口计算
```python
Expanding.count([numeric_only])
Expanding.sum([numeric_only, engine, ...])
Expanding.mean([numeric_only, engine, ...])
Expanding.median([numeric_only, engine, ...])
Expanding.var([ddof, numeric_only, engine, ...])
Expanding.std([ddof, numeric_only, engine, ...])
Expanding.min([numeric_only, engine, ...])
Expanding.max([numeric_only, engine, ...])
Expanding.corr([other, pairwise, ddof, ...])
Expanding.cov([other, pairwise, ddof, ...])
Expanding.skew([numeric_only])
Expanding.kurt([numeric_only])
Expanding.apply(func[, raw, engine, ...])
Expanding.aggregate(func, *args, **kwargs)
Expanding.quantile(quantile[, ...])
Expanding.sem([ddof, numeric_only])
Expanding.rank([method, ascending, pct, ...])
```
##### 指数加权移动窗口
```python
ExponentialMovingWindow.mean([numeric_only, ...])
ExponentialMovingWindow.sum([numeric_only, ...])
ExponentialMovingWindow.std([bias, numeric_only])
ExponentialMovingWindow.var([bias, numeric_only])
ExponentialMovingWindow.corr([other, ...])
ExponentialMovingWindow.cov([other, ...])
```