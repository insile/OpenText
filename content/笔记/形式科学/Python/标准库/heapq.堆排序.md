##### heapq.堆排序
- 在这个案例中，我们定义了一个 heap_sort 函数，它接受一个列表作为输入，并使用 heapq 模块中的函数将输入列表转化为堆（最小堆）
- 然后，我们循环地从堆中弹出最小元素，直到堆为空，这样就得到了一个按照升序排列的有序列表。
```python
import heapq

def heap_sort(arr):
    heap = arr[:]
    heapq.heapify(heap)  # 将列表转化为堆

    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))  # 弹出堆中最小元素

    return sorted_list

if __name__ == "__main__":
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = heap_sort(input_list)
    print("Original List:", input_list)
    print("Sorted List:", sorted_list)

```