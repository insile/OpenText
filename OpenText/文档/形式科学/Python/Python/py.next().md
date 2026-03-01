##### next()
- `next( iterator [, default] )`
	- 返回[[py.迭代器对象|迭代器对象]]下一个项目
	- 如果给出`default`，则在迭代器耗尽时返回，否则引发[[py.异常类型|StopIteration]]
```python
a = [1,2,3,4]
b = iter(a)
next(b)  # 1
next(b)  # 2
next(b)  # 3
next(b)  # 4
next(b,'None')  # None
```