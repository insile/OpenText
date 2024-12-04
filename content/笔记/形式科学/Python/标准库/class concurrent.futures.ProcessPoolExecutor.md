##### class concurrent.futures.ProcessPoolExecutor
- 进程池异步
- `ProcessPoolExecutor.创建`
```python
ProcessPoolExecutor(max_workers=None, mp_context=None, initializer=None, initargs=(), max_tasks_per_child=None)
# max_workers 最大进程数
```
##### 示例
```python
from concurrent.futures import ProcessPoolExecutor
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):  # 是不是素数
    if n < 2: 
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
	# 创建一个 ProcessPoolExecutor 对象，并使用 map() 方法提交任务
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
	        print(f'{number} is prime: {prime}')

if __name__ == '__main__':
    main()
```