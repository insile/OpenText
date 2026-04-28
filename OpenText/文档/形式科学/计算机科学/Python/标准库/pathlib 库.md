##### pathlib 库
- `pathlib` 用于处理文件路径和目录路径的对象导向的方式。它提供了一个更面向对象的 API，使得对文件系统路径进行操作更加简单和直观。`pathlib` 模块的核心类是 `Path` 类。
- [[pathlib.绝对路径和相对路径]]
- [[pathlib.遍历目录]]
```python
from pathlib import Path
```
##### pathlib 主要API
- [[pathlib.纯路径类]]
- [[pathlib.具体路径类]]
```python
# 继承关系
PurePath()  # 纯路径抽象基类，根据系统风格实例化路径，返回 PurePosixPath 或 PureWindowsPath
	PurePosixPath(PurePath)  # 纯路径类
	PureWindowsPath(PurePath)  # 纯路径类
Path(PurePath)  # 具体路径抽象基类，根据系统风格实例化路径，返回 PosixPath 或 WindowsPath
	PosixPath(Path, PurePosixPath)  # 具体路径
	WindowsPath(Path, PureWindowsPath)  # 具体路径

# 纯路径，提供纯计算操作没有 I/O ，无论运行什么系统，都可以实例化这些类，因为操作不做任何系统调用
# 具体路径，从纯路径继承而来提供 I/O 操作，你只能实例化与当前系统风格相同的类
# POSIX 风格的路径（Unix 和 Linux 系统）
# Windows 风格的路径（Windows）
# 类路径参数都接受该库中的类
```
