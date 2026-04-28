##### in
- `in`
	- 中用于判断某个元素是否属于容器 (如字符串, 列表, 元组, 字典, 集合等) 的成员运算符, 它用于检查某个元素是否存在于给定容器中, 如果存在则返回 True, 否则返回 False
```python
# 字符串中检查子串
text = "Hello, world!"
print("Hello" in text)  # 输出: True
print("Python" in text)  # 输出: False

# 列表中检查元素
fruits = ["apple", "banana", "orange"]
print("banana" in fruits)  # 输出: True
print("grape" in fruits)  # 输出: False

# 元组中检查元素
colors = ("red", "green", "blue")
print("green" in colors)  # 输出: True
print("yellow" in colors)  # 输出: False

# 字典中检查键
person = {"name": "John", "age": 30, "gender": "male"}
print("name" in person)  # 输出: True
print("city" in person)  # 输出: False

# 集合中检查元素
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # 输出: True
print(6 in numbers)  # 输出: False

```