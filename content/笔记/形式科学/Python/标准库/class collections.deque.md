##### class collections.deque 双向队列
- 实例化方法
```python
collections.deque(iterable , maxlen)
	# 双端操作： deque 支持在两端（左侧和右侧）进行添加和删除元素操作，这些操作的时间复杂度为 O(1)。
	# 有限长度： 可以通过指定 maxlen 参数来创建一个有限长度的 deque，当 deque 达到指定的最大长度时，新添加的元素将从另一端弹出。
	# 高效队列： 由于 deque 的底层实现使用了双向链表，它在添加和删除元素方面比普通列表表现更好，特别是在首尾操作频繁的情况下。
```
- 实例方法
```python
deque.append(x) # 添加 x 到右端
deque.appendleft(x) # 添加 x 到左端
deque.clear() # 移除所有元素，使其长度为0
deque.copy() # 创建一份浅拷贝
deque.count(x) # 计算 deque 中元素等于 x 的个数

deque.extend(iterable) # 扩展deque的右侧，通过添加iterable参数中的元素。
deque.extendleft(iterable) # 扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。

deque.index(x[, start[, stop]]) # 返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError。

deque.insert(i, x) # 在位置 i 插入 x 。如果插入会导致一个限长 deque 超出长度 maxlen 的话，就引发一个 IndexError。

deque.pop() # 移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发一个 IndexError。
deque.popleft() # 移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。

deque.remove(value) # 移除找到的第一个 value。 如果没有的话就引发 ValueError。

deque.reverse() # 将deque逆序排列。返回 None 。

deque.rotate(n=1) # 向右循环移动 n 步。 如果 n 是负数，就向左循环。
```
##### 示例
```python
from collections import deque

# 创建一个空的 deque
d = deque()

# 在右侧添加元素
d.append(1)
d.append(2)
d.append(3)

# 在左侧添加元素
d.appendleft(0)

print(d)  # deque([0, 1, 2, 3])

# 弹出右侧元素
print(d.pop())  # 3

# 弹出左侧元素
print(d.popleft())  # 0

print(d)  # deque([1, 2])
```