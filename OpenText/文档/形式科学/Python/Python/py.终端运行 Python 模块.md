##### 终端运行 Python 模块
- 在带有 Python 环境的终端直接运行一个 Python 模块
```shell
# Anaconda 没有添加环境变量，需要先激活环境
conda activate <env-name>

# 运行 myscript.py 模块并传参
python myscript.py <arg1>

# 在 sys.path 系统路径中搜索指定模块，并以 __main__ 执行其内容
python -m myscript <arg1>
```

