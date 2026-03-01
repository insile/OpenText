##### asyncio.任务
- 任务
	- 任务用于**封装协程**，并将其添加到事件循环中以进行调度和执行。它是一种用于管理和控制异步操作的对象。
	- 任务类型用于表示一个正在执行的协程。每个 任务 都与一个协程相关联，并且可以通过事件循环来调度和执行。Task 的状态可以是运行中、等待中或已完成。
	- **多个 任务 可以同时在事件循环中并发执行**，从而实现并发性和并行性。这对于处理多个异步操作非常有用，例如同时发起多个网络请求
	- 当你使用 `await` 关键字等待一个任务时，实际上是等待任务对象的执行结果。任务对象内部封装了一个协程，事件循环可以在后台并发地执行这个协程。因此，`await` 一个任务不会阻塞事件循环，而是会让事件循环继续处理其他可执行的任务，实现了并发执行的效果。
##### 示例
```python
import asyncio  

async def custom_coro(people):
    print(f"{people}号客人: 点餐")
    await asyncio.sleep(1)  # 等待另一协程
    print(f"{people}号客人: 拿餐")
 
async def main():  
    task_1 = asyncio.create_task(custom_coro(1))  # 创建任务  A
    task_2 = asyncio.create_task(custom_coro(2))  # 创建任务  B
    await task_1  # 等任务完成  
    await task_2  # 等任务完成  

asyncio.run(main())

# 并行任务
# 1号客人: 点餐  
# 2号客人: 点餐  
# 1号客人: 拿餐  
# 2号客人: 拿餐
```
