##### yield
- `yield`
	- 创建[[py.生成器对象|生成器类型]]
	- 每次调用 [[py.next()|next()]] 的时候执行，遇到 `yield` 语句返回，再次执行时从上次返回的 `yield` 语句处继续执行
- `yield from` 
	- `yield from` 语句是在生成器函数中用于委托另一个生成器的一种方式
```python
# 生成形式
'''
yield 变量
'''

# 斐波那契数列 1 1 2 3 5 8 ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
	print(n)

# 拿返回值 'done'
g = fib(6)

while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# 简单的 yield from
def f1():
    yield from [1, 2, 3]

for i in f1():
    print(i)

# 复杂的 yield from
def sub_generator():
    yield 1
    yield 2
    yield 3

def main_generator():
    yield 'Start'
    yield from sub_generator()
    yield 'End'

gen = main_generator()
for value in gen:
    print(value)

```