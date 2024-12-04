##### IDLE
- IDLE
	- IDLE 是 Python 自带的集成开发环境 (Integrated Development Environment)，它提供了一个简单的图形用户界面, 用于编写, 运行和调试 Python 程序. IDLE运行代码方式有交互式和文件式. 直接打开就是交互式, 菜单栏新建文件或者打开模块后就是文件式. IDLE 位于 Python 安装目录可以直接点击打开或命令行调用
```shell
# Anaconda 没有添加环境变量，需要先激活环境
conda activate <env-name>

# 启动 Python IDLE 方式1
idle
# 启动 Python IDLE 方式2
python -m idlelib.idle
```

```python
print('Hello')
```