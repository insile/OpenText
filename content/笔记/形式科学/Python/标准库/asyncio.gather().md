##### asyncio.gather()
- `awaitable asyncio.gather(*aws, return_exceptions=False)`
	- `asyncio.gather()` 函数用于同时运行多个可等待对象（awaitable objects），并等待它们全部完成。它返回一个包含所有可等待对象的结果的列表。这些可等待对象可以是协程、任务、Future 对象等。
	- `*aws`：一个可变数量的可等待对象（协程、任务等）。你可以传递一个或多个可等待对象作为参数。
	- `return_exceptions`：一个可选参数，如果设置为 `True`，则在等待期间抛出的异常将被收集并放在结果列表中；如果设置为 `False`（默认值），则遇到异常时整个 `asyncio.gather()` 调用将被中断。
	- 该函数返回一个协程（`coroutine`），在调用这个协程时，它会并发地运行传递的可等待对象，并等待它们全部完成。最终返回一个包含所有可等待对象的结果的列表。

```python
import asyncio

async def coro1(people):
    print(f"{people}号客人: 点中餐")
    await asyncio.sleep(1)  # 模拟等待另一制作协程
    print(f"{people}号客人: 拿中餐")
    return f"{people}号客人: 中餐完成"

async def coro2(people):
    print(f"{people}号客人: 点西餐")
    await asyncio.sleep(1)  # 模拟等待另一制作协程
    print(f"{people}号客人: 拿西餐")
    return f"{people}号客人: 西餐完成"

async def main():
    results = await asyncio.gather(coro1(1), coro2(2))
    print("Results:", results)

asyncio.run(main())
```
