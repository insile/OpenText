##### requests 函数
- [[requests.request()]]
```python
requests.head(url, **kwargs)
	# 获取HTML网页头信息的方法，对应于HTTP的HEAD	
requests.get(url, params=None, **kwargs)
	# 获取HTML网页的主要方法，对应于HTTP的GET
requests.post(url, data=None, json=None, **kwargs)
	# 向HTML网页提交POST请求的方法，对应于HTTP的POST
requests.put(url, data=None, **kwargs)
	# 向HTML网页提交PUT请求的方法，对应于HTTP的PUT
requests.patch(url, data=None, **kwargs)
	# 向HTML网页提交局部修改请求，对应于HTTP的PATCH
requests.delete(url, **kwargs)
	# 向HTML页面提交删除请求，对应于HTTP的DELETE
```

