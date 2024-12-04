##### map()
- `map( function, iterable )`
	- 用于对[[py.迭代器对象|可迭代对象]]中的每个元素应用指定的函数, 返回map对象, 是[[py.迭代器对象|迭代器对象|]]

```python
# 定义一个函数，将数字加倍
def double(x):
    return x * 2

# 创建一个列表
numbers = [1, 2, 3, 4, 5]

# 使用 map() 函数将函数应用到列表的每个元素
doubled_numbers = map(double, numbers)

# 转换为列表查看结果
result = list(doubled_numbers)
print(result)  # 输出：[2, 4, 6, 8, 10]

```

