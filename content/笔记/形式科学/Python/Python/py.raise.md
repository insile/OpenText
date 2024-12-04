##### raise
- `raise`
	- 用于[[py.异常处理|异常处理]]主动抛出异常终止程序语句
```python
# 形式
'''
raise 异常名称('异常描述')
'''

try:
    a = input("输入一个数：")
    if not a.isdigit():
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：", e)
```

