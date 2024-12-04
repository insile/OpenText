##### class Playwright
- `Playwright.说明`
	- 这是剧作家, 启动任务的开始, 通过[[sync_playwright()]]创建
```python
from playwright.sync_api import sync_playwright

def run(playwright):  # 运行一个Playwright实例
    chromium = playwright.chromium  # 返回 BrowserType 的实例
    browser = chromium.launch()  # 启动
    page = browser.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)  # 通过上下文管理器创建了Playwright实例
```
- `Playwright.实例方法`
	- `playwright.stop()` -> NoneType
		- 终止此 Playwright 实例, 上下文管理器结束时自动终止
- `Playwright.实例属性`
	- `playwright.chromium` -> [[class BrowserType|BrowserType]] 
		- 此对象可用于启动或连接 Chromium
	- `playwright.firefox` -> [[class BrowserType|BrowserType]] 
		- 此对象可用于启动或连接到 Firefox
	- `playwright.webkit` -> [[class BrowserType|BrowserType]] 
		- 此对象可用于启动或连接到 WebKit
	- `playwright.request` -> [[class APIRequest|APIRequest]] 
		- 公开可用于 Web API 测试的 API
	- `playwright.selectors` -> [[class Selectors|Selectors]] 
		- 选择器
	- `playwright.devices` -> Dict
		- 返回与 [[Browser.new_context()]] 或 [[Browser.new_page()]] 一起使用的设备字典。
