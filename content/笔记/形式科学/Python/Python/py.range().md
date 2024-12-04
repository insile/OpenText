##### range()
- `range( stop )`
- `range( start, stop [, step] )`
	- 返回循环计数序列, 是[[py.迭代器对象|可迭代对象]]
	- 产生0到stop-1的整数序列，共n个
	- 产生start到stop-1的整数序列，步长为step
```python
# 生成一个包含整数序列的 range 对象
nums = range(5)
print(list(nums))  # 输出：[0, 1, 2, 3, 4]

# 生成一个从 2 到 8 的整数序列，步长为 2
even_nums = range(2, 9, 2)
print(list(even_nums))  # 输出：[2, 4, 6, 8]

# 使用 range() 循环迭代
for i in range(3):
    print(i)
# 输出：
# 0
# 1
# 2
```
