##### class concurrent.futures.Executor
- 抽象基类提供异步执行调用方法。要通过它的子类调用，而不是直接调用。
```python
Executor.submit(fn, /, *args, **kwargs)
# 调度可调用对象 fn
# 以 fn(*args, **kwargs) 方式执行
# 返回一个代表该可调用对象的执行的 Future 对象
# 适用于需要对每个任务进行个性化控制，或者需要立即获取单个任务的执行结果的场景

Executor.map(func, *iterables, timeout=None, chunksize=1)
# 类似于 map(func, *iterables) 函数，除了以下两点：
# iterables 是立即执行而不是延迟执行的；
# func 是异步执行的，对 func 的多个调用可以并发执行。
# 适用于需要对一个可迭代对象中的每个元素执行相同的任务，并且希望一次性获取所有任务的执行结果的场景

Executor.shutdown(wait=True, *, cancel_futures=False)
# 等待执行完成后关闭调用释放资源, 使用with避免显式使用
```
- 上下文管理器对象
```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(name: str):
    """
    定义一个任务函数，接受一个名称参数，并打印任务执行的步骤。
    :param name: str, 任务名称
    :return: str, 任务完成消息
    """
    print(f'{name} 点餐\n', end='')
    time.sleep(1) 
    print(f'{name} 拿餐\n', end='')
    return f'{name} 完成'


# 创建一个 ThreadPoolExecutor 对象，并使用 submit() 方法提交任务
with ThreadPoolExecutor() as execute:
    r1 = execute.submit(task, 'A')  # 返回 Future 
    r2 = execute.submit(task, 'B')
    print('继续运行')
	# 线程池内继续运行
	
print('等待结束')
# 线程池外等待shutdown


# A 点餐
# B 点餐
# 继续运行
# B 拿餐
# A 拿餐
# 等待结束
```