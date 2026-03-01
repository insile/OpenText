##### parsel.xpath
```python
import requests
from parsel import Selector

url = 'https://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)

# <html>
#  <head>
#   <base href='http://example.com/' />
#   <title>Example website</title>
#  </head>
#  <body>
#   <div id='images'>
#    <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
#    <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
#    <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
#    <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
#    <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
#   </div>
#  </body>
# </html>

```
##### `节点名` 选取根节点下的节点
```python
selector.xpath('head')
# [<Selector query='head' data='<head>\n  <base href="http://example.c...'>]
selector.xpath('head').xpath('title')
# [<Selector query='title' data='<title>Example website</title>\n </hea...'>]
```
##### `/` 从根节点开始选取（绝对路径）
```python
selector.xpath('/html')
# [<Selector query='/html' data='<html>\n <head>\n  <base href="http://e...'>]
selector.xpath('/html/head')
# [<Selector query='/html/head' data='<head>\n  <base href="http://example.c...'>]
```
##### `//` 从任意位置的节点开始
```python
selector.xpath('//head')
# [<Selector query='head' data='<head>\n  <base href="http://example.c...'>]
selector.xpath('//a')
# [<Selector query='//a' data='<a href="image1.html">Name: My image ...'>,
#  <Selector query='//a' data='<a href="image2.html">Name: My image ...'>,
#  <Selector query='//a' data='<a href="image3.html">Name: My image ...'>,
#  <Selector query='//a' data='<a href="image4.html">Name: My image ...'>,
#  <Selector query='//a' data='<a href="image5.html">Name: My image ...'>]
```
##### `.` 选取当前节点
```python
selector.xpath('.')
# [<Selector query='.' data='<html>\n <head>\n  <base href="http://e...'>]
selector.xpath('//a/.')
# [<Selector query='//a/.' data='<a href="image1.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image2.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image3.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image4.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image5.html">Name: My image ...'>]
```
##### `..` 选取当前节点的父节点
```python
selector.xpath('.')
# [<Selector query='.' data='<html>\n <head>\n  <base href="http://e...'>]
selector.xpath('//a/.')
# [<Selector query='//a/.' data='<a href="image1.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image2.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image3.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image4.html">Name: My image ...'>,
#  <Selector query='//a/.' data='<a href="image5.html">Name: My image ...'>]
```
##### `@` 选取属性
```python
selector.xpath('//base/@href')
# [<Selector query='//base/@href' data='http://example.com/'>]
selector.xpath('//a').xpath('@href')
# [<Selector query='@href' data='image1.html'>,
#  <Selector query='@href' data='image2.html'>,
#  <Selector query='@href' data='image3.html'>,
#  <Selector query='@href' data='image4.html'>,
#  <Selector query='@href' data='image5.html'>]
```
##### `[]` 条件选取节点
```python
node[1] # 第一个node节点
node[last()] # 最后一个node节点
node[last()-1] # 倒数第二个node节点
node[position()<3] # 前两个node节点
node[@class] # 带有class属性的node节点
node[@class="main"] # class属性为main的node节点
node[price>30] # price元素大于30的node节点
```
##### `*` 所有子节点
```python
selector.xpath('*')
# [<Selector query='*' data='<head>\n  <base href="http://example.c...'>,
#  <Selector query='*' data='<body>\n  <div id="images">\n   <a href...'>]
selector.xpath('/*')
# [<Selector query='/*' data='<html>\n <head>\n  <base href="http://e...'>]
```
##### @* 所有有属性的节点
```python
selector.xpath('//@*')
# [<Selector query='//@*' data='http://example.com/'>,
#  <Selector query='//@*' data='images'>,
#  <Selector query='//@*' data='image1.html'>,
#  <Selector query='//@*' data='image1_thumb.jpg'>,
#  <Selector query='//@*' data='image2.html'>,
#  <Selector query='//@*' data='image2_thumb.jpg'>,
#  <Selector query='//@*' data='image3.html'>,
#  <Selector query='//@*' data='image3_thumb.jpg'>,
#  <Selector query='//@*' data='image4.html'>,
#  <Selector query='//@*' data='image4_thumb.jpg'>,
#  <Selector query='//@*' data='image5.html'>,
#  <Selector query='//@*' data='image5_thumb.jpg'>]
```
##### `|` 或
```python
selector.xpath('//head|//body')
# [<Selector query='//head|//body' data='<head>\n  <base href="http://example.c...'>,
#  <Selector query='//head|//body' data='<body>\n  <div id="images">\n   <a href...'>]
```
##### text() 节点文本; comment() 节点注释
```python
selector.xpath('//title/text()')
# [<Selector query='//title/text()' data='Example website'>]
selector.xpath('//title/comment()')
# []
```
##### xpath 函数
```python
selector.xpath('string(//div)')
# [<Selector query='string(//div)' data='\n   Name: My image 1 \n   Name: My ima...'>]

selector.xpath('//a[contains(@href, "image")]/@href').getall()
# ['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

selector.xpath('//a[starts-with(@href, "image1")]/@href').getall()
# ['image1.html']

selector.xpath('//a[not(@href)]').getall()
# []

```