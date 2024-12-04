##### copy.浅拷贝和深拷贝
```python
import copy

list1 = [[1, 2], (30, 40)]
list3 = copy.copy(list1)     # 浅拷贝
list2 = copy.deepcopy(list1)  # 深拷贝
 
list1[0].append(100)   # 子元素添加值
print("list1:", list1)  # list1 变
# [[1, 2, 100], (30, 40)]
print("list3:", list3)  # 浅拷贝是存储原对象的子对象的引用，所以跟着改变
# [[1, 2, 100], (30, 40)]
print("list2:", list2)  # 深拷贝以后和list1没有关系，list2不变
# [[1, 2], (30, 40)]
```