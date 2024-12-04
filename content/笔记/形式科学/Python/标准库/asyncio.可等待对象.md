##### asyncio.可等待对象
- 如果一个对象可以在 [[py.await 表达式|await 表达式]] 中使用，那么它就是可等待对象。许多 asyncio API 都被设计为接受可等待对象。等待一个可等待对象，实际上是在等待这个对象的异步操作完成
	- [[asyncio.协程|协程]]
		- [[asyncio.sleep()]] 休眠
		- [[asyncio.wait()]] 等待一组
		- [[asyncio.wait_for()]] 带时间的等待
	- [[asyncio.任务|任务]]
		- [[class asyncio.Task]] 任务
		- [[class asyncio.TaskGroup]] 任务组
	- 其他
		- [[asyncio.gather()]] 等待一组
```python
await custom_coro(1)  # 等待一个协程

await asyncio.sleep(1)  # 等待休眠

await asyncio.wait([task1, task2, task3])  # 等待一组任务

await asyncio.wait_for(coro1(1), timeout=3)  # 带时间的等待

await asyncio.gather(coro1(1), coro2(2))  # 等待一组协程
```
