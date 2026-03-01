##### compile()
- `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=- 1)`
	- `source` 编译为代码对象并返回
	- `source` 需要编译的源代码，可以是字符串、字节对象或AST（Abstract Syntax Tree）对象
	- `filename` 用于指定代码的文件名，如果不是从文件中读取源代码，可以使用一个虚拟文件名
	- `mode` 指定编译的模式，有三种选项：'exec'、'eval' 和 'single'。'exec' 用于编译代码块，'eval' 用于编译单个表达式，'single' 用于编译单个交互式语句。
	- `flags` 可选参数，用于指定编译器旗标。参考标准库 `ast` 中带有 `PyCF_` 前缀的名称
	- `dont_inherit` 可选参数，如果为 `True`，则不继承来自父级编译对象的标志
	- `optimize`：可选参数，用于指定优化级别，-1 表示使用默认级别。
```python
# 单个表达式
source_code = "print('Hello, world!')"
compiled_code = compile(source_code, filename='<string>', mode='eval')
exec(compiled_code)

# 编译代码块
def create_function(b):
    source_code = \  # 动态创建函数
    f"""def factorial(n):
        if n == 0:
            return {b}
        else:
            return n * factorial(n - 1)
        print(factorial(5))"""
    compiled_code = compile(source_code, filename='<string>', mode='exec')
    exec(compiled_code)
create_function(2)
factorial(1)
```