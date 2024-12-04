##### id()
- `id( object )`
	- 返回对象的标识值
```python
x = 5
print(id(x))  # 输出 x 对象的唯一标识符

my_list = [1, 2, 3]
print(id(my_list))  # 输出 my_list 对象的唯一标识符

y = x
print(id(y))  # 输出 y 对象的唯一标识符，与 x 相同

z = 5
print(id(z))  # 输出 z 对象的唯一标识符，与 x 相同
```