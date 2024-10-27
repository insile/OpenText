##### requests.Session 实例方法
```python
Session.close()
	# 关闭所有适配器，从而关闭会话

Session.request(method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)
	# 使用会话对象发送自定义HTTP方法的请求

Session.get(url, **kwargs)
	# 使用会话对象发送GET请求

Session.post(url, data=None, json=None, **kwargs)
	# 使用会话对象发送POST请求

Session.put(url, data=None, **kwargs)
	# 使用会话对象发送PUT请求

Session.delete(url, **kwargs)
	# 使用会话对象发送DELETE请求

Session.patch(url, data=None, **kwargs)
	# 使用会话对象发送PATCH请求
	
Session.head(url, **kwargs)
	# 使用会话对象发送HEAD请求

Session.options(url, **kwargs)
	# 使用会话对象发送OPTIONS请求

Session.get_adapter(url)
	# 返回给定 URL 的适当连接适配器。 
	# 返回 requests.adapters.BaseAdapter
	
Session.get_redirect_target(resp)
	# 接收一个响应。返回一个重定向 URI 或无

Session.merge_environment_settings(url, proxies, stream, verify, cert)
	# 检查环境并将其与一些设置合并。
	# 返回 dict

Session.mount(prefix, adapter)
	# 将连接适配器注册到前缀
	# 适配器按照前缀长度降序排序。

Session.prepare_request(request)
	# 构造用于传输的 requests.PreparedRequest 并返回

Session.rebuild_auth(prepared_request, response)
	# 当被重定向时，我们可能希望从请求中删除身份验证，以避免泄漏凭据。此方法在可能的情况下智能地删除和重新应用身份验证，以避免凭据丢失。

Session.rebuild_method(prepared_request, response)
	# 当被重定向时，我们可能希望根据某些规范或浏览器行为更改请求的方法。


Session.rebuild_proxies(prepared_request, proxies)
	# 此方法通过考虑环境变量重新评估代理配置


Session.resolve_redirects(resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)
	# 接收响应。返回响应或请求的生成器


Session.send(request, **kwargs)
	# 发送给定的准备请求 PreparedRequest

```