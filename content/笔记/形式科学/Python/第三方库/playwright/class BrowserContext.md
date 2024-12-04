##### class BrowserContext
- `BrowserContext.说明`
	- 浏览器上下文提供了一种操作多个独立浏览器会话的方法。
	- 如果一个页面打开另一个页面, 弹出窗口将属于父页面的浏览器上下文。
	- 通过[[Browser.new_context()]]创建, 支持创建隐身浏览器上下文, 不会将任何浏览数据写入磁盘。
```python
context = browser.new_context()  # 浏览器上下文
page = context.new_page()  # 在上下文中创建一个新页面
page.goto("https://example.com")  # 导航前往
context.close()  # 关闭上下文
```
- [[BrowserContext.实例方法]]
- [[BrowserContext.实例属性]]
- [[BrowserContext.事件]]
