##### 导入系统
- 导入系统
	- 导入系统指导入[[py.库|库]]扩充 Python 程序功能, 主要使用[[py.import|import]], [[py.from|from]], [[py.as|as]]
		- 查找模块或包
			- 首先, Python 解释器会在内置模块, 已安装的第三方模块和当前工作目录下查找要导入的模块或包
		- 创建命名空间
			- 一旦找到要导入的模块或包文件, Python 解释器会为该模块或包创建一个新的命名空间, 用于存储模块中的变量, 函数, 类等成员
		- 执行模块代码
			- 接下来, Python 解释器会执行模块文件中的代码
			- 导入模块不会运行 `if __name__ == '__main__':` 后的语句
			- 导入包自动执行 `__init__.py` 初始化
		- 创建模块对象
			- 导入模块或包后, Python 解释器会在内存中创建一个[[py.模块类型|模块对象]], 该对象包含了导入模块的命名空间和相关信息. 导入实际上是在创建一个模块对象, 并将其绑定到一个名称, 以便在其他地方使用
		- 绑定到名称
			- 一旦模块对象创建成功, Python 解释器会将模块对象绑定到导入时指定的名称。这个名称可以是模块的原始名称，也可以是使用 as 关键字重命名后的名称。
		- 使用模块或包
			- 导入成功后, 我们就可以使用导入时指定的名称来访问模块或包中定义的变量, 函数, 类等成员, 我们可以通过名称和点号 `.` 来访问模块中的成员
```python
# 标准导入
''' 
import 模块/包 [as 别名]
from 模块/包 import 对象 [as 别名]
'''
import pandas 
from pathlib import Path


# 相对导入
''' 
from 模块/包 import 对象 [as 别名]
'''
# 考虑以下目录结构
# package/
#    __init__.py
#    subpackage1/
#        __init__.py
#        moduleX.py
#        moduleY.py
#    subpackage2/
#        __init__.py
#        moduleZ.py
#    moduleA.py

# 以下导入都是有效，对subpackage1中moduleX.py和__init__.py
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```
