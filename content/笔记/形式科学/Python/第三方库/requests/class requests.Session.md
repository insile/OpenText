##### class requests.Session
- 请求会话。提供 Cookie 持久性、连接池和配置。
- [[Session.创建]]
- [[Session.属性]]
- [[Session.方法]]
##### 示例
```python
import requests

# 创建一个Session实例
session = requests.Session()

# 发送登录请求，并保持登录状态
login_data = {'username': 'your_username', 'password': 'your_password'}
login_response = session.post('https://www.example.com/login', data=login_data)
if login_response.status_code == 200:
    print("Login successful!")

# 在登录状态下，发送受保护页面的请求
protected_page_response = session.get('https://www.example.com/protected-page')
print(protected_page_response.text)

# 关闭Session
session.close()

```