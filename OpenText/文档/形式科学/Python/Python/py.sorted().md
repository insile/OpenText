##### sorted()
- `sorted( iterable, *, key=None, reverse=False )`
	- 对[[py.迭代器对象|可迭代对象]]排序，返回[[py.列表|列表]]
	- `iterable` 要排序的可迭代对象
	- `key` 可选参数，用于指定一个函数，用于从每个元素中提取用于排序的键。默认为 None
	- `reverse` 可选参数，如果为 True，则以降序排序。默认为 False
	- 嵌套对象内先比较第一个值，值小的在前。如果相等就比较下一个值
```python
# iterable
numbers = [5, 2, 8, 1, 10]
result = sorted(numbers)
print(result)  # 输出：[1, 2, 5, 8, 10]
# key
words = ["apple", "banana", "cherry"]
result = sorted(words, key=len)
print(result)  # 输出：['apple', 'banana', 'cherry']
# reverse
result = sorted(numbers, reverse=True)
print(result)  # 输出：[10, 8, 5, 2, 1]

# 先按照成绩降序排序，相同成绩的按照名字升序排序：
d1 = [{'name':'alice', 'score':38}, 
	  {'name':'bob', 'score':18}, 
	  {'name':'darl', 'score':28}, 
	  {'name':'christ', 'score':28}]
l = sorted(d1, key=lambda x:(-x['score'], x['name']))
print(l)
	'''
	[{'name': 'alice', 'score': 38}, 
	 {'name': 'christ', 'score': 28}, 
	 {'name': 'darl', 'score': 28}, 
	 {'name': 'bob', 'score': 18}]
	'''


# 正数在前负数在后，正数从小到大，负数从大到小
# 使用lambda生成元组，元组第一个数为负数判断值，第二个数为绝对值
list1 = [7, -8, 5, 4, 0, -2, -5]
list2 = sorted(list1,key=lambda x:(x<0, abs(x)))
print(list2) 
	'''
	[0,4,5,7,-2,-5,-8]
	'''
```