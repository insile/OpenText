##### 字典方法
- 字典方法
```python
d[key]  # 返回 d 中以 key 为键的项
d[key] = value  # 将 d[key] 设为 value
del d[key]  # 将 d[key] 从 d 中移除。 如果映射中不存在 key 则会引发 KeyError
key in d  # 如果 d 中存在键 key 则返回 True，否则返回 False
key not in d  # 等价于 not key in d
d.keys()  # 返回所有键信息，字典视图对象
d.values()  # 返回所有值信息，字典视图对象
d.items()  # 返回所有键值对信息，字典视图对象
d.popitem()  # 取出键值对，先进后出

d.get(k,default)  # 返回值，不存在返回default
d.setdefault(k,default)  # 返回值，不存在插入键值
d.pop(k,default)  # 取出键值，不存在返回default

d.update(other)  # 更新覆盖字典
d.clear()  # 删光键值对
d.copy()  # 浅拷贝

```
