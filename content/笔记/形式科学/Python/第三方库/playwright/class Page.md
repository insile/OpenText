##### class Page
- `Page.说明`
	- 提供了与浏览器中的单个选项卡或 Chromium 中的扩展后台页交互的方法。一个浏览器实例可能有多个页面实例。通过 [[BrowserContext.new_page()]] 或 [[Browser.new_page()]] 创建
```python
from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit  # 浏览器启动器
    browser = webkit.launch()  # 浏览器实例
    context = browser.new_context()  # 浏览器上下文
    page = context.new_page()  # 新标签页
    page.goto("https://example.com")  # 导航网页
    page.screenshot(path="screenshot.png")  # 截图
    browser.close()  # 关闭

with sync_playwright() as playwright:
    run(playwright)
```
- [[Page.实例方法]]
- [[Page.实例属性]]
- [[Page.事件]]
