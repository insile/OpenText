##### requests.Session 实例属性
```python
Session.auth = None
	# 要附加到请求的默认身份验证元组或对象。
	
Session.cert = None
	# 用于设置SSL客户端证书，可以是证书文件路径字符串或('cert', 'key')元组
	
Session.cookies = cookiejar_from_dict({})
	# 这个属性是一个CookieJar对象，用于管理cookies。会话中的所有请求都会自动处理和维护这个CookieJar。
	
Session.headers = default_headers()
	# 一个字典，用于设置默认的请求头。可以通过直接操作这个字典来添加、修改或删除请求头，将在本会话发送的每个请求上发送。
	
Session.hooks = default_hooks()
	# 一个字典，包含多个键（表示不同的生命周期阶段）的回调函数

Session.max_redirects = DEFAULT_REDIRECT_LIMIT
	# 允许的最大重定向数。如果请求超过此限制，则会引发 TooManyRedirects 异常，默认值是 requests.models.DEFAULT_REDIRECT_LIMIT, 为30

Session.params = {}
	# 要附加到 URL 的 URL 参数字典
	
Session.proxies = {}
	# 这个属性用于设置默认的代理信息，允许您在会话中使用代理来进行HTTP请求。如 {'http': 'foo.bar:3128', 'http://host.name': 'foo.bar:4012'}

Session.stream = False
	# 如果为 False，则会立即下载响应内容。

Session.trust_env = True
	# 代理配置的信任环境设置

Session.verify = True
	# SSL 验证
```