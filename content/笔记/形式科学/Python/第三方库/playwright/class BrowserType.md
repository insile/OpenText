##### class BrowserType
- `BrowserType.说明`
	- 提供了启动特定浏览器实例或连接到现有实例的方法, 通过 [[class Playwright|Playwright.chromium]] 等创建
```python
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium  # chromium 的 BrowserType
    browser = chromium.launch()  # 返回浏览器实例
    page = browser.new_page()
    page.goto("https://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```
- [[BrowserType.实例方法]]
- [[BrowserType.实例属性]]
