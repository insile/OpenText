##### sys 库
- 提供了对 Python 解释器的访问以及与解释器交互的功能
- [[sys.获取命令行参数]]
```python
import sys
```
##### sys 主要API
```python
sys.argv  # 一个列表，其中包含了被传递给 Python 脚本的命令行参数
sys.platform  # 当前运行 Python 的平台标识符
sys.version  # Python 解释器的版本信息
sys.exit([arg])  # 退出 Python 解释器，可指定退出状态码 0为成功终止，其他为异常终止

sys.path  #  用于指定导入模块的搜索路径
sys.modules  # 一个字典，包含当前已导入的所有模块

sys.getsizeof(object)  # 返回对象的内存占用大小
sys.getrefcount(object)  # 返回对象的引用计数
sys.getdefaultencoding()  # 返回默认字符串编码。
```