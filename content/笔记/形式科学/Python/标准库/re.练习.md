##### re.练习
```python
# 查找
re.search('^\w+ ',"Hello 世界\nHi 你好")  # 第一个匹配的单词
	# <re.Match object; span=(0, 6), match='Hello '>

re.search(' \w+',"Hello 世界\nHi 你好")  # 匹配空格接一个单词
	# <re.Match object; span=(5, 8), match=' 世界'>
re.match(' \w+',"Hello 世界\nHi 你好")  # 从头匹配到 '^ \w+'
	# None

re.findall(' \w+',"Hello 世界\nHi 你好")
	# [' 世界', ' 你好']

# 替换
re.sub(' \w+', ' 您好', "Hello 世界\nHi 你好")
	# 'Hello 您好\nHi 您好'
re.sub(' \w+', ' 您好', "Hello 世界\nHi 你好")
	# ('Hello 您好\nHi 您好', 2)

# 分割
re.split(' \w+', "Hello 世界\nHi 你好")
	# ['Hello', '\nHi', '']
re.split('\w+ ', "Hello 世界\nHi 你好")
	# ['', '世界\n', '你好']

# 分组匹配
re.findall('(\w+) (\w+)', "Hello 世界\nHi 你好")  # 匹配内容按括号的内容分组
	# [('Hello', '世界'), ('Hi', '你好')]

re.findall('(?:\w+) (?:\w+)', "Hello 世界\nHi 你好")  # 不分组
	# ['Hello 世界', 'Hi 你好']

re.findall('\w+ \w+', "Hello 世界\nHi 你好")  # 同不分组效果
	# ['Hello 世界', 'Hi 你好']
```