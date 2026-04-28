##### asyncio.wait()
- `asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)`
	- 用于等待一组协程任务的完成
	- `aws`：一个可迭代的可等待对象集合，表示待等待的协程任务
	- `timeout`：等待的最长时间秒
	- `return_when`：等待结束的条件，默认值为 `ALL_COMPLETED`，表示等待所有任务完成后返回
	- `asyncio.wait()` 函数返回一个元组 `(done, pending)`，其中 `done` 是一个包含已完成的 Future 对象的集合，`pending` 是一个包含未完成的 Future 对象的集合。当 `return_when` 参数为 `FIRST_COMPLETED` 时，`done` 集合将包含至少一个已完成的 Future 对象
```python
import asyncio

async def coro1(people):
    print(f"{people}号客人: 点中餐")
    await asyncio.sleep(2)  # 模拟等待另一制作协程
    print(f"{people}号客人: 拿中餐")

async def coro2(people):
    print(f"{people}号客人: 点西餐")
    await asyncio.sleep(1)  # 模拟等待另一制作协程
    print(f"{people}号客人: 拿西餐")

async def main():
    # 创建协程任务
    task1 = asyncio.create_task(coro1(1))
    task2 = asyncio.create_task(coro2(2))
    task3 = asyncio.create_task(coro1(3))

    # 等待所有协程任务完成
    done, pending = await asyncio.wait([task1, task2, task3])

    # 输出已完成的任务信息
    for task in done:
        print(f"{task} 完成服务")

asyncio.run(main())

# 1号客人: 点中餐
# 2号客人: 点西餐
# 3号客人: 点中餐
# 2号客人: 拿西餐
# 1号客人: 拿中餐
# 3号客人: 拿中餐
```