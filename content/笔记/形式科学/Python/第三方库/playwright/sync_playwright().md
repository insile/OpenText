##### sync_playwright()
- `sync_playwright()`
	- 一个创建 [[class Playwright]] 上下文管理器对象的顶层API
	- 开始时返回 [[class Playwright]] 实例
	- 结束时终止此 [[class Playwright]] 实例
```python
from playwright.sync_api import sync_playwright

# sync_playwright() 创建了一个上下文管理器
with sync_playwright() as playwright  

	# 开始返回了 Playwright 实例
	
	playwright.chromium.launch()
	
	# 结束终止此 Playwright 实例
```
