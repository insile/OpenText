##### 其他符号
- 其他符号
	- 引号 `'` `"` `"""`；圆括号 `()`；方括号 `[]`；花括号 `{}`
	- 逗号 `,`；冒号 `:`；分号 `;`；at `@`；箭头 `->`
	- 海象运算赋值 `:=`	
```python
# 单双引号 用于表示字符串
'This is a string with single quotes.'
"This is a string with double quotes."
"This is a string with 'single quotes' inside."

# 三重引号 用于创建多行字符串或者多行注释
multiline_single_quoted_string = '''
This is a multiline string
using three single quotes.
'''
print(multiline_single_quoted_string)

# 圆括号 () 用于表示元组
(1, 2)  # 是一个元组

# 方括号 [] 用于表示列表
[1, 2, 3]  # 是一个列表

# 花括号 {} 用于表示字典、集合、集合推导等
{'name': 'John'}  # 是一个字典
{1, 2, 3}  # 是一个集合

# 逗号 , 用于分隔序列中的元素，如元组、列表
(1, 2, 3)
[4, 5, 6]

# 冒号 : 用于定义代码块、切片、字典键值对等。
for item in [4, 5, 6]: print(item)

# 分号 ; 用于在同一行上分隔多个语句
x = 5; y = 10。

# at @ 在装饰器语法中表示装饰器，也在矩阵乘法运算符中使用 (numpy)
@property

# 箭头 -> 用于注解函数返回类型
def add(x: int, y: int) -> int:
	print(x+y)
add(1,2)
```