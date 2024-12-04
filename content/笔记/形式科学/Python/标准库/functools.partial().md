##### functools.partial()
- `functools.partial(func, /, *args, **keywords)`
	- 将函数 `func` 的部分参数 `args` `keywords` 固定, 并返回
```python
from functools import partial
basetwo = partial(int, base=2)  # 将int()的base固定为2并返回
basetwo('10010')  # 转为二进制
```

