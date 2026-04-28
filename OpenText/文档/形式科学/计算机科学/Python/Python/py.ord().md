##### ord()
- `ord( c )`
	- 编码：返回字符对应的十进制 Unicode 码点
	- 仅适用于表示单个字符的字符串
	- a-z: 97-122；A-Z: 65-90；0-9: 48-57
```python
print(ord('A'))  # 输出：65
print(ord('a'))  # 输出：97
print(ord('0'))  # 输出：48
print(ord('中')) # 输出：20013
```