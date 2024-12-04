##### playwright.sync_api
```python
from playwright.sync_api import sync_playwright, Playwright
```
- [[sync_playwright()]]  顶层API
---
- [[class Playwright]]  任务启动器
	- [[class BrowserType]]  用于启动特定类型浏览器的工厂类
		- [[class Browser]]  表示一个浏览器实例，可以用来控制和操作浏览器
			- [[class BrowserContext]] 浏览器上下文对象，表示浏览器中的一个独立会话
				- [[class Page]] 浏览器页面
					- [[class Request]] 页面请求
					- [[class Response]] 页面响应
					- [[class Mouse]]  鼠标
					- [[class Keyboard]]  键盘
					- [[class Locator]]  定位器
					- [[class Dialog]] 页面对话框
					- [[class Download]] 页面下载
					- [[class ElementHandle]] 页内 DOM 元素
					- [[class FileChooser]] 页面文件选择器
					- [[class Frame]] 页面框架
						- [[class FrameLocator]] 框架定位器
					- [[class WebSocket]] 页面 WebSocket 连接
					- [[class Worker]] 页面 WebWorker
					- [[class JSHandle]] 页面 JavaScript 对象
					- [[class Touchscreen]] 触摸屏
				- [[class Route]] 路由
			- [[class CDPSession]]  CDP 会话对象，用于与浏览器通信
			- [[class ConsoleMessage]] 代表浏览器中的控制台消息
			- [[class Tracing]] 操作追踪
			- [[class Video]] 录制视频
	- [[class APIRequest]]  用于发出 API 请求的对象
		- [[class APIRequestContext]] API 请求的上下文对象
		- [[class APIResponse]] API 请求的响应对象
	- [[class Selectors]] 自定义选择器引擎
- [[class Error]] 异常对象
	- [[class TimeoutError]] 超时异常
	- [[class WebError]] 网络异常
- [[playwright.断言|Assertions]] 断言
	- [[class APIResponseAssertions]] API响应断言
	- [[class LocatorAssertions]] 定位器断言
	- [[class PageAssertions]] 页面断言


