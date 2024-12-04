##### 异步生成器
- 异步生成器（Async Generator）是一种特殊类型的生成器，用于在异步代码中生成序列化的值。与普通生成器一样，异步生成器也使用 `yield` 语句来产生值，但它允许在生成值的过程中进行异步操作。
- 通过使用异步生成器，可以在生成值的同时执行异步操作，例如异步网络请求、文件读写等。
```python
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # 模拟异步操作
        yield i

async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())

```