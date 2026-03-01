##### slice()
- `slice( stop )`
- `slice( start , stop , step )`
	- 创建一个切片对象
```python
# 创建一个切片对象，表示从索引 1 到 5 的子序列
my_slice = slice(1, 5)
print(my_slice)  # 输出：slice(1, 5, None)

# 创建一个切片对象，表示从索引 2 到 10，每隔 2 个元素取一个
step_slice = slice(2, 10, 2)
print(step_slice)  # 输出：slice(2, 10, 2)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_slice = slice(2, 8, 2)
sub_list = my_list[my_slice]
print(sub_list)  # 输出：[3, 5, 7]

```