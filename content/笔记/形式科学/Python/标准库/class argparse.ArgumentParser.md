##### class argparse.ArgumentParser 解析器类: 创建解析器
- 实例化方法
```python
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, 
							  parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-',
							fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', 
							add_help=True, allow_abbrev=True, exit_on_error=True)
# 创建一个新的 ArgumentParser 对象
# prog - 程序的名称 (默认值: os.path.basename(sys.argv[0]))
# usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
# description - 简介 (默认值： None)
# epilog - 后续说明 (默认值： None)
# parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
# formatter_class - 用于自定义帮助文档输出格式的类
# prefix_chars - 可选参数的前缀字符集合（默认值： '-'）
# fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值： None）
# argument_default - 参数的全局默认值（默认值： None）
# conflict_handler - 解决冲突选项的策略（通常是不必要的）
# add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
# allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）
# exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)
```
- 实例方法
	- [[ArgumentParser.add_argument()]] 实例方法: 添加参数
	- [[ArgumentParser.parse_args()]] 实例方法: 解析参数