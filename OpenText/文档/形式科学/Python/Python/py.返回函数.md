##### 返回函数
- 返回函数
	- 返回函数指一个函数返回值为函数
```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

a = lazy_sum(1,2,3)
a()

Out:6
```