##### class collections.Counter 计数器
- 实例化方法
```python
collections.Counter([iterable-or-mapping])
	# Counter 是 dict 的子类，用于计数 hashable 对象
	# 支持所有常用字典方法
	# 支持常见的集合操作，如相加、相减、交集、并集等
```
- 实例方法
```python
Counter.elements()
# 返回一个迭代器，其中每个元素将重复出现计数值所指定次
# 元素会按首次出现的顺序返回
# 如果一个元素的计数值小于1，elements() 将会忽略它
# c = Counter(a=4, b=2, c=0, d=-2)
# sorted(c.elements())  # ['a', 'a', 'a', 'a', 'b', 'b']

Counter.most_common([n])
# 返回一个列表，其中包含 n 个最常见的元素及出现次数，按常见程度由高到低排序
# 如果 n 被省略或为 None，将返回所有元素
# 计数值相等的元素按首次出现的顺序排序
# Counter('abracadabra').most_common(3)  # [('a', 5), ('b', 2), ('r', 2)]

Counter.subtract([iterable-or-mapping])
# 减去一个 iterable-or-mapping 中的元素。输入和输出都可以是 0 或负数。
# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d)
# c  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

Counter.total()
# 计算总计数值
# c = Counter(a=10, b=5, c=0)
# c.total()  # 15

# 运算符
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
# Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
# Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x])
# Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
# Counter({'a': 3, 'b': 2})
c == d                      # equality:  c[x] == d[x]
# False
c <= d                      # inclusion:  c[x] <= d[x]
# False
```
##### 示例
```python
from collections import Counter

# 创建 Counter 对象
data = [1, 2, 3, 1, 2, 1, 3, 4, 5, 5, 5]
counter = Counter(data)

print(counter)            # Counter({1: 3, 2: 2, 3: 2, 5: 3, 4: 1})
print(counter[1])         # 3，元素 1 出现的次数
print(counter[5])         # 3，元素 5 出现的次数

# 获取出现频率最高的元素
print(counter.most_common(2))  # [(1, 3), (5, 3)]

# 计算元素总数
print(sum(counter.values()))   # 11

# 两个 Counter 对象相加
other_counter = Counter([1, 2, 2, 3, 3, 3])
combined_counter = counter + other_counter
print(combined_counter)        # Counter({1: 4, 3: 5, 2: 4, 5: 3, 4: 1})

# 两个 Counter 对象相减
subtracted_counter = counter - other_counter
print(subtracted_counter)      # Counter({1: 2})

```