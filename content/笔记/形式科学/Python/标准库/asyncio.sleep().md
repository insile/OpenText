##### asyncio.sleep()
- `coroutine asyncio.sleep(delay, result=None)`
	- 用于在指定的时间内暂停协程的执行，从而模拟等待操作
	- 这个函数的作用类似于在同步代码中使用 `time.sleep()`，但在异步环境中使用它不会阻塞整个事件循环，而只会暂停当前协程的执行
	- `delay`：暂停的时间，以秒为单位。可以是一个浮点数，表示小数秒，也可以是一个整数，表示整数秒。
	- `result`：可选参数，表示协程完成后返回的结果。
```python
import asyncio

async def main(people):
    print(f"{people}号客人: 点餐")
    await asyncio.sleep(1)  # 异步等待
    print(f"{people}号客人: 拿餐")

asyncio.run(main(1))
```





