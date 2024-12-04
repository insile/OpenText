##### sys.获取命令行参数
- 在脚本中使用 `sys.argv` 获取终端传递的参数，类似 `input()` 
- 终端调用脚本语句 `python [脚本路径] [参数1,参数2,...]`
- 参数以字符串形式保存在列表
- `sys.argv` 的第一个元素是脚本名，其余的元素则是传递给脚本的参数
```python
# 这是一个简单的脚本实例，可保存在py文件通过终端调用传递任意参数
import sys

# 获取脚本名
script_name = sys.argv[0]

# 获取传递给脚本的参数
arguments = sys.argv[1:]

print("Script Name:", script_name)
print("Arguments:", arguments)
```

