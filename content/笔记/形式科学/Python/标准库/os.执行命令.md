##### os.执行命令
```python
import os
# 执行一个简单的命令
exit_code = os.system("chcp 65001")
exit_code = os.system("dir")
# 检查命令的执行结果
if exit_code == 0:
    print("Command executed successfully.")
else:
    print("Command failed with exit code:", exit_code)

# popen 运行
po = os.popen("dir")
msg = po.buffer.read().decode('utf-8')

```
##### Command Prompt
- Command Prompt 是 Windows 中的传统命令行工具，功能相对较简单。
- 使用的是类DOS命令，命令格式相似，适用于执行基本的文件和系统操作。
```cmd
CD             显示当前目录的名称或将其更改。
CHCP           窗口的编码, 默认代码为 936 简体中文 GBK，65001 为 UTF-8
DEL            删除至少一个文件。
DIR            显示一个目录中的文件和子目录。
HELP           提供 Windows 命令的帮助信息。
MD             创建一个目录。
MKDIR          创建一个目录。
MOVE           将一个或多个文件从一个目录移动到另一个
               目录。
RD             删除目录。
RMDIR          删除目录。
TIME           显示或设置系统时间。

ipconfig       显示和管理计算机的网络配置信息 ipconfig /？
ping           网络诊断工具 ping /?
```