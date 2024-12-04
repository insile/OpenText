##### Series 索引,迭代,选择,标签
- [[Series.align()]]  对齐列
- [[Series.reindex()]]  重新索引
- [[Series.reset_index()]]  重置索引，默认将索引提出为列
```python
Series.pop(item)
	# 返回并删除行
Series.items()
	# 将 Series 行作为 (index, value) 进行迭代
Series.head(n=5)
	# 返回前 n 行
Series.tail(n=5)
	# 返回最后 n 行
Series.isin(values)
	# Series 中的元素是否包含在值中，返回布尔值
Series.equals(other)
	# 两个 Series 是否相等

Series.filter(items=None, like=None, regex=None, axis=None)
	# 行列标签筛选
Series.drop(labels)
	# 删除行标签返回新序列
Series.drop_duplicates(*, keep='first', inplace=False, ignore_index=False)
	# 删除重复值返回新序列
Series.duplicated(keep='first')
	# 返回布尔Series，标记重复值为True。
	# first 标记第一次出现后。last 标记最后一次之前的。False 标记所有

Series.idxmax([axis, skipna])
	# 最大值标签
Series.idxmin([axis, skipna])
	# 最小值标签

Series.sample([n, frac, replace, weights, ...])
	# 抽样

Series.add_prefix(prefix[, axis])
	# 标签加前缀
Series.add_suffix(suffix[, axis])
	# 标签加后缀

Series.truncate(before, after)
	# 在某个索引值之前和之后截断 Series 

Series.mask(cond, other=_NoDefault.no_default, *, inplace=False, axis=None, level=None)
	# 替换条件 cond 为 False 的值为 other
Series.mask(cond, other=_NoDefault.no_default, *, inplace=False, axis=None, level=None)
	# 替换条件 cond 为 True 的值为 other
```
##### DataFrame 索引,迭代,选择,标签
- [[DataFrame.xs()]]  交叉索引
- [[DataFrame.set_index()]]  使用现有列设置索引
- [[DataFrame.query()]]  布尔查询
- [[DataFrame.insert()]]  插入列
- [[DataFrame.drop()]]  从行或列中删除指定的标签
