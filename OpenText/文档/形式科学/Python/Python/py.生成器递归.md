##### 生成器递归
- 生成器递归
	- 生成器递归有两种 [[py.yield|yield from]] 递归 或者 [[py.yield|yield]] 递归, 需要手动在一个生成器中遍历另一个生成器, 并在每次遍历时使用 `yield` 将值传递出来, 区别于[[py.函数递归|函数递归]]
```python
# yield from 生成器递归
def increasing_generator(n):
    if n <= 0:
        return
    yield n
    yield from increasing_generator(n - 1)

increasing_gen = increasing_generator(5)  # 54321
for num in increasing_gen:
    print(num)


# yield 递归
def increasing_generator(n):
    if n <= 0:
        return
    yield n
    for i in increasing_generator(n - 1):
        yield i

increasing_gen = increasing_generator(5)  # 54321
for num in increasing_gen:
    print(num)
```
