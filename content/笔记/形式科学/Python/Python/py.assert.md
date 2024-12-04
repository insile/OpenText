##### assert
- `assert`
	- 用于[[py.异常处理|异常处理]]断言检查语句, 在代码中检查某个条件是否满足, 不满足则触发[[py.异常类型|AssertionError]]断言异常, 并返回一个可选的错误消息
```python
# 断言检查形式
'''
assert 检查条件, 错误消息
'''

# 简单的断言检查
def divide(a, b):
    assert b != 0, "错误: 分母不能为0"
    return a / b

result = divide(10, 2)
print("Result:", result)

result = divide(10, 0)  # 这里会触发 AssertionError
print("Result:", result)  # 这一行代码不会执行，因为上一行已经中断了程序的执
```