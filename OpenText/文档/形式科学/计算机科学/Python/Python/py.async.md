##### async
- `async def`
	- 指定一个函数为[[asyncio.协程|协程]]，使用 [[py.await|await]] 关键字来等待异步操作的结果
	- 结合 [[py.yield|yield]] 定义一个[[py.异步生成器|异步生成器]]
- `async for`
	- [[py.异步迭代器|异步迭代器]]，可以在其 `__anext__` 方法中调用异步代码。
- `async with`
	- [[py.异步上下文管理器|异步上下文管理器]]，可以在协程的进入和退出时执行异步操作，以确保资源在正确的时间被获取和释放。
- [[asyncio 库|asyncio 库]]
```python
import asyncio
import time

async def say_after(delay, what): # 子协程
    await asyncio.sleep(delay)
    print(what)

async def main(): # 主协程
    print(f"started at {time.strftime('%X')}")

	# 主协程挂起，等待子协程
    await say_after(1, 'hello') # 等待子协程
    await say_after(2, 'world') # 等待子协程

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
# 事件循环处理主协程
```

