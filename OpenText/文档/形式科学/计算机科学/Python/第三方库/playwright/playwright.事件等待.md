##### playwright.事件等待
- 事件等待函数
	- [[Page.实例方法]]
```python
with page.expect_request("**/*logo*.png") as first:
  page.goto("https://wikipedia.org")
print(first.value.url)
# 等待具有指定 url 的请求

with page.expect_popup() as popup:
  page.get_by_text("open the popup").click()
popup.value.goto("https://wikipedia.org")
# 等待弹出窗口
```
- 事件监听器
	- [[Browser.事件]]
	- [[BrowserContext.事件]]
	- [[Page.事件]]
	- [[WebSocket.事件]]
	- [[Worker.事件]]
```python
def print_request_sent(request):
	# 请求处理函数
	print("Request sent: " + request.url)

def print_request_finished(request):
	# 请求完成处理函数
	print("Request finished: " + request.url)

page.on("request", print_request_sent)  # 监听
page.on("requestfinished", print_request_finished)  # 监听
page.goto("https://wikipedia.org")

page.remove_listener("requestfinished", print_request_finished)  # 移除监听
page.goto("https://www.openstreetmap.org/")
```
