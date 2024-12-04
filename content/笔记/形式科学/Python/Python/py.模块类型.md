##### 模块类型
- 模块类型 `<class 'module'>`
	- 模块唯一的特殊操作是属性访问, 模块对象具有内置特殊属性
```python
# math 模块
import math
print(type(math))  # <class 'module'>
print(type(math.pi))  # 3.141592653589793
print(type(math.__name__))  # 'math'

# 模块预先定义的可写属性
module.__name__
# 模块的名称。
# 当一个 Python 脚本被直接执行时，解释器会将该脚本的特殊变量 __name__ 设置为 '__main__'
# 如果脚本被导入为模块，那么 __name__ 将是模块的名字
# if __name__ == '__main__' 用于判断一个 Python 脚本是否被直接执行，还是被作为模块导入到其他脚本中

module.__doc__
# 模块的文档字符串，如果不可用则为 None。

module.__file__
# 被加载模块所对应文件的路径名称，如果它是从文件加载的话。 对于某些类型的模块来说 __file__ 属性可能是缺失的，例如被静态链接到解释器中的 C 模块。 对于从共享库动态加载的扩展模块来说，它将是共享库文件的路径名称。

module.__annotations__
# 包含在模块体执行期间收集的 变量标注 的字典。 有关使用 __annotations__ 的最佳实践，请参阅 对象注解属性的最佳实践。
```
