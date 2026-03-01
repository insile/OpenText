##### pathlib.纯路径类 
- 实例化
```python
class pathlib.PurePath(*pathsegments)
class pathlib.PurePosixPath(*pathsegments)
class pathlib.PureWindowsPath(*pathsegments)
	# pathsegments 参数相同，代表路径片段的字符串或者其他对象
	# 参数为空创建当前目录相对路径 PurePath()
	# 相对路径 PurePath('./code')
	# 绝对路径 PurePath('d:/code')
	# 多路径拼接 PurePath('d:/','code', 'p.py')
```
- 实例属性和方法
```python
str(PurePath)  # 转字符串
PurePath('c:/') / PurePath('Program Files') / 'p.py'  # / 运算符 拼接路径


PurePath.parts  # 路径组件，返回元组 ('c:\\', 'Program Files', 'p.py')
PurePath.drive  # 驱动器盘符 c:
PurePath.root  # 根字符串 \\
PurePath.anchor  # 驱动器和根的联合 c:\\
PurePath.parents  # 逻辑祖先
	# PurePath.parents[0]  PureWindowsPath('c:/Program Files')
	# PurePath.parents[1]  PureWindowsPath('c:/')
PurePath.parent  # 逻辑父路径, PurePath.parents[0]
PurePath.name  # 最后路径组件的字符串，p.py，PurePath.parts[-1]
PurePath.suffix  # name中文件扩展名 .py
PurePath.suffixes  # # name中文件扩展名列表 ['.py']
PurePath.stem  # name中去除扩展 p


PurePath.as_posix()  # 正斜杠路径字符串
PurePath.as_uri()  # file URI file://
PurePath.is_absolute()  # 绝对路径判断 
PurePath.is_relative_to(*other)  # 相对路径判断
PurePath.joinpath(*other)  # 拼接路径
PurePath.match(pattern)  # 模式匹配，成功返回 `True`，否则返回 `False`
	# PurePath('a/b.py').match('*.py') True
PurePath.relative_to(*other)  # 相对other的相对路径
```