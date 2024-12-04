##### class re.Match
- 实例方法
```python
Match.group([group1, ...])
	# 返回一个或者多个匹配的子组，0为整体匹配
Match.groups()
	# 返回一个元组，包含所有匹配的子组
Match.groupdict()
	# 返回一个字典，包含了所有的 命名 子组
Match.start([group])
Match.end([group])
	# 返回 group 匹配到的字串的开始和结束标号，默认整体
Match.span([group])
	# 返回一个二元组 (m.start(group), m.end(group))，默认整体

Match.re
	# 返回产生这个实例的 正则对象 
Match.string
	# 传递到 match() 或 search() 的字符串。
```
##### 示例
```python
text = "现在的日期是2021-07-02，超过最后期限"  
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"  
match = re.search(pattern, text)

match.groups()  # ('2021', '07', '02')
match.group(0)  # '2021-07-02'
match.group(1) == match[1] == match['year']  # '2021'
match.group(2) == match[2] == match['month']  # '07'
match.group(3) == match[3] == match['day']  # '02'
match.groupdict()  # {'year': '2021', 'month': '07', 'day': '02'}
match.start()  # 6
match.end()  # 16
match.span()  # (6, 16)
match.re  # re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', re.UNICODE)
match.string   # "现在的日期是2021-07-02，超过最后期限" 
```