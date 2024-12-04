##### 同步异步示例
- 同步
```python
import time

# 定义同步任务函数
def sync_task(name):
    print(f'点餐 {name}')
    time.sleep(1)  # 模拟同步任务的执行 制作餐品
    print(f'拿餐 {name}')

# 执行同步任务
for i in range(1, 6):
    sync_task(f'{i}')

# 点餐 1
# 拿餐 1
# 点餐 2
# 拿餐 2
# 点餐 3
# 拿餐 3
# 点餐 4
# 拿餐 4
# 点餐 5
# 拿餐 5
```
- 异步
```python
import asyncio

# 定义异步任务函数
async def async_task(name):
    print(f'点餐 {name}')
    await asyncio.sleep(1)  # 模拟异步任务的执行 制作餐品
    print(f'拿餐 {name}')

# 执行异步任务
async def main():
    tasks = [async_task(f'{i}') for i in range(1, 6)]
    await asyncio.gather(*tasks)

asyncio.run(main())

# 点餐 1
# 点餐 2
# 点餐 3
# 点餐 4
# 点餐 5
# 拿餐 1
# 拿餐 3
# 拿餐 5
# 拿餐 2
# 拿餐 4
```