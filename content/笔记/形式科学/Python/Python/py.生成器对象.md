##### 生成器对象
- 生成器对象 `Generator`
	- 生成器是一边循环一边计算的机制, 而不是一次性将所有值计算出来并存储在内存中, 是一种[[py.迭代器对象|迭代器]], 配合[[py.next()|next()]]和[[py.for 语句|for 语句]]使用, 支持[[py.生成器递归|生成器递归]]
- [[py.生成器定义|生成器定义]]
- [[py.生成器方法|生成器方法]]

```python
def generator():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3

g = generator()
next(g)
# a
# 1
# 运行到 yield 1 暂停

for i in generator():
    print(i)
# a
# 1
# b
# 2
# c
# 3
```
