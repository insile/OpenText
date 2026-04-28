##### for 语句
- for 语句
	- 循环语句，按照一定次数循环执行一组语句
	- 用于遍历[[py.迭代器对象|可迭代对象]]，按顺序逐个访问其中的元素，从而对每个元素执行相应的操作
	- for 循环本质就是调用[[py.迭代器对象|可迭代对象]]的[object.\_\_iter\_\_()](py.object.__iter__().md)方法获得一个迭代器，然后不断调用迭代器[object.\_\_next\_\_()](py.object.__next__().md)方法实现的
	- [[py.for|for]]
```python
# for 语句形式
'''
for 变量 in 可迭代对象
	循环体
'''

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```
- 结合函数[[py.range()|range()]]，循环计数控制
```python
'''
for 变量 in range()
	循环体
'''

for i in range(5):
    print(i)

for _ in range(5):
    # 循环5次，但不用这个变量_
```
