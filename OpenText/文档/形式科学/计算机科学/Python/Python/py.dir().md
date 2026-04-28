##### dir()
- `dir( object )`
	- 带参数，返回 `object` 的属性、方法列表
	- 不带参数，返回[[py.作用域和命名空间|当前作用域]]内的变量、方法和定义的名称列表
	- 如果作用域相同，实际上就是 [[py.vars()|vars()]]、[[py.locals()|locals()]]、[[py.globals()|globals()]] 的字典键列表
```python
# 当前作用域中的名称列表
gdir = dir()  # 全局
def f():
    a = b = 1
    return dir(), locals(), vars()  # 局部
ldir, loc, var= f()
# ldir ['a', 'b']
# loc {'a': 1, 'b': 1}
# var {'a': 1, 'b': 1}

# 列表的属性、方法列表
dir([])
```