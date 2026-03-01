##### class asyncio.Task
- `Task.说明`
	- [[asyncio.任务]]
- `Task.创建`
```python
asyncio.create_task(coro, *, name=None, context=None)
# `coro`：要转换为任务的协程（或可等待对象）。
# `name`：可选参数，指定任务的名称。这个名称可以在调试和日志记录时使用，以便标识任务。
# `context`：可选参数，设置任务的上下文。上下文可以是一个字典，其中包含与任务关联的上下文信息。
```
- `Task.实例方法`
```python
Task.done()
# 如果 Task 对象 已完成 则返回 True

Task.cancel(msg=None)
# 请求取消 Task 对象
```
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