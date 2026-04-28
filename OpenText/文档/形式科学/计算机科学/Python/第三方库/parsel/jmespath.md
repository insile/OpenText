##### jmespath
- 基本表达式
```python
# 键
Selector('{"a": "foo", "b": "bar", "c": "baz"}',type='json').jmespath('a')
# [<Selector query='a' data='foo'>]
Selector('{"a": {"b": {"c": {"d": "value"}}}}',type='json').jmespath('a.b.c.d')
# [<Selector query='a.b.c.d' data='value'>]

# 索引
Selector('["a", "b", "c", "d", "e", "f"]',type='json').jmespath('[1]')
# [<Selector query='[1]' data='b'>]

# 切片 
Selector('["a", "b", "c", "d", "e", "f"]',type='json').jmespath('[0:5]')
# [<Selector query='[0:5]' data='a'>,
#  <Selector query='[0:5]' data='b'>,
#  <Selector query='[0:5]' data='c'>,
#  <Selector query='[0:5]' data='d'>,
#  <Selector query='[0:5]' data='e'>]
```