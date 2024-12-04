##### del
- `del`
	- 用于 `del` 语句删除一个对象
```python
'''
del 变量
'''

# 删除变量
x = 10
print(x)  # 输出: 10

del x
print(x)  # 引发 NameError: name 'x' is not defined

# 删除列表元素
fruits = ["apple", "banana", "orange", "grape"]
print(fruits)  # 输出: ['apple', 'banana', 'orange', 'grape']

del fruits[2]
print(fruits)  # 输出: ['apple', 'banana', 'grape']

del fruits[1:3]
print(fruits)  # 输出: ['apple']

# 删除字典元素
person = {"name": "John", "age": 30, "gender": "male"}
print(person)  # 输出: {'name': 'John', 'age': 30, 'gender': 'male'}

del person["age"]
print(person)  # 输出: {'name': 'John', 'gender': 'male'}

```