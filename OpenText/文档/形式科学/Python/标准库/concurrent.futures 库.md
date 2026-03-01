##### concurrent.futures 库
- 用于并发执行任务的高级库
```python
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
```
##### concurrent.futures 主要API
- [[class concurrent.futures.Executor]] 抽象基类执行器
	- [[class concurrent.futures.ThreadPoolExecutor]] 线程池异步
	- [[class concurrent.futures.ProcessPoolExecutor]] 进程池异步
- [[class concurrent.futures.Future]] 结果
- [[concurrent.futures.wait()]] 等待
