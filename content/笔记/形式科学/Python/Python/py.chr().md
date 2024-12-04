##### chr()
- `chr( i )`
	- 解码：返回十进制 Unicode 码点对应的字符
	- 仅适用于表示单个字符的字符串
	- a-z: 97-122；A-Z: 65-90；0-9: 48-57
```python
print(chr(65))   # 输出：'A'
print(chr(97))   # 输出：'a'
print(chr(48))   # 输出：'0'
print(chr(20013))# 输出：'中'
```