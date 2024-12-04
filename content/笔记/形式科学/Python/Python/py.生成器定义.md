##### 生成器定义
- 生成器定义
	- 生成器定义使用[[py.生成器表达式|生成器表达式]]或者[[py.yield|yield 语句]]
```python
# 生成器表达式
generator=(x * x for x in range(10))

# 生成器函数
def generator():
    yield 1
    yield 2
    yield 3
for n in generator():
	print(n)
```