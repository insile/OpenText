##### class Browser
- `Browser.说明`
	- 具体的浏览器对象, 通过[[BrowserType.launch()]]创建
```python
from playwright.sync_api import sync_playwright

def run(playwright):
    firefox = playwright.firefox
    browser = firefox.launch()  # 浏览器实例, 默认无头
	# browser = firefox.launch(headless= False)  # 有头
    page = browser.new_page()
    page.goto("https://example.com")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```
- [[Browser.实例方法]]
- [[Browser.实例属性]]
- [[Browser.事件]]
