##### class asyncio.Runner
- `Runner.说明`
	- 对在相同上下文中多个异步函数调用进行简化的上下文管理器。`3.11`
- `Runner.创建`
```python
asyncio.Runner(*, debug=None, loop_factory=None)
```
- `Runner.实例方法`
```python
Runner.run(coro, *, context=None)
# 在嵌入的循环中运行一个 协程 coro。

Runner.close()
# 关闭运行器。

Runner.get_loop()
# 返回关联到运行器实例的事件循环。
```
##### 示例
```python
import asyncio

async def main(people):  
    print(f"{people}号客人: 点餐")  
    await asyncio.sleep(1)  # 等待另一协程  
    print(f"{people}号客人: 拿餐")

with asyncio.Runner() as runner:
	runner.run(main(1))
```