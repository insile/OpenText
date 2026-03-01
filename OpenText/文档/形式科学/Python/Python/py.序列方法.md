##### 序列方法
- 通用序列方法
```python
x in s  # 如果 s 中的某项等于 x 则结果为 True，否则为 False
x not in s  # 如果 s 中的某项等于 x 则结果为 False，否则为 True
s + t  # s 与 t 相拼接
s * n 或 n * s  # 相当于 s 与自身进行 n 次拼接
s[i]   # s 的第 i 项，起始为 0
s[i:j]  # s 从 i 到 j 的切片
s[i:j:k]  # s 从 i 到 j 步长为 k 的切片
s.index(x,i,j) # 在i到j位置中查找第一个x的位置
s.count(x) # 返回x出现的总次数
```
- 可变序列方法
```python
s[i] = x  # 将 s 的第 i 项替换为 x
s[i:j] = t  # 将 s 从 i 到 j 的切片替换为可迭代对象 t 的内容
del s[i:j]  # 等同于 s[i:j] = []
s[i:j:k] = t  # 将 s[i:j:k] 的元素替换为 t 的元素
del s[i:j:k]  # 从列表中移除 s[i:j:k] 的元素
s.append(x)  # 最后增加x
s.clear()  # 删光
s.copy()  # 生产新列表并赋值
s.extend(t)  # 用 t 的内容扩展 s
s += t  # 用 t 的内容扩展 s
s *= n  # 使用 s 的内容重复 n 次来对其进行更新
s.insert(i,x)  # i位置增加x
s.pop(i)  # 取出i位置元素并删除
s.remove(x)  # 删除第一个x
s.reverse()  # 反转列表
```
- 列表方法
```python
ls.sort(*, key=None, reverse=False)  # 原地排序
```
- 字符串函数及方法
```python
str.encode(encoding='utf-8', errors='strict')  # 返回编码为 bytes 的字符串
str.lower()  # 返回字符串小写副本
str.upper()  # 返回字符串大写副本
str.capitalize()  # 首个字符大写
str.title()  # 每个单词第一个字母为大写

str.join(iter)  # 使用指定字符str将字符串列表iter连接成一个字符串
str.split(sep=None)  # 返回一个根据sep分割的列表
str.count(sub[, start[, end]])  # 返回子串sub在[start,end]范围非重叠出现次数
str.replace(old,new)  # old替换为new并返回
str.find(sub[, start[, end]])  # 返回字符子串sub在s[start:end]切片内被找到的最小索引，否则返回-1
str.endswith(suffix[, start[, end]])  # 检查字符串是否以指定的后缀结尾, 可指定位置
str.startswith(suffix[, start[, end]])  # 检查字符串是否以指定的前缀开头, 可指定位置

str.zfill(width)  # 左边填充0达到宽度width
str.center(width,[fillchar])  # 根据宽度居中，两侧填充
str.strip(chars)  # 去掉头尾指定字符
str.format(*args, **kwargs)  # 字符串格式化
	' {0:} {1:} '.format(字符串0，字符串1)
	{字符串序号: 格式控制标记}
	0        # 字符串序号
	:        # 引导符号
	<填充>   # 用于填充的单个字符
	<对齐>   # <左对齐，>右对齐，^居中对齐
	<正负>   # "+" | "-" | " "
	<宽度>   # 槽设定的输出宽度
	< , >    # 数字的千位分隔符
	<.精度>  # 浮点数小数精度或字符串最大输出长度
	<类型>   # 整数类型b,c,d,o,x,X；浮点数类型e,E,f,%

```
- 二进制序列类型方法
```python
bytes.decode(encoding='utf-8', errors='strict')
bytearray.decode(encoding='utf-8', errors='strict')
	# 返回解码为 encoding 的字节串
```