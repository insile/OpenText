##### requests.百度搜索
```python
import requests

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1',
    'Connection': 'keep-alive'
}

# 定义URL参数
params = {
    'wd': 'python'  # 搜索关键词为python
}

# 使用代理（如果需要的话）
# proxies = {
#     'http': 'http://your_proxy_address',
#     'https': 'https://your_proxy_address'
# }

# 定义表单数据（如果需要的话，例如登录时）
# data = {
#     'username': 'your_username',
#     'password': 'your_password'
# }

# 发送GET请求
response = requests.get("https://www.baidu.com/s", headers=headers, params=params)

# 如果使用代理，可以传入 proxies 参数
# response = requests.get("https://www.baidu.com/s", headers=headers, params=params, proxies=proxies)

# 如果有表单数据，可以传入 data 参数
# response = requests.post("https://www.baidu.com/s", headers=headers, params=params, proxies=proxies, data=data)

# 编码
response.encoding = response.apparent_encoding

# 输出响应内容
print(response.text)


```

