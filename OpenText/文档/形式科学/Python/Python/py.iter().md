##### iter()
- `iter( object [, sentinel] )`
	- 返回[[py.迭代器对象|迭代器]]
	- 如果对象是函数等可调用对象，当返回值与`sentinel`相同时，迭代将停止
```python
# 返回迭代器
a = [1,2,3,4]
b = iter(a)
next(b)  # 1
next(b)  # 2
next(b)  # 3
next(b)  # 4

# 迭代到期望值
from random import randint 
def guess():  # 0-10随机整数生成
	return randint(0, 10)
num = 1
for i in iter(guess, 5):  # 随机到5时，循环停止
	print("第%s次猜测，猜测数字为: %s" % (num, i))
	num += 1

```