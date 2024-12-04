##### class concurrent.futures.Future
- `submit` 返回的结果
- `Future.方法`
```python
Future.done()
# 如果调用已被取消或正常结束那么返回 True
Future.result(timeout=None)
# 返回调用所返回的值, 最多等待timeout秒, 默认无限
```
