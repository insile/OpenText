##### 异步上下文管理器
- 异步上下文管理器 是 上下文管理器 的一种，它能够在其` __aenter__` 和 `__aexit__ `方法中暂停执行。
- 异步上下文管理器可在 [[py.async|async with|async|async with]] 语句中使用。
```pythoon
object.__aenter__(self)
	# 在语义上类似于 __enter__()，仅有的区别是它必须返回一个 可等待对象。

object.__aexit__(self, exc_type, exc_value, traceback)
	# 在语义上类似于 __exit__()，仅有的区别是它必须返回一个 可等待对象。
```
##### 示例
```python
import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource asynchronously")  # 1
        await asyncio.sleep(1)
        print("Resource acquired")  # 2
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Releasing resource asynchronously")  # 4
        await asyncio.sleep(1)
        print("Resource released")  # 5

async def main():
    async with AsyncResource() as resource:
        print("Using the resource asynchronously")  # 3
        await asyncio.sleep(2)

asyncio.run(main())

```