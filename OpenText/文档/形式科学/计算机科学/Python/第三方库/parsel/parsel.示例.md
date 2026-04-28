##### parsel.示例
```python
from parsel import Selector

text = """
<html>
	<body>
		<h1>Hello, Parsel!</h1>
		<ul>
			<li><a href="http://example.com">Link 1</a></li>
			<li><a href="http://scrapy.org">Link 2</a></li>
		</ul>
		<script type="application/json">{"a": ["b", "c"]}</script>
	</body>
</html>"""

selector = Selector(text=text)
# 选择器

selector.css('h1::text').get()
# css 选择器
# 'Hello, Parsel!'

selector.xpath('//h1/text()').re(r'\w+')
# xpath 选择器
# ['Hello', 'Parsel']

for li in selector.css('ul > li'):
    print(li.xpath('.//@href').get())
# css 选择器
# http://example.com
# http://scrapy.org

selector.css('script::text').jmespath("a").get()
# JMESPath 选择器
# 'b'

selector.css('script::text').jmespath("a").getall()
# JMESPath 选择器
# ['b', 'c']


```