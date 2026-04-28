##### async_playwright()
- `async_playwright()`
	- 一个创建异步 class Playwright 上下文管理器对象的顶层API
	- 开始时返回异步 class Playwright 实例
	- 结束时终止此异步 class Playwright 实例
```python
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```
