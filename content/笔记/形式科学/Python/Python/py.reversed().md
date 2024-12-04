##### reversed()
- `reversed( sequence )`
	- 用于反转一个序列, 返回[[py.迭代器对象|迭代器对象]]
	- 可反转字典键
```python
string = "Hello"
reversed_string = reversed(string)
print(list(reversed_string))  # 输出：['o', 'l', 'l', 'e', 'H']

numbers = [1, 2, 3, 4, 5]
reversed_numbers = reversed(numbers)
print(list(reversed_numbers))  # 输出：[5, 4, 3, 2, 1]

my_tuple = (2.5, 3.5, 4.5)
reversed_tuple = reversed(my_tuple)
print(tuple(reversed_tuple))   # 输出：(4.5, 3.5, 2.5)

```