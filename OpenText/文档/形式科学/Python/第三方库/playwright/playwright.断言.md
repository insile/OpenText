##### playwright.断言
- `expect()`
	- `expect(response)`
		- [[class APIResponseAssertions]] API响应断言
	- `expect(locator)`
		- [[class LocatorAssertions]] 定位器断言
	- `expect(page)`
		- [[class PageAssertions]] 页面断言
```python
from playwright.sync_api import expect


locator = page.locator('.my-element')
expect(locator).to_be_visible()  # 期望可见
```
