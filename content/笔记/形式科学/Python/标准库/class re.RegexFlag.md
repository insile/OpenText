##### class re.RegexFlag
```python
re.A 
	# 只匹配ASCII 
	# 让 \w, \W, \b, \B, \d, \D, \s 和 \S 只匹配ASCII，而不是Unicode

re.I 
	# 忽略大小写
	# 表达式如 [A-Z] 也会匹配小写字符

re.M 
	# 多行匹配
	# `^` 和 `$` 符号开始匹配每一行的开头的结尾，而不是一个字符串
```
##### 示例
```python
re.findall('\w+',"Hello 世界", flags=re.A)  # 只匹配ASCII
	# ['Hello']

re.findall('[a-z]+',"Hello 世界", flags=re.I)  # 忽略大小写的单词
	# ['Hello']

re.findall('^\w+ ',"Hello 世界\nHi 你好", flags=re.M)  # 每行单词及后面空格
	# ['Hello ', 'Hi ']
```


