##### 集合方法
- 集合方法
```python
x in s  # 检测 x 是否为 s 中的成员
x not in s  # 检测 x 是否非 s 中的成员

s.isdisjoint(other)  # s不相交判断
s.issubset(other)  # s子集判断
s.issuperset(other)  # s父集判断

s.union(*s)  # 返回新集合，所有元素
s.intersection(*s)  # 返回新集合，相交元素
s.difference(*s)  # 返回新集合，原集合独有元素
s.symmetric_difference()  # 返回新集合，两者独有元素

s.add(x)  # 增加
s.discard(x)  # 移除x，不存在不会报错
s.remove(x)  # 移除x，不存在KeyError异常
s.clear()  # 移除所有元素
s.pop()  # 随机抽取一个元素，更新S，若S为空则KeyError异常
s.copy()  # 浅拷贝
s.update(*s)  # 更新集合，添加元素
s.intersection_update(*s)  # 更新集合，保留相交元素
s.difference_update(*s)  # 更新集合，保留s独有元素
s.symmetric_difference_update()  # 更新集合，保留两者独有元素

set <= other  # s子集判断
set < other  # s真子集判断
set >= other  # s父集判断
set > other  # s真父集判断
set | other | ...  # 返回新集合，所有元素
set & other & ...  # 返回新集合，相交元素
set - other - ...  # 返回新集合，原集合独有元素
set ^ other  # 返回新集合，两者独有元素
```