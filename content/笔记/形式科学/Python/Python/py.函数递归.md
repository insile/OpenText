##### 函数递归
- 函数递归
	- 递归是一种在函数内部调用自身的编程技术
	- 在递归过程中，函数通过不断地调用自身来解决问题，直到达到某个基本条件，然后逐步返回结果。递归在解决一些问题时可以非常简洁和优雅，但也需要注意避免无限递归和性能问题。
	- 递归函数通常包括两部分：基本情况（基准情况）和递归情况。基本情况是指可以直接求解的问题，而递归情况是指将问题分解为更小的子问题，并通过递归调用函数来解决这些子问题。
```python
# n 的阶乘递归
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(result)  # 输出：120

# n 项斐波那契数列递归
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 计算斐波那契数列的前 10 项
for i in range(10):
    print(fibonacci(i), end=" ")
```
