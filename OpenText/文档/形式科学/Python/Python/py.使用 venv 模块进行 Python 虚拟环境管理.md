##### venv 模块
- venv
	- venv 是 Python 标准库中用于创建和管理虚拟环境的模块. 虚拟环境允许你在项目之间隔离 Python 包的依赖关系, 以避免冲突和保持项目的独立性
- 步骤
	1. 在带有 Python 环境的终端运行 venv 模块创建管理虚拟环境
```shell
# 进入安装目录
cd <安装目录>

# 创建环境
python -m venv <名字>

# 进入bin目录
cd bin

# 激活环境
activate.bat

# 在该环境安装包
pip install <包>

# 退出环境
deactivate
```
