##### aiohttp.客户端
- [[aiohttp.简单框架]]
- [[class aiohttp.ClientSession]]  客户端会话
- [[class aiohttp.ClientResponse]]  客户端响应
##### 示例
```python
# 异步请求
import asyncio
import time
import aiohttp

async def async_http():
	# 协程
    async with aiohttp.ClientSession() as session:
        # 声明一个支持异步的上下文管理器客户端会话
        res = await session.get('http://httpbin.org/delay/2')  # 等待GET响应
        print(f'当前时间：{time.ctime()}, status_code = {res.status}')

tasks = [async_http() for _ in range(5)]  # 5个协程
start = time.time()  # 开始时间
asyncio.run(asyncio.wait(tasks))  # 创建事件循环等待一组5个协程完成
print(f'aiohttp异步耗时：{time.time() - start}')


# 同步请求
import time
import requests

def main():
    start = time.time()
    for i in range(5):
        res = requests.get('http://httpbin.org/delay/2')
        print(f'当前时间：{time.ctime()}, status_code = {res.status_code}')
    print(f'requests同步耗时：{time.time() - start}')

main()
```