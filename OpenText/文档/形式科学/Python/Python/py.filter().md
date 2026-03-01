##### filter()
- `filter( function, iterable )`
	- 过滤掉不符合条件的元素，返回由符合条件元素组成的[[py.迭代器对象|迭代器对象]]
```python
# 定义一个函数，判断数字是否为偶数
def is_even(x):
    return x % 2 == 0

# 创建一个列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用 filter() 函数筛选出偶数
even_numbers = filter(is_even, numbers)

# 转换为列表查看结果
result = list(even_numbers)
print(result)  # 输出：[2, 4, 6, 8, 10]

```