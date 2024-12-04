##### 类型注解支持
- 基础类型注解
	- typing 库
	- collections.abc 库
```python
# 任何类型
x: any = 1

# 简单类型
x: int = 5
x: float = 3.14
x: bool = True
x: str = "John"
x: complex = 1+2j

# 容器类型
x: list[int] = [1, ]
x: list[int,...] = [1, 2, 3, 4, 5]
x: tuple[float, float] = (3.5, 4.2)
x: dict[str, int] = {'a': 2}

# 可选类型
from typing import Optional
x: Optional[int] = None
x: Optional[int] = 2

# 联合类型
from typing import Union
x: Union[str, float, complex] = 1
x: int | float | complex = 1
x: int | float | complex = 1.1
x: int | float | complex = 1+2j

# 可调用对象
from collections.abc import Callable
x: Callable[[int, int], int] = func

# 可迭代对象
from collections.abc import Iterable
def x(items: Iterable[int]) -> int:
	pass

# 迭代器
from collections.abc import Iterator
def x(start: int) -> Iterator[int]:
	pass

# 生成器
# Generator[YieldType, SendType, ReturnType]
from collections.abc import Generator
def x() -> Generator[int, float, str]:
	pass

```
