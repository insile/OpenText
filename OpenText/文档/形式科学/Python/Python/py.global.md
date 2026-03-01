##### global
- `global`
	- 声明[[py.作用域和命名空间|全局作用域中的全局变量]], 可修改
```python
# 声明形式
'''
global 变量
'''

def global_test():  
    global a  # 声明全局变量
    a += 1
    print(a)

a = 1  # 定义全局变量
global_test()
```
