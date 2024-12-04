##### class re.Pattern
- 实例化方法
```python
re.compile(pattern, flags=0)
	# 创建正则表达式对象
```
- 实例方法
```python
# 同re函数
Pattern.search(string[, pos[, endpos]])
Pattern.match(string[, pos[, endpos]])
Pattern.split(string, maxsplit=0)
Pattern.findall(string[, pos[, endpos]])
Pattern.finditer(string[, pos[, endpos]])
Pattern.sub(repl, string, count=0)
Pattern.subn(repl, string, count=0)
```