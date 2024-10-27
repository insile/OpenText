##### playwright.async_api
```python
from playwright.async_api import async_playwright, Playwright
import asyncio
```
- [[async_playwright()]]  顶层API
---
- 命名与同步相同
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
# 事件循环主协程
```
