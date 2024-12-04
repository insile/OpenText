##### playwright.百度搜索
```python
def baidu_search(query):
    # 创建 Playwright 实例
    with sync_playwright() as p:
        # 在 Chromium 浏览器中创建一个上下文
        browser = p.chromium.launch(headless=False)  # 有头
        context = browser.new_context()

        # 创建一个新页面并导航到百度搜索页面
        page = context.new_page()
        page.goto('https://www.baidu.com')

        # 在搜索框中输入查询关键字并提交搜索
        page.fill('input[name="wd"]', query)
        page.press('input[name="wd"]', 'Enter')

        # 页面使用xpath定位器, 定位每一条搜索结果
        loc = page.locator("//div/h3")
		# 等待最后一个结果出现才继续运行
		loc.last.wait_for()
        # 搜索结果列表
        a = loc.all()
        # 遍历列表
        for li in a:
            print(''.join(li.all_inner_texts()))  # 搜索结果文本
            print(li)  # 定位器对象


# 执行百度搜索
baidu_search("Python")



# python-Python电脑版下载-一键安装-下载中心
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=0'>
# python菜鸟教程-零基础入门
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=1'>
# Welcome to Python.org官方
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=2'>
# python - 百度翻译
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=3'>
# [官] python-中文网站
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=4'>
# 适合初中生的Python高阶人工智能编程课-高清视频在线观看
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=5'>
# Python - 百度百科
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=6'>
# 官python-中国中文网站
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=7'>
# Python - 视频大全 - 高清在线观看
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=8'>
# python - 相关博客 - 开发者搜索
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=9'>
# python_2024最新版_天天下载
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=10'>
# python是什么意思_python的翻译_音标_读音_用法_例句_爱...
# <Locator frame=<Frame name= url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0x9b8e470f006a0027&rsv_t=8a5aF2sB8mXKvVoePtKFai6yfv6%2B1VgMAzDGZR4lZgz5dmDEjkubd5J2HZXG&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=4&rsv_sug4=4'> selector='//div/h3 >> nth=11'>

```