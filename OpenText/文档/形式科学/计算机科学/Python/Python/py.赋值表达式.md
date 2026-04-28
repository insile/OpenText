##### 赋值表达式
- 赋值表达式
	- 赋值表达式使用海象运算符 `:=`, 与[[py.赋值语句|赋值语句]]不同的就是表达式返回一个值, 可继续参与其他运算, 比如赋值后直接条件判断
```python
# := 赋值表达式形式, 赋值后进行条件判断
'''
variable := expression
'''

text = '123'
# 旧写法
length = len(text)
if length > 10:
	print("Text is too long:", length)

# 新写法（使用海象运算，赋值后直接判断）
if (length := len(text)) > 10:
	print("Text is too long:", length)
```

