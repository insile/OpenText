##### requests 异常
```python
exception requests.ConnectionError(*args, **kwargs)
	# 发生连接错误

exception requests.HTTPError(*args, **kwargs)
	# HTTP错误异常

exception requests.URLRequired(*args, **kwargs)
	# URL缺失异常

exception requests.TooManyRedirects(*args, **kwargs)
	# 超过最大重定向次数，产生重定向异常

exception requests.ConnectTimeout(*args, **kwargs)
	# 连接远程服务器超时异常

exception requests.Timeout(*args, **kwargs)
	# 请求URL超时，产生超时异常
```
##### 示例
```python
import requests

try:
    response = requests.get('https://www.baidu.com', timeout=5)  # 设置超时时间为5秒
    print(response.raise_for_status())
except requests.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print("HTTPError:", e)
except requests.exceptions.RequestException as e:
    print("RequestException:", e)
```
