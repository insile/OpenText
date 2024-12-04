##### queue 库
- `queue`模块提供了多种队列实现，用于在多线程编程中进行线程安全的队列操作
- [[queue.消息队列]]
```python
import queue
```
##### queue 主要API
- `class queue.Queue(maxsize=0)` 先进先出队列类
- `class queue.LifoQueue(maxsize=0)` 先进后出队列类
- `class queue.PriorityQueue(maxsize=0)` 优先级队列类
```python
# 通用实例方法
Queue.qsize()
# 返回队列的大致大小

Queue.empty()
# 如果队列为空，返回 True ，否则返回 False

Queue.full()
# 如果队列是满的返回 True ，否则返回 False 

Queue.put(item, block=True, timeout=None)
# 将 item 放入队列
# block = False, 一旦队列中没有空位以将对象放入队列中, 直接报错
# block = true, timeout = None，阻塞至有空闲空间可用
# 如果 timeout 是个正数，将最多阻塞 timeout 秒，如果在这段时间没有可用的空闲插槽，将引发 Full 异常。反之 (block 是 false)，如果空闲插槽立即可用，则把 item 放入队列，否则引发 Full 异常 (在这种情况下，timeout 将被忽略)。 

Queue.get(block=True, timeout=None)
# 从队列中移除并返回一个项目
# block = False, 一旦队列中没有项目提取, 直接报错
# block = true, timeout = None，阻塞至项目可得到
# 如果 timeout 是个正数，将最多阻塞 timeout 秒，如果在这段时间内项目不能得到，将引发 Empty 异常。反之 (block 是 false) , 如果一个项目立即可得到，则返回一个项目，否则引发 Empty 异常 (这种情况下，timeout 将被忽略)。

```