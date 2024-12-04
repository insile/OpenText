##### ArgumentParser.add_argument()
- ArgumentParser 实例方法: 添加参数
```python
ArgumentParser.add_argument(name or flags...[, action][, nargs]
							[, const][, default][, type][, choices]
							[, required][, help][, metavar][, dest])
# 增加参数
# name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
# action - 当参数在命令行中出现时使用的动作基本类型。
	# store - 存储参数的值
	# store_const - 存储由 const 关键字参数指定的值
	# store_true and store_false - 分别用作存储 True 和 False 值
# nargs - 命令行参数应当消耗的数目。
# const - 被一些 action 和 nargs 选择所需求的常数。
# default - 当参数未在命令行中出现并且也不存在于命名空间对象时所产生的值。
# type - 命令行参数应当被转换成的类型。如 float 或 int
# choices - 有效参数列表
# required - 此命令行选项是否可省略
# help - 一个此选项作用的简单描述
# metavar - 在使用方法消息中使用的参数值示例
# dest - 被添加到 parse_args() 所返回对象上的属性名

```