##### class collections.ChainMap 映射链
- 实例化方法
```python
collections.ChainMap(*maps)
	# 将多个字典或者其他映射通过引用组合在一起，返回 ChainMap
	# 支持所有常用字典方法
	# 搜索键，只返回第一个被找到的
	# 写，更新和删除只操作第一个映射
```
- 实例属性
```python
collections.maps
# 一个可以更新的映射列表。这个列表是按照第一次搜索到最后一次搜索的顺序组织的。它是仅有的存储状态，可以被修改。列表最少包含一个映射。
collections.parents
# 属性返回一个新的 ChainMap 包含所有的当前实例的映射，除了第一个。这样可以在搜索的时候跳过第一个映射。
```
##### 示例
```python
from collections import ChainMap
# 创建三个字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}
# 创建 ChainMap 对象
chain_map = ChainMap(dict1, dict2, dict3)
# 使用 ChainMap 查找键
print(chain_map['a'])  # 1，从 dict1 中找到
print(chain_map['b'])  # 2，从 dict1 中找到
print(chain_map['c'])  # 4，从 dict2 中找到
print(chain_map['d'])  # 6，从 dict3 中找到

# 获取所有键和值
print(list(chain_map.keys()))  # ['c', 'd', 'b', 'a']  去重键
print(list(chain_map.values()))  # [4, 6, 2, 1]  键第一个找到的值

# 只更新第一个映射
chain_map['c'] = 4
# [{'a': 1, 'b': 2, 'c': 4}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
```