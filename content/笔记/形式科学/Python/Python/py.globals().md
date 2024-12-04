##### globals()
- `globals( )`
	- 返回[[py.作用域和命名空间|全局作用域|]]中的变量和值的字典
	- 函数返回的字典是对实际变量的引用，因此实时更新，对字典的修改会影响变量本身
	- 在[[py.作用域和命名空间|全局作用域]]与[[py.locals()|locals()]]，[[py.vars()|vars()]]相等
```python
x = 10
y = 'Hello'

def example_function():
    z = 20
    print(globals())

example_function()

vars() == locals() == globals()  # True
```