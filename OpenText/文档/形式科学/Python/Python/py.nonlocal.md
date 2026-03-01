##### nonlocal
- `nonlocal`
	- 声明[[py.作用域和命名空间|嵌套作用域中的外部变量]], 可修改
	- 在[[py.闭包|闭包]]中修改外部变量
```python
# 声明形式
'''
nonlocal 变量
'''

def nonlocal_test():
    count = 0  # 外部变量

    def test():
        nonlocal count  # 声明外部变量
        count += 1  # 声明后可修改
        return count

    return test  # 调用test()


val = nonlocal_test()

print(val())  # 1
print(val())  # 2
print(val())  # 3
```

