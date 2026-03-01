##### itertools 库
- 本模块实现一系列迭代器
```python
import itertools
```
##### itertools 主要API
```python
# 无穷迭代器：
itertools.count( start [,step] )
	# count(10) --> 10 11 12 13 14 ...
itertools.cycle(p)
	# cycle('ABCD') --> A B C D A B C D ...
itertools.repeat(elem [,n] )
	# repeat(10, 3) --> 10 10 10

# 根据最短输入序列长度停止的迭代器：
itertools.accumulate(	p [, func, *, initial=None ] )
	# accumulate([1,2,3,4,5]) --> 1 3 6 10 15
	# func为双目运算函数，initial为起始值
itertools.chain(p, q, ...)
	# chain('ABC', 'DEF') --> A B C D E F
itertools.compress(data, selectors)
	# compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
itertools.dropwhile(predicate, iterable)
	# dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
	# 去掉第一个 False 之前的元素，保留后面所有元素
itertools.filterfalse(predicate, iterable)
	# filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
	# 只返回 iterable 中 predicate 为 False 的元素
itertools.groupby(iterable, key=None)
	# 先按 key 排序 sorted，再按 key 结果值分组
itertools.pairwise(iterable)
	# pairwise('ABCDEFG') --> AB BC CD DE EF FG
itertools.starmap(function, iterable)
	# starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
itertools.takewhile(predicate, iterable)
	# takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
	# 返回真值，遇到第一个错误停止
itertools.zip_longest(*iterables, fillvalue=None)
	# zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
	# 创建一个迭代器，从每个可迭代对象中收集元素。
	# 长度未对齐，将根据 fillvalue 填充缺失值。

# 排列组合迭代器：
product(*iterables, repeat=1)
	# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
	# 元组表示组合，存在列表中
	# 笛卡尔积
	
permutations(iterable, r=None)
	# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
	# 排列
	
combinations(iterable, r)
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# 组合

combinations_with_replacement(iterable, r)
	# combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
	# 允许重复的组合
```
