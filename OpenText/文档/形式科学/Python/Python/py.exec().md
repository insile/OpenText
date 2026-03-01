##### exec()
- `exec(object, globals=None, locals=None, /, *, closure=None)`
	- 动态执行 Python 代码，返回值为 `None`
	- `object` 要执行的代码字符串，可以是一个代码块、一个单独的语句或者一系列语句。
	- `globals` 可选参数，用于指定[[py.作用域和命名空间|全局命名空间]]（全局变量和函数）。如果没有提供，则默认为当前全局命名空间
	- `locals` 可选参数，用于指定[[py.作用域和命名空间|局部命名空间]]（局部变量和函数）。如果没有提供，则默认为当前局部命名空间
```python
# 执行代码块
source_code = """
def greet(name):
    print(f'Hello, {name}!')
greet('Alice')
"""
exec(source_code)

# 改变本地字典
globals_dict = {"x": 10}
locals_dict = {}
code = 'a, b = x, 2'
exec(code, globals_dict, locals_dict)
print(locals_dict)  # 输出：{'a': 10, 'b': 2}

```

