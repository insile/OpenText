##### class collections.namedtuple 命名元组
- 实例化方法
```python
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
	# 用于创建带有命名字段的元组
	# 命名字段： namedtuple 创建的元组中的每个字段都有一个命名，可以像对象属性一样访问字段。
	# 不可变性： 与普通元组一样，namedtuple 也是不可变的，一旦创建就不能修改其值。
	# 字段访问： 可以通过字段名或索引来访问元组的字段值。
	# 解构： 可以将 namedtuple 解构为变量，通过字段名或索引获取值。
```
##### 示例
```python
from collections import namedtuple

# 创建一个名为 Point 的 namedtuple 类型
Point = namedtuple('Point', ['x', 'y'])
# 创建一个 Point 实例
p = Point(x=1, y=2)

print(p.x)           # 1
print(p.y)           # 2

# 使用索引访问字段值
print(p[0])          # 1
print(p[1])          # 2

# 解构元组
x, y = p
print(x, y)          # 1 2

# namedtuple 是不可变的，以下代码会引发 AttributeError
# p.x = 10
```