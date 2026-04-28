##### asyncio.事件循环
- 事件循环是协程运行环境
- [[asyncio.run()]]
- [[class asyncio.Runner]]
```python
import asyncio
 
# 第一个协程
async def task_coro1():
    print('正在运行第一个协程')
    await asyncio.sleep(1)

# 第二个协程
async def task_coro2():
    print('正在运行第二个协程')
    await asyncio.sleep(1)
 
# 结构1
asyncio.run(task_coro1())  # 创建第一个事件循环运行协程
asyncio.run(task_coro2())  # 创建第二个事件循环运行协程
# 这种方法的成本很高，因为必须为每个协程创建并关闭新的事件循环

# 结构2
async def main():
	# 创建主协程
    await task_coro1()  # 等待第一个协程
    await task_coro2()  # 等待第二个协程
asyncio.run(main())  # 创建一个事件循环运行协程
# 必须使用新的包装协程作为执行所有协程的入口点

# 结构3
with asyncio.Runner() as runner:
	# 事件循环上下文管理器
    runner.run(task_coro1())
    runner.run(task_coro2())
# 每个协程都在同一个事件循环中执行，并且直到第一次调用 run() 才会创建所使用的循环
```