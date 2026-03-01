##### 条件表达式
- 条件表达式
	- 条件表达式使用 [[py.if|if]], [[py.else|else]], 是一个简化条件语句
```python
# 条件表达式形式
'''
表达式1 if 判断条件 else 表达式2
'''

age = 20 

status = "Adult" if age >= 18 else "Minor"

age += 20 if age >= 18 else age - 10

print(1) if 1>0 else print(0)
```

