##### from
- `from`
	- 用于[[py.库|引用库]]
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
#     subpackage1/
#         __init__.py
#         moduleX.py
#        moduleY.py
#     subpackage2/
#         __init__.py
#         moduleZ.py
#     moduleA.py

# 以下导入都是有效，对subpackage1中moduleX.py和__init__.py
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo

```