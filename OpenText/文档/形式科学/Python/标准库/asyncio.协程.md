##### 协程
- 协程
	- 协程是一种特殊的函数，可以在执行过程中被挂起并暂停，然后在需要的时候恢复执行。协程的使用能够实现异步编程，避免了阻塞，提高了程序的并发性能。协程对象只能在事件循环运行时运行
	- 在Python中，使用 [[py.async|async def]] 关键字来定义一个协程函数，而在协程函数中，使用 [[py.await|await]] 关键字来等待异步操作的结果
	- 当你直接使用 `await` 关键字等待一个协程时，事件循环会阻塞在这个协程上，直到这个协程执行完成为止。这意味着，后续的代码需要等待这个协程执行完成后才能继续执行，因此不能并发执行其他任务
```python
# 定义一个协程
async def custom_coro(people):
    print(f"{people}号客人: 点餐")
    await asyncio.sleep(1)  # 等待另一协程
    print(f"{people}号客人: 拿餐")
 
# 创建协程对象，没有运行
coro = custom_coro(1)
print(type(coro))
# <class 'coroutine'>

# 创建主协程
async def main(people):  
    await custom_coro(1)  # 等待另一协程  
    await custom_coro(2)  # 等待另一协程  

# 创建事件循环运行主协程
asyncio.run(main(1))

# 没有并行
# 1号客人: 点餐  
# 1号客人: 拿餐  
# 2号客人: 点餐  
# 2号客人: 拿餐
```

