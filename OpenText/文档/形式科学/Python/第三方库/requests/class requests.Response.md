##### class requests.Response
- 响应对象，其中包含服务器对HTTP请求的响应。请求的返回值
- Response.实例属性
```python
Response.status_code 
	# HTTP响应状态, 200正常，其他不正常
Response.headers 
	# 返回字典，响应头信息
Response.url 
	# 响应的最终URL位置

Response.content
	# HTTP响应内容的二进制形式（以字节为单位）
Response.text
	# 以unicode表示的响应内容
	# 如果没有 Response.encoding, 会使用 chardet 解码
Response.raw 
	# 原始响应内容

Response.encoding 
	# 访问Response.text时的编码，来自header，不准确
Response.apparent_encoding
	# 响应内容表面编码方式，由 chardet 库提供
Response.cookies 
	# 服务器返回的CookieJar Cookies
```
- Response.实例方法
```python
Response.raise_for_status()
	# 主动捕获异常
Response.json(**kwargs)
	# 返回响应的JSON编码内容（如果有）
```
##### 示例
```python
import requests

# 发送GET请求并获取响应
response = requests.get('https://www.example.com')

# 获取状态码
status_code = response.status_code
print(f"Status Code: {status_code}")

# 获取响应头部信息
headers = response.headers
print("Response Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")

# 获取响应内容
content = response.text
print("Response Content:")
print(content)

# 检查响应内容是否是HTML
if 'html' in response.headers.get('content-type', '').lower():
    print("Response contains HTML content")

# 关闭响应
response.close()

```