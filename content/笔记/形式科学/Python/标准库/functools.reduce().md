##### functools.reduce()
- `functools.reduce(function, iterable[, initializer])`
	- 将两个参数的 `function` 从左至右积累地应用到 `iterable` 的条目
```python
from functools import reduce
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
#  ((((1+2)+3)+4)+5) = 15
```