##### class asyncio.TaskGroup
- `Task.说明`
	- 持有一个任务分组的[[py.异步上下文管理器|异步上下文管理器]]
	- 可以使用 `TaskGroup.create_task()` 将任务添加到分组中
	- 当该上下文管理器退出时所有任务都将被等待
##### 示例
```python
import asyncio

# 次协程
async def worker(task_group, i):
    await asyncio.sleep(i)
    await task_group.status("任务 {} 完成".format(i))

# 主协程
async def main():
	# 创建一个任务组
    async with asyncio.TaskGroup() as tg:
        # 循环创建任务
        for i in range(3):
            tg.create_task(worker(tg, i))
	# 任务组结束所有任务都将被等待
    
    print("所有任务完成")

asyncio.run(main())

```
