##### concurrent.futures.wait()
- `concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED)`
	- 等待 `fs:iterable[Future]` 完成
	- 最大等待 `timeout ` 秒
	- `return_when` 指定此函数应在何时返回
		- `concurrent.futures.FIRST_COMPLETED` 任意一个任务完成
		- `concurrent.futures.FIRST_EXCEPTION` 任意一个任务异常
		- `concurrent.futures.ALL_COMPLETED` 所有任务都完成
	- 返回两个集合组成的元组,  第一个集合的名称为 done，包含在等待完成之前已完成的 future。 第二个集合的名称为 not_done，包含未完成的 future
```python
from concurrent.futures import ThreadPoolExecutor  
from concurrent.futures import wait  
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
    return f'{name} complete'  
  
# 创建一个 ThreadPoolExecutor 对象，并使用 submit() 方法提交任务  
with ThreadPoolExecutor() as execute:  
    r1 = execute.submit(task, 'A')  # 返回 Future    
    r2 = execute.submit(task, 'B')  
    done, not_done = wait([r1,r2])  # 等待
    print('完成')  
```