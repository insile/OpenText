##### 可迭代拆包
- 允许你将可迭代对象的元素拆包（unpack）到变量中。这种语法主要涉及到两个符号：`*` 和 `**`
```python
# *
# 在函数调用中使用单星号拆包
numbers = [1, 2, 3, 4, 5]
print(*numbers)  # 相当于 print(1, 2, 3, 4, 5)

# 在赋值语句中使用单星号拆包
first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# **
# 在函数调用中使用双星号拆包
person_info = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
print(**person_info)  # 相当于 print(name='Alice', age=30, city='Wonderland')

# 在赋值语句中使用双星号拆包
person = {'name': 'Bob', 'age': 25}
full_info = {'city': 'Dreamland', **person}
print(full_info)  # {'city': 'Dreamland', 'name': 'Bob', 'age': 25}
```