##### callable()
- `callable( object )`
	- 判断一个对象是否可以调用，如果对象可以被调用，即表示该对象是一个可调用对象
```python
# 检查函数是否可调用
def my_function():
    pass

result = callable(my_function)
print(result)  # 输出：True

# 检查类是否可调用
class MyClass:
    pass

result = callable(MyClass)
print(result)  # 输出：True

# 检查实例对象是否可调用
obj = MyClass()
result = callable(obj)
print(result)  # 输出：False

```