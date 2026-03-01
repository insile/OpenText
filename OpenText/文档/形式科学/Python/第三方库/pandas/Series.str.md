##### Series.str
- [[str.cat()]]  拼接字符串
- [[str.re]]  正则示例
```python
# 操作处理
str.len() # 元素长度
str.lower()  # 小写
str.upper()  # 大写
str.capitalize()  # 首字母大写
str.title()  # 每个首字母大写
str.swapcase()  # 大小写互换
str.translate(table)  # 映射字符串
str.repeat(repeats)  # 复制每个字符串repeats次
str.zfill(width)  # 补0
str.slice(start=None, stop=None, step=None)  # 切片
str.join(sep)  # 连接列表，每个元素为存储字符的列表
str.startswith  # 开头判断
str.endswith  # 结尾判断
str.find(sub, start=0, end=None)  # 搜索第一个子串，返回位置
str.center(width[, fillchar])  # 左右侧填充fillchar
str.ljust(width[, fillchar])  # 右侧填充fillchar
str.just(width[, fillchar])  # 左侧填充fillchar
str.strip([to_strip])  # 删除开头和结尾字符to_strip
str.rstrip([to_strip])  # 删除开头字符to_strip
str.lstrip([to_strip])  # 删除结尾字符to_strip

# 正则相关
str.findall(pat, flags=0)
	# 提取正则表达式的所有匹配项
str.extract(pat, flags=0, expand=True)
	# 将正则表达式中的捕获组提取为 DataFrame 中的列，第一个匹配的
str.extractall(pat, flags=0)
	# 将正则表达式中的捕获组提取为 DataFrame 中的列，所有匹配的

str.replace(pat, repl[, n, case, ...])  
	# 替换匹配项
str.split(pat=None, *, n=- 1, expand=False, regex=None)  
	# 按匹配项分割

str.contains(pat, case=True, flags=0, na=None, regex=True)
	# 内容正则表达式包含判断
str.match(pat[, case, flags, na])
	# 确定每个字符串是否以正则表达式的匹配开始
str.fullmatch(pat, case=True, flags=0, na=None)
	# 确定每个字符串是否完全匹配正则表达式。

str.count(pat, flags=0)
	# 统计每个字符串中正则表达式出现次数


# 编码解码
str.decode(encoding[, errors])
str.encode(encoding[, errors])
```