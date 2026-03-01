##### asyncio.wait_for()
- `coroutine asyncio.wait_for(aw, timeout)`
	- 在异步编程中，有时候我们希望在等待一个异步操作的完成时设置一个最大的等待时间，以防止某个操作耗时过长导致整个程序被阻塞。`asyncio.wait_for()` 用于在一个异步操作中等待一段指定的时间，如果操作在超时时间内未完成，就会引发超时异常。
	- `aw`：要等待的可等待对象（例如协程、`Future` 对象等）。
	- `timeout`：等待的最大时间，以秒为单位。可以是一个浮点数，表示小数秒，也可以是一个整数，表示整数秒。

```python
import asyncio

async def coro1(people):
    print(f"{people}号客人: 点中餐")
    await asyncio.sleep(5)  # 模拟等待另一制作协程
    print(f"{people}号客人: 拿中餐")


async def main():
    try:
        await asyncio.wait_for(coro1(1), timeout=3)
    except asyncio.TimeoutError:
        print("制作事件太长客人取消订单")

asyncio.run(main())

# 1号客人: 点中餐  
# 制作事件太长客人取消订单
```
