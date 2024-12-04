##### 动态执行
- 动态执行
	- 动态执行是指在程序运行时生成并执行代码, 而不是在编写代码时已经确定的部分. 这种技术允许程序根据运行时的条件, 输入或其他因素动态构建和运行新的代码片段. 在 Python 中, 主要通过 [[py.eval()|eval()]] 和 [[py.exec()|exec()]] 来实现, 它们可接受代码对象, 来自[[py.compile()|compile()]] 
- 动态执行命名空间
	- 动态执行代码的[[py.作用域和命名空间|命名空间]]管理, 使用 [[py.globals()|globals()]] 和 [[py.locals()|locals()]] 或者使用自定义字典命名空间

```python
# 当您希望代码能够访问当前全局命名空间和局部命名空间中的变量、函数和类时，可以传入 globals() 和 locals()。这样代码将在当前作用域内执行，并且可以访问当前作用域中的所有内容。适合于在当前上下文中执行动态生成的代码，充分利用已有的命名空间。
x = 10
def execute_code(code):
    exec(code, globals(), locals())
source_code = """
print(x)
"""
execute_code(source_code)


# 当您想要限制代码的访问范围，防止代码对当前作用域中的变量产生影响时，可以传入自定义的字典命名空间。这样代码只能访问和操作传入的字典中的变量，不会影响当前作用域。适合于执行具有受限制的代码，以确保代码不会对外部环境造成意外影响。
# 创建特定的命名空间
globals_namespace = {
    'x': 10,
    'y': 20,
    'add': lambda a, b: a + b
}
locals_namespace = {}
# 要执行的代码，其中 result 定义在 locals_namespace
source_code = """
result = add(x, y)  
print(result)
"""

# 在特定的命名空间中执行代码
exec(source_code, globals_namespace,  locals_namespace)
locals_namespace  # {'result': 30}
```