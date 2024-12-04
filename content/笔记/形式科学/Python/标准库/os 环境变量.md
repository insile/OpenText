##### os 环境变量
```python
os.environ  # 返回一个映射对象
os.environ[key]="value"  # 临时设置环境变量
os.environ.keys()  # 获取环境变量键
os.environ.get(key)  # 获取环境变量值方法1
os.getenv(key, str)  # 获取环境变量值方法2(推荐使用这个方法)
del os.environ[key]  # 删除环境变量

# 设置常见环境变量
os.environ['http_proxy']  # 代理url(如127.0.0.1:8888）
os.environ['HOMEPATH']  # 当前用户主目录
os.environ['TEMP']  # 临时目录路径
os.environ['PATHEXT']  # 可执行文件
os.environ['SYSTEMROOT']  # 系统主目录
os.environ['LOGONSERVER']  # 机器名
os.environ['PROMPT']  # 设置提示符
```