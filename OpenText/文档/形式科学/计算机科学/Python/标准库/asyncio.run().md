##### asyncio.run()
- `asyncio.run(coro, *, debug=None)`
	- 用于运行一个协程，作为异步程序的入口点。它会自动创建一个新的事件循环，执行指定的协程，并在协程完成后关闭事件循环，确保程序正确运行。`3.7`
	- `coro`：要运行的协程对象（coroutine）。
	- `debug`：用于设置事件循环的调试模式。
```python
import asyncio

async def main(people):
    print(f"{people}号客人: 点餐")
    await asyncio.sleep(1)  # 等待另一协程
    print(f"{people}号客人: 拿餐")

asyncio.run(main(1))
```
##### 注意
- 在同一程序中，应该只调用一次 `asyncio.run()` 函数来启动整个异步程序，因为它会创建一个新的事件循环并在协程完成后关闭它。
- 如果在已有的事件循环中运行协程，可以使用 `await` 来执行协程，而不是使用 `asyncio.run()`。`asyncio.run()` 主要用于简化启动异步程序的过程。
- 在Python 3.7之前的版本中，如果需要使用 `asyncio`，则需要手动创建和管理事件循环。`asyncio.run()` 是在3.7版本中引入的，使得启动异步程序更加方便。

