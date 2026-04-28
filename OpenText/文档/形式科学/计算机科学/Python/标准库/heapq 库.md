##### heapq 库
- 这个模块提供了堆队列算法的实现，也称为优先队列算法。
- 适用于**需要高效地处理最小/最大元素的场景**，例如任务调度、数据流中的滑动窗口等。它提供了一种轻量级的实现方式来处理堆队列，可以在一些特定场景中提供性能优势。
- [[heapq.堆排序]]
```python
import heapq
```
##### heapq 主要API
```python 
# 可以使用列表调用下列方法，也可以通过heapq.heapify(x)
heapq.heapify(x)
# 将list x 转换成堆，原地，线性时间内。

heapq.heappush(heap, item)
# 将 item 的值加入 heap 中，保持堆的不变性。

heapq.heappop(heap)
# 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。  

heapq.heappushpop(heap, item)
# 将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。
  
heapq.heapreplace(heap, item)  
# 弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。  

# 这个单步骤操作比 heappop() 加 heappush() 更高效，并且在使用固定大小的堆时更为适宜。 pop/push 组合总是会从堆中返回一个元素并将其替换为 item。

# 返回的值可能会比添加的 item 更大。 如果不希望如此，可考虑改用 heappushpop()。 它的 push/pop 组合会返回两个值中较小的一个，将较大的值留在堆中。
```
