##### aiohttp.简单框架
```python
import aiohttp  
import asyncio  
  
  
async def process_page(kw):  
    # 中心协程 主要逻辑  
    async with aiohttp.ClientSession() as session:  # 会话  
        html = await get_html(session, kw)  # 请求协程  
        data = await process_html(html)  # 解析协程  
        await out_data(data, kw)  # 输出协程  
  
  
async def get_html(session, kw):  
    # 请求协程  
    url = "http://www.baidu.com/s"  
    params = {  
        'wd': kw,  # 搜索关键词  
        'ie': 'utf-8',  
    }  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',  
        'Connection': 'keep-alive',  
    }  
    async with session.request('GET', url, headers=headers, params=params) as response:  
        return await response.text(encoding='utf-8')  
  
  
async def process_html(html):  
    # 解析协程  
    return html[0:100]  
  
  
async def out_data(data, kw):  
    # 输出协程  
    print(kw, '\n', data)  
  
  
async def main():  
    # 主协程  
    kws = ['python', 'c', 'java']  # 关键字列表  
  
    tasks = []  
    for kw in kws:  
        tasks.append(asyncio.create_task(process_page(kw)))  # 构建url处理任务  
    results = await asyncio.gather(*tasks)  # 开始并等待任务完成  
  
  
asyncio.run(main())  # 事件循环主协程
```