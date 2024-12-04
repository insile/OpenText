##### enumerate()
- `enumerate( iterable, start=0 )`
	- 返回一个枚举对象, 是[[py.迭代器对象|迭代器对象]]
	- 将[[py.迭代器对象|可迭代对象]]每个元素及其元素下标组合为一个元组，将这些元组组合成列表，下标从`start`开始
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']  

list(enumerate(seasons))  
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]  

list(enumerate(seasons, start=1)) 
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```