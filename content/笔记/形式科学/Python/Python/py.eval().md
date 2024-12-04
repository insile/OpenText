##### eval()
- `eval( expression, globals=None, locals=None )`
	- 用于执行一个字符串表达式`expression`，并返回表达式的结果
	- `expression` 要执行的字符串表达式或者代码对象
	- `globals` 可选参数，用于指定[[py.作用域和命名空间|全局命名空间]]（全局变量和函数）。如果没有提供，则默认为当前全局命名空间
	- `locals` 可选参数，用于指定[[py.作用域和命名空间|局部命名空间]]（局部变量和函数）。如果没有提供，则默认为当前局部命名空间
```python
x = 10
result = eval("x + 5")
print(result)  # 输出：15

expression = "2 * 3 + 5"
result = eval(expression)
print(result)  # 输出：11

globals_dict = {'a': 5, 'b': 7}  # 命名空间
result = eval("a + b", globals_dict)
print(result)  # 输出：12

```