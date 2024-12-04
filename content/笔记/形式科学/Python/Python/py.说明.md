##### Python 说明
- Python 说明
	- Python 是一种高级, 通用, [[py.动态类型|动态类型]], 具有[[py.垃圾回收|垃圾回收]]的, [[py.面向对象程序设计|面向对象]]的[[py.解释型编程语言|解释型]]编程语言, 语法设计简洁明了, 易于学习和阅读, 适用于多种领域. 通过[[py.解释器|解释器]]执行, 目前[[py.版本|主版本]]为 Python 3. 每一个包含 Python 代码的文件后缀通常是 `.py`, 也称为[[py.模块|模块]], 多个模块目录组织起来可称为[[py.包|包]], 这些可以统称为[[py.库|库]]. 在实际应用中可对不同的项目使用不同的[[py.虚拟环境|虚拟环境]]. [[py.工作目录|工作目录]]是代码运行时路径的参考基准
- Python 官方与文档
	- Python 由 Python 软件基金会维护, 包括 CPython, Python 包索引, Python 文档 以及 Python 社区依赖的许多其他服务, 例如制作并赞助了 PyCon US 大会, 这是 Python 社区最大的年度聚会
		- https://www.python.org/
		- https://docs.python.org/3/
- Python PEP 
	- PEP 代表 Python Enhancement Proposal 即 Python 增强提案, PEP 是一个设计文档, 为 Python 社区提供信息, 或者描述 Python 或其流程或环境的新功能. PEP 应提供该功能的简明技术规范以及该功能的基本原理. 例如[PEP 8 – Python 代码风格指南](https://peps.python.org/pep-0008/)值得仔细阅读

```python
# 定义一个函数并执行
def add_numbers(a, b):
    """
    这个函数接受两个参数并返回它们的和。
    """
    return a + b
    
# 调用函数获得结果赋值给 result
result = add_numbers(3, 5)  

# 打印字符串 "结果:" 和变量 result，用空格连接
print("结果:", result)  
```


