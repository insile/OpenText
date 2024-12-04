##### class parsel.Selector
- `Selector.说明`
	- 选择器对象
- `Selector.创建`
```python
Selector(text: str | None = None, # str 的 HTML XML JSON  
		 type: str | None = None, # 选择器类型 "html"(默认)|"json"|"xml"
		 body: bytes = b'', # 字节对象
		 encoding: str = 'utf8', # 字节编码
		 namespaces: ~typing.Mapping[str, str] | None = None, 
		 root: ~typing.Any | None = <object object>, 
		 base_url: str | None = None, # 文档的url
		 _expr: str | None = None, 
		 huge_tree: bool = True)

```
- `Selector.选择方法`
```python
Selector.css(query: str)→ SelectorList[_SelectorType]
	# 应用CSS选择器并返回SelectorList对象

Selector.xpath(query: str, namespaces: Mapping[str, str] | None = None, **kwargs: Any)→ SelectorList[_SelectorType]
	# 应用xpath选择器并返回SelectorList对象
	
Selector.jmespath(query: str, **kwargs: Any)→ SelectorList[_SelectorType]
	# 应用jmespath选择器并返回SelectorList对象
	
Selector.re(regex: str | Pattern[str], replace_entities: bool = True)→ List[str]
	# 应用正则表达式，并返回一个包含匹配项的字符串列表

Selector.get()→ Any
	# 序列化并返回匹配的节点

Selector.getall()→ List[str]
	# 序列化并返回字符串的1元素列表中的匹配节点
```
- `Selector.修改方法`
```python
Selector.drop()→ None
# 从父元素中删除匹配的节点
```